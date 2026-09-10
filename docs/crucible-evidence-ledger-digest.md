<!-- Action: reference -->
<!-- Tracked-by: AIW-110, AIW-121 -->
# Crucible FMT Evidence — aIware digest (complete-data source for §8.9 + companion paper Gruber 2026d)

**Source:** crucible `docs/results/fmt-evidence-ledger.md` + `backlog.md` + `docs/decisions.md`, read-only, verified S267 2026-07-24 (WSL). Canonical experimental authority = crucible; this is aIware's working digest so paper-side work uses COMPLETE data.

**ROOT-CAUSE NOTE (why this file exists):** `docs/pending-cru36-prediction-revision.md` foregrounds the CRU-36 *null* and does NOT carry the banked positives below. Drafting §8.9 or the companion paper from that brief alone UNDERSELLS the evidence (it did, once — S267). **Always draft paper/companion content from THIS digest, not the null-forward brief.**

**S269 CORRECTION (2026-07-24):** item A.1 below (closure-maintenance) was itself a FALSE positive inherited from crucible's ledger row #1 — re-verified against the runnable code (`scripts/verify_closure_maintenance.py`) and DROPPED. Lesson the other way: the digest is only as good as the ledger it mirrors; **verify a banked positive against runnable code before any paper use** (the underselling risk and the overselling risk are both real).

## A. MODEL evidence — BANKED (survived adversarial replication), toy/numpy scale

1. **~~[BANKED positive — RETRACTED S269, 2026-07-24]~~ Closure-maintenance on an undifferentiated blob is a NULL.** Re-running the cited code (`experiments/closure_maintenance.py`, CRU-40 Part A) at its own research defaults (interference 0.5, delay 40, 5 seeds) gives closure ON−OFF ≈ **+0.08, 95% CI crosses 0**. The large advantage (+0.5 to +0.72) appears ONLY at near-zero interference (0.05) + long delay (40–80) = a trivial leaky-integrator effect that a **linear delay-line matches** (B0 gate G9: self-model ≯ delay-line). The prior *"read-only control FAILS → the maintenance is the recursion"* positive is **not supported by the code**, and the crucible red-team (`cru40-design-redteam.md`) rules a rate-ESN positive *"triply-measured impossible."* FMT-consistent (sibling of the CRU-36 null, §C): an undifferentiated pool has no distinct self/world models for a loop to close between. **DROPPED from FMT §8.9 + companion §4.1 (MG ratified S269).** crucible ledger row #1 correction + a possible differentiated-substrate redo to reach a real result: tasked to `cru` via inbox 2026-07-24.
2. **Criticality does real work — it COMPUTES, demand- AND scale-gated.** The edge-peak in compute capability appears ONLY for medium-hard tasks and sharpens with N. The earlier "compute floor" was a readout-symmetry bug (fixed via input bias), not a null. (CRU-40 Part A, `cru40-compute-leg-criticality.md`; 6 confirmations CRU-27/33b/c/d/B0.)
3. **P1 — a self/other model (ESM) causally carries a capability its ablation cannot.** Observational death-transfer: FMT **0.98** vs ESM-ablated **0.78**, **Cohen's d = 2.44, p = 2e-17**; transfer = 1.0 every FMT arm, 0.0 ablated. Strongest confirmed prediction. (CRU-23; needs the CRU-22 mechanism build; categorical/shallow task.)
4. **A self-model-gated planner scales with problem depth where competent reactive policies can't.** Fitted self-model + planner beats a FULL reactive bracket — tabular-Q, action-conditioned FQI + ensemble, behavioral clone, wall-follower (all 0.00–0.33); 6/6 gates green; MG-ratified. (CRU-40 B1 R1 gridworld GO, `cru40-b1-R1-S0pre2-gridworld-fitted-arms.md`; numpy; world-conditional RT-1 + capacity-relative RT-6.)
5. **Prospective self-in-simulation (closure) yields a behavioral survival advantage.** Self-preservation via the self-model's own survival prediction: survival **0.29–0.33** vs reactive **0.17–0.25** (5/10/20 seeds). First positive closure-on-performance result. (CRU-32b; toy, small magnitude; the predictive-*perception*-mask variant showed NO robust benefit.)
6. **(partial) Closure maintenance is content-specific.** Holds decodable operands (D = 20–45) across a delay while a scrambled generic-drive control stays at chance (gate G2). BUT at B0 spiking scale the self-model did NOT beat a passive linear delay-line on downstream capability (gate G9 failed): maintained-decodable ≠ computable-upon. (CRU-40 B0 atom, `cru40-partB0-atom.md`.) Honest half-result.

**Supporting dissociations:**
- **CRU-29:** clean 3-way closure dissociation — P1 transfer DV carried by ESM mechanism-binding (1.0 vs 0.0 ablated); projection re-entry reshapes the self-model (selfΔ≈0.99); the perception mask lowers self-knowledge R (0.987→0.90). "Closure" = ≥3 distinct loops (Root C).
- **CRU-27:** nominal σ=1 is NOT the edge of chaos for the leaky ESN (true edge σ≈2.6); memory + computation co-peak in the ordered regime, co-collapse at the edge — no dissociation → P2 reframe: FMT requires universal-computation *capability* (Class 4), not criticality per se.

## B. The OPEN / decisive goal (NOT banked — state as open)
The decisive result — a **scaled, spiking, closure-driven free-modeler whose capability DIES when the loop is cut** — is not yet achieved. The **stationary-closure impossibility theorem** (`cru40-b1-R1-phase0-statedep-DEAD.md`, Fable-found + Opus-reproduced) proves the loop-cut CANNOT be a clean binary oracle test on any deterministic, episode-stationary task (generic recurrence computes any fixed table). Consequence: self-re-entry necessity is a **capacity/learning** property → the decisive test must be **graded, capacity/novelty-relative**, on an open-ended / co-adaptive workload where novelty outruns the amortizer. Aligns with the two-dials (Extent×Complexity, AIW-94) and R5 (salvia = graded detune). The misbind/fixed-task path banked 3 Fable-ratified DEADs.

## C. CRU-36 — the null, in its correct (minor) place
Spiking self-referential re-entry on a HOMOGENEOUS critical reservoir → no advantage over the passive substrate (H_native≈100 ≫ τ=15; closure ON never exceeds OFF). **FMT-CONSISTENT, not a refutation** — mis-wired feedback on an undifferentiated blob with no distinct self/world models between which a loop could close; it tested closure as if it were the effect, not the enabling condition. Diagnostic: it sharpened the closure-gated, differentiated-substrate design.

## D. Differentiation from rivals (differentiating predictions, not yet confirmed differentiations)
- vs **Predictive processing / active inference:** PP has no apex/closure/computational-class claim; vanilla predictive coding relaxes to a MAP fixed point (Class-1). Cannot predict a closure-caused maximally-stable self-attractor nor a level-graded closure-OFF collapse. FMT test: closure-OFF at matched recurrence abolishes the self-circuit's supremacy.
- vs **IIT:** redescribes collapse; FMT predicts the ORDER (self-body core last, world circuits first) + the closure-causation.
- vs **GWT:** no stable-self-attractor; FMT predicts the closure-bearing self is the most stable / longest-living circuit.

## E. REAL-world anchors (mostly consistent-with; R1 the FMT-specific exception)
R1 architecture match (Fedorenko-lab fMRI: ~5%-volume distributed periphery maps ~1:1 to FMT components — FMT-SPECIFIC); R2 criticality (macro-scale, demand-gated); R3 PCI ≥ 0.31; R5 salvia/ketamine graded self-dissolution with persistent modeling; R6 anaesthesia collapse order (self-body core last out / first back), closure-caused, graded-by-level.

## Honest scope (CRU-39 discipline)
Foreground the positive, state the ceiling: model evidence = toy/numpy-scale mechanism demonstrations + one strong statistical prediction (P1, d=2.44); real evidence = mostly consistent-with (R1 the FMT-specific exception). **Banked is banked, open is open — never conflate.**
