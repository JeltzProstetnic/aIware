<!-- Action: reference -->
<!-- Tracked-by: AIW-94 (two-dials mathematical formalization) -->
# AIW-94 — Two-dials formalization (Extent × Complexity) — Fable draft, S243 2026-07-06

**Provenance:** Fable-5 agent, S243. Attempted per MG "94 if easy." **VERDICT: NOT easy —
MODERATE** (definitions/orthogonality/C_N-distinction EASY; seizure-separation MODERATE, rests on
one load-bearing assumption A2; quantitative time-dilation law HARD, NOT delivered — only
directional product-scaling earned). **Integration DEFERRED** — this is roadmap-grade content for
`paper/fmt_formal/`, not main-paper-grade. Review before integrating. Two findings DO touch existing
prose (see §3, flags 5 + the seizure/C_N point).

---

## 1. VERDICT (verbatim)

MODERATE. Definitions, orthogonality, and the C_N distinction are EASY; the seizure-separation is
MODERATE — it rests on one statable, load-bearing assumption (A2 below); the *quantitative*
time-dilation law is HARD and is NOT delivered — only its qualitative/directional form is.

Self-contained: needs only off-the-shelf machinery — a percolation order parameter on a labeled
graph (Dial 1), a Lempel-Ziv / entropy-rate functional on the on-cluster trajectory (Dial 2), the
Tononi–Sporns–Edelman 1994 complexity as prior art, and ∫C dt for processing volume. Three caveats
keep it out of EASY: (a) the "extent collapses in seizure" result depends on the local Class-4
membership predicate rejecting Class-2 synchrony (a λ_max≈0 test alone does NOT — a limit cycle has
λ_max=0); (b) percolation-*transition* sharpness is only as good as the cortical graph topology
permits (the *fraction* is always defined; the *sharp transition* is not guaranteed on small-world/
scale-free graphs); (c) the time-dilation scaling is dimensionally clean and directionally
falsifiable but κ and exponents are free ⇒ no predicted number. **Main skeptical finding: the
generalised seizure does NOT demonstrate advantage over C_N** — C_N also scores a synchronous
seizure low; the 2-D decomposition earns its keep on the *off-diagonal* states and the joint-corner
time-dilation law, NOT the negative control.

## 2. Formal subsection (Fable draft)

### 2.0 Setup
Roadmap substrate (§4.1): network dynamical system x(t+1)=f(x(t),s(t),W), x∈ℝ^N, over units i=1..N,
coupling graph G=(V,E), (i,j)∈E iff W_ij≠0. Fix operating window [t,t+T] (quasi-stationary).

> **Assumption A1 (regional estimability).** Each unit i has *locally* estimable dynamical
> statistics on the window — local branching ratio σᵢ, DFA αᵢ, avalanche-size distribution, activity
> entropy rate hᵢ. Replaces the paper's globally-estimated σ/α (§3.7) — required so extent is
> measurable independently of "is the system critical" (discharges the audit Q2 circularity).

### 2.1 Local Class-4 membership (load-bearing)
**Def 1.** Unit i is Class-4-critical, χᵢ=1, iff [σᵢ∈[σ_low,σ_high]] ∧ [avalanche-size distribution
at i scale-free over accessible range] ∧ [hᵢ≥h_min>0]. Rejects supercritical Class 3 (σᵢ>σ_high),
frozen Class 1 (hᵢ→0), and periodic/synchronous Class 2 (characteristic-scale non-power-law
avalanches, low entropy rate). χᵢ=0 otherwise.

> **Assumption A2 (periodicity rejection — LOAD-BEARING).** Membership must reject Class-2 synchrony.
> λ_max,i≈0 is INSUFFICIENT: a limit cycle (periodic, synchronous) has λ_max=0 and would pass an
> edge-of-chaos Lyapunov test while being Class 2. The scale-free + entropy-floor conjuncts carry the
> whole clean seizure result (§2.5). Consistent with Kanders et al. (2017) (roadmap §4.3) and paper
> line 426 ("Hypersynchronous, low-complexity dynamics are Class 2/3, not Class 4").

**Critical subgraph.** G_c = subgraph induced by {i:χᵢ=1}, edge (i,j) kept iff W_ij≠0 AND
|corr(xᵢ,xⱼ)|≥c₀ (correlation gate ⇒ one integrated critical process, not disconnected islands —
this is what makes extent the *integration* dimension).

### 2.2 Dial 1 — EXTENT (percolation order parameter)
**Def 2 (EXTENT).** P∞ := |LCC(G_c)| / N — normalized size of the largest connected component (giant
critical cluster) of G_c; GC := LCC(G_c). A percolation order parameter: below threshold p_c,
P∞=O(1/N)→0; above, P∞=O(1). Functional of the *labeled connectivity graph* (G,{χᵢ}) — spatial/
topological. Reuses §4.6 graph-phase-transition machinery.

### 2.3 Dial 2 — COMPLEXITY (on-cluster Lempel-Ziv / entropy rate)
Restrict to giant cluster: X_GC(·)={xᵢ(·):i∈GC}. Symbolize (binarize about median; Schartner et al.
2017) → s_GC. **Def 3 (COMPLEXITY).** Extensive: K:=LZ76(s_GC). Intensive/rate: k:=lim_{T→∞}
LZ76(s_GC)/(|GC|·T)→ĥ (per-unit entropy rate, bits/unit/step). Depends only on dynamics restricted to
GC, not on |GC|/N. PCI/LZc map here, never to extent.

### 2.4 Orthogonality (constructive independence)
P∞ : (G,{χᵢ})↦[0,1] (functional of the graph); k : x|_GC↦ℝ≥0 (functional of the trajectory).
Different objects ⇒ not definitionally linked (answers "you renamed one axis into two").

**Proposition 1 (constructive independence).** state↦(P∞,k) is onto a 2-D region — all four quadrants
realizable:

| | k low | k high |
|---|---|---|
| **P∞ high** | (+−) broad+shallow: large percolating cluster, each unit a *minimal* Class-4 rule (drowsy diffuse wakefulness) | (++) broad+rich: the rare joint corner (alert multimodal cognition; NDE/salvia) |
| **P∞ low** | (−−) origin: seizure, deep anesthesia | (−+) narrow+intense: single small Class-4 cluster running a rich universal computation (focal processing) |

Off-diagonal (+−) and (−+) both constructible ⇒ P∞ and k are independent coordinates. ∎

> **Reviewer-bait defusal.** "Orthogonal" = independent degrees of freedom / independently settable
> coordinates — NOT statistical independence (the two share a finite metabolic budget, §5.3) and NOT
> inner-product orthogonality. The load-bearing claim is Prop 1 (constructive independence). The
> resource ceiling constrains the *operating trajectory* to an anti-correlated frontier ("rides a
> frontier"); constructive independence and empirical anti-correlation are both true, not in tension.

### 2.5 Generalised seizure — separating case
Naive measure the theory must NOT use: co-activation A:=(1/N)Σᵢ𝟙[xᵢ active]. Generalized tonic-clonic
seizure: (1) A≈1; (2) hypersynchronous/rhythmic ⇒ characteristic-scale avalanches, hᵢ<h_min or
σᵢ>σ_high ⇒ χᵢ=0 ⇒ G_c sparse, no giant component ⇒ **P∞≈0 (extent collapses)**; (3) synchronous
activity maximally compressible ⇒ **k≈k_min**. Seizure sits at the origin (P∞≈0,k≈0) while A≈1. Three
functionals; seizure separates them: A high, P∞ low, k low ⇒ predicted unconscious. Makes the paper's
line-426 negative control a *consequence of the definitions*.
- A2 load-bearing: drop periodicity-rejection ⇒ limit-cycle seizure (λ_max=0) passes membership ⇒
  P∞ spuriously high. "Extent is low in seizure" is true IFF A2 holds. State it.
- Robust to ictal route: supercritical (σᵢ>σ_high) and hypersynchrony (Class 2) both ⇒ χᵢ=0 ⇒ P∞→0.

### 2.6 Processing volume ∫C dt and time-dilation
**Instantaneous rate:** C(t):=P∞(t)·N·k(t)=|GC(t)|·k(t) — total bits/step of incompressible
self-simulation (extent × per-unit complexity rate). Criticality-grounded instance of roadmap §3.5
C(t). No double-counting (P∞=how many units, k=bits per unit).
**Processing volume:** V(Δt):=∫C(t)dt over [t₀,t₀+Δt] — units: *bits* (a quantity, not a rate).
**H-time:** subjective time clocked by self-model updating done, not the physical clock ⇒
D_subj(Δt)=κ·V(Δt), κ=subjective-seconds/bit. **Dilation factor:** δ(Δt):=D_subj/Δt=κ·⟨C⟩_{Δt}.
Calibrate κ so δ=1 in ordinary wakefulness ⇒ δ=⟨C⟩/C_baseline.
**Joint corner ⇒ dilation:** both dials spike (P∞→1 AND k→k_max, the (++) corner) ⇒ C≫C_baseline ⇒
brief clock interval contains vast self-simulation ⇒ δ≫1 (NDE life-review / high-dose salvia).
Falsifiable-directional: dilation co-varies with the **product P∞·k**, not complexity alone.
**Dimensional correction:** the draft phrase "subjective duration = processing volume / clock-second"
conflated *duration* (=κV, a quantity) with the *dilation factor* (=κV/Δt=κ⟨C⟩, a ratio). Corrected:
**duration = κ·(processing volume)**; the "/clock-second" belongs to the dilation factor.

> **HARD-FLAG.** κ and the functional form (why product P∞·k vs P∞^a·k^b or a saturating combo) are
> NOT derived — simplest dimensionally-consistent choice. Law is quantitative in *form* but constant
> and exponents free ⇒ no predicted number. Only directional product-scaling is earned.

### 2.7 Relation to Tononi–Sporns–Edelman C_N (1994)
C_N(X) is a single scalar functional of p(x): C_N=Σ_k[(k/N)I(X)−⟨I(X_k^j)⟩_j], I(X)=ΣH(xᵢ)−H(X).
C_N≈0 at both extremes (segregated / homogeneous-redundant), maximal in the intermediate
integrated-and-differentiated regime.
1. **Different objects.** C_N is a functional of p(x) alone — no spatial/topological order parameter.
   P∞ is a percolation order parameter on (G,{χᵢ}) — an object C_N does not see. **EXTENT is genuinely
   new relative to C_N**, not a re-encoding. Decisive point vs "you renamed C_N."
2. **C_N bundles what FMT splits.** C_N is a joint-corner detector (peaks near (++)). FMT decomposes
   that peak into two independently-set coordinates; added content = representability of off-diagonal
   (+−),(−+) (which C_N collapses to one low value) + a reachability claim about (++).
3. **Seizure does NOT distinguish them (key finding).** C_N also scores a synchronous seizure low.
   Negative control passed by both ⇒ validates "co-activation≠consciousness" but does NOT show the
   2-D account's advantage over C_N. Argue superiority on off-diagonal states + time-dilation, NOT the
   seizure.
4. Formal relation (conjecture): near (++), C_N plausibly monotone in P∞·k; diverges away from it.

## 3. Gaps / risks / reviewer-bait
1. A2 estimability (sharpest risk) — per-parcel avalanche/entropy estimation is data-hungry; paper's
   σ/α are global. Commit to regional estimation (A1); concede higher empirical bar.
2. λ_max≈0 ≠ Class 4 — membership must not be Lyapunov-only, or seizure separation fails.
3. Percolation "transition" vs "fraction" — cortical graphs small-world/scale-free ⇒ p_c→0, smeared
   transition. Claim the fraction; hedge the "transition" word.
4. LZ estimator dependence — pin the pipeline (Schartner et al. 2017).
5. Free time-dilation parameters — state directional product-scaling only; NO number.
6. Do not reproduce a C_N equation you can't hand-verify — keep schematic + cite.
7. "Orthogonal" wording — define as constructive independence; distinguish from empirical correlation.
8. §3.5 identity mismatch — roadmap C(t) is a *content* integral; §2.6 C(t) is a *rate*. Roadmap must
   decide whether "conscious content" is a quantity or a rate and unify/distinguish the two C(t)'s.

**Bottom line:** decomposition is defensible-formal and mostly free (reuses §4.6 percolation, standard
LZc, TSE 1994). Do NOT oversell (i) the seizure as evidence against C_N (it isn't — C_N passes too),
(ii) any numerical time-dilation prediction (only product-scaling direction earned). A2 is the single
assumption doing the real work.
