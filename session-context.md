# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-17 (Session 67, post-push, final)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Write SB-HC4A cosmology formalization paper — DONE

## Current State
- **Active Task**: Ready for restart
- **Progress**:
  - Cosmology formalization paper written and pushed
  - All open decisions resolved (see below)
  - Ready for next session

## DECISIONS MADE THIS SESSION
1. **Cosmology → final book chapter** (not separate book). Once reader understands consciousness, cosmology is compact (~1-2 chapters).
2. **Five-class taxonomy stays in cosmology paper** for now. Option to expand into separate paper later remains open.
3. **Paper ordering**: 1-consciousness, 2-intelligence, 3-cosmology, 4-6 formalizations.

## TOP TODO (Next Session)
1. **IMMEDIATE: Write cosmology book chapter** — add to `pop-sci/book-manuscript.md` as final chapter(s). Adapt from `paper/cosmology/sb-hc4a.md` for general audience. No jargon, no equations.
2. Intelligence paper: trim ~358 words, highlights, .docx, submit to *New Ideas in Psychology*
3. NoC resubmission (trimmed paper .docx ready)
4. Outreach emails (3 ready to send)

## Key Files
- `paper/cosmology_formal/sb-hc4a-formalization.md` — cosmology formalization paper (CANONICAL SOURCE)
- `paper/cosmology_formal/sb-hc4a-formalization.pdf` — generated PDF
- `paper/cosmology/sb-hc4a.md` — cosmology paper (CANONICAL SOURCE)
- `pop-sci/book-manuscript.md` — book manuscript (CANONICAL SOURCE, cosmology chapter to be added)
- PDF build for formalization: `pandoc paper/cosmology_formal/sb-hc4a-formalization.md -o paper/cosmology_formal/sb-hc4a-formalization.pdf --pdf-engine=pdflatex -V geometry:margin=1in -V fontsize=11pt -V documentclass=article -H paper/cosmology_formal/unicode-header.tex`

## Recovery Instructions
1. Read `pop-sci/book-manuscript.md` to understand current book structure
2. Read `paper/cosmology/sb-hc4a.md` for source material to adapt
3. Write cosmology as final chapter(s) of the book — pop-sci tone, no equations
4. CANONICAL SOURCE RULE: edit .md first, regenerate .tex/.pdf after

## Conversation Summary
Session 67. Wrote the SB-HC4A cosmology formalization paper (third in the "Toward..." series, ~9,200 words, 8 modules). Fixed Bruno Gruber death year (HE IS ALIVE). Restructured README. Decisions: cosmology as final book chapter (not separate book), taxonomy stays in cosmology paper for now. Ready for restart.
