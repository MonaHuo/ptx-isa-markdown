# NVIDIA CUDA Documentation + Claude Code Skill

NVIDIA's **PTX ISA 9.4**, **CUDA Runtime API 13.4**, and **CUDA Driver API 13.4** documentation converted to searchable Markdown, with a Claude Code skill for GPU development.

## What's Here

| Reference | Version | Markdown files, including index | Size |
| --- | --- | ---: | ---: |
| [PTX ISA](cuda_skill/references/ptx-docs/INDEX.md) | 9.4 | 506 | 2.0 MB |
| [CUDA Runtime API](cuda_skill/references/cuda-runtime-docs/INDEX.md) | 13.4 | 115 | 1.2 MB |
| [CUDA Driver API](cuda_skill/references/cuda-driver-docs/INDEX.md) | 13.4 | 151 | 1.3 MB |

Sizes use decimal MB. The complete skill, including search and profiling guides, is approximately 4.5 MB.

- **PTX ISA:** 505 section files organized by chapter, including 228 instruction-set files and the 9.2, 9.3, and 9.4 release notes. Deeper subsections remain in their parent file. Code examples, tables, and 292 image references are retained; section, table, and figure links resolve locally.
- **Runtime API:** 38 API modules, 69 dedicated structure/union pages, and 7 overview/reference pages covering synchronization, version mixing, deprecated APIs, and notices.
- **Driver API:** 51 API modules, 92 dedicated structure/union pages, and 7 overview/reference pages. Types documented inside a module remain in that module.
- **Development skill:** PTX and API search guides, profiling workflows (`nsys`, `ncu`), debugging patterns (`compute-sanitizer`, `cuda-gdb`), and TensorCore references.

## Update to PTX 9.4 and CUDA 13.4

The PTX refresh includes new target architectures, packed arithmetic and conversion forms, fabric operations, sparse compression instructions, and updated TensorCore and synchronization instructions. Consult the official release notes converted here:

- [PTX ISA 9.4 changes](cuda_skill/references/ptx-docs/13-release-notes/13.1-changes-in-ptx-isa-version-9.4.md)
- [PTX ISA 9.3 changes](cuda_skill/references/ptx-docs/13-release-notes/13.2-changes-in-ptx-isa-version-9.3.md)
- [PTX ISA 9.2 changes](cuda_skill/references/ptx-docs/13-release-notes/13.3-changes-in-ptx-isa-version-9.2.md)

CUDA 13.4 uses new Sphinx pages under `cuda_runtime_api/` and `cuda_driver_api/`. The old top-level module URLs can still serve older documentation. The scraper follows the new listings and checks the version of every page before generating output.

Chapter numbers and some filenames changed. Search guides and indexes use the current paths. Stale generated Markdown is removed after a successful regeneration.

## Structure

```text
cuda_skill/
├── SKILL.md
└── references/
    ├── ptx-docs/                          # PTX ISA 9.4
    │   ├── 9-instruction-set/
    │   ├── 5-state-spaces-types-and-variables/
    │   ├── 8-memory-consistency-model/
    │   ├── 13-release-notes/
    │   ├── 14-notices/
    │   └── INDEX.md
    ├── cuda-runtime-docs/                 # CUDA Runtime API 13.4
    │   ├── modules/
    │   ├── data-structures/
    │   ├── overview/
    │   └── INDEX.md
    ├── cuda-driver-docs/                  # CUDA Driver API 13.4
    │   ├── modules/
    │   ├── data-structures/
    │   ├── overview/
    │   └── INDEX.md
    ├── ptx-isa.md
    ├── cuda-runtime.md
    ├── cuda-driver.md
    ├── nsys-guide.md
    ├── ncu-guide.md
    └── debugging-tools.md
scrape_cuda_docs.py                        # Unified uv scraper
tests/test_scrape_cuda_docs.py            # Conversion regression tests
```

## Using the Skill

```bash
cp -r cuda_skill ~/.claude/skills/cuda
```

Ask Claude about register fragment layouts, TMA swizzling, CUDA errors, context management, or profiling. The skill searches local documentation and returns section references. You can also search the Markdown directly with any editor or CLI.

## Search Examples

```bash
# WGMMA register fragments
rg -n 'register fragment' cuda_skill/references/ptx-docs/9-instruction-set/

# TMA swizzle settings
rg -n 'swizzle_mode|No swizzling' cuda_skill/references/ptx-docs/

# New sparse compression instructions
rg -n 'spcompress|spdecompress' cuda_skill/references/ptx-docs/9-instruction-set/

# Runtime errors and device properties
rg -n -A 10 'cudaErrorInvalidValue' cuda_skill/references/cuda-runtime-docs/
cat cuda_skill/references/cuda-runtime-docs/data-structures/structcudadeviceprop.md

# Driver context and virtual memory APIs
rg -n -A 20 'cuCtxCreate' cuda_skill/references/cuda-driver-docs/modules/group__cuda__ctx.md
cat cuda_skill/references/cuda-driver-docs/modules/group__cuda__va.md
```

## Regenerating

Run from the repository root with [uv](https://docs.astral.sh/uv/) installed. Dependencies (`beautifulsoup4`, `html2text`, and `requests`) are declared in the script.

```bash
# Refresh each reference from NVIDIA
uv run --script scrape_cuda_docs.py ptx
uv run --script scrape_cuda_docs.py runtime --force
uv run --script scrape_cuda_docs.py driver --force

# Reconvert previously downloaded API HTML without network access
uv run --script scrape_cuda_docs.py runtime --skip-download
uv run --script scrape_cuda_docs.py driver --skip-download

# Reconvert a saved official PTX HTML page
uv run --script scrape_cuda_docs.py ptx --source-html /path/to/ptx-index.html

# Generate into a separate directory for review
uv run --script scrape_cuda_docs.py ptx --output-dir /tmp/ptx-docs
```

The scraper expects PTX **9.4** and CUDA **13.4** by default. A mismatched or incomplete source fails before replacing generated documentation. When deliberately upgrading again, select `--ptx-version` or `--cuda-version` and review changes to the upstream layout, indexes, and guides.

API HTML caches live beside the output directory in `cuda-runtime-docs-raw/` and `cuda-driver-docs-raw/`; they are ignored by Git and can be deleted. `--force` refreshes cached pages, while `--skip-download` requires a complete cache. Only generated Markdown belongs in the output directories, as regeneration removes obsolete `.md` files there.

## Conversion and Verification

- PTX sections are split without duplicating nested content. Explicit anchors preserve internal links, and every section records its original source URL and version.
- PTX code is fenced and preserves indentation and blank lines; trailing horizontal whitespace is normalized. Simple tables use Markdown. Complex tables retain HTML to preserve merged cells and header structure.
- API pages retain function/type declarations, parameters, return values, semantic notes, examples, and cross-reference names. Duplicate summaries are removed only when the detailed definitions exist on the same page.
- Navigation and permalink icons are excluded. API symbol links are reduced to their names for readable local search; each page retains its authoritative source URL.
- PTX diagrams remain external NVIDIA image URLs and require network access to display.

See [QUALITY_REPORT.md](QUALITY_REPORT.md) for the source-coverage checks for this refresh.

Run the regression tests:

```bash
uv run --with beautifulsoup4 --with html2text --with requests \
  python -m unittest discover -s tests -v
```

## Sources and License

Documentation © NVIDIA Corporation. Original notices are included in the converted references. This is an unofficial conversion; NVIDIA's documentation is authoritative:

- [PTX ISA](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html)
- [CUDA Runtime API](https://docs.nvidia.com/cuda/cuda-runtime-api/index.html)
- [CUDA Driver API](https://docs.nvidia.com/cuda/cuda-driver-api/index.html)
