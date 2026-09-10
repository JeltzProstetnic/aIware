# Unreachability, PII, and the Termini — Fable 5 re-analysis of the author's objections

**Scope:** author pushback on corrections C1/C1b/C3 (spec: `docs/pending-cosmology-corrections.md`),
against the current `paper/cosmology/sb-hc4a.md` (§4.2, §5.1–5.3, §5.5, §5.7, abstract).
Analysis + recommendations only; no edits applied.

**Headline:** The author is substantially right on points 2, 3, 4 and 6 — more right than the
prior correction pass allowed — but each point needs a corrected technical form to survive review.
He is wrong (in the strong form) on point 5, though a weaker operational form of it is both correct
and already in the text. C1's physics (η finite at t→0 = the horizon problem; geodesic
incompleteness at finite proper time) is robust and must be preserved verbatim in substance.
What should change is the *framing*: "horizons vs termini / unreachable vs reached" is a false
dichotomy. The honest structure is a three-axis taxonomy of unreachability with three distinct
*modes*, in which the termini are not "reachable" but unreachable in a different way:
**boundary-without-arrival-event**. The single most important physical insight supporting the
author: in the paper's own ontology (time = automaton update steps; proper time emergent),
*finite proper time does not imply finite computational depth* — the Mixmaster/BKL approach to a
generic spacelike singularity packs unboundedly many dynamical epochs into finite proper time, so
the terminus can be computationally asymptotic even where it is geometrically finite.

---

## A. Language: "computationally irreducible computation" (point 1) — REVISE (change the noun, not the adjective)

The author's ear is right: "computationally irreducible computation" is a pleonasm and reads badly
in the abstract. But his proposed fix — "irreducible computation" — drops the wrong word.
"Computationally irreducible" is Wolfram's term of art (Wolfram, 2002, §12.6); it is the exact
keyword that signals to a referee which technical concept is meant and connects to §2.4. Bare
"irreducible" is ambiguous (irreducible representation? indivisible? non-decomposable?), and the
abstract must be self-contained.

**Fix:** keep the adjective, change the noun.

> Current: "Classes 1–3 cannot sustain the computationally irreducible computation the universe
> demonstrably performs"
>
> Proposed: "Classes 1–3 cannot sustain the **computationally irreducible dynamics** the universe
> **demonstrably exhibits**"

(Alternative if "dynamics... exhibits" feels weak: "...cannot sustain computation of the
computationally irreducible kind the universe demonstrably performs" — heavier; first option
preferred.) Sweep the body for the same doubled construction; §2.4/§3.2 uses are fine where
"computation" is not the immediate noun.

**Verdict: REVISE** as above. The author's instinct (kill the repetition) is right; his specific
cure (drop "computationally") would cost the term of art.

---

## B. PII as a secondary line (point 2) — REVISE §5.2 (keep single-surface primary, reinstate a *scoped* indiscernibility argument as secondary); CUT the abstract disclaimer

### Where the author is right

1. **The indiscernibility at issue is in-principle, not merely unobserved.** The impermeability of
the inventory's boundaries is nomological: no observation available to any observer *who remains in
causal contact with the computational domain* can ever discriminate between the putative interiors.
This is categorically stronger than "we haven't looked," and it is exactly the condition under
which an *operational* identification principle has bite. The prior pass treated PII as if the
author were invoking it against merely-unobserved differences; he isn't.

2. **The surface/interior asymmetry is real and does dialectical work.** Surfaces are richly
discernible — mass, charge, angular momentum, and they can be *collided* (LIGO mergers are
observed events; the author's "colliding them with other such surfaces" is literally GW astronomy).
Interiors are discernible by nothing. That asymmetry maps precisely onto §5.2's existing
reflection/presentation distinction ("these are properties of the *reflection*"): the discernible
properties are exactly the ones the single-surface ontology assigns to the presentation, and the
indiscernible "remainder" is exactly what it says doesn't exist. So a scoped PII is not in
*tension* with the single-surface ontology — it is its operational shadow, and a natural fallback
for readers who balk at the postulate.

3. **"Relatively true" is the right epistemics.** As a *necessary metaphysical law*, PII is
contested; as a *methodological razor* ("do not multiply entities that differ in no
domain-accessible respect"), it is just parsimony — and parsimony is already the paper's declared
defense of the postulate. The secondary line costs nothing the paper hasn't already spent.

### What a referee would still object to — and the required scoping

- **Black's spheres (Black, 1952, *Mind*).** PII as a necessary truth has a famous counterexample:
  two qualitatively identical spheres in an otherwise empty symmetric universe are indiscernible
  yet two. The quantum-statistics literature (French & Redhead 1988; Saunders 2006 on weak
  discernibility) keeps the principle contested even for physics. **Therefore: never present PII
  as a law; present it as a razor.** One clause suffices.
- **Verificationism.** "Indiscernible-to-us ⇒ identical" is verificationism unless the paper has
  independently argued that there are no vantage-independent facts beyond horizons. It *has* —
  that is §4.1 ("no existence independent of its boundary encoding") and the Step-4 postulate. So
  the honest logical order is: the razor *presupposes* the operational reading of horizons the
  paper already adopts; it cannot replace the postulate, only corroborate it. State this
  dependence explicitly or the referee will state it for you.
- **The infalling-observer hole (the sharpest physics objection).** In classical GR, black-hole
  interiors are NOT indiscernible simpliciter. The interior of a Schwarzschild black hole is a
  perfectly regular spacetime region; an infalling observer measures tidal profiles, encounters
  recently-infallen matter, and two holes of identical exterior (M, Q, J) can differ transiently
  inside (no-hair characterizes the settled *exterior*). Indiscernibility holds only **relative to
  the class of observers who remain in the computational domain** — the infaller leaves it. The
  paper can absorb this (on the single-surface ontology the infaller's experience is itself a
  decompressed presentation, and §5.3 already defines the operative domain as "the domain in which
  physics operates and information is exchanged"), but the secondary PII text MUST carry the index
  "from within the domain," or a relativist will demolish it with one sentence.

### Recommended action

**Keep §5.2 Step 4 and the "Note what this postulate does *not* rely on" paragraph essentially as
they stand** ("probably no need to correct page 12 much" — agreed). The existing paragraph attacks
the *burden-shifting* form of the indiscernibility argument ("grant distinct interiors, then argue
they must be counted identical") — that criticism remains correct and should stay. **Add one new
paragraph immediately after it**, reinstating the operational form as explicitly secondary:

> *Proposed insertion (after the "Note what this postulate does not rely on" paragraph):*
>
> A weaker, operational relative of that retired argument does, however, survive as a secondary
> line of support. Even a reader who declines the postulate — who insists on distinct
> interiors-with-contents — must grant that those interiors are indiscernible *in principle* from
> within the computational domain: impermeability is nomological, not practical, so no observation
> available to any observer in causal contact with the domain could ever distinguish them — while
> their *surfaces* are richly discernible, in mass, charge, and angular momentum, and can even be
> made to collide (black-hole mergers are observed events). An operational razor — do not multiply
> entities that differ in no domain-accessible respect — then counsels the same conclusion the
> postulate asserts. This is offered strictly as corroboration, not foundation: as a metaphysical
> law the Identity of Indiscernibles is contested (Black, 1952), and indiscernibility-to-the-domain
> licenses identity only given the reading of horizons Section 4.1 already adopts — which is why
> the unification rests on the single-surface postulate, with the razor as its operational shadow.

(Four sentences; matches the paper's hedging register. **New citation to verify before adding:**
Black, M. (1952). "The Identity of Indiscernibles." *Mind* 61(242), 153–164. If the author prefers
zero new citations, "is philosophically contested" works without the cite, but the cite is cheap
armor: it shows the objection is known, named, and priced in.)

**Abstract:** Yes — cut the defensive clause. "argued from a single-surface ontology rather than
from the Identity of Indiscernibles" should become simply "argued from a single-surface ontology."
Abstracts should not enumerate what the argument is *not*; the clause wastes ~10 words, advertises
an internal course-correction to referees, and after the reinstatement above it would also be
half-false.

**Verdict: REVISE** (insertion above + abstract trim). Do not revert C3 — the single-surface
primary is strictly stronger than PII-as-foundation and the retirement of the *burden-shifting*
version was correct.

---

## C. The taxonomy of unreachability (points 3 & 4) — REVISE §5.3: the C1/C1b narrowing was too strong; reframe as three axes, three modes

### Was the narrowing too strong? Yes — in framing, not in physics.

C1/C1b correctly fixed two factual errors (η finite at t→0; crunch reached at finite proper time).
But it then adopted the frame "horizons are unreachable; termini are reached," which concedes more
than the geometry requires. The author's question 3 — "isn't this only by definition? how would ANY
observer 'reach' the big crunch?" — lands on a genuine distinction in GR:

**A singularity is not a place; "reached" is a façon de parler.** Geodesic incompleteness
(Hawking & Penrose, 1970) says a causal worldline has finite affine length and *no extension* — it
does not say the worldline arrives anywhere. The singular boundary is not a point-set in the
manifold; for every proper time τ before the end, the observer is at finite curvature, inside
perfectly ordinary spacetime; the "endpoint" itself is never an element of the worldline, never an
event, never an experience. It can be attached only as an *ideal* boundary point (Geroch,
Kronheimer & Penrose, 1972, causal boundary; Schmidt, 1971, b-boundary) — an abstract completion,
not a location. So the precise statement is:

- **Horizon:** a genuine null hypersurface *in* the spacetime, which the exterior domain
  asymptotically approaches and never attains (infinite coordinate time, infinite redshift). The
  boundary exists as a locus; arrival is forbidden.
- **Terminus:** a boundary that is *not in the spacetime at all*. Worldlines end at finite proper
  time, but nothing ever arrives *at* the singularity, because there is no "at." Arrival is not
  forbidden; it is **undefined**.

Both are failures of arrival. They are different *modes* of the same fact: **no observer, ever, is
at any member of the singularity inventory.** The author's "maybe it is a different KIND of
unreachability" is exactly right, and it is standard GR, not special pleading. C1's concession
(finite proper time, geodesic incompleteness, η finite) survives untouched inside this frame — what
changes is the conclusion drawn from it: not "termini are reached," but "termini terminate without
being reached-as-events."

A useful sharpening the current text misses: in ΛCDM the *future* conformal time is also finite
(η → η_max as t → ∞) — that finiteness is precisely why a future event horizon exists. So finite
conformal coordinate does not separate horizons from termini at all; both have it. The real
discriminator is **proper time** (infinite to the de Sitter future, finite to the Bang/Crunch).
Stating this makes the taxonomy look like what it is — geometry — rather than a rhetorical rescue.

### The author's three axes — evaluation

One **terminological landmine first**: do NOT use "space-like" and "time-like unreachability." In
GR parlance the Big Bang and Big Crunch are *spacelike* singular hypersurfaces, and event horizons
are *null* hypersurfaces — the author's axis-labels are nearly the inverse of the technical usage,
and a gravitation referee will flinch on contact. Use **"unreachability along the spatial axis /
the temporal axis / the scale axis"** (matching §4.2–4.3's existing space/time/scale structure),
and add one parenthetical showing the technical classification is known ("the termini are, in the
technical classification, *spacelike* singular hypersurfaces; the axis language used here refers to
the direction of approach within the computational domain, not to the causal character of the
boundary").

- **Spatial axis — asymptotic recession (rigorous).** Event horizons and the observer-dependent
  cosmological horizon, exactly as the current §5.3 has them. No change needed.
- **Scale axis — asymptotic shielding (standard-heuristic, and a genuine strengthening).** The
  author's point 4 is right and the current §5.3 *does* omit it, even though §4.3 declares scale a
  bounded axis and §5.1 lists two scale-axis members. The defensible content: (i) resolution
  improves with collision energy as Δx ~ ħ/p only until horizon formation reverses it — at
  trans-Planckian energies the collision region collapses into a black hole whose Schwarzschild
  radius *grows* with further energy, so pushing harder toward the Planck floor makes the boundary
  *recede* (the minimal-length/GUP literature already cited: Garay 1995; Hossenfelder 2013; the
  self-completeness form is Dvali & Gomez, if a cite is wanted — verify before adding). This is the
  same "recedes as approached" geometry as the spatial horizons, realized in resolution rather than
  distance. (ii) The author's "particles never touch": true classically for like charges (zero
  separation costs unbounded energy) and true operationally in general (no experiment localizes two
  particles at zero separation; the floor is the same GUP floor). **Caution for review:** phrase it
  as "no interaction ever resolves zero separation / interactions exchange information at finite
  resolution," NOT "particles never touch" — in QFT, vertices are pointlike in perturbation theory
  and "touching" is not an observable; a particle physicist will object to the naive phrasing.
- **Temporal axis — termination without arrival (the corrected C1/C1b content).** Keep every
  factual element of the current text: η finite at t→0 = the horizon problem; geodesic
  incompleteness at finite proper time; past-eternal continuations as the explicitly conditional
  escape; the cyclic mechanism not usable as independent support. Add the boundary-not-event
  distinction above, plus two honest enrichments from §E below (causal fragmentation of the
  realistic crunch; computational depth). Also note heat death separately: the de Sitter-like
  *future* is genuinely asymptotic in proper time (and §4.2 already says so) — the future temporal
  boundary largely folds into the horizon class; only the Bang and Crunch are termini.

### Does this restore unreachability as a shared property — strengthening the unification?

Partially, and the paper should say *exactly how much*:

1. **Shared rigorously by all six: impermeability (IB1–IB3).** Unchanged. Still the foundation.
2. **Shared by all six, in axis-dependent modes: no-arrival.** Nothing is ever at any of these
   boundaries as an event in the domain. Rigorous for horizons (forbidden) and termini (undefined);
   standard-heuristic for the scale floor (shielded). This is a real, true, shared property — but
   it is *weaker* than asymptotic approach, and for the termini it is partly a fact about
   definitions (what "arrival at a non-place" would even mean). Present it as a unifying
   *observation*, not a load-bearing premise.
3. **Asymptotic-approach geometry: horizons (rigorous), scale floor (heuristic), termini only
   conditionally** (past-eternal continuations) **or in computational-step count** (§E; heuristic,
   matter-dependent). Not universal; do not reclaim it as universal.

### Recommended skeleton for the reframed §5.3

> **§5.3 Unreachability Along Three Axes** *(title change from "Horizons versus Termini")*
> 1. Opening ¶: impermeability is the shared property the unification rests on (unchanged
>    commitment). Beyond it, every member of the inventory is unreachable from within the domain —
>    but in three distinct modes along the domain's three bounded axes, and the differences must be
>    drawn precisely. Parenthetical disarming the spacelike/timelike terminology collision.
> 2. **Spatial axis — recession.** Current event-horizon + cosmological-horizon paragraphs, as is.
> 3. **Scale axis — shielding.** New ¶: GUP/trans-Planckian horizon formation; boundary recedes in
>    resolution as approached in energy; zero-separation never resolved. Flag: standard arguments,
>    heuristic at the edges.
> 4. **Temporal axis — termination without arrival.** Current Bang/Crunch paragraphs (η finiteness
>    = horizon problem; finite proper time; geodesic incompleteness; conditional continuations —
>    all preserved), then: the singularity is not a locus in the manifold; worldlines end, nothing
>    arrives (ideal-boundary constructions); "reached" means only "of finite length." Then the two
>    §E additions: (a) realistic-crunch causal fragmentation; (b) computational-depth divergence
>    (clearly flagged as heuristic). Note the future/past proper-time asymmetry and that heat death
>    belongs with the horizons.
> 5. **What survives** (rewrite of current closing ¶): the three-tier honesty ladder above
>    (impermeability rigorous-universal > no-arrival universal-but-weaker > asymptotic approach
>    partial). The unification rests, as before, on the first; the taxonomy shows the termini do
>    not break the pattern of unreachability — they change its mode.

Consequential touch-ups: §4.2's definition already says bounds "either recede ... or terminate
information access" — extend to the three modes (recede / shield / terminate-without-arrival) in
one clause. Abstract sentence: see F.

**Verdict: REVISE** (reframe; preserve all C1/C1b physics inside the new frame).

---## D. Big Bang, finite proper time, and inflation (point 5) — the finite-depth claim is ROBUST; the author's strong form fails, but his operational form is right and worth one added paragraph

### Where the author overreaches (and would not survive review)

1. **"Inflation makes the finite-time claim wrong" — no; if anything the opposite.** The
   Borde–Guth–Vilenkin theorem (2003) shows that any spacetime with average expansion rate > 0
   along a congruence is past-geodesically incomplete — *inflation included*. Eternal inflation
   does not buy a past-eternal history; the classical description still ends at finite affine
   length. So inserting inflation between us and t = 0 does not convert the past boundary into an
   asymptotic one. (BGV shows the classical description is incomplete; it does not prove a
   *curvature singularity* — the boundary could be a quantum-gravity region, a bounce, or a
   junction. That distinction is the honest residue, and it belongs in the text.)
2. **"How would you go back in time THROUGH inflation?" conflates geometry with biography.**
   Proper time along a past-directed comoving worldline is a geometric functional; it is
   well-defined whether or not any physical clock could survive the trip. "Reached at finite proper
   time" is a statement about geodesics, not about traversability by an apparatus. A referee will
   say this in one line, so the paper must not rest anything on the traversability reading.
3. **"Maybe everything is actually wrong"** (finite past as the root error, inflation as the
   epicycle) is a respectable *minority research program* — it is precisely what CCC, Boyle–Turok,
   and bounce cosmologies explore, and the current §5.3 already cites all of them as the
   conditional escape — but as an argument it cannot be asserted; it is the model's own commitment,
   and the existing sentence ("this cannot be offered as independent support... the argument must
   not lean on it") is exactly the right amount of honesty. Keep it.

### Where the author is operationally right (and the text can honestly say so)

In the paper's own currency — *information access*, not geodesic length — the past terminus IS
shrouded: every signal channel decouples strictly before t = 0. Photons end at last scattering
(~380 kyr); neutrinos at ~1 s; gravitational waves are the deepest channel and decouple at the
Planck epoch — and reheating (~10²⁷ K) destroys any structured record that could constitute a
"traversal." So while the geometric depth of the past is finite, **no information channel extends
to the terminus**; the boundary is operationally asymptotic in the only sense the computational
ontology cares about, even though it is geometrically finite. This is the temporal-axis analogue of
the scale-axis shielding, and it is uncontroversial physics. One added paragraph in the
temporal-axis subsection captures it:

> *Proposed content (sketch):* The finite geometric depth of the past should be distinguished from
> its informational depth. Each observational channel terminates strictly before the boundary —
> photons at last scattering, neutrinos at weak decoupling, gravitational waves at the Planck
> epoch — and no record survives reheating. The terminus is therefore geometrically finite but
> informationally shrouded: finite proper time to a boundary no channel reaches. Note also that
> past-incompleteness is robust to inflation itself (Borde, Guth & Vilenkin, 2003): inserting an
> inflationary epoch does not extend the classical past to infinity; what it leaves open is only
> the *nature* of the finite-depth boundary — curvature singularity, bounce, or junction.

**New citation to verify before adding:** Borde, A., Guth, A. H., & Vilenkin, A. (2003). "Inflationary
spacetimes are incomplete in past directions." *Phys. Rev. Lett.* 90, 151301. (This cite actively
*helps* the paper: it preempts "but eternal inflation evades your finite past" from a referee.)

**Verdict on the C1 conformal-time content: KEEP-AS-IS**, with the one-paragraph operational
addition above. Do not adopt the author's strong reading ("the finite-time claim is wrong");
adopt his operational reading ("no observer/channel reaches it"), which is correct and strengthens
the section.

---

## E. Big Crunch, horizon-shrouding, and computation (point 6) — the author's intuition is RIGHT in corrected form; this is the best new material in the whole exchange

### Disentangling the two crunches

**Idealized homogeneous closed-FRW recollapse:** the author's claim is wrong here. The final
singularity is a global spacelike boundary; every comoving observer terminates at finite proper
time; there is no black-hole event horizon to cross first, because there is no "outside" — the
whole universe collapses together. If §5.3 said "one must cross an event horizon to reach the
crunch," a relativist would refute it with the closed-FRW Penrose diagram in one move.

**Realistic inhomogeneous recollapse:** here the author's picture is qualitatively vindicated,
with two technical corrections:

1. **"Event horizon" is the wrong object.** An event horizon is defined as the boundary of the
   causal past of future null infinity — and a recollapsing universe *has no future null infinity*.
   Black holes in a crunch are characterized by **apparent horizons / trapped surfaces**, not event
   horizons. Moreover the signature exterior-observer phenomenology of "never reaching the horizon"
   (asymptotic freeze-out, infinite redshift) requires a *persisting exterior observer class* — and
   the crunch destroys that class: every would-be exterior observer is themselves terminating. So
   the specific mechanism "you can't reach the merged endpoint because you can't reach an event
   horizon" does not go through as stated.
2. **What is true is stronger and better.** During contraction, inhomogeneities grow violently
   (shear scales as a⁻⁶), structure collapses into black holes, trapped regions form and merge, and
   eventually *every* observer is inside a trapped region — the distinction between "falling into a
   black hole" and "hitting the crunch" dissolves; the black-hole singularities and the
   cosmological singularity are one spacelike singular boundary, generically approached in the
   chaotic BKL/Mixmaster manner (Belinskii, Khalatnikov & Lifshitz, 1970; Misner, 1969). And near a
   generic spacelike singularity the dynamics exhibit **asymptotic silence**: light cones collapse
   onto worldlines, causal contact between neighboring worldlines shuts off, and the dynamics
   become ultralocal (Uggla, van Elst, Wainwright & Ellis, 2003; Andersson et al., 2004 — verify
   cites). Consequences, exactly in the paper's currency:
   - The computational domain does not march collectively into a wall; it **fragments into
     causally silent shards** before terminating — the time-reverse, structurally, of the Big Rip
     fragmentation the paper already describes in §5.4/§5.7. (This symmetry is a gift to the
     paper: the Rip shatters the domain outward, the crunch shatters it inward; both end in
     mutually silent Bekenstein-bounded fragments.)
   - **The "merged endpoint" is in no observer's past light cone.** No observer ever possesses the
     information that the merging "happened"; each worldline ends privately, in causal isolation,
     at finite proper time, without arrival (§C). The author's conclusion — *no observer reaches
     the endpoint-of-all-mergers* — is therefore correct, even though his mechanism (crossing an
     event horizon) is not. The endpoint is unreachable not because a horizon stands in front of it
     but because causal connectivity itself dies on the approach.

### "What happens to time and computation during a crunch?" — the deepest point

In the vacuum-dominated generic approach, the BKL behavior consists of an **infinite sequence of
Kasner epochs within finite proper time** — a Zeno-like packing of unboundedly many dynamical
transitions into a finite interval. For an ontology in which time *is* the automaton's update
sequence and proper time is emergent, this matters enormously: **finite proper time does not bound
computational depth.** Measured in the substrate's native units — update steps, dynamical epochs —
the terminus can be asymptotic even though the emergent geometric clock assigns it a finite
reading. That is the cleanest possible rehabilitation of the author's "different KIND of
unreachability," and it comes from mainstream singularity dynamics, not from the model.

**Honesty flags that MUST accompany it:** (i) the oscillation count diverging is matter-dependent —
a stiff fluid or massless scalar field suppresses the oscillations (monotonic AVTD behavior), so
"infinitely many epochs" is generic for vacuum-dominated approaches, not a theorem for all matter;
(ii) "update steps of the substrate" is not an operationally defined quantity in known physics —
the identification of BKL epochs with computational steps is the model's interpretive layer, and
the text should label it so; (iii) keep Tipler's Omega Point *out* of it (the superficially similar
"infinite computation in a crunch" claim is observationally dead under Λ > 0 and reputationally
radioactive; the BKL/asymptotic-silence literature carries the point without it).

### What §5.3/§5.4 should say

In the temporal-axis subsection (per the §C skeleton): one paragraph on the homogeneous/realistic
distinction (concede the idealized case has no shroud — this protects against the one-move
refutation), then trapped-surface proliferation + asymptotic silence + endpoint-in-no-past-light-cone,
then the computational-depth remark with its flags. In §5.4, one sentence connecting the crunch's
inward fragmentation to the Rip's outward fragmentation (both: domain → mutually silent saturated
fragments) — it tightens the "robust across all three endgames" claim already there.

**New citations to verify before adding:** Belinskii, Khalatnikov & Lifshitz (1970, *Adv. Phys.*
19, 525); Misner (1969, *PRL* 22, 1071, Mixmaster); Uggla, van Elst, Wainwright & Ellis (2003,
*PRD* 68, 103502); optionally Geroch, Kronheimer & Penrose (1972, *Proc. R. Soc. A* 327, 545) for
the ideal-boundary point in §C.

**Verdict: REVISE §5.3/§5.4** to include the corrected form. The author's claim as stated ("has to
go through a normal black hole event horizon first, which he can't reach") must NOT go in verbatim
— it fails for the homogeneous case and misuses "event horizon" — but its corrected form (causal
fragmentation; private termination; endpoint never observed; computational depth possibly
unbounded) is both true and the strongest addition this exchange produces.

---

## F. Net recommendations

| Item | Verdict | Summary |
|---|---|---|
| C1 (§5.3 conformal time) | **KEEP-AS-IS** (content) | η finite at t→0, finiteness = horizon problem, conditional past-eternal continuations: all correct, all preserved verbatim in substance inside the reframe. Add the BGV + informational-shrouding paragraph (§D). |
| C1b (§5.3 crunch / narrowing) | **REVISE** | Keep the physics (finite proper time, geodesic incompleteness — the concession stands). Replace the *frame* "horizons unreachable vs termini reached" with the three-axis, three-mode taxonomy (§C skeleton): recession (spatial), shielding (scale — new, restores particles/Planck floor to the section), termination-without-arrival (temporal). Add realistic-crunch fragmentation + computational-depth material (§E) with honesty flags. Title: "Unreachability Along Three Axes." |
| C3 (§5.2 single-surface / PII) | **REVISE** (minor) | Single-surface primary stays exactly as is ("page 12" needs almost no change — author is right). Reinstate a *scoped, operational* indiscernibility razor as explicitly secondary (proposed 4-sentence paragraph in §B), indexed to domain-internal observers, with the Black caveat. Cut the abstract's "rather than from the Identity of Indiscernibles" clause. |

**Abstract sentence** (consequential edit, replacing the current unreachability sentence):

> "Event horizons and the cosmological horizon recede asymptotically from every approach within the
> computational domain; the temporal termini (the Big Bang and a possible Big Crunch) terminate
> world-lines at finite proper time yet are never reached as events — a distinct mode of
> unreachability — and it is information impermeability, shared by every member of the inventory,
> on which the unification rests."

(Keeps impermeability load-bearing — do not re-inflate unreachability into a premise — while
honoring the taxonomy. Also apply §A's fix in the same sentence-pass: "computationally irreducible
dynamics the universe demonstrably exhibits.")

**Plain warnings — where the author's intuitions, as stated, would not survive review:**
1. "Space-like / time-like / scale-like unreachability" as labels: terminology collision with the
   GR classification (Bang/Crunch are *spacelike* singularities). Use axis language (§C).
2. "Inflation means the finite-time claim is wrong": BGV blocks this; inflation does not extend
   the classical past. The operational form (no channel reaches the terminus) is the survivable
   version (§D).
3. "Must cross an event horizon to reach the crunch": false for homogeneous recollapse and
   technically ill-posed (no future null infinity ⇒ no event horizons). The trapped-surface /
   asymptotic-silence form is the survivable version (§E).
4. "Particles never touch": phrase as resolution floor / no interaction resolves zero separation,
   not as naive non-contact — QFT vertices are pointlike in perturbation theory (§C).
5. PII reinstatement must be a razor indexed to domain-internal observers, never a law — Black's
   spheres and the infalling-observer objection are one-line refutations of the unscoped form (§B).

**New citations queued for the mandatory verification pass (CLAUDE.md rule) if the revisions are
adopted:** Black (1952); Borde, Guth & Vilenkin (2003); Belinskii, Khalatnikov & Lifshitz (1970);
Misner (1969); Uggla, van Elst, Wainwright & Ellis (2003); optionally Geroch–Kronheimer–Penrose
(1972) and Dvali & Gomez (2010, self-completeness). All others needed (Garay 1995; Hossenfelder
2013; Hawking & Penrose 1970; Penrose 2010; Boyle & Turok 2018; Guth 2007) are already in the
paper.

**The single most important insight:** in the paper's own ontology — time as substrate update
steps, proper time emergent — *finite proper time does not bound computational depth*. The
BKL/Mixmaster approach to a generic spacelike singularity packs unboundedly many dynamical epochs
into a finite proper-time interval, and asymptotic silence fragments the domain into causally
isolated shards before termination. The termini are therefore geometrically finite but
computationally and informationally asymptotic — which is precisely the "different kind of
unreachability" the author was reaching for, supplied by mainstream singularity dynamics rather
than by the model.
