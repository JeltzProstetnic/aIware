# Session History

Rolling window of the last 3 sessions. Newest first.

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

### 2026-07-12T07:30Z — WSL
**Goal:** Startup — awaiting MG direction. Live handover is AIW-109 final split review (Fable IT/PT/JA/ZH first, then Opus EN/ES/FR/DE).
**Completed:**
- Startup protocol run: private remote pulled (up to date), SessionStart additionalContext surfaced
- Read ground truth: conversation-log + git log (S253–256) + backlog [>] + pending-aiw109-final-review.md
- Fable review IT/PT/JA/ZH (cost-free, worked) — all 22 fix-spec items landed native, constraints held
- Opus review EN/ES/FR/DE — EN & DE ship-clean; ES/FR had the two-decades + TOC defects
- Applied unambiguous fixes to all 8 editions (see below), verified (line counts intact, greps 0/1)
**Key Decisions:**
- Fable confirmed cost-free this session (IT/PT reviewers ran clean) → used for CJK/IT review + edits per handover.
- Applied "two decades → ~two years" to ALL 6 translations (EN/DE were already correct); genuine internal contradiction → applied under MG's "apply real fixes" directive.
- Insect passage: 7/8 editions keep "just ask any insect"; only IT reconciled to "animal kingdom" → recommend revert IT (MG call).
- Held commit until MG resolves the 5 judgment calls (may add edits to same 8 files) — one clean commit.
**Recovery/Next session:**
- ~40 files edited/created, verified, NOT committed. Includes: 8 manuscripts (text), 18 new `figures/*-{es,fr,pt,it,ja,zh}.svg` + 18 `.png`, 6 .md figure-path rewires. Render script: `tmp/render_localized_figures.py`. Review folder: `tmp/figure-review/` (open).
- If resuming: `git -C ~/aIware status`; if MG approved figures → commit "S257 AIW-109: final split-review fixes + localized figures (6 langs) across 8 editions" (filtered-push needs clean worktree; stash tmp/ first). NOTE user font install (~/.local/share/fonts CJK) is machine-local, not in git — re-render needs it.
- Downstream (separate, after commit): ed.3 interior rebuild + KDP re-upload; per-language human-native reviewer gate before any translation publish.
- Fix-spec: `drafts/aiw109-fix-spec.md`. Handover: `docs/pending-aiw109-final-review.md`.

### 2026-07-11T11:15Z — WSL (home PC)
**Goal:** AIW-109 — apply ALL cross-edition QA fixes across all 8 book editions (EN/DE/ES/FR/PT/IT/JA/ZH). Hidden-defect QA cleanup, NOT theory revision. Work-list = `drafts/aiw108-cross-edition-qa-findings.md`.
**Completed:**
- Startup: sync check (both remotes up-to-date), read handoff + work-list + publication-build.md, persona=Bartl
- §0 WebSearch DONE: Hengen/Shew + Algom/Shriki ConCrit = REAL (no fabrication, no escalation); IIT letter = PsyArXiv Sept 2023 (fixed); Kanzi dance=verified, ice-cream=unverifiable (FLAG MG); Bach=Joscha Bach @Plinz X-post, verbatim unverifiable via search (FLAG MG)
- EN source-shared fixes DONE: #1-17 factual + #37/#40/#41/#42 artifacts + TOC clean (#43) + "automata" grammar. All verified count==1, defects gone. Paragraph-merge from comment-deletion caught+fixed. Line count 2475.
- EN: ALL source-shared + aphorism (keep 1) + automata. DONE, verified.
- DE: ALL source-shared (Opus German rewrites) + aphorism + §2 typography (222 quote-pairs→„…", 852 dashes→spaced en-dash) + calques/register. DONE, verified. Line 2368.
- ES/FR/PT/IT/JA/ZH: source-shared + §2 + BLOCKERs applied via Fable per-language agents (spec: `drafts/aiw109-fix-spec.md`). FR BLOCKERs (L1088 English note, L636 garbled, L554 unclosed italic) resolved; PT L518 corrupted-para reconstructed + free-will meaning-inversion fixed. All verified (grep, line counts sane, no merges).
- Checkpoint commit of all 8 manuscripts.
**Key Decisions:**
- Fix EN/DE `.md` first for source-level items, then re-propagate (AIW-109 non-divergence rule).
- Method: verified find→replace, `count==1` per file, never parallel-write one file.
- Model conflict to resolve with MG: handoff says "Fable is back / cost-free" (S254); agent-roster config still shows Fable COST HOLD from 2026-07-08. Default to Opus for fix work unless MG confirms Fable.
**Recovery/Next session:**
Read `docs/pending-aiw108-fix-all-editions.md` + `drafts/aiw108-cross-edition-qa-findings.md`. Editions file: `pop-sci/book-manuscript{,-de,-es,-fr,-pt,-it,-ja,-zh}.md`. Verify each line number in-file before editing.

