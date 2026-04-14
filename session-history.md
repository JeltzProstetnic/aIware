# Session History

Rolling window of the last 3 sessions. Newest first.

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

### 2026-03-18T14:45Z — the office
**Goal:** Gmail triage — McFarnell reply, Wittmann reply, RIM paper updates
**Completed:**
- Synced with private remote (rebased, 30 commits pulled from sessions 157-165)
- Gmail inbox checked — 7 messages, 2 new today (Wittmann, McFarnell), 5 already handled
- McFarnell reply drafted and SENT — addresses phenomenality location, weather simulation objection, ESM recruitment triggers, proposes joint predictions
- Wittmann reply drafted (Gmail draft, fully German) — acknowledges risk-taking finding, shares consciousness paper links + book, asks for Singapore paper
- Wittmann Singapore paper (2002 ICAP) read and ingested to private/
- RIM paper updated: Wittmann & Süß (1999) and Wittmann & Hattrup (2004) citations added to Section 3.4
- Rosenthal/Pygmalion reference qualified per Wittmann feedback, Rosenthal (2002) and Jussim & Harber (2005) added
- OTCS Ivoclar email noted — Ivoclar scope, not actioned here
**Key Decisions:**
- Pygmalion: qualify rather than remove (add meta-analysis citations)
- Wittmann email fully in German (no language switching)
**Pending at shutdown:** Wittmann draft in Gmail (3 drafts — user to delete old 2, send the corrected one)
**Recovery/Next session:**
- Wittmann draft needs sending (user correcting inline in Gmail)
- OTCS API email should be routed to ivoclar project via inbox
- D'Angiulli follow-up ~2026-04-07, Kanai follow-up when he reaches out

