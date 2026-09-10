<!-- Action: act -->
<!-- Tracked-by: AIW-242 -->
# Cosmology (SB-HC4A) — Fable review, S312 (2026-08-26)

**Five Fable agents: §1–4, §5–6, §7–9, §10–12 + Abstract, and a whole-paper cross-section + citation audit.**
Each was handed the non-litigable rulings (criticality is an *effect*, not a prerequisite — the requirement is
open-ended Class 4 computation; closure is an advantage in a fit window, never a necessity, with the
budget-relative exception; "closure" not "return"; convergence is "consistent with", never a discriminating
test), the prose-register ban list, and the S311 verification discipline — *seven of nine deep findings in the
FMT review were refuted on adversarial check, the failure mode being a verbatim-accurate, context-false
quotation.* Every agent had to state what it checked before a finding counted, and several dropped candidate
findings at that stage.

**All five agents have reported.**

**Why this paper is being reviewed now.** `AIW-229` said the published PDF was stale against its own source.
**Measured, and it is:** a fresh build gives **68 pp / 29,142 words** against the committed-and-published
**66 pp / 27,985**, and `simulation` appears **9 times in the build against 22 in the published PDF** — §7.0's
terminology note, the `AIW-188` Φ-composition definition and the `AIW-184` jointness/minimality clauses never
reached the artifact. The `cosmology_formal` companion regenerates identically (47 pp / 17,091 words both) and
needs no republish.

**But the review found blockers a rebuild does not fix.** Those are the point of this record.

---

## ⭐ CONVERGENCES — found independently by two or more agents

| what | found by | status |
|---|---|---|
| **Abstract `:15` and §1.2 `:31` announce FOUR frameworks and list THREE** | §1–4, §10–12, **and** cross-section | **BLOCKER** — three agents |
| **Criticality sits inside the pattern's *definition*** at `:15`, `:25`, `:35`, `:106`, `:706`, `:727` | §1–4 **and** §10–12 | **BLOCKER** — the second stratum, exactly as predicted |
| **Axiom 3 carries two names, and neither is compliant** — "criticality stability" at `:27`, "Criticality Selection" at `:638`/`:729` | §1–4, §10–12 **and** cross-section | **BLOCKER** (escalated by §10–12) |
| **`:106` "Class 4 is the only class that can nest instances of itself"** | §1–4 **and** cross-section | **BLOCKER** |
| **`:130` Identity of Indiscernibles** used to support Axiom 2, while `:222` declines to rest anything on PII because it "is contested (Black, 1952)" | §1–4 **and** cross-section | SHOULD-FIX |
| **Planck floor asserted flatly at `:174`/`:191`, downgraded to "heuristic at the edges" at `:240`** | §1–4 **and** cross-section | SHOULD-FIX |
| **`:74` "quasi-infinite" used two sections before `:166` defines it, in a different sense** | §1–4 **and** cross-section | OPTIONAL |
| **Van Raamsdonk (2010) called a "demonstration" providing "strong support"** — a heuristic essay-contest argument | §5–6 **and** cross-section | SHOULD-FIX (ruling 4) |
| **`:574` offers the CMB as resolving evidence; `:588` declares it uninformative** | §7–9 **and** cross-section | **BLOCKER** (escalated by §7–9) |
| **`:570` Gutenberg & Richter (1956) listed as documenting SOC**, three decades before SOC existed | §7–9 **and** cross-section | SHOULD-FIX |

---

## 🔴 THE CITATION FINDING THAT MATTERS MOST — confirmed against the primary

**`:212` — Bahiru et al. (2024) is cited for the opposite of its thesis.**

The paper writes: *"on the holography-of-information results there is no bulk information that is not already
available at the boundary (Raju, 2022; Bahiru et al., 2024)"*.

The primary (arXiv:2301.08753, published JHEP 05(2024)261) says, verbatim: *"…information deep in the interior
of the bulk is invisible to single-trace correlators in the time-band and hence that it is **possible to
localize information in perturbative quantum gravity**."* They construct approximately local bulk observables
commuting with boundary charges to all orders in 1/N — **a qualification of Raju-style holography of
information, not support for it.**

⚠ This also weakens the paper's own argument at `:214` ("both relocate the information to the boundary"),
since Bahiru et al. deny the relocation perturbatively. **Repair:** drop them, or cite them honestly as the
counter-position and note that the architecture's IB1 needs only the non-perturbative statement.

**This is the sibling audit's exact failure mode** — an author's position cited in support when that author
disputes the very axis being claimed.

---

## 🔴 THE PHYSICS MISATTRIBUTION

**`:352` — Kerr–Newman uniqueness credited to the wrong people.** The paper says the rotating charged case
"rests on the uniqueness results of Carter (1971) and Robinson (1975) together with Hawking's (1972) rigidity
theorem." Carter and Robinson proved uniqueness for the **vacuum** rotating case (Kerr). Charged rotating
uniqueness is **Mazur (1982) and Bunting (1983)** — **neither appears anywhere in the paper.**

The paper's own reference list makes the error visible: Carter's cited title is *"Axisymmetric black hole has
only **two** degrees of freedom"*, and the sentence needs three.

---

## 🔴 TWO REAL MATHEMATICAL ERRORS IN §6

**`:437` — the James–Stein theorem is given a hypothesis it does not have.** The paper says dominance holds
"when d ≥ 3 parameters are drawn from a shared distribution … it is dominated by a joint 'shrinkage'
estimator that exploits the shared origin." There is no shared-distribution hypothesis: dominance under joint
quadratic loss holds for **arbitrary fixed θ ∈ ℝᵈ**, and the notorious point is that shrinkage helps even for
entirely unrelated parameters. **As printed, the error weakens the very reading the lens needs** — universal
dominance cannot be a signature of common origin.

**`:439` — the shrinkage coefficient is printed as a function of the unknown parameter.** The text gives
`w = (d−2)σ²/‖θ‖²`. The James–Stein estimator's coefficient is `(d−2)σ²/‖x‖²` — a function of the **data**.
No estimator can depend on θ. This is a flat error, not a framing choice.

**`:429` — the Bell factorizability condition omits the measurement settings.** Printed as
`P(a,b|λ) = P(a|λ)P(b|λ)`; the CHSH premise is `P(A,B|x,y,λ) = P(A|x,λ)·P(B|y,λ)`. As written it is not the
condition the argument needs — and in CHSH notation *a, b* conventionally denote the settings, compounding
the ambiguity.

**`:445` — the information-causality substitution is a further step, and it is not named.** The paper puts
"the locus capacity in place of a transmitted-bit count" and says "the quantum ceiling follows." Information
causality bounds the receiver's gain relative to *classical communication in a task protocol*; a static
capacity bound on jointly accessible information is a different, weaker statement (LHV models are also
capacity-bounded and sit at S ≤ 2). The condition conceded at `:447` covers the single-locus decoding
postulate but **not** the capacity-for-message substitution.

---

## 🔴 CROSS-SECTION CONTRADICTIONS

**The cyclic engine fires on a state two other sections say is never reached.** `:168` and `:252` file the
heat-death future with the horizons — "approached asymptotically and **never arrives at any finite time**",
"approached and never attained" — while §5.4 needs the saturated state *occupied* so its instability can
trigger decompression (`:272` "the moment the interior finishes emptying"; `:282`'s chain
"expansion → heat death (holographic saturation) → …"). §9.7 acknowledges a trigger-timing worry but only on
entropy-budget grounds. **Penrose's CCC faces the same structural issue and resolves it explicitly** via
conformal rescaling; this paper's analogue is silent. The repair is to separate the two futures — the
asymptotic de Sitter limit, and the finite-time configuration in which interior entropy has fallen to zero.

**Class 4's defining criterion is stated two incompatible ways.** `:76`: "**Irreducibility is the defining
criterion of the class**"; `:138`: "Universality serves here as *evidence* of irreducibility … rather than as
the class criterion itself". Against `:394`: "the **defining criterion is irreducibility with universality**".
⚠ **Under §6.2's version, Rule 30's Class 4 membership becomes doubly conjectural** — `:88` concedes its
universality rests on Wolfram's PCE conjecture — which unravels the §2.2 re-filing of Rule 30 the whole
taxonomy is built on. (`:394`'s cross-reference to "Section 2.3" is also wrong; the material is in §§2.2, 2.4, 2.5.)

**`:274` states an entailment the paper's own commitments deny.** "Irreversibility and computational
irreducibility (Section 2.4) entail that the decompression cannot retrace the previous cycle." §8.4 `:542`
commits the substrate to reversibility, under which a closed finite-state system is exactly recurrent — which
`:280` itself concedes ("Poincaré recurrence replaces renewal"). **And §2.4 contains no irreversibility result
at all**; it defines effective randomness and irreducibility.

**`:362` says of the cosmological horizon exactly what §4.1 denies.** "plainly an artifact of finite signal
speed: what lies beyond it is more of the same universe" against `:162` "not merely an observational
limitation — it is an ontological boundary… The boundary does not conceal a further fact". The paper has the
reconciliation available (observer-relativity, `:226`) and does not invoke it here.

**`:366` contradicts §5.6 on whether particles exchange information.** "never touching, never exchanging
information across their boundaries" against `:330`, where particle interaction *is* information exchange
across boundary surfaces ("This information exchange *is* the interaction"), and `:222`, where particle
surfaces "can even be made to collide."

**`:328` vs `:336` on quantum numbers as boundary labels.** `:328` derives the discreteness of colour, baryon
and lepton number from their being "labels on these states"; `:336` says "**Colour and weak isospin do not
appear as boundary labels** … **Baryon and lepton number have no boundary home at all**." The `:334`
discreteness/conservation split does not rescue it — discreteness-via-boundary-labels still needs a label.

**IB2 is a premise partly supplied by the model whose conclusion it supports.** `:210` lists holographic
saturation as shared by all inventory members; it is established only for the horizons (`:206`, `:270`). For
particles it is **the model's own prediction** (`:314`), for the Big Bang a consequence of the cyclic
mechanism that `:246` explicitly bars from support duty, and for the Planck floor nowhere established. `:260`
then labels the whole triple "rigorous… shared by every member" while defending only impermeability.

**`:552` (§8.4) endorses a timeless fixed-point reading that §5.4's instability argument rules out.**
`:274` needs closure to be "an ongoing encoding operation, not a stored configuration"; `:552` reads
Φ(U) = U as "a **timeless** fixed-point condition on the whole four-dimensional block". The two may be
reconcilable — process within emergent time, condition on the block from outside — but the paper never
performs the reconciliation, and the trigger argument works under only one of them.

**`:574` offers the CMB as resolving evidence; `:588` declares it uninformative.** An asymmetric
"evidence counts only if positive" posture across two weak-point subsections. (The companion's own result is
reported accurately at `:588`.)

---

## 🔴 CLAIM-STRENGTH DEFECTS IN THE DISCUSSION AND ABSTRACT

**`:707` "structurally guaranteed"** — *no section argues guaranteed emergence.* §2.5 establishes only that
Class 4 *can* nest Class 4; §7 labels the correspondence conjectural; and the sentence's own dash-clause is
conditional on a subsystem *already having* closure, so it cannot ground a guarantee that such subsystems
emerge. ⚠ **This is `AIW-164`, filed 2026-08-06 and independently rediscovered here 20 days later** — it was
live when v4 published on 2026-08-08.

**`:686`/`:700` "derives cyclicity"** — asserts a derivation the paper disclaims elsewhere: §5.4 "proposed
here as a motivated conjecture, not a result"; §9.7's own title, "The Saturation Trigger Is a Motivated
Conjecture". The same phrase recurs at `:616`, inside a weak-point section.

**`:27` "a unique architecture emerges"** — contradicted by the next sentence, by `:146` ("the elimination
selects a computational class, not a single architecture") and by `:664` ("they underdetermine the model
within that class").

**`:690` drops the conditionality** that `:306` carries on the endgame-robustness claim, and adds
self-evaluation ("is a significant strength").

**`:714` "The structural identity is architectural"** — §7.2 `:488` explicitly leaves open "Whether this rises
to a strict structural identity — rather than a strong correspondence".

**`:310` "resolves the baryon asymmetry problem"** — what is explained is the global CPT accounting; the
within-cycle asymmetry is posited, as `:308` concedes.

**§10's title over-promises, but its substance is compliant.** The §10–12 agent examined the ruling-2
collision head-on and reports **no forbidden necessity claim in §10** — closure appears only as a derivation
bullet, and the necessity asserted is of the *axioms for the conclusion*, with §10.2 disclaiming
model-uniqueness at `:664`. **Only the title needs scoping** → "The Axiom-Necessity Argument".

---

## SHOULD-FIX — citation characterization (all confirmed against primaries)

- **`:346`/`:692` Wetterich (2022c)** — the primary says diffeomorphism symmetry emerges in the **naive**
  continuum limit and that the setting "**could serve as** a model for quantum gravity **if** diffeomorphism
  symmetry is realized in the **true** continuum limit." The paper's "This **is** a cellular automaton model of
  quantum gravity — **not a metaphor**" drops both conditions. (The exact-local-Lorentz half **is** verbatim
  in the primary.)
- **`:354` Arcos & Pereira (2004)** — "confirmed … reproduces **all electron quantum numbers**" against the
  primary's "can thus be consistently **interpreted as a model** … in which the concepts of **mass, charge and
  spin** become connected with the spacetime geometry." Three quantities, an interpretation, not a confirmation.
- **`:294` Ruggiero (2020)** — "**Independent support** … who **showed** that Hawking radiation heating … **can
  produce conditions matching** the conformal boundary required by Penrose's CCC". The primary shows only that
  energy density and temperature diverge at the Big Rip, then **proposes** a CCC variant. Sole-author,
  unpublished arXiv note cited as support.
- **`:358`/`:368` Poplawski (2010)** — cited for preventing the "point or **ring**" singularity; the primary
  concerns the **cosmological** singularity. The ring extension is this paper's own conjecture wearing
  Poplawski's citation. (The `:362` baby-universe use of the same paper **is** supported.)
- **`:570` Gutenberg & Richter (1956)** listed as documenting self-organized criticality — SOC was proposed in
  1987. They documented the magnitude–frequency power law SOC later reinterpreted.
- **`:439` Salmon et al. (2024)** — glossed as "James-Stein advantages in entangled Gaussian sensing"; the
  primary finds entanglement **diminishes** the JS advantage in the noiseless case and noise **restores** it.
- **`:490` Hengen et al. (2016)** cited for maintaining criticality; its own title is firing-rate homeostasis.
  The criticality-tuning claim is Ma et al. (2019).

**Ruling 4 — convergence framed as support, five sites:** `:216` (ER=EPR "provides independent support",
Complexity=Action "further strengthens"), `:294`, `:360`, `:415`, `:427`. The paper's own correct register
exists at `:228` ("presented as *consistent with*… a consistency check it passes, not evidence for it") and
`:316`, so these are deviations from house style rather than house style.

---

## SHOULD-FIX — argument hygiene

- **`:419` files three distinct obstructions under one wrong label.** Gödel's theorems concern derivability in
  consistent r.e. formal systems, not describability — and on the model's own premise (`:82`) the substrate has
  a **finite rule table**, so an equation stating the true rule would be a complete dynamical law. The three
  real obstructions are *capacity* (boundary state ~A/4ℓ_P² bits), *irreducibility* (no predictive shortcut)
  and *undecidability* (universality ⇒ undecidable questions). ⚠ `:364` then cites "the inexpressibility
  **theorem** of Section 6.4", and §6.4 states no theorem.
- **`:274` attributes to §6.3's definition a dynamical premise §6.3 does not contain.** §6.3 `:403` defines
  Φ(U) = U as a **losslessness** condition, which a static configuration can satisfy; the "continuously
  recompute" reading the instability argument needs is an *additional* premise. §9.7 tacitly concedes this by
  asking for "a proof that Φ(U) = U admits no static solution".
- **`:652`'s closure bullet uses the vacuous reading §6.3 disowns** — §6.3 says "Read loosely, Φ(U) = U is
  true by definition for any system whatever", yet the bullet derives closure from structure alone without
  invoking A4's "Information is conserved."

---

## Prose register

`:94` "so it is worth drawing precisely" · `:126` "One deflationary reply **deserves recording**, since it is
the last exit" · `:228` "a corollary **worth stating**" · `:252` "One sharpening is **worth recording**,
because it shows the taxonomy is geometry rather than rhetoric" · `:292` "**the paper should not present** the
three endgames as equally supported" (an editorial note left in the manuscript) · `:324` "sharp enough to be
**worth stating**" · `:366` heading "**The Big Rip as didactic bridge**" · `:409` "a regime where it
**bites** hardest" · `:447` "Two clauses of that postulate are **load-bearing**" and "which is the bound the
section **exists to escape**" · `:692` "**Most remarkably**, Wetterich…" · `:731` "is, I believe, **the most
important open question in the philosophy of science**".

Deliberately **not** flagged: epistemic-status labels ("flagged explicitly as the model's interpretive layer",
"offered as corroboration, not foundation") are scope-labeling, not self-narration; and `:729`'s "the deepest
being the cognitive ceiling problem" is earned verbatim by §9.5.

---

## ✅ Verified clean — do not re-litigate

**Confirmed against primaries:** Rowland (2006) at `:64` — row 2ⁿ reappearance on the **right** side, "begin
again" locally, reversibility "under the condition that the right half of each row is white", k-colour
generalization via bijectivity: all four details exact (one agent suspected "left edge" and withdrew the
finding after reading the PDF). **Jow & Scott (2020)** at `:616` — "no statistically significant evidence for
the presence of Hawking points in the CMB", verbatim. **Elze (2024)** at `:348`. **Poplawski** baby-universe
use at `:362`. **Wetterich's** exact-local-Lorentz claim.

**Re-derived or re-counted and correct:** the Bekenstein-bound → area-law algebra at `:206`; the capacity
arithmetic at `:324` (0.36 bits; A ≥ 4ℓ_P² ln N); "seven weak points" (§9.1–9.7); "five axioms" (A1–A5);
"approximately 60 orders of magnitude" at `:179` (actual ≈ 62); DESI DR2 significances; Egan & Lineweaver
entropy figures and the "eighteen orders" arithmetic; Carter (1968) g = 2; BGV; BKL and asymptotic silence;
Klinkhamer–Manton sphalerons preserving B−L; Harlow–Ooguri; Culik & Yu undecidability; Tsirelson 2√2 and
PR-box 4; the ATLAS/CMS top-entanglement framing (entanglement observed, Bell violation not established —
correctly stated).

**Rule 30's irreducibility** stated flatly at `:76`/`:84`/`:86` is handled two paragraphs later at `:88`
("Rule 30's irreducibility is a conjecture… Nothing here claims…") — **not** context-false. Its centre-column
aperiodicity at `:86` is correctly hedged "as far as it has been computed".

**The elimination argument (§3.2–3.3)** declares its conditionality on substrate determinism upfront, labels
the Class 5 elimination abductive, and flags the stochastic-law alternative as removed by assumption. Clean.

**Ruling 3 ("return")** — clean throughout; every grep hit is an ordinary verb use, not the banned property name.

**The Abstract is in the best shape of the three scope regions** on conditionalization: substrate-determinism,
saturation-instability, DESI disfavour-not-exclude, and the Kerr–Newman "connected to (though not established
by)… unresolved scale and horizon tension" all correctly mirror §§3.2, 5.4, 5.7, 9.7.

---

## §7–9 — the FMT bridge survives; the falsification section does not

**The headline is a negative result worth having: §7 is the highest-risk section in the paper for the project
rulings, and it is clean.** No criticality-as-prerequisite formulation, no closure-necessity claim, no
capability-barrier on either FMT axis, no "return" as a property name. §7.2's boundary-opacity and
meta-cognitive-limitation statements are the architecture's own Gödel-diagonal limits rather than axis
barriers, and §9.5's Class-5 ceiling is theorem-grounded on the Kolmogorov pigeonhole. **The cross-scale
bridge is properly hedged.** The defects are elsewhere.

**🔴 `:574` (§9.2) names resolution criteria that cannot discriminate.** "Power-law distributions in the
cosmic microwave background, scale-free structure in galaxy distributions" — both are **generic outputs of
standard inflation plus gravitational hierarchical clustering with no criticality anywhere**. And the CMB
criterion contradicts §9.4(b), which rules the CMB uninformative for the SOC hypothesis. ⚠ **The asymmetric
reading does not rescue it:** if inflationary processing severs the CMB from substrate dynamics — §9.4's own
argument — then a *positive* CMB power law would be attributed to inflation, not criticality. So the criterion
fails in both directions. §9.4(b) already names the better targets: primordial gravitational-wave statistics,
higher-order non-Gaussianity, late-time nonlinear structure.

**🔴 `:482` (§7.1 mapping table, row 6) asserts a conservation claim nobody defends.** "Conservation of
energy/information across boundary | Conservation of information across implicit-explicit split". The
cognitive side appears **nowhere else in the paper** and is contradicted by the paper's own descriptions:
§8.3 calls the explicit form "a lower-bandwidth, organized projection of **selected** information" — selective
and lossy — while §8.4 concedes "Landauer erasure is real for the interior description", and brains are
interior systems. Meanwhile the cosmological side is a *losslessness* condition (§6.3 `:403`). ⚠ **§7.2's
defended feature list silently omits this row**, which is the tell: the paper does not defend it because it
cannot. The row papers over a genuine disanalogy at the exact point the cross-scale bridge is made.

**The falsification section names only confirming resolutions.** §9.6 concedes no derivable signature
currently exists — so nothing can be observed to fail — and §9.7 omits the symmetric falsifier even though
§5.4 `:280` has already proven its closed-system form (Poincaré recurrence instead of renewal). Of the seven
weak points, 9.1, 9.3 and 9.4(a) are implicitly two-sided; **9.6 and 9.7 are confirmation-only**.

**`:592` cites the wrong mechanism for unfalsifiability.** Incompleteness blocks complete self-description —
i.e. *verification* — not falsification, which needs one failed prediction, and §9.4 lists testable
predictions directly above. The genuine unfalsifiability argument is §9.5's Class-4 ceiling, not §6.4's Gödel.

**`:602` — predicting one's own unfalsifiability confirms nothing.** "either the strongest possible
confirmation of the cross-scale computational symmetry (the model predicts this exact epistemological
limitation) or the strongest possible objection to it." **Every unfalsifiable theory that declares itself so
predicts the same limitation**, so the confirmation branch is logically empty. §9.4's parallel is more careful
("either a devastating weakness or a structural prediction"). "Strongest possible" twice is also an empty
superlative.

**Physics gaps in §8 that the weak-point section does not cover:**
- **`:518` E = I is not yet well-posed.** The two cited results give *different, context-dependent* exchange
  rates — Landauer's kT ln 2 per bit is temperature-dependent, Bekenstein's is radius-dependent via
  S ≤ 2πkER/ħc — so **no universal conversion factor exists** for "the same quantity" to be measured in. §9.1
  addresses only "correlated vs identical", never the missing rate.
- **`:518` collides with general relativity.** In FRW spacetime global energy conservation is not well-defined
  (no timelike Killing field; photons redshift), so E = I plus the exact information conservation of §8.2/§8.4
  and Axiom 4 would entail a globally conserved energy GR does not supply. **The paper's own machinery
  supplies the fix** — exact conservation as a substrate property, energy as an interior bookkeeping quantity
  conserved locally and approximately, like the arrow of time.
- **`:550` "on inspection it confirms it" assumes what it confirms.** The sentence states the CPT theorem's
  premises as "Lorentz-invariant, local, **unitary**", then uses the theorem to confirm substrate
  reversibility ≈ unitarity. And 't Hooft's own information-loss variant (equivalence classes with emergent
  unitarity), cited in the same sentence, is a live counterexample to "pin".

**`:508` cites the wrong mechanism for the fractal pattern.** "since Class 4 dynamics contain Class 3
(self-similar) behavior as a subprocess" — but recurrence of the full Class 4 self-referential architecture at
smaller scale is **Class-4-in-Class-4 self-nesting**, which §2.5 `:106` explicitly names as "the structural
foundation for the cross-scale identity developed in Section 7". Class 3 containment yields reducible
self-similar *products*; an embedded brain is not a reducible fractal subprocess.

**`:564` Vopson (2025) is a theoretical proposal, not an empirical result** — "provides empirical support"
is a category error on top of the ruling-4 problem, and the "If correct" hedge conditions truth, not the
category. ⚠ Resting Weak Point 1's mitigation on a contested infodynamics paper is also reputational exposure
inside the falsification section.

**`:602` "ESM" is used exactly once in the paper and never expanded**, and "the Meta-Problem" is capitalized
as a term of art with no in-text citation — Chalmers (2018) is cited at `:498` but not here. A cosmology
reader has no referent for either.

**`:600` rests the paper's deepest objection on an uncited evolutionary-psychology claim** — "faces of
predators and prey are the most symmetric, and therefore most survival-relevant, patterns" is a non sequitur,
and faces are not uniquely the most symmetric environmental patterns. **The argument only needs the weaker,
well-supported premise** that human perception is strongly biased toward symmetry detection.

**Register in scope:** `:558` "A theory that claims no weaknesses is not a theory." (lecturing the reader on
how science works) · `:596` "and it was identified during the model's initial formulation" (the objection's
provenance is irrelevant) · `:606` "I include it because intellectual honesty requires it." (the two preceding
sentences already do the honest work; announcing honesty undercuts it) · `:622` "The honest state of the
evidence is sobering:".

**Optional:** `:465` cross-references §6.1 as distinguishing the two senses of "holographic" — §6.1 *uses*
both and never distinguishes them; §7.0 is where the distinction is drawn. `:490` "maintains criticality
through self-organized criticality" is circular — SOC *is* untuned maintenance of criticality; §3.2 already
has the non-circular form. `:494` rests a 2026 distributed-storage claim solely on Lashley (1950) and Pribram
(1971) — the content is protected by §7.0's narrow definition, but the exposure is citational. `:588` "large
angular scales (ℓ < 1500)" — conventionally *large* means low ℓ (≲ 30); ℓ < 1500 reaches down to ~7 arcmin.
