# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-03-12T10:45Z — WSL
**Goal:** AICE-26 draft paper, correspondence, paper fixes
**Completed:**
- Built 8-page AICE-26 draft paper (LaTeX, anonymized, proper formatting)
- Fixed "real-time" → "ongoing"/"dynamically" in AICE draft
- Removed "will not emerge from scaling current systems" claim
- Fixed voice: "I present" → "This paper presents"
- Fixed Table 2 overflow (tabularx)
- Updated OpenReview submission fields file (added TL;DR)
- Drafted Joel Parthemore thank-you email (Gmail draft, threaded)
- Drafted Lukas Kob reply (Gmail draft, threaded, CC Marvan) — SENT by user
- Fixed "real-time" in full FMT paper (16 replacements) and NoC paper (11 replacements)
**Key Decisions:**
- Submit 8-page draft paper (not extended abstract) to AICE-26 — stronger for reviewers
- "Real-time" replaced with "ongoing"/"dynamically"/"continuously" across all three papers (AICE draft, full FMT, NoC trimmed)
- Removed claim that AC "will not emerge from scaling current systems" — we don't know what's being built
- Digital Minds Fellowship evaluated — recommended as P1 backlog item (deadline Mar 27)
**Pending at shutdown:** User needs to submit on OpenReview, send Joel email after submission
**Recovery/Next session:**
- AICE draft: `tmp/aice-draft-paper-anon.tex` / `tmp/aice-draft-paper-anon.pdf` (8 pages)
- OpenReview fields: `tmp/aice-openreview-fields.txt`
- Submission URL: https://openreview.net/group?id=aisb.org.uk/AISB/2026/AICE_Symposium

### 2026-03-10 18:36 — WSL
**Goal:** Check Joel Parthemore's AICE-26 reply, assess whether to send documents directly
**Completed:**
- Read Joel Parthemore's reply to AICE-26 OpenReview submission thread
- Assessed "send documents directly" option — recommended waiting for profile activation (~24h per Joel)
**Key Decisions:**
- **Don't email PDF directly to Joel yet.** His reply indicates profile approval within 24h, deadline is Mar 15 (5 days). Fallback: email PDF if still pending by Thursday Mar 12.
**Pending at shutdown:** OpenReview profile approval (check tomorrow Wed Mar 11)
**Recovery/Next session:**
- Check OpenReview login at https://openreview.net tomorrow
- If approved: upload `tmp/aice-extended-abstract-anon.pdf` immediately
- If still pending Thu Mar 12: email Joel the PDF directly
- Pending file `docs/pending-aice-submission-guide.md` still active — has all submission details

### 2026-03-10 17:35 — WSL
**Goal:** Fix tmp/ warning — create drafts/ convention, move draft files, route reference papers to DMS
**Completed:**
- Investigated config-check.sh tmp/ warning (Check 15 flags build artifacts as documents)
- Created `drafts/` directory for persistent draft content
- Moved 5 draft files from tmp/ to drafts/ (kanai-response, nilsen-response, kdp-marketing-playbook, cover-letter-noc-resubmission, editor-reply-andrillon)
- Added `drafts/` to .push-filter.conf (excluded from public remote)
- Posted DMS intake inbox task for 3 reference papers (oizumi-kanai, kob-marvan, mcfarnell)
**Key Decisions:**
- `drafts/` is the new standard directory for content awaiting user action (emails, cover letters, response drafts). `tmp/` remains throwaway only.
- Reference papers collected for citation go to DMS, not project tree.
- Global `drafts/` convention tracked in cfg-agent-fleet inbox (line 123) — config-check.sh fix, template update, CLAUDE.md rule all pending there.
**Pending at shutdown:** Nothing
**Recovery/Next session:**
- Short session, no complex state. Next session should present pending-aice-submission-guide.md per its Action: present header.

