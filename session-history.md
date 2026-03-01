# Session History

Rolling window of the last 3 sessions. Newest first.

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

