# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-26T~22:00+01:00 (Session 118)
- **Machine**: WSL
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Git pull + resolve multi-remote divergence

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
  - Pulled from origin — divergent branches (3 local, 3 remote commits since merge-base)
  - Merged origin/main: 3 modify/delete conflicts (conversation-log, push.sh, session-context) — kept local versions
  - Merged private/main: session-context conflict — kept local (private had blank template)
  - **Key fix**: origin merge silently deleted 16 pop-sci source files (book manuscripts, .tex, .pdf, .epub). Origin is the filtered public remote and never carries these files, so git treated the merge as "delete them". Manually restored all 16 from private/main.
  - Also picked up Session 116-117 changes: session-history.md, docs/session-log.md, CLAUDE.md dual-remote rule, reply-andre.txt

## Recovery Instructions
1. Active TODOs are listed above — pick one to work on
2. Full backlog at `backlog.md` (read when active TODOs are done)
3. **IMPORTANT**: Always pull from BOTH remotes. Origin merge can delete private-only files. After origin merge, always `git diff --name-status HEAD private/main` to check for missing files.
4. push.sh now has divergence guard — if it aborts, run `git pull --rebase private main` first
5. bibtex MUST run with dangerouslyDisableSandbox (sandbox blocks .bbl writes)
