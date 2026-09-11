"""Verify generated references against a saved PTX page and API HTML caches.

Run from the repository root with the scraper's dependencies installed:
    python tests/verify_source_coverage.py --ptx-html /path/to/ptx-index.html
"""
import argparse
from collections import Counter
from pathlib import Path
import re

from bs4 import BeautifulSoup


def normalize_code(text):
    return re.sub(r'[ \t]+$', '', text, flags=re.MULTILINE).strip('\n')


def check_links(root):
    files = {p.resolve(): p.read_text() for p in root.rglob('*.md')}
    for path, text in files.items():
        links = re.findall(r'\]\(([^)]+)\)', text)
        links.extend(a['href'] for a in BeautifulSoup(text, 'html.parser').find_all('a', href=True))
        for link in links:
            link = link.strip('<>')
            if re.match(r'[a-z]+:', link):
                continue
            filename, _, anchor = link.partition('#')
            target = (path.parent / filename).resolve() if filename else path
            assert target in files, (path, link)
            if anchor:
                assert f'<a id="{anchor}"' in files[target], (path, link)
    return files


def check_ptx(source, root):
    content = BeautifulSoup(source.read_bytes(), 'html.parser').find(attrs={'itemprop': 'articleBody'})
    files = check_links(root)
    combined = '\n'.join(files.values())
    ids = Counter(re.findall(r'<a id="([^"]+)"', combined))
    source_ids = {element['id'] for element in content.find_all(id=True)}
    assert source_ids == ids.keys(), source_ids - ids.keys()
    assert all(count == 1 for count in ids.values())
    raw_html = BeautifulSoup(combined, 'html.parser')
    raw_code = [normalize_code(pre.get_text()) for pre in raw_html.select('pre')]
    code = [normalize_code(pre.get_text()) for pre in content.select('pre')]
    for example in code:
        assert example in combined or example in raw_code, example[:100]
    image_count = len(re.findall(r'!\[', combined)) + len(raw_html.select('img'))
    assert image_count == len(content.select('img'))
    assert 'PTXPRESERVED' not in combined
    print(f'PTX: {len(files)} files, {len(ids)} anchors, {len(code)} code blocks, '
          f'{image_count} images; all local links valid')


def check_api(api, root):
    cache = root.with_name(root.name + '-raw')
    counts = Counter()
    check_links(root)
    for path in root.rglob('*.md'):
        if path.name == 'INDEX.md':
            continue
        text = path.read_text()
        url = re.search(r'^Source: (.+)$', text, re.MULTILINE).group(1)
        source = cache / url.split(f'cuda-{api}-api/')[1]
        soup = BeautifulSoup(source.read_bytes(), 'html.parser')
        assert f'{api.title()} API Reference Manual 13.4 documentation' in soup.title.get_text()
        content = soup.find(attrs={'itemprop': 'articleBody'})
        for link in content.select('.headerlink'):
            link.decompose()
        counts['pages'] += 1
        for signature in content.select('dt.sig'):
            value = signature.get_text().strip().replace('\n', ' ')
            assert value in text, (path, value[:100])
            counts['signatures'] += 1
        for field in content.select('dl.field-list > dt'):
            name = field.get_text(strip=True)
            if name in ('Parameters', 'Returns'):
                counts[name] += 1
        for pre in content.select('pre'):
            assert normalize_code(pre.get_text().strip()) in text, (path, 'code')
            counts['code_blocks'] += 1
        assert 'CUDAAPIPRESERVED' not in text
    print(f'CUDA {api}: {dict(counts)}; all indexed files present')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ptx-html', required=True, type=Path)
    args = parser.parse_args()
    references = Path('cuda_skill/references')
    check_ptx(args.ptx_html, references / 'ptx-docs')
    for api in ('runtime', 'driver'):
        check_api(api, references / f'cuda-{api}-docs')
