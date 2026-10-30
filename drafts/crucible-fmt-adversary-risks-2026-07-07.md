# Crucible → FMT integration — ADVERSARIAL RISK REVIEW (Fable-5, 2026-07-07)

<!-- Banked from workflow wzv0b5wfl. Planner half failed (session limit); re-run pending. Opus implements later. -->

I have the full picture. Here is the adversarial risk review — text only, no files edited.

---

# ADVERSARIAL RISK REVIEW — integrating crucible findings (1)(2)(3) into FMT paper

Files read: crucible notes (2026-07-07), `four-model-theory-full.md` (§3.7, §4.2.4, §5.3, §6, §6.4, §8.5, §9, abstract/intro), `prediction-framing.md`, `neuroscience-communication.md`, `didactic-patterns.md`.

Bottom line up front: findings (2)+(3) as written are a **credibility landmine** — they reproduce the exact weakness that got FMT desk-rejected before ("predictions too general," Andrillon/NoC; AICE reviewers). Finding (1) is mostly a legitimate *sharpening* but collides head-on with one specific sentence in §"Why Class 4 specifically," and with the paper's own Langton-λ citation. None of the three toy results belong in the paper's evidence register.

---

## RISK 1 — UNFALSIFIABILITY / SPECIAL-PLEADING (Severity: HIGH — highest priority)

**The trap.** Findings (2)+(3) combine into a heads-I-win-tails-I-win structure:
- (2) "a *small* effect on simple/individual tasks is *theoretically expected*" (crucible §2)
- (3) "no current task is deep enough… its *absence there is consistent with the theory*, not against it" (crucible §3)

A hostile reviewer reads: **large effect → confirms FMT; small effect → expected, confirms FMT; absent effect → task wasn't deep/social enough, still consistent with FMT.** There is no stated outcome that counts against the theory. This is a textbook immunizing stratagem (Popper), and it lands on FMT's single most-scarred spot — `prediction-framing.md` records that "predictions too general" is the *literal desk-rejection reason* and that reviewers "converged on the same weakness." Shipping (2)+(3) in their current prose *re-opens that wound with the theory's own words*.

**The specific phrase that must never appear in the paper:** "its absence … is *consistent with* the theory." Using "consistent with" to defend a *null result* is the special-pleading tell. `prediction-framing.md` reserves "consistent with" for *converging positive evidence*, not for excusing failures.

**Mitigation — mandatory reframe to stay falsifiable.** The escape hatch ("the task wasn't deep enough") is only legitimate if **depth is operationalized a priori from task structure, independently of the σ-outcome.** Convert the qualitative dodge into a **risky, pre-registered, monotonic prediction over a graded task battery:**

1. **Define two independent metrics from task structure, before any σ-sweep:**
   - **depth `d`** = minimum number of multi-step counterfactual rollout steps over abstract situations the task provably requires (≥k-step planning verified by task construction, not by the result).
   - **sociality `s`** = number of other agents whose fate must be modelled *through* the self-model (0 = individual, 1 = dyadic observation, ≥2 = multi-agent).
2. **State the functional form (the risky claim):**
   - effect size `E(s,d)` of an explicit-self-model controller over a matched non-self-model controller **increases monotonically** with `s` and `d`;
   - criticality-dependence — operationalized as the width of the σ-window supporting task performance, or the performance drop Δ as σ leaves the critical band — **increases monotonically with `d`**, appearing as a σ-collapse **only above a threshold depth `d*`**.
3. **State the failure criteria explicitly (this is what makes it fail-able):** the prediction is **falsified** if
   - (a) a task with independently-verified high `d` shows **no σ-collapse** / substrate-robust performance; **or**
   - (b) effect size is **flat or non-monotonic** across the graded battery; **or**
   - (c) a **low-`d` (shallow) task shows a sharp σ-collapse** — criticality-dependence without depth breaks the depth↔criticality coupling the theory now stakes itself on.
4. **Pre-register `d` and `s` from task structure BEFORE running the sweep** and say so in the paper. Then "the task wasn't deep enough" is a *pre-committed prediction* ("depth `d` was below `d*`"), not a *post-hoc rescue*.

Without item 4, the claim is circular and reviewers will say so. With it, FMT gains a genuinely discriminating, quantitative test and turns the liability into a strength. Place this in the Predictions section as a single risky claim ("effect-size and criticality-dependence *scale with* a defined depth/sociality metric"), **not** as five/nine numbered items — `prediction-framing.md`: fixed counts become attack surfaces.

---

## RISK 2 — INTERNAL CONTRADICTION: "criticality NOT required for general computation" vs the paper's own text (Severity: HIGH)

Finding (1) says: "neural networks compute well *without* criticality… general computation reveals no criticality-dependence" and CRU-27 shows "memory AND computation co-peak **in the ordered regime** … general computation needs no criticality." This **directly contradicts** the paper's capability argument:

- **§"Why Class 4 specifically" (line 464):** *"only Class 4 supports open-ended computation: Class 1 and Class 2 dynamics … transport no information, while Class 3 dynamics are chaotic, their positive Lyapunov exponents destroying the long-range, structured correlations that **any sustained computation requires**."* → "any sustained computation" is exactly what finding (1) and CRU-27 refute. **Contradiction.**
- **§3.7.2 (line 450):** *"Without the automaton's Class 4 dynamics, the models cannot generate a coherent simulation."* → borderline; readable as "no computation without Class 4." Must be scoped to *open-ended self-simulation*, not computation-in-general.
- **§"Why Class 4 specifically" (line 464)** cites **Langton's λ** as support for computation-at-the-edge. But CRU-27 (the project's *own* result) shows computation **peaking in the ordered regime and collapsing at the chaos edge** — this cuts *against* the naive "computation lives at the edge" reading of Langton, and aligns with the reservoir-computing critiques (Bertschinger & Natschläger 2004; Boedecker et al. 2012). Citing Langton uncritically while the companion crucible data contradicts it is an **honesty exposure** a reviewer familiar with reservoir computing will exploit.

**Mitigation.** Narrow the criticality claim's *scope* (do NOT demote it):
- Rewrite line 464 to: criticality is required for **open-ended, self-referential, multi-step explicit-space simulation** — *not* for shallow/general computation, which is substrate-robust and (per reservoir-computing results) often favours the ordered side. Replace "any sustained computation requires" with "the *open-ended self-simulation* the architecture requires."
- Reframe §3.7.3's "two thresholds" so the criticality threshold explicitly reads **"criticality is the maintenance mechanism that keeps the substrate capable of explicit-space modelling"** — this is the S242-vs-formalization resolution, and it is fully consistent with `prediction-framing.md` S204 rule #1 ("criticality ≠ consciousness; criticality enables the computation").
- Reconcile the Langton citation: cite it for *edge-of-chaos as the regime for open-ended/universal computation*, and explicitly acknowledge that *shallow* computation does not require the edge (cite the reservoir-computing literature "consistent with").

---

## RISK 3 — TABLE 4 / §5.3 vs finding (3)'s σ-independent readout (Severity: MED)

- **§3.7 (line 424):** *"any manipulation that moves all three toward subcriticality (σ → 0 …) should degrade consciousness."*
- **§5.3 / Table 4 (line 594):** *"Consciousness tracks the substrate's position relative to the critical point."*
- Finding (3): the toy ESM death-projection is **σ-independent — death-confidence 0.999 from frozen order to chaos** (i.e., a self-relevant readout that is rock-solid deep into the *subcritical* regime).

A reviewer holding the crucible data can say: "your own simulation exhibits a stable self-model readout at σ = 0.3, well subcritical — so 'move toward subcriticality → consciousness degrades' is contradicted by your own bench." It isn't, *if* the paper scopes the degradation claim to **deep multi-step self-simulation**, not any self-referential readout. But the current blanket wording (424) and Table 4's blanket "consciousness tracks criticality" leave the flank open.

**Mitigation.** Scope line 424 and Table 4 to *deep explicit-space modelling*: "manipulations toward subcriticality degrade the substrate's capacity for **multi-step self-simulation**"; explicitly note that *shallow* self-relevant readouts can survive subcriticality (consistent with finding 1 and 3). Do not let the toy's σ-robust death-readout be mistakable as a counterexample — pre-empt it.

---

## RISK 4 — OVERCLAIM: toy sims read as empirical confirmation of FMT (Severity: HIGH)

Three distinct overclaim vectors:

1. **The 1.0-vs-0.0 "clean match" (CRU-29).** Finding (2) calls the social-transfer result "a **clean match**": transfer 1.0 (FMT) vs 0.0 (no-ESM ablation). But this is **near-circular**: a module built to project fate through a self-model, ablated, stops doing the thing that definitionally requires it. It confirms *the toy implements the mechanism*, **not** that FMT is true of brains, nor that the dissociation exists in biology. A reader (or the author) can slide from "our toy shows the predicted dissociation" to "FMT's dissociation is empirically confirmed." **Do not** present CRU-29 as confirmation of FMT.
2. **§4.2.4 collision.** The paper *already* uses the exact CRU-29 scenario as its flagship evolutionary argument: *"By modelling another organism's experience (projecting the ESM onto an observed other), a conscious system can learn from observed deaths without personal exposure"* (line 528). If the toy is cited here as evidence, the paper would be **citing its own toy simulation as biological/empirical support for the evolutionary claim.** That is an evidence-laundering exposure.
3. **Inconsistent evidential accounting.** Presenting CRU-29 (1.0/0.0) as *support* while excusing CRU-33b's null as "consistent with the theory" applies **two different standards to two results from the same toy.** Reviewers notice asymmetric bookkeeping instantly.

**Mitigation.** Create a **third evidence category**, kept strictly separate from (a) converging biological evidence (Hengen & Shew, ConCrit) and (b) untested predictions: **"proof-of-concept simulations of the mechanism."** State plainly: these demonstrate the *architecture behaves as specified in a toy*, are **not** evidence that biological consciousness works this way, and — per finding (3) — are **too shallow to test the criticality-dependence at all.** `prediction-framing.md` explicitly warns against conflating "criticality findings with FMT confirmations" (S204). The honest sentence: "no existing toy task has the depth required to test this; the claim is **untested**, and here is the depth-graded experiment that would put it at risk" — *not* "consistent with."

---

## RISK 5 — COMMS-RULE violations (Severity: MED)

1. **Modularism tripwire (highest of the comms risks).** The toy's native vocabulary — **"no-ESM ablation," "the ESM module," "ablate → 0.0"** — reintroduces exactly the "discrete separable box" framing that `neuroscience-communication.md` forbids ("NEVER … discrete brain modules"). Worse, it would **directly contradict the paper's own hard-won hedge** at line 897: *"functional selectivity, not the focal excision of a localized module, **which the theory does not posit**."* If integration imports "ablate the ESM module," the paper contradicts itself and trips the modularism rejection reflex. **Mitigation:** describe the toy as *"a controller with vs. without the explicit self-modelling capability"* / *"self-model function disabled,"* never "ESM module ablated." Keep "**two kinds of models**" framing throughout; never "four modules."
2. **"Non-conscious insects flourish" (finding 2 premise) vs the paper's agnosticism.** §6.4 (line 681) is carefully agnostic — *"insects (basic, if present)"*, and cites Barron & Klein (2016) who argue insects **may** be conscious. Importing "non-conscious insects flourish" as a flat premise **contradicts §6.4 and Barron & Klein.** **Mitigation:** phrase as *"organisms with minimal or absent explicit self-modelling"* — never assert insects are non-conscious.
3. **"Consistent with" / no-priority toward IIT/LZ/PCI and now Langton/reservoir computing.** The paper already credits IIT-Φ/LZ/PCI correctly (line 430). Finding (1)'s "criticality is for computation-of-a-certain-kind, not general computation" is **not FMT's discovery** — it's the reservoir-computing / Bertschinger–Natschläger / Boedecker result. `didactic-patterns.md` caution: credit with "consistent with," claim no priority. **Mitigation:** cite the reservoir-computing literature explicitly and use "consistent with"; do not let finding (1) read as FMT *owning* the computation-vs-criticality distinction.

---

## RISK 6 — Coherence of the "convergence" selling point vs finding (1)'s narrowing (Severity: MED)

The paper's credibility leans hard on "empirical neuroscience *independently converged* on our 2015 criticality claim" (abstract line 15; §3.7 line 401: *"consciousness tracks criticality across pharmacological, pathological, and physiological state changes"*; Hengen & Shew 140-dataset meta-analysis). Finding (1) **narrows** criticality's role to "maintenance mechanism for explicit-space modelling." These are compatible, but the paper must not simultaneously claim (a) *criticality = global consciousness-level marker* (for the convergence/credibility story) and (b) *criticality = enabling-condition-for-one-capability* (for finding 1). A reviewer will ask which one FMT actually claims. **Mitigation:** pick one consistent line — criticality maintains the substrate for the deep self-simulation whose loss *is* what the anesthesia/pathology literature measures as "loss of consciousness." State that explicitly so the narrowing *strengthens* rather than undercuts the convergence claim.

---

## RISK 7 — §4.2.4 "decisive survival advantage" vs finding (2) "small edge, rare, costly" (Severity: MED)

- **§4.2.4 (line 530):** consciousness *"confers **decisive survival advantage** in environments containing lethal contingencies."*
- **§4.2.5 (line 542):** phenomenal character is *"not a free-rider."*
- Finding (2): the advantage is **small** on simple/individual tasks; consciousness is **rare and metabolically costly**; simple organisms thrive without it.

Once finding (2) is added, an unmodified §4.2.4 makes the paper **internally inconsistent**: if the advantage is "decisive" in general, why is consciousness rare and costly? **Mitigation:** soften §4.2.4 to "decisive advantage **specifically in social / lethal-counterfactual niches**, small elsewhere" — which is precisely finding (2)'s scaling claim and makes the rarity/cost self-consistent.

---

## Summary table

| # | Risk | Severity | One-line mitigation |
|---|------|----------|---------------------|
| 1 | (2)+(3) → unfalsifiable/special-pleading; re-opens "too general" desk-rejection | **HIGH** | Replace "absence consistent with theory" with a pre-registered, monotonic effect-size-vs-depth/sociality prediction + explicit falsification criteria (a/b/c); `d`,`s` measured a priori from task structure |
| 2 | "criticality not required for general computation" contradicts line 464 ("any sustained computation requires") + Langton citation vs CRU-27 | **HIGH** | Scope criticality to open-ended self-simulation; acknowledge shallow computation is substrate-robust; cite reservoir-computing "consistent with" |
| 4 | Toy sims (1.0/0.0; 0.05) read as empirical FMT confirmation; §4.2.4 self-citation laundering; asymmetric bookkeeping | **HIGH** | Third evidence category "proof-of-concept simulation"; explicitly "untested," never "consistent with" a null |
| 3 | Line 424 / Table 4 blanket "toward subcritical → degrade" vs σ-independent toy death-readout | MED | Scope degradation claim to deep multi-step self-simulation |
| 5 | "ESM ablation" modularism (contradicts line 897); "non-conscious insects" (contradicts §6.4/Barron & Klein); no-priority credit | MED | "self-model capability disabled" not "module ablated"; "minimal/absent explicit self-modelling"; cite reservoir computing |
| 6 | Finding (1) narrowing undercuts "independent convergence" selling point | MED | Pick one line: criticality maintains the deep-self-sim substrate = what anesthesia literature measures |
| 7 | §4.2.4 "decisive advantage" vs finding (2) "small/rare/costly" | MED | Soften to "decisive in social/lethal-counterfactual niches, small elsewhere" |

**Single most important action:** do not ship finding (3)'s "absence is consistent with the theory" sentence in any form. Either it becomes a pre-registered depth-threshold prediction with stated failure criteria (Risk 1), or the criticality-of-explicit-modelling claim stays at the *mechanism* level and is flagged **untested** — never defended as a confirmed null.
