# Cosmology (SB-HC4A) — adversarial check of the S313 repairs

Checked 2026-08-27 against the live working tree of `/home/jeltz/aIware/paper/cosmology/sb-hc4a.md`
(file is under active edit by another process — line numbers below are approximate and drifted
during the check; every finding is anchored to quoted text, not line numbers). Baseline for
"what changed" = git diff `ccc5ff99..HEAD` (the repairs landed in `4f75b54d` + `de6d43f3`;
52 insertions / 40 deletions). Primaries verified via web: Bahiru arXiv:2301.08753 abstract,
Mazur 1982 (IOPscience), Bunting 1983 thesis (literature citations), Bak 1996 / G-R law (SOC
literature), G&R 1956 Annali di Geofisica entry.

---

## Repair 1 — Bahiru et al. (2024): CORRECT, but INCOMPLETE

**What I checked:** the rewritten "IB1 is a two-tier property" passage (§5.2), the following
paragraph ("both relocate the information to the boundary"), every occurrence of
Bahiru/Raju/"holography of information" in the file (4 sites), the reference entry, and the
primary's abstract via WebFetch.

**The rewrite is correct and matches the primary.** Current text: "…on the holography-of-information
results there is no bulk information that is not already available at the boundary (Raju, 2022) — a
claim contested in perturbation theory by Bahiru et al. (2024), who construct approximately local
bulk observables invisible to boundary correlators; the architecture requires only the
non-perturbative statement." The arXiv abstract confirms the thesis ("possible to localize
information in perturbative quantum gravity"; observables commuting with boundary charges to all
orders in 1/N). Reference entry (JHEP 2024(5), 261, five authors) matches. The follow-on sentence
"Neither the island results nor the holography of information supplies that: both relocate the
information to the boundary" now refers to islands + Raju (not Bahiru) and sits under the two-tier
caveat — defensible. §8.2 correctly carries the tier language ("This is the non-perturbative tier
of IB1 (Section 5.2)").

**INCOMPLETE — one passage still leans on the unqualified strong claim.** §6.5, "One locus, two
reflections" (byte-identical to the pre-repair version): "The same conclusion follows from the
holography-of-information results discussed in Section 8.2 (Raju, 2022): boundary data are not
localized in the interior sense at all." That is precisely the perturbative-strength claim Bahiru
et al. contest (approximately local bulk observables exist), stated flatly and used as convergent
support, with no propagation of the "requires only the non-perturbative statement" caveat. It cites
Raju (who does claim it), so it is not a citation reversal — but the repair's own concession makes
"not localized … at all" over-strong as written. This paragraph is also the unapplied ruling-4 site
(see below), so one edit would fix both.

## Repair 2 — Kerr-Newman uniqueness: CORRECT and COMPLETE

**What I checked:** the full attribution sentence, every occurrence of
Carter/Robinson/Israel/Mazur/Bunting/Hawking-1972 in the file, all six reference entries, and
independent web confirmation of Mazur 1982 and Bunting 1983.

Current text: "Israel (1967, 1968) proved uniqueness for the *static* (J = 0) vacuum and electrovac
cases; the rotating vacuum case rests on the uniqueness results of Carter (1971) and Robinson (1975)
together with Hawking's (1972) rigidity theorem, and the rotating, charged case on their extension
by Mazur (1982) and Bunting (1983)."

- Every attribution is correct (Israel static vacuum 1967 / electrovac 1968; Carter+Robinson+Hawking
  rigidity = vacuum rotating; Mazur/Bunting = charged rotating). "Their extension" is apt — Mazur's
  proof proceeds via a generalized Robinson-type identity (confirmed from the IOP abstract).
- Carter (1971)/Robinson (1975) appear nowhere else in the body; no passage still credits them with
  the charged case. The Abstract's Carter (1968) g = 2 use is the different, correct paper.
- Reference entries all confirmed: Mazur, J. Phys. A 15(10), 3173–3180, 1982 (IOPscience:
  10.1088/0305-4470/15/10/021) ✓; Bunting, *Proof of the uniqueness conjecture for black holes*,
  PhD thesis, University of New England, Armidale, 1983 ✓ (standard citation across the uniqueness
  literature); Israel 1967 Phys. Rev. 164, 1776 ✓; Israel 1968 Commun. Math. Phys. 8, 245 ✓;
  Carter 1971 PRL 26(6), 331–333 ✓; Robinson 1975 PRL 34(14), 905–906 ✓; Hawking 1972
  Commun. Math. Phys. 25(2), 152–166 ✓ (entry present — the rigidity theorem needed a reference and
  has one).

## Repair 3 — James-Stein (§6.5): CORRECT; argument survives; one pre-existing wart

**What I checked:** both repaired sentences, a whole-file grep for "shared distribution", "drawn
from", "shared origin", "‖θ‖", the surrounding three paragraphs, and the section's closing
"What this section claims" summary.

- **Theorem statement fixed:** "for d ≥ 3 parameters estimated under joint quadratic loss,
  estimating them independently is *inadmissible*: it is dominated by a joint 'shrinkage' estimator
  — and dominated for every value of the parameters, whether or not they share an origin. What a
  shared origin adds is not the dominance but its magnitude." No shared-distribution hypothesis
  survives anywhere in the file. The added magnitude sentence is statistically right (risk gain
  depends on proximity of θ to the shrinkage target).
- **Coefficient fixed:** "The shrinkage coefficient w = (d−2)σ²/‖x‖²" — function of the data. No
  ‖θ‖² survives anywhere.
- **The surrounding argument still works — and is in fact cleaner.** The old text needed dominance
  to signal common origin (which the review showed universal dominance destroys). The repaired text
  no longer asks that of the theorem: the direction of argument is ontology → reinterpretation
  ("Under the single-surface ontology … Read this way, the theorem says …"), and the section's own
  summary downgrades the whole thing to "a heuristic lens … illuminating, quantitatively
  uninterpreted", with formalization deferred to holographic QEC. Nothing concluded from
  James-Stein now exceeds what the corrected premise licenses.
- **Residual technical inaccuracy (pre-existing, not introduced by the repair):** "…and the
  entangled — jointly shrunk — description is the admissible one." The James-Stein estimator is
  itself inadmissible (dominated by positive-part JS). The theorem yields "dominating", not
  "admissible". Same wording existed in the baseline; the repair did not touch it. Low stakes for
  the lens, but it is the kind of thing the same reviewers would flag next round.

## Repair 4 — Bell factorizability: CORRECT and COMPLETE

**What I checked:** the factorizability statement, every `P(` occurrence in the file, and the
symbol usage in the rest of §6.5 (information-causality paragraph, empirical-anchor paragraph).

Current text: "*factorizability* (P(A,B|x,y,λ) = P(A|x,λ) P(B|y,λ): given the settings x, y and the
common cause λ, the outcomes at the two wings are statistically independent)". Settings included;
the inline gloss fixes the roles of every symbol. This is the only factorizability formula in the
file. No lowercase a, b are used as outcomes anywhere; the a_k, b in the information-causality
inequality (Σ_k I(a_k : b | K = k) ≤ m) are that literature's own notation, introduced with their
roles stated ("a sender's database", "a receiver") — no CHSH-settings collision.

## Repair 5 — Gutenberg-Richter / SOC: CORRECT; one dating nuance to note

**What I checked:** the §9.2 sentence, the reference entry, web confirmation of the entry and of
Bak 1996's treatment of the G-R law.

Current text: "earthquakes (the Gutenberg-Richter law, 1956, read as an SOC signature by Bak,
1996)". The anachronism is gone. **Bak 1996 does read the G-R law as an SOC signature** — *How
Nature Works* presents the earthquake magnitude-frequency power law as headline evidence for SOC
(this is also Bak & Tang 1989's thesis); confirmed via the SOC literature. Reference entry
"Gutenberg, B., & Richter, C. F. (1956). Magnitude and energy of earthquakes. *Annali di
Geofisica*, 9, 1–15." is bibliographically correct (confirmed against the Annals of Geophysics
archive copy).

**Nuance, not an error:** the frequency-magnitude law itself canonically dates to Gutenberg &
Richter 1944 (BSSA 34, 185); the 1956 Annali paper is the magnitude-energy relation. Citing the
1956 paper for "the Gutenberg-Richter law" follows a widespread convention in the SOC/statistical-
physics literature, so this is defensible as-is — but a seismologist referee could quibble.

---

## SHOULD-FIX set — applied / not applied (current wording, primaries not re-verified)

| Item | Status | Current wording |
|---|---|---|
| **Wetterich 2022c** (old :346/:692) | **NOT APPLIED** | §10.3 still reads "This is a cellular automaton model of quantum gravity — not a metaphor." verbatim; §5.6 and §10.3 still state "emergent diffeomorphism symmetry in the continuum limit" without the primary's naive-vs-true-limit condition. Only the "Most remarkably" register fix landed. |
| Arcos & Pereira 2004 (old :354) | APPLIED | "argued that the extreme Kerr-Newman solution can be consistently interpreted as a model of the electron, with mass, charge, and spin — including half-integral angular momentum — arising from the spacetime geometry." |
| Ruggiero 2020 (old :294) | APPLIED | "Consistent with reading the Big Rip as a cyclic transition, Ruggiero (2020, unpublished preprint) notes that Hawking-radiation temperature diverges … and proposes on that basis …" |
| Poplawski 2010 (old :358/:368) | **PARTIAL** | :358 site fixed well ("Poplawski (2010) showed it prevents the cosmological singularity … Extending that mechanism to the Kerr-Newman ring singularity is a step Poplawski does not take and is conjectured here"). But the later "Torsion and the nature of the boundary" paragraph is unchanged and still cites Poplawski for preventing "classical point singularities" generally — broader than the cosmological result the primary contains. |
| **Salmon et al. 2024** (old :439) | **NOT APPLIED** | Gloss unchanged: "James-Stein advantages in entangled Gaussian sensing (Salmon, Strelchuk, & Arvidsson-Shukur, 2024)" — the review found the primary shows entanglement *diminishes* the JS advantage noiselessly and noise restores it. |
| Hengen et al. 2016 (old :490) | APPLIED | Split correctly: "homeostatic set-point regulation: Hengen et al., 2016; tuning to criticality: Ma et al., 2019". Ma et al. reference entry (Neuron 104(4), 655–664, 2019) is correct. |
| Van Raamsdonk (convergence item) | APPLIED | "The holographic architecture is consistent with Van Raamsdonk's (2010) argument …" ("strong support"/"demonstration" gone). |

## Ruling 4 — the five convergence-as-support sites

| Site | Status | Detail |
|---|---|---|
| old :216 (§5.2) | **HALF-APPLIED** | ER=EPR now "is consistent with this unification" ✓ — but the very next sentence keeps "The Complexity=Action conjecture (Brown et al., 2016) **further strengthens** the computational interpretation", which the review flagged in the same breath. |
| old :294 (Ruggiero) | APPLIED | see above |
| old :360 (spin/LQG) | APPLIED | "This interpretation **is consistent with** loop quantum gravity, where Rovelli and Smolin (1995) derived …" (was "receives support from") |
| old :415 (Van Raamsdonk) | APPLIED | see above |
| old :427 (§6.5 "One locus, two reflections") | **NOT APPLIED** | Paragraph is byte-identical to the pre-repair baseline: ER=EPR "asserts exactly this", Van Raamsdonk "supplies the complementary half", "The same conclusion follows from the holography-of-information results". This is also where the Bahiru incompleteness lives (Repair 1). |

## Other observations

- A parallel editing process is actively working through the remaining review findings in the
  working tree (register fixes, the IB2 evidential-status paragraph, quantum-number label
  restriction, "didactic bridge" heading rename, §2.3→§§2.2/2.4/2.5 cross-reference fix). None of
  its in-flight hunks touch the five repairs checked here.
- The committed repair diff also cleanly landed several fixes outside my scope that I incidentally
  confirmed present: four→three frameworks, Axiom 3 renamed "Class 4 Selection", "unfalsifiable"→
  "unverifiable" (old :592), the symmetry-faces premise weakened (old :600), the Chalmers 2018
  citation attached to the meta-problem (old :602), E=I exchange-rate and local-conservation
  qualifications (old :518), "on inspection it confirms it"→"is consistent with it" (old :550).
- No newly-introduced factual or bibliographic error was found in any of the five repairs.

**Verdict in one sentence:** the five prescribed repairs are all genuinely and correctly applied at
their primary sites with every new bibliographic claim verified, but the fix pass stopped one
paragraph short — §6.5's "One locus, two reflections" still carries both the unqualified Raju
delocalization claim and the old convergence-as-support framing, and the Wetterich "not a metaphor"
and Salmon glosses were never touched.
