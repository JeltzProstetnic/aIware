# Tsirelson's bound from holographic capacity — the derivation, its one premise, and what it still owes

**Status:** research note, S293 (2026-08-07). Tracks `AIW-174`. Not yet a paper section.
**Verdict in one line:** the derivation goes through, but *conditionally* — it reduces to a single
premise, and that premise turns out to be the single-surface ontology the paper already asserts on
independent grounds in §5.2. That is a materially stronger position than §6.5's current "candidate
direction," and materially weaker than the unconditional result `AIW-174` set as its success criterion.

Every reference below was verified against Crossref or the arXiv API this session; the resolved
metadata is recorded at the end.

---

## 1. What §6.5 owes

§6.5 rejects factorizability rather than measurement independence, which dissolves the Bell constraint
— and dissolves it too well. No-signalling alone permits correlations up to the Popescu–Rohrlich value
S = 4 (Popescu & Rohrlich, 1994), while nature stops at Tsirelson's S = 2√2 (Cirel'son, 1980). Emitting
2√2 is not an achievement; any number of mechanisms can be tuned to emit it. The obligation is to
*derive the ceiling*.

## 2. The existing chain, and where the architecture could enter

The one route that recovers exactly 2√2 from a physical principle runs:

> **information causality (IC)** ⟹ Uffink inequality ⟹ CHSH ≤ 2√2

IC (Pawłowski et al., 2009) says that if Alice sends Bob *m* classical bits, the total information Bob
can obtain about Alice's database is at most *m*:

  Σ_k I(a_k : b | K = k) ≤ m

Jain, Gachechiladze and Miklin (2024) turned IC from a principle that was hard to apply into a working
tool, giving a technique that generates polynomial inequalities bounding the quantum set in any
bipartite Bell scenario, and recovering part of the quantum boundary beyond Uffink; they extend it in
Jain, Miklin and Gachechiladze (2026).

The architecture's proposed entry point is the left end: **derive IC from bounded boundary capacity.**

## 3. The first thing to get right: this is an identification, not a derivation

Trying to *derive* IC from a capacity bound is the wrong shape, and seeing why is most of the work.

Write the IC inequality beside the holographic bound on a boundary region of area A:

| | bound | bounded quantity |
|---|---|---|
| IC | Σ_k I(a_k : b \| K=k) ≤ m | information Bob obtains about Alice's database |
| Holographic | I ≤ A / (4 ℓ_P² ln 2) | information accessible on the boundary region |

Under §6.5's own reading, an entangled pair is **one locus** on the boundary, and the two interior
"systems" are two decodings of it. Bob's wing is not a second system receiving influence; it is a second
reading of the same surface. So the information Bob can obtain about Alice's setting and database is,
by construction, information read off *that locus* — and the holographic bound caps exactly that.

The two rows are then not analogous inequalities. **They are the same inequality**, once *m* is read as
the capacity of the shared locus rather than as a count of transmitted bits. IC is not a consequence of
the capacity bound; IC is what the capacity bound *says* when stated in the interior's vocabulary.

This is worth being precise about because it changes what is owed. Nothing has to be proven about
implication between two principles. What has to be justified is a single identification.

## 4. The premise the derivation reduces to

Stated sharply:

> **Single-locus decoding postulate.** The joint statistics of measurements on an entangled pair are the
> statistics of decodings of one boundary locus, and the information jointly extractable by those
> decodings is bounded by that locus's holographic capacity.

Granting it, the IC inequality holds with *m* = capacity, the Pawłowski chain runs unmodified, and
CHSH ≤ 2√2 follows. Denying it, nothing follows.

The postulate is not an extra assumption bolted on for this purpose. It is §5.2's single-surface
ontology — "there are no interiors-with-contents at all" — applied to the entangled pair, which is
precisely the application §6.5 already makes when it rejects factorizability. **The paper already
holds this premise, for reasons that have nothing to do with Tsirelson's bound.** That is what makes
the reduction interesting rather than circular: an ontological commitment adopted to unify singularities
turns out to carry a quantitative constraint on correlation strength.

What it is not: a theorem. The postulate asserts that the accessible information of the *pair* is
governed by the capacity of *one* region. In AdS/CFT that kind of claim is the business of
entanglement-wedge reconstruction (Dong, Harlow & Wall, 2016) and the holographic error-correction
picture §6.5 already names (Almheiri, Dong & Harlow, 2015; Pastawski et al., 2015) — which is where the
formalization has to come from, exactly as §6.5 anticipates for the James–Stein lens.

## 5. Answering Oughton and Timpson — the measure is inherited, not chosen

The sharpest live objection to the IC route is Oughton and Timpson (2024): IC's recovery of Tsirelson
depends on the information measure being **Shannon**. Reformulate IC with Rényi entropies and the
derivation fails. If the principle only works for one arbitrary choice of measure, its claim to be a
*physical* principle is weak.

The architecture has a non-arbitrary answer, and it is the reason the §5.2 repair matters here.

**The bound is not postulated at the information-theoretic level with a free choice of measure. It
descends from a physical inequality that already fixes one.** The rigorous forms of the Bekenstein
bound are statements about *Umegaki* (α = 1) relative entropy, and about nothing else:

- Casini (2008) identifies the Bekenstein bound with positivity of the vacuum relative entropy,
  ΔK − ΔS ≥ 0, in quantum field theory.
- Longo (2024) proves model-independently that the vacuum relative entropy of a state localized in a
  region of width 2R is bounded by 2πR times its energy — the Bekenstein inequality itself, as a
  relative-entropy statement.
- Kudler-Flam, Leutheusser, Rahman, Satishchandran and Speranza (2025) prove the bound with a covariant
  entanglement-entropy regulator, again in relative-entropy form.

Now close the loop. Quantum mutual information *is* a relative entropy, I(A:B) = S(ρ_AB ‖ ρ_A ⊗ ρ_B),
and on states diagonal in a common basis the von Neumann relative entropy reduces exactly to the
classical Kullback–Leibler divergence. The registers in the IC protocol — Alice's database bits a_k,
Bob's guess b — are classical. **So the α = 1 relative-entropy bound the physics supplies, restricted
to the protocol's classical registers, is Shannon mutual information.** Not by stipulation: by
restriction.

Oughton and Timpson ask why Shannon rather than Rényi-2. On this account the answer is that the choice
is made upstream, by which inequality the Bekenstein bound actually is, and it is the α = 1 one.

**The honest limit of this reply.** Sandwiched Rényi divergences exist, satisfy data processing, and
have modular-theory analogues; the claim here is not that no Rényi statement can be written. It is that
the specific inequality carrying the 2πRE content — the one Axiom 4 asserts — is the α = 1 case, and no
Rényi-α analogue is known to deliver it. Should such an analogue be found, this reply weakens
accordingly, and the objection returns.

## 6. A second route, and why it lands short — recorded so it is not re-attempted

The obvious alternative avoids IC entirely and is worth writing down mainly to record that it does
*not* work as cleanly as it first appears.

Van Dam (2012) showed PR boxes make communication complexity trivial; Brassard et al. (2006) showed
triviality already follows above CHSH ≈ 3.266. If the architecture forbade communication-complexity
triviality, it would get S ≤ 3.266 — weaker than Tsirelson, but unconditional.

It does not get there. Triviality protocols consume a number of nonlocal boxes growing exponentially in
input size, so a finite-capacity locus fails to supply them — but that is a statement about *how many*
boxes a given area supports, not about *how strong* one box may be. The capacity bound constrains the
density of independent nonlocal resources per unit area; it does not by itself constrain the CHSH value
of a single locus. Getting from one to the other needs the same single-locus postulate of §4.

So the two routes do not provide independent support. **They fail at the same joint**, which is at least
diagnostic: the missing ingredient is not the choice of principle but the link from an area bound to a
per-locus correlation bound.

## 7. Verdict

| Claim | Status |
|---|---|
| Tsirelson from capacity **alone** | **Not achieved.** `AIW-174`'s success criterion is not met. |
| Tsirelson from capacity **+ single-locus decoding** | **Achieved**, via Pawłowski/Uffink, with no new machinery. |
| That premise is independently held by the paper | **Yes** — it is §5.2's single-surface ontology. |
| Oughton–Timpson Shannon-dependence objection | **Answered**, conditional on §5's honest limit. |
| A no-go result instead | **No.** Nothing here shows the derivation *cannot* close. |

Two things this still would not buy, even completed. Information causality does not single out the
quantum set: certain supra-quantum "almost quantum" correlations satisfy its known consequences
(Navascués, Guryanova, Hoban & Acín, 2015). And a conditional derivation from an ontological postulate
is a consistency result about the architecture, not a reconstruction of quantum theory.

**What it is worth publishing as:** not "we derived Tsirelson," but a short, precise claim — *the
holographic single-surface ontology entails information causality, and hence Tsirelson's bound, given
one clearly stated decoding postulate; and it answers the standing measure-dependence objection to
information causality by fixing the measure from the underlying relative-entropy bound.* The second
half may be the more novel contribution: it is a reply to Oughton and Timpson that is not available to
anyone who takes IC as a primitive principle.

## 8. Next concrete steps

1. **Formalize the postulate** in the entanglement-wedge language (Dong, Harlow & Wall, 2016) — state
   which boundary subregion's algebra the pair's joint statistics are a decoding of. This is the whole
   remaining gap.
2. **Run the Jain–Gachechiladze–Miklin machinery** with *m* = capacity to see whether the capacity
   reading yields any inequality *tighter* than Uffink, using their extended principle (2026). If it
   does, that would be a result independent of the reduction above.
3. **Check the monogamy step.** §6.5 asserts finite capacity is "the structural source of entanglement
   monogamy." That is stated, not shown, and it is the natural bridge from area to per-locus strength.
4. Only then revise §6.5. Proposed replacement text for its final paragraph is drafted in §9 below,
   held for MG's approval rather than landed.

## 9. Proposed §6.5 revision — NOT applied, for review

> **⚠ SUPERSEDED IN PART, S297 2026-08-08 (`AIW-184`, MG-approved).** The draft below states the
> single-locus step in the informal wording that **does not block the distributive reading** — each
> wing separately decoding the locus content, with measurement independence retained. Read that way
> the postulate **is a local hidden-variable model and yields CHSH ≤ 2**, i.e. it is refutation-shaped
> rather than merely weaker. The wording shipped into `paper/cosmology/sb-hc4a.md` §6.5 therefore
> carries two explicit clauses this draft lacks, taken from
> `drafts/aiw174-entanglement-wedge-postulate.md` §4 (L1/L2/L3):
>
> - **Jointness** — the reconstruction is irreducibly joint; the statistics do not factor through any
>   decomposition into per-wing decodings with setting-independent locus content. This is what makes
>   the postulate *compatible with the observed violation* in the first place, not an added
>   strengthening. And "one locus" means one **connected wedge**, not one connected boundary patch —
>   the locus may be disconnected on the surface while its wedge is connected in the bulk (the
>   eternal-black-hole configuration, Maldacena & Susskind, 2013).
> - **Minimality** — the locus must be the minimal one meeting that condition. Read as licensing the
>   whole encoding surface the capacity bound constrains nothing: ~10¹²² bits cuts no correlation set,
>   and the argument would run for supra-quantum correlations as readily as for quantum ones.
>
> Keep the draft below as the record of what was proposed; do not reuse its wording.

Replacing the final two sentences of "**What is actually owed: Tsirelson's bound.**":

> The ceiling is closer to hand than it first appears. The
> holographic bound makes boundary information finite per unit area, and under the single-surface
> ontology of Section 5.2 an entangled pair is one boundary locus rather than two systems. Those two
> commitments together state that the information jointly extractable by the two wings is bounded by
> that locus's capacity — which is the information-causality inequality (Pawłowski et al., 2009), with
> the capacity in place of a transmitted-bit count. Information causality yields Tsirelson's bound
> through the Uffink inequality, and recent work makes it an efficient tool for bounding the quantum
> set generally (Jain, Gachechiladze, & Miklin, 2024). The ceiling therefore follows from commitments
> the paper already makes, given one further step: that the pair's joint statistics are decodings of a
> single boundary locus whose accessible information is capacity-bounded. That step is asserted here,
> not proven; making it a theorem is a question for entanglement-wedge reconstruction (Dong, Harlow, &
> Wall, 2016) — the same direction the formalization of the preceding lens points.
>
> Oughton
> and Timpson (2024) show that information causality recovers Tsirelson's bound only when the
> information measure is Shannon, and fails under Rényi-2 — which makes the principle look like it
> depends on an arbitrary choice. Here the choice is not made at the level of the principle. The
> rigorous forms of the Bekenstein bound are statements about relative entropy at α = 1 (Casini, 2008;
> Longo, 2024; Kudler-Flam et al., 2025), quantum mutual information is itself a relative entropy, and
> on the classical registers of the protocol the von Neumann quantity reduces to the Shannon one. The
> measure is inherited from the physical bound rather than selected for convenience. Were a Rényi-α
> analogue of the 2πER inequality established, this reply would weaken accordingly.

---

## References resolved this session

| Cited as | Verified record |
|---|---|
| Popescu & Rohrlich (1994) | *Foundations of Physics* 24, 379–385. DOI 10.1007/BF02058098 |
| Pawłowski et al. (2009) | *Nature* 461, 1101–1104 |
| Brassard et al. (2006) | *Phys. Rev. Lett.* 96, 250401. DOI 10.1103/PhysRevLett.96.250401 |
| van Dam (2012) | *Natural Computing* 12, 9–12. DOI 10.1007/s11047-012-9353-6 |
| Casini (2008) | *Class. Quantum Grav.* 25, 205021. DOI 10.1088/0264-9381/25/20/205021 |
| Oughton & Timpson (2024) | *Entropy* 26(7), 562. DOI 10.3390/e26070562 |
| Jain, Gachechiladze & Miklin (2024) | *Phys. Rev. Lett.* 133, 160201 (arXiv:2308.02478) |
| Jain, Miklin & Gachechiladze (2026) | arXiv:2606.02416, "Bounds on Nonlocality and Random Access Codes from Extended Information Causality Principle" |
| Longo (2024) | arXiv:2409.14408, "A Bekenstein-type bound in QFT" |
| Kudler-Flam, Leutheusser, Rahman, Satishchandran & Speranza (2025) | *Phys. Rev. D* 111, 105001 — "Covariant regulator for entanglement entropy: Proofs of the Bekenstein bound and the quantum null energy condition" |

⚠ The handover's citation of Kudler-Flam et al. as PRD 111, 105001 is **correct** — confirmed by DOI.
Note that a *different* Kudler-Flam paper, "Generalized black hole entropy is von Neumann entropy"
(PRD 111, 025013), is easy to confuse with it; the 105001 paper is the one that proves the Bekenstein
bound, and is the one wanted here.
