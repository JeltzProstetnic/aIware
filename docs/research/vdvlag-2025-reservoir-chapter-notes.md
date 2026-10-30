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

## Crucible status for the call (crucible fyi, 2026-10-28)
Use only if the call turns to our own models. Refresh before Thursday night: crucible promised an update on (3).
1. **P1 on the old creature: NOT TESTABLE** under the pre-stated judge. No lasting activity pattern formed in any learning seed. The frozen arm's "lasting objects" were a single insula input echo. Fast inhibitory homeostasis, which pulls every cell to 3 Hz, removed it. The cortex had no copy of its own motor command (`~/crucible/docs/results/cru227-p1-2026-10-28.md`). The old creature is retired for this question. **Follow-up (crucible, same day): the learning-arm null is an INSTRUMENT LIMIT, not a finding.** With 30-s windows of 4000 cells, a perfectly constant pattern needs a correlation eigenvalue of about 6.8 to be matched across two windows at the 0.7 threshold (spiked-covariance bound; planted patterns: 0/7 tracked at 5–6.2, 7/7 at 8.7–10.7). Every real component in the learning runs sat at 4.71–4.94, most at the noise floor. So the null cannot tell "no lasting pattern" from "a lasting pattern below that strength". Do not state it as evidence for or against anything (may-say / must-not-say: `cru227-p1-2026-10-28.md` §6).
2. **New creature (CRU-231):** a forage world with food and danger, hardwired reflexes below the cortex, balanced reward-gated learning, and an efference copy. The frozen small creature eats by reflex: 10 items against 1 in 2 min without reflexes (RAW). It passes most of the feasibility gate: shoulder angle decodes from S1 and parietal, and hunger from insula.
3. Learning-vs-frozen twins are running. The first 2 min are RAW and unchecked, so draw no conclusion.
4. Long-run launchers now refuse to start unless the variables under test decode at start and after a short learning stretch (CRU-230).

### Refresh S366 (2026-10-30 morning, from crucible's files and two fyi of 2026-10-29)
- **Fig. readings verified against the PDF (S366):** Fig. 2 MPR DFA colourbar −0.2 to 1.2, LYA 0.20–0.45, PCI 0.5–3.0; Fig. 3 LB DFA ~0 to 1.0, LYA 0.15–0.35, PCI 0–3.0. p.8 states λ > 0 "0.2–0.5" throughout. The subagent's readings above hold.
- **CRU-231 twins** (`~/crucible/docs/results/cru231-learning-twins-2026-10-28.md`): the first runs had weight normalisation unwired (CRU-232), so they are a runaway diagnostic, not a learning result. The normalised re-run (seed 0, n = 1) kept the S1 readout in the frozen band at minutes 1–2; low minutes later coincided with high pain. Use only that file's may-say.
- **CRU-233 critic** (crucible fyi 05:45, `cru233-critic-k10-2026-10-28.md`): feeding and pain contact did not differ between arms beyond the noise, and a reflex-only arm ate as much as the intact one. Must not say the creature learned anything. MG parked the critic line ~05:55 on 2026-10-29: *"what we need most until Friday is ways to find explicit models, that was always the main goal"*.
- **CRU-234** (unlabelled search for stable cortical patterns, free vs sensory areas): not run by call time. Crucible's session ended 2026-10-29 07:00 with the recordings unfinished; the promised plain-words may-say did not arrive. Present it as the plan only.
- **CRU-234 first result** (crucible fyi 09:40, RAW, `~/crucible/docs/results/cru234-find-frozen-2026-10-30.md`): MAY SAY — free areas show a stable, weak co-firing structure, ~18–20 directions, same in both halves of a 23-min run, all three creatures, gone under cell-timing scramble; WRITE against body/world variables being tested. MUST NOT SAY explicit models were found (pre-stated window search: none qualifies). Area rates follow hunger (R² 0.25–0.63): one number per area, not a model.
- **CRU-234 update** (crucible fyi 09:45, RAW, red-team pending, same file §3): none of the ~18–20 stable directions follows arm, food or danger or adds beyond the area's overall rate (one tiny hunger pattern in 1/3 creatures). MAY SAY: stable co-firing structure but no explicit model yet; area rates track hunger and danger proximity; next = 40k creature with learning on. MUST NOT SAY explicit models found.
- **CRU-238** (crucible fyi 09:58, Fable red-team + reproduction s0/s4, result file §4): the frontal 'axis' carries hunger only as a weaker copy of the insula's relayed hunger signal (insula rate R² 0.83–0.87, frontal 0.62–0.77, frontal adds ~0 beyond insula). Danger not yet tested properly (scoring fix pending). Hand position absent from the free areas. Open definition question to MG: does a relayed copy count as a (robust) explicit model?
- **MG ruling D7** (crucible decisions, fyi 10:00): a pattern that only re-carries its input area's signal COUNTS as a simple robust explicit model. So the free-frontal weighted rate direction = a simple robust explicit model of hunger, 3/3 creatures (8k, learning off). Beating an input filter is a KIND question, not a model criterion. Results file §5.
- The call sheet built from all of this: `drafts/aiw351-juelich-call-sheet-v2.pdf`.
