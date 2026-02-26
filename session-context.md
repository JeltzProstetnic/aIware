# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-25T21:00:00+01:00 (Session 115)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Repo cleanup after multi-machine divergence

## Active TODOs (top-level — work on these next)
1. **COGITATE commentary** — trim `tmp/cogitate-commentary-draft.md` from 1,587 → 1,500 words, submit to NoC ScholarOne
2. **Seth BBS peer commentary** — deadline Jun 12, 2026. Draft proposal via anilseth.com/bbs-commentaries
3. **Cosmology → SSRN** — submit SB-HC4A to SSRN PhysicsRN
4. **Bochum registration** — register by May 30 at RUB site. Poster abstract already submitted. Attend in person.
5. **Researcher outreach Wave 2** — 8 targets not yet contacted (see `tmp/outreach-master-list-2026.md`)

## Waiting (no action — track responses)
- NoC resubmission (~6 weeks from ~Feb 2026)
- **Theory & Psychology** intelligence paper (~2-3 months from Feb 25) — last attempt
- Bochum abstract decision (before May 30)
- 5 conference/school submissions (Feb 22–24)
- 13+ researcher outreach emails (Feb 14–24)

## Current State
- **Active Task**: None — session complete
- **Progress (this session)**:
  - Picked up cross-project inbox task from claude-config: multi-machine divergence warning
  - Audited merge commit 26ba2bf — confirmed no data loss (119 vs 82 divergent commits since Session 59)
  - Root cause: push.sh never pulled, so two machines worked independently
  - Fixed push.sh: now fetches private/main, fast-forwards if behind, aborts if diverged
  - Cleaned tmp/: deleted 60+ stale files (revision chunks, comparison PDFs, old HTMLs, pycache)
  - Updated .gitignore: __pycache__, *.pyc, reference PDFs
  - Committed .claude/publication-workflow.md pointer and build_comparison.py
  - Cleared inbox task

## Recovery Instructions
1. Active TODOs are listed above — pick one to work on
2. Full backlog at `backlog.md` (read when active TODOs are done)
3. push.sh now has divergence guard — if it aborts, run `git pull --rebase private main` first
4. bibtex MUST run with dangerouslyDisableSandbox (sandbox blocks .bbl writes)
5. After ANY PDF build, run: `pytest tmp/test_content_integrity.py tmp/test_pdf_verification.py -v`
