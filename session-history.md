# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-03-06 12:45 — WSL
**Goal:** Build comprehensive book marketing campaign for English pop-sci book
**Completed:**
- Launched 4 parallel research agents (market analysis, KDP tools, content channels, campaign strategy)
- All 4 agents returned with comprehensive findings
- Consolidated into `docs/book-marketing-campaign.md`
- Cross-project inbox task posted for social project (podcast pitching, Substack, Twitter, media kit)
**Key Decisions:**
- User has 30 author copies + early positive feedback ("really good", "polished")
- Book confirmed live on Amazon, exclusive for ~6 months
- Asking researchers for pop-sci endorsements = bad idea; target podcasters/reviewers/communicators instead
- Send physical copies to podcast hosts with pitches
- Budget: EUR 300-500/month, must show ROI
- Podcast pitching handled in social project
- Amazon metadata optimization (#3) and Author Central/Goodreads (#4) = next session actions
**Pending at shutdown:** Execute Amazon metadata optimization (categories, keywords, pricing) + Author Central / Goodreads setup in next session
**Recovery/Next session:**
- Full campaign plan: `docs/book-marketing-campaign.md`
- Social project inbox task covers podcast/Substack/Twitter strategy
- User approved items 3 (Amazon optimization) and 4 (Author Central + Goodreads) for execution

### 2026-03-06 11:28 — WSL
**Goal:** Update hardcover book cover on KDP (AIW-20)
**Completed:**
- Located ultimate upscale source artwork (9112×2560) on Windows Pictures folder
- Persisted source to `figures/art-consciousness-ultimate-upscale.png`
- Rebuilt `cover-wrap-hc.tex` with TikZ clip, height=9.6in, shifted right for eye composition
- Uploaded to KDP and published
- Marked AIW-20 done in backlog
- Restored accidentally overwritten `cover-wrap-hc.jpg` from git
**Key Decisions:**
- Used ultimate upscale source (9112×2560) instead of pre-cropped derivatives — gives full composition control
- TikZ clip approach: scale image to 9.6in height (tiny black bands within 0.51" wrap zone = invisible), shift node to x=3.5in to frame eye at top-right
- Black borders confirmed invisible on physical hardcover (fold-under covered by white paper)
- Paperback cover left unchanged (user confirmed it's perfect)
- EU cover variants not yet checked for same issue
**Pending at shutdown:** Nothing
**Recovery/Next session:**
Session complete. No pending work.

### 2026-03-06 10:20 — WSL
**Goal:** Repair and resubmit NoC paper (NCONSC-2026-071)
**Completed:**
- Opened ScholarOne submission portal
- Verified build script fix (tabularx→tabular preprocessing) works correctly
- Rebuilt .docx with `python3 tmp/build_noc_pdf.py --docx` — all 4 tables present, captions at top
- Updated resubmission kit (`tmp/noc-resubmission/manuscript.docx`)
- Reviewed .docx in Word — tables verified
- Decided NOT to add Wada content to trimmed version (word count, scope creep, submission stability)
- Fixed Metzinger opposed reviewer reason to professional framing (conflict of interest, not personal)
- User submitted on ScholarOne — NCONSC-2026-071 resubmitted
**Key Decisions:**
- Wada procedure content stays in full paper only, not added to NoC trimmed version (word count limit, scope creep risk, submission already bounced twice)
- Metzinger opposition reason reworded from personal to professional (competing theory conflict of interest)
**Pending at shutdown:** None
**Recovery/Next session:**
NoC resubmission complete. Next: wait for editorial acknowledgment. Track under NCONSC-2026-071.

