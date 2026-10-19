# The single-locus decoding postulate in entanglement-wedge language — what the translation buys, and what it does not

**Status:** research note (2026-08-08). Tracks `AIW-174`, step 1 of the S293 note's "next concrete
steps." Companion to `drafts/aiw174-tsirelson-from-capacity.md` (S293), which is assumed read.
The cosmology paper is published (Zenodo v4, DOI 10.5281/zenodo.21844284); nothing here edits it.

**Verdict in one line:** entanglement-wedge reconstruction does **not** supply the postulate — for a
single Bell pair it remains an independent commitment, now identifiable as *the conjecture that the
DHW/JLMS structure is scale-invariant down to O(1)-capacity loci* (strong ER=EPR plus area metering
at the bit scale) — but the translation is not renaming either: it repairs the postulate's statement
at one point where the informal version self-destructs (per-wing decoding is a local hidden-variable
model and yields CHSH ≤ 2, so "joint" is load-bearing), exposes a vacuity trap (locus = whole
surface makes the capacity bound empty), and localizes exactly which term of established holography
the postulate extends and which theorem is the macro-scale shadow of each of its three components.

Every reference introduced in this note was verified against Crossref this session; resolved
metadata is at the end. References already resolved in the S293 note or the published paper are
reused without re-verification.

---

## 1. The job

S293 reduced the Tsirelson derivation to one premise:

> **Single-locus decoding postulate.** The joint statistics of measurements on an entangled pair are
> the statistics of decodings of one boundary locus, and the information jointly extractable by those
> decodings is bounded by that locus's holographic capacity.

The task here is to state this in entanglement-wedge-reconstruction (EWR) language — the natural
formal home, since EWR is precisely the theory of which boundary region's algebra decodes which
bulk contents — and then to say honestly what the translation buys and what it costs.

## 2. The toolkit, in five statements

The established results the translation can draw on, stated at the resolution actually used below:

1. **Subregion duality (DHW).** For a boundary region R with entanglement wedge W[R] (the bulk
   domain bounded by R and its minimal/extremal surface χ_R), any bulk operator supported in W[R]
   has a representative in the boundary algebra A(R) acting correctly on the code subspace
   (Dong, Harlow & Wall, 2016). Reconstruction is *region-relative*: what is decodable depends on
   which locus you hold.
2. **The capacity of a region is its generalized entropy.** At leading order S(R) = A(χ_R)/4G
   (Ryu & Takayanagi, 2006); with quantum corrections S(R) = A(χ_R)/4G + S_bulk(W[R])
   (Faulkner, Lewkowycz & Maldacena, 2013), extremized as one functional (Engelhardt & Wall, 2015).
   **The area term and the bulk-entropy term are separate lines of the ledger.** This split matters
   below.
3. **Metering (JLMS).** Boundary relative entropy of a region equals bulk relative entropy of its
   wedge (Jafferis, Lewkowycz, Maldacena & Suh, 2016). Information accounting done on the locus and
   accounting done on its decoded interior agree — the macro-scale form of "decodings extract no
   more than the locus carries."
4. **Complementary recovery.** For a boundary bipartition R, R̄, the code reconstructs the wedge of
   R on A(R) and the complementary wedge on A(R̄): one global state, two complementary decodings
   (Harlow, 2017). This is "one locus, two reflections," as an exact code property — for the
   *global* bipartition.
5. **Wedges of unions jump, and correlations have a throat.** The wedge of a union A∪B has a
   disconnected phase (W[A]∪W[B]) and a connected phase, with a transition when the leading-order
   mutual information turns on (Headrick, 2010); leading-order holographic mutual information is
   monogamous (Hayden, Headrick & Maloney, 2013). In the connected phase the correlation between
   the two parts is metered by the entanglement-wedge cross-section E_W = A(σ)/4G — conjecturally
   the entanglement of purification (Umemoto & Takayanagi, 2018) or half the reflected entropy
   (Dutta & Faulkner, 2021) — and E_P ≥ I(A:B)/2 holds for all states (Terhal, Horodecki, Leung &
   DiVincenzo, 2002), so in that phase "I(A:B) ≤ 2 · (throat capacity)" is theorem-shaped.

## 3. Two failure modes that discipline the statement

Writing the postulate in decoding language immediately exposes two readings that must be excluded,
and excluding them is the first real yield of the exercise.

**Failure mode 1: distributive reading — self-destructs to CHSH ≤ 2.** Read "the pair's statistics
are decodings of one locus" distributively — each wing's outcome is separately a decoding of the
locus content λ plus the local setting: P(a|x,λ) and P(b|y,λ) — and keep measurement independence,
which §6.5 explicitly retains. That *is* factorizability with λ = locus content: a local
hidden-variable model located at the locus. Bell's theorem then gives CHSH ≤ 2, contradicting
experiment and the architecture at once. The informal phrase "decodings of one locus" does not by
itself block this reading; the formal statement must. **"Joint" is load-bearing:** the object that
is decoded is the pair's joint statistics, and the postulate must assert that no per-wing
factorization of the decoding exists — §6.5's denial of factorizability, transplanted onto the
boundary. EWR is the right vocabulary for exactly this: reconstruction is region-relative, and the
formalism distinguishes what is decodable from A(ℓ_A) ⊗ A(ℓ_B) from what is decodable only from
A(ℓ_A ∪ ℓ_B) jointly.

**Failure mode 2: global reading — vacuous.** Read "one locus" as the one encoding surface itself
(which the ontology, taken flatly, invites: there is only one surface). Then the claim is trivially
true — everything is a decoding of the whole boundary — and the capacity bound is empty: the
surface's capacity is ~10¹²² bits, and an information-causality inequality with m ~ 10¹²² cuts
nothing. The Pawłowski chain needs the bound with *m* = the capacity actually engaged by the
protocol — the few bits written. So the postulate must be a **localization** claim: the pair, and
each write, has a *minimal* locus, and the area-law capacity calculus remains valid at that locus's
scale — which for a Bell pair and for an m-bit message is O(1) bits, i.e. Planckian area.

Between these failure modes sits the intended content. It is worth recording the trichotomy they
frame, because it says precisely where capacity does its work: per-wing decodings of a classical
register give CHSH ≤ 2 (Bell); unrestricted joint decodings of a classical register give CHSH ≤ 4
(a PR box is a = λ, b = λ ⊕ x·y — no-signalling by masking, but the far setting is freshly written
onto the near readout on every use, an *unmetered* write, which is exactly what the van Dam
protocol exploits); joint but capacity-metered decodings land at 2√2 under α = 1 accounting, via
IC/Uffink. The postulate's decoding structure must therefore be **joint but metered**: non-factorized
enough to escape Bell, accounting-disciplined enough to forbid the masked unbounded channel.

## 4. The postulate, stated in EWR terms

Let Σ be the encoding surface. Let the entangled pair present, in the decompressed interior
description, as systems s_A, s_B measured by the wings with settings x, y and outcomes a, b.

> **Single-locus decoding postulate (EW form).**
>
> **(L1) Localization.** There is a locus ℓ ⊆ Σ — *not necessarily connected as a subset of Σ* —
> whose wedge W[ℓ] is connected and contains the pair, and every joint probability P(a,b|x,y) is the
> expectation of an operator reconstructible from A(ℓ). The capacity of ℓ is area-metered,
> C(ℓ) = A(ℓ)/4ℓ_P² ln 2, and this metering remains valid down to O(1)-bit loci.
>
> **(L2) Jointness.** The reconstruction is irreducibly joint: the statistics do not factor through
> any decomposition A(ℓ_A) ⊗ A(ℓ_B) with per-wing decodings and setting-independent locus content.
> (Equivalently: the pair's locus is "one" in the sense that its wedge is connected — a nonzero
> cross-section — not in the sense of boundary connectedness.)
>
> **(L3) Metering.** Decoding creates nothing: two readings of ℓ jointly extract no more information
> about any external variable X than ℓ carries about X, and an operation on either wing changes what
> ℓ carries about X by at most the capacity of the sub-locus it writes. Information is measured at
> α = 1, inherited from the relative-entropy form of the underlying bound (S293 note, §5).

Granting L1–L3, the S293 argument runs: the IC inequality is L3 stated for the protocol's registers
with L1 supplying the finite m, the Pawłowski–Uffink chain gives CHSH ≤ 2√2, and L2 is what makes
the postulate compatible with the observed violation of the classical bound in the first place.

Three precisions the task asked for, answered explicitly:

- **Single connected boundary region?** No. The locus may be disconnected *on the surface* while
  its wedge is connected *in the bulk* — this is exactly the eternal-black-hole/ER-bridge
  configuration, where two disjoint boundaries hold one connected wedge (Maldacena & Susskind,
  2013). "One locus" means one connected wedge, not one connected patch. This is the correct
  formal residue of "one configuration with no gap to bridge" in §6.5.
- **Wedge of a union?** Yes — the relevant object is W[ℓ_A ∪ ℓ_B] in its *connected* phase.
  The disconnected phase is the regime where the postulate's "one locus" has no leading-order
  geometric referent at all (see §6 below).
- **Complementary recovery?** It is the formal home of a *different* part of §5.2 — "one surface,
  two reflections" for an observer and her complement — not of the pair postulate. Complementary
  recovery concerns the bipartition R, R̄ of the whole boundary and says both sides decode one
  global state. It does not localize the pair, does not meter anything at O(1), and holds for any
  bipartition of any holographic state; it therefore cannot carry the postulate, though it is a
  correct and pleasing formalization of the reflections picture.

## 5. What does real work, and what is decoration

MG's standing objection — formalism that adds notation without adding constraint — applied honestly:

**Doing real work:**

1. **The jointness repair (L2).** The wedge formalism is the only vocabulary on the table in which
   "decodable from the parts" vs "decodable only from the whole" is a precise, region-indexed
   distinction. Without it, the postulate as informally stated in §6.5 and S293 admits the
   distributive reading, which is not a weaker version of the claim but a *refutation-shaped* one
   (CHSH ≤ 2). Catching this is a material correction to how the postulate must be written anywhere
   it appears again.
2. **The vacuity exposure (L1).** "One locus" must be minimal-locus, or the capacity bound cuts
   nothing. The informal statement does not force this; the EW statement does, because a wedge and
   its capacity are defined region by region.
3. **The ledger split (§6 below).** Only in the QES/FLM language can one even ask "which term of the
   entropy functional does the pair's correlation sit in?" — and the answer is where the postulate's
   real cost shows up.

**Decoration:**

4. The algebraic dress itself — "A(ℓ)," code subspaces, operator reconstruction — adds no
   constraint beyond what "decoding of a register" already said, *and cannot*, for the circularity
   reason in §7: any Hilbert-space formalization already contains Tsirelson's theorem, so no
   intra-quantum machinery can non-trivially deliver the bound. The EWR vocabulary earns its keep
   on points 1–3; as a derivation engine for the ceiling it is inert by construction.

## 6. Does the capacity accounting survive the translation?

This is where the translation is least kind to the postulate, and the finding should be stated
without cushioning.

**(a) The pair sits in the wrong term of the ledger.** In established holography the capacity of a
locus is the *area* term. A single Bell pair distributed into the bulk contributes its ebit to
**S_bulk** — the quantum-correction term of the FLM/QES formula — and is invisible in the area term
at leading order. Standard AdS/CFT therefore does *not* say "the pair's correlations are bounded by
an area"; it says they are bounded by quantum mechanics (Tsirelson's theorem), with the area
metering only the O(1/G) geometric entanglement. The postulate needs the pair's correlation budget
on the *capacity* side of the ledger. Within the paper's ontology this is at least coherent — the
single-surface ontology denies independent interiors, so a fundamentally independent S_bulk term is
exactly what it rejects; the FLM split must be an artifact of the decompressed description. But
coherent is not established: no result in the EWR line converts bulk-matter entanglement into
surface capacity. This is the precise, term-level location of what the postulate adds.

**(b) The disconnected phase is the generic phase for the object of interest.** For a microscopic
pair held by two distant parties, the joint wedge of any natural pair of loci is in its
disconnected phase: leading-order mutual information is zero (Headrick, 2010), and the "one locus"
has *no leading-order geometric referent* — the geometry shows two separate wedges. The connected
phase, where "one locus" is literal (a wedge with a throat, capacity E_W, and the theorem-shaped
bound I ≤ 2E_W), requires O(1/G) entanglement: black-hole pairs, thermofield doubles. The
postulate therefore asserts that the connected-wedge structure *persists* below the transition —
which is verbatim the strong form of ER=EPR: a Planck-scale, "highly quantum" bridge for every
entangled pair, explicitly conjectural in Maldacena & Susskind (2013). The paper already endorses
ER=EPR (§5.2, §6.5), so this costs the paper no new commitment — but it must be flagged that the
postulate leans on the *strong* form, not the established TFD case. The entanglement-wedge phase
transition itself does not break the accounting; it marks the boundary of where the accounting is
established.

**(c) The conditional-mutual-information sum: nothing breaks, and nothing is gained.** IC's
left-hand side, Σ_k I(a_k : b | K=k), conditions on a classical register and sums over its values.
The proof of IC from the entropic axioms (chain rule, data processing) goes through for von Neumann
quantities and restricts to Shannon on the protocol's classical registers — the α = 1 inheritance
of the S293 note, unchanged. The geometric side contributes nothing here: the burden is carried
entirely by the entropic axioms, i.e. by L3, not by any property of wedges. No obstruction; no
assistance. Consistent with S293 §5, the measure question stays settled upstream.

**(d) The one theorem-shaped consolation.** In the regime where geometry exists (connected phase),
"jointly carried correlation ≤ 2 × throat capacity" *is* established: I(A:B) ≤ 2E_P (Terhal et al.,
2002) with E_P conjecturally geometrized as E_W (Umemoto & Takayanagi, 2018; Dutta & Faulkner,
2021). So the postulate's capacity claim is *true where it can currently be checked*. But every
link in that chain is proven inside quantum mechanics, so it is consistency support only — see §7.

## 7. The circularity boundary — where the derivation must live

A point that the translation makes unavoidable. Tsirelson's bound is a theorem of quantum
mechanics. EWR — wedges, codes, JLMS, cross-sections — is a body of theorems *about quantum
systems*. Inside any Hilbert-space formalization, CHSH ≤ 2√2 holds automatically and the capacity
premise does no work; a "derivation" of Tsirelson from intra-quantum EWR machinery would be
circular. The derivation's entire value is device-independent: it must run over the space of
no-signalling theories, where super-quantum boxes exist to be excluded.

The consequence for the postulate's formalization is structural, and it is the note's second main
finding: **the EW form of §4 is the postulate's consistency home, not its derivation home.** The
derivation home is the device-independent skeleton — registers, decodings, metered writes, α = 1
accounting (L1–L3 stripped of the algebraic dress) — which is essentially the IC premise, held as
physics rather than as an axiom about boxes. What EWR contributes is the demonstration that this
skeleton is not ad hoc: at macro scale, quantum gravity provably instantiates each component —
L1 ↔ DHW subregion duality, L2 ↔ connected-wedge/cross-section structure, L3 ↔ JLMS. The
postulate is then exactly the statement that this instantiation is scale-invariant down to
O(1)-capacity loci. Notably, scale invariance of boundary structure is already Step 2 of the
paper's own §5.2 argument — so within the paper's axiom set the postulate is not a new kind of
assumption, it is the existing scale-invariance proposition applied to the DHW/JLMS structure.
Externally, it is an open conjecture of quantum gravity (strong ER=EPR plus bit-scale area
metering), and nothing in this note changes that.

## 8. What the postulate now costs

| Question | Answer after translation |
|---|---|
| Does EWR supply the postulate? | **No.** Not under complementary recovery, not under a connectedness condition — at pair scale the connectedness condition *is* the conjecture. |
| Is the postulate entailed by any established result? | No. Its macro-scale analogue is established (DHW + JLMS + connected-wedge structure); the O(1) extension is strong ER=EPR territory. |
| Is it more or less plausible than before? | Internally: same commitments, better organized — it is §5.2's Step-2 scale invariance applied to a structure quantum gravity provably has at macro scale, and its capacity claim holds where checkable (§6d). Externally: unchanged — an independent conjecture. |
| Did the translation only rename? | No, but narrowly. Three real yields: the jointness repair (without which the postulate reads as a CHSH ≤ 2 model), the minimality requirement (without which the bound is vacuous), and the ledger-split localization of the gap (area term vs S_bulk). The algebraic machinery beyond that is decoration, and provably must be (§7). |
| Status of §6.5's conditional derivation | **Unchanged.** Conditional, condition named, not met unconditionally, not a no-go. This note sharpens the condition's statement; it does not discharge it. |

**Net assessment.** The S293 note said the remaining gap is "state which boundary subregion's
algebra the pair's joint statistics are a decoding of." That is now done (§4), and doing it showed
the gap is deeper than a statement problem: the postulate is a scale-invariance conjecture about
the DHW/JLMS structure, its derivation must live device-independently to avoid circularity, and
its two honest supports are (i) the paper's own scale-invariance axiom and (ii) the fact that
every component of it is a theorem at macro scale. If §6.5 is ever revised (post-publication, in a
successor paper or formalization document), the phrase "a question for entanglement-wedge
reconstruction" should become "the conjecture that entanglement-wedge reconstruction's
subregion-duality and metering structure is scale-invariant down to single-pair loci" — a sharper
and more falsifiable-sounding IOU, and an honest one.

## 9. Concrete residue for AIW-174

1. Any future statement of the postulate must carry L2 explicitly. The distributive reading is not
   a nuance; it is a different theory with CHSH ≤ 2.
2. The Jain–Gachechiladze–Miklin step (S293 next-step 2) is unaffected by this note and remains
   worth running: it operates at the device-independent level, which §7 identifies as the right
   arena anyway.
3. The monogamy step (S293 next-step 3) acquires a precise target from this note: HHM monogamy
   (Hayden, Headrick & Maloney, 2013) is a *leading-order geometric* fact — same regime limitation
   as everything else here — so "finite capacity is the structural source of monogamy" faces the
   same O(1)-extension gap, at the same joint. That convergence (Tsirelson gap, monogamy gap, and
   the S293 communication-complexity dead end all failing at the area-to-single-locus link) is
   itself diagnostic and worth one sentence in any successor document.

---

## References resolved this session

All verified against Crossref by DOI on 2026-08-08.

| Cited as | Verified record |
|---|---|
| Dong, Harlow & Wall (2016) | "Reconstruction of Bulk Operators within the Entanglement Wedge in Gauge-Gravity Duality," *Phys. Rev. Lett.* 117, 021601. DOI 10.1103/PhysRevLett.117.021601 |
| Ryu & Takayanagi (2006) | "Holographic Derivation of Entanglement Entropy from the anti–de Sitter Space/Conformal Field Theory Correspondence," *Phys. Rev. Lett.* 96, 181602. DOI 10.1103/PhysRevLett.96.181602 |
| Faulkner, Lewkowycz & Maldacena (2013) | "Quantum corrections to holographic entanglement entropy," *JHEP* 2013(11), 74. DOI 10.1007/JHEP11(2013)074 |
| Engelhardt & Wall (2015) | "Quantum extremal surfaces: holographic entanglement entropy beyond the classical regime," *JHEP* 2015(1), 73. DOI 10.1007/JHEP01(2015)073 |
| Jafferis, Lewkowycz, Maldacena & Suh (2016) | "Relative entropy equals bulk relative entropy," *JHEP* 2016(6), 4. DOI 10.1007/JHEP06(2016)004 |
| Harlow (2017) | "The Ryu–Takayanagi Formula from Quantum Error Correction," *Commun. Math. Phys.* 354, 865–912. DOI 10.1007/s00220-017-2904-z |
| Almheiri, Dong & Harlow (2015) | "Bulk locality and quantum error correction in AdS/CFT," *JHEP* 2015(4), 163. DOI 10.1007/JHEP04(2015)163 |
| Pastawski, Yoshida, Harlow & Preskill (2015) | "Holographic quantum error-correcting codes: toy models for the bulk/boundary correspondence," *JHEP* 2015(6), 149. DOI 10.1007/JHEP06(2015)149 |
| Headrick (2010) | "Entanglement Rényi entropies in holographic theories," *Phys. Rev. D* 82, 126010. DOI 10.1103/PhysRevD.82.126010 |
| Hayden, Headrick & Maloney (2013) | "Holographic mutual information is monogamous," *Phys. Rev. D* 87, 046003. DOI 10.1103/PhysRevD.87.046003 |
| Umemoto & Takayanagi (2018) | "Entanglement of purification through holographic duality," *Nature Physics* 14, 573–577. DOI 10.1038/s41567-018-0075-2 — note author order: Umemoto first |
| Dutta & Faulkner (2021) | "A canonical purification for the entanglement wedge cross-section," *JHEP* 2021(3), 178. DOI 10.1007/JHEP03(2021)178 |
| Terhal, Horodecki, Leung & DiVincenzo (2002) | "The entanglement of purification," *J. Math. Phys.* 43, 4286–4298. DOI 10.1063/1.1498001 |
| Maldacena & Susskind (2013) | "Cool horizons for entangled black holes," *Fortschr. Phys.* 61, 781–811. DOI 10.1002/prop.201300020 |

Reused from prior resolution (S293 note / published paper reference list, not re-verified):
Pawłowski et al. (2009); Popescu & Rohrlich (1994); Cirel'son (1980); van Dam (2012); Casini
(2008); Longo (2024); Kudler-Flam et al. (2025) — **PRD 111, 105001**, per the S293 note's explicit
warning not to confuse it with PRD 111, 025013; Oughton & Timpson (2024); Jain, Gachechiladze &
Miklin (2024); Jain, Miklin & Gachechiladze (2026); Navascués, Guryanova, Hoban & Acín (2015).
