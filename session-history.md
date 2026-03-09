# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-03-09 19:48 — WSL
**Goal:** Quick tracking task — add ResearchGate paper to backlog
**Completed:**
- Added AIW-25 to backlog: "Affective Control under Uncertainty — A Two-Level Theory of Consciousness" (ResearchGate, P3)
- Reviewed inbox items, surfaced time-sensitive items to user
**Key Decisions:**
- Paper tracked as P3 (evaluate later, no urgency)
**Pending at shutdown:** Nothing — minimal session
**Recovery/Next session:**
No recovery needed. Clean session.

### 2026-03-06 18:50 — WSL
**Goal:** German A+ Content for KDP + German book manuscript revision + book PDF/DOCX builds
**Completed:**
- Created German A+ Content (5 modules, all images, preview HTML)
- German bubble diagram SVG created (figure2-real-virtual-split-simple-de.svg)
- German comparison table image rendered
- Opus agent completed full German manuscript review (18 edits)
- Manual corrections: reverted knockout passage, restored Bernhard's name, varied "Originalbeitrag" repetition
- Recovered build_book_pdf.py from git history, created German variant (build_book_pdf_de.py)
- Built book-manuscript-de.pdf (1.1 MB, US Trade 6x9)
- Built book-manuscript-de.docx for text review phase
- AIW-11b marked done (German quality pass complete)
- AIW-21 marked done (content changes — drugs, Bernhard, Metzinger)
- AIW-24 created (translate remaining figures to German)
- English A+ Content updated (Metzinger removed from author bio)
**Key Decisions:**
- **Metzinger rule**: Don't promote or name-drop Metzinger in marketing/public-facing materials. Academic citations stay, promotional language removed.
- **German translation analogy style**: Adapt analogies for German audience — experiential beats technical (e.g., "Spielfigur fühlt Schmerzen" > "Rendering-Engine")
- **Knockout passage stays first-person**: Author's direct experience of being knocked unconscious is rhetorically powerful, stays as-is
- **Bernhard Glück**: Name stays, specific roasting examples removed
- **Review workflow**: .docx for text review phase, switch to PDF when text is finalized for layout review
- **A+ Content approved**: English version auto-approved by Amazon. German version prepared, ready for submission.
**Pending at shutdown:** Nothing
**Recovery/Next session:**
- German A+ Content files in tmp/: a-plus-content-de.txt, a-plus-preview-de.html, a-plus-comparison-de.png, a-plus-bubble-square-de.png
- Book build: `python3 tmp/build_book_pdf_de.py --edition us` (PDF) or pandoc command for .docx
- .docx build: `pandoc pop-sci/book-manuscript-de.md -o pop-sci/book-manuscript-de.docx --from markdown-yaml_metadata_block --to docx --toc --standalone --resource-path=/home/jeltz/aIware/pop-sci:/home/jeltz/aIware`

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

