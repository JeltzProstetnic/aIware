<!-- Action: reference -->
# FMT Paper — Revision Notes (Session 217)

Specs for the next-session paper revision. Each resolves a "must-fix" from the Fable analysis (`docs/fable5-fmt-analysis/00-SYNTHESIS.md`) — reconciled with Matthias's clarification of his actual argument (the printed text mis-states the thinking; these are *wording/exposition* fixes, not substantive retractions, except where noted).

## F3 — Deflationism vs realism/supervenience seam (§4.3)

**Diagnosis:** the prose drifts into sounding like it posits a phenomenal fact "not contained in any complete description" → reads as property dualism the theory elsewhere denies. Matthias's actual position: the third-person description **exists and fixes every fact** (supervenience holds), but it (a) can't be *experienced* by being read, and (b) can't *discursively explain* the felt quality. Both gaps are **epistemic**, not ontological.

**Fix:** name the position and reword.
- This is **type-B physicalism / the phenomenal-concepts strategy** (Loar, Papineau) + the **ability hypothesis** (Lewis, Nemirow: knowing-what-it's-like = know-how, not new propositional fact).
- Replace "exists only in the running process and **cannot be extracted from any description, however complete**" → "cannot be **had** by description, only by instantiation" (acquaintance, not non-entailment). The description fixes the facts; it doesn't put you in the state (menu ≠ meal, both fully physical).
- Drop the "qualia lack independent causal power" hedge (only there to dodge epiphenomenalism, which the deflationary reading doesn't need) — qualia do causal work *qua* the self-model's evaluative representations.
- Replace the circular zombie rebuttal ("a self-referential loop that isn't self-referential — a contradiction" presupposes phenomenality ≡ closure) with the Frankish/Dennett **conceivable-but-impossible** move.
- Stop flirting with both "dissolved!" (deflationism) and "can't explain" (gap) as if identical — they're one specific position (phenomenal concepts); name it and commit.

## F4 — "Universal computation requires Class 4" (criticality necessity argument)

**Diagnosis:** the printed one-liner ("self-referential simulation is universal computation, and universal computation requires Class 4 dynamics") reads as the abstract-Turing claim → invites the laptop refutation. Matthias's actual argument is stronger and different; rewrite to state it. **Not a retraction.**

**Fix — restate as three explicit steps:**
1. **Capability.** Open-ended (universal) computation, *as a dynamical-substrate property*, occupies only the Class-4/edge-of-chaos regime — Class 1/2 settle (no computation), Class 3 scrambles (positive Lyapunov → no structured information transport). **State as a strongly-motivated principle** (Langton λ; Wolfram; the info-theoretic chaos argument) **NOT as a theorem** — the classes aren't rigorously enough defined to *prove* "Class 3 can't compute"; you argue it. Principle-with-argument = unkillable; theorem = the attackable version.
2. **Free instantiation.** Rich neural substrates *accidentally* instantiate a Class-4-capable automaton (Game of Life shows universality is cheap to instantiate) → an open-ended computational layer "for free" atop the implicit dynamics; no reason for evolution to decline it or pay for a costlier substitute.
3. **Evolutionary forcing.** An autonomous, self-referential, resource-constrained system *selected to use* that layer for self-modeling is driven to and held at criticality (self-organized criticality) — that's where the computation it exploits lives, and criticality maximizes dynamic range/susceptibility. The cortical automaton isn't Game of Life: higher-dimensional, far more open ruleset, *forced into the universal-computation regime by evolutionary demand*.

**Keep the trichotomy explicit and load-bearing:** *capable of* universal computation → *actually doing* it → *doing maximally efficient autonomous self-modeling*. This disarms every counterexample: laptop = capable but **heteronomous** (externally clocked/programmed) so never forced; chaos/fractal = can't host it at all → "ultimate seizure," not experience. Both excluded, for different reasons.

**Terminology guard:** never write "the laptop is not universal" (it IS Turing-universal). Write "universal but **heteronomous / not self-referential**."

**Narrative payoff (ties F4 + F7 + convergence into ONE story):** step 1 is the Jan-2015 claim; the empirical criticality literature (Toker 2022, Hengen & Shew 2025, ConCrit 2026) is *convergent confirmation* arriving 7–11 years later from an independent discipline. Cover-letter line: "derived the criticality requirement in 2015 from computational principles; empirical confirmation followed 2022–2026."

## PP-scoping reframe (dissolves the "thin differentiation from PP" discard-knock → turns it into a positive)

**Claim:** PP/predictive processing is a theory of **perception and inference**, NOT of consciousness. It describes information processing and gestures at which signals "may become conscious or not" but has **no account of why/when** any of it is conscious — the same explanatory gap, untouched.

**Receipts:** Hohwy & Seth (2020) concede PP is a *framework for locating NCCs*, "largely orthogonal" to what *makes* a state conscious. Seth reaches a consciousness claim only by *adding* a self-model ("controlled hallucination," "beast machine," interoceptive selfhood) — i.e., importing FMT's territory.

**Positioning for the paper (replace any defensive "we differ from PP" hedging):** PP supplies the inference dynamics (the implicit/predictive layer); FMT supplies the consciousness-making layer (the explicit self-model + closure + criticality that determine *which* inferential systems are conscious). FMT can take PP's prediction-error machinery wholesale as the implicit layer and add what PP structurally lacks. The clinical-breadth overlap = PP explaining the information-processing face of each syndrome, FMT the consciousness face. **Complementary, not rival; FMT is PP's missing top floor.** Scope PP, don't dismiss it ("PP is right about inference, silent on consciousness").

## Also (from citation audit `docs/fmt-citation-audit.md`)
- Fix abstract: "Bhatt, D.K. (2024)" → correct author **Xu et al.** (copied from Toker author list).
- Chowdhury (2026) + Katlowitz (2026) wrong titles (each cited 3×, load-bearing); add Katlowitz DOI.
- 9 detail-wrong, 6 preprint-only flagged — metadata fixes, convergence cites all real/published.
- `references.md` lives at `docs/references.md` (not project root).
