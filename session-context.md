# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-23T20:15Z (Session 108)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Fix intelligence paper formatting issue + prepare for preprint uploads

## What Was Done This Session

### 1. Intelligence Paper Formatting Fix
- **Issue**: Paragraph starting "Conversely, the model predicts that motivation-enhancing interventions—environments" had first line extending 18pt (6mm) past right margin on page 16
- **Root cause**: LaTeX `---` (em dash) doesn't naturally insert a line break point. Combined with first-line paragraph indent, "interventions---environments" couldn't be broken
- **Fix**: Build scripts now emit `---\hspace{0pt}` instead of bare `---` for all em dashes. The `\hspace{0pt}` creates a zero-width break point
- **Applied to**: `tmp/build_intelligence_pdf.py` and `tmp/build_fmt_full_pdf.py`
- **Verified**: All lines now within margins (margin ≥55pt across all 25 pages). LaTeX hyphenates "envi-ronments" correctly.

### 2. Formatting Rules Updated
- Added "Em Dash Line Breaking" section to `paper/intelligence/paper.formatting-rules.md`

### 3. Test Added
- `test_em_dash_has_break_hint` in `tmp/test_build_scripts.py` — verifies em dashes include `\hspace{0pt}`
- 147/147 tests pass (was 146)

### 4. Both Papers Rebuilt
- Intelligence: 25pp, 139 KB, 0 warnings
- FMT full: 60pp, 718 KB, 0 warnings

## Pending — Next Session
1. **Upload preprints** — ALL 3 papers ready:
   - FMT full → Zenodo (new version, DOI: 10.5281/zenodo.18669891)
   - Intelligence → PsyArXiv (new version, DOI: 10.31234/osf.io/kctvg)
   - Cosmology → Zenodo (new version)
2. **Bochum poster abstract** — 700 words, deadline Apr 1

## Recovery Instructions
1. Read this file
2. All 3 PDFs are built and ready in canonical locations
3. Walk user through preprint uploads step by step (browser-based for Zenodo and PsyArXiv)
