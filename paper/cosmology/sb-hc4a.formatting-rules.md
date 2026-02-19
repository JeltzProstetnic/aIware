# Formatting Rules for Cosmology Paper (Symmetry-Breaking via Higher-C4A)

Rules for pandoc-based PDF generation. Unicode header status: MISSING.

## Build Process

- **Build tool**: `pandoc`
- **Likely command**: `pandoc sb-hc4a.md --pdf-engine=pdflatex -o sb-hc4a.pdf`
- **Unicode header**: `unicode-header.tex` is **MISSING from this directory**

## Unicode Support Status

- **TODO**: Audit `sb-hc4a.md` for Unicode math symbols
- If Unicode symbols are present, copy `unicode-header.tex` from `paper/fmt_formal/` or `paper/rim_formal/`
- If Unicode symbols are present, update build command to include `-H unicode-header.tex`

## Maintenance Notes

- **CRITICAL**: `unicode-header.tex` is MISSING from `/home/jeltz/aIware/paper/cosmology/`
- Before next build:
  1. Read `sb-hc4a.md` and check for Unicode math symbols (Greek letters, math operators, arrows, etc.)
  2. If found, copy `unicode-header.tex` from `paper/fmt_formal/` or `paper/rim_formal/`
  3. Update build command to: `pandoc sb-hc4a.md -H unicode-header.tex --pdf-engine=pdflatex -o sb-hc4a.pdf`
  4. Verify mappings in `unicode-header.tex` cover all symbols used in `sb-hc4a.md`
- If no Unicode symbols are used, document that fact here and confirm simple pandoc build is sufficient
