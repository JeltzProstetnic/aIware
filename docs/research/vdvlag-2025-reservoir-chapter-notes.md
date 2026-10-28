# van der Vlag et al. — "Complexity and Criticality in Neuro-Inspired Reservoirs": call notes

Read S364 (2026-10-28) by an Opus subagent. The full 12 pages were read; the source is `Downloads/Complexity and Criticality in Neuro-Inspired Reservoirs.pdf`.
Prepared for the Jülich call on Fri 2026-10-30 at 10:00 (D-S363-7). **These are a subagent's findings:**
check the figure readings, especially the colourbar ranges, against the PDF before quoting them to Michiel.

## Bibliographic
van der Vlag, M., Yegenoglu, A., Jimenez-Romero, C., Morrison, A., Diaz, S. *Complexity and Criticality in
Neuro-Inspired Reservoirs.* Pre-final LNCS-style chapter, built 2025-10-07. The citation markers are unresolved, and no venue or DOI is printed.
FZJ JuSER record 1046968; eBRAIN-Health (H2020 101058516). Code: github.com/DeLaVlag/TVB-Reservoir.

## What it does
- **Model.** TVB is used as a reservoir computer. A 96-node connectome of neural-mass nodes is driven by the Lorenz system and predicts it. Input nodes are 10/17/30 and output nodes 15/20/22. It runs on GPUs via RateML (p.1–3).
- **Training and test.** Training is 625 steps, including 125 of warm-up, with ridge-regression readout. The test is a 375-step spin-up followed by a 250-step macro prediction. The error is exponentially weighted normalised MSE (p.3–4).
- **Two mean-field models.**
  - Montbrió–Pazó–Roxin (MPR): sweep over I, J, η.
  - Larter–Breakspear (LB): sweep over aee, VT, rNMDA.
  - Parameter ranges are in Table 1, p.5.
- **Three instruments.**
  - PCI: LZ divided by source entropy, with the Lorenz onset as the "perturbation" (p.5).
  - DFA: the Nolds library ported to GPU (p.6).
  - Largest Lyapunov exponent (LYA): Nolds-style time-delay embedding (p.6–7).
- **Results.**
  - MPR: lowest MSE near a plane separating high-DFA from low-LYA, which they call "near critical". LYA is 0.2–0.5 throughout (p.7–8).
  - LB: MSE rises at high VT and high aee. They call the band just before that rise "critical-like" (p.9).
  - Median-threshold masks (Fig. 4, p.9): MPR does best in the active mask, LB in the resting mask. Sample sizes are about 50 simulations per mask for MPR and about 500 for LB.
- **What it does not report:** fitting range, detrending order, embedding parameters, nulls or surrogates, statistics, or a limitations section.
- **Internal inconsistencies:**
  - The p.10 conclusion says MPR's best fits come with "high" complexity, then "lower" complexity.
  - p.4 and p.9 disagree on what VT does.

## Instrument issues, as read from the page
- **DFA.**
  - Fig. 2's colourbar reportedly runs from −0.2 to 1.2. A negative α is impossible for a correct standard DFA.
  - The text claims a log–log regression that does not depend on amplitude. The shipped code takes the median of log F / log n, which does (crucible finding A4; A1–A3 alongside, `~/crucible/docs/cru226-vdvlag-code-verification.md`).
  - "α in 0–1 = Hurst" is wrong in general.
  - 625 samples is short for DFA.
  - **Gift only: offer it after the instrument exchange is agreed, never raised cold (D-S363-6).**
- **LYA.** A positive value is read as chaos. Crucible showed that a stable linear system driven by noise also reads positive, and the fit uses only 250 samples. Without a null, this is not evidence of chaos.
- **PCI.** Not Casali's PCI: no source modelling and no significance binarisation against a baseline. Its values exceed 1 (up to 3.0). "Normalised spatiotemporal LZ" is the accurate name.
- **No nulls anywhere.** Our conformance rule, which reports criticality only beside a rate-matched null, is something we can offer.
- **Connectome size.** The text says 96 nodes, but crucible's notes log 68 analysed regions. Clarify this before plan stage S2 adopts their connectome.

## Exchange candidates (M4 package, `docs/plans/fmt-mini-model-plan.md`)
- **From them:** the LYA kernel (Rosenstein, verified correct by crucible), the GPU PCI, and the 96-region connectome as the S2 long-range scaffold.
- **From us:** a validated DFA, the activity-model detector run on their reservoirs, and null baselines.
- **Framing:** a joint known-answer validation step, not a correction.

## Questions for the call
1. **p.3:** Which parcellation is the 96-node connectome? Is it usable for TVB–NEST co-simulation with spiking areas embedded? (This sets up S2.)
2. **p.8:** λ is positive everywhere. Have you compared it against a noise-driven linear reservoir or a surrogate? Offer to share null baselines both ways. (This opens the exchange without naming the DFA.)
3. **p.6 / Fig. 2:** What DFA fitting range and detrending order did you use? How do you read the α < 0 region? **Ask only after the exchange is agreed**; this is the bridge to the gift.
4. **p.5:** Would you run a clean pulse perturbation on our spiking objects, so that the two PCIs are comparable?
5. **p.9 / Fig. 4:** Is the active-versus-resting preference robust across seeds and connectomes, and could JSC run it at 10^5–10^6 neurons? (This bridges to S1.)

## Bearing on FMT ("consistent with" only, and weakened by the instrument issues above)
- **Abstract, p.1 / p.10:** edge-of-chaos dynamics go with better memory and prediction. This is consistent with the Class-4 lineage.
- **Fig. 4:** the two models are best in different regimes. This is consistent with criticality being a signature, not a requirement (S329).
- **p.8:** complexity is not tied solely to chaos or long memory.
- **Cite none of these as support** until the instruments have been re-run with fixes and nulls.
