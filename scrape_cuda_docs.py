#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "beautifulsoup4",
#   "html2text",
#   "requests",
# ]
# ///
"""
Unified CUDA documentation scraper.

Scrapes NVIDIA CUDA documentation (PTX ISA, Runtime API, Driver API)
and converts to searchable markdown format.
"""

import argparse
import json
import os
import re
from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

import html2text
import requests
from bs4 import BeautifulSoup, Tag


class DocumentationScraper:
    """Base class for CUDA documentation scrapers."""

    def __init__(
        self,
        base_url: str,
        output_dir: Path,
        cache_dir: Path | None = None,
        skip_download: bool = False,
        force: bool = False,
    ):
        self.base_url = base_url
        self.output_dir = output_dir
        self.cache_dir = cache_dir or (output_dir.parent / f"{output_dir.name}-raw")
        self.skip_download = skip_download
        self.force = force

        # HTTP session with headers
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            }
        )

        # html2text configuration
        self.h2t = html2text.HTML2Text()
        self.h2t.body_width = 0
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.ignore_emphasis = False
        self.h2t.skip_internal_links = False
        self.h2t.unicode_snob = True
        self.h2t.decode_errors = "ignore"

    def fetch_page(self, url: str) -> BeautifulSoup | None:
        """Fetch and parse a webpage."""
        try:
            print(f"Fetching: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return BeautifulSoup(response.content, "html.parser")
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def sanitize_filename(self, name: str, section_num: str = "") -> str:
        """Convert title to safe filename."""
        # Remove section number from title if present
        name = re.sub(r"^\d+(\.\d+)*\.?\s*", "", name)
        name = re.sub(r"#.*$", "", name)  # Remove anchors
        name = re.sub(r"\.html?$", "", name)  # Remove extensions
        name = re.sub(r"[^\w\s\-_.]", "", name)  # Remove special chars
        name = re.sub(r"\s+", "-", name)  # Spaces to hyphens
        name = name.lower().strip("-")

        # Add section number prefix if provided
        if section_num:
            name = f"{section_num}-{name}"

        return name if name else "index"

    def extract_main_content(self, soup: BeautifulSoup) -> BeautifulSoup:
        """Extract main documentation content from page."""
        content = soup.find("div", class_="contents")
        if not content:
            content = soup.find("div", id="doc-content") or soup.find("body")
        if not content:
            raise ValueError("Could not find main content")

        # Remove navigation elements
        for nav in content.find_all(
            ["div", "ul"],
            class_=["header", "headertitle", "navigate", "breadcrumb"],
        ):
            nav.decompose()

        for elem in content.find_all(
            ["div"],
            id=["top", "titlearea", "projectlogo", "projectname", "projectbrief"],
        ):
            elem.decompose()

        # Remove large navigation lists
        for textblock in content.find_all("div", class_="textblock"):
            links = textblock.find_all("a", href=True)
            if len(links) > 10:
                html_links = [
                    link for link in links if link.get("href", "").endswith(".html")
                ]
                if len(html_links) > 10:
                    textblock.decompose()

        return content

    def convert_to_markdown(self, soup: BeautifulSoup, page_url: str) -> str:
        """Convert HTML to markdown."""
        content = self.extract_main_content(soup)

        # Make image URLs absolute
        for img in content.find_all("img"):
            src = img.get("src")
            if src and not src.startswith(("http://", "https://")):
                img["src"] = urljoin(page_url, src)

        # Make link URLs absolute
        for link in content.find_all("a"):
            href = link.get("href")
            if href and not href.startswith(("http://", "https://", "#", "mailto:")):
                link["href"] = urljoin(page_url, href)

        markdown = self.h2t.handle(str(content))
        markdown = self._clean_navigation_markdown(markdown)
        markdown = re.sub(r"\n{4,}", "\n\n\n", markdown)
        return markdown.strip()

    def _clean_navigation_markdown(self, markdown: str) -> str:
        """Remove navigation cruft from markdown."""
        lines = markdown.split("\n")
        cleaned_lines = []
        in_nav = False
        found_header = False

        for line in lines:
            if (
                "NVIDIA" in line
                and "Toolkit Documentation" in line
                and not found_header
            ):
                in_nav = True
                continue

            if line.startswith("###") or (
                line.startswith("##") and "Public Members" in line
            ):
                in_nav = False
                found_header = True

            if not in_nav:
                cleaned_lines.append(line)

        return "\n".join(cleaned_lines)


class APIScraper(DocumentationScraper):
    """Scrape the versioned Sphinx Runtime/Driver manuals introduced in 13.4."""

    def __init__(
        self, api_type: str, output_dir: Path, skip_download: bool = False,
        force: bool = False, expected_version: str = "13.4",
    ):
        self.api_type = api_type
        self.expected_version = expected_version
        super().__init__(
            f"https://docs.nvidia.com/cuda/cuda-{api_type}-api/", output_dir,
            skip_download=skip_download, force=force,
        )
        self.api_url = urljoin(self.base_url, f"cuda_{api_type}_api/")

    def _validate_source(self, soup: BeautifulSoup) -> Tag:
        title = soup.title.get_text() if soup.title else ""
        expected = f"CUDA {self.api_type.title()} API Reference Manual {self.expected_version} documentation"
        if expected not in title:
            raise ValueError(f"Expected {expected!r}, found {title!r}")
        content = soup.find(attrs={"itemprop": "articleBody"})
        if content is None or content.find("h1") is None:
            raise ValueError("Could not find CUDA API article body")
        return content

    def _load_source(self, url: str) -> BeautifulSoup:
        relative = url.removeprefix(self.base_url)
        if relative == url or ".." in Path(relative).parts:
            raise ValueError(f"Source URL outside this manual: {url}")
        cache = self.cache_dir / relative
        if cache.exists() and (self.skip_download or not self.force):
            soup = BeautifulSoup(cache.read_bytes(), "html.parser")
        elif self.skip_download:
            raise FileNotFoundError(f"Missing cached source: {cache}")
        else:
            soup = self.fetch_page(url)
            if soup is None:
                raise RuntimeError(f"Failed to fetch {url}")
            self._validate_source(soup)
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(str(soup), encoding="utf-8")
        self._validate_source(soup)
        return soup

    def discover_pages(self) -> list[dict[str, str]]:
        """Discover modules, structs/unions, and introductory/reference chapters."""
        pages = {}
        for listing, directory, pattern in (
            (urljoin(self.api_url, "apis.html"), "modules", r"group__.*\.html"),
            (urljoin(self.api_url, "structs.html"), "data-structures", r"(?:struct|union).*\.html"),
            (urljoin(self.base_url, "index.html"), "overview", r".*\.html"),
        ):
            content = self._validate_source(self._load_source(listing))
            discovered = 0
            for link in content.find_all("a", href=True):
                url = urljoin(listing, link["href"]).split("#")[0]
                filename = Path(urlsplit(url).path).name
                if url == listing or not re.fullmatch(pattern, filename) or not url.startswith(self.base_url):
                    continue
                if directory == "overview" and filename in ("index.html", "apis.html", "structs.html"):
                    continue
                if url in pages:
                    continue
                discovered += 1
                pages[url] = dict(url=url, title=link.get_text(" ", strip=True),
                                  path=f"{directory}/{self.sanitize_filename(filename)}.md")
            if not discovered:
                raise ValueError(f"No {directory} pages found in {listing}")
        paths = [page["path"] for page in pages.values()]
        if len(paths) != len(set(paths)):
            raise ValueError("CUDA API output filename collision")
        return list(pages.values())

    def convert_api_page(self, soup: BeautifulSoup, url: str) -> str:
        content = deepcopy(self._validate_source(soup))
        for element in content.select(".headerlink"):
            element.decompose()
        # Summary lists repeat the detailed definitions. Remove them only when
        # every linked target actually has a detailed definition on this page.
        for summary in content.select(".dl-as-table"):
            targets = [a["href"][1:] for a in summary.select('a[href^="#"]')]
            if targets and all(content.find(id=target) for target in targets):
                rubric = summary.find_previous_sibling("p", class_="rubric")
                if rubric:
                    rubric.decompose()
                summary.decompose()
        for paragraph in content.find_all("p"):
            if paragraph.get_text(strip=True) == "impl_private":
                paragraph.decompose()
        for link in content.find_all("a", href=True):
            # Keep external references, but avoid long mangled API symbol URLs.
            if "reference internal" in " ".join(link.get("class", [])):
                link.unwrap()
            else:
                link["href"] = urljoin(url, link["href"])
        for img in content.find_all("img", src=True):
            img["src"] = urljoin(url, img["src"])
        # Protect signatures as inline code and examples as fenced code.
        preserved = {}
        for element in list(content.select("dt.sig, pre")):
            value = element.get_text().strip()
            if element.name == "pre":
                value = re.sub(r"[ \t]+$", "", value, flags=re.MULTILINE)
                fence = "`" * max(3, max((len(m.group()) + 1 for m in re.finditer(r"`+", value)), default=3))
                value = f"{fence}cpp\n{value}\n{fence}"
            else:
                value = "`` " + value.replace("\n", " ") + " ``"
            key = f"CUDAAPIPRESERVED{len(preserved):06d}TOKEN"
            preserved[key] = value
            replacement = BeautifulSoup(f"<p>{key}</p>", "html.parser").p
            element.replace_with(replacement)
        markdown = "\n".join(line.rstrip() for line in self.h2t.handle(str(content)).splitlines())
        markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()
        for key, value in preserved.items():
            markdown = markdown.replace(key, value)
        # Preserve all semantic notes, return values, parameters, and See also.
        return (f"<!-- CUDA {self.api_type.title()} API {self.expected_version} -->\n"
                f"Source: {url}\n\n{markdown}\n")

    def run(self) -> None:
        pages = self.discover_pages()
        print(f"Discovered {len(pages)} CUDA {self.api_type.title()} API {self.expected_version} pages")
        # Fetch independently; conversion stays sequential because HTML2Text has
        # mutable parser state. No output files change if any download fails.
        with ThreadPoolExecutor(max_workers=6) as pool:
            list(pool.map(lambda page: self._load_source(page["url"]), pages))
        files = {}
        for page in pages:
            soup = BeautifulSoup((self.cache_dir / page["url"].removeprefix(self.base_url)).read_bytes(), "html.parser")
            files[Path(page["path"])] = self.convert_api_page(soup, page["url"])
        index = [f"# CUDA {self.api_type.title()} API {self.expected_version} Documentation Index", "",
                 f"Source: {self.base_url}index.html", ""]
        for directory, title in (("overview", "Overview"), ("modules", "Modules"), ("data-structures", "Data Structures")):
            group = [page for page in pages if page["path"].startswith(directory + "/")]
            index.extend([f"## {title} ({len(group)})", ""])
            index.extend(f"- [{page['title']}]({page['path']})" for page in group)
            index.append("")
        files[Path("INDEX.md")] = "\n".join(index)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        for path, markdown in files.items():
            destination = self.output_dir / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(markdown, encoding="utf-8")
        for old_file in self.output_dir.rglob("*.md"):
            if old_file.relative_to(self.output_dir) not in files:
                old_file.unlink()
        print(f"CUDA {self.api_type.title()} API {self.expected_version}: wrote {len(files)} Markdown files to {self.output_dir}")


class PTXScraper(DocumentationScraper):
    """Convert PTX's nested Sphinx sections without duplicating their contents."""

    def __init__(
        self, output_dir: Path, source_html: Path | None = None,
        expected_version: str = "9.4",
    ):
        super().__init__(
            "https://docs.nvidia.com/cuda/parallel-thread-execution/", output_dir,
        )
        self.source_html = source_html
        self.expected_version = expected_version

    def run(self) -> None:
        """Validate and render the whole source before replacing generated files."""
        if self.source_html:
            soup = BeautifulSoup(self.source_html.read_bytes(), "html.parser")
        else:
            soup = self.fetch_page(urljoin(self.base_url, "index.html"))
        if soup is None:
            raise RuntimeError("Failed to fetch PTX documentation")
        files = self.render(soup)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        for path, markdown in files.items():
            destination = self.output_dir / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(markdown, encoding="utf-8")
        # Section numbers and filenames can change between versions. Only remove
        # stale generated markdown after the complete replacement is rendered.
        for old_file in self.output_dir.rglob("*.md"):
            if old_file.relative_to(self.output_dir) not in files:
                old_file.unlink()
        for directory in sorted(self.output_dir.rglob("*"), reverse=True):
            if directory.is_dir() and not any(directory.iterdir()):
                directory.rmdir()
        print(f"PTX ISA {self.expected_version}: wrote {len(files)} Markdown files to {self.output_dir}")

    def render(self, soup: BeautifulSoup) -> dict[Path, str]:
        """Build section files, cross-references, and a complete chapter index."""
        content = soup.find(attrs={"itemprop": "articleBody"})
        if content is None:
            raise ValueError("Could not find PTX article body")
        version = re.search(r"PTX ISA (\d+\.\d+) documentation", soup.title.get_text() if soup.title else "")
        if version is None or version.group(1) != self.expected_version:
            actual = version.group(1) if version else "unknown"
            raise ValueError(f"Expected PTX ISA {self.expected_version}, found {actual}; output left unchanged")
        for unwanted in content.select(".headerlink, .viewcode-link, .navigation, .related"):
            unwanted.decompose()

        sections = []
        paths_by_id = {}
        chapter = None
        numbers = set()
        for heading in content.find_all(["h1", "h2", "h3", "h4"]):
            number = heading.find(class_="section-number")
            node = heading.parent
            if number is None or node.name != "section" or not node.get("id"):
                raise ValueError("Unrecognized PTX section structure")
            section_num = number.get_text(strip=True).rstrip(". ")
            if section_num in numbers:
                raise ValueError(f"Duplicate section number: {section_num}")
            numbers.add(section_num)
            # Keep the existing filename convention, including inline-code titles.
            filename = self.sanitize_filename(heading.get_text(strip=True), section_num) + ".md"
            title = heading.get_text(" ", strip=True)
            level = int(heading.name[1])
            if level == 1:
                chapter = Path(self.sanitize_filename(heading.get_text(strip=True), section_num))
            if chapter is None:
                raise ValueError("PTX section appears before its chapter")
            path = chapter / filename
            paths_by_id[node["id"]] = path
            sections.append(dict(node=node, path=path, title=title, number=section_num, level=level))
        if not sections or not content.find(id=f"changes-in-ptx-isa-version-{self.expected_version.replace('.', '-')}"):
            raise ValueError("PTX source is incomplete: sections or current release notes missing")

        # Map all figure/table/deep-section IDs to the file owning that content.
        anchors = {}
        for element in content.find_all(id=True):
            owner = element
            while owner is not None and owner.get("id") not in paths_by_id:
                owner = owner.parent
            if owner is not None:
                anchors[element["id"]] = paths_by_id[owner["id"]]

        files = {}
        index = [f"# PTX ISA {self.expected_version} Documentation Index", "",
                 f"Source: {self.base_url}index.html", "",
                 f"{len(sections)} section files. Deeper subsections are included in their parent file.", ""]
        for section in sections:
            path = section["path"]
            if path in files:
                raise ValueError(f"Duplicate output path: {path}")
            node = deepcopy(section["node"])
            children = []
            for child in list(node.find_all("section")):
                if child.get("id") in paths_by_id:
                    # Skip descendants already detached along with their parent.
                    if child.find_parent("section") is node:
                        child_heading = child.find(["h1", "h2", "h3", "h4"])
                        children.append((child_heading.get_text(" ", strip=True), paths_by_id[child["id"]]))
                        child.extract()
            markdown = self._convert_section(node, path, anchors)
            if children:
                markdown += "\n\nSubsections:\n\n" + "\n".join(
                    f"- [{title}]({self._relative_path(target, path)})" for title, target in children
                )
            source_url = f"{self.base_url}index.html#{section['node']['id']}"
            metadata = (f"---\ntitle: {json.dumps(section['title'], ensure_ascii=False)}\n"
                        f"section: {json.dumps(section['number'])}\n"
                        f"version: {json.dumps(self.expected_version)}\nurl: {source_url}\n---\n\n")
            files[path] = metadata + markdown.strip() + "\n"
            index.append(f"{'  ' * (section['level'] - 1)}- [{section['title']}]({path.as_posix()})")
        files[Path("INDEX.md")] = "\n".join(index) + "\n"
        return files

    @staticmethod
    def _relative_path(target: Path, current: Path) -> str:
        return Path(os.path.relpath(target, current.parent)).as_posix()

    def _convert_section(self, node: Tag, path: Path, anchors: dict[str, Path]) -> str:
        """Preserve code and complex tables, and resolve source URLs locally."""
        for img in node.find_all("img", src=True):
            img["src"] = urljoin(self.base_url, img["src"])
        for link in node.find_all("a", href=True):
            absolute = urljoin(urljoin(self.base_url, "index.html"), link["href"])
            parsed = urlsplit(absolute)
            fragment = unquote(parsed.fragment)
            if parsed._replace(fragment="").geturl() in (self.base_url, self.base_url + "index.html") and fragment in anchors:
                target = anchors[fragment]
                prefix = "" if target == path else self._relative_path(target, path)
                link["href"] = f"{prefix}#{fragment}"
            else:
                link["href"] = absolute
        # Heading self-links add noise; the explicit IDs below retain navigation.
        for heading in node.find_all(re.compile(r"^h\d+$")):
            for link in heading.find_all("a"):
                link.unwrap()
            if int(heading.name[1:]) > 6:
                heading.name = "h6"

        # html2text drops IDs and damages merged table cells and some code blocks.
        # Protect these fragments with standalone placeholders during conversion.
        preserved = {}

        def protect(element: Tag, text: str) -> None:
            key = f"PTXPRESERVED{len(preserved):06d}TOKEN"
            preserved[key] = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
            placeholder = BeautifulSoup(f"<p>{key}</p>", "html.parser").p
            element.replace_with(placeholder)

        for element in list(node.find_all(id=True)):
            anchor = BeautifulSoup("<p></p>", "html.parser").p
            element.insert_before(anchor)
            protect(anchor, f'<a id="{element["id"]}"></a>')
        # The wrapper's ID is not returned by find_all().
        prefix = f'<a id="{node["id"]}"></a>\n\n'
        for pre in list(node.find_all("pre")):
            if pre.find_parent("table"):
                # Markdown fences inside an HTML table do not render as code.
                # Retain these examples as literal HTML preformatted blocks.
                pre.string = pre.get_text()
                continue
            code = pre.get_text().rstrip("\n")
            fence = "`" * max(3, max((len(m.group()) + 1 for m in re.finditer(r"`+", code)), default=3))
            protect(pre, f"{fence}ptx\n{code}\n{fence}")
        for table in list(node.find_all("table")):
            # HTML tables retain rowspan/colspan, multiline cells, and captions.
            # Simple rectangular tables remain Markdown for easy text searches.
            caption = table.find("caption")
            if caption:
                table.insert_before(caption.extract())
                caption.name = "p"
            if (table.select("[rowspan], [colspan], pre, ul, ol")
                    or len(table.select("thead tr")) > 1
                    or "|" in table.get_text()):
                # IDs have already been emitted above the table/cells.
                for element in [table, *table.find_all(True)]:
                    element.attrs = {k: v for k, v in element.attrs.items()
                                     if k in ("rowspan", "colspan", "href", "src", "alt")}
                # Expand placeholders for IDs inside the raw HTML table now.
                raw = str(table)
                # Keep the HTML block contiguous in Markdown. Encode newlines
                # inside preformatted cells so their blank lines still render.
                for pre in table.find_all("pre"):
                    raw = raw.replace(str(pre), str(pre).replace("\n", "&#10;"))
                raw = "\n".join(line for line in raw.splitlines() if line.strip())
                for key, value in preserved.items():
                    raw = raw.replace(f"<p>{key}</p>", value)
                protect(table, raw)
        markdown = "\n".join(line.rstrip() for line in self.h2t.handle(str(node)).splitlines())
        markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()
        for key, value in preserved.items():
            markdown = markdown.replace(key, value)
        return prefix + markdown


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Scrape CUDA documentation to markdown"
    )
    parser.add_argument(
        "api_type",
        choices=["ptx", "runtime", "driver"],
        help="API type to scrape",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory (default: cuda_skill/references/<api>-docs)",
    )
    parser.add_argument(
        "--skip-download",
        action="store_true",
        help="Skip download, use cached files (runtime/driver only)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-download even if cache exists",
    )

    parser.add_argument(
        "--source-html", type=Path,
        help="Read a saved official HTML page instead of downloading (PTX only)",
    )
    parser.add_argument(
        "--ptx-version", default="9.4",
        help="Required PTX source version (default: 9.4); reject unexpected releases",
    )
    parser.add_argument(
        "--cuda-version", default="13.4",
        help="Required Runtime/Driver source version (default: 13.4)",
    )
    args = parser.parse_args()
    if args.source_html and args.api_type != "ptx":
        parser.error("--source-html is supported only for PTX")

    # Set default output directory
    if not args.output_dir:
        api_name = "ptx" if args.api_type == "ptx" else f"cuda-{args.api_type}"
        args.output_dir = Path(f"cuda_skill/references/{api_name}-docs")

    # Create appropriate scraper
    scraper: PTXScraper | APIScraper
    if args.api_type == "ptx":
        scraper = PTXScraper(args.output_dir, args.source_html, args.ptx_version)
    else:
        scraper = APIScraper(
            args.api_type, args.output_dir, args.skip_download, args.force, args.cuda_version
        )

    scraper.run()


if __name__ == "__main__":
    main()
