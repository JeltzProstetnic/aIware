<!-- Action: reference — demoted S298 2026-08-09. The finding is written, the fix is specified, and the
     remaining action belongs to cfg-agent-fleet, not aIware: apply the hook patch, add the behavioural test,
     assign CFG-xxx. aIware has nothing left to do and this file kept surfacing as ACT_PENDING because of it.
     Tracked-by: cfg-agent-fleet inbox item 2026-07-30 → CFG-xxx (to be assigned by a cfg session).
     Delete this file once cfg confirms the patch has landed. -->
# lrn audit — 2026-07-30 (aIware follower session, WSL)

## Incident
Session launched via `af` into a **follower worktree** (`/home/jeltz/.afleet-worktrees/aIware-20260730-181430`,
branch `afleet-wt-20260730-181430`) while another session held the main aIware checkout (`/home/jeltz/aIware` on `main`).
Startup did **not** announce follower mode; the agent opened with machine+persona and began the user's cover task.
The user had to state twice that a concurrent session was working the same project. `afd lock status aIware` → 404
(no AFD lock registered); SessionStart `additionalContext` carried **no** `SESSION_LOCKED`/`SESSION_LOCKED_REMOTE`.

## Finding
```
FINDING: A follower launched into a worktree gets no SESSION_LOCKED warning, so neither the
         user nor the agent learns a concurrent session owns the project.
ROOT CAUSE: Check 7b.4 keys follower detection on $PWD/.claude/.session-lock, but a worktree's
         $PWD is not the locked main-repo path, so it reads an empty lock, self-acquires, and
         writes role=leader — the reliable signal (CWD under .afleet-worktrees/) is never consulted.
FIX: In 07b-platform-env.sh Check 7b.4, when $PWD matches */.afleet-worktrees/*, emit the
     SESSION_LOCKED follower warning and write role=follower instead of acquiring the lock.
TARGET: cfg-agent-fleet global/hooks/checks/07b-platform-env.sh:106 (Check 7b.4)
TIER: hook (0 tokens)
```

## Why the fix is sound (no false positives)
`afleet.sh:294,301` (`_create_worktree_and_retarget`) creates a worktree under `.afleet-worktrees/`
**only** when `acquire_lock` fails (project already locked by another session) and the user picks
`[w] follower mode`; it then returns early, *skipping* lock acquisition. So a `.afleet-worktrees/` CWD
is *always* a follower workspace — the short-circuit cannot mislabel a legitimate leader.

## No global-rule change needed
Startup protocol step 0.5 already mandates surfacing every `SESSION_LOCKED` `additionalContext` item.
Once the hook emits it for worktree CWDs, the existing rule forces the announcement. The only gap is
the hook not emitting it.

## Proposed hook patch (cfg-agent-fleet session finalizes)
Guard the existing Check 7b.4 body:
```bash
if [[ "$PWD" == *"/.afleet-worktrees/"* ]]; then
    WARNINGS="${WARNINGS:+$WARNINGS | }SESSION_LOCKED: Running in an afleet follower worktree ($PWD) — a concurrent session owns the main checkout. FOLLOWER — load knowledge/follower-mode.md and follow it."
    write_role "$PWD" follower "${CC_SESSION_ID:-}" "${AFLEET_SESSION_ID:-}" 2>/dev/null || true
else
    # ... existing check_lock "$PWD" + case logic unchanged ...
fi
```
Add a **behavioral** test (`setup/tests/test-*.sh`, not a static config read — lrn Pattern 6):
run the check with `PWD` set to a `.afleet-worktrees/...` path and assert `SESSION_LOCKED` is emitted
and role=follower is written.

## Status
- [x] Finding written here (Action: act).
- [x] Routed to cfg-agent-fleet via `~/cfg-agent-fleet/cross-project/inbox.md` (2026-07-30).
- [ ] cfg-agent-fleet: apply hook patch + behavioral test, assign CFG-xxx, update this file's Tracked-by.
