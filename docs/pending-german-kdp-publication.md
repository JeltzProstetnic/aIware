Action: act

# German KDP Publication — Next Session

All assets built and committed in Session 185. Tomorrow: upload to KDP.

## Assets Ready

| Publication | File | Size |
|---|---|---|
| Kindle eBook | `pop-sci/book-manuscript-de.epub` | 3.0 MB |
| Kindle front cover | `pop-sci/cover-kindle-de.jpg` (1600×2560) | 2.2 MB |
| Paperback interior | `pop-sci/book-manuscript-de.pdf` (269 pp, 6×9) | 1.2 MB |
| Paperback wrap | `pop-sci/cover-wrap-de.pdf` (spine 0.606") | 3.1 MB |
| Paperback front | `pop-sci/cover-front-de.pdf` | 1.7 MB |
| Hardcover interior | `pop-sci/book-manuscript-de-hc.pdf` | 1.2 MB |
| Hardcover wrap | `pop-sci/cover-wrap-hc-de.pdf` (14.370×10.417 case laminate) | 3.6 MB |

## Before Upload — Required Actions

### 1. German ISBNs
Both wraps were built with placeholder ISBNs (`[TBD-DE-PB]`, `[TBD-DE-HC]`). No ISBN barcode embedded.

**Decision needed:** Use KDP-free ISBNs (Amazon-only distribution, fastest) or buy own ISBNs (wider distribution, costs money)?

After decision:
1. Edit `tmp/build_book_cover_de.py` — replace `[TBD-DE-PB]` and `[TBD-DE-HC]` with real ISBNs in EDITIONS dict
2. Ensure `python-barcode` installed (`pip install python-barcode`)
3. Rerun `python3 tmp/build_book_cover_de.py --edition all --wrap` to regenerate wraps with barcodes
4. Also rerun `--kindle` if front cover title area needs tweaks

### 2. Upload Order (recommended — follows English pattern)
1. **Kindle eBook first** — fastest review cycle, validates metadata
   - KDP → Create Kindle eBook → upload `book-manuscript-de.epub` + `cover-kindle-de.jpg`
   - Metadata: title "Die Simulation namens Ich", subtitle "Die Architektur von Bewusstsein, Berechnung und Kosmos", author Matthias Gruber, language German
   - Description: use back cover blurb (in `tmp/build_book_cover_de.py` BACK_COVER_BLURB)
   - Categories: same as English (Philosophy > Consciousness, Science > Neuroscience, etc.)
2. **Paperback** — after Kindle approved
   - Upload `book-manuscript-de.pdf` (interior) + `cover-wrap-de.pdf` (wrap)
   - Link to Kindle edition
3. **Hardcover** — last
   - Upload `book-manuscript-de-hc.pdf` + `cover-wrap-hc-de.pdf`
   - Link to paperback

### 3. Known Limitations
- **Figure 3** (phenomenological content graph) missing from German EPUB. Only SVG exists for German (`figures/figure3-phenomenological-content-bw-de.svg`), no rendered PNG. English version inserts it post-preprocess. For German, either render the SVG → PNG before upload, or accept the missing figure (one of four figures).
- **Back cover tagline** — English had placeholder "Review pending". German stripped it entirely. Can add one post-upload when a real German quote is available.

## Build Scripts Reference
- `tmp/build_book_pdf_de.py --edition us` — paperback interior
- `tmp/build_book_pdf_de.py --edition us-hc` — hardcover interior
- `tmp/build_book_cover_de.py --edition de --wrap` — paperback wrap
- `tmp/build_book_cover_de.py --edition de-hc --wrap` — hardcover wrap
- `tmp/build_book_cover_de.py --edition de` — paperback front only
- `tmp/build_book_cover_de.py --kindle` — 1600×2560 Kindle front JPG
- `tmp/build_book_epub_de.py` — EPUB
