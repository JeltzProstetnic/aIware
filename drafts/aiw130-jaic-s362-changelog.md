# AIW-130 JAIC draft — S362 revision changelog

Source audit: `docs/research/aiw130-claims-audit-s362.md`. Manuscript: `drafts/aiw130-jaic-draft.md`.
Each finding was re-checked against companion v6 (`drafts/companion-computational-paper-draft.md`), `~/crucible/docs/cru226-juelich-substance.md` §4, `~/crucible/docs/model-explainer/index.html` (P2 = "NEXT — CRU-40"), `~/crucible/docs/results/p1-causal-transfer.md` (Q-learning 0.94 tie-break artefact) and the Kanai & Ma full text (`literature/fulltext/Kanai2026.pdf`, §4.5, §4.7, §9.2 quotes confirmed). Every source supported its finding; none was rejected.

Abstract: 149 → 148 words. Keywords: 6 (unchanged). §§1–9: 9,874 → 9,985 words.

## Findings

| id | old (short) | new (short) | status |
|---|---|---|---|
| B1 | §6(b) "In simulation we can already show that the checks separate systems…" | "the companion reports capability dissociations that bear on the structures the checks target; none of them runs the checks themselves" | APPLIED. Subsection heading "(b) The checks discriminate: …" also changed to "(b) In-silico dissociations and their scope", since it made the same claim. |
| B2 | "open-ended computation does real, demand- and scale-gated work … sharpens as the system grows" | accuracy peak at intermediate difficulty, 30/30 reservoirs, ordered regime, moves with memory horizon, "not evidence that operating at the edge of chaos pays" (§4.4) | APPLIED (companion §4.4 l.139, §7 l.234) |
| B3 | "The banked positive results are the ones where open-ended computation and closure are present together…" | the interaction is the discriminating *prediction* and is untested; positives obtained with no regime manipulation; re-entry null on a task the passive reservoir already solved (§6) | APPLIED, reworded so it opens on the prediction rather than a denial; m8's "already solved" clause is part of the audit's B3 text |
| B4 | "should, and in the toy systems does, move the readout" | "These ablations are the experiments the checks call for … None has yet been run as specified." | APPLIED. Same paragraph's opening "is made clean by" changed to "would be made clean by" for tense consistency. |
| B5 | Box 1: $L_W$ tracks κ "validated in the companion" | "…not an identity, and it has not yet been tested" | APPLIED. Box 1's "behavioural correlate reported in Section 6" changed to "specified in Section 6" (nothing is reported there). |
| B6 | §6(a) "every branching ratio is reported … closed-loop perturbation test (Gruber, 2026b) … design … given in the companion" | conditional tense; rate-meter fact cited to companion §3.2; closed-loop-perturbation clause and last sentence deleted | APPLIED |
| B7 | "decisive test is open: … capability *dies* when the loop is cut" | decisive test is not a loop-cut (feedforward plus memory, companion §8); it is cost at matched function on an open-ended workload | APPLIED; the paragraph's universal-approximation argument merged into the new text, the duplicated "binary cut" sentences and the self-narrating opener "We are equally plain about the ceiling" removed |
| B8 | "checks are *implementable* and *discriminating* … show that the readouts move … a proof that the detector is runnable" | "specified precisely enough to implement … does not license the claim that the checks have been run … a specification of a runnable detector plus … capability dissociations" | APPLIED; dangling "It licenses" given the subject "The evidence" |
| B9 | §8 "corroborated side … closure advantage is an interaction" | companion's toy-scale capability results; transfer via projection, non-unique; planner at fixed budget; interaction untested | APPLIED |
| B10 | Conclusion "grounded … by in-silico dissociations whose discriminating result is an interaction" | "specified down to a buildable … motivated by toy-scale capability dissociations; the checks themselves, and the decisive scaled test, have not yet been run" | APPLIED |
| M1 | Abstract "in-silico dissociations show they discriminate" | "toy-scale in-silico dissociations motivate them" | APPLIED |
| M2 | §1 "This paper supplies all three … dissociations that show they discriminate"; §9 "supplies all three" | "proposes an answer to each … bear on the structures the checks target" | APPLIED at §1 and §9; also applied to the abstract's "We supply all three" for consistency, paid for by cutting "end to end" (148 words) |
| M3 | "survival task … capacity- and recurrence-matched ablation of the self-model … d ≈ 2.4" | observational-to-outcome transfer, projection removed, 0.98 vs 0.78 (chance), d = 2.44, 40 seeds, non-unique | APPLIED (companion §4.3 l.129–133) |
| M4 | "full bracket of competent reactive policies … plateaus" | "scores 0.00–0.33 at the same sample budget … could not reach the behaviour with more samples" | APPLIED (companion §4.1 l.117) |
| M5 | §1 "needs a substantive theory to fix the target" | §9.2 quote "a tier-III, dynamics-internal feature of the system itself"; theories guide the search | APPLIED (quote verified verbatim) |
| M6 | "Recurrent realizers pass; tables and unfolded nets fail." | conditional on the persistent component belonging to the relevant organization; Kanai & Ma leave that open (§4.7) | APPLIED (verified: "a tier-II/III question the framework deliberately leaves open") |
| M7 | §4 "any world-model … is driven to carve … The self-attractor thus falls out of embodiment"; Check 1 "will carve" | "plausibly … we expect … This is a hypothesis: … self/world split was built in … wiring-cost argument (§5.3)"; Check 1 "is expected to carve" | APPLIED (CRU-226 §4 item 3; companion §2 l.85, §5.3) |
| M8 | §7 "(i)∧(ii), which is the specific structure the detector adds" | mutual dependence is common; closure is what recurrence already gives (§5.1); discriminating content in (iii) and the off-line sub-clause | APPLIED (companion §7 l.236) |
| M9 | §7 PP "cannot predict a closure-caused, level-graded collapse" | PP makes no prediction about the cost gap at matched recurrence; FMT predicts it exists and grows with openness | APPLIED |
| M10 | §8 "cutting the self-model's contribution … should degrade world-modelling" | at matched function the cut system needs more capacity or samples; gap grows with novelty | APPLIED |
| M11 | §6 "A null in that regime then counts as a disconfirmation of closure…" | relates excess-$L_W$ to the companion's cost-at-matched-function DV; both readings must agree in sign | APPLIED. "the prediction is pre-registered" changed to "is to be pre-registered" (no pre-registration exists yet). |

Applied: 21 (10 BLOCKER, 11 MAJOR). Rejected: 0.

## Left for MG (MINOR findings, not applied)

- m1 (l.20) "which we abbreviate ICCR": ICCR is Kanai & Ma's own abbreviation.
- m2 (l.46) "requires a substantive theory ICF does not provide": softer form of M5; now inconsistent with the revised §1 sentence.
- m3 (l.52) "these openings do not weaken": Kanai says this of the grain problem only.
- m4 (l.64) "in rate reservoirs the computational optimum sits in the driven-stable, ordered regime": scope to "the rate reservoirs tested so far … §4.4".
- m5 (l.84) "best-validated readout": the subsampled branching ratio has failed as a stand-alone certificate (companion §8).
- m6 (§6(b)) survival advantage: companion calls it small, a toy, an existence result (0.29–0.33 vs 0.17–0.25).
- m7 (§6(b)) "toy rate- and spiking-network models": the cited results are gridworld and rate-reservoir models; none is spiking. **APPLIED S362 by main loop** (factual: no cited result is spiking).
- m8: folded into B3 (applied as part of B3).
- m9 (§8 l.186) uncited "companion treatment" and generalised "usually turns subcritical" (reverse-direction risk under `prediction-framing.md`).
- m10 (§8 l.190) homeostatic controller "passes the closed-loop forms of all three checks": should be checks 1 and 2.
- m11 (§7 l.170) "the detector supplies the tier-III structure": over-strong, same S281 point as M2.
- m12 AI-use disclosure: see "For MG".
- m13 Baltieri & Kanai (2026) BBS reference unverified; ledger has PsyArXiv 2025, doi 10.31234/osf.io/m4gk3.
- m14 Figures 2 and 3 have no in-text callout.
- m15 (§6(c)) "terrifyingly competent": editorialising.

## For MG

1. **AI-use disclosure (m12).** Not touched, per instruction. It is not the S342 wording chosen at D-S359-2, and "analysis code used for the in-silico checks reported in the companion" repeats the B1 error (no checks were run). MG to choose the text before entry (S345 rule).
2. **Title.** Not touched. `decisions.md` l.371 (S277) records "…a Self-Model That Takes Itself for Its Bearer"; the draft uses "An Operational Detector for Machine Consciousness: …". Probably superseded by the NoC lane; confirm.
3. **§6 heading "Constructive grounding — the detector is runnable".** Left as is. After B8 the section claims a runnable *specification*, not a run; "the detector is specified to the point of being runnable" or similar may fit better.
4. **Pre-existing self-narration in §8 l.196** ("we are careful to separate what has been corroborated post hoc…", "we do not claim they do") was not in the audit and was left.

## Re-check pass (docs/research/aiw130-recheck-s362.md), applied by main loop S362
- F1 l.154 regime-manipulation over-correction → §4.1–4.3 vs §4.4 split. APPLIED
- F2 re-entry null (§6, CRU-36) marked under re-analysis (artefact audit). APPLIED
- F3 §5.1 scoped to graph structure. APPLIED
- F4 §6 heading 'runnable' → 'specified to implementation'; l.162 wording. APPLIED
- F5 survival numbers + §4.2 added. APPLIED
- m10 → 'check 1 and the closed-loop form of check 2'. APPLIED
- m2 and the remaining minors: left for MG (S362-7).

## S363 fix pass (D-S363-5)

Sources re-checked: companion `drafts/companion-computational-paper-draft.md` (§3.2, §4.2, §4.4, §4.6, §5.1, §8), FMT master `paper/full/four-model-theory-full.md` l.17, Crossref/OpenAlex for m13.

- F6 → §6(b): "only for tasks of intermediate difficulty" → "only for the medium-difficulty task at the base size" (companion §4.4: hard task lifts with N).
- F7 → §6(b): "interaction, not a main effect" → "an interaction: the closure advantage should depend on the substrate keeping its open-ended capability".
- F8/m5 → check 3 neural readout: branching ratio "reported beside a rate-matched surrogate"; guardrail "best-validated readout … physical medium" → "a corroborating readout for that property in self-organizing tissue".
- F9 → §6(b) substrate baseline: "tuned to a critical spectral radius by fiat" → "set to its measured edge (driven Lyapunov exponent ≈ 0)".
- F10/m4 → §3 and §6(b): "in rate reservoirs" → "in the rate reservoirs tested so far" (§3 pinned to Gruber 2026b §4.4).
- F11 → §6(b): "capacity FMT holds consciousness requires … floor of that capacity band" → "shown at scale"; clause cut.
- F12 → check 1 "the body is plausibly…"; §6(a) "would carve"; §6(c) "suppose intrinsically identified self-attractors form there. Check 1 then passes".
- F13 → resolved by aligning §7 to the F3 wording: "the closed-loop form of (i)∧(ii) discriminates little … off-line clause of (i) and … (iii)"; Box 1 unchanged.
- F3 residue → §7: "Mutual dependence … is common" (stated as fact) → "a returning path through the self region is what recurrence already gives (§5.1; a graph result). Mutual dependence … plausibly comes as cheaply"; "says nothing about dynamics" fence removed.
- F14 → §8: "The predicted interaction … is untested" cut from the corroborated list (stated in §6).
- F15 → "decodable" → "intrinsically identified" in §6(c), Box 1, §8 dual-threshold and falsification; Fig. 1 alt text now quotes the figure's own readout ("a self-state maintained across the perturbation and re-established after it"); falsification check 2 now "world-transition invariant under swept clamps of its self-attractor (κ ≈ 0)". The definitional uses of "decodable" in §3 (explicit mode) were kept.
- F16 → check 2 "as Section 6 shows" → "argues"; Box 1 "behavioural correlate specified in Section 6" → "behavioural correlate of check 2, on the workload fixed in Section 6".
- F17/m11 → §7: "is the substantive tier-III target §9.2 calls for" → "is a candidate for the tier-III target Kanai and Ma call for"; "supplies the tier-III structure" → "proposes".
- F18 → §1 roadmap: "Section 7 relates it to ICCR and to rival frameworks; Section 8 states scope and falsifiers."
- F19/m1 → §1: "which we abbreviate ICCR" → "Intrinsic Causal-Computational Realization (ICCR)".
- F20/m3 → §2: "these openings do not weaken" → "the grain opening does not weaken"; the "First, … Second, …" ordinals dropped (ordinal ceiling).
- F21/m12 → AI-use disclosure replaced by MG's wording verbatim (kept under the existing bold label "AI-use disclosure."); no in-silico claim remains in it.
- m2 → §2: "requires a substantive theory ICF does not provide" → "remains an empirical question, with theories guiding the search"; Box 1: "methodology ICF's §9.2 invites a substantive theory to supply" → "methodology through which Kanai and Ma propose to operationalize the search for the tier-III target".
- m6 → §6(b) survival result reworded per companion §4.2: "In a toy survival task … outlives a matched reactive agent by a small margin (0.29–0.33 against 0.17–0.25)".
- m9 → §8 "One condition, two sides": uncited "companion treatment of consciousness in biological brains" replaced by the full framework (Gruber, 2026a), which states near-criticality as the signature free modelling leaves in neural tissue (master l.17); the reverse-direction sentence "abolish free modelling, and the substrate usually turns subcritical with it" deleted (`prediction-framing.md`: no criticality→free-modelling inference); "Both cite the full framework" removed as redundant.
- m13 → Baltieri & Kanai: BBS version verified on Crossref and OpenAlex ("Steam-engine naturalism", BBS 49, article e318, online 2026-09-17, doi 10.1017/S0140525X25103531, a commentary on Seth's biological naturalism). The ledger's PsyArXiv DOI 10.31234/osf.io/m4gk3 does not resolve (doi.org "DOI Not Found"). Reference kept as BBS, article number e318 added.
- m14 → callouts added: "(Figure 2)" after the four model kinds in §3; "(Figure 3)" after the three deliverables at the end of §2.
- m15 → §6(c): "terrifyingly competent" → "may be highly competent".
- For MG 4 (+ same class in §8) → "we are careful to separate what has been corroborated post hoc from what remains an untested forecast" → "some corroborated post hoc and some untested"; "they do not demonstrate consciousness, and we do not claim they do" → "and do not demonstrate consciousness"; "and we do not overclaim past it" cut; "We record this as a downstream consequence" → "This is a downstream consequence". For MG 3 (heading) was already done as F4.
- R1 → callbacks cut (below).
- R2 → §6(b) "; none of them runs the checks themselves" and "no result in this subsection is drawn from a running instance" cut; ablation paragraph "None has yet been run as specified." cut; "Reported this way, …" (self-narrating duplicate of the paragraph's first sentence) cut. "Not run" now stands once in §6 (the "evidence licenses" paragraph) and once in §9.
- R3 → "since a loop between two things needs two things" → "since the reservoir had no distinct self- and world-models for a loop to close between".

**Section-reference density.** Callbacks removed: all Kanai & Ma §9.x pins after §1 (kept once each at their first statement in §1, and in the Fig. 3 alt text because the figure prints them), the §2 italic-header pins, the repeated Gruber 2026a "Section 3.5 / 3.7.3" pins (3.7.3 kept once, §3), the four §6(b) per-result companion pins (one "§4" at the end), the §4.1–4.3/§4.4/§6 pins in the interaction paragraph, the second "§8", and the internal "Section 3/4/5/6/7" pointers in §2, §4, Box 1, §5, §6(c), §7 and §8 that only pointed. Kept: §1 roadmap, §4.7 (quote), §3.7.3, §5.3, §3.2, §4, §4.4, §5.1, §8, §7.4, §3.4.3, "Section 6 argues" (check 2), "workload fixed in Section 6" (Box 1).
Counted three ways on the whole file (references and figure alt text included):
| count | before (HEAD) | after |
|---|---|---|
| `structural_slop.py --profile paper` callbacks_per_k | 5.51 (10,159 words) | **1.70** (9,996 words) |
| raw regex matches, gate pattern `(Chapter|Section|Part|Appendix)\s+\d|§\s*\d` | 59 (5.81/1k) | 20 (2.00/1k) |
| inclusive, plural "Sections N" also counted | 61 (6.00/1k) | 21 (2.10/1k) |

Other gated measures after: denial openers 1.00, ordinal openers 0.80, scope fences 0.40, contrast verdicts 0.10, undecidability tags 0.00, pet words 0.00 — PASS on all. `check_prose_register.py`: 0 register hits, 0 aidioms; one dense window (words 5900–6300, §5 grain-dial paragraph), pre-existing and untouched by this pass. Abstract: 148 words (unchanged).

## S363 second fix pass (re-check N1–N10)

Source: `docs/research/aiw130-recheck-s363.md`. Sources re-read for the fixes: companion §4.4 Methods (five further scans, two nulls among the rate reservoirs), companion §6 (re-entry null), master §3.7 ("the signature the property leaves … not the requirement itself"; "usually shows").
- N1 → figures renumbered to first-citation order: ICCR-openings table = Fig. 1 (§2 callout "(Figure 3)" → "(Figure 1)"), 2×2 grid stays Fig. 2, decision flow = Fig. 3 (§4 "Figure 1 renders the procedure" → "Figure 3 renders"). Figures section reordered; captions and alt texts moved with their figures. New files `figures/aiw130/jaic-fig1-iccr-openings.{svg,pdf,png}` and `jaic-fig3-decision-flow.{svg,pdf,png}`; the old `jaic-fig1.*`/`jaic-fig3.*` are left in place, unreferenced. Generator `scripts/gen-aiw130-figures.py` writes the new names; `test_gen_aiw130_figures.py` updated (3 passed).
- N2a → §2 italic headers carry their locators again: "(§9.2)", "(§9.4)", "(§9.3)"; §5 quote "could play that role" gets "(Kanai & Ma, 2026b, §9.3)".
- N2b → §6(b) re-entry null pinned "(Gruber, 2026b, §6)"; "the framework expects it either way" → "the framework predicts a null here".
- N3 → check 3: "a branching ratio near unity reported beside a rate-matched surrogate" → "a branching ratio near unity that a rate-matched surrogate does not reproduce".
- N4 → §3: "the computational optimum sits in the driven-stable, ordered regime" → "where a capability optimum appeared, it sat in the driven-stable, ordered regime"; §6 ablation wording kept.
- N5 → §7: "plausibly comes as cheaply, so the closed-loop form … discriminates little, and" → "is plausibly as common, so the closed-loop form … would discriminate little;".
- N6 → §8 falsification: check 2 also fails "for a system whose closure-specific excess $L_W$ does not exceed the capacity-matched sham" (added to the "It also fails" sentence rather than appended to the long κ sentence, which reads more cleanly).
- N7 → §8 "One condition, two sides": "is the signature free modelling leaves rather than the requirement itself" → "is the usual signature free modelling leaves, not the requirement itself (Gruber, 2026a, §3.7)"; closing "The two describe one condition at two grains." cut.
- N8 → §7: "are the structure-*extraction* method they name" → "are a structure-*extraction* method of the kind they name".
- N9 → §8: "makes differentiating predictions" → "makes predictions".
- N10 → §6(b): "were obtained at one fixed regime" → "were obtained without varying the substrate's regime".
- §4 optional (re-check §4) → Box 1: "on the workload fixed in Section 6 — … on an open-ended workload" → "in Section 6 — … on the open-ended workload fixed there".
- §3(d) → decision-flow verdict box "Graded conscious-or-not verdict + explicit confidence" → "Verdict on the tested conditions + explicit confidence"; Fig. 3 caption follows it; Fig. 3 alt text rewritten box by box from the SVG's text strings. Fig. 1 alt text also aligned to its SVG ("§9.x" as printed, "(intervention + readout each)" added, arrows described).

Gate after: `structural_slop.py --profile paper` PASS, 10,020 words — denial 1.00, ordinal 0.80, callbacks 2.30 (was 1.70; +6 pins from N2a, N2b, N7), fences 0.40, contrast 0.10, undecided 0.00, pet words 0.00. `check_prose_register.py`: 0 register hits, 0 aidioms, the same pre-existing dense window (words 5900–6300). Abstract 148 words (unchanged); AI-use disclosure unchanged.
