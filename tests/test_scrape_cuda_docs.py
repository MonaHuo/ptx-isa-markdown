"""Regression checks for source migrations and content-preserving conversion."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from bs4 import BeautifulSoup
from scrape_cuda_docs import APIScraper, PTXScraper


def ptx_source(version="9.4"):
    return BeautifulSoup(f'''<html><title>PTX ISA {version} documentation</title>
    <div itemprop="articleBody">
    <section id="intro"><h1><span class="section-number">1. </span>Introduction</h1>
    <p>Parent-only prose.</p>
    <section id="child"><h2><span class="section-number">1.1. </span>Child</h2>
    <p>Child-only prose. <a href="#deep">Deep reference</a></p>
    <section id="deep"><h5>1.1.1.1.1. Deep</h5>
    <pre>ld.global.u32 %r1, [%rd1];\n\n\n    // retain blank lines\n</pre>
    <table id="table"><tr><th colspan="2">Merged heading</th></tr>
    <tr><td>A</td><td>B</td></tr></table>
    <img src="_images/example.png"></section></section></section>
    <section id="release-notes"><h1><span class="section-number">13. </span>Release Notes</h1>
    <section id="changes-in-ptx-isa-version-9-4"><h2><span class="section-number">13.1. </span>Changes in PTX ISA Version 9.4</h2>
    <p><a href="#child">Child reference</a></p></section></section>
    </div></html>''', "html.parser")


def api_source(body, version="13.4"):
    return BeautifulSoup(f'''<html><title>CUDA Runtime API Reference Manual {version} documentation</title>
    <div itemprop="articleBody"><h1>Device Management</h1>{body}</div></html>''', "html.parser")


class PTXTests(unittest.TestCase):
    def test_table_captions_and_preformatted_cells(self):
        soup = ptx_source()
        table = soup.find('table')
        caption = soup.new_tag('caption')
        caption.string = 'Table caption'
        table.insert(0, caption)
        pre = soup.new_tag('pre')
        pre.string = 'first();\n\n\nsecond();'
        table.find('td').append(pre)
        files = PTXScraper(Path('unused')).render(soup)
        markdown = files[Path('1-introduction/1.1-child.md')]
        self.assertIn('Table caption\n\n<table>', markdown)
        parsed = BeautifulSoup(markdown, 'html.parser')
        self.assertEqual(parsed.find('table').find('pre').get_text(), pre.get_text())
        self.assertNotIn('```', str(parsed.find('table')))

    def test_nested_content_has_one_owner_and_local_links(self):
        files = PTXScraper(Path("unused")).render(ptx_source())
        combined = "\n".join(v for p, v in files.items() if p.name != "INDEX.md")
        self.assertEqual(combined.count("Parent-only prose."), 1)
        self.assertEqual(combined.count("Child-only prose."), 1)
        self.assertIn('(../1-introduction/1.1-child.md#child)', combined)
        self.assertIn('<a id="deep"></a>', combined)
        self.assertIn('[1.1. Child](1-introduction/1.1-child.md)', files[Path("INDEX.md")])
        self.assertIn('ld.global.u32 %r1, [%rd1];\n\n\n    // retain blank lines', combined)
        self.assertIn('colspan="2"', combined)
        self.assertIn('https://docs.nvidia.com/cuda/parallel-thread-execution/_images/example.png', combined)
        self.assertNotIn('PTXPRESERVED', combined)

    def test_wrong_version_does_not_touch_existing_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            old = root / 'existing.md'
            old.write_text('keep this')
            with patch.object(PTXScraper, 'fetch_page', return_value=ptx_source('9.3')):
                with self.assertRaises(ValueError):
                    PTXScraper(root).run()
            self.assertEqual(old.read_text(), 'keep this')

    def test_regeneration_removes_stale_sections_but_keeps_other_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'stale.md').write_text('old version')
            (root / 'keep.txt').write_text('unrelated')
            with patch.object(PTXScraper, 'fetch_page', side_effect=lambda _: ptx_source()):
                PTXScraper(root).run()
                first = {p: p.read_bytes() for p in root.rglob('*.md')}
                PTXScraper(root).run()
            self.assertFalse((root / 'stale.md').exists())
            self.assertTrue((root / 'keep.txt').exists())
            self.assertEqual(first, {p: p.read_bytes() for p in root.rglob('*.md')})


class APITests(unittest.TestCase):
    def test_details_notes_and_code_survive_summary_cleanup(self):
        soup = api_source('''<div class="dl-as-table"><a href="#func">duplicate summary</a></div>
        <dl class="cpp function"><dt class="sig" id="func">cudaError_t cudaExample(int *value)</dt>
        <dd><p>Detailed behavior.</p><div class="admonition note">A semantic restriction.</div>
        <div class="admonition seealso">See also cudaOther</div>
        <dl class="field-list"><dt>Parameters</dt><dd>value: output pointer</dd>
        <dt>Returns</dt><dd>cudaSuccess</dd></dl></dd></dl>
        <pre>example();\n\n\n    next();</pre>''')
        markdown = APIScraper('runtime', Path('unused')).convert_api_page(soup, 'https://example.com/page')
        self.assertNotIn('duplicate summary', markdown)
        for text in ['cudaError_t cudaExample(int *value)', 'Detailed behavior.',
                     'A semantic restriction.', 'See also cudaOther', 'output pointer',
                     'cudaSuccess', 'example();\n\n\n    next();']:
            self.assertIn(text, markdown)
        self.assertNotIn('CUDAAPIPRESERVED', markdown)

    def test_summary_without_details_is_kept(self):
        soup = api_source('<div class="dl-as-table"><a href="#absent">only description</a></div>')
        markdown = APIScraper('runtime', Path('unused')).convert_api_page(soup, 'https://example.com/page')
        self.assertIn('only description', markdown)

    def test_reject_legacy_or_mixed_version_pages(self):
        scraper = APIScraper('runtime', Path('unused'))
        for soup in [api_source('', '13.3'), BeautifulSoup('<title>CUDA Runtime API :: CUDA Toolkit Documentation</title>', 'html.parser')]:
            with self.assertRaises(ValueError):
                scraper._validate_source(soup)

    def test_discovery_includes_unions_and_overview(self):
        scraper = APIScraper('runtime', Path('unused'))
        def source(url):
            if url.endswith('apis.html'):
                return api_source('<a href="group__CUDART__DEVICE.html">Device Management</a>')
            if url.endswith('structs.html'):
                return api_source('<a href="structs.html#structs">Self link</a><a href="unioncudaValue.html">cudaValue</a><a href="structcudaInfo.html">cudaInfo</a>')
            return api_source('<a href="api-sync-behavior.html">Synchronization</a><a href="cuda_runtime_api/apis.html">APIs</a>')
        with patch.object(scraper, '_load_source', side_effect=source):
            pages = scraper.discover_pages()
        self.assertEqual(len(pages), 4)
        self.assertIn('data-structures/unioncudavalue.md', [p['path'] for p in pages])
        self.assertTrue(all('cuda_runtime_api/' in p['url'] for p in pages if p['path'].startswith('modules/')))

    def test_failed_download_leaves_output_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            old = root / 'existing.md'
            old.write_text('keep this')
            scraper = APIScraper('runtime', root)
            with patch.object(scraper, 'discover_pages', return_value=[{'url': 'https://example.com/missing'}]), patch.object(scraper, '_load_source', side_effect=RuntimeError('download failed')):
                with self.assertRaises(RuntimeError):
                    scraper.run()
            self.assertEqual(old.read_text(), 'keep this')


if __name__ == '__main__':
    unittest.main()
