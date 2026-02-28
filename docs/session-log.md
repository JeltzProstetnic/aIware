# Session Log

Full session history. Newest first. Never pruned.

### 2026-02-28T~evening — WSL
**Goal:** Quick check-in, no work done
**Completed:**
- Startup loading completed, verified clean state from Session 122
- Inbox items noted (CIMCAI + Digital Minds — not actioned)
**Key Decisions:**
- No decisions made this session
**Pending at shutdown:** Same as Session 122 end state
**Recovery/Next session:**
1. Active TODOs: Seth BBS (Jun 12), Cosmology→SSRN, Bochum registration (May 30), Wave 2 outreach
2. Inbox: CIMCAI conference (May 29-31) + Digital Minds Fellowship (Mar 27) still pending evaluation

### 2026-02-28T14:30Z — WSL
**Goal:** Compile 16 AC design PDFs + landscape overview document
**Completed:**
- Read inbox (CIMCAI + Digital Minds Fellowship items still pending — not addressed)
- Built landscape overview PDF: `docs/engineering/designs/pdf/00-design-overview-landscape.pdf`
- Built 16 individual design PDFs with simple + detailed Mermaid diagrams
- Color-coded IWM (blue), ISM (green), EWM (light grey/dark yellow stroke), ESM (red)
- Neutral Mermaid theme (grey subgraph backgrounds, not yellow)
- ASCII diagrams stripped from individual PDFs
- Build scripts: `tmp/build_design_overview.py` + `tmp/build_individual_pdfs.py`
- Dropped cfg-agent-fleet inbox task re: shareable Mermaid-to-PDF automation
- Cleaned up old redundant PDFs (00-comparison-overview, 16-quick-win-pseudo-ac)
**Key Decisions:**
- EWM color: light grey fill (#EAECEE) with dark yellow stroke (#B7950B) — user preference
- Mermaid theme: `neutral` (grey subgraph backgrounds) not `default` (yellowish)
- Base64-embedded images in HTML for weasyprint compatibility (file:// paths don't work)
- Designs 13-15 extracted from single `new-proposals-13-15.md` into individual PDFs
- Agent-created build scripts in `docs/engineering/designs/pdf/` can be deleted (superseded by unified `tmp/build_individual_pdfs.py`)
**Pending at shutdown:** Nothing from this session's scope
**Recovery/Next session:**
1. Design PDFs are DONE. All 17 files in `docs/engineering/designs/pdf/`
2. Backlog item "[P2] Compile 16 AC design PDFs" can be marked done
3. Inbox items still pending: CIMCAI conference eval, Digital Minds Fellowship eval
4. To rebuild: `python3 tmp/build_design_overview.py` (overview) or `python3 tmp/build_individual_pdfs.py` (individual)
5. Old agent build scripts to clean up: `docs/engineering/designs/pdf/build_design_pdfs.py`, `tmp/build_design_pdfs_13_16.py`

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


### 2026-02-26T~14:45+01:00 — the office (Fedora)
**Goal:** Fix git sync + handle André Sevenius reply
**Completed:**
- (no completed items recorded)
**Key Decisions:**
- Set upstream tracking to private/main (origin is a filtered mirror, private is the real remote)
- Reply to André: focused on falsifiability (Predictions 3+4), not on "is this correct" framing. Deliberately omitted 8-requirement comparison table — let him discover it.


### 2026-02-26T~09:00+01:00 (Session 116) — the office (Fedora)
**Goal:** Fix missing private remote on office machine
**Completed:**
- (no completed items recorded)
**Key Decisions:**
- (no decisions recorded)
