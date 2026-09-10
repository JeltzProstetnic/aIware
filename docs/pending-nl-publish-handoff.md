<!-- Action: reference — S268 handoff for the Dutch (nl) edition. Tracked-by: AIW-123. -->
# NL (Dutch) edition — publish handoff (S268, 2026-07-24)

**Branch:** `s268-translations-zh-print` — **MERGED TO MAIN + PUSHED (S273, 2026-07-28, WSL)**; worktree removed and local branch deleted. All NL deliverables below are now on `main` (private full + origin filtered; manuscripts excluded from public per push filter). Remaining = MG human review + Wednesday Fable pass + publish (see below).

## DONE this session (all built + QA-passed)
- Manuscript reconciled → publish-candidate: `pop-sci/book-manuscript-nl.md` (Kalk Fable pass-1 full + pass-2 26/54 + Opus 3 more → 349+ objective fixes applied; interior-review 5 High + book-wide consistency: event-horizon unified, Appendix→Bijlage, 181 straight quotes → curly, **295 matched `„…"` pairs**).
- **Interiors:** `book-manuscript-nl.pdf` (pb, 288pp) + `-nl-hc.pdf` (hc, 288pp) — both **margin-gate CLEAN**.
- **Epub:** `book-manuscript-nl.epub` (34 chapters, 5 figures).
- **Covers (AIW-60 QA passed):** `cover-kindle-nl.jpg`, `cover-wrap-nl.pdf` (pb), `cover-wrap-nl-hc.pdf` (hc). No ISBN → barcode clear-zone left for KDP.
- **KDP metadata:** `drafts/kdp-nl-metadata.txt` (title/subtitle/blurb/7 keywords/bio/categories). MG initializing KDP to get the free ISBN.
- **Build now reproducible:** nl is a first-class target in `tmp/build_translation_interior.py`, `build_book_epub_lang.py`, `build_translation_covers_latex.py`. Dutch babel installed (`sudo apt install texlive-lang-european`).

## REMAINING for nl publish
1. **MG HUMAN-NATIVE DUTCH REVIEW** (locked gate — do NOT publish before it). Review the manuscript + the HELD findings in `drafts/aiw108-nl-kalk-findings.md`: **[S268 held]** 255 B voice-calls, 5 D grandeur, 43 un-auto-appliable A's + **[S276 held, at bottom of doc]** 146 B, 2 D, 1 C, 2 ambiguous A; **the 2 L78 calls** (the "geen rivaliserende theorie kan evenaren" claim vs "toetsbare"; and "in het Engels" localization — both deliberately NOT applied), and the interior-review Med terminology standardizations (rekendomein vs berekeningsdomein, reduceerbaar vs herleidbaar, permeabiliteit vs doorlaatbaarheid, DIS/DID, Planck compounds).
2. ~~**FINAL FABLE PASS**~~ **DONE S276 (2026-07-30, WSL).** The 28 pass-2 aggressive segments (24,26,28-31,33-54) scanned on Fable (workflow `wf_a3b44fde-5a3`, tracked keeper `scripts/translation/kalk-nl-fable2.js`). 248 findings → **97 category-A auto-applied** (match-once) + 1 cross-segment consistency fix (`architecturale`→`architectonische` L1904, twin of the seg-28 fix). **HELD for the MG review below:** 2 ambiguous A (appear 2×), 146 B, 1 C, 2 D — all appended to `drafts/aiw108-nl-kalk-findings.md` (§ "Pass-2 Fable completion — S276"). Quote-pair (295/295) + heading (120) + line (2475) invariants preserved; commit diff = the record. *(NB: the S273 "Opus 3 more" note was inaccurate — findings doc had "no Opus re-scan yet"; ran the full 28-seg superset, resolved either way.)*
3. **ISBN → re-wrap if own-ISBN:** ~~currently the wraps leave a barcode clear-zone (KDP-free path).~~
   - **PAPERBACK DONE (S277, 2026-07-30, WSL follower worktree):** ISBN **9798189912351** baked into `cover-wrap-nl.pdf` (12.899"×9.250", spine 0.6486" @288pp). Rebuilt via worktree-safe `tmp/build_nl_wrap.py` (re-creates the deleted S268 wrapper, `__file__`-relative → output stays in the checkout). AIW-60 QA passed (title/subtitle no art-overlap; EAN-13 legible, check digit verified). KDP-free wrap backed up to `tmp/cover-wrap-nl-kdpfree-bak.*`. kdp-specs.md NL row added.
   - **HARDCOVER DONE (S277, 2026-07-30):** ISBN **9798189928499** baked into `cover-wrap-nl-hc.pdf` (14.413"×10.417" case laminate, spine 0.6486" @288pp) via `scripts/build_nl_wrap.py us-hc 9798189928499`. AIW-60 QA passed (title/subtitle no art-overlap; EAN-13 legible, check digit 9). KDP-free HC backed up to `tmp/cover-wrap-nl-hc-kdpfree-bak.pdf`. Both wraps delivered to `Desktop/kdp-nl-kit/` (stale no-barcode versions removed). kdp-specs NL row updated. **NL Kindle ebook already public.**
4. **Figure localization** (optional, for parity with other editions): 3 figures still EN-labelled (`homunculi.en`, figure1/2/five-layer). Localize SVG labels → nl PNG, update manuscript refs, rebuild. **MG steer (2026-07-30): the Dutch edition currently ships ENGLISH figures — acceptable for now (Dutch readers handle English well), NOT a publish blocker; fix one day for parity.** Low priority; tracked under AIW-123's figure-localization tail.
5. **Merge to main + publish:** ~~merge / filtered-push / worktree remove~~ **DONE S273 (2026-07-28)** — merge commit `efb09267`, pushed both remotes, worktree+branch removed. STILL PENDING: MG uploads to KDP (Kindle → pb → hc) after the human review + Fable pass.
6. **Reproducibility gap:** the print-wrap nl config lives only in the worktree wrapper `tmp/build_nl_wrap.py` (nl LANG + Dutch back-cover blurb injected at runtime). Promote it into the tracked `tmp/build_translation_covers_print.py` LANG + `tmp/translation_blurbs.py` BLURBS.

## KDP kit for MG
`tmp/kdp-nl-kit/` (+ copied to Desktop): the 2 interiors, epub, 3 covers, metadata.txt.

## Wednesday (Fable back) — the deferred lane
- **ZH font fix + rebuild** (MG wants the live zh ebook replaced): the shipped zh print + ebook render Simplified Chinese in the **JP** Noto face. Full diagnosis + fix in `docs/pending-el-ko-zh-print-consolidation.md` (xeCJK OTC face-selection for print; SC-first CSS + `zh-Hans` for the epub).
- **el/ko translations** downstream (Kalk+coherence+reconcile+build) — same pipeline as nl.
- **Platform:** el/ko/zh print+ebook consolidate on **PublishDrive** (see the same doc). Korean domestic retail = the one unavoidable gap.
