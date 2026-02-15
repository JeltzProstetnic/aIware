# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-15 (Session 39, complete)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Finalize long paper for bioRxiv (content integration) — DONE

## Current State
- **Active Task**: COMPLETE — all feedback items integrated into long paper
- **Paper status**: `paper/full/arxiv/paper.tex` — 53 pages, compiles cleanly, 7 new content additions + 1 acknowledgment fix
- **Build**: `cd paper/full/arxiv && bibtex paper && pdflatex paper.tex && pdflatex paper.tex`

## Next Session Plan (Session 40)
**Priority: Final thorough check of long paper before bioRxiv submission**
1. Citation audit — verify every \citep/\citet has a matching bib entry, correct year, correct author names
2. Internal consistency check — do forward/back references within the paper match?
3. Auditor concerns — look for overclaims, unsupported assertions, missing caveats
4. Abstract check — does the abstract still accurately reflect the paper after additions?
5. bioRxiv formatting requirements — any specific prep needed for upload?

**After submission:**
- Book manuscript edits (48 feedback items from `tmp/book-feedback-session37.md`)
- Short/long paper comparison session (assess what can be ported during NoC peer review)

## Key File Locations
- **Long paper**: `paper/full/arxiv/paper.tex` (the bioRxiv target)
- **References**: `paper/full/arxiv/references.bib`
- **Trimmed paper**: `paper/trimmed/arxiv/paper.tex` (NoC submission, under review)
- **Feedback log**: `tmp/book-feedback-session37.md` (48 items)
- **Book manuscript**: `pop-sci/book-manuscript.md`
- **Intelligence paper**: `paper/intelligence/paper.md`

## Recovery Instructions
1. Read this file for orientation
2. Read `docs/conversation-log.md` Session 39 entry for detailed change list
3. The paper is in clean, compilable state — no pending edits
4. Start with citation audit of paper.tex against references.bib
