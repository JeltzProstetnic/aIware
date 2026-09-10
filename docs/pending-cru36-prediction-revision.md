<!-- Action: reference -->
<!-- Tracked-by: AIW-110 -->
# CRU-36 → FMT prediction-set revision — decision brief

> ⚠️ **This brief is NULL-FORWARD and INCOMPLETE for paper drafting.** It foregrounds the CRU-36 null and omits the banked positive closure/criticality evidence. For §8.9 / companion-paper / any "what has crucible shown" work, use **`docs/crucible-evidence-ledger-digest.md`** (complete-data digest of crucible's evidence ledger), NOT this brief. (Root cause of the S267 undersell.)

**Created:** S259 2026-07-13 (WSL). **Source:** crucible `docs/` (CRU-36 null + 2026-07-07 meta-review + 2026-07-08/09 decisions), synthesized read-only. **Purpose:** lay out the prediction revisions + the 3 theory decisions only MG can make, so pre-registration can proceed. This is context/analysis; status lives in AIW-110.

## A. What CRU-36 showed (the null)
CRU-36 toggled self-referential re-entry (ON/OFF) on a critical spiking reservoir at delay τ=15. Result: the **passive** reservoir (closure OFF) already maintains the cue near-perfectly to ~75 steps (**H_native≈100 ≫ τ=15**); closure ON **never beats** OFF at any re-entry scale/delay (neutral at re≤0.5, destructive at re≥3). Per the 2026-07-07 meta-review **Root C**: *no experiment toggles a real recursive closure loop (Φ(m*)=m*); none of P1/P2/P3 exercises the constitutive mechanism.* MG's reading: the null is **FMT-consistent** — closure and criticality *do nothing on their own*; they are **enabling conditions for the modelling step**. Testing closure as if it were the effect was the category error; that closure adds nothing over the critical substrate's native capacity is exactly what FMT predicts.

## B. The two closures (from `paper-clarification-two-closures.md`)
- **Closure-1 (BUILT / engineered):** the world↔self *control* ring — External-model output flows down to modulate autonomous subsystems (body/sensor control). The engineerable, toggleable knob.
- **Closure-2 (EMERGENT):** the self-in-world *predictive* loop — the ESM sits embedded in the EWM and, by predicting, shapes its own input. Not wired; it emerges once ESM-nested-in-EWM is trained to predict.
- CRU-36's re-entry was **neither** — it was feedback on a homogeneous reservoir ("blob-on-blob"), which collapses the four models (IWM/ISM/EWM/ESM) into one undifferentiated pool, leaving no distinct self/world models for a loop to close *between*.

## C. Proposed prediction revisions
- **P1 — KEEP as basic-science anchor.** Current: learn a causal model, transfer to a novel task (categorical gap vs baseline). Confirmed in-model; proves the mechanism is implementable + FMT-consistent. Caveat: general to ANNs, not unique to FMT.
- **P2 — REDIRECT.** Current: memory-curve *step* vs σ (XOR memory shapes, CRU-23/26/27). Proposed: **task-outcome categorical collapse** — de-tuning criticality categorically collapses the P1 observational→causal-transfer *modelling* task **only with closure ON** (replace XOR, which has no self-model/closure, with the observational-causal-transfer task that recruits ESM perspective-projection + world model).
- **P3 — REDIRECT.** Current: EWM-coverage → proportional ESM degradation. Proposed: **ESM↔IWM/EWM interface causal chains + reproduce biological signatures** (analyze the ESM/IWM "surfaces", trace causal chains, predict/reproduce cellular/synaptic signatures — anchors FMT in basic science like P1).

## D. Three OPEN theory decisions (block pre-registration) — MG's call
1. **Which criticality is P2's IV?** (formalization §4.3: both-required / avalanche-σ / edge-of-chaos.) Crucible leans **resolve toward Class-4 capability** (avalanche-σ≈1 and Lyapunov/edge-of-chaos are *different* transitions — Kanders 2017: they don't co-occur — but both deliver universal-computation capability). Meta-review's own pick was option 1 "both required" (σ≈1 AND λ≈0) as most falsifiable.
2. **Ratify P2's DV as task-outcome-categorical** ("observational-causal-learning collapses off-criticality, with closure ON"), NOT a memory-curve step/shape. (Recorded resolved-yes 2026-07-08 evening — needs MG ratification into aIware canon.)
3. **Resolve formalization(rate-ESN/Lyapunov) vs S242(spiking/avalanche) contradiction.** Crucible frame: *two instruments for the same capability band at different substrate levels* (rate reservoir + spectral radius for abstract Class-4 proof; spiking avalanche for biological realism) — different audiences, both correct.

> Note: crucible's docs already record these three as *resolved* under MG's 2026-07-08 "capability-first" framing and **routed to aIware to make canonical**. Treat D as "ratify + write into aIware canon (paper/formalization)", not "decide from scratch" — but confirm each with MG before locking.

**RATIFIED — MG, S266 2026-07-24 (all three capability-first, as recommended). Now aIware canon:**
1. **P2 IV = Class-4 capability.** The substrate must support universal / free computation; avalanche-σ≈1 and Lyapunov λ≈0 are *interchangeable instruments* certifying it, so the σ-detuning arm is dropped. Dissolves the "which criticality" (Root A) ambiguity into a capability requirement — consistent with §3.7's Wolfram Class-4 grounding.
2. **P2 DV = task-outcome categorical.** De-tuning criticality categorically collapses the observational→causal-transfer modelling task, *only with closure ON*. Not a memory-curve step/shape. XOR retired (no self-model/closure → doesn't exercise the constitutive mechanism).
3. **Formalization = two instruments, one capability band.** Rate-ESN + spectral radius (abstract Class-4 proof) and spiking + avalanche (biological realism) certify the *same* capability at different substrate levels — complementary, not contradictory. Moot-by-#1.

**Residual AIW-110 work (→ folded into AIW-121 v13 epic):** reword §8 P1/P2/P3 to match these + update `.claude/knowledge/prediction-framing.md`. No experimental-design work remains on the aIware side (crucible owns that, done).

## E. New modelling-taxonomy (MG 2026-07-08)
Modelling stack: **self-model → 3rd-person (other) model → free modelling** (abstract/counterfactual). **Free modelling manifests as idle activity / PLAY** — a candidate explanation of the **play↔consciousness correlation** across animals. **Tool use = another modelling-step kind** (modelling affordances / causal body-world extensions). These make "closure enables the modelling step" concrete: the steps are enumerable capabilities (self / other / free-play / tool) whose presence + efficiency are the DVs future tests should target.

## F. VM-tax reframe (MG 2026-07-09)
**Consciousness pays the VM tax:** self-referential closure is a virtual-machine / simulation layer on neural hardware — intrinsically slow + lagging, so it loses on fast reactive tasks. **Nonlinear "now"-solving is the SUBSTRATE's native strength** (why the net is first in the chain). The conscious subprocess does simulation + optimization, as-needed and compute-scaled → division of labor. Recontextualizes the R1-S0-pre reafference null (closure inert there) as **confirmatory**: reafference cancellation is substrate "now"-work; closure there is pure tax. **Testable signature:** capability scales with internal-simulation budget ("thinking time") **only when closure is ON**; the reactive substrate is flat in thinking-time. Digital-twin clincher: we build internal twins despite having ANNs precisely where reactive approximation fails (counterfactual / OOD-mechanism / optimize-over-model) — the VM earns its tax exactly there, not on interpolative now-tasks.

## G. Loose ends / contradictions the docs flag
1. **Criticality demand-gating** (MG 2026-07-08 late → 07-09): is criticality always-on or demand-gated/scale-dependent? Current lean: criticality is intrinsic/always-on; R1 manipulates **closure + extent**, not σ-detuning → the σ-detuning arm is dropped. This dissolves the "which criticality" (Root A) ambiguity into a capability requirement.
2. **Blob vs structure:** CRU-36's substrate is NOT memory-limited (H_native≈100 ≫ τ=15) — the gating issue is the *absence of differentiated self/world models*, not capacity. Pushes the connectome-structure question (CRU-28) to 2nd order.
3. **Core DV unsettled:** the detection DV (reafference cancellation) is dead (structurally an adaptive-noise-cancellation problem with no self-vs-forward-model deciding regime); pivoted to a self-vs-exogenous **classification** DV — but the VM-tax lens questions whether classification is VM-work only when it needs *counterfactual* simulation, else it's substrate discrimination (trap relocated). Crucible's next session must fix the R1 task with MG.

## Downstream targets when executing AIW-110
- FMT paper §8 predictions (P1/P2/P3 wording) + `.claude/knowledge/prediction-framing.md`.
- Modelling-taxonomy (E) → paper + book candidate + crucible CRU-37 cooperation-apex arc.
- VM-tax (F) → candidate paper paragraph (why the conscious edge is compute-scaled/long-horizon, not reactive).
- Coordinate with AIW-92/AIW-94 (two-dials criticality) to avoid §3.7/§8 churn.
