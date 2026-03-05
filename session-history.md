# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-03-05 — WSL
**Goal:** Hardcover cover subtitle fix + German book revision tracking
**Completed:**
- Fixed hardcover cover subtitle position — moved up 0.25in in `pop-sci/cover-wrap-hc.tex` (y: 7.5085 → 7.7585) to avoid overlap with image
- Rebuilt `pop-sci/cover-wrap-hc.pdf` — user confirmed fix looks correct
- Added AIW-20 to backlog: upload updated cover to KDP/Amazon
- Added AIW-21 to backlog: German book content revisions (no drug self-reports, less autobiographical, cut Glück roasting examples)
**Key Decisions:**
- Subtitle shift of 0.25in (one line at 18pt leading) confirmed as correct by user
- German book revision scoped to 3 specific content issues (AIW-21)
**Pending at shutdown:** Nothing
**Recovery/Next session:**
Cover fix is local only — needs KDP upload (AIW-20). Check paperback/EU variants for same subtitle-image overlap issue during that task.

### 2026-03-05 19:20 — WSL
**Goal:** Gmail triage, NoC table fix, inbox notifications
**Completed:**
- Gmail inbox triaged (10 messages, 3 days)
- NoC NCONSC-2026-071 unsubmission identified — tables dropped by pandoc
- Fixed build script: tabularx→tabular preprocessing + explicit Table N. captions + .csl copy
- Verified all 4 tables present in rebuilt .docx
- Committed and pushed fix to private remote
- Cross-project inbox: ivoclar notified about ECHA AI support email
- Cross-project inbox: cfg-agent-fleet notified about proposed global Gmail de-duplication rule
- Cross-project inbox: cfg-agent-fleet notified about VPS maintenance Mar 9
- Cross-project inbox: Updated NoC tracking item with unsubmission details
**Key Decisions:**
- Gmail de-duplication rule proposed as GLOBAL (all projects), not aIware-specific — user confirmed "all projects must be able to deal with gmail and other communication channels to a degree"
- Root cause of NoC unsubmission: pandoc silently drops complex tabularx tables. Fix: preprocess .tex before pandoc (tabularx→tabular, add Table N. prefixes)
- Build script also fixed to copy .csl files (APA style was missing from .docx builds)
**Recovery/Next session:**
- NoC resubmission: run `python3 tmp/build_noc_pdf.py --docx` on any machine (fix is committed to private), upload `tmp/noc-paper.docx` to ScholarOne
- André Nilsen email in inbox is ALREADY HANDLED (Sessions 137-138) — do not re-process

### 2026-03-05 13:45 CET — WSL
**Goal:** Learn from user edits to Nilsen + Kanai email drafts, calibrate email drafting rules
**Completed:**
- Retrieved sent Nilsen + Kanai emails from Gmail, compared against draft versions in tmp/
- Identified 7 corrections across both emails
- User corrected my analysis: Nilsen congratulations removal was about not repeating (already congratulated one day early), not a style preference
- User rejected 4 of 7 proposed rules (C, E, F, G), approved 3 (A, B, D)
- Added 3 approved rules to CLAUDE.md Communication Rules section
- Reverted premature rule writes to MEMORY.md and memory/email-drafting-rules.md
- Posted 2 inbox tasks: communications KB (near people management) + meta-rule (rule changes require user consent)
- Inbox task for email learning marked done
**Key Decisions:**
- Email drafting rules: only 3 of 7 proposed rules approved (check comms log, hedge presumptions, don't re-explain)
- Communications log/KB belongs near people management (life-management domain), not in project memory
- Rule changes require user consent before persisting — posted as proposed global rule to cfg-agent-fleet inbox
- Rules do NOT belong in auto-memory (MEMORY.md) — they go in CLAUDE.md or knowledge files
**Pending at shutdown:** None
**Recovery/Next session:**
- No pending work. Two cfg-agent-fleet inbox tasks awaiting pickup by that project.
- Communications KB doesn't exist yet — will be created by cfg-agent-fleet session.

