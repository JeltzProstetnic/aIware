# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-02-27T19:50Z — WSL
**Goal:** Handle correspondence, restore Session 120 data loss, drop cfg inbox task
**Completed:**
- AISB reply: 300-word abstract drafted and sent to Torrance
- PsyArXiv v2 rejection noted, resubmission parked
- Restored scripts/ (5 files) and 7 other files deleted by Session 120
- Root cause identified: origin merge treated filtered state as deletions
- Added NEVER-merge-origin rule to CLAUDE.md
- Dropped P1 inbox task for cfg-agent-fleet: centralized push infra + branch-per-remote
**Key Decisions:**
- PsyArXiv v2 resubmission parked (accepted v1, rejected v2 for same title — absurd)
- Push script logic should be centralized in cfg-agent-fleet, per-project config only in repos
- Branch-per-remote architecture needed to structurally prevent origin merge disasters
**Recovery/Next session:**
1. cfg-agent-fleet inbox has the P1 push infrastructure task — pick up next cfg session
2. Waiting: NoC, Phil Psych, AISB (Mar 21), Bochum, Neurophenomenology, MetaLab
3. aIware inbox still has CIMCAI + Digital Minds Fellowship items (not addressed this session)

### 2026-02-27T19:45Z — WSL
**Goal:** Handle incoming correspondence, restore deleted scripts
**Completed:**
- AISB reply: drafted 300-word abstract, Gmail draft created, user sent it
- PsyArXiv v2 rejection noted — resubmission parked
- Restored scripts/ directory (5 files) deleted in Session 120
- Push script working again — origin now properly filtered
- Backlog and MEMORY.md updated
- Conversation log appended (Session 121)
**Key Decisions:**
- AISB 300-word abstract sent to Torrance. Awaiting acceptance by Mar 21.
- PsyArXiv v2 resubmission parked indefinitely (accepted v1, rejected v2 for "scope")
- scripts/ restored from pre-deletion commit (5187bae)
**Recovery/Next session:**
1. Waiting on: NoC, Phil Psych, AISB (Mar 21), Bochum, Neurophenomenology, MetaLab, 13+ outreach emails
2. Cross-project inbox has 3 unaddressed items: CIMCAI, Digital Minds Fellowship, filtered push (push issue now resolved)
3. Push script works — use `bash scripts/push.sh` for all future pushes

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

