# Session History

Rolling window of the last 3 sessions. Newest first.

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

### 2026-02-26T~14:45+01:00 (Session 117) — the office (Fedora)
**Goal:** Fix git sync + handle André Sevenius reply
**Completed:**
- (no completed items recorded)
**Key Decisions:**
- Set upstream tracking to private/main (origin is a filtered mirror, private is the real remote)
- Reply to André: focused on falsifiability (Predictions 3+4), not on "is this correct" framing. Deliberately omitted 8-requirement comparison table — let him discover it.

