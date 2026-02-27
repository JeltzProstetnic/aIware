# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-02-27 — WSL
**Goal:** Create FMT implementation spec for Claude Code AC implementation
**Completed:**
- Created `tmp/fmt-implementation-spec.md` — targeted engineering extract of FMT + formalization roadmap (~400 lines)
- PDF generated and opened
- Cross-project inbox task dropped for `aIware.implementation` to pick up the spec
- Git divergence on origin resolved (force-push with lease — local was superset)
- Added divergence recovery + session-context protection rules to CLAUDE.md Git & Push section
**Key Decisions:**
- Implementation spec is in `tmp/` (not pushed to public). Implementation project gets it via inbox task.
- Git divergence caused by same sessions committed on VPS and WSL with different merge topologies. Resolved by force-pushing origin (public mirror) since local was the superset. Added recovery procedure to CLAUDE.md.
- Session context was blank because a stale push from another machine overwrote it. Added protection rule to CLAUDE.md.
**Pending at shutdown:** 4 active TODOs (see MEMORY.md). Inbox still has CIMCAI and Digital Minds tasks to evaluate.
**Recovery/Next session:**
- Read `tmp/fmt-implementation-spec.md` if continuing implementation work
- The inbox task for aIware.implementation is live — next session in that project should pick it up
- 4 active TODOs: Seth BBS (Jun 12), Cosmology→SSRN, Bochum registration (May 30), Wave 2 outreach
- Inbox tasks pending evaluation: CIMCAI conference (May 29-31), Digital Minds Fellowship (Mar 27)

### 2026-02-26T~22:30+01:00 (Session 119) — WSL
**Goal:** Oizumi preprint review + Kanai follow-up + COGITATE triage
**Completed:**
- (no completed items recorded)
**Key Decisions:**
- (no decisions recorded)
**Recovery/Next session:**
1. Active TODOs are listed above — pick one to work on
2. Full backlog at `backlog.md` (read when active TODOs are done)
3. **IMPORTANT**: Always pull from BOTH remotes. Origin merge can delete private-only files. After origin merge, always `git diff --name-status HEAD private/main` to check for missing files.
4. push.sh now has divergence guard — if it aborts, run `git pull --rebase private main` first
5. bibtex MUST run with dangerouslyDisableSandbox (sandbox blocks .bbl writes)


### 2026-02-26T~22:00+01:00 (Session 118) — WSL
**Goal:** Git pull + resolve multi-remote divergence
**Completed:**
- Merged origin/main (3 commits from office sessions 116-117)
- Merged private/main (restored 16 pop-sci files incorrectly deleted by origin merge)
- All conflicts resolved, nothing lost
**Key Decisions:**
- Origin merges can silently delete private-only files — always verify against private/main after origin merge

