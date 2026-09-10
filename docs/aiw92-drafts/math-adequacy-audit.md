# Math-Adequacy Audit — "Two Kinds of Criticality" (the two-dials model) for FMT

**Reviewer brief:** mathematical-physics review of whether the *extent vs. complexity* ("two dials") claim is given a proper formal/mathematical treatment in FMT, or only a verbal/operational one.
**Sources audited:**
- `paper/full/four-model-theory-full.md` §3.7 (criticality requirement, lines 381–448), Table 1/1b (lines 162, 182), §5.1/§5.3 (lines 536–576).
- `docs/aiw92-drafts/fmt-paper.md` — the proposed Pattern-2 insertion block + Table-1 additions (the treatment under audit).
- `paper/fmt_formal/fmt-formalization.md` — the formalization roadmap (§3.5 C(t), §4.1–4.6 criticality).

**One-line verdict:** *Partially addressed, leaning to "not yet."* The draft is a careful, honest **verbal/operational** treatment. It is **not** a formal one. No equation, order parameter, or measure is defined for either dial; the orthogonality is asserted, not constructed; "processing volume" is undefined; and the fmt_formal roadmap does **not** cover the two-dials decomposition at all (it formalizes a *single*-axis criticality threshold). The draft also slightly over-reaches in one place (the "second axis" Table-4 warning is correct but the draft's own prose treats extent/complexity as if they ride the existing single critical-point axis, which they do not).

---

## Q1 — Coherence of "two orthogonal observables off ONE critical point"

**Verdict: The verbal claim is coherent ONLY under a specific reading the draft gestures at but never pins down; as written it risks the incoherence you flagged.**

The physics worry is real. At a single critical point a homogeneous system has *one* order parameter, *one* set of critical exponents, *one* correlation length ξ. "Two independently variable dials off one critical point" is, taken literally, a category error — you cannot move "extent" and "complexity" independently if both are just "distance from the one critical point σ→1 / λ_max→0." The current paper reinforces this single-axis reading everywhere: Table 1 (line 162), Table 1b (line 182), Table 4 (line 562) and the entire fmt_formal §4 treat criticality as **one** scalar coordinate (sub-/at-/super-critical). The draft's own sentence "two orthogonal dimensions read off one edge-of-chaos substrate" is therefore in tension with the rest of the paper unless the substrate is explicitly treated as **spatially heterogeneous**.

**The cleanest rigorous formulation (which the draft hints at but does not state):** abandon "one critical point" and replace it with "a substrate that is a *field* of locally-critical regions." Then the two dials are mathematically distinct objects living on different mathematical structures:

- **EXTENT** is a measure over *space*: the fraction (or measure) of the substrate whose **local** dynamics sit in the Class-4 regime. Rigorous candidates, in increasing strength:
  - Φ_ext = |{ i : local branching σ_i ∈ [σ_low,σ_high] AND local λ_max,i ≈ 0 }| / N  — the fraction of functional units meeting the criticality criterion locally.
  - The normalized size of the **giant critical cluster** (largest connected component of locally-critical, mutually-correlated units) — a percolation order parameter P_∞. This is the mathematically cleanest single number, and it is genuinely an *order parameter of a spatial phase transition* (percolation), distinct from the temporal/avalanche critical point.
  - The correlation length ξ relative to system size L (ξ/L → O(1) ⇒ integration spans the substrate). ξ is the natural "how far does criticality reach" quantity and is exactly the integration intuition.
- **COMPLEXITY** is a property of the *dynamics within* the critical region(s): the algorithmic/statistical richness of the trajectories the critical subsystem computes — Lempel-Ziv complexity of the activity, or an entropy-rate / excess-entropy measure restricted to the recruited cluster. This is **not** a spatial measure; it is a measure on the dynamics (state-space trajectory), conditioned on being critical.

Under this reading the two are genuinely orthogonal: you can grow the critical cluster while keeping each cell's computation simple (extent↑, complexity≈const), or hold a small cluster doing intricate computation (complexity↑, extent≈const). **There is no contradiction with "one critical point" because there is no longer one critical point — there is a critical *phase* with spatial structure.** This is a defensible, standard move (it is how spatially-extended critical systems are actually analyzed: percolation order parameter for spatial extent, dynamical/algorithmic complexity for the on-cluster computation).

**Where the draft lands:** it *names* "spatial fraction of the substrate currently participating in Class-4 dynamics" (good — that is the percolation/fraction idea) and "differentiated richness of the Class-4 patterns themselves" (good — that is the on-cluster complexity idea). So the draft has the **right intuition**. But it never (a) says the substrate is spatially heterogeneous / a field of local critical points, (b) names a spatial order parameter (fraction, P_∞, or ξ), or (c) acknowledges that this *replaces* the single-critical-point picture used in the rest of §3.7 and all of fmt_formal §4. As written it asserts orthogonality on top of a single-axis substrate, which is precisely the incoherence risk. **Gap = the heterogeneity premise and the spatial order parameter are missing.**

**Fix:** add one sentence establishing spatial heterogeneity ("criticality is not a single global operating point but a spatially varying field; locally critical regions tile the substrate") and name extent as a *spatial* order parameter (fraction-at-criticality, or giant-critical-cluster size, or ξ/L) explicitly distinct from the temporal critical point σ/λ_max that detects whether a *region* is critical at all.

---

## Q2 — Operationalization / observable mapping

**Verdict: Observable mapping exists at the verbal level and is internally consistent on the PCI point, but the EXTENT observable is under-specified and partly circular as stated.**

The draft's Table-1 additions propose:
- EXTENT → "fraction of cortical parcels meeting the criticality criterion; integrated-information / global-integration (Φ-family) as convergent index," with the seizure falsifier (must score LOW for a hypersynchronous seizure).
- COMPLEXITY → "Lempel-Ziv complexity; perturbational complexity (PCI)," with the PCI-is-differentiation-not-criticality caveat.

**What is right:**
- The COMPLEXITY mapping is consistent with the paper's existing commitments. The PCI caveat (line 418) lands correctly: PCI sits on the differentiation/complexity axis, *not* the extent axis. The draft preserves this without contradiction. ✔
- "Fraction of cortical parcels meeting the criticality criterion" is the correct *type* of object for extent (a spatial fraction). ✔
- The seizure falsifier is the strongest part: it correctly forces EXTENT ≠ co-activation. ✔ (See Q-aside below.)

**What is wrong / under-specified:**
1. **Φ as the extent index is a mis-assignment, or at least a contestable one.** Integrated information Φ is canonically the *integration* quantity, and the draft equates integration↔extent. But Φ in IIT is *not* a spatial-fraction measure and is *not* "how much of the substrate is critical" — Φ is a measure of irreducibility of the whole system's cause-effect structure, which conflates integration AND differentiation (Φ is high only when the system is both integrated *and* differentiated). Using Φ as the EXTENT (pure-integration) index therefore double-counts complexity and breaks the orthogonality the draft is trying to establish. The cleaner extent index is a **percolation/fraction/correlation-length** measure (Q1), not Φ. If Φ is cited at all it should be cited as a measure of the *joint* corner (both dials), not of extent alone.
2. **Potential circularity in "fraction of parcels meeting the criticality criterion."** If a parcel "meets the criticality criterion" by *globally-estimated* σ/α (which is how σ and DFA-α are actually computed in the paper — whole-recording estimates), then "extent" is not independently measurable from "is it critical." The operationalization only works if σ_i, α_i are estimated *per parcel/region* and then a spatial fraction is taken. The draft does not say this, and the paper's existing σ/α machinery is global, so the observable as written is not yet computable as a distinct quantity.
3. **No mapping to the percolation/ξ candidates** (which are the mathematically natural extent observables) — the draft only offers "fraction" and "Φ-family."

**Fix:** (a) drop or demote Φ as the extent index; make extent = per-region fraction-at-criticality / giant-critical-cluster size / ξ. (b) State explicitly that σ and DFA-α must be estimated *regionally* to yield a spatial fraction. (c) Keep LZ/PCI for complexity as drafted.

---

## Q3 — Relation to the integration/differentiation MATH tradition

**Verdict: The mapping is mathematically apt at the level of *intuition* and the draft credits the tradition honestly — but the draft does NOT add formal content beyond the single-quantity tradition, and it omits the one measure (Tononi–Sporns–Edelman neural complexity C_N) that is the closest formal precedent and the strongest check on whether "2-D plane" adds anything.**

The integration–differentiation tradeoff is exactly the right tradition to cite, and the draft's honest-convergence framing ("claims no priority over it... Φ and the differentiation measures are consistent with FMT's two dimensions and supply candidate operationalizations") is the correct posture (matches the no-strawman audit in the draft, PASS). The draft cites Tononi 2004 (Φ), Albantakis 2023, Casali 2013 (PCI), Schartner 2017 (LZc).

**The critical omission: Tononi–Sporns–Edelman neural complexity C_N (1994).** C_N is *literally* the formalization of "integration × differentiation as a single optimized scalar": C_N = Σ_k [ (k/n)·H(X) − ⟨H(X_k^j | X−X_k^j)⟩ ] summed over subset sizes, i.e. it is maximized exactly when the system is simultaneously integrated (whole-mutual-information high) and differentiated (subsets near-independent). This matters enormously for the audit because:

- C_N already collapses "integration" and "differentiation" into **one** number on the grounds that the interesting regime is where *both* are high. The two-dials draft instead proposes a **2-D plane with a trade-off frontier**. The reviewer's sharp question is: *does the 2-D-plane add formal content beyond C_N, or merely re-spread a single optimized scalar back into two axes?*
- The honest answer the draft must give (and currently does not even raise): the 2-D plane **does** add content **iff** the two axes are independently manipulable and independently measurable (Q1/Q2). C_N assumes a single substrate-wide optimum; the two-dials claim asserts you can ride a *frontier* (one high, the other low) and that the joint corner is reachable only rarely. That is a genuinely stronger, more falsifiable structure than C_N — **but only if extent and complexity are defined on different mathematical objects (spatial measure vs. dynamical measure), which is exactly the Q1 fix.** If both are just "integration-flavored" and "differentiation-flavored" components of one C_N-like scalar, the 2-D plane is a renaming, not new content.

So: the mapping is apt, the framing is honest, but **the draft has not earned the claim that the 2-D plane adds formal content** — because it neither defines the axes on distinct structures nor engages C_N (the precise prior art that would force the question). Right now a referee from the IIT/complexity tradition would say "this is C_N with the axes pulled apart and no new measure."

**Fix:** (a) cite and engage Tononi–Sporns–Edelman C_N (1994) as the closest formal precedent; (b) state precisely what the 2-D reading adds over C_N — *independent manipulability of a spatial extent measure vs. an on-cluster complexity measure, with a reachability claim about the joint corner* — and tie that to the seizure (extent↓ while a C_N-style scalar might not cleanly separate the failure mode) and to Prediction 5 (joint-corner signature). This is the difference between "new content" and "renaming."

---

## Q4 — "subjective duration = processing volume / clock-second"

**Verdict: Hand-waving. "Processing volume" is given no formal or operational definition anywhere. This is the least-earned formal claim in the package.**

The phrase appears in the draft's Prediction-5 block and its §3.4.4 bridging sentence. "Processing volume" is never defined. Candidate definitions exist and matter — they are not interchangeable:
- avalanche count per clock-second (∫ avalanche events dt),
- integrated suprathreshold activity (∫∫ activity dx dt over the recruited cluster),
- bits computed (entropy production / excess entropy over the interval),
- state-space trajectory length (path length of x(t) in X over the interval),
- C(t) integrated over the interval (using the roadmap's own "total conscious content" scalar, §3.5).

The draft picks none. Worse, "subjective duration = processing volume / clock-second" is dimensionally and conceptually slippery: if "processing volume" already has time in it (per clock-second), then "duration = volume / second" is "duration = rate," which is not obviously a *duration*. To be a duration the numerator must be a *quantity of processing* (dimensionless count or bits) accumulated over the interval, and subjective duration = accumulated-processing(interval) / (calibration constant), with the *physical* clock-second appearing only because the substrate runs at a finite physical rate. The draft's wording inverts this.

**Is "both maxed → time dilation" formally distinct and falsifiable?** As a *qualitative joint-signature* prediction (integration-extent and complexity rise *together*, correlated with reported dilation, vs. trading off in ordinary states) — **yes, it is falsifiable and theory-distinctive** (the draft's falsification clause is genuinely good: "if dilation occurs with high complexity but ordinary extent, the processing-volume account is wrong"). As a *quantitative* claim it is **not yet** falsifiable, because without a definition of processing volume there is no predicted functional form (linear? does dilation factor = k·∫processing? what is k?). So the prediction is admissible at the qualitative level the paper claims, but the *mechanism sentence* ("duration = processing volume / clock-second") pretends to a quantitative law it has not specified.

**Fix:** either (a) demote the mechanism to explicitly qualitative ("subjective duration scales monotonically with the amount of self-simulation processing completed per unit physical time") and drop the equation-styled phrasing, or (b) commit to **one** definition — the cleanest is processing-volume(Δt) := ∫_{Δt} C(t) dt using the roadmap's existing C(t) (§3.5), giving subjective_duration ∝ ∫ C(t) dt — which also *connects the time-dilation claim to the existing formal apparatus* and makes the joint-corner prediction quantitative (both dials up ⇒ C(t) up ⇒ ∫C dt up ⇒ dilation). Option (b) is the high-value move because it formally unifies Prediction 5 with §3.5 and §3.4.4.

---

## Q5 — Honesty of the qualitative stance

**Verdict: Mostly honest, with two specific over-reaches.**

The paper-wide stance ("permeability is currently specified qualitatively"; "qualitative framework is sufficient to generate predictions but not effect sizes," lines 375–377) is admirably honest, and the draft mostly inherits it: it says "Normal experience rides a frontier... the two are jointly maximized only rarely," and frames Prediction 5's testability qualitatively. The convergence-framing audit in the draft is genuine (it does not strawman IIT/PP/Block).

**Two over-reaches where the draft asserts more rigor than it has earned:**
1. **"two orthogonal dimensions read off one edge-of-chaos substrate" / "extent and complexity are two ways of measuring how much Class-4 dynamics a critical system is doing, not two substances."** This *sounds* like a derived orthogonality result. It is a stipulation. Orthogonality (independent manipulability) is the load-bearing formal claim of the whole block and it is asserted, not shown — and, as Q1 notes, it is in tension with the single-axis treatment in the rest of §3.7 and fmt_formal §4 unless heterogeneity is added. An honest version says "we *propose* extent and complexity as two separable dimensions" and flags that their independence is an empirical/formal conjecture.
2. **The "duration = processing volume / clock-second" equation-styled phrasing** (Q4) reads as a quantitative law inside an otherwise-qualitative section. That is the clearest instance of asserting a formal result not earned.

Everything else (the seizure negative control, the governors, the joint-signature prediction) stays within the honest qualitative bound. **Fix: re-flag orthogonality as a conjecture and de-equation the time-dilation mechanism (see Q1, Q4 fixes).**

---

## Q-aside — the seizure "extent = Class-4 involvement, not co-activation" move

This is the **strongest** formal contribution in the package and worth isolating. It is genuinely a sharper definition: it says EXTENT must be the spatial measure of *Class-4-regime* tissue, and a generalized tonic-clonic seizure (near-maximal co-activation, but hypersynchronous ⇒ Class 2/3 locally) therefore scores **low** extent and predicts unconsciousness. Mathematically this is exactly the right consequence of the Q1 spatial-fraction definition: co-activation is Σ activity; extent is |{ regions in Class-4 }|; a hypersynchronous state has high Σ activity and ≈0 Class-4 fraction. The two are provably different functionals, and the seizure is the case that *separates* them. This is the one place the two-dials idea already behaves like a real measure-theoretic distinction rather than a metaphor — and it is the empirical anchor that should *drive* the formal definition (the definition should be chosen so that the seizure falls out, which the percolation/fraction definition does and a Φ-based or co-activation-based definition does not). It also exposes that **Φ is the wrong extent index** (Q2): IIT would not cleanly score a hypersynchronous seizure as low, because the issue is local Class-4 loss, not global irreducibility.

---

## Minimal formal treatment the paper needs

Concrete, minimal additions that would move the two-dials from verbal to defensible-formal without committing to a full theory:

**1. Establish spatial heterogeneity (one sentence, §3.7 prose).** "Criticality is not a single global operating point but a spatially varying property; the substrate is a field of locally-critical regions, and two independent questions can be asked of it: *how much* of the field is critical, and *how complex* the critical dynamics are."

**2. Define EXTENT as a named spatial order parameter (§3.7 prose + one Table-1 row).**
Let the substrate be partitioned into units i = 1..N with locally-estimated criticality (σ_i ∈ [σ_low,σ_high] and/or λ_max,i ≈ 0). Define
> **E (extent)** = either (a) the fraction Φ_ext = (1/N)·|{ i : unit i is locally critical }|, or (b) the normalized giant-critical-cluster size P_∞ (largest connected component of mutually-correlated critical units / N), or (c) ξ/L (correlation length over system size).
P_∞ (b) is recommended — it is a true percolation order parameter, it captures "one integrated critical process," and it makes the binding claim of §5.1 (maximal correlation length ⇒ integration) the *same* quantity as extent.

**3. Define COMPLEXITY as a named dynamical measure (§3.7 prose + one Table-1 row).**
> **K (complexity)** = Lempel-Ziv complexity (or entropy rate / excess entropy) of the activity of the recruited critical cluster — algorithmic richness of the on-critical dynamics, conditioned on criticality. PCI maps here (per the line-418 caveat), NOT to extent.

**4. State orthogonality precisely (one sentence).** "E and K are defined on different mathematical objects — E is a measure over space (which regions are critical), K is a measure over dynamics (how rich the critical computation is) — and are therefore independently variable: a hypersynchronous generalized seizure has E ≈ 0 with high co-activation (the negative control that forces E ≠ co-activation), while a small but intricate critical cluster has high K with low E." Flag independence as a **conjecture** to be tested, not a derived theorem.

**5. Relate to the tradition honestly (one sentence + C_N citation).** "Tononi–Sporns–Edelman neural complexity C_N (1994) and integrated information Φ (Tononi 2004) collapse integration and differentiation into a single optimized scalar; FMT's contribution is to separate them onto distinct measures (spatial E vs. dynamical K) whose *independent* behavior — and whose rare joint maximum — is the new, falsifiable structure (Prediction 5)." This is what earns "adds content beyond renaming."

**6. (Optional, high-value) Define processing volume via existing C(t).** processing-volume(Δt) := ∫_{Δt} C(t) dt (using fmt_formal §3.5's C(t)); subjective_duration ∝ ∫ C(t) dt. This converts the time-dilation hand-wave into a claim tied to existing apparatus and makes Prediction 5 quantitative. If not adopted, de-equation the mechanism to a monotonic-scaling statement.

**Where each piece should live:**
- Items 1, 4, 5 → **§3.7 prose** (the new two-dimensions subsection in the draft).
- Items 2, 3 → **the two new Table-1 rows** the draft already proposes (replace "Φ-family" with the percolation/fraction definition for extent; keep LZ/PCI for complexity).
- Item 6 → **fmt_formal roadmap** (new subsection under §4 or alongside §3.5), with a forward-pointer from §3.4.4/§8.6 of the main paper. The time-dilation *law* is roadmap-grade, not main-paper-grade.
- The full E/K order-parameter formalization (percolation order parameter, regional σ/α estimation, conditional LZ) → **fmt_formal roadmap, new §4.x "The two dimensions of criticality: extent and complexity"** — this is the natural home and it is currently empty (see next section).

---

## Does fmt_formal already cover it?

**No. The two-dials / extent-vs-complexity decomposition is ABSENT from the formalization roadmap.** Specific findings:

- **Criticality is treated as a single axis.** §4.2–4.5 give *three alternative detectors of one critical point* (branching ratio σ, Lyapunov λ_max, DFA α) and §4.3 worries about which to use — but all three answer "is the system at the (one) critical point?" There is no spatial-fraction, percolation, correlation-length, or giant-cluster quantity. There is no notion of "how much of the substrate is critical" as distinct from "is it critical." Extent (in the FMT two-dials sense) does not exist in the roadmap.
- **The roadmap's only "two dimensions" are scope × mode** (the model space, §2.1–2.4), plus a hierarchical-depth axis ℓ (§2.4). These are orthogonal to the extent/complexity distinction — scope/mode is *which models*, not *how much criticality / how complex the critical dynamics*.
- **Complexity exists, but as a single scalar conflated with total content.** §3.5 defines C(t) = ∫∫ ρ dν ds ("total conscious content") and says it "should correlate with PCI and Lempel-Ziv." So the roadmap has a complexity-flavored scalar — but it is *total content*, not "richness of the critical dynamics," and crucially it is **one** number, not one of a pair. The roadmap nowhere splits content into integration-extent × differentiation-complexity.
- **The two-threshold formalization (§4.5)** is `σ ∈ [σ_low,σ_high] ∧ (architecture)` — again single-axis criticality. No extent/complexity factorization of the criticality conjunct.
- **No processing-volume / subjective-duration / time-dilation formalization anywhere.** "Processing volume," "subjective duration," "time dilation" do not appear. §3.5's C(t) is the *only* hook (and is exactly the hook recommended in Item 6 above).
- **C_N (Tononi–Sporns–Edelman 1994) is not cited.** The roadmap cites Tononi 2004 Φ and Casali PCI but not C_N — the same omission as the main-paper draft.

**Net:** fmt_formal supplies *raw material* (substrate-as-dynamical-system §4.1; regional dynamics are representable; C(t) §3.5; graph-phase-transition §4.6 which is actually close to the percolation-extent idea) but contains **no** formalization of the two dials. The two-dials block is therefore a **net-new formal task**, and the roadmap is the correct place for the heavy version (Items 2, 3, 6 in full). The §4.6 graph-phase-transition (clustering coefficient, modularity, giant component) is the nearest existing scaffold and could be extended into the extent order parameter with little new machinery — that is the single cheapest formal win.

---

## Summary table

| Q | Verdict | Core gap | Highest-value fix |
|---|---|---|---|
| Q1 orthogonality coherence | Coherent only under unstated heterogeneity reading | No spatial heterogeneity premise; no spatial order parameter; tension with single-axis rest of paper | Define substrate as field of local critical points; name extent = percolation P_∞ / fraction / ξ |
| Q2 observable mapping | Verbal-consistent; extent observable under-specified & partly circular | Φ mis-assigned to extent; regional σ/α estimation not stated | Drop Φ-as-extent; extent = regional fraction-at-criticality / giant cluster |
| Q3 vs integration/diff tradition | Apt + honest, but no formal content beyond C_N as written | C_N (1994) un-cited; "2-D adds content" not argued | Cite/engage C_N; state precisely what independence + joint-corner adds |
| Q4 processing volume | Hand-waving | "Processing volume" undefined; equation is dimensionally inverted | Define proc-vol := ∫ C(t) dt (ties to §3.5); or demote to monotonic |
| Q5 honesty of stance | Mostly honest; 2 over-reaches | Orthogonality stipulated-as-derived; time-dilation equation styled as law | Re-flag orthogonality as conjecture; de-equation time-dilation |

**Single highest-value formalization step:** define **EXTENT as a percolation/giant-critical-cluster order parameter (P_∞)** and **COMPLEXITY as on-cluster Lempel-Ziv (K)**, on explicitly different mathematical objects (space vs. dynamics), with the generalized seizure as the case that separates them. This single move (a) makes orthogonality coherent, (b) fixes the Φ mis-assignment, (c) gives the 2-D plane real content beyond C_N, (d) reuses the existing §4.6 graph-phase-transition machinery, and (e) makes the seizure negative control a theorem-shaped consequence rather than a worked example. Everything else (time-dilation law, full roadmap module) hangs off it.
