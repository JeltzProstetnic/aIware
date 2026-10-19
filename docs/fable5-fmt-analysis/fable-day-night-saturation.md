# Day & Night (B3678/S34678) and the Saturation-Trigger Conjecture (NEW-1)

**Question (author):** could the Day & Night automaton demonstrate phase transition at Bekenstein
saturation? Is D&N the "richer Class-4 rule" that exhibits the saturate-and-decompress cycle that
Game of Life is too primitive to show (§5.4, §9.7)?

**Analysis-only exploration. Fable 5 subagent, 2026-06-11. Includes pilot numerics (verified, code
inline below); all simulation numbers in this file were actually computed, not estimated.**

**TL;DR.** Yes — but with one decisive correction to the naive reading. The CA analogue of the
Bekenstein-saturated state is **not the full lattice** (that is the all-on Class-1 vacuum, which §5.4
itself already excludes as the "ordered extremum"); it is the **maximum-entropy ρ = 1/2 soup**, which
in D&N is precisely the **fixed locus of the on↔off symmetry — a self-dual, maximally disordered
configuration sitting exactly between the two ordered vacua**. Pilot runs confirm that this state is
dynamically unstable in exactly the way NEW-1 conjectures: it spontaneously breaks the symmetry and
coarsens into ordered day/night domains (2×2 block entropy 4.0 → 1.6 bits in 400 steps) while
**density stays near 1/2 and interface activity persists** — whereas GoL's entropy drop is pure decay
to near-vacuum ash (density 0.5 → 0.06, frozen debris). D&N therefore gives the cleanest available
CA illustration of "maximal disorder is an unstable saddle, dynamics forced off it into order," plus
an exact Z₂ analogue of the C in CPT-alternation. What it does **not** give is reversibility — it
models the *interior-effective* face of §8.4, not the NEW-4 substrate. The reversible target exists:
**Critters** (Margolus block CA), which is exactly reversible, Class-4-complex, and — remarkably —
**complements its entire state every timestep**, a literal per-step on↔off flip built into a
reversible law.

---

## 1. The on↔off symmetry as the crux

### Established facts (verified algebraically and numerically this session)

D&N (B3678/S34678) is **exactly self-complementary**: for every cell state s and neighbor count n,

> step(1−s, 8−n) = 1 − step(s, n).

Verified exhaustively over all 18 (s, n) pairs. Consequence (standard, e.g. Bell 1997; LifeWiki
"Day & Night"): complementing a configuration and evolving is identical to evolving and
complementing. Every pattern has an anti-pattern — same dynamics, inverted background. GoL fails the
same check (verified: it is not self-complementary), which is *the* structural reason its dense
regime is dead: GoL has one vacuum and one preferred (sparse) phase; D&N has two equivalent vacua
related by the symmetry.

Three exact consequences:

1. **Extremes map to extremes.** The all-on lattice maps to the all-off lattice. Both are fixed
   points (verified: s=1, n=8 → survives; s=0, n=0 → stays dead). So the maximal-density extreme is
   *dynamically identical* to the minimal-density extreme — and both are **ordered Class-1 vacua**,
   exactly the "all-off or all-on lattice" that §5.4 explicitly contrasts with the saturated state.
   This is the first half of the answer: in D&N, "all-night" is not saturation. It is the mirror of
   "all-day" — a dead ordered extremum. The naive identification "saturation = full lattice" is wrong
   *in the paper's own terms*, and D&N's symmetry makes that vivid rather than embarrassing.

2. **Near-saturation density ≅ near-vacuum density, exactly.** A lattice at density 1−ε (sparse
   holes in night) is isomorphic under the symmetry to a lattice at density ε (sparse cells in day).
   A fully loaded lattice with a few defects is computationally identical to an empty lattice with a
   few seeds. This is an exact theorem-level statement, not an analogy — and it is the precise
   automaton form of "the only direction off a maximally compressed state is decompression into a
   fresh low-entropy start." Caveat from the pilot run: *random* sparse defects at ε = 0.05 die out
   entirely in D&N (the ρ = 0.95 soup collapsed to the all-on vacuum in <50 steps, activity → 0);
   survival in D&N needs ≥3 neighbors, so isolated random debris is culled harder than in GoL.
   Complexity at high density persists for *structured* configurations (anti-gliders,
   anti-oscillators — guaranteed by the symmetry), not for arbitrary thin noise.

3. **Complexity persists at high density — exactly, by symmetry.** Every documented D&N spaceship,
   oscillator, gun, and rake (Bell 1997 constructed many; LifeWiki catalogs them; Catagolue's
   apgsearch infrastructure supports this rule) has a complement twin running on the live background.
   "Does complexity persist at high density?" — yes, with exactly the same richness as at low
   density. This is established, not conjectural, and it is what GoL cannot do.

### The crux, restated

The on↔off symmetry has a **fixed locus**: configurations statistically invariant under complement,
i.e. density 1/2 — and the *maximum-entropy* member of that locus is the i.i.d. ρ = 1/2 soup. So in
D&N the maximally disordered state is also the **self-dual point of the symmetry, poised exactly
between the two ordered vacua**. That is the structure of an unstable saddle in the Landau sense: a
Z₂-symmetric disordered state above two symmetry-broken ordered phases. NEW-1's conjecture —
"saturated = maximally disordered = saddle, not resting place" — is, for this automaton, not just
plausible but the *expected* behavior of a Z₂ system quenched from infinite temperature to below its
ordering transition (cf. Ising/model-A phase-ordering kinetics; Bray, Adv. Phys. 43:357, 1994).

A clean exact lemma falls out of the symmetry (provable in two lines): **if the initial measure is
complement-invariant (e.g. i.i.d. ρ = 1/2), the law of the configuration at every later time is
complement-invariant, so the ensemble-mean density is exactly 1/2 for all t.** D&N *cannot* decay to
GoL-style sparse ash from the saturated state — symmetry forbids any net density drift. Whatever the
saturated state decays into must live at mean density 1/2: i.e., either persistent disorder or
**ordered domains of both phases**. The pilot run shows it is the latter.

### Pilot numerics (256×256 torus, i.i.d. ρ = 0.5, synchronous updates, single seed)

| t | D&N density | D&N S₂ (2×2 block entropy, bits, max 4) | GoL density | GoL S₂ |
|------|------|------|------|------|
| 0 | 0.500 | 3.999 | 0.500 | 3.999 |
| 50 | 0.461 | 3.229 | 0.124 | 1.947 |
| 200 | 0.407 | 1.825 | 0.073 | 1.313 |
| 400 | 0.407 | 1.644 | 0.063 | 1.171 |

Activity (fraction of cells flipped per step) at t = 400: D&N 0.032, GoL 0.044 (GoL's residual
activity is blinker ash; D&N's is moving domain walls — qualitatively different, needs the structure
census of §4 to separate). Reading: **both rules flee maximal entropy, but in opposite ways.** GoL's
entropy drop is density collapse — the soup evaporates to 6% ash in a single vacuum. D&N's entropy
drop occurs *at conserved (ensemble) density*: the soup organizes into growing day and night domains
— spontaneous symmetry breaking with order emerging from maximal disorder. (The single-run density
drift 0.50 → 0.41 is the finite-size symmetry breaking itself: one phase is winning on this seed; on
a finite torus one vacuum eventually takes over, with the loser surviving as anti-debris.)

This is the demonstration GoL is "too primitive" for, in precisely §5.4's sense: driven to the
maximally disordered state, D&N does not freeze and does not evaporate — it **reorganizes**.

## 2. CPT analogue

The complement symmetry is an exact internal Z₂ — the automaton analogue of **C** (charge
conjugation): day-phase ↔ night-phase, pattern ↔ anti-pattern, with identical dynamics guaranteed by
the rule. The mapping onto §5.4's CPT alternation is structurally tight at three points:

1. **Symmetric law, broken state.** The rule is exactly C-symmetric; any *realized* post-saturation
   state breaks the symmetry (one phase dominates a given region/cycle). That is the same logical
   shape as Boyle–Turok: CPT-symmetric laws, CPT-asymmetric branches, with the conjugate "missing"
   half realized elsewhere (previous/next cycle, sibling domain).
2. **Orientation is a property of the new interior, not inherited.** Which vacuum wins the coarsening
   from a symmetric soup is spontaneously and (for a Class-4, computationally irreducible rule)
   unpredictably selected — matching §5.4's "the specific form of the decompression is a property of
   the new interior, not a constraint inherited from the old one," and §9.6's parsimony framing.
3. **Domain structure = mixed-signature multiverse.** Before one phase wins, the lattice is a
   patchwork of day and night domains separated by active walls — a direct cartoon of the Big-Rip
   branch of §5.4 (many regions, independently realized "CPT" orientations).

Honest limits: this is a **C analogue only**. P is trivial (the rule is isotropic, parity-symmetric
by construction), and **T is absent — D&N is irreversible** (see §5), so nothing here models the T in
CPT. The paper should call it "matter/antimatter (C-type) alternation" if it ever cites this; calling
it a CPT analogue outright would overclaim. The rule that supplies the missing T is Critters (§5).

## 3. What is "Bekenstein saturation" for a CA?

Three candidate definitions, in increasing fidelity:

- **(a) Maximal cell density (full lattice).** Wrong, and provably so within D&N: the full lattice is
  the ordered all-on fixed point — §5.4's *Class-1 dead extremum*, the very thing the conjecture
  distinguishes saturation from. Pilot confirmation: ρ = 0.95 i.i.d. soup collapses into this vacuum
  within 50 steps and freezes (activity = 0). Density-saturation tests the wrong extremum.
- **(b) Maximal configurational entropy.** The i.i.d. ρ = 1/2 soup: every distinguishable degree of
  freedom in use, no further distinction encodable — exactly §5.4's wording, transposed to the bulk.
  This is the right operational analogue for a non-holographic toy, with the bonus that in D&N it
  coincides with the self-dual locus of the symmetry. This is what the experiment of §4 drives.
- **(c) Genuine boundary saturation.** Bekenstein saturation proper is a *boundary* statement:
  region's information content = max encodable on its bounding surface. No ordinary CA satisfies a
  holographic bound — CA information is extensive (scales with area in 2D, volume in 3D), not with
  the perimeter. A 2D Life-like rule simply has no regime where bulk states are limited by boundary
  capacity. **Therefore: any Life-family experiment, D&N included, tests only the
  "maximal-disorder-is-a-saddle" half of NEW-1, not the "holographic decompression" half.** This
  limitation must be stated wherever the result is used; pretending (b) is (c) would hand a referee
  Weak Point 7 back with interest.

Under definition (b), the pilot already answers the operative question: driving D&N to saturation
produces **reorganization, not freezing** — block entropy falls 4.0 → 1.6 bits while activity
persists and ensemble density is pinned at 1/2. The maximally disordered state is transient; ordered
structure (domains) condenses out of it; localized complex structures (walls, wall-bound gliders)
survive the transition. That is the saturate-and-decompress cartoon, minus holography and minus
reversibility.

One more honest note on "entropy": for a deterministic CA from a single configuration, fine-grained
entropy is not a dynamical variable; all statements above are about **coarse-grained observables**
(block entropy of the empirical block distribution, ensemble density). That is the correct level —
§8.4 places the arrow of time at exactly this coarse-grained interior level — but the file/figure
must say "configurational/block entropy," never bare "entropy."

## 4. A concrete, runnable computational experiment

**Rule:** B3678/S34678, synchronous, Moore neighborhood. **Control:** B3/S23 (GoL), identical
protocol. **Optional second control:** HighLife B36/S23 (complex but not self-complementary —
isolates the symmetry as the active ingredient).

**Grids:** 256², 512², 1024² (finite-size scaling); torus (periodic) as primary BC — avoids edge
artifacts and matches the closed-domain reading of Φ(U) = U. A fixed-boundary variant as robustness
check.

**Initial conditions:** (i) i.i.d. Bernoulli(ρ), ρ ∈ {0.05, 0.1, …, 0.95}, ≥20 seeds each — the
ρ = 0.5 row is "saturation," the sweep locates the basin boundaries of the two vacua; (ii) the exact
complement of each seed (free check: trajectories must be exact complements — a built-in correctness
test of the implementation); (iii) for the decompression visual: a saturated disk embedded in vacuum,
and vice versa.

**Duration:** 10⁵ steps at 1024² (lifelib/Golly with arbitrary-rule support makes this minutes, not
hours; the pure-Python pilot above did 400 steps at 256² in ~1 min).

**Observables (recorded on a log-spaced schedule):**
1. Density ρ(t) per run + ensemble mean (exact prediction: ⟨ρ⟩ = 1/2 for all t at ρ₀ = 0.5 — a
   falsifiable check of the symmetry lemma).
2. Activity a(t) = fraction of cells flipped per step (Class-4 indicator: slow decay to a persistent
   nonzero plateau vs Class-1 freeze vs Class-3 saturation).
3. Block entropy S_k(t), k = 2, 4, 8 (configurational order).
4. **Order parameter:** coarse-grain into b×b cells (b ≈ 8), m_i = 2ρ_i − 1 ∈ [−1, 1];
   φ(t) = ⟨|m_i|⟩ measures local phase order (0 at saturation, → 1 in pure domains). Plus the
   two-point correlation C(r, t); the characteristic domain length L(t) from its first zero.
   **Coarsening law:** L(t) ~ t^(1/z). Curvature-driven Z₂ coarsening predicts z ≈ 2 (Bray 1994);
   measuring z for D&N is a small publishable result in itself, and deviations (pinned walls along
   the orientations where straight D&N interfaces are stable) would show up as a crossover to slower
   growth.
5. **Structure census:** apgsearch/lifelib census of stabilized regions (ash objects, spaceships) on
   *both* backgrounds; count of moving structures localized on domain walls (detect via the activity
   field's connected components and their displacement).
6. **Irreversibility/recurrence quantification:** exhaustive predecessor census on small toruses.
   Pilot result (4×4 torus, all 2¹⁶ states, computed this session): D&N reaches 33,200/65,536 states
   (49.3% Gardens of Eden, max preimage multiplicity 309); GoL reaches 17,879/65,536 (72.7% GoE, max
   preimage multiplicity 9,628 — the vacuum's enormous basin). D&N is decisively many-to-one (not
   reversible) but **discards information far more slowly than GoL** — a quantitative bridge toward
   the reversible substrate, worth a half-figure. Extend to 5×5/6×6 (2²⁵, 2³⁶ — the latter needs a
   bit of care but is feasible with hashing) to check the trend.

**SUPPORT for the saturate-and-decompress conjecture (all four needed):**
- (S1) From ρ₀ = 0.5: S_k(t) falls substantially below maximum and φ(t) rises toward O(1) —
  maximal disorder is unstable toward order.
- (S2) L(t) grows without bound (power law) until finite-size cutoff — genuine phase-ordering
  transition, not local freezing.
- (S3) Activity a(t) remains nonzero with *propagating* localized structures present at late times
  on both backgrounds — Class-4 complexity survives the transition (vs GoL's static blinker ash).
- (S4) The GoL control shows the contrasting pathway (entropy drop by density collapse into a single
  vacuum, frozen ash) under the identical protocol — establishing that the symmetry, not the
  protocol, is the active ingredient.

**REFUTATION:**
- (R1) D&N's ρ = 0.5 soup relaxes to a *statistically stationary disordered* state (S_k stays near
  max, φ stays near 0, L(t) saturates at O(1)) — the saturated state would then be a stable phase,
  directly contradicting the saddle claim; or
- (R2) it freezes into a static finite-scale labyrinth (a → 0, L bounded) — glassy arrest, not
  decompression; or
- (R3) ⟨ρ⟩ drifts from 1/2 at ρ₀ = 0.5 (would indicate an implementation bug, since the symmetry
  forbids it — but if confirmed, the whole framing collapses).

The pilot run already shows S1, S2 (qualitatively), and S4; S3 needs the census machinery. Risk of
refutation looks low; risk of a *boring* result (z ≈ 2 plain Ising coarsening with little Class-4
decoration) is moderate — which would still support NEW-1's saddle claim but weaken the "Class 4"
flavor of the story.

**The figure** (one figure, four panels, for a future SB-HC4A §5.4 or a short companion note):
(a) snapshots at t = 0 / 10² / 10³ / 10⁵: white-noise soup → coarsening day/night domains with
visible wall structures (with a GoL strip below: soup → ash); (b) S₂(t) and a(t), D&N vs GoL —
the two escape routes from maximal entropy; (c) L(t) on log-log with the fitted exponent;
(d) a pattern and its anti-pattern evolving identically (the C-symmetry demonstration), or the
preimage-census bar chart (D&N vs GoL information loss). Caption writes itself: *"The maximally
disordered state of a self-complementary Class-4 rule is an unstable saddle between two ordered
vacua: saturation decays into order with persistent localized complexity, rather than into ash."*

## 5. Honest assessment

**Is D&N actually Class 4?** Yes by the standard informal criteria, and this is established in the
hobbyist-to-semiformal literature: long transients, gliders, oscillators, guns, rakes, and large
engineered constructions on both backgrounds (Bell, "Day & Night — An Interesting Variant of Life,"
1997; LifeWiki; Catagolue census). Two cautions for paper use: (i) I know of **no rigorous
universality proof** for D&N (unlike GoL and Rule 110) — say "exhibits complex dynamics / supports
glider engineering," which is what §9.6 already carefully does; (ii) Wolfram-class labels in 2D are
informal and the classification problem is undecidable (Culik & Yu 1988) — also already in §9.6. The
current §9.6 sentence ("Day & Night exhibits complex dynamics under an exact on–off state symmetry")
is exactly right and needs no change.

**Does its "ash" differ from GoL's because of the symmetry?** Yes, structurally and provably at the
ensemble level: complement-invariant initial measures stay complement-invariant, so mean density is
pinned at 1/2 and decay-to-sparse-ash is impossible from saturation. The realized end state on a
finite torus is one vacuum plus anti-debris (a single run eventually breaks the symmetry), but the
*route* there is phase-ordering with active interfaces, not evaporation — and the route is the
physics. One nuance to keep: D&N's truly sparse random regime is *deader* than GoL's (≥3-neighbor
survival culls isolated debris — verified: ρ = 0.05 random soup in GoL leaves ash + blinkers, while
the complementary D&N ρ = 0.95 soup dies completely into the vacuum). D&N's complexity lives at
intermediate densities and on interfaces, which is fine — that is where the model's interesting
dynamics are supposed to live too.

**The reversibility gap — squarely.** D&N is irreversible: many-to-one (verified exhaustively:
49.3% Garden-of-Eden states on the 4×4 torus; by Moore–Myhill, GoE existence and non-injectivity are
equivalent for such rules). NEW-4 commits the substrate to exact reversibility. So **D&N cannot be
the substrate automaton; it can only be a toy of the interior-effective dynamics** — and the paper's
own architecture (§8.4) makes that a *licensed* role, not a fudge: the interior description is
exactly the coarse-grained, information-discarding, Rule-30-like face of a reversible boundary
computation, with the discarded information sequestered behind horizons. An irreversible toy of an
irreversible effective description is the right level of analogy. Indeed the disorder→order
transition D&N exhibits is *possible only because* it discards information — which mirrors the
model's claim that interior renewal is paid for by information flow across the boundary. Any future
text must state this scoping in the same breath as the result.

- **Deep caveat (the reason a reversible demo is hard):** a *closed* reversible CA started from a
  typical maximal-entropy state cannot exhibit this transition at all — fine-grained information is
  conserved, coarse-grained entropy of a typical state stays maximal, and Poincaré recurrence
  replaces renewal. A reversible demonstration therefore *necessarily* needs the holographic
  ingredient: an explicit boundary subsystem into which the interior's entropy is exported during
  decompression. That is not a weekend experiment; it is a research program — and it is exactly what
  §9.7's "What would resolve it" already asks for. The D&N result should be framed as evidence for
  the *saddle-instability half* of NEW-1 (the disordered extremum is not a resting place), explicitly
  not as the holographic-decompression half.

- **Does a reversible Class-4 rule with on/off symmetry exist? Yes: Critters.** Critters (Margolus
  neighborhood block CA; Toffoli & Margolus, *Cellular Automata Machines*, 1987; Margolus,
  "Physics-like models of computation," Physica D 10:81, 1984 for the block-CA framework) is exactly
  invertible, conserves particle number in its natural representation, supports gliders and complex
  collision dynamics (billiard-ball-style logic, hence plausibly universal), and — the striking part —
  its standard formulation **complements the entire lattice every timestep**: the state alternates
  pattern/anti-pattern with period 2 built into the law. A reversible Class-4 rule whose *dynamics
  literally alternate day and night* is the natural next target, and the per-step complement is a
  toy of T-conjugation layered on the C-conjugation, much closer to a genuine CPT analogue. Other
  reversible routes: second-order (Fredkin) construction s(t+1) = F(neighborhood at t) XOR s(t−1)
  applied to D&N itself — manifestly reversible, and worth checking whether self-complementarity
  survives the construction (plausible since F is self-complementary; verify before claiming); and
  the reversible block rule Tron. Expected sobering outcome per the deep caveat: Critters from a
  typical ρ = 1/2 soup will *stay* disordered (reversibility forbids the entropy drop) — which is
  itself a publishable contrast pair: "irreversible interior-effective rule decompresses; closed
  reversible rule cannot; therefore renewal requires the boundary information channel." That triptych
  (GoL / D&N / Critters) states NEW-1's logic as three runnable facts.

## Recommendation

**Run it.** The experiment is cheap (days of work with Golly/lifelib, not weeks), the pilot already
shows the headline effect, the refutation criteria are sharp, and every outcome is informative:

1. **Minimum result (high confidence):** the D&N-vs-GoL contrast figure — "saturation decays into
   order with persistent complexity under an exact on↔off symmetry; without the symmetry it decays
   into ash." This directly upgrades §5.4's honest caveat ("no known cellular automaton demonstrates
   this behavior") to "a partial demonstration exists for the saddle-instability component," and
   gives §9.7 a concrete exhibit. It does NOT discharge Weak Point 7 — holography and reversibility
   remain undemonstrated — and the text must say so.
2. **Stretch result:** the GoL/D&N/Critters triptych plus the preimage-census quantification of
   information loss, framing renewal as *requiring* an information export channel — which is the
   paper's own architecture talking, now with numbers.
3. **Paper placement:** one figure + ~2 paragraphs in §5.4 (replacing the bare GoL caveat) and a
   sentence in §9.7; alternatively a short standalone companion note ("Order from saturation in a
   self-complementary cellular automaton") that the paper cites — keeps SB-HC4A's length down and
   gives the result its own citable home.
4. **Wording discipline if adopted:** "C-type (matter/antimatter) alternation," not "CPT"; "block
   entropy," not "entropy"; "saddle-instability component of the conjecture," not "saturation
   trigger demonstrated"; "complex / glider-supporting," not "universal," for D&N.

### Appendix: pilot code (for reproduction)

Symmetry check, vacuum fixed points, 256² soup comparison (D&N vs GoL: density, 2×2 block entropy,
activity at t ∈ {0, 50, 200, 400}), ρ = 0.95 collapse runs, and the exhaustive 4×4-torus predecessor
census were run with throwaway pure-Python scripts in this session (single seed, synchronous
updates, torus BCs). Headline numbers: D&N ρ₀ = 0.5 → S₂: 3.999 → 1.644 bits at t = 400 with
density 0.407 and activity 0.032; GoL same protocol → density 0.063, S₂ 1.171, activity 0.044
(blinker ash); D&N 4×4 GoE fraction 49.3% (max preimages 309) vs GoL 72.7% (max preimages 9,628).
A production rerun should use lifelib/Golly with ≥20 seeds and the observables of §4.
