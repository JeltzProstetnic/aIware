<!-- Action: reference -->
<!-- Tracked-by: AIW-319, AIW-320, AIW-321, AIW-322 -->
# Perplexity assessment of FMT v23 (MG via Bartl, 2026-10-20) — checked against the master

Sources (verbatim): `docs/sources/perplexity-2026-10-20/fmt-decisive-tests-three-rivals.md`,
`docs/sources/perplexity-2026-10-20/ai-handoff-brief-fmt-rivals.md` (Gmail `1a15b3fc06a8b9dc`).
Checked S347 against `paper/full/four-model-theory-full.md` (v23 source) and the primaries named below.
The 6–7/10 ratings are a chatbot's subjective numbers and carry no evidential weight.

## Verdict per point

| # | Perplexity point | Holds? | Evidence in the master | Action |
|---|---|---|---|---|
| 1 | Table 1b's free-modeling falsifier ("robust consciousness where a fixed lookup reproduces the system's behaviour on novel input") is too weak: beating a lookup shows generalisation, not free modeling. | **Holds.** A lookup fitted to past behaviour cannot reproduce novel-input behaviour except trivially, so the falsifier almost never fires. It is the same "maximise the discriminator, not the confound" lesson as didactic patterns #18/#26. | Table 1b row 1; §3.7 text repeats it (l.452). | `AIW-320` |
| 2 | Prediction 2 (input shapes the identity content of ego dissolution) may not discriminate from predictive processing: a PP model with **modality-specific precisions** could predict modality-specific tracking. | **Holds as an open question.** The master asserts REBUS "stops short of the modality-specific tracking FMT commits to" (l.947). That is true of REBUS as published, but nobody has checked whether a PP model with modality-specific likelihoods/precisions predicts the same, which is the comparison a reviewer will make. | l.877, l.947, §8.3 | `AIW-319` (Perplexity's recommended next task) |
| 3 | Active inference is now a consciousness theory: Whyte et al. 2024 is the minimal theory, and AI-C has a test protocol. | **Holds — and it dates our PP section.** The master cites Hohwy & Seth 2020 for "PP is not itself a theory of consciousness" and says PP "offers no account of why or when". Whyte, Corcoran, Robinson, Smith, Moran, Parr, Friston, **Seth & Hohwy** (2024), arXiv 2410.06633, "On the Minimal Theory of Consciousness Implicit in Active Inference", is by those same authors. Protocol verified: Robinson, Corcoran, Whyte, Sárközy, Seth & Kovács (2025), PLOS ONE, 10.1371/journal.pone.0328836. Corcoran et al. 2026 (the adversarial review) is already cited. | §7 PP paragraph (l.877) | `AIW-321` |
| 4 | Kleiner's no-go theorem for consciousness on a chip should be addressed. | **Holds — not engaged at all.** Kleiner & Ludwig (2024), "The case for neurons: a no-go theorem for consciousness on a chip", *Neurosci. Conscious.*, 10.1093/nc/niae037 (verified). The master cites only Kleiner & Ludwig 2024 *Synthese* and Mallavarapu & Percy's process-theory no-go (l.561). Kleiner is an associate editor at NoC (the `AIW-103` target) and on the JAIC board, so the omission is visible exactly where it costs most. Perplexity's caveat is correct: an FMT-style constitutive account may reject the "dynamical relevance" premise; that is a reply to write, not a refutation in hand. | l.561, l.1091 | `AIW-322` |
| 5 | Closure needs an operational definition independent of the consciousness verdict, a selective intervention, independent assessment, and pre-stated rival predictions. | **Partly addressed already.** Table 1b concedes there is no established protocol and gives a report-free decision procedure for inspectable systems. Still missing: a written rival (GNW / active-inference) prediction for the same intervention. | l.186, Table 1b row 3 | Fold into `AIW-319` (same rival-specification work) |
| 6 | IWMT is the closest comparator. | **Already done.** §7.2 (l.895, l.919) engages Safron 2020 as "the closest peer". | — | none |
| 7 | GNW is not "just report"; COGITATE is no free promotion for FMT. | Fair; no specific master sentence found that claims otherwise. Watch the register in outreach. | — | none |
| 8 | Ratings (Kleiner ~7, FMT 6–7, cosmology 3–4/10). | Subjective chatbot numbers. No action. | — | none |

## Bottom line

Four of the eight points call for changes to the next master version (v24). None of them threatens the core,
but #2 and #4 are the two a reviewer at NoC or JAIC would raise first. #3 is the easiest fix and the most
embarrassing to leave in: our PP section quotes Seth and Hohwy against a position they have since published.
