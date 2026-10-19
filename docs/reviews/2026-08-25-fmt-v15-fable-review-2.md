<!-- Action: act -->
<!-- Tracked-by: AIW-236 -->
# FMT v15 — the second mandatory pre-publish Fable review

**Run S310, 2026-08-25. ⛔ INCOMPLETE — Fable usage credits ran out mid-run. MG parked it to resume 23:00.**

Six Fable agents commissioned, read-only, each given `docs/reviews/2026-08-24-fmt-citation-audit.md` and
`docs/reviews/2026-08-24-fmt-v15-fable-review.md` so nothing already repaired was re-found. Five section
reviewers plus one whole-paper cross-section pass.

**Why it was run:** MG, 2026-08-25 — *"definitely needs a full fable review later."* The manuscript had
taken **184 edits** since the first review, so this is a re-review of a substantially different document,
not a formality.

**Two rulings handed to every agent as non-litigable:** criticality is an **effect** (the requirement is
open-ended Class 4 computation); and the Introduction's addresses-all-eight claim is **ruled and rejected
as a finding**. Both held — no agent tried to re-open either.

## Status board

| # | range | state | found |
|---|---|---|---|
| 1 | `:1–131` — title, Abstract, §1, §2 | ✅ complete | 2 blockers, 10 should-fix |
| 2 | `:132–539` — §3 The Four-Model Theory | ⛔ **DIED on credits, no findings** | — |
| 3 | `:540–695` — §4 Philosophical Commitments, §5 Binding/Criticality/Holographic | ✅ complete | 4 blockers, 17 should-fix |
| 4 | `:696–894` — §6 Explanatory Range, §7 Comparative Analysis | ✅ complete | 4 blockers, 12 should-fix |
| 5 | `:895–1113` — §8 Predictions, §9, §10, §11, back matter | ⛔ **DIED on credits, no findings** | — |
| 6 | whole-paper cross-section pass | ⛔ **DIED on credits — one partial lead, verified by hand** | 1 confirmed defect class |

**Running total from the half that completed: 10 blockers, 39 should-fixes.** §3 — the theoretical core
and the longest section — has not been reviewed at all, and neither have the predictions.

⚠ **Nothing in this review has been folded in.** The manuscript is untouched as of this writing.

---

## ⭐ THE HEADLINE, and it is the same headline as last time

**The half-applied-repair disease is alive at four independent sites, found by three different routes.**
The first review's lesson was *sweep by pattern across the whole file, never by line number*. It was not
followed, and the criticality-is-an-effect ruling — applied at twelve sites — **left at least four sites
still calling criticality a prerequisite or a commitment.** Reviewer 4 found two, the dying cross-section
agent found three, and a hand grep afterwards found a fifth wording family neither had named.

**Do the sweep by pattern before anything else at 23:00.** The findings below give the full site list.

### Confirmed violations — criticality stated as a requirement/prerequisite/commitment

| line | text | also in `.tex` |
|---|---|---|
| `:771` | *"The theory's commitments — continuum (not binary), substrate independence, **criticality threshold** — predict a gradient…"* | `paper.tex:970` |
| `:877` | *"without specifying the four-model taxonomy or **the criticality prerequisite**"* | `paper.tex:1105` |
| `:901` | *"the theory's core commitments — **criticality as prerequisite**, variable permeability, holographic storage"* | `paper.tex:1138` |
| `:1058` | *"architectural properties (**criticality as computational prerequisite**, permeability…)"* | `paper.tex:1322` |

All four are inside *lists of the theory's commitments*, so the list item must be **renamed**, not softened.
The paper's own model wording is at `:174` — *"The requirement itself is the open-ended regime; criticality
is how that requirement is observed in a biological substrate."*

### ⚠ A FIFTH WORDING FAMILY — needs an MG ruling, not a unilateral fix

**"criticality commitment"** appears at `:889` (twice), `:905` and `:1080`. It is weaker than "prerequisite"
— a commitment to criticality being *the observed signature* is defensible — but it still puts criticality
on the commitments list, which is what the ruling moved away from. **Decide once, apply everywhere.**

### Verified CLEAN in the same sweep — do not re-check these

| line | why it is fine |
|---|---|
| `:174` | glossary; the canonical effect-framing, and the model for the repairs above |
| `:194` | table: *"Consciousness requires the open-ended computational regime, whose neural effect is near-criticality"* |
| `:905` | *"pushing the substrate below the criticality threshold"* — an effect-level empirical claim about the neural signature, correct as written |
| `:955`, `:1013` | *"the criticality threshold"* as a neural quantity to be specified — correct |
| `:1312`, `:1350` | reference-list entries (the companion's own title; Kanders et al. 2017's title). Not violations — but `AIW-140` separately slates the companion's title to change |

⚠ **Borderline, flagged not ruled:** `:1003` — *"the capability-first reading of criticality it requires"*.
Parsed correctly, "it requires" attaches to the companion **program**, not to consciousness, so it is not a
violation. It is ambiguous enough for a skimming referee to misread. Worth a rewrite while the others go in.

### Other patterns swept by hand — all CLEAN

| pattern | result |
|---|---|
| "anterior prefrontal" / "anterior PFC" in REM contexts | **none** — the S309 repair held |
| five principles vs three | **clean** — `:17`, `:70`, `:134`, `:702` all say "three principles" |
| "four modules" | **clean** — the only hit is `:15`'s deliberate pre-emption, *"four model kinds rather than four modules"* |
| banned exact string "the criticality requirement" | **none** |

⚠ **Not swept — the greps timed out and must be re-run at 23:00:** capability-barrier language,
localized-concept language (hub / grandmother cell / circumscribed synapse set), and the seizure route
(supercritical / hypersynchrony / Class-2). Reviewer 3 reports no seizure claims in `:540–695` and
Reviewer 4 reports no barrier-shaped sentences in `:696–894`, so the exposure is confined to the two
unreviewed ranges.

---

## Reviewer 1 — lines 1–131 (title, Abstract, §1 Introduction, §2 Eight Requirements)

**Verdict: close to publishable, but the IIT mischaracterisation repaired in §7 survives verbatim in §2.1,
and one primary citation is the wrong paper.**

Reviewer's own verification, so nobody re-checks it: criticality directionality compliant at all four range
sites (`:15/:17`, `:54`, `:58`, `:66`); Hengen & Shew correctly scoped at `:19` and `:58` (the first review's
`:58` misattribution **is** repaired); the four-model-kinds pre-emption present at `:15`; no barrier-shaped
sentences; no banned exact strings; requirement attributions 1–8 (`:39`–`:46`) all check out.
`pytest scripts/test_content_integrity.py` 32/32.

### Blockers

**B1 — `:86` — "consciousness = Φ" survives in §2.1 while §7 now states it correctly.**
> *"IIT attempts to address it by defining consciousness as intrinsic causal power (Φ), treating experience
> as identical to integrated information"*

`:834` and `:843` were repaired to *"identifying an experience with a maximally irreducible cause-effect
structure, whose irreducibility Φ quantifies"*. `:86` still asserts the identity IIT proponents explicitly
reject, so §2.1 and §7.2 disagree — and the loose form sits in the requirements centrepiece, which is where
an IIT-sympathetic referee reads first.
**Repair:** mirror `:834`'s wording; the Aaronson and Doerig cites stay.

**B2 — `:98` — Markov blankets cited to the wrong Friston paper, inside the sentence adjudicating whose
blankets are whose.**
> *"PP uses Markov blankets (Friston, 2010), though Bruineberg et al. (2022) argue that this use conflates
> an instrumental modeling construct (Pearl's blankets) with a metaphysical claim about system boundaries
> (Friston's blankets)."*

Bruineberg et al.'s own history dates the FEP use to Friston & Ao (2012) and Friston (2013), *"Life as we
know it"* — not the 2010 *Nature Reviews Neuroscience* free-energy review.
⚠ **Friston (2013) is not in the reference list** — only Friston 2010 at `:1282` — so the repair needs a bib
entry too. Friston 2010 stays for the free-energy citations elsewhere; those are correct.
**Repair:** cite Friston (2013), *J. R. Soc. Interface* 10(86):20130475, and add the reference.

### Should-fix

| # | line | what is wrong | repair |
|---|---|---|---|
| S1 | `:62` | Element 5's gloss does not match §3.5. **"simple consciousness" appears nowhere else in the paper** (§3.5, §6.3, §6.4 and the animal table all say *basic*), and *"a system that models itself"* is §3.5's definition of **simply extended** (`:392`), not the entry rung (`:390`). A referee checking contribution 5 against its own section finds a term that does not exist and a gloss on the wrong rung. | *"from basic consciousness (minimal self-simulation) through triply extended consciousness (third-order self-observation…)"* |
| S2 | `:31` | A 2022 citation inside a *"published in 2024-2025"* claim — Seth & Bayne is 2022, on the sentence's own face. | "2022–2025", or move Seth & Bayne to `:37` |
| S3 | `:52` | *"five elements that neither MDM, SMT, nor any other existing framework provides **individually** or in combination"* — "individually" asserts no framework provides even one. `:66` then credits Damasio with *"progressively elaborated self-representations"*, element 5's genus. A hostile referee quotes `:66` against `:52`. | *"…five elements whose combination no existing framework provides"* — MG's call |
| S4 | `:54` | *"not to a substrate-neutral quantity"* contradicts `:845` (*"that running, **substrate-neutral**, evolved-closure-gated updating"*) and `:52`. The intended contrast is quantity-vs-kind-of-dynamics; the modifier points the wrong way. | *"…not to a scalar quantity abstracted from the dynamics."* |
| S5 | `:66` | Same requirement called *"physical"* here and *"computational-regime"* at `:58`. Residue of the repaired *"physical prerequisite (criticality)"* — noun fixed, adjective left, and "physical" re-blurs the line the ruling settled. | *"adding a computational-regime requirement on the substrate…"* |
| S6 | `:86` | *"HOT and AST offer deflationary accounts"* — Rosenthal's HOT is reductive-representationalist and claims to **explain** phenomenal consciousness. Rosenthal would reject the label; a HOT referee will. | *"…offer reductive accounts that explain why we report…"* |
| S7 | `:90` | Block's access/phenomenal distinction presented as *"further refined"* Levine's gap. Different distinction — kinds of consciousness, not forms of explanation. Philosophy referees are pedantic here. | *"Relatedly, Block (1995, 2007) distinguished…"* |
| S8 | `:122` | *"Epiphenomenalism (Huxley, 1874; Jackson, 1982) is widely dismissed as absurd (how could evolution produce something causally inert?)"* — **Jackson 1982 defends epiphenomenalism and answers that exact objection** (qualia as by-products). The paper cites a source for a position while calling it absurd on grounds that source rebuts. "Absurd" also overstates the field. | *"widely rejected"* + name Jackson's by-product reply |
| S9 | `:128` | *"This is a genuine insight."* — banned register class: copula + evaluative noun carrying no claim. | delete |
| S10 | `:1` | Title: one does not *unify* a single problem. Titles get read literally, and first. | *"…Framework for the Hard Problem, Binding, and Altered States"* — MG's call |

**Micro:** `:70` — *"a convergence shared in part with…"* — the *claims* were derived, not the convergence;
and `:19` says "shared" where this says "shared in part."

### Three attention questions, answered

- **Abstract delivery — CLEAN.** Every promise delivered: the six phenomena (psychedelics, anaesthesia,
  dreams/lucid dreams, split-brain, DID `:757`, animal consciousness `:775`); redirection / permeability /
  forking as consequences (`:739`, `:757`, §4.2.3); the anosognosia prediction (`:919`); three-principles
  structure matches AIW-138 exactly; *"five predictions"* (`:74`) verifies against Predictions 1–5.
- **Requirements crisp enough for §6 scoring — YES**, one soft spot: §2.6 is disjunctive (combination
  problem for panpsychists, emergence for physicalists), so a theory can "address" it by answering only its
  own horn, and Table 5's grade implicitly picks a horn. Not a defect — worth knowing. (Reviewer 4
  independently escalated the same thing to should-fix — see its S4.)
- **Hostile-referee survival — GOOD after repairs.** Remaining exposure is exactly B1, B2 and S3. The `:58`
  priority claim is carefully double-hedged and judged survivable as written.

---

## Reviewer 2 — lines 132–539 (§3, The Four-Model Theory)

⛔ **DIED on credits before producing any findings.** It had loaded the knowledge base and read the full
range, and was moving to line-number verification and pattern sweeps when it terminated.

**This is the theoretical core and the longest section — 408 lines, roughly a quarter of the paper — and it
is entirely unreviewed. It must be re-run first at 23:00.** The commissioned focus was: implicit/explicit
and world/self axes used consistently; the closure material (narrow waist buys efficiency, feeding back into
the same population buys self-consistency); the asserted-not-derived cut at §3.4.3; the *erweitert* ladder;
and any sentence implying a concept is **localized** structure — a hub, a grandmother cell, a circumscribed
synapse set — which crucible's `cru115` sweep has now measured against and which is a known exposure.

---

## Reviewer 3 — lines 540–695 (§4 Philosophical Commitments, §5 Binding, Criticality, Holographic Storage)

**Verdict: far better shape than last round — the rulings took and the discipline holds — but two of the
four blockers are the paper contradicting its own already-repaired positions.**

### Blockers

**B1 — `:572` — the superseded "presents as uncaused" formulation survives, twice, four lines after the
approved formulation.**
> *"In a deterministic universe the apparatus is unrepresented and the choice presents as uncaused; in an
> indeterministic universe the apparatus is still unrepresented and the choice still presents as uncaused."*

`:568` states the approved form verbatim — *"The choice therefore presents not as uncaused but as
*originating* in the self"* — and the S300 refinement explicitly superseded "presents/feels uncaused" as a
**paper** formulation (an event with no represented cause presents as *arbitrary*, not free; the
phenomenology of volition is self-origination). `:572` contradicts `:568` inside the same subsection, and
sits in the neutrality paragraph a referee reads most carefully.
**Repair:** both clauses → *"…presents as originating in the self."* The rest of `:572` — scope guard,
neutrality, no evidential weight — is exactly right and untouched.

**B2 — `:630` — "cannot be made return-free at all" contradicts the paper's own sixth banked result.**
> *"A recurrent network cannot be made return-free at all — one can only choose which of its subsets sit
> inside a returning component."*

§8.9 at `:999` states the opposite and **prices** it: buying return-freedom — no closed walk anywhere —
costs 74.0% and 71.5%. Expensive-but-achieved is not "cannot at all." Identical defect class to the closed
`:993` blocker, surviving at a site the sweep missed.
**Repair:** scope to the local operation, mirroring `:999`'s own language — *"cannot be made return-free by
any local intervention — opening the loop in one place relocates the returning component rather than
abolishing it; global return-freedom is achievable only at the cost of the recurrence itself, and Section
8.9 prices that operation at a factor of five to six over relocation."* The follow-on sentence then follows
validly from the local-intervention scope.

**B3 — `:564` — Schurger et al. (2012) cited for the claim their paper is famous for deflating, which
`:576` itself states correctly.**
> *"The ESM narrates decisions already made at the substrate level (Libet, 1985; Schurger et al., 2012;
> Wegner, 2002)"*

`:576`, twelve lines later, correctly reports that Schurger *"showed that the readiness potential reflects
stochastic fluctuations rather than a discrete 'decision' moment"* — i.e. that there is no early
already-made decision of the kind `:564` cites them for. One citation on both sides of the same question.
**Repair:** drop Schurger from `:564` (Libet and Wegner carry the setup), or demote to *"cf. Schurger et al.,
2012, on what the substrate-level precursor actually is."*

**B4 — `:642` — the LLM parenthetical is factually wrong in the direction an AI-literate referee catches
first.**
> *"A base LLM lacks persistent implicit models (knowledge resets between interactions)"*

An LLM's weights — its implicit knowledge — are precisely what does *not* reset between interactions; what
resets is the interaction state. The rest of the sentence is accurate and careful, which makes the false
parenthetical stand out more.
**Repair:** *"lacks persistent, experience-updated implicit models (weights are frozen at deployment;
interaction state resets between sessions)"* — also the architecturally correct FMT claim, since the
theory's implicit models are continuously reshaped by use.

### Should-fix

| # | line | what is wrong | repair |
|---|---|---|---|
| S1 | `:656` | A **theory** paper listed as an empirical finding: Tucker, Luu & Friston 2025 (*Entropy* 27:829) is a theoretical active-inference argument, not an empirical criticality-signature study — and `:905` characterises it correctly. | move out of the empirical list ("cf." or a separate theoretical-convergence clause) |
| S2 | `:690`, Table 4 `:684` | Dose-scope extension: *"Ketamine does not push the substrate subcritical — it increases neural entropy (Schartner et al., 2017)"* sits in a paragraph whose subject is ketamine as **anaesthetic**. Schartner 2017's own title says *psychoactive* doses — sub-anaesthetic. Same class as audit finding 10. | cite Casarotto et al. (2016) — already in the reference list and already used at `:905` for exactly this — or state the dose scope |
| S3 | `:658` | *"returning to the dynamical regime that consciousness requires"* — the nearest antecedent in the paragraph is criticality, so it reads as criticality-as-requirement. Not the banned string, but the same content one paraphrase away. | *"…the computational regime the simulation requires — the regime whose neural signature is proximity to criticality."* |
| S4 | `:674` | Table intro claims an ordering the table lacks: rows run waking, REM, NREM, propofol, ketamine (not subcritical), psychedelics (past-critical), vegetative, covert awareness (at critical), MCS — not monotonic. | "ordered" → "characterized"/"classified" |
| S5 | `:628` | Mirror self-recognition attributed to corvids **and parrots**. In the cited literature MSR is reported only in magpies (Prior et al. 2008), with failed replications on record. Audit flagged it parenthetically; it survives. | drop MSR from the list, or attribute to magpies specifically |
| S6 | `:632` | *"not a manipulable axis"* is quotable against §8.9, which built and priced exactly that comparison in silico. Both true across lanes (biological substrate vs constructed comparison system) — the text does not draw the lane here. | add the lane distinction |
| S7 | `:634` | Wolfram's **conjecture** stated as delivering the result: *"is, by Wolfram's equivalence principle, capable of universal computation"*. Only specific universality results (Rule 110, Cook) are proven. | *"is, if Wolfram's (2002) equivalence principle holds, capable of…"* — the next sentence already models the right posture |
| S8 | `:614` | Uncited empirical claim: *"the subcortical brain beneath it already sustains an essentially complete behavioral repertoire of orientation, locomotion, and motivated action"*. True to the decorticate literature, uncited in a manuscript under citation audit. | cite Merker (2007, BBS) or the decorticate-rat work, or hedge |
| S9 | `:604` | The falsifiability sentence is vacuous under the paper's own constitutive reading — if phenomenal character *is* the closure computation, the functional signatures of experience just are signatures of that computation, which the system has by hypothesis. Also borders on advertising the paper's own scientific virtue. | delete, or name an independent signature that would count |
| S10 | `:608` | Strong illusionism slightly misstated — under it there are no phenomenal properties to misrepresent; introspection misrepresents *quasi-phenomenal* states **as** phenomenal. Also *"which Frankish argues they can"* needs verifying against Frankish 2016. | correct the statement; verify or soften the attribution |
| S11 | `:638` | Seth's position glossed weaker than he holds it: the appositive *"an operation that living tissue happens to perform but does not exclusively possess"* reads as Seth's, but it is FMT's editorial move — Seth leans toward life mattering. | mark it as the theory's reading |
| S12 | `:600` | False dichotomy the next sentence undercuts — a generic agent-model applied to many targets is a third option, and the passage concedes it two sentences later. | soften: the alternative pays either per perspective or for generic agent-structure built from scratch |
| S13 | `:598` | The per-instance price overstates — similarity-based stimulus generalization extends avoidance to unfamiliar feature-sharing instances cheaply, with no categorical abstraction. | reword the price to precision/reliability, not instance count |
| S14 | `:606` | The Mary pair is quotable against itself: *"does she learn something new? Under FMT, yes"* vs, same passage, *"Mary learns no new fact"*. The old-fact/new-concept resolution is present and correct. | *"She gains something new — but not a non-physical fact"* |
| S15 | `:558`, `:1594` | **"Van Rullen" should be "VanRullen"** (one word; Rufin VanRullen), in text and reference list | fix both |
| S16 | `:560` vs `:590` | Consistent in fact — `:560`'s spreadsheet-sum qualifier pins the component sense and `:590` reconciles via §4.2.1 — but quotable against each other. | forward pointer at `:560`: *"in the component sense distinguished in Section 4.2.3"* |
| S17 | `:658` | Uncited mechanism: *"as metabolic resources — particularly neurotransmitter pools — are depleted"*. | hedge or cite the synaptic-homeostasis literature |

**Verification pointers (not findings):** Corlett et al. 2011 (`:690`) — reference exists, characterisation
plausible, not independently verified. Sela et al. 2009 / Courtiol & Wilson 2015 (`:640`) — "confirms" is
strong for a lesion case series; consider "indicates".

### Confirmed clean in this range

The approved free-will formulation is present verbatim at `:568`, the stand-in mechanism (hunger → empty
stomach) at `:568`, and the approved "no missing cause" wording at `:570`; the scope guard is stated at
`:564` and `:572` — **the sole breach is B1.** Price-never-barrier discipline holds throughout §4.2.4/§4.4
(`:598`, `:600`, `:616`, `:632`); the §4.2.3 necessity claim is correctly scoped as
constitutive-not-competitive (`:588`). **Pattern 32 intact** — holography confined to the implicit models,
explicit models expressly excluded as *"processes, not stored structures"* (`:664`–`:666`). No seizure
claims in range. Table 4's psychedelic row now draws the slightly-past-critical vs runaway distinction —
prior cross-section finding closed. **The readout-vs-causal-power distinction is drawn correctly**: `:590`
matches MG's dashboard ruling exactly — component of a causal-power system when read; causal power only
where the value issues in further simulation. Zero hits file-wide for "load-bearing" and sentence-initial
"Crucially,"/"Importantly,"; no "sampling" as an FMT mechanism; no "gate/gating" for conscious-content
update in range.

---

## Reviewer 4 — lines 696–894 (§6 Explanatory Range, §7 Comparative Analysis)

**Verdict: the fold-in held — publishable after four small blockers, all one-sentence repairs, three of them
survivors of sweeps this paper has already ruled on.**

### Blockers

**B1 — `:877` — *"the criticality prerequisite"*.** See the headline section above. Residual site of the
criticality-is-an-effect sweep.
**Repair:** *"…or the open-ended-computation requirement (Class 4, with criticality as its neural
signature)"*.

**B2 — `:771` — *"The theory's commitments — continuum (not binary), substrate independence, criticality
threshold — predict a gradient…"*.** Same sweep, second survivor. Listing "criticality threshold" among the
theory's *commitments* restates criticality as a requirement, contradicting `:174` in the same manuscript.
Misconception-registry #3 names "criticality threshold" as the seductive misread.
**Repair:** *"continuum (not binary), substrate independence, and the computational-regime requirement
(Section 3.7)"*.
⚠ **Secondary in the same sentence:** *"continuum (not binary)"* sits ten lines above `:781`'s *"principled
boundary… systems below self-referential closure lack phenomenal experience"* and against `:879`'s *"single
binary criterion"*. The binary-floor-plus-graded-levels structure is coherent, but as worded the two are
quotable against each other — add *"above the closure floor"* or equivalent.

**B3 — `:869` — the corvid argument against biological computationalism does not follow.**
> *"Biological computationalism (Milinkovic & Aru, 2025) argues that consciousness requires specifically
> biological computation… The existence of conscious corvids with non-cortical brain architecture… favors
> substrate independence."*

**Corvids are biological.** Their consciousness is fully compatible with the rival's thesis and cannot count
against it; the corvid case supports independence from *cortical lamination*, not from *biology* — and the
paper's own §6.4 (`:777`) states it correctly as an anti-laminar argument. Also *"the existence of conscious
corvids"* asserts as fact what `:773` and `:777` carefully treat as an inferential test case.
**Repair:** *"Corvid consciousness, if granted (§6.4), shows the architecture need not be cortical; it does
not by itself decide the biological-computation question, which the theory treats as the empirical
prediction stated above (§8.7)."*

**B4 — `:839` vs `:891` — the paper contradicts itself on its own weakness, inside one section.**
`:839`: *"Mathematical formalization… represents an open opportunity for the theory's development, **not a
structural weakness**."* `:891`: *"The theory's **primary disadvantage** is the absence of mathematical
formalization."* A referee quotes one against the other in a sentence. `:891` — with §9's Open Question 2
and `:1058`'s *"qualitative… partly by design"* — is the honest, established position.
**Repair:** end `:839` with *"…remains an open task, recorded as such in Section 9"* and delete *"not a
structural weakness."*

### Should-fix

| # | line | what is wrong | repair |
|---|---|---|---|
| S1 | `:749` | *"the thalamocortical breakdown reported by Boly et al. (2012) is the signature the architecture **predicts rather than one it accommodates afterward**"* — Boly 2012 predates every statement of the architecture; the clause denies the retrodiction that chronologically occurred. Strongest instance of the retrodiction-as-prediction class. | *"is the signature the architecture entails rather than one fitted to it — a retrodiction, but a forced one."* |
| S2 | `:757` (DID) | The null attributed to the sociocognitive model — *"should not follow a self-referential gradient"* — is **FMT's auxiliary assumption**, not anything Lilienfeld/Lynn assert; enactment demonstrably modulates self-referential networks too. | present the gradient-null as the theory's operationalization; name motivated-simulator controls (Reinders et al., 2012) as the discriminating design |
| S3 | `:726`–`:733` | The dose-ordered visual progression (V1 phosphenes → form constants → figures → full scenes) is asserted as established with only Klüver (1966) for form constants; the **ordering itself carries no citation**. | add a citation or hedge to *"characteristically reported progression"* |
| S4 | `:829`/`:836` (Table 5, Combination row) | §2.6 is "Combination **and Emergence**", yet GNW/HOT/PP/AST/RPT get flat n/a while FMT alone is scored ◐ on the Emergence half. The n/a rationale applies to those non-panpsychist rivals exactly as to FMT. **The centrepiece table applies its own rule asymmetrically in FMT's favour.** | score the rivals' emergence halves too, or give FMT n/a and move the emergence credit to prose |
| S5 | `:839` | *"**provably** intractable for realistic systems (Aaronson, 2014)"* — Aaronson argues infeasibility and absurd Φ-values for expander graphs; he proves no intractability theorem. | drop "provably" (`:843`'s form is fine) |
| S6 | `:875` | *"multiple independent frameworks converge on **self-referential closure at criticality**"* — two sentences after stating the closure+criticality *combination* is what *"neither RIFT nor Beautiful Loop fully replicate."* Likely over-attributes a criticality commitment to Laukkonen et al. (2025). | *"converge on self-referential closure — in RIFT's case at criticality —"*. Carry-over: the audit's bibliographic check on Bieberich 2026's nonstandard DOI is still open, and *"25 years of independent development"* was never verified |
| S7 | `:855` (RPT) | *"silent on the Hard Problem and limited in scope to visual consciousness"* — Lamme identifies phenomenality with localized recurrent processing and would contest "silent"; `:814` promises contested ratings are noted, and this one is not. "Limited to visual" overstates: the evidence base is visual, the principle general. | *"developed primarily in the visual domain; proponents would contest the Hard-Problem rating…"* |
| S8 | `:853` (AST) | *"AST is deflationary about phenomenality"* — Graziano has repeatedly resisted the deflationary/illusionist label. | *"deflationary about phenomenality as standardly conceived — a characterization its proponent qualifies."* |
| S9 | `:788` (cetacean row) | *"one hemisphere maintains waking-level **criticality** while the other enters subcritical rest (Mukhametov, Supin, & Polyakova, 1977)"* — a 1977 EEG study cannot carry a criticality finding; the audit already noted this is FMT's gloss. | move the gloss outside the cited clause |
| S10 | `:883`–`:887` (§7.4 list) | Items 3 and 4 overlap — the psychedelic-anosognosia connection appears in both — and item 3's *"Unique mechanism"* sits awkwardly beside the paper's own concessions at `:739` and `:889`. | merge 3+4; let the specificity carry the claim instead of "unique" |
| S11 | `:871` | Clustering FMT *"with IIT on the structural/intrinsic side rather than with functionalism"* is quotable against §4.4's substrate independence. | one clause: the structure FMT appeals to lives at the virtual level and is multiply realizable |
| S12 | `:751`/`:753` | Cotard's (*"distorted interoceptive input produces 'I am dead'"*) is uncited; *"the substrate registers the paralysis"* in anosognosia is asserted where supporting evidence exists and would strengthen it (Fotopoulou et al., 2010). | add citations or mark both explicitly as the theory's account |

### Confirmed clean in this range

**§6.0 does its job:** each of the three mechanisms is genuinely *derived* from the three principles —
redirection from P2+P3+the ESM's input-driven character, permeability forced by generation-from-substrate
with variability as default, forking from P1 — not asserted; source distinguishability is correctly framed
as a requirement and engages Johnson et al. (1993) on the right side of the source-monitoring literature;
all four Dijkstra citations exist and match their claims; §6.0 heading depth is fixed.
**All eight §2 requirements are scored in Table 5**, the footnote apparatus cashes out every non-● FMT cell,
the Hard-Problem ◐ honours the standing `:298` ruling, and **the Introduction's addresses-all-eight claim is
cashed out as ruled — not flagged.**
**Rival characterisations are in materially good shape** — the Frankish inversion, the "consciousness = Φ"
mischaracterisation, the fabricated Hohwy & Seth quote (now the genuine verbatim fragment *"PP is not itself
a theory of consciousness"*), and the backwards unfolding argument are all correctly repaired; IIT's
interventional-TPM reply is stated; COGITATE is described evenhandedly; PP/GNW/HOT/AST comparisons follow the
"FMT additionally does X" form. **The unfolding passage (`:859`–`:865`) matches the MG-approved commitment
exactly, and every figure in it checks against §8.9 verbatim — no new numbers imported.**
Prior blockers and audit findings in range all held: Katlowitz recall-scoping (`:747`), the Hengen & Shew vs
ConCrit credit split (`:839`), the criticality-table species repair with the Kanders out (`:789`), magpie
failed-replications (`:787`), the salvia evidence-class hedge (`:737`), Dresler case-study and Voss
replication hedges (`:767`), Passos-Ferreira expert-opinion framing (`:794`), the Phillips blindsight caveat
(`:800`).

---

## Reviewer 5 — lines 895–1113 (§8 Predictions, §9 Open Questions, §10 Discussion, §11 Conclusion)

⛔ **DIED on credits before producing any findings.** It had read the range and was moving to targeted
cross-checks — the "prerequisite" pattern sweep, §3.7.1's hierarchy order, §5.1's correlation-length
wording, banned-phrase sweeps and dangling-citation checks — when it terminated.

**Must be re-run.** The commissioned focus was: §8.9's cost/efficiency arithmetic (a previous version
claimed *"roughly an order of magnitude for each additional subsystem"* over 195 / 2159 / 6048, where the
second step is a factor of 2.8 — crucible has this open as a **P0** against the published master); whether
each prediction names what would falsify it; whether §9's open questions are honest rather than decorative;
whether the Conclusion claims more than §§3–8 delivered; and no crucible-sourced figure quoted past 3
decimal places.

---

## Reviewer 6 — whole-paper cross-section pass

⛔ **DIED on credits.** It returned one partial lead before terminating; **that lead has been verified by
hand, is confirmed, and is the headline finding above.** Everything else the pass was commissioned for is
**not done**: the remaining half-applied-repair sweeps, cross-section contradictions, numbers disagreeing
between appearances, the §2→§6 requirement-scoring audit, terminology drift, and structural problems.

⚠ **Note for the re-run:** the two section reviewers that *did* complete found cross-section defects the
section passes were not scoped for — `:839` vs `:891`, `:630` vs `:999`, `:564` vs `:576`, `:86` vs `:834`.
That is four cross-section contradictions found incidentally, which suggests the dedicated pass will find
more. **It is the highest-value of the three re-runs.**

---

## Re-run order at 23:00

1. **Reviewer 6, the cross-section pass** — highest value, and four incidental finds suggest a rich seam.
2. **Reviewer 2, §3** — the theoretical core, a quarter of the paper, entirely unreviewed.
3. **Reviewer 5, §8–11** — carries the P0 arithmetic check crucible raised against the published master.

The three completed reviews do **not** need re-running. Their findings are recorded above in full.
