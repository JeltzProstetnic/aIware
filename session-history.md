# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-03-06 16:30 — WSL
**Goal:** KDP A+ Content upload — guide user through module selection and image preparation
**Completed:**
- Loaded previous session handoff (docs/pending-a-plus-kdp.md)
- Rewrote a-plus-content.txt with proper copy-paste formatting (no hard wraps, no leading spaces)
- Mapped 5 modules to KDP template types
- Module 1: Standard Image & Light Text Overlay (hero banner, 300 char body)
- Module 2: Standard Single Left Image — cropped bubble diagram to square via white padding (2340x2340)
- Module 3: Standard Text — "What You Will Discover" bullet list
- Module 4: Comparison table rendered as image (HTML→PNG, 3750x1241) — workaround for KDP's ASIN-only comparison chart. Compares vs Seth, Dehaene, Tononi.
- Module 5: Standard Single Right Image — author photo + bio
- Added alt text for all images (~100 chars each)
- All content submitted to KDP for review
**Key Decisions:**
- KDP comparison chart requires ASINs of own brand only — replaced with image-based comparison table rendered from HTML
- Used text overlay template for comparison image (wide aspect ratio, no padding needed)
- Module 1 body trimmed to 300 chars for overlay template limit
**Pending at shutdown:** Amazon review (~7 business days)
**Recovery/Next session:**
- A+ Content submitted. No action needed until Amazon review completes.
- If rejected, comparison image is the most likely flag — fallback: replace Module 4 with Standard Text.
- All source files in tmp/: a-plus-content.txt, a-plus-hero-banner.png, a-plus-bubble-square.png, a-plus-comparison.png, a-plus-comparison.html, a-plus-author-photo.jpg

### 2026-03-06 13:55 — WSL
**Goal:** Create A+ Content for KDP book listing and guide through publishing
**Completed:**
- Read marketing playbook and book manuscript for context
- Drafted 5 A+ Content modules (hero banner, bubble diagram, what you'll discover, comparison chart, about author)
- Prepared hero banner image from ultra-wide cover art (9112x2560 → 1940x600)
- Prepared author photo (resized to 600x600)
- Created HTML visual preview of all 5 modules (`tmp/a-plus-preview.html`)
- User reviewed preview — "looks good"
- Saved author photo path to MEMORY.md (`/mnt/c/Users/Matthias/Pictures/1749406479497.jpg`)
**Key Decisions:**
- 5 modules chosen: hero banner (ultra-wide art), bubble diagram (left image), text discovery list, comparison chart (FMT vs IIT vs GNW), author bio (right image with photo)
- Author photo canonical path established: `/mnt/c/Users/Matthias/Pictures/1749406479497.jpg`
- Comparison chart uses 3 columns (FMT vs IIT vs GNW) — KDP charts have limited columns
**Recovery/Next session:**
All A+ Content artifacts are in `tmp/`:
- `tmp/a-plus-content.txt` — full text copy for all 5 modules (paste into KDP)
- `tmp/a-plus-preview.html` — visual HTML preview (open in browser to review)
- `tmp/a-plus-hero-banner.png` — prepared hero image (1940x600)
- `tmp/a-plus-author-photo.jpg` — prepared author photo (600x600)
Bubble diagram: use `figures/figure2-real-virtual-split-simple.png` directly.
Next session: user just needs to open KDP A+ Content Manager and follow the step-by-step in `tmp/a-plus-content.txt`.

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

