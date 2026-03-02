# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-03-03T14:30Z — WSL
**Goal:** AIW-15 diagram redesign + Gmail check + inbox processing
**Completed:**
- AIW-15: Redesigned all 16 simple Mermaid diagrams in `tmp/build_individual_pdfs.py` — LR→TD flow, subgraph grouping, shortened labels, visible self-ref loops
- Increased render height 600→900px for TD layouts
- Fixed Design 16 empty first page (max-height constraint + page-break override)
- Fixed Design 15 B&W/confusing (added explicit IWM/ISM/EWM/ESM nodes with colors, simplified arrows)
- Rebuilt all 16 PDFs, verified no empty-page issues across all designs
- Checked Gmail: MetaLab Summer School application acknowledged (Sarah Kalwarowsky, UCL, Mar 2)
- Updated backlog: AIW-15 done, MetaLab status updated, TSC+AAAI added to AIW-06
- Processed 4 aIware inbox items (cleared from cross-project inbox)
- Nilsen congratulatory email already sent by user
**Key Decisions:**
- Subgraph labels kept short (~15 chars) to avoid truncation in Mermaid rendering
- Design 15 restructured to show four models explicitly (instead of abstract SNN/LLM-only nodes) for color and clarity
- Overview images constrained to max-height 150mm to prevent page overflow on designs with tall diagrams
**Pending at shutdown:** None
**Recovery/Next session:**
1. AIW-15 is complete. All 16 design PDFs regenerated in `docs/engineering/designs/pdf/`
2. Build script is `python3 tmp/build_individual_pdfs.py` — regenerates all .mmd, .png, and .pdf files
3. Next priorities: AIW-16 (Digital Minds Fellowship, deadline Mar 27), AIW-17 (McFarnell SMRI feedback), AIW-01 (Seth BBS commentary)

### 2026-03-02 — WSL
**Goal:** Process open TODOs, inbox tasks, prepare Wave 2 outreach, backlog housekeeping
**Completed:**
- AIW-02: Verified session-context.md + MEMORY.md persist correctly — closed as resolved
- Backlog split: older Done items archived to `docs/backlog-archive.md`
- AIW-11 split into AIW-11a (English, P3) + AIW-11b (German, P1)
- AIW-08 downgraded to P4 (endorsement unlikely without affiliation)
- Inbox: 7 aIware items processed — CIMCAI declined (travel), AAAI declined (travel), Digital Minds Fellowship added as AIW-16, McFarnell feedback added as AIW-17, RIM preprint v2 target added as AIW-18, Torrance/Nilsen verified sent, backlog split done
- AIW-05 Wave 2 outreach: 8 Gmail drafts created with PDF attachments, all sent by user
- Contacts.md updated (8 entries flipped to Contacted, Carhart-Harris + Priesemann added)
- Engagement log updated with all 8 outreach emails
- Nilsen PhD defense congratulations draft created (defense Mar 3)
- Strategy file updated: CIMCAI + AAAI added to Passed/Declined
**Key Decisions:**
- CIMCAI (Berkeley) and AAAI (Burlingame): declined — won't self-fund US travel per stance
- Digital Minds Fellowship (Cambridge, Aug 3-9): recommended apply — fully funded, exact research domain, added as P1
- AIW-08 arXiv: downgraded P3→P4, endorsement unlikely without institutional affiliation
- Wave 2 outreach: all 8 targets contacted same day (email first per strategy rules)
- AIW-15 diagram redesign: deferred to next session, prototype designs 15+16 only
**Recovery/Next session:**
1. Check Gmail drafts — Nilsen congratulations may still be unsent
2. Monitor 8 Wave 2 emails for replies (~2 weeks)
3. Next session: AIW-15 diagram prototype (designs 15+16), read mirror-box README for target clarity
4. Digital Minds Fellowship application needs attention before Mar 27
5. McFarnell SMRI feedback still needs drafting (read his ACU preprint first)

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

