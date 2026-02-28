# Session History

Rolling window of the last 3 sessions. Newest first.

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

