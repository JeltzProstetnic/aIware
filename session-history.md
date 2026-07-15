# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-15T08:20Z — WSL (home PC)
**Goal:** S264 — run the MG-requested LAST Fable review of AIW-109 (5 agents: source spot-check + built print-interior PDF sampling), consolidate findings, apply real defects, then close out toward full re-upload.
**Completed:**
- Startup: private-remote sync (up to date), handoff + next-session-task read, session-context populated
- 5 Fable agents ran (Fable confirmed by MG) — all editions reviewed, source + print PDFs
- Consolidated → `drafts/aiw109-final-review-S264.md`; every build-defect claim re-verified vs scripts
- MG triage decisions collected (subtitle, figure labels, boilerplate, homunculus)
- Fixes A–D implemented in build scripts + verified per edition (rendered pages + text extraction)
- Rebuilt 14 print interiors (7 translations × PB+HC; EN untouched) + DE eBook
- Rebuilt 10 covers (DE/ES/FR/IT/PT × PB+HC) — AIW-60 visual QA gate rendered + PASSED all 5
- eBook check: EN/ES/FR/IT/PT/JA unaffected by print fixes (verified); only DE.epub needed + refreshed
- Deliverables written: review doc, print manifest, kit README; backlog AIW-109 + AIW-115 + conv-log updated
- Committed 5bad968d + pushed both remotes (private full + origin filtered, 19 LFS objects)
- Built full re-upload kit `tmp/aiw109-reupload-S264/` (all 8 editions × interior PB+HC + cover PB+HC + eBook; ZH eBook=PublishDrive; PUBLISH-PACK.md) — opened in Explorer. NB reference frame = vs KDP-live: ALL interiors + ALL eBooks are new (whole ed.2 never uploaded); only DE/ES/FR/IT/PT cover spines changed (EN/JA/ZH spines still fit).
- Desktop cleanup: recycled 26 redundant book build-artifacts (all had committed backups) to Windows Recycle Bin; kept tool shortcuts + desktop.ini + 2 non-book files (optimized-cnc-prompt.md, space.xspf — flagged for MG)
**Key Decisions:**
- Resuming AIW-109 per handoff; NOT diverting to the 13 pending aIware inbox items (flagged for later backlog promotion).
- Review verdict: text clean in all 8 editions; defects are build-template chrome only, no blockers.
- **MG triage (2026-07-15):** (1) DE subtitle = "Die Architektur von Bewusstsein, Berechnung und Kosmos" (keep title page, suppress phantom source line-3 subtitle from body/TOC). (2) Localize figure labels ALL editions (Abbildung/Figura/図/图 + FR colon-spacing). (3) Latin rights boilerplate = LEAVE English (no change). (4) Homunculus = ACCEPT English labels (no change).
- Fix round: A=contentsname localize (both translation builders, ES/FR/IT/PT/JA/ZH); B=dedication skip (Latin builder, ES/FR/IT/PT); C=DE subtitle phantom suppress (de builder); D=figurename per edition. Fix E (TOC folio glue, NIT) DEFERRED to keep EN pristine + avoid tocloft risk pre-upload.
**Recovery/Next session:**
- S264 close-out handover: `docs/pending-aiw109-s264-handover.md`. All 8 editions' interiors BUILT + gate-clean (H+V); translation covers barcoded (ZH pending ISBN). Kit `tmp/aiw109-reupload-S264/` + PUBLISH-PACK.md. MG was mid-re-upload at shutdown.
- Margin gate (run before ANY KDP upload): `python3 scripts/check_pdf_margins.py pop-sci/book-manuscript*.pdf`.

### 2026-07-14T23:05Z — WSL (home PC, DESKTOP-32ILURB)
**Goal:** Resume AIW-109 BUILD & SHIP (ed.2). Manuscripts are TEXT-FINAL (6 translations @ 2475 lines). Remaining = build-level typography → edition-marker flip → rebuild interiors+eBooks → hand MG the KDP upload kit.
**Completed:**
- Startup: private ff-merge clean; surfaced additionalContext (config-repo-dirty in cfg sibling noted, not touched; 11 aIware inbox items parked as outreach/theory lane)
- Verified manuscripts: ES/FR/IT/JA/PT/ZH all 2475 lines; DE 2367 (own structure); EN 2475 — matches handoff
- Read §5 build-checklist (drafts/aiw109-combined-cross-language-findings-S259.md)
- Step 1: build-level typography — new tested `tmp/typography_fixes.py` (14-pass pytest). FR EPUB narrow-NBSP U+202F (apostrophe already curled by pandoc smart); JA+ZH `*CJK*`→bold, Latin titles kept italic. Wired into epub + CJK print builders.
- Step 2: edition marker First→Second on PRINT copyright page, all 8 langs (verified; 0 stale first-markers). eBooks keep © 2026.
- Step 3: rebuilt 8 eBooks + 18 print interiors fresh; ZH docx rebuilt + PublishDrive kit refreshed. Source .md untouched, 6 translations still 2475 ln.
- Step 4: KDP re-upload kit `drafts/aiw109-ed2-reupload-2026-07-14/` (7 eBooks + README) ready for MG-manual upload.
**Key Decisions:**
- Text is FINAL — NO more text editing (S262 judgment round + MG decisions applied, commits 172dcdc9→8e6e5717).
- Edition marker: "Second" only, drop "corr." — PRINT copyright page ONLY; eBooks keep just `© 2026` (MG S260).
- Build-level typography lives in `scripts/typography_fixes.py` (moved out of tmp/ per MG "move non-throwaway out of tmp"; imports fixed + verified). Rest of book-build toolchain stays in tmp/ pending AIW-114.
- MG S263: next session re-does all cover art IF necessary, then RE-UPLOADS EVERYTHING (print + covers + eBooks). Spine check done — all covers' baked page counts match built interiors → no cover redo needed unless the final Fable review flags a defect.
- MG S263: next session must run a LAST Fable review (3–5 agents, overall checks + samples, INCLUDING sampling the built print-interior PDFs, not just source text) → then close AIW-109.
**Recovery/Next session:**
- Handoff: docs/pending-aiw109-multilang-fix-and-reupload.md (§ "NEXT SESSION (S263)")
- Build-checklist: drafts/aiw109-combined-cross-language-findings-S259.md §5
- Build scripts: tmp/build_translation_interior.py (ES/FR/IT/PT), tmp/build_translation_interior_cjk.py (JA/ZH), tmp/build_book_pdf.py (EN/DE), tmp/build_book_epub_lang.py (eBooks)
- comgarra-guard rule in .claude/knowledge/publication-build.md — applies to ANY global/substring swap

### 2026-07-14T13:10Z — WSL (home PC, DESKTOP-32ILURB)
**Goal:** Continue AIW-109 (multilang book corrections) to publication — resolve Fable cost-hold conflict with MG, then run the judgment review round on corrected manuscripts, then build-level typography → build & ship.
**Completed:**
- Startup: private remote ff-merged (already up to date), session-context populated
- Read HANDOFF file `docs/pending-aiw109-multilang-fix-and-reupload.md`
- Fable cost-hold conflict RESOLVED — MG cleared Fable cost-free; propagated to cfg inbox + decisions.md
- Judgment review round DONE — 6 Fable agents, all 6 manuscripts still 2475 lines; results in `docs/pending-aiw109-judgment-round-S262.md`
- Crash-safe checkpoint: committed + pushed to private
- MG ruled on all needs_MG_decision items ("a + go with recs"); applied via 4 Fable agents (ES/ZH/JA/PT); all 6 manuscripts still 2475 lines → text-FINAL for ed.2
- Root-cause guard for the comgarra bug: knowledge entry + AIW-113 + cfg inbox escalation (MG-approved)
**Key Decisions:**
- Fable cost-hold RESOLVED (S262) — MG confirmed cost-free; used Fable for the judgment round. Fleet-config clearance propagated via cfg inbox.
- comgarra guard (S262, MG-approved) — blind substring/`replace_all` swaps banned without a grep pre-check + post-check; recorded in `.claude/knowledge/publication-build.md` + AIW-113 + cfg global-rule inbox proposal.
- Edition marker: print copyright page only (eBooks keep `© 2026`, no edition line) — S260.
- Line 678 anosognosia = ESM in all 8 editions — S260.
**Pending at shutdown:** Steps 1–4 (build & ship) deferred to next session per MG. 11 cross-project inbox tasks still un-triaged → backlog.
**Recovery/Next session:**
- Handoff/work-order: `docs/pending-aiw109-multilang-fix-and-reupload.md` (AIW-109).
- Primary findings: `drafts/aiw109-combined-cross-language-findings-S259.md` (§4 = judgment-round worklist, §5 = FMT term decisions + build checklist).
- Low-risk mechanical pass committed `fcf82704`; do NOT assume every §4 row is still open — re-verify against current text.

