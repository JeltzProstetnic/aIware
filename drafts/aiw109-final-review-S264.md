# AIW-109 — FINAL Fable review (S264, 2026-07-15, WSL)

5 Fable-5 agents, one per edition-group. Each did a source spot-check **and** sampled the
built print-interior PDFs (rendered via Read `pages:`). REPORT-ONLY. This doc = consolidation
+ mechanism-confirmed root causes + triage. Main loop verified every build-defect claim against
the actual build scripts (not trusting agent theories) before writing the fixes below.

## Verdict in one line
**Text is clean in all 8 editions. Every defect found is build-template chrome, not manuscript
text.** No BLOCKERs. Two are unambiguous build defects (fixing); the rest are editorial calls for MG.

## GREEN LIGHTS (independently confirmed on rendered pages)
- **Edition markers correct everywhere**: EN "Second US edition, 2026" · DE "Zweite deutsche Ausgabe, 2026"
  · ES "Segunda edición, 2026" · FR "Deuxième édition, 2026" · IT "Seconda edizione, 2026" ·
  PT "Segunda edição, 2026" · JA 第二版 2026年 · ZH 第二版，2026年. © 2026 on every copyright page.
- **CJK emphasis renders BOLD, never slanted** — confirmed with page evidence in BOTH JA and ZH.
  (Engine is script-aware: Latin book titles stay italic on the same pages; CJK emphasis goes bold.)
- **FR guillemets « » + narrow-NBSP** (inside « » and before ; : ! ?) render correctly in print.
- **comgarra / glued-token grep**: zero hits in IT + PT sources. No fused tokens anywhere.
- **EN + DE coherence carry-overs all intact**: Coda re-narration coherent (DE Coda's "Kapitel 13"
  avalanche cross-ref resolves correctly), Ch.15 criticality re-intro intact, DE self-reference to
  *Die Emergenz des Bewusstseins* correct (Uncle Bruno present-tense, no death date — correct).
- **ZH**: 《》 titles, full-width punctuation, pangu Latin↔CJK spacing, —— em-dash all correct.
- **No mojibake / tofu / missing-glyph boxes / right-margin overflow / orphaned headings** in any
  sampled edition. Latin-translation & CJK interiors use bottom-centered folios, no running header —
  consistent by design (EN/DE the same). Roman→arabic \mainmatter transition correct everywhere.

## FINDINGS (consolidated, deduplicated)

| # | severity | editions | location | defect | root cause (verified) |
|---|----------|----------|----------|--------|------------------------|
| 1 | MAJOR | ES FR IT PT JA ZH | TOC page (p.vii) | TOC heading prints English **"Contents"** in a localized book | Both translation builders rewrite `## Índice`→`## Contents` for converter recognition (build_translation_interior.py:63, _cjk.py:86) but never localize `\contentsname`. EN default = "Contents" (correct); DE does `\renewcommand{\contentsname}{Inhalt}` (build_book_pdf_de.py:728); translations do neither. |
| 2 | MAJOR | ES FR IT PT | dedication on **both** p.v and p.ix | dedication printed twice | EN builder skips the in-body dedication line by matching the *English* text (build_book_pdf.py:471). CJK builder renames the translated dedication→English so it's skipped (_cjk.py:88-89). **Latin builder is missing that rename** → translated dedication renders in body too. |
| 3 | MAJOR | DE | title page vs body p.ix + TOC | title page shows subtitle "Die Architektur von Bewusstsein, Berechnung und Kosmos" but the DE **source** subtitle (line 3) is "Bewusstsein und Kosmos – Eine unerwartete Verwandtschaft", which the builder renders as a phantom heading-only page (folio ix) + spurious TOC entry | de builder hardcodes the EN-parallel subtitle on the title page (build_book_pdf_de.py:880) while the source line-3 subtitle falls into the chapter-heading path (list at :585). **Which subtitle is canonical = MG decision.** |
| 4 | MINOR/editorial | DE ES IT PT JA ZH | every figure caption | caption label is English **"Figure"** | translation builders inherit EN `\figurename`; not localized (Abbildung/Figura/図/图). EN correct; FR "Figure" is correct French (only its colon-spacing is English-style — see #5). |
| 5 | MINOR | FR | figure captions | "Figure 1:" uses English colon spacing, not French "Figure 1 :" (NNBSP) | caption `labelsep` not French-spaced (body prose IS correct). |
| 6 | MINOR | IT | TOC (p.viii) | two long TOC rows glue the folio to the last word ("…referimento**217**", "…cosmologico**259**") | leader collapses on near-full lines. Also seen as NIT on EN "Appendix F**241**", DE "Anhang G**275**". |
| 7 | NIT/editorial | ES FR IT PT | copyright page | rights boilerplate ("No part of this publication…") stays **English** | Latin builder doesn't localize cr2. **JA/ZH ARE localized** (_cjk.py cr2) → Latin editions are the inconsistent ones. |
| 8 | NIT/editorial | all translations | Fig. 2 (Penfield homunculus) | anatomical labels inside the image are English | shared `homunculi.en.png` fallback; DE alone has `homunculi.de.png`. Localized caption is fine. |

Non-defects explicitly cleared: aIware URL rendering ("alware" is serif I/l glyph ambiguity — source
correct), half-width vs full-width colon in JA reference notes (deliberate), figure numbering scheme
difference (EN/DE "2.1" vs translations "1" — two builders, cosmetic), EN/DE Coda opening divergence
(independent native texts — legitimate authorial difference).

## FIXES — mechanism + exact change

**Fix A (defect #1, Contents) — both translation builders.** In each `patched()` doc, inject
`\renewcommand{\contentsname}{<cfg toc>}` immediately before `\tableofcontents` (after \begin{document}
+ any babel language selection, so it wins). Latin: build_translation_interior.py. CJK: _cjk.py (CJK
toc string is fine — xeCJK is loaded). Affects ES FR IT PT JA ZH.

**Fix B (defect #2, dedication) — Latin builder only.** In build_translation_interior.py `preprocess_md`,
add the line the CJK builder already has:
`if s == f"*{cfg['dedic']}*": lines[i] = "*" + EN_DEDIC + "*"` (exact-match verified against source line 9
of es/fr/it/pt — FR apostrophe is straight in both, matches). Affects ES FR IT PT.

**Fix C (defect #3, DE subtitle) — de builder, AFTER MG picks canonical subtitle.** Put the chosen
subtitle on the title page (build_book_pdf_de.py:880 + pdfsubject:789) and suppress the source line-3
subtitle from the body/TOC (skip it like EN skips its `## The Architecture…`). Kills the phantom page + TOC entry.

**Fix D (defects #4/#5, figure labels) — IF MG wants localization.** Set `\figurename` per edition
(Abbildung/Figura/図/图) and, for FR, French-space the caption colon (`labelsep`). Affects DE ES IT PT JA ZH (FR = colon only).

**Fix E (defect #6, TOC folio glue) — optional.** Add a non-collapsing min-space/leader between TOC
title and folio in the shared builder. Would also tidy EN + DE. Low priority, cosmetic.

**Fix F (defect #7, Latin boilerplate) — IF MG wants it.** Localize cr2 for ES/FR/IT/PT (needs 4
translated rights paragraphs). JA/ZH already done.

**Fix G (defect #8, homunculus) — IF MG wants it.** Commission homunculi.{es,fr,it,pt,ja,zh}.png. Low priority.

## Rebuild scope
- Fixes A+B (the two clear defects): rebuild **ES FR IT PT** (both, dedication + Contents) + **JA ZH**
  (Contents). EN + DE not touched by A/B.
- Fix C: rebuild **DE**.
- Fixes D/F/G if approved: fold into the same rebuild round (avoid double rebuilds).
- After rebuild: re-verify page counts vs baked cover spines (EN 271, DE 299, ES 290, FR 299, IT 288,
  PT 288, JA 282, ZH 218) — a page-count move forces the matching cover rebuild (+ AIW-60 QA). Front-matter
  fixes (dedication removal drops ~1 leaf in ES/FR/IT/PT; DE phantom removal drops ~2 leaves) **WILL move
  page counts** → cover spine recheck is REQUIRED for the rebuilt editions. Then refresh the re-upload kits
  in `drafts/aiw109-ed2-reupload-2026-07-14/` (7 KDP eBooks) + `drafts/publishdrive-zh-2026-07-13/`.
- eBooks: the dedication/Contents defects are print-interior (LaTeX) issues; check whether the epub builders
  share the same TOC-title / dedication behavior before assuming eBooks are clean.

## Decisions needed from MG (blocking the fix round)
1. **DE canonical subtitle** — ✅ ANSWERED (MG, 2026-07-15): **"Die Architektur von Bewusstsein, Berechnung und
   Kosmos"** (EN-parallel, current title page). Fix C = keep title page as-is, suppress source line-3 subtitle
   "Bewusstsein und Kosmos – Eine unerwartete Verwandtschaft" from body/TOC (kill phantom page + TOC entry).
2. **Figure caption labels** — localize to Abbildung/Figura/図/图, or leave "Figure"?
3. **Latin rights boilerplate** — localize ES/FR/IT/PT to match JA/ZH, or leave English?
4. **Homunculus image** — commission localized labels, or accept the English-labeled classic figure?
(TOC folio glue = optional cosmetic; will fix unless told not to.)

---

## FIXES APPLIED + VERIFIED (S264, 2026-07-15)

All build-script edits made with the Edit tool; each fix verified on the rebuilt output before moving on.

- **Fix A (Contents)** — `build_translation_interior.py` + `_cjk.py`: inject `\renewcommand{\contentsname}`
  before `\tableofcontents`. Verified: ES=Índice, FR=Table des matières, IT=Indice, PT=Sumário,
  JA=目次, ZH=目录. ✅
- **Fix B (dedication)** — `build_translation_interior.py` `preprocess_md`: rename translated dedication
  to the English string so the shared skip catches it. Verified: ES dedication now on p.5 only (was p.5 + p.ix). ✅
- **Fix C (DE subtitle phantom)** — `build_book_pdf_de.py`: skip the source-line-3 subtitle. Verified:
  "Eine unerwartete Verwandtschaft" no longer appears as body heading or TOC entry; title page keeps the
  canonical "Die Architektur…". Also fixed the **DE eBook** (`build_book_epub_de.py`: rewrite the source
  subtitle to the canonical one) — DE.epub re-exported + refreshed in the kit. ✅
- **Fix D (figure labels)** — `\figurename` per edition: DE=Abbildung, ES/IT/PT=Figura, JA=図, ZH=图
  (FR keeps "Figure"). Verified on rendered captions in every edition. ✅
- **Fix E (TOC folio glue)** — **DEFERRED** (NIT; would pull the pristine EN edition into the rebuild
  and needs tocloft tuning that risks the TOC layout right before re-upload). Backlogged.
- **Boilerplate / homunculus** — no change (MG: leave English / accept). ✅

**Rebuilt:** 14 print interiors (DE/ES/FR/IT/PT/JA/ZH × PB+HC; EN untouched), 10 covers (DE/ES/FR/IT/PT
× PB+HC — AIW-60 QA PASSED on all 5 languages), 1 eBook (DE). Page counts: DE 297, ES 288, FR 297,
IT 286, PT 286 (−2 each from front-matter removal); JA 282 / ZH 218 unchanged; EN 271 unchanged. Cover
spines re-derived to match. Re-upload manifest: `drafts/aiw109-print-reupload-S264.md`.

**Still open (MG-owned):** human-native reviewer gate per language; MG-manual re-upload of the changed set.
