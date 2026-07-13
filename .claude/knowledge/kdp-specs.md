<!-- consumed-by: MEMORY.md (convenience mirror); build scripts tmp/build_book_{pdf,epub,cover}.py -->
# KDP Publishing — ISBNs & Specs

Canonical home for the print specifications mirrored in `MEMORY.md`. Durable reference data.

## ISBNs
- **US Paperback:** 9798249169121
- **US Hardcover:** 9798249172268
- **EU Paperback:** TBD
- **German editions (amazon.de):** Kindle (KU), paperback 9798257520600, hardcover 9798257524424. Canonical URL `https://www.amazon.de/dp/B0GX2WJYB1/`.

## English print specs
- **Trim:** 6"×9", 251 pages, white paper, B&W ink
- **Spine:** pages × 0.002252" = 0.565"
- **Paperback margins:** inner 0.875", outer/top/bottom 0.75"
- **Hardcover cover:** case laminate; wrap 0.51", hinge 0.4", text safety 0.635"
- **Hardcover formula:** width = 2×trim_w + spine + 0.394 + 2×0.591; height = trim_h + 0.2
- **Barcode:** EAN-13, 2"×1.2", 300 DPI, ≥0.76" from bottom, ≥0.25" from hinge
- **KDP minimums:** images 300 DPI, lines 0.75pt

## Build
- **Scripts:** `tmp/build_book_{pdf,epub,cover}.py` (EN), `tmp/build_book_cover_de.py` (DE)
- **Outputs:** `pop-sci/book-manuscript.{pdf,epub}`, `pop-sci/cover-{front,wrap,kindle}.{pdf,jpg}`, `pop-sci/isbn-barcode.{png,svg}`
- **Cover QA (AIW-60):** the subtitle/artwork overlap bug shipped twice — visually verify the rendered wrap at print size before declaring any cover done. See `memory/feedback_book_cover_qa.md`.

## Translation editions (S258, 2026-07-12/13)
- **Kindle covers (all 8):** built via `tmp/build_translation_covers_latex.py` (EN/DE/ES/FR/IT/PT, pdflatex + palatino, the EN LaTeX front-cover recipe: black!90→black!25 top gradient @0.72 + black!82→black!20 author gradient @0.68; subtitle anchored to `covtitle.south` so it never overlaps; per-lang title size 26–36 for a 2-line fit). JA/ZH via `tmp/build_translation_kindle_covers.py` (PIL — same gradient in `_lerp_gradient`; Yu Gothic / Microsoft YaHei) because **xelatex is NOT installed on WSL**.
- **eBooks (translations):** `tmp/build_book_epub_lang.py` (pandoc, CJK-native, copies the localized inline figures, omits figure3 which isn't localized).
- **Print interiors (translations):** `tmp/build_translation_interior.py` drives `build_book_pdf.py` with per-language overrides (babel hyphenation, KDP-free blank ISBN, translated edition line, and `.tex` post-processing to swap the hardcoded EN front matter — title page / subtitle / running header / pdftitle / dedication; renames the translated title/subtitle/TOC headings to the EN skip-targets so they don't leak into the body). Copyright legal boilerplate stays EN (accepted). **Latin four only — JA/ZH print interiors need a CJK LaTeX engine (xelatex absent, lualatex has no luatexja; weasyprint is available as an alternate pipeline, or `sudo apt install texlive-xetex`).**
- **KDP language gotchas:** KDP has **no Simplified-Chinese** eBook option — only **Chinese (Traditional) (experimental, beta)**, which requires a **.docx** upload (not epub) and **horizontal content only**. A Simplified edition must ship as .docx under the Traditional tag, or be converted to Traditional (opencc, not installed). Japanese needs extra KDP fields: title/subtitle **katakana pronunciation** (no `、` commas — katakana only), **romanized** title/subtitle (English or ASCII romaji — macrons ē/ū/ā are rejected), and author-name katakana.
