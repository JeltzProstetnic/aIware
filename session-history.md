# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-02-27T19:30Z — WSL
**Goal:** Handle incoming correspondence (AISB reply, PsyArXiv v2 rejection)
**Completed:**
- AISB reply from Steve Torrance — reviewed, drafted 300-word short abstract, created Gmail draft reply, user sent it
- PsyArXiv v2 rejection of intelligence paper — noted, v2 resubmission parked
- Backlog updated (AISB added to Waiting table)
- MEMORY.md updated (PsyArXiv v2 rejection recorded)
- Cross-project inbox items read (CIMCAI, Digital Minds Fellowship, filtered push — not acted on this session)
**Key Decisions:**
- AISB 300-word abstract sent to Steve Torrance (sbtorrance@outlook.com). Conference is University of Sussex, 1-2 July 2026. Remote presentation conditional on review score.
- PsyArXiv v2 resubmission PARKED — they rejected an update to an already-accepted preprint citing "outside scope." Third scope-based rejection for intelligence paper.
**Recovery/Next session:**
1. AISB: awaiting acceptance notification by Mar 21, 2026
2. PsyArXiv v2: parked indefinitely. v1 still live at https://osf.io/preprints/osf/kctvg
3. Cross-project inbox has 3 pending items not addressed this session (CIMCAI, Digital Minds Fellowship, filtered push)

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


