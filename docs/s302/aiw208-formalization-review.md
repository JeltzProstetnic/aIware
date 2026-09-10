<!-- Action: act -->
<!-- Tracked-by: AIW-208, AIW-204, AIW-206 -->
# `Gruber2026b` — Fable review of the FMT formalization roadmap (S302, 2026-08-12)

**File reviewed:** `paper/fmt_formal/fmt-formalization.md` (693 lines, last substantive commit 2026-08-08).
**Why:** the FMT master cites it **four times** as an unpublished manuscript, so readers cannot obtain it.
MG's instruction (2026-08-12): *"first fable pass on that draft, it probably needs updates from cru and
theory and has to be careful about the patent thing."* All three concerns were founded.

**VERDICT: PUBLISH-AFTER-FIXES.** Publishing as-is would (a) disclose unpublished crucible methodology
into EPC absolute novelty and (b) put MG's name on a paper stating a principle structure his own project
retired ten days earlier.

---

## 1. ⚠ PATENT — BLOCKER, but surgically removable

**HIT 1 — ENABLING, line 563** (§8 "Ablation-validity audit"). Discloses the **CRU-58** result together
with the **dominant-loop-mode probe**, in reconstructable procedural detail: that zeroing the self-model's
efferent block *decomposed one irreducible closed system into two* (intact arm one strongly-connected
component, ablated arm two), plus a three-step audit recipe with its failure modes and gate semantics.

Provenance confirmed against crucible: `~/crucible/docs/results/cru58-closure-off-is-two-closed-systems.md`,
with the probe appearing in `cru78-localization-landscape.md` and `cru40-b1-R1-D1-dec-builder.md` — i.e.
localization/decompilation tooling adjacent to the **CRU-72 pipeline on the protected list**.

**This is not a name-plus-gloss.** It is a procedure plus an unpublished experimental finding plus a
description of the substrate's regional structure. Under EPC Art. 54 that is permanent.
**Fix: delete the specifics and the probe; replace with one generic sentence** — *"ablations on recurrent
substrates can relocate rather than remove a loop; any ablation protocol must verify removal, e.g. via
connectivity analysis of both arms."* SCC decomposition alone is textbook and safe; the probe and the
result are not.

**HIT 2 — NOMINATIVE but self-defeating, lines 547 / 601.** *"Phase 4 results from the architectural
ablation gridworld will be incorporated before publication."* Not a disclosure in itself, but a standing
commitment that drags crucible results into a public artifact before filing — and it makes publishing
*without* them a self-contradiction. **Must be rewritten either way.**

**HIT 3 — CLEAR, lines 549-556.** Reservoir substrate with tunable spectral radius, gating family G,
recursive depth ≥ 2: all generic published constructs. **Confirmed absent from the whole draft:** the
connectivity table, τ heterogeneity, the second-filter-state return path, the three-factor rule, M1s3, and
the embodiment seam. A skilled reader cannot reconstruct the non-foldable loop or the credit-routing rule.

**HIT 4 — CAUTION, lines 140-144.** The localization-gate methodology note reveals that gated localization
runs exist in the unpublished programme, but discloses no mechanism. Defensible as theory-side method.

⇒ **With Hit 1 removed and Hit 2 rewritten, the draft drops to CLEAR.**

## 2. Staleness — it states a theory that was retired ten days ago

| line | superseded claim | current position |
|---|---|---|
| 25 | *"five principles: criticality, virtual qualia, a redirectable ESM, variable permeability, virtual model forking"* | **`AIW-138`, MG-settled 2026-08-03: THREE principles.** Criticality → signature of P1; virtual qualia renamed and merged into P3; redirection/permeability/forking → consequences. |
| 264 | *"Consciousness **requires** σ ∈ [σ_low, σ_high]"* | Criticality is what P1 looks like in tissue, not the principle. **And crucible CRU-27 undermines the band empirically:** nominal σ=1 is *not* the edge of chaos for a leaky ESN (true edge ≈ 2.6). ⚠ §§4.4-4.5 already hold the correct hedged posture — §4.2 contradicts the draft's own later sections. |
| 553 | *"edge-of-chaos dynamics as computational prerequisite"* | same demotion; CRU-27 reframes to universal-computation *capability* (Class 4) |
| 559 | Prediction 1: ESM ablation produces a **categorical** behavioural difference | **Contradicted by the stationary-closure impossibility theorem** — a loop-cut cannot be a clean binary test on any deterministic, episode-stationary task. Must be graded/capacity-relative. Also violates pattern 18 (advantage, never necessity). |
| 560 | Prediction 2: *"**cannot** sustain universal computation… should fail **regardless of architecture**"* | Barrier language on both the criticality and the capability axes. Licensed form is **PRICE, never BARRIER**. |
| 345 | seizure *"hypersynchronous, hence locally Class 2/3"* | **Explicitly forbidden by the S300 caution** — the ictal route is phase- and scale-dependent and unsettled. Licensed: *"exit from Class-4 (route unsettled) → Class-4 involvement drops → unconscious."* |
| 73, 183, 414 | cross-references to *"Gruber, 2026, v7"*, §3.6/§3.7/Prediction n | parent is at v13+ with a restructured principle set. **A published companion citing internal draft version numbers is not acceptable.** Re-pin against the Zenodo version. |

**Checked and NOT stale:** §6.1's weather-simulation contrast (consistent with pattern #36 — it is the
same device); implicit-models-distributed in §4.1 (consistent with the pattern-32 ruling); the L1/L2
open-lemma treatment, which is exactly the current epistemic posture.

## 3. ⚠ The draft contains its own citation defects — the same class just fixed in the master

- **Kauffman (2005)** → the paper is **1987** (*J Soc Biol Struct* 10(1):53-72). Wrong in text (459) and
  reference list (647).
- **"Bhatt, D. H., Zhang, S., & Bhatt, W. B. (2009)"** → the third author is **Gan, W.-B.** (Wen-Biao Gan).
  **A corrupted author name of exactly the shape a fabrication audit exists to catch.** Also: the paper is
  about dendritic spine dynamics, which is thin support for the *"intracellular signalling constitutes its
  own learning intelligence"* claims at lines 37/110 — Bhalla 2014 carries those better.
- **Hengen & Shew (2025)** reference (line 641) is a **placeholder with an invented-format title**
  (*"Meta-analysis of neural criticality across 140 datasets. [Consolidated in ConCrit framework.]"*). The
  real paper is *"Is criticality a unified setpoint of brain function?"*, **Neuron**, 2025.
- **Orphaned** (in the list, never cited): Baars 1988, Carhart-Harris 2014.
- **Verify before use:** Oizumi/Lim/Kanai 2025 author *order* (the announcement suggests Oizumi and Kanai
  are co-first with Lim as co-author); Smithe (2024) has no venue — complete it from the arXiv version;
  Wetterich 2022a arXiv:2203.14081 not directly resolved.
- **Verified real:** Algom & Shriki 2026 (ConCrit, *NBR*); Oizumi/Lim/Kanai 2025 (`10.31234/osf.io/agupq`);
  Wetterich 2022b (PRD 105:074502).

### ⚠⚠ The structural catch: publishing 2026b half-fixes the problem it is meant to fix
**`Gruber2026c` (cosmology) is cited five times in this draft as "Manuscript"** — reproducing the exact
unobtainable-citation defect that motivated this review. Publishing 2026b to resolve the master's four
dangling citations, while 2026b itself dangles on 2026c, is half a fix. Decide the 2026c strategy in the
same pass: hedge as "in preparation", publish it too, or trim the SB-HC4A dependencies.

## 4. Quality — honest read

**It is a roadmap describing a formalization, not a formalization** — and it says so plainly in the
abstract and §1.3, which is the right register for something titled *"A Recommended Approach"*. **Its best
feature is the scholarly honesty of §§4.4-4.5**, which declare L1/L2 open and refuse the entailment; that
is above the field's norm.

Real defects: the permeability definition (line 160) writes transfer entropy *"between density regions"* —
TE is defined between time series, so as written it is gestural, not well-formed. **Symbol collisions:** ρ
serves as the model density (§2.2), the recursion map ρ_n (§6.3) *and* the group representation ρ(g)
(§2.5); Φ is both the self-representation map (§6.4) and the extent fraction Φ_ext (§4.7), sitting pages
from a discussion of IIT's Φ. The stated audience is a mathematician collaborator, who will notice in
minutes. **Internal tension:** line 58 makes the implicit-explicit boundary *"graded, not binary"* while
line 80 posits a hard ontological threshold ν_crit — coherent, but the draft never says how.

**Level: after the fixes, a legitimate Zenodo preprint.** Not journal-grade, and does not claim to be.

## 5. What crucible would add — and why most of it cannot go in yet

`docs/crucible-evidence-ledger-digest.md` exists and is current (S269-corrected).

- **P1/CRU-23** (banked): observational death-transfer, FMT 0.98 vs ESM-ablated 0.78, d=2.44, p=2e-17 —
  **this is the draft's own Prediction 1, now confirmed at toy scale.** ⚠ **And folding it in is exactly
  what the freeze forbids.** The draft's strongest available upgrade is the one thing it cannot have.
- **CRU-27** forces the §4.2 σ-band revision — a *contradiction*, not merely an addition.
- **The stationary-closure impossibility theorem** forces the Prediction-1 rewrite; the graded framing can
  be motivated **theory-side** via No-Free-Lunch unrolling, which is the patent-safe route.
- **CRU-40 B1**, **CRU-32b** support §5 and the Phase-4 motivation — same freeze constraint.
- **R1** (Fedorenko-lab architecture match) is a **published-data** anchor, so it may be citable without
  touching the implementation layer. Relevant to §2.7's localization question.

⇒ **Recommended resolution: publish the roadmap WITHOUT results**, rewriting lines 547/601 to *"computational
validation is under way in a companion programme and will be reported separately"*, and revise the two
claims the banked evidence contradicts using theory-side arguments only.

## 6. Ordered fix list (1-6 mandatory, 7-8 recommended)

1. **(PATENT)** Delete the CRU-58 specifics and the dominant-loop-mode probe from line 563; replace with the
   generic verify-removal sentence.
2. **(PATENT + self-consistency)** Rewrite lines 547/601 — drop the incorporate-Phase-4-before-publication
   commitment.
3. Rewrite §1.1 line 25 to the three-principle structure, and re-pin every *"v7 / §x.y / Prediction n"*
   cross-reference against the published Zenodo version.
4. Criticality demotion pass: line 264 requirement → operating-regime hypothesis matching §4.4's own
   posture; line 553 prerequisite → capability framing; line 560 drop *"cannot"* / *"regardless of
   architecture"*.
5. Prediction 1 (line 559): categorical → graded/capacity-relative, motivated theory-side.
6. Citations: Kauffman **1987**; Bhatt/Zhang/**Gan**; Hengen & Shew real title and venue; complete Smithe;
   delete or cite Baars and Carhart-Harris; verify Oizumi author order; **decide the Gruber 2026c strategy**.
7. Line 345: seizure → the route-agnostic licensed form.
8. Symbol hygiene (ρ triple-use, Φ collision), a well-formed TE definition, one sentence reconciling the
   graded boundary with the hard ν_crit, one sentence framing §2.3's necessity claims as definitional.
