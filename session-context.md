# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-19 (Session 72)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Pop-sci book — deep review, editing, illustration, publishing

## Current State
- **Active Task**: READY FOR RESTART
- **All infrastructure TODOs from Session 71**: DONE (Session 72)
- **Skills installed**: Restart required to load (docx, pdf, doc-coauthoring + 6 global skills)

## What Session 72 Did
1. Absorbed wsl-claude-setup into `~/claude-config/setup/` (12 files, ~90KB). Local repo deleted. Remote preserved until setup proven.
2. Evaluated Agent Teams vs TEAM_MODE — documented in `~/claude-config/knowledge/agent-teams-vs-team-mode.md`. Keep TEAM_MODE.
3. Cloned skill collections (Anthropic, obra, Trail of Bits, Sentry). Installed 3 aIware skills + 6 global skills.
4. Consolidated 4 review scripts into `~/claude-config/tools/review_changes.py`. Old scripts archived.
5. Created formatting-rules.md for all 6 papers.
6. Removed obsolete `paper/cosmology/SB-HC4A_formal.md`.

## NEXT SESSION — Book Pipeline

### Phase 1: Deep Review
- Read `pop-sci/book-manuscript.md` (~31,000 words) end-to-end
- Assess: flow, consistency, accuracy, readability, narrative arc
- Flag: repetition, gaps, unclear passages, tonal shifts
- Generate review HTML for author to scan

### Phase 2: Editing
- Apply review findings
- Ensure chapter transitions are smooth
- Verify all theory references are consistent with papers
- Check that pop-sci tone is maintained (not too academic, not too casual)

### Phase 3: Illustration
- Identify passages that need figures/diagrams
- Design illustrations for key concepts (four models, real/virtual split, qualia)
- Create or commission visuals

### Phase 4: Publishing
- Final proofread
- Format for target platform (self-publishing? publisher submission?)
- Cover design, metadata, ISBN

## Parked TODOs (not next session)

### Publications
- Intelligence paper: trim ~358 words, highlights, .docx, submit to *New Ideas in Psychology*
- NoC resubmission (trimmed paper .docx ready)
- Outreach emails (3 ready to send: Priesemann, Metzinger, Carhart-Harris)
- Computational atoms insight — separate short paper?

### Infrastructure (low priority)
- Cosmology paper missing unicode-header.tex
- Papers 1 and 3 need build scripts (.tex currently hand-maintained)
- Update Claude Code 2.1.37 → 2.1.47
- Deploy on other machines (NUC, Steam Decks, etc.)

## Recovery Instructions
1. Read this file. Next step: deep book review.
2. Book manuscript: `pop-sci/book-manuscript.md`
3. Book formatting rules: `pop-sci/book-manuscript.formatting-rules.md`
4. Build script: `tmp/build_book_pdf.py`
5. Review tool: `tmp/review_changes.py` (symlink to `~/claude-config/tools/`)
6. Skills need restart to load.
