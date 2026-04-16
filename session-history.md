# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-04-16T10:30Z — WSL
**Goal:** AICE-26 attendance commitment reply to Steve Torrance
**Completed:**
- Discussed AICE-26 location and implications of acceptance
- Received Steve Torrance email requesting attendance commitment within 7 days
- Drafted and user sent reply confirming in-person paid delegate commitment if accepted
**Key Decisions:**
- Committed to attending AICE-26 in person as paid delegate if paper is accepted (reply to Torrance sent Apr 16)
**Pending at shutdown:** Nothing
**Recovery/Next session:**
Short session. All work complete. Torrance reply sent — await acceptance/rejection decision.

### 2026-04-16T09:30Z — WSL
**Goal:** Brief session — explain AISB-AICE2026 email, draft Wittmann reply, update tracking for German book completion
**Completed:**
- Explained AISB-AICE2026 email (Mar 4 Parthemore — administrative resubmission to OpenReview, not a decision)
- Drafted Wittmann reply (acknowledgment of Apr 6/9/15 emails, brief delay explanation)
- User sent Wittmann reply manually
- Updated correspondence/wittmann-werner.md with Messages 12-15 (Apr 6, 9, 15 from Wittmann + Apr 16 reply)
- Marked AIW-50 (German KDP publication) as done in backlog
- Deleted pending-german-book-review.md (review complete, book published)
**Key Decisions:**
- German book review confirmed complete, German book published (all 3 KDP editions)
- AISB-AICE2026: submission was already made to OpenReview (AIW-19 done in Session 157). The Mar 4 email was the original instruction. Follow-up sent Mar 30 — still awaiting decision.
**Pending at shutdown:** McFarnell reply draft still in Gmail (pending-mcfarnell-reply.md)
**Recovery/Next session:**
If session terminates: all tracking updated. Wittmann reply sent. Shutdown in progress.

### 2026-04-15T13:15Z — WSL
**Goal:** Publish German book (Die Simulation namens Ich) on KDP — all 3 formats
**Completed:**
- Fractal-Coda fix — reframed as recurring childhood dream (line 1859)
- Figure 3 rendered from German SVG → PNG via cairosvg
- EPUB build script: German trigger + German caption for figure3
- PDF build script: full German front matter (title, copyright, dedication, TOC heading "Inhalt")
- Chapter trigger `Kapitel 1:` — `\mainmatter` now activates, Arabic page numbering
- Backmatter (Coda/Danksagung/Anhang) → non-numbered chapters
- Anhang A/E TOC entries: em-dash subtitle split, short form for TOC/running header
- German hyphenation: tolerance=3000, emergencystretch=4em, 40+ manual \hyphenation hints
- Y/Z column types with `\hspace{0pt}` trick for tabularx hyphenation
- Convert_table_cell soft-hyphen dict (15+ stubborn compounds)
- `\tabcolsep=4pt` for tighter table padding
- Landscape tables: replaced pdflscape with `\rotatebox{90}{\begin{minipage}{7.25in}}` (KDP preflight-safe)
- Warum das Gehirn heading: line-break override
- Figure 2 grayscale B&W (PIL desaturate)
- pandoc EPUB reader: `-simple_tables-multiline_tables` to fix Der Autor→Kapitel 3 phantom-table bug
- Paperback ISBN 9798257520600 embedded (copyright page + wrap barcode)
- Hardcover ISBN 9798257524424 embedded (copyright page + wrap barcode)
- Upload kit `tmp/kdp-upload-de/` with metadata cheat-sheet
- Kindle eBook published on KDP
- Paperback published on KDP
- Hardcover published on KDP
**Key Decisions:**
- **KDP-free ISBNs** for both paperback and hardcover (Amazon exclusive, fastest path, matches English edition approach)
- **70% royalty + KDP Select** for Kindle eBook (€6.99 price point, KU inclusion for discovery on amazon.de)
- **Fractal Coda reframe** — dream frame instead of drug reference, hooks to Chapter 7 recurring childhood fractal dream (narrative coherence preserved)
- **Figure 2 grayscale via PIL** instead of proper SVG-level recoloring — acceptable for B&W print; revisit if muddy in physical proof
- **\rotatebox{90} over pdflscape** for landscape tables — KDP's preflight doesn't apply /Rotate 90 metadata when measuring margins, so pdflscape content appears 2"+ past page right edge. Rotatebox embeds rotated minipage within portrait frame → all content stays within page bounds.
- **\footnotesize default for German tables** (was \small for English) — German compounds require smaller font to fit narrow columns
- **Landscape detection by header** ('Wolfram-Klasse', 'Berechnet', 'Reduzierbar') + forced to rotatebox route
- **TOC em-dash suffix split** — Anhang A/E full title in chapter header, short form in TOC + running header
- **Translation metadata in KDP setup** — "This book is a translation" checkbox + all four sub-fields so Amazon auto-links to English edition on product pages within 2-14 days
**Pending at shutdown:** None — publication complete
**Recovery/Next session:**
All three German editions published and live on KDP. Paperback ISBN 9798257520600, hardcover ISBN 9798257524424. Files archived in `pop-sci/` (canonical) and `tmp/kdp-upload-de/` (upload kit with README + metadata cheat-sheet). Build scripts `tmp/build_book_{pdf,epub,cover}_de.py` fully German-localized and KDP-preflight-safe.

