# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-03-06 12:55 — WSL
**Goal:** Book marketing campaign Phase 0 — Amazon listing optimization
**Completed:**
- Verified Amazon listing — all 3 formats LIVE and searchable (but not yet indexed by Google)
- Updated paperback description with Amazon-optimized HTML (`tmp/amazon-description.html`)
- Updated paperback categories: AI/Neural Networks, Cognitive Psychology, Neurology
- Updated paperback keywords (7 slots from campaign plan)
- Paperback pricing confirmed at $19.80 ($7.87 royalty)
- Kindle pricing at $5.00/35% — user wants to investigate 70% tier disadvantages before switching
- Hardcover at $29.00 — in review (cover image), can't edit description/categories/keywords yet
- Goodreads: user has login but can't remove wrongly attributed books or claim authorship easily
- ResearchGate: exists, active. Google Scholar: exists, up to date.
- Created backlog items: AIW-22 (Phase 0 remaining), AIW-23 (PhilPapers)
- Prepared A+ Content guidance — bubble diagram 2340x1680 ready, explained where to find A+ in Author Central
- Amazon Ads: explained "reviews first, ads second" — need 5+ reviews before spending on ads
**Key Decisions:**
- Pricing strategy: cheap Kindle ($5) for reach → paperback ($19.80) for revenue → hardcover ($29) for premium. User prefers this over uniform pricing.
- Amazon Ads deferred until 5+ reviews exist (campaign plan guidance)
- PhilPapers tracked as high priority but deferred to a later session
- Additional academic platforms (beyond ResearchGate + Scholar) deferred — low ROI so far
**Pending at shutdown:** Hardcover description/categories/keywords (blocked on cover review), Kindle 70% pricing decision, A+ Content creation, PhilPapers profile, BookSirens/Reedsy for review seeding
**Recovery/Next session:**
- Campaign plan: `docs/book-marketing-campaign.md`
- KDP action checklist: `tmp/kdp-phase0-checklist.md`
- Amazon description HTML: `tmp/amazon-description.html`
- Backlog items AIW-22 and AIW-23 track remaining Phase 0 + PhilPapers

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

