# Session History

Rolling window of the last 3 sessions. Newest first.

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

### 2026-03-10 15:15 — WSL
**Goal:** AICE-26 OpenReview follow-up email
**Completed:**
- Reviewed AICE-26 pending file and email thread with Parthemore
- Drafted follow-up email to Parthemore: OpenReview registration not activated, cannot log in, asks for expedited activation or direct PDF submission as fallback
- User sent previous draft (less urgent wording) before this one was ready — new draft (r-5716405074959201769) still in Gmail drafts, can be sent as follow-up or deleted
**Key Decisions:**
- OpenReview profile still not activated — user literally cannot log in. Deadline March 15.
**Pending at shutdown:** Nothing
**Recovery/Next session:**
Previous draft was sent. New stronger-worded draft still in Gmail drafts — user can send or delete.

### 2026-03-10 14:00 — WSL
**Goal:** AICE-26 OpenReview submission support
**Completed:**
- Found existing AICE-26 materials (abstract, anonymized PDF from Session 151)
- Reviewed Gmail thread with Parthemore (3 messages)
- User created OpenReview profile (Uni Vienna without end date as workaround — Ivoclar/independent not selectable)
- Follow-up email to Parthemore sent (transparent about affiliation workaround)
- Submission guide prepared for user (form fields, URL, PDF location)
**Key Decisions:**
- Transparency with Parthemore about OpenReview institutional affiliation workaround
- User handles OpenReview submission manually (not via browser automation)
**Pending at shutdown:** User rebooting, will complete submission next session
**Recovery/Next session:**
Pending file `docs/pending-aice-submission-guide.md` (Action: present) has the full submission guide. Present it at next session start.

