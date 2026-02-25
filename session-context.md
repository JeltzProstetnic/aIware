# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-25T11:00:00+01:00 (Session 113)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Create CLAUDE.md manifest (inbox task)

## Active TODOs (top-level — work on these next)
1. **COGITATE commentary** — trim `tmp/cogitate-commentary-draft.md` from 1,587 → 1,500 words, submit to NoC ScholarOne
2. **Seth BBS peer commentary** — deadline Jun 12, 2026. Draft proposal via anilseth.com/bbs-commentaries
3. **Cosmology → SSRN** — submit SB-HC4A to SSRN PhysicsRN
4. **Bochum registration** — register by May 30 at RUB site. Poster abstract already submitted. Attend in person.
5. **Researcher outreach Wave 2** — 8 targets not yet contacted (see `tmp/outreach-master-list-2026.md`)

## Waiting (no action — track responses)
- NoC resubmission (~6 weeks from ~Feb 2026)
- Phil Psych intelligence paper (~5 months from Feb 23)
- Bochum abstract decision (before May 30)
- 5 conference/school submissions (Feb 22–24)
- 13+ researcher outreach emails (Feb 14–24)

## Current State
- **Active Task**: None — session complete
- **Progress (this session)**:
  - Created `CLAUDE.md` manifest at project root (Knowledge Loading, Key Files, Cross-Project, Project Structure, Build Infrastructure, Communication Rules)
  - Added cross-project reference to `fmt-visibility-strategy.md` (shared with social project)
  - Removed old `.claude/publication-workflow.md` pointer (superseded by manifest)
  - Cleared aIware entry from cross-project inbox

## Recovery Instructions
1. Active TODOs are listed above — pick one to work on
2. Full backlog at `backlog.md` (read when active TODOs are done)
3. Cross-project strategy: `~/claude-config/cross-project/fmt-visibility-strategy.md`
4. bibtex MUST run with dangerouslyDisableSandbox (sandbox blocks .bbl writes)
5. After ANY PDF build, run: `pytest tmp/test_content_integrity.py tmp/test_pdf_verification.py -v`
