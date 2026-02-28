# Session Context

## Session Info
- **Last Updated**: 2026-02-28T14:30Z
- **Machine**: WSL
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Compile 16 AC design PDFs + landscape overview document

## Current State
- **Active Task**: Design PDF compilation — COMPLETE
- **Progress** (use `- [x]` checkbox for each completed item):
  - [x] Read inbox (CIMCAI + Digital Minds Fellowship items still pending — not addressed)
  - [x] Built landscape overview PDF: `docs/engineering/designs/pdf/00-design-overview-landscape.pdf`
  - [x] Built 16 individual design PDFs with simple + detailed Mermaid diagrams
  - [x] Color-coded IWM (blue), ISM (green), EWM (light grey/dark yellow stroke), ESM (red)
  - [x] Neutral Mermaid theme (grey subgraph backgrounds, not yellow)
  - [x] ASCII diagrams stripped from individual PDFs
  - [x] Build scripts: `tmp/build_design_overview.py` + `tmp/build_individual_pdfs.py`
  - [x] Dropped cfg-agent-fleet inbox task re: shareable Mermaid-to-PDF automation
  - [x] Cleaned up old redundant PDFs (00-comparison-overview, 16-quick-win-pseudo-ac)
- **Pending**: Nothing from this session's scope

## Key Decisions
- EWM color: light grey fill (#EAECEE) with dark yellow stroke (#B7950B) — user preference
- Mermaid theme: `neutral` (grey subgraph backgrounds) not `default` (yellowish)
- Base64-embedded images in HTML for weasyprint compatibility (file:// paths don't work)
- Designs 13-15 extracted from single `new-proposals-13-15.md` into individual PDFs
- Agent-created build scripts in `docs/engineering/designs/pdf/` can be deleted (superseded by unified `tmp/build_individual_pdfs.py`)

## Recovery Instructions
1. Design PDFs are DONE. All 17 files in `docs/engineering/designs/pdf/`
2. Backlog item "[P2] Compile 16 AC design PDFs" can be marked done
3. Inbox items still pending: CIMCAI conference eval, Digital Minds Fellowship eval
4. To rebuild: `python3 tmp/build_design_overview.py` (overview) or `python3 tmp/build_individual_pdfs.py` (individual)
5. Old agent build scripts to clean up: `docs/engineering/designs/pdf/build_design_pdfs.py`, `tmp/build_design_pdfs_13_16.py`
