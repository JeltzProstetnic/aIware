task: true
file: docs/pending-german-kdp-publication.md
backlog: AIW-50
description: German KDP publication. All assets built in Session 185 (ebook/paperback/hardcover). BEFORE upload: decide German ISBNs (KDP-free vs bought), update `tmp/build_book_cover_de.py` EDITIONS dict, rerun `python3 tmp/build_book_cover_de.py --edition all --wrap` to regenerate wraps with barcodes. Optionally render `figures/figure3-phenomenological-content-bw-de.svg` → PNG and rebuild EPUB. Upload order: Kindle first, then paperback, then hardcover. Metadata and back cover blurb are in the build script. Full checklist in `docs/pending-german-kdp-publication.md`.
