# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-03-01T~20:30Z — WSL
**Goal:** Quick session — process feedback on inbox handling, drop cfg-agent-fleet tasks
**Completed:**
- Startup, pulled from private (already up to date)
- User identified missed mirror-box inbox task — parent projects should flag child project tasks
- Incorrectly edited global CLAUDE.md directly — user corrected, reverted commit
- Dropped 3 cfg-agent-fleet inbox tasks: parent-child rule, statusline persona, colored persona text
**Key Decisions:**
- Cross-project edits go through inbox, even for cfg-agent-fleet (system project exception doesn't mean "edit freely")
- Parent projects should flag child project inbox tasks at session start
**Pending at shutdown:** Nothing
**Recovery/Next session:**
1. Nothing pending — clean shutdown
2. cfg-agent-fleet has 3 new inbox tasks to process next session

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

