# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-19 (Session 77)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Build scripts + Serena fix + publications + About page + personalization

## Current State
- **Active Task**: Session complete — commit and push pending

## What Session 77 Did
1. **Build scripts (Priority 0)**: Created `tmp/build_cosmology_pdf.py` for Papers 3 & 6. Both built successfully. Created missing formatting-rules.md for Paper 6. Updated document registry.
2. **Serena browser fix**: Added `--open-web-dashboard False` to all 5 `.mcp.json` files system-wide. Takes effect next restart.
3. **Personalization prompt**: Created `~/claude-config/global/rules/user-profile.md`, symlinked, wired into global CLAUDE.md "always read first" table.
4. **Publications integration**: Created `publications/` directory with 7 historic PDFs (3 academic, 3 theses incl. bachelor's, 1 book). Merged perplexity reports into `tmp/publications-inventory.md` (21+ works).
5. **About the Author page**: Created `ABOUT.md` (separate page, not in README). Bio narrative + complete publication list with links. Linked from README.
6. **README cleanup**: Removed all markdown source links (7), removed inaccessible docs/ links (6), fixed formalization companion link, added ABOUT.md references.

## NEXT SESSION — Priorities
1. SSRN PhysicsRN submission (abstract finalized, Zenodo done)
2. Book edits (Ch 7 expand, Ch 14-15 restructure, em-dash pass) — USER INPUT NEEDED for Ch 7
3. Intelligence paper trim (~358 words) + highlights + .docx + submit to NIdP
4. User review of ABOUT.md on GitHub — may need corrections/additions

## Parked TODOs

### Publications
- Intelligence paper: trim ~358 words, highlights, .docx, submit to *New Ideas in Psychology*
- NoC resubmission (trimmed paper .docx ready)
- Outreach emails (3 ready to send: Priesemann, Metzinger, Carhart-Harris)
- **Wetterich contacted** — waiting for reply
- Computational atoms insight — separate short paper?

### Research
- **Perplexity findings → FMT formalization**: What do Wetterich, Levin-Wen, and QCA/QFT results mean for the mathematical formalization of the four-model theory?

### Infrastructure (low priority)
- Paper 1 (full consciousness paper) still needs build script
- Update Claude Code
- Deploy on other machines

## Recovery Instructions
1. Read this file + MEMORY.md
2. User may have corrections to ABOUT.md after reviewing on GitHub
3. Build scripts: `tmp/build_book_pdf.py` (book), `tmp/build_cosmology_pdf.py` (Papers 3 & 6)
4. Publications inventory: `tmp/publications-inventory.md`
