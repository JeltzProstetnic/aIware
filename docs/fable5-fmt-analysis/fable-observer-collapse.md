# The Observer in a Collapsing Region: Self-View vs. Outside-View — Fable 5 analysis

**Question (author, verbatim):** "what happens to an observer as seen by himself vs as seen from
outside if he happens to be already inside a region that collapses into a black hole (be it during
the big crunch or elsewhere)?"

**Scope:** analysis only, against `paper/cosmology/sb-hc4a.md` (§5.2, §5.3, §5.4, §6, §8.2) and
`tmp/cosmology-drafts/fable-unreachability-analysis.md` (asymptotic silence, no-arrival,
computational depth). No edits applied.

**Headline:** The two views are the textbook pair of black-hole complementarity, and they map onto
the paper's substrate/simulation split with unusual precision: the outside-view is the
surface-encoded (compressed) description, the self-view is the decompressed interior description,
and complementarity's no-cloning structure is a concrete, established instance of the paper's
"one surface, many reflections" ontology. The crunch case adds the genuinely novel twist: a global
collapse destroys the exterior observer class, so the outside-view loses every interior holder —
and on the single-surface ontology that is not a pathology but the model's own limiting case: all
reflections collapse back into the one encoding surface (§5.4's saturation). Two to three sentences
should enter §8.2, with one optional clause in the reframed §5.3 crunch material.

---

## 1. The self-view: smooth crossing, finite time, termination without arrival

All of the following is standard general relativity.

**Nothing marks the horizon locally.** By the equivalence principle, a freely falling observer
crossing the event horizon of a large black hole detects no membrane, no wall, no local
discontinuity — the curvature invariants at the horizon scale as ~1/M², arbitrarily small for
large M (for a 10⁹ M_⊙ supermassive hole, tidal forces at the horizon are weaker than Earth's).
The paper already states this correctly in §5.2 ("no membrane, no wall, no detectable marker").
The horizon is globally defined (boundary of the causal past of future null infinity) and is
teleological: its location depends on the entire future of the spacetime, so an infalling observer
*cannot even know in principle* the moment of crossing from local measurements.

**Finite proper time, with a hard ceiling.** From horizon crossing to termination, the maximum
proper time inside a Schwarzschild interior is τ_max = πGM/c³ ≈ 15 μs × (M/M_⊙) — about a quarter
hour for a 10⁹ M_⊙ hole. Inside, the radial coordinate becomes timelike: decreasing r is as
compulsory as advancing t outside; the singularity is in the observer's *future*, not at a place
he travels toward. Firing rockets does not help — accelerated worldlines reach the singularity
*sooner* than geodesics (geodesics maximize proper time).

**The view out.** A misconception worth preempting: the infaller does **not** see the entire
future history of the universe compressed at the horizon. He continues receiving exterior signals
(moderately blueshifted/aberrated) all the way to termination, but only a finite slice of exterior
time ever reaches him. The "see the whole future" phenomenon belongs to Cauchy (inner) horizons of
Kerr/Reissner-Nordström, not to the Schwarzschild interior or a generic collapse.

**Tidal growth and the generic approach.** Tidal acceleration grows as ~GM/r³ (spaghettification),
diverging at the singularity. But the idealized Schwarzschild interior is not generic: near a
generic spacelike singularity the dynamics are BKL/Mixmaster (Belinskii, Khalatnikov & Lifshitz,
1970; Misner, 1969) — chaotic oscillations of anisotropic stretching and squeezing — with
**asymptotic silence** (Uggla, van Elst, Wainwright & Ellis, 2003): light cones collapse onto
worldlines, causal contact with neighbors shuts off, and the final dynamics are ultralocal. The
observer ends alone, in causal isolation, even from his own extended body's parts.

**No arrival.** The terminus is geodesic incompleteness (Penrose, 1965; Hawking & Penrose, 1970):
the worldline has finite length and *no extension*, but the singularity is not a point-set in the
manifold — there is no event of arrival, nothing is reached (ideal-boundary constructions: Geroch,
Kronheimer & Penrose, 1972). This is the **boundary-without-arrival-event** mode established in
the unreachability analysis (§C there), and the computational-depth observation carries over
verbatim: in the vacuum-dominated BKL approach, *unboundedly many dynamical epochs* pack into the
finite proper-time interval — geometrically finite, computationally asymptotic (flag: matter-
dependent; stiff fluid/scalar suppresses oscillations; the epoch-to-update-step identification is
the model's interpretive layer).

**Self-view summary:** an unremarkable crossing he cannot date, a finite private future, growing
tides, terminal causal solitude, and an ending that is a cessation-of-worldline rather than a
collision with anything. He never observes "being inside a black hole" as an event; he only ever
observes ordinary local physics, then does not observe.

## 2. The outside-view: freeze, dim, thermalize, re-emit — and who is left to watch

**The asymptotic picture (requires a persisting exterior).** For a distant observer, the infaller
asymptotically approaches the horizon in coordinate time, never crossing: signals redshift as
e^(−t/4GM) (e-folding time ~4GM/c³, so a stellar-mass infaller fades below any detection threshold
in milliseconds — "frozen star" is the right geometry but the wrong visual; he *dims out*, fast).
In the membrane paradigm / stretched-horizon description (Thorne, Price & Macdonald, 1986;
Susskind, Thorlacius & Uglum, 1993), the exterior observer's account is fully physical: the
infaller's information is deposited on a Planck-proper-length stretched horizon, heated to the
Hawking temperature, scrambled across the horizon on the fast-scrambling timescale
t* ~ (β/2π) ln S (Sekino & Susskind, 2008; Hayden & Preskill, 2007), and eventually re-emitted in
Hawking radiation. Unitarity bookkeeping is the Page curve (Page, 1993): radiation entropy rises,
turns over at the Page time, returns to zero — the resolution the paper already cites (Penington,
2020; Almheiri et al., 2020; Raju, 2022, §8.2). On the exterior account the infaller is never
lost: he is compressed onto a surface, thermalized, and returned as correlations in radiation.

**The crucial wrinkle: the outside-view is class-relative.** Every element of that description —
coordinate time diverging, the frozen image, the Page curve running to completion — presupposes an
observer class that persists: technically, a future null infinity (or at least a long-lived
quasi-exterior). Two cases must therefore be split:

- **Local black hole in a persisting universe.** Both descriptions are instantiated. The exterior
  class exists, collects the radiation (in principle — evaporation takes ~10⁶⁷ yr (M/M_⊙)³), and
  the complementarity structure of §3 below is fully operative.
- **Global collapse / Big Crunch.** A recollapsing universe has **no future null infinity**, hence
  strictly no event horizons — collapsing regions are characterized by apparent horizons and
  trapped surfaces instead. More importantly, the exterior observer class is itself terminating:
  during contraction inhomogeneities grow violently (shear ~ a⁻⁶), trapped regions form and merge,
  and eventually *every* observer is inside one — the distinction between "falling into a black
  hole" and "hitting the crunch" dissolves into one spacelike singular boundary. There is no Page
  time (crunch time ≪ evaporation time), no completed Page curve, no persisting vantage from which
  the freeze-picture is ever held. **The outside-view does not become false; it becomes
  unoccupied.** Everyone is, in the end, the infalling observer — each terminating privately, in
  asymptotic silence, with the "merged endpoint" in no one's past light cone (per the
  unreachability analysis, §E).

So the answer to "as seen from outside" bifurcates: *outside a local hole*, a dimming freeze
followed by thermal re-emission; *in a crunch*, there is no outside — the question's second half
loses its subject while its first half (the self-view) holds for every observer there is.

## 3. Black-hole complementarity: why the two views do not contradict

Susskind, Thorlacius & Uglum (1993), building on 't Hooft (1985), proposed that the two
descriptions are **both valid and never in conflict**, because no single observer can access both.
The apparent contradiction — the infaller's bits smoothly inside *and* scrambled on the
horizon/in the radiation — would violate quantum no-cloning only if some observer could verify
both copies. No one can: an exterior observer who collects the Hawking-radiated copy and then
jumps in to compare cannot receive the interior copy before termination — the required signal
from the early infaller would have to be sent with energy exceeding the hole's mass once the
verification window (set by the Page/scrambling times) is worked out (Susskind & Thorlacius, 1994;
Hayden & Preskill, 2007). The horizon's causal structure *enforces* the consistency: the two
accounts are complementary in an operationally exact sense — like conjugate descriptions, valid
relative to disjoint observer classes, with no super-observer to register a contradiction.

Two refinements the paper already cites point the same way, harder:

- **ER=EPR** (Maldacena & Susskind, 2013; §5.2): interior modes and early radiation are not two
  entangled systems but two presentations of one configuration connected through Planck-scale
  wormholes — proposed precisely to resolve the firewall tension (§5) by *identifying* the interior
  with the radiation rather than duplicating it.
- **Holography of information** (Raju, 2022; §8.2): in quantum gravity the information in a bulk
  region is also available on its boundary at all times — the exterior description is not a
  late-time reconstruction but holds continuously.

## 4. The mapping to SB-HC4A: is self-vs-outside literally the simulation/substrate split?

**The mapping, stated.** In §8.2's terms: the outside-view is the **compressed form** — the
infaller's information encoded on a Bekenstein-saturated surface (the stretched horizon literally
is a maximum-density, scrambled, boundary encoding — "the substrate"). The self-view is the
**decompressed form** — the same information experienced as an organized, low-density, smooth
interior with a person in it ("the simulation"). Complementarity then asserts what §5.2 asserts:
these are not two things but **one information content under two presentations**, with the
interior being "the same encoding surface viewed from the far side, decompressed into the
observer's emergent description" (§5.2, Step 4, nearly verbatim). The no-cloning protection — no
observer accesses both — is the operational face of impermeability (IB1): the same causal
structure that makes the boundary information-impermeable is what makes the dual descriptions
consistent. So yes: black-hole complementarity is a concrete, mainstream-physics instance of the
paper's surface/reflection duality, and the single-surface ontology is recognizably its
generalization (one surface, *all* horizons, all scales). This is the paper's strongest available
anchor for the substrate/simulation language in established physics — stronger than analogy,
because the two SB-HC4A forms (compressed/decompressed, §8.2) correspond term-by-term to the two
complementary descriptions (stretched-horizon/infalling).

**Where the analogy is exact:**
1. Two valid descriptions of one information content — never co-instantiated for any observer
   (complementarity) ↔ one surface, many reflections, impermeability between them (§5.2).
2. Surface description = maximum-density, scrambled, thermal (stretched horizon) ↔ compressed
   substrate form (§8.2). Interior description = organized, accessible, low-density ↔
   decompressed simulation form (§8.2).
3. ER=EPR's "interior = radiation, identified not duplicated" ↔ "no interiors-with-contents;
   the interior IS the surface seen from elsewhere" (§5.2 Step 4).
4. Crunch limit: all observers become infallers, reflections merge, only the surface encoding
   persists ↔ §5.4's saturation-and-restart, where the boundary carries the cycle's information
   forward. The exterior-view "losing its holder" is fatal for purely *relational* readings of
   complementarity (a description with no describer) but is exactly what the substrate ontology
   predicts: the encoding surface never needed an interior observer to hold it.

**Where it strains (the paper must not overclaim):**
1. **Complementarity is epistemic/operational; the single-surface ontology is metaphysical.**
   Susskind–Thorlacius–Uglum claim the two descriptions are *both valid*; they do not claim the
   interior "does not exist" or is ontologically derivative. The SB-HC4A's asymmetry — surface
   fundamental (substrate), interior derived (simulation) — is an added interpretive commitment.
   Holography-of-information and ER=EPR lean toward surface-primacy, but standard complementarity
   is symmetric between the descriptions. Flag the overlay as overlay.
2. **Relativity of the split.** The exterior observer holding the "substrate-side" description of
   this black hole is himself a decompressed pattern relative to the *cosmological* boundary. The
   self/outside split is therefore not the absolute substrate/simulation split but its local,
   scale-indexed re-instantiation at one member of the inventory. This is actually a feature — it
   is §5.2's "reflections at every scale" made concrete — but stated carelessly ("the outside
   observer sees the substrate") it would be wrong: he sees a *reflection of* the substrate from
   inside the domain, one level up.
3. **Complementarity is not settled physics.** AMPS (§5 below) showed the naive version is
   internally strained; the islands program currently repairs it, but a referee will object to
   "complementarity is established" without a hedge. Say "the complementarity *structure*" and
   cite the tension.
4. **The infaller's experience as "decompression" is the model's reading.** GR says the interior
   description is smooth; it does not say the interior is *computed by decompressing the surface*.
   The direction of explanation is the model's, licensed but not mandated by holography.

**Net answer to the author's question, in SB-HC4A currency:** by himself, the observer
experiences the decompressed description to its last update — ordinary physics, no boundary
event, terminal causal solitude, ending as cessation rather than arrival (and, in BKL approaches,
possibly unbounded computational depth inside finite proper time). From outside — *when an
outside exists* — he is watched being compressed: frozen, dimmed, thermalized onto the surface,
and returned as Hawking correlations per the Page curve. The two are one process under the two
forms of §8.2. In a Big Crunch the second description loses every holder because the whole
observer inventory joins the first; what persists is what the model says always persisted — the
surface encoding, which is precisely the object §5.4 hands to the next cycle.

## 5. Firewalls (AMPS): state the tension, do not adopt a side

Almheiri, Marolf, Polchinski & Sully (2013) showed that three assumptions, each individually
compelling, are jointly overconstrained for an old (post-Page-time) black hole: (i) unitary
evaporation (the Page curve), (ii) validity of effective field theory outside the horizon,
(iii) a smooth horizon (no drama for the infaller). After the Page time, an outgoing late mode
must be near-maximally entangled with the early radiation (by unitarity) *and* with its interior
partner mode (by smoothness) — violating monogamy of entanglement. Something gives: either the
infaller hits a Planck-energy "firewall" at the horizon (smoothness fails — the self-view of §1
would be wrong), or EFT fails, or the entanglement accounting is subtler. Proposed resolutions:
ER=EPR (interior mode *is* the early radiation — identification, not double entanglement),
state-dependent interior operators (Papadodimas & Raju, 2013), and the replica-wormhole/islands
results (Penington, 2020; Almheiri et al., 2020 — both already cited) which recover the Page
curve from gravity while keeping the horizon smooth, currently the mainstream direction.

**Recommendation: mention, one clause, no side.** The paper's commitments (unitarity §8.2/§8.4,
smooth crossing §5.2, monogamy doing load-bearing work in §6.5) are exactly the AMPS triple, so
silence would be conspicuous to a knowledgeable referee — but adjudicating it is far outside the
paper's scope. Note it as an open problem whose leading resolutions (ER=EPR, islands — both
already in the reference list) are the ones the paper already relies on. Incidentally, that the
paper's §6.5 uses entanglement monogamy and AMPS is a monogamy argument is a nice consistency
point but should not be expanded — one clause, no more.

## 6. Recommendation: yes — 2–3 sentences in §8.2, one optional clause in reframed §5.3

**Where.** §8.2 is the right home: complementarity is *about* the dual description of infalling
matter, and §8.2 is where the compressed/decompressed duality is defined. §5.3's
termination-without-arrival material (per the pending reframe) gains one optional clause on the
crunch's destruction of the exterior class. §6 needs nothing — the architecture section should
not carry physics arguments.

**Proposed text for §8.2** (insert after the sentence ending "...a requirement Section 8.4
elevates to an explicit architectural commitment."):

> Black-hole complementarity (Susskind, Thorlacius, & Uglum, 1993; 't Hooft, 1985) gives this
> conservation an observer-indexed form that the present model generalizes: the exterior
> description — infalling matter freezing, thermalizing, and scrambling on a stretched horizon
> before re-emission — and the infalling description — a smooth, markerless crossing followed by
> ordinary interior physics — are both valid accounts of the same information, and no observer
> can access both, the horizon's causal structure protecting the no-cloning theorem. These are,
> respectively, the compressed and decompressed forms defined below: complementarity is the
> established local instance of the substrate/simulation duality, of which the single-surface
> ontology of Section 5.2 is the proposed generalization. Whether the smooth interior survives
> unitarity for old black holes remains contested (the firewall argument: Almheiri, Marolf,
> Polchinski, & Sully, 2013); the entanglement-island results already cited (Penington, 2020;
> Almheiri et al., 2020) currently favor smoothness, and nothing in this section depends on the
> outcome.

(Three sentences. Sentence 1 is established physics; sentence 2 is the interpretive SB-HC4A
overlay and is worded as a proposal — "proposed generalization"; sentence 3 is the honesty flag.)

**Optional clause for the reframed §5.3** (temporal-axis/crunch material, attachable to the
causal-fragmentation paragraph recommended in the unreachability analysis §E):

> The exterior member of the complementary pair, moreover, requires a persisting exterior: a
> recollapsing universe has no future null infinity and hence no event horizons properly so
> called, and the would-be distant observers are themselves terminating — in a global crunch the
> frozen-infaller description loses every holder, and only the infalling description, ending
> privately and without arrival, remains instantiated.

**Established vs. overlay, stated plainly:**
- *Established:* equivalence-principle smoothness; finite proper time; geodesic incompleteness
  and no-arrival; BKL/asymptotic silence (generic, matter-dependent); exterior freeze/dimming;
  stretched-horizon thermalization; Page curve; complementarity as proposal + no-cloning
  protection; AMPS tension; islands resolution; no-event-horizons-in-recollapse.
- *SB-HC4A overlay (flag in any inserted text):* surface = substrate, interior = decompressed
  simulation; surface-primacy (asymmetric reading of a symmetric duality); crunch as
  reflections-merging-into-the-one-surface feeding §5.4's cycle; BKL epochs as substrate update
  steps.

**New citations to verify before any insertion (CLAUDE.md rule):**
- Susskind, L., Thorlacius, L., & Uglum, J. (1993). The stretched horizon and black hole
  complementarity. *Physical Review D*, 48(8), 3743–3761.
- 't Hooft, G. (1985). On the quantum structure of a black hole. *Nuclear Physics B*, 256,
  727–745. (Distinct from the two 't Hooft entries already in the list.)
- Almheiri, A., Marolf, D., Polchinski, J., & Sully, J. (2013). Black holes: complementarity or
  firewalls? *Journal of High Energy Physics*, 2013(2), 62. (Note: different Almheiri paper from
  the 2020 RMP already cited — both needed if the firewall clause goes in.)
- Optional, only if "Page curve" is named with attribution: Page, D. N. (1993). Information in
  black hole radiation. *Physical Review Letters*, 71(23), 3743–3746.
- BKL/Misner/Uggla et al. are already queued for verification by the unreachability analysis;
  no duplication needed here.
