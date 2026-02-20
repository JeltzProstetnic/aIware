# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-20 (Session 88)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: KDP publishing pipeline — EPUB, covers, hardcover preparation

## What Session 88 Did
1. **EPUB build script** (`tmp/build_book_epub.py`): Pandoc-based, generates `pop-sci/book-manuscript.epub` (2.86 MB)
2. **KDP paperback audit** against G202145060 — 5 issues found and fixed:
   - 3 images re-rendered from SVG at 361 DPI (was 154-197)
   - Table `\midrule` bumped to 0.8pt (was 0.54, KDP min 0.75)
   - PDF bookmarks removed (`bookmarks=false`)
   - PDF metadata added (title, author, subject)
   - ISBN 9798249169121 added to copyright page
3. **ISBN barcode** generated (EAN-13) and placed on back cover wrap
4. **Hardcover edition** prepared:
   - Interior PDF: `pop-sci/book-manuscript-hc.pdf` (ISBN 9798249172268)
   - Case laminate cover: `pop-sci/cover-wrap-hc.pdf` (14.141"×10.382")
   - Separate barcode: `pop-sci/isbn-barcode-hc.png`
5. **Page count corrected** to 251 (was 253 in cover script)
6. **Memory updated** with ISBNs, KDP specs, build outputs

## ISBNs
- **US Paperback**: 9798249169121
- **US Hardcover**: 9798249172268
- **EU Paperback**: TBD

## KDP-Ready Files
| File | Purpose | Status |
|------|---------|--------|
| `pop-sci/book-manuscript.pdf` | US paperback interior | READY |
| `pop-sci/book-manuscript-hc.pdf` | US hardcover interior | READY |
| `pop-sci/book-manuscript.epub` | Kindle eBook | READY |
| `pop-sci/cover-wrap.pdf` | US paperback full cover | READY |
| `pop-sci/cover-wrap-hc.pdf` | US hardcover case laminate | READY |
| `pop-sci/cover-kindle.jpg` | Kindle eBook cover | READY |
| `pop-sci/isbn-barcode.png` | Paperback barcode | READY |
| `pop-sci/isbn-barcode-hc.png` | Hardcover barcode | READY |

## Current Stats
- Pages: 251 (US 6"×9"), both paperback and hardcover
- Figures: 5 (all B&W, all ≥361 DPI)
- All lines ≥0.75pt, no bookmarks, metadata set

## Submission Status
- NoC: RESUBMITTED, awaiting feedback
- SSRN: SUBMITTED, awaiting acceptance
- Zenodo cosmology: PUBLISHED (DOI: 10.5281/zenodo.18698606)
- PsyArXiv intelligence: PUBLISHED (https://osf.io/preprints/osf/kctvg)

## Recovery
1. Read this file + MEMORY.md
2. Book: `pop-sci/book-manuscript.md` — content source of truth
3. Build: `tmp/build_book_{pdf,epub,cover}.py`
4. Next: Upload to KDP (paperback + hardcover + eBook)
