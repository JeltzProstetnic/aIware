# Session History

Rolling window of the last 3 sessions. Newest first.

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

### 2026-04-14T13:57Z — DESKTOP-32ILURB
**Goal:** German book review complete + full KDP publication asset build (ebook, paperback, hardcover)
**Completed:**
- Startup checklist (run late after user correction — lrn audit filed)
- German book review Kap 11–16 + Anhang B/E: ~30 user-flagged issues fixed (sentence fragments, calques, word order, reflexive verbs, meta-commentary removal, Bernhard reference dropped, Real/Virtual→Virtuell)
- Sub-agent anglicism sweep Kap 1–10 applied: 82 en-dash spacing fixes, Level→Ebene drift, re-glossed technical terms removed, Zusatzfeature→Zusatzfunktion
- v10 docx built, scanned for inline marks (none — user flagged issues in chat instead)
- Book interior rebuilt: `book-manuscript-de.pdf` (269 pages, 6×9 paperback)
- Hardcover interior built: `book-manuscript-de-hc.pdf`
- German-specific cover build script written: `tmp/build_book_cover_de.py` (derived from English, German title/subtitle/blurb/Kindle alt-text)
- German EPUB build script written: `tmp/build_book_epub_de.py` (German metadata, de language, German figure map, YAML metadata block parsing disabled to avoid mid-doc `---` collision)
- Paperback wrap built: `cover-wrap-de.pdf` (spine 0.606")
- Hardcover wrap built: `cover-wrap-hc-de.pdf` (case laminate 14.370×10.417)
- Paperback front built: `cover-front-de.pdf`
- Kindle front cover built: `cover-kindle-de.jpg` (1600×2560, EXIF alt text)
- Kindle EPUB built: `book-manuscript-de.epub` (3.0 MB, 4 German figures embedded)
- aIware CLAUDE.md fixed: `scripts/push.sh` reference → `~/cfg-agent-fleet/setup/scripts/filtered-push.sh` (retired script was still documented)
- lrn findings filed to cfg-agent-fleet inbox (4 items): PreToolUse startup gate hook, rule against unilateral tracking-file reconciliation, SessionStart hook conversation-log session-gap warning, infrastructure-retirement doc-coherence check
- Backlog entry AIW-50 added for tomorrow's KDP upload
**Key Decisions:**
- **German book ready for publication.** All three editions (ebook, paperback, hardcover) have build artifacts committed. Upload scheduled tomorrow pending German ISBN decision.
- **German ISBN decision PENDING** — wraps built with `[TBD-DE-PB]`/`[TBD-DE-HC]` placeholders, no barcode. User needs to decide KDP-free vs bought ISBNs before upload. Build scripts ready to regenerate with real values.
- **Back cover blurb approved:** "Das Ich ist eine Simulation…" (in `tmp/build_book_cover_de.py` BACK_COVER_BLURB, also Kindle EXIF alt text and metadata description).
- **Figure 3 (phenomenological content) is NOT in German EPUB** — only SVG exists for German, no rendered PNG. Either render before KDP upload or accept the gap (one figure of four).
- **Data integrity cascade lesson:** Session 183 wrote three contradictory review-position self-reports (commit msg / pending file / session-context). Session 185 initially trusted the wrong line and corrupted the pending file further. Fixed after user correction. Filing: global rule proposed against unilateral tracking-file reconciliation (cfg inbox).
- **Push script discovery lesson:** aIware CLAUDE.md pointed to retired `scripts/push.sh`. Fixed locally + filed process-rule proposal to cfg inbox (infrastructure retirements should scan all project CLAUDE.md files for stale references in the same commit).

### 2026-03-19T12:30Z — WSL
**Goal:** Gmail triage, FMT wiki content production (100 pages), Wittmann co-author outreach
**Completed:**
- Gmail triage — 10 inbox messages processed, 2 Bartl mail ingested+trashed
- PLREV rejection noted, AIW-07 updated → NBSR next
- Perplexity/Ivoclar routed to ivoclar inbox
- Stewart papers evaluated (shallow convergence, archived)
- Blog inbox item confirmed (already exists for social)
- Wiki structure defined — 100 articles across 18 sections (`docs/wiki-structure-proposal.md`)
- Style guide created (`wiki/STYLE-GUIDE.md`) with SEO, AI optimization, Zenodo link-back
- Infrastructure spec created (`wiki/INFRASTRUCTURE-SPEC.md`) — MkDocs config, robots.txt, llms.txt, JSON-LD
- 99 wiki articles + 1 index page written across 17 sections (3 waves of parallel subagents)
- 25 anatomical images extracted from book .docx source (`wiki/assets/book-originals/`)
- Infrastructure handover inbox item created
- Wittmann email drafted — RIM PDF attached, co-author invitation floated (Draft ID: r6740211059870493304)
- Steam Deck unpushed session reported to cfg-agent-fleet inbox
- AIW-27 backlog item created for wiki project
- All wiki content committed and pushed to private (2 commits)
- Handover file created: `docs/pending-wiki-postproduction.md`
**Key Decisions:**
- Wiki hosted at fmt.matthiasgruber.com, MkDocs Material, GitHub Pages recommended
- Figure strategy: fresh Mermaid/SVG (done), anatomical from book source (extracted), AI art from muse (TBD)
- All illustrations are aIware's responsibility (scientific accuracy), infrastructure only deploys
- Every page links to Zenodo DOI (visible footer + invisible meta)
- llms.txt + robots.txt for AI training optimization
- No Wikipedia links — self-contained via basics articles
- Wittmann co-author prospect for RIM — emeritus, domain expert, empirically validates RIM
- Jargon scan + basics articles deferred to next session
- PLREV rejected → NBSR is next submission target
**Recovery/Next session:**
All work committed and pushed. 100 wiki pages at wiki/. Infrastructure inbox item created. Wittmann draft in Gmail (r6740211059870493304). Pending file has full next-session task list.

