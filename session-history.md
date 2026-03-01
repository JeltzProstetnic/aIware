# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-03-01T22:30Z — WSL
**Goal:** Compare mirror-box README ASCII diagram with AC design PDF diagrams, decide on diagram standardization
**Completed:**
- Explored mirror-box project for diagram files (all ASCII art, no rendered diagrams)
- Extracted and examined AC design documentation PDFs (17 PDFs, WeasyPrint from Mermaid→PNG→HTML)
- Compared PDF diagrams (simple + detailed) with README ASCII art — neither is 1:1 match
- Opened PNG diagrams for user to visually inspect
- User decided: ASCII diagram is the most human-readable, should be the canonical "simple" level
- Tracked mirror-box task: replace ASCII with Mermaid block using PDF colors (cross-project inbox)
- Tracked AIW-15: redesign all "simple" PDF diagrams to match README clarity level
**Key Decisions:**
- The mirror-box README ASCII architecture diagram is the gold standard for human readability — all "simple" diagrams should target this level of detail
- README diagram will use Mermaid ```mermaid block (option 2) with PDF color scheme, not a PNG image
- New backlog item AIW-15 (P3) for redesigning simple diagrams across all 16 AC design PDFs
**Pending at shutdown:** Nothing
**Recovery/Next session:**
1. Tasks tracked — no immediate follow-up needed
2. Mirror-box Mermaid replacement: write a new .mmd that matches the README ASCII flow exactly, using style directives for PDF colors
3. AIW-15: review each design's simple diagram against the README's clarity standard

### 2026-03-01T22:50Z — WSL
**Goal:** Launch Mirror Box web UI for screenshot, fix environment issues
**Completed:**
- Launched Mirror Box web chat UI (Mistral-7B FP16 on RTX 4090)
- Fixed missing deps: fastapi, uvicorn[standard] not installed in fresh venv
- Added setup.sh to mirror-box (one-command env bootstrap)
- Added [web] extra to pyproject.toml (fastapi + uvicorn[standard])
- Added AI-first launch rule to mirror-box CLAUDE.md (auto-open browser)
- Copied dashboard screenshot to docs/dashboard-screenshot.png
- Updated README.md with screenshot, simplified install, web UI docs
- Committed and pushed mirror-box to GitHub (rebased on Steam Deck Unicode diagram commit)
**Key Decisions:**
- mirror-box venv was fresh (Feb 28 repo split) and missing web deps — root cause was no setup.sh
- Added `uvicorn[standard]` not just `uvicorn` — bare uvicorn has no WebSocket library
- AI-first rule: always auto-open browser when launching web UIs, never just print URLs
**Pending at shutdown:** None
**Recovery/Next session:**
1. Mirror Box web UI was stopped after screenshot
2. All changes committed and pushed to origin/main
3. Inbox tasks for aIware NOT processed this session (quick session, screenshot only)

### 2026-03-01T20:45Z — WSL
**Goal:** Send AC design documentation to Bernhard Glück
**Completed:**
- Opened AC design overview landscape PDF
- Zipped all 17 design PDFs (overview + 16 architectures, 3.7 MB)
- Sent zip to bernhard.glueck@aitive.at via Gmail (from matthias@matthiasgruber.com)
- Sent FMT engineering specification PDF (62 KB) to same recipient
**Key Decisions:**
- Sent from matthias@matthiasgruber.com alias (not jeltz.prostetnic@gmail.com)
- Included all 17 PDFs in zip (overview + designs 01-16)
- FMT implementation spec sent as separate email for clarity
**Pending at shutdown:** None
**Recovery/Next session:**
1. Both emails sent successfully (Message IDs: 19caaece69c4cdb0, 19caaf92514db256)
2. No follow-up actions needed unless Bernhard replies

