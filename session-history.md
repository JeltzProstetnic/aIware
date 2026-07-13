# Session History

Rolling window of the last 3 sessions. Newest first.

### 2026-07-13T22:05Z — WSL (home PC)
**Goal:** AIW-109 — apply Fable interior-review fixes across all 6 translations → rebuild → re-upload eBooks as ed.2 corr.2
**Completed:**
- Startup: private ff-merge (up to date), session-context populated, config-dirty on cfg-agent-fleet flagged
- Read EN source anchors (378 callback intact, 674 anosognosia ¶ present, 678 EWM/ESM, 1674/1726 distinct)
- Applied ALL High-severity fixes via 6 parallel Fable subagents (one per manuscript file, no collision):
- FR: title self-citation «Je»(+echo), anosognosia ¶ restore, Class-4 bullet close, Ch2 callback, Ch5 xref
- JA: title self-citation (+echo), weak-point-4 authorial line, Ch2 callback, Ch5 xref
- ES: meaning-inversion 1324 →«en tu lugar», Ch2 callback, 1674/1726 made distinct (678 NOT touched)
- IT: broken impersonal-si grammar 330–340 (4 edits, «si prova» consistent), Ch2 callback, 1674/1726 distinct (678 NOT touched)
- PT: 1550 truncation restored, Ch2 callback
- ZH: meaning-inversion 1750 →推出第四类之外, term-collision 1298 →通透性, Chalmers name 1308, Ch2 callback, Ch5 xref, 1674/1726 distinct
- Med pass (~127) applied via 6 Fable per-language agents (Low ~222 deferred per MG)
- Line 678 EWM→ESM across all 8 editions (MG: info that arm isn't behaving as predicted never reaches ESM)
- Build-checklist §5 verified: PT quotes auto-curled by pandoc `smart`; FR EPUB NBSP + CJK emphasis deferred (build-level)
- Committed 52db8226; work-order updated with build&ship handoff
**Key Decisions:**
- Model routing: Fable for risky/challenging native-language fixes, Opus for mechanical (per MG directive + work-order §Model policy; Fable cost-free as of S259).
- Line 678 anosognosia deficit = Explicit Self Model (ESM), not World Model (MG, author decision).
- Edition marker "Second edition" = PRINT copyright page ONLY (MG S260); eBooks keep just © 2026.
- Another review round on the corrected manuscripts BEFORE any rebuild (MG S260) — reduces churn after ~800 edits.
- EN source (book-manuscript.md) deliberately NOT edited: 378 callback is intact (per-translation restore only); 678 EWM/ESM deferred to MG; 1674/1726 EN is already the canonical distinct pair (translations propagate FROM it).
- All 6 translation manuscripts are line-aligned ±2, so shared clusters (378, 1674/1726) fixed per-file.
**Pending at shutdown:** build & ship deferred to next session behind another review round (MG S260).
**Recovery/Next session:**
- High-fix diffs are on disk (uncommitted): `git -C ~/aIware diff --stat pop-sci/book-manuscript-*.md`.
- To continue: get MG answers to the 3 gate questions (Med/Low scope, line 678, edition label), then Med/Low pass → build-checklist → rebuild → re-upload.
- Flagged-but-out-of-scope (next pass): FR ~2248 «(voir Chapitre 6)» capital-C vs lowercase convention; IT chapter-title/TOC «ci si sente qualcosa» (grammatically valid, but body now uses «si prova» — consider harmonizing the heading).

### 2026-07-13T14:56Z — WSL
**Goal:** S259 startup — first session of 2026-07-13 (Mon). Load, surface startup intelligence, triage inbox/pending files under user direction.
**Completed:**
- git-sync (private) — up to date; origin fetch clean
- Loaded startup intelligence, populated session-context
- Safron PDF ingest (inbox #9 part 1): identified 3 PDFs; Safron 2020 IWMT already in corpus (dedup, redundant copy ignored); added Safron2022a (AIXI/FEP-AI) + Safron2022b (G-SLAM) to literature/fulltext/, 3-copy mirror (local+NAS+8TB), INDEX.md addendum (Session 259). Source Windows Documents copies left in place (user state — await OK to clear).
- CRU-36 "look into" (inbox #1): Explore-agent synthesis of crucible CRU-36 null + prediction revisions + 3 open decisions + modelling-taxonomy + VM-tax → `docs/pending-cru36-prediction-revision.md`. Created backlog AIW-110 (propose P1).
- "track: decisions need structuring" — fleet-wide (p0rn 231K/cfg 155K/crucible 121K/aIware 108K). Filed AIW-111 (aIware split, P3) + cfg-agent-fleet inbox convention proposal (threshold + archive split; no fleet convention exists yet).
- Fable cost-hold resolved: roster text stale (MG re-enabled S254, 41 clean passes S255–57); user reconfirmed "use where it makes sense". Authorized, Opus fallback. Already-open S255 inbox item covers the stale-roster fix.
- ZH Simplified .docx for KDP Traditional-beta → tmp/kdp-zh-docx/book-manuscript-zh.docx (932KB)
- CJK LaTeX toolchain installed (MG ran tmp/install-cjk-latex.sh): xeCJK/ctex + Noto Serif CJK + IPA Mincho
- **NEW: 4 CJK print interiors** (ja/zh pb+hc) via tmp/build_translation_interior_cjk.py (xelatex+xeCJK, Noto Serif CJK). JA 282pp, ZH 218pp. QA'd: proper glyphs, arabic body pagination, localized chapter labels, translated copyright/dedication.
- **BUG FOUND+FIXED: translation interiors were roman-paginated.** \mainmatter only fired on English "Chapter 1:", so ALL 6 translations (incl. the 4 "shipped/candidate" Latin) paginated the whole body in roman numerals; only EN/DE correct. Added language-agnostic fix_structure() to BOTH build_translation_interior.py (Latin) + _cjk.py: all chapters →\chapter* (localized number stays in title, no double-numbering) + \mainmatter before ch1. Rebuilt all 8 Latin interiors (290/299/288/288pp, unchanged) — now arabic. QA'd ES.
- **6 back-cover blurbs** translated+reviewed by Fable (es/fr/it/pt/ja/zh) → tmp/translation_blurbs.py
- **12 translation print COVERS** (wraps, pb+hc) via tmp/build_translation_covers_print.py (Latin pdflatex+inputenc, CJK xelatex+xeCJK; spine from page count; NO barcode = KDP-free-ISBN clear zone). QA'd es/ja/zh pb + es/ja hc + fr pb — no overlap/tofu, correct geometry.
- 2nd Fable review pass on FR + JA blurbs: JA confirmed unchanged; FR typography fix (’ apostrophes + French NBSP via fr_nbsp) → FR covers rebuilt + kit refreshed + QA'd.
- **PublishDrive package** (ZH Simplified) → drafts/publishdrive-zh-2026-07-13/ (epub+docx+cover+metadata+README w/ mainland-China routing).
- **KDP print-upload kit** → tmp/kdp-print-translations-2026-07-13/ (24 files: 12 interiors + 12 covers).
- **FULL FABLE INTERIOR REVIEW — all 6 translations** (54 Fable agents: 9 sections × FR/JA/ES/IT/PT/ZH, each vs aligned EN). ~10-11 High, ~127 Med, ~222 Low. Per-lang docs `drafts/aiw109-{lang}-interior-fable-review-S259.md`; **combined cross-language work-order `drafts/aiw109-combined-cross-language-findings-S259.md`** (synthesis agent). Key: meaning-inversions (ES 1324, ZH 1750), FR+JA-only Ch17 title bug, digital-twin callback dropped at ~378 in ALL SIX, IT grammar, PT truncation, ZH term/name errors.
- Beautiful Loop paper tracked → AIW-112 (P3).
- Next-session handover written: `docs/pending-aiw109-multilang-fix-and-reupload.md` (Action: act) — apply fixes all langs → rebuild interiors+eBooks → **re-upload eBooks as ed.2 corr.2** → rebuild print → human-native gate.
**Key Decisions:**
- The \mainmatter roman-pagination bug was CROSS-LANGUAGE (every translation built via the generic script, not just CJK); EN/DE fine via own scripts. Fixed language-agnostically (fix_structure) — never patch the generated .tex.
- Cover + interior builds made fully SCRIPT-reproducible (all config in the .py, no hand-edited artifacts) — the S140/S144 "fix lived only in generated .tex → silently reverted" trap. New build scripts force-added to git (tmp/ is gitignored in aIware); 278MB of regenerable HC-cover binaries gitignored (regenerate from the committed script).
- Full 6-language Fable interior review done; FIXES deferred to next session; eBooks to be re-uploaded as ed.2 corr.2 after fixes.
- decisions.md schema MG specified: date · structured scope · criticality (cost-if-ignored × access-frequency × other) · lifetime · recheck-interval (auto-flag stale). Fleet convention proposal routed to cfg inbox (AIW-111).
- Fable authorized (cost-hold lifted; roster text stale) — used for all blurb + 54 interior-review agents this session.
**Recovery/Next session:**
Everything is in files: build scripts (tmp/build_translation_interior{,_cjk}.py, build_translation_covers_print.py, translation_blurbs.py, install-cjk-latex.sh), review work-order (drafts/aiw109-combined-cross-language-findings-S259.md + per-lang docs), handover (docs/pending-aiw109-multilang-fix-and-reupload.md). Print kit tmp/kdp-print-translations-2026-07-13/ + PublishDrive kit drafts/publishdrive-zh-2026-07-13/ regenerate from scripts. No conversation-only state.

### 2026-07-12T19:00Z — WSL (home PC)
**Goal:** Resume AIW-109 — bring all 8 book editions to publish-readiness (ed.3) incl. covers. Start with Phase A (EN/DE ed.3 rebuild end-to-end). Fable re-enabled by MG this session ("still free, use where it counts").
**Completed:**
- Startup: private-remote pull (up to date), context surfaced, session-context populated
- Phase A: all 6 EN/DE interiors rebuilt at ed.3 (EN us 271, hc 271, eu 267; DE us 299, hc 299, eu 285)
- Phase A: page-count check — EN us/hc unchanged (covers VALID); EN-eu +2, DE us/hc/eu −2 (spine shift)
- Phase A: DE us+hc KDP covers rebuilt at 299pp (cover script pages 301→299)
- Phase A: eBooks (EN + DE) rebuilt
- Phase A: cover visual QA — found BOTH hardcovers (EN+DE) had the recurring subtitle-over-art bug
- HARDCOVER SUBTITLE BUG FIXED (durable, in-script): EN+DE hc wraps rebuilt, subtitle on dark backing, visually verified against the S140 good cover
- HARDCOVER EYE-FRAMING RESTORED (durable, in-script): the neural eye + glint were cropped OUT of frame because the current script used a center-crop (crop_for_wrap). Restored the S144 method — clip the full ultimate-upscale source (`figures/art-consciousness-ultimate-upscale.png`, 9112×2560) and shift it right so the eye lands top-right of the front. Calibration: `eye_node_x = front_center_x - 7.144` (S144 was x=3.5 at fc=10.644), `height=9.6in`. In build_book_cover{,_de}.py hardcover branch. Also raised the whole HC title+subtitle block ~0.25in (title_offset 0.6→0.35, sub_offset 2.2→1.70) so it matches the paperback height instead of looking squished.
- Covers ed.3 final: EN us/hc + DE us/hc — eye framed, no black band, subtitle/title fixed. Committed (1e179e53).
- KDP metadata kit — all 8 languages (drafts/kdp-publish-2026-07-12/KDP-metadata-all-languages.txt), committed (f59a0c4b). Fable-localized descriptions+keywords; EN in-house. Opened in Notepad for MG.
**Key Decisions:**
- Fable cost-hold LIFTED by MG 2026-07-12: "fable still free to use, make use of it where it counts." Deploy Fable on quality-critical creative/QA passes (translation pre-human QA, cover/metadata copy) — NOT mechanical rebuilds. Persist fleet-wide via cfg inbox.
- HARD BLOCKERS (MG's to resolve, surfaced up front): (1) human-native reviewer gate per translation before publish; (2) ISBNs for 6 translations not reserved + confirm translated titles/subtitles; (3) CJK (JA/ZH) interior-PDF rendering unproven.
**Pending at shutdown:** Phase B/C — build the 6 translation editions (eBook + interior + cover) so all 8 can publish. See "PUBLISH-READINESS" below.
**Recovery/Next session:**
- Plan: docs/pending-book-publish-readiness.md (Phases A-E). Tracked-by AIW-109/108/24/93.
- Build: `python3 tmp/build_book_pdf.py` (EN) + `tmp/build_book_pdf_de.py` (DE); covers `tmp/build_book_cover{,_de}.py`; eBooks `tmp/build_book_epub{,_de}.py`. Tests `pytest tmp/test_content_integrity.py -v`.
- Cover QA MANDATORY visual check (feedback_book_cover_qa) — overlap shipped twice.

