# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-16 (Session 52, complete)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: README fixes + book illustrations + table rendering

## What Was Done (Session 52)

### README Fixes
1. **Restored broken arxiv link**: Copied PDF to `paper/full/arxiv/paper.pdf` so old URLs shared with people still work
2. **Updated links**: README now points to `paper/full/biorxiv/paper.pdf` (current location)
3. **Removed duplicate figure**: Real/Virtual Split appeared twice — removed standalone occurrence
4. **Fixed stale data**: session count 42→51+, book word count 26,500→29,000
5. **Fixed typo**: "two few" → "two that few"
6. **Reframed paper descriptions**: "Short paper" → "Core mechanism paper", "Full paper" → "Extended framework paper" — avoids redundant-publication optics for NoC vs PLoR

### Book Illustrations & Build Script
1. **Replaced 4 figure placeholders** in book-manuscript.md:
   - Bubble diagram → `figures/book/book_page_064_render.png` (German original with English caption)
   - Real/Virtual split → `figures/figure2-real-virtual-split.png`
   - Five-layer stack → HTML comment TODO (needs manual SVG creation)
   - VR illustration → SDXL/Flux prompt written in HTML comment
2. **Fixed table rendering**: Switched from `longtable` (bare columns, overflow) to `tabularx` (auto-wrapping X columns). Font size reduction for 4+ column tables.
3. **Build script overhaul** (`tmp/build_book_pdf.py`):
   - Added markdown image parsing (`![alt](path)` → LaTeX figure)
   - Added HTML comment skipping
   - Greek letter escaping (Φ → $\Phi$), Unicode arrows
   - Subprocess encoding fix
   - Expanded graphicspath for book figures subdir
   - Removed figure2 from FIGURE_INSERTIONS (now embedded in markdown)
4. **PDF rebuilt**: 0.9 MB, zero LaTeX errors, zero table overflow warnings

### Journal Strategy Discussion
- **BBS (Behavioral and Brain Sciences)** discussed as alternative to Physics of Life Reviews
- IF 13.7, Open Peer Commentary format (20-40 invited commentaries)
- Near-perfect fit for the theory — cross-disciplinary, testable predictions
- Recommendation: wait for NoC decision, then submit BBS proposal
- Overlapping publication concern addressed by reframing README (core mechanism vs extended framework)

## Canonical File Paths
- **Full paper Markdown**: `paper/full/four-model-theory-full.md` (RECONCILED — ~16,744 body words)
- **Full paper LaTeX**: `paper/full/biorxiv/paper.tex` (STALE — needs regeneration from .md)
- **Full paper PDF**: `paper/full/biorxiv/paper.pdf` (bioRxiv version)
- **Trimmed paper (NoC)**: `paper/trimmed/noc/` (FROZEN — submitted 2026-02-13)
- **Intelligence paper**: `paper/intelligence/paper.md` (canonical, ~8,757 words)
- **Book manuscript**: `pop-sci/book-manuscript.md` (~29,000+ words, 14 chapters + 3 appendices)
- **Book .tex**: `pop-sci/book-manuscript.tex` (REBUILT — in sync with .md)
- **Book PDF**: `pop-sci/book-manuscript.pdf` (REBUILT — 0.9 MB)
- **Build script**: `tmp/build_book_pdf.py` (updated with image/table fixes)

## User TODOs (Carried Forward + New)
1. **Review book PDF** — just opened on Windows desktop. Check figures and tables render properly.
2. **Create five-layer stack SVG** — technical diagram, needs manual creation (see TODO comment in book-manuscript.md)
3. **Generate VR illustration** — SDXL/Flux prompt is in book-manuscript.md HTML comment
4. **Full paper .tex regeneration**: Still stale — needs regeneration from reconciled .md
5. **BBS journal decision**: After NoC decision (~late March), consider submitting target article proposal
6. **Intelligence paper → NIP submission**

## Recovery Instructions
1. Read this file
2. Session 52 work is COMMITTED and PUSHED to both remotes
3. Book PDF is rebuilt with figures and fixed tables
4. Two figure TODOs remain: five-layer stack SVG + VR illustration (SDXL prompt written)
5. Full paper .tex is still stale (from Session 51)
