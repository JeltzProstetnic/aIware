<!-- Action: reference -->
<!-- Tracked-by: v12 build/publish (see docs/pending-fmt-v12-zenodo.md) -->

# FMT v12 — citation verification (Session 241, 2026-07-05)

Verified via Crossref / DOI resolvers / publisher pages by a research subagent, in response to the Opus-4.8 + Fable-5 convergent review. **These are the authoritative corrections to apply to `paper/full/four-model-theory-full.md`, `paper/full/latex/paper.tex`, and `paper/full/latex/references.bib`.**

## Must-fix (verified errors)

1. **Katlowitz et al. (2026)** — manuscript line 1154 says *Nature* **642, 195–203** → **WRONG**. Correct: *Nature* **654(8119): 714–723**, DOI 10.1038/s41586-026-10448-0 (online 6 May 2026). Full authors: Katlowitz, K.A., Cole, E.R., Mickiewicz, E.A., et al. **Also:** an Author Correction exists (10.1038/s41586-026-10784-1) — cite corrected version or note.

2. **"~140 datasets" attribution** — belongs to **Hengen & Shew (2025)** *Neuron* 113(16):2582–2598 (DOI 10.1016/j.neuron.2025.05.020), which contains the ~140-dataset (2003–2024) meta-analysis. **Algom & Shriki (2026) ConCrit** (*Neurosci. Biobehav. Rev.* 180:106483, DOI 10.1016/j.neubiorev.2025.106483) is a **REVIEW/framework paper — NO original 140-dataset meta-analysis.** Fix the two spots that credit ConCrit with the 140 datasets:
   - **Line 162** ("ConCrit meta-analysis (Algom & Shriki, 2026) confirms... across 140 datasets") → reattribute the meta-analysis to Hengen & Shew; ConCrit = unifying framework.
   - **Line 395** ("the ConCrit framework (Algom & Shriki, 2026), which synthesized evidence from 140 datasets") → the 140-dataset synthesis is Hengen & Shew.
   - Lines 54, 407, 931 already attribute 140 correctly to Hengen & Shew. Lines 410, 782 say "both across 140 datasets" — make clear the meta-analysis is Hengen & Shew; ConCrit is the framework synthesis.
   - (Caveat: the 140 figure for Hengen & Shew is verified-high-confidence from consistent secondary sources, not verbatim-from-paywalled-PDF. Keep "~140".)

3. **Chowdhury et al. (2026)** — *Nature Human Behaviour*, DOI 10.1038/s41562-026-02446-z (online 27 May 2026), **vol/pages not yet assigned (cite advance-online)**. Full title/journal in ref (line 1046) correct. **Finding: a SINGLE ~19–45 Hz central-thalamic oscillation** (wake + REM, absent NREM) — NOT a two-loop 40/20 Hz split. Manuscript §4.2.2 (line 504) overclaims it "spans precisely the frequency range predicted by [the] dual-loop architecture... exactly as the theory requires." **Fix:** keep the state-tracking support (wake/REM present, NREM absent — that IS supportive), drop the claim that a single band confirms the 20/40 two-loop split; align band to 19–45 Hz. Line 657 REM/NREM usage is already careful — leave.

## Verified correct (spot-check .bib, otherwise no change)

- **Toker et al. (2026)** — *Nature Neuroscience* **29(4): 964–977**, DOI 10.1038/s41593-026-02220-4 (online 24 Mar 2026). >680,000 electrophysiology samples; adversarial AI. Verify .bib matches.
- **Xu et al. (2024)** — *Nature Neuroscience* 27(2): 328–338, DOI 10.1038/s41593-023-01536-9. **Correct as-is.**
- **Tucker, Luu & Friston (2025)** — *Entropy* **27(8): 829** (article no.), DOI 10.3390/e27080829. Verify .bib (cited by article number, MDPI style, not page range).

**No fabricated references detected.** Only outright error = Katlowitz vol/pages; only attribution error = 140-datasets→ConCrit.
