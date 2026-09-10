<!-- Action: act -->
<!-- Tracked-by: AIW-236 -->
# FMT v15 — the second Fable review, COMPLETED (S311, 2026-08-26)

**Completes `docs/reviews/2026-08-25-fmt-v15-fable-review-2.md`**, which ran half its agents before Fable
credits ran out. MG parked it with *"wait for 23:00 to continue"*. Fable credits confirmed restored by a
one-word probe before commissioning.

**This run: seven Fable agents.** The three the handover ordered (cross-section pass, §3, §8–11) plus four
more commissioned after MG's *"we have tokens to burn — use fable and parallelization a lot"*: a
rival-theory referee panel, a citation audit of the two unreviewed ranges, a full `.tex` content-equivalence
audit, and a prose-register pass.

Every agent was handed all three prior review records and the two non-litigable rulings (criticality is an
**effect**; *"we DO address all"* is ruled and rejected as a finding). No agent tried to re-open either.

⚠ **Nothing here has been folded in yet.** The manuscript and `.tex` are untouched — last commit on them is
`aef1bfe1` (S309). The whole review lands as ONE pattern-swept pass, never by line number.

---

## Gates re-run in the main loop this session (banked — do not re-run)

| gate | result |
|---|---|
| `git-sync-check.sh --pull` (private) | up to date |
| `publish_gate.py 10.5281/zenodo.18669891` | **BLOCKED on the same four**, re-derived from scratch, identical for the third time: `PUBLISH_GATE_ACK=AIW-229,AIW-210,AIW-193,AIW-156` |
| `pytest scripts/test_content_integrity.py` | **32 passed** |
| `pytest scripts/` (full suite) | **432 passed, 6 skipped** |
| `verify_references.py --check` | **OK — 724 references (554 verified, 170 verified-manual), 349 printed bibtex citations matched** |

### The three greps that timed out at S310 — re-run here, all three now banked

- **Capability-barrier language: CLEAN on the banned axes.** No axis-(A) (implicit/unconscious vs
  explicit/conscious) or axis-(B) (self-model vs world-model) barrier claims survive. The hits at `:204`,
  `:233`, `:255`, `:506`, `:513` are all within-architecture derivations (the ISM is needed to generate the
  ESM; Class 4 is needed for open-ended computation), which are licensed.
- **Localized-concept language: CLEAN, and the paper actively pre-empts it.** `:206` — *"not a claim about
  spatial organization in the brain — the models are functionally distinct processes, not anatomically
  localized regions"*; `:652` — *"features encoded across the full network rather than localized in specific
  neurons"*; `:670` — Lashley, memory is not localized; `:1021` — *"not the focal excision of a localized
  module, which the theory does not posit"*.
  ⇒ **crucible's `cru115` carving sweep does NOT bite this paper.** The inbox item's flagged exposure is not
  realised in the manuscript. (It remains a live constraint on any *future* figure or sentence.)
- **Seizure route: compliant at `:472` and `:1066`; ONE borderline at `:486`.** `:1066` is route-independent
  as required, names both directions, scopes Meisel and Truccolo to focal seizures, labels the extrapolation
  to generalized seizures, and commits to loss of Class 4 rather than to a branching-ratio value. `:486`
  asserts *"Hypersynchronous, low-complexity dynamics are Class 2/3, not Class 4"* — a Wolfram-class
  assignment for ictal dynamics that the literature does not settle, and which `didactic-patterns.md`
  specifically bans ("do not write ordered/synchronous Class-2"). The surrounding sentence already does the
  work without it. → **should-fix**.

---

## Agent 1 — the dedicated whole-paper cross-section pass

**Verdict: the criticality-is-an-effect repair is still only half applied — six MORE sites state criticality
as part of the theory's definition, two of them contradicting §8.7 one section away — and the paper's central
"explicit models are processes, not stored structures" claim is flatly contradicted once, in §3.7.2, in both
files.**

⭐ **This is the half-applied-repair disease for the FOURTH time, and it is now clear why line-number sweeps
keep missing it: the surviving sites are a SECOND STRATUM.** The twelve repaired sites called criticality a
prerequisite *by name*. These six put criticality inside the theory's *definition or criterion* without using
the banned words, so every grep written against the old vocabulary passed them.

### BLOCKERS

**B1 — `:506` (`paper.tex:652`) — the explicit models are called "stored in the substrate", contradicting the
paper's central ontological claim at four sites.**

> `:506`: *"Consciousness arises from the interplay between the automaton's dynamics and the models **stored
> in the substrate — the IWM, ISM, EWM, and ESM**."*

Against `:223` (the ESM is *"a transient process… constituted at the computational level rather than stored
in the substrate"*), `:229` (*"The explicit models have no permanent physical substrate of their own"*),
`:666` (*"they are processes, not stored structures"*) and Table 1 at `:170` (*"no permanent physical
substrate"*).

The real/virtual split — the paper's whole Hard-Problem machinery — rests on exactly this asymmetry. §3.7.2
asserts its negation for the EWM and ESM by name. A referee quotes `:506` against `:229` in one sentence.
**Never found before because §3 is the range whose reviewer died twice.**

**Repair:** *"…the interplay between the automaton's dynamics and the models it carries — the implicit models
(IWM, ISM) stored in the substrate and the explicit models (EWM, ESM) generated from them."*

**B2 — six more criticality-as-definition sites.**

The canonical wording is `:174`; it is restated correctly at `:441`, `:476`, `:513`, `:548`, `:624`, `:977`,
`:1037`. These contradict it:

| site | `.tex` | quoted text | why it violates |
|---|---|---|---|
| `:626` | `:795` | *"The theory's **architectural requirements** — persistent models, dynamic simulation, self-referential closure, **criticality** — are functional specifications"* | criticality named in a list of the theory's requirements — same defect class as the known `:771`/`:901`/`:1058`. **The sentence contradicts its own footnote**, which states the correct form (*"self-referential simulation in the Class 4 regime"*). |
| `:869` | `:1097` | *"**artificial substrates** implementing the four-model architecture **at criticality** should produce consciousness"* | contradicts `:476` (*"across substrates the individual criticality statistics need not co-occur; the requirement is then better stated as Class 4 capability"*), `:480`, and §8.7's own `:977`. |
| `:987` | `:1236` | build-a-machine spec: *"four models along two axes … **operating at criticality** on a substrate of sufficient complexity"* | §8.8 contradicts §8.7 one section above (`:977`) and §10.1 (`:1037`), both of which state the same spec correctly. |
| `:845` | `:1070` | *"consciousness **is** the ongoing self-referential updating — **sustained at criticality** — … FMT locates it in that running, **substrate-neutral**… updating"* | a *constitutive identity* statement that embeds a neural-tissue signature, and calls the same updating substrate-neutral in the same paragraph. Both cannot hold on the paper's own `:476`. |
| `:875` | `:1103` | *"the **combination of self-referential closure with criticality**…"*, *"converge on self-referential closure **at criticality** as constitutive of consciousness"* | names criticality as a defining element of the theory's distinctive combination. Separate from Reviewer 4's banked S6, which flagged only the Laukkonen attribution. |
| `:843` | `:1068` | *"it characterizes consciousness through the functional organization of implicit and explicit models **operating at criticality**"* | a definitional contrast with IIT in a substrate-general context, not a biological-signature claim. |

**Uniform repair:** replace with *"in the Class 4 regime"* or *"the open-ended-computation requirement (Class
4, with near-criticality as its neural signature)"* — the form the paper already uses at `:548`, `:624`,
`:977`, `:1037`.

*Borderline, flagged not ruled (biological context arguably licenses the signature):* `:777`, `:857` (×2),
`:604`. Cheap to sweep alongside the six.

**B3 — `:885` and `:1047` (`paper.tex:1116`, `:1308`) — "ESM-network localization" is the exact framing `:945`
disavows as a pitfall.**

`:945` was written to pre-empt naive modularism: *"formulated in terms of representational dissimilarity
**rather than anatomical localization to avoid the naive-modularism pitfall of equating the ESM with any
specific brain network**… not activation of a named region."* Two summary sites then re-introduce the banned
frame by name — `:885` *"ESM-network localization in DID (Prediction 3)"* and `:1047` *"Test ESM-network
localization in DID"*. Summaries are what a referee reads first, and naive modularism is this paper's
costliest external failure mode.

**Repair, both sites:** *"the self-referential representational gradient across alter states in DID
(Prediction 3)"*.

**B4 — `:1080` (`paper.tex:1347`) vs `:929` — the Conclusion claims Prediction 1 is "distinctive" while §8.2
concedes its coarse version is one REBUS step away.**

`:929`: *"the coarse version of this prediction is derivable from REBUS in one step. FMT's differential
content is the fine structure…"* — but `:1080` grants the REBUS caveat for P2 and withholds it for P1.
Hedged-in-body / flat-in-conclusion, the same defect shape as the already-closed gamma and Kawakita cases.
**A desk rejection for "predictions too general" is already on this paper's record.**

**Repair:** *"Predictions 3 and 4 are distinctive to the Four-Model Theory; Predictions 1 and 2 are
distinctive in their fine structure (dose profile, lesion-type boundary condition, modality-specific
tracking), their coarse forms being derivable from REBUS…"*

### SHOULD-FIX

- **S1 — `:443` vs `:997`.** §3.7 says the criticality dependence should appear *"only on a task carrying
  genuine multi-step counterfactual depth. No task of that depth has yet been built"* — while §8.9 reports the
  band's advantage already appearing on medium and hard temporal-parity tasks, demand-gating *"confirmed in
  six independent model settings"*. The reconciliation (lag-gap *demand* ≠ counterfactual *depth*) exists at
  `:1001` but is never drawn at `:443`, so `:443`'s "only" is falsified by the paper's own §8.9.
- **S2 — `:441` vs Table 4 (`:681`–`:682`).** `:441` accommodates *"a near-critical cortex engaged in heavy
  unconscious modelling — as in some sleep phases"*, but no row of the state table is simultaneously
  near-critical and unconscious (REM = near-critical, consciousness degraded-but-present; NREM =
  predominantly subcritical). Cite the actual case or drop the clause.
- **S3 — `:294` vs `:506`/`:54`.** "Cortical automaton" is glossed with three incompatible referents across
  `:294` (it *is* the simulation), `:498`/`:1025` (it *constitutes* the models) and `:54`/`:506` (it is *mere
  medium*). The medium reading is the one the rest of the paper needs.
- **S4 — the "criticality commitment" family is FAR larger than the four sites the handover listed.** Full
  enumeration for the MG ruling: `:470`, `:472`, `:480`, `:839`, `:873`, `:889`, `:903` (×2), `:905`, `:907`,
  `:1080`, `:1082` (×2) — **13 instances on 11 lines**, plus the near-variant *"Class 4 commitment"* at
  `:907`, which is the correct form and could serve as the template. ⇒ **The handover's four-site list was
  incomplete by nine.**
- **S5 — `:1100` (`paper.tex:1367`) Data Availability vs §8.9.** *"No new data were generated. Section 9
  reports a secondary analysis…"* covers §9 only, while §8.9 reports eight quantitative results sourced to the
  companion. A checking editor will query it.
- **S6 — `:194` vs `:441`/`:1066`.** Table 1b's falsifier is *"convergently **subcritical** dynamics"*, but
  `:1066` makes supercritical dynamics equally incompatible with consciousness, so robust consciousness in a
  supercritical cortex would also falsify. Align to *"convergently off-critical (subcritical or
  supercritical)"*.

### VERIFIED CLEAN by this agent — swept by pattern across the whole file, do not re-check

Hengen & Shew scoping (all 11 sites, family closed) · Kawakita group-level (all sites incl. the S309 `:1074`
survivor, family closed) · Katlowitz sedation (zero hits in `.md` and `.tex`, family closed) · "three
principles" (`:17`, `:70`, `:134`, `:702`; zero "five principles") · "four modules" (only `:15`'s deliberate
pre-emption) · "anterior prefrontal"/"anterior PFC" (zero) · banned exact string "the criticality requirement"
(zero) · seizure route (`:472`, `:486`, `:1066` only) · localized-concept phrasing (zero grandmother/hub hits)
· every S307 citation-audit repair held (Doyon gone; "Siclari et al. (2021)" gone; Schartner 15–20% gone;
Hohwy–Seth quote genuine; Timmermann is DMT; animal-table species Shew 2015 turtle / Hahn 2010 cat; Pinto at
both `:666` and `:915`; Li 2010 single-case; Benjamin & Kording relocated with rat-labelled Oorschot counts;
Rouault 22% and Rahnev triples gone) · prior cross-section findings re-verified closed (five-system hierarchy
order, P4 testability, Table 4 psychedelic row, `:206`/`:215` orthogonality, `:280`/`:372` recoverability, ToM
pointer now §4.2, "four nested models" gone, closure-falsified-five-times qualified, τ_syn clause).

### ⭐ §8.9 arithmetic — the crucible P0 is ALREADY REPAIRED in the current text

Verified in the manuscript: **2159/195 = elevenfold ✓; 6048/2159 = under three ✓; 74.0/14.0 = 5.3× ✓;
71.5/12.0 = 6.0× ✓; `:863` ↔ `:999` figures identical ✓; the endpoint-vs-paired R² discrepancy now explicitly
glossed ✓.**

⇒ **The crucible inbox item's P0 — *"the advantage grows by roughly an order of magnitude for each additional
subsystem"* over 195 / 2159 / 6048 — describes the PUBLISHED master, not the working manuscript. The working
text no longer says it.** The item still needs closing against the *published* Zenodo PDF, which is what
`AIW-210` already covers (source fixed, shipped PDF stale, redeposit waits for the version bump).

### `.tex` mirror — no drift beyond the shared defects

All sampled recent repairs propagated (Data Availability, Katlowitz, both Pinto sites, animal-table species,
both Kawakita sites, τ_syn clause, R²-normalisation gloss, unfolding-argument figures, Hohwy–Seth quote).
**The `.tex` mirrors the `.md` faithfully — which means every blocker above must be fixed in BOTH files:**
B1 → `paper.tex:652`; B2 → `:795`, `:1097`, `:1236`, `:1070`, `:1103`, `:1068`; B3 → `:1116`, `:1308`;
B4 → `:1347`. The four known criticality sites remain at `paper.tex:970`, `:1105`, `:1138`, `:1322`, plus
`:131` for the known `:86` IIT blocker and `:799` for the known `:630`.

---

## Agent 2 — §3, lines 132–539 (the theoretical core, previously unreviewed twice over)

**Verdict: §3 is in better shape than its unreviewed status suggested — every ruling and prior repair held — but it carries three blockers, and two of them are the paper contradicting its own axis definitions in the theoretical core.**

### BLOCKERS

**B5 — `:206` (`paper.tex:292`) — the implicit models are called "processes", violating the structure/process axis the section itself defines.**
> *"the models are functionally distinct **processes**, not anatomically localized regions"*

"The models" is all four. Against `:227` (*"inscribed in structure rather than in any running process"*), `:229` (explicit models are *"generated processes"*), `:251`. `:206` flattens both sides into "processes".
**Repair:** *"…the four kinds are functionally distinguished — two stored as structure, two generated as processes — not anatomically localized regions."*
⚠ **Note the collision:** `:206`'s *other* half is what makes the paper clean on the localized-concept sweep. The repair must preserve the anti-localization clause.

**B6 — `:294` and `:498` vs `:506` — "cortical automaton" is content in two places and medium in the third.**
`:294` equates automaton = the virtual self-simulation; `:498` says its pattern *"constitutes the explicit models"*; `:506` says it is *"the computational medium… necessary infrastructure, not the program itself"*. **This is the in-range root of the §9 conflict already carried at `:1019`** — repairing §9 without these two leaves the contradiction standing in the core.
**Repair:** `:498` → *"the computational level realized by the cortical automaton's dynamics (§3.7.2), whose organized, model-shaped patterns are the explicit models"*; `:294` → drop the apposition.
⇒ **Merges with cross-section S3 and B1 — one repair, four sites (`:294`, `:498`, `:506`, `:1019`/`:1025`).**

**B7 ⭐ — `:518`/`:520` — the third leg of the computational prerequisite is named "evolutionary forcing", which excludes artificial systems BY DEFINITION.**
> `:518`: *"a three-part condition — capability, free instantiation, and **evolutionary forcing** — and the laptop fails the third."*

A system built to spec (§8.7, §8.9) has no evolution, so **the paper's own AC programme fails its own prerequisite by definition.** Directly quotable against `:144` (*"biological or artificial"*), §4.4 substrate independence, and §8.9's own framing paragraph, which invokes the trichotomy verbatim. The text already contains the correct condition at `:522` — *"in the service of autonomous self-modeling"* — **the label misnames it.**
**Repair:** rename the leg *"autonomous recruitment"*: *"…in biology supplied by evolutionary forcing — selection drives the system toward criticality and holds it there — in an artificial substrate by design (§8.7)."* Apply at `:518`, `:520`, `:522` and the §8.9 trichotomy reference.

### SHOULD-FIX (§3)

| # | line | defect | repair |
|---|---|---|---|
| S7 | `:514` | *"**Above criticality** but without the architecture, there is complex dynamics"* — "above criticality" literally means supercritical, which the paper says precludes consciousness. Plus subject-verb. | *"In the Class 4 regime but without the architecture, there are complex dynamics but no consciousness."* |
| S8 | `:255` | *"through their **projections** into the explicit models"* — a neuroscientist reads axonal projections between two populations, the exact two-population misread the axis ruling bans. | *"…through what the generation draws from them into the explicit models."* |
| S9 | `:338`, `:340` | **"the self region"** ×3 — *"efferent disconnection of the self region"*. In a biological brain there is no circumscribed self region; the paragraph opens with dolphins, so it reads as proposing invasive dolphin surgery. ⚠ **This IS the crucible `cru115` exposure, and it is the only site in the paper where it lands.** | scope explicitly: *"the region implementing the self-model in a system built to the theory's specification (§8.7)"* |
| S10 | `:488` | LLMs hold wide contexts *"with **no return path**"* — (a) "return" naming the mechanism; (b) an AI-literate referee objects that autoregression *is* a return path. | *"…with no operation that closes the modelling on itself — autoregressive re-entry carries output back into the context, but no self-model enters the update of what is modelled."* |
| S11 | `:352` | *"nothing in it **models the carrying**"* — over-absolute; the paper's own Stage-2 monitor (`:310`) can log state history without closure. | *"…but nothing in it represents the carried state as the recent past of a perspective, so no 'now' is constructed."* |
| S12 | `:366` | *"deflationary accounts (Graziano, 2024)"* — Graziano resists the label. Same exposure as accepted R4-S8 at `:853`. | *"…nor with accounts on which the phenomenal is an attribution the system makes about itself"* |
| S13 | `:280` vs `:372` | *"not recoverable by aggregating transistor-level descriptions"* vs *"in principle reconstructable from a sufficiently detailed substrate description"*. Reconciliation is drawn but `:280` names the decompiler's exact input. | *"not recoverable within transistor-level vocabulary, however exhaustive the aggregation."* |
| S14 | `:522` | *"the empirical criticality literature that **converged** roughly a decade later"* — the literature began 2003; the paper's own Table 3 says so. Only the *consolidation* is a decade later. | *"the large-scale consolidation of the empirical criticality literature roughly a decade later…"* |
| S15 | `:231` | Squire 2004 cited for a declarative→procedural **shift**; Squire documents the *taxonomy*, not a conveyor. | cite Squire for the distinction; source the automatization claim separately |
| S16 | `:433` | *"requires **exactly one thing**"* — quotable against §3.7.3's own two-thresholds structure (a seizure abolishes experience via the regime, not the channel). | *"is achieved whenever the channel fails while the wired layer stands"* |
| S17 | `:225` | *"an **effectively uncountable** number of overlapping models"* — uncountable is a cardinality term. | *"innumerable"* |

### §3 VERIFIED CLEAN — do not re-check

**Closure material is exemplary** — `:423` is exactly the commissioned form: *"What the narrow path buys is efficiency; what its output, fed back into the world-model's update rule, buys is self-consistency… only the second is closure."* No site attributes efficiency to the feedback or self-consistency to the narrowness. · **Closure-not-return**: no surviving use of "return" as the property name (only `:488` needs work, and for the autoregression exposure). · **The §3.4.3 cut holds** — marked argued-not-derived at `:138`, `:274`, `:304`, `:334`; pattern 15 does NOT appear; the person-format triad does NOT appear. · **The *erweitert* ladder** (`:386`–`:398`) is pure self-recursion at every rung; other-agent modelling routed through redeployment, consistent with pattern 38. · **Barrier language clean on all three axes.** · **Three principles** at `:134`; consequence list correct at `:140`. · **Criticality-as-effect took throughout §3** (`:136`, `:174`, `:194`, `:439`, `:441`, `:453`, `:476`, `:478`, `:486`, `:513`). · Numbers all consistent with the audit's verified set (PCI 0.31, σ≈0.98, DFA 0.6–0.9, τ≈−3/2, 7±2/4±1, 2kN vs N²). · **Prose register: zero hits in range** for load-bearing, bite, sentence-initial Crucially/Importantly, empty-praise predicates.

---

## Agent 3 — §8–11, lines 895–1113 (previously unreviewed)

### ⛔ THE P0 IS RESOLVED AT SOURCE — close it, do not repair it

The phrase *"by roughly an order of magnitude for each additional subsystem the loop spans"* **no longer exists anywhere in the `.md` or the `.tex`.** It was repaired in commit **`3ec61acb`** (2026-08-23, *"AIW-216/217: two §8.9 defects repaired in the published master"*), whose message does the same arithmetic. Current text at `:999`:

> *"— 195, 2159, and 6048 synapses for one, two, and three subsystems at 84 units each, **an elevenfold step and then a further factor of under three** — monotonically at every substrate size tested"*

Arithmetic re-done independently by two agents: 2159/195 = 11.07 ✓, 6048/2159 = 2.80 ✓. Mirrored at `paper.tex:1250`.
⇒ **Crucible's P0 closes with a pointer to `3ec61acb`.** It was open against the *published* master, which `AIW-210` already covers (source fixed, shipped PDF stale, redeposit waits for the version bump).

### BLOCKERS

**B8 — `:981` (`paper.tex:1228`) — stale prediction count, factually wrong about the paper's own structure.**
> *"This implication is listed separately from **Predictions 1–4**…"* — the paper has **five** predictions (§8.2–8.6; `:897` and `:1080` both say five). A leftover from the four-prediction era, in a paper with a desk rejection on prediction framing already on record. **Fix: "Predictions 1–5", both files.**

**B9 — `:1082` — audit finding 9's repair applied at `:470` but NOT in the Conclusion. Hengen & Shew jointly credited with the criticality–consciousness account again.**
> *"Hengen and Shew's (2025) meta-analysis… and Algom and Shriki's (2026) ConCrit framework — consolidated the near-criticality setpoint **and extended it into an explicit criticality-consciousness account**."*

The joint subject makes H&S a co-author of the extension. The repaired site `:470` carries the scoping the Conclusion lacks: *"and, **in ConCrit's case**, extended it…"*. **The half-applied-repair disease at a site both prior sweeps missed.** Fix: insert *"in ConCrit's case,"* mirroring `:470` verbatim.

**B10 — `:1080` and `:1046` — the REBUS concession is not propagated to §10.2 or the Conclusion.** *(= cross-section B4; two independent routes.)* `:1046` additionally calls P2 *"uniquely generated"* against `:939`'s *"PP (REBUS) generates a related prediction"* and `:1080`'s own *"partially derivable"*.
**Fix `:1080`:** *"Predictions 3 and 4 are distinctive to the Four-Model Theory; Predictions 1 and 2 are coarsely derivable from REBUS, with FMT's differential content in their fine structure (§§8.2–8.3)…"*
**Fix `:1046`:** *"…the modality-specific input tracking is generated by the redirectable ESM mechanism, where REBUS predicts only general input-driven updating (§8.3)."*

**B11 ⭐⭐ — `:1021` — the second arm of the claimed double dissociation is an uncited empirical assertion.** *(Found independently by THREE agents: §8–11, the rival panel, and the citation audit. The strongest-confirmed finding in this review.)*
> *"Conversely, manipulations of stimulus difficulty within subjects raise first-order sensitivity substantially while leaving metacognitive efficiency essentially unchanged."*

Audit finding 8 removed the fabricated Rahnev (2013) numbers **and left the sentence they propped up standing with no source at all** — while the paragraph builds on it: *"Together these assemble… the two arms of a double dissociation."* One arm rests on Rouault 2018 + Rahnev 2020 (cited, verified); the other rests on nothing — in a manuscript whose citation audit's headline defect class was exactly this, in the section metacognition researchers (Fleming, Rouault — the likely referees) read closest. The Data Availability statement at `:1100` also promises §9's sources are *"cited there."*
**Fix:** cite a real within-subject difficulty result with stable M-ratio; or declare it as the author's own reanalysis of a *named* Confidence Database dataset with the numbers; or delete it and rescope to the decoupling Rouault + Rahnev actually carry.

**B12 — `:977`, `:989`, `:1060`, `:1088` — the "difference in kind / qualitatively obvious" family is the BARRIER form of a claim §8.9 states as a PRICE.** ⚠ **NEEDS MG SIGN-OFF — the two-lane rule is his.**
`:993` states *"no input-output capability is closed to a feedforward architecture given unbounded width and data"*, and `:616` states the rule outright: *"Stated as a barrier it is false; stated as a price it is both true."* `:1088` already uses the licensed form (*"a matter of cost, not of possibility"*); `:989`'s *"a difference in kind, not merely in degree"* carries no budget anchor and contradicts it.
**Proposed (keep the ontological kind-claim, budget-anchor the interactional one), `:989`:** *"…the difference between interacting with a conscious artificial system and any current AI should be readily apparent to human observers — not because imitation is impossible in principle (§8.9 concedes it is not), but because sustaining it without the architecture carries a cost no current system pays (§4.2)."*

**B13 — ⚠ NEEDS MG RULING, DO NOT FIX — Prediction 4's discontinuity commitment conflicts with a recorded ruling in `prediction-framing.md`.**
`prediction-framing.md`, *Theoretical corrections (Session 204, user)* #2: *"No sharp developmental discontinuity … practically unmeasurable as a sharp transition. **Same applies to lucid dream onset.** Don't impose digital thinking onto analog processes."*
P4 commits to the opposite: `:953` *"the structural signature of a phase transition — critical slowing beforehand, **discontinuous onset** — rather than a gradual ramp"*; `:955` *"a threshold, not a gradient."*
**Two readings:** (a) P4 violates a standing ruling; (b) **the ruling is stale** — Li et al. (2025), cited at `:911`, has since demonstrated a measurable bifurcation with critical slowing at ordinary sleep onset, which is precisely the "unmeasurable" objection failing empirically, and MG has approved P4 through several review rounds since S204.
Same site, separable: `:955` *"Lucid dreaming **occurs when** the substrate reaches sufficient criticality"* is sufficiency-shaped; *"becomes possible when"* is the compliant form regardless of how the discontinuity question is ruled.

### §8–11 SHOULD-FIX

`:935` *"users **reliably** report"* (salvia) — uncited strength; §6.1 `:737` carries the hedge this drops *(also found by the citation audit)* · `:943` *"the direction and **magnitude** of the gap, **not the absolute values**"* — a gap's magnitude is a function of the absolute values just disclaimed · `:907` *"predating the consciousness-criticality program"* — Carhart-Harris 2014 is one, and the paper lists it at `:903`/`:1082` as already underway pre-2015 → *"independently of"* · `:999` **three precision-of-match statements**: *"ties to four decimal places"*, *"identical across arms to seventeen decimal places"*, *"cost margins to four significant figures"* — a four-decimal tie sits at the 4090's 2.6e-4 noise floor, and a seventeen-decimal identity exceeds float64's decimal precision for values ≥1. **The seventeen-decimal phrasing should become "bitwise identical" either way**; the other two need one crucible confirmation of substrate (numpy vs GPU) · `:1029` *"deep layers **4–6**"* — layer 4 is the granular input layer, not deep, and not a corticostriatal source *(also found by the citation audit, which additionally found it is the **wrong Shepherd**)* · `:1029` *"cognitive = noisy"* mapping appears only in a parenthetical · `:1094` *"Claude (Anthropic, 2025)"* resolves to the *"Exploring model welfare"* blog post — right referent for `:1039`, wrong one for the tool · `:1043–1048` §10.2's priorities list covers P1–P4 and omits **P5, the only prediction testable today on existing open datasets** · `:1100` Data Availability covers §9 but not §8.9's eight quantitative results · `:1037`/`:1039` register: *"This is a concrete deliverable, not an abstract philosophical claim"* (not-X-but-Y for rhythm) and *"has immediate ethical and engineering value"* (self-praise predicate) · `:897` the provenance of the "two theoretical implications" is unstated where the predictions are explicitly *"derived afresh"* · `:1001` *"criticality dependence"* — adjacent member of the commitment family, fold into the MG ruling.

### §8–11 VERIFIED CLEAN

All §8.9 arithmetic recomputed by hand (every ratio, count, range and combinatorial claim: 7×10+2 = 72 ✓; survival ranges non-overlapping ✓; d = 2.44 internally coherent ✓) · **no computational figure past 3 decimals anywhere in the file** · criticality-as-prerequisite: **no new members in range** — the other "prerequisite" hits (`:513`, `:518`, `:520`, `:524`) are all *"computational prerequisite"* = Class 4 with criticality as signature, the licensed form · barrier language: none beyond the B12 family; **§8.9's price-discipline is the best in the paper** (`:993` pre-concedes the unrolling result, `:999` explicitly disclaims closure-necessity — *"falsified five times in this program"*) · localized-concept: zero hits, **three active disclaimers** at `:945`, `:953`, `:1021` · seizure route at `:1066` fully route-independent · closure/return vocabulary: only the ruled §8.9 uses; **the v14 phrases *"the cycle that carries the return"* and *"reads back over a short return"* were replaced in `3ec61acb`** by *"the cycle that closes"* and *"reads back over a short path"* — ⇒ **the crucible inbox item asking aIware to check A#9's "reads back over a short return" is ALSO already closed** · one-directionality: no banned constructions in range (single soft site `:955`, folded into B13) · back matter: S309 blockers 15 and 16 both hold · Predictions 1, 2, 3, 5 framing-compliant; §8.7/8.8 correctly quarantined as untestable implications.

---

## Agent 4 — the rival-theory referee panel (IIT / GNWT / PP / HOT / Illusionism / AST)

**Plain verdict: the named-rival characterisations in §7 are now in good shape. The expensive remaining exposures are two surviving instances of already-repaired defect classes, three self-contradictions a rival referee can quote, and two structural flanks with no answer in the text — one of which the theory's own registry already holds the reply for.**

### BLOCKERS

**B14 — `:54` [IIT] — the "consciousness = Φ" mischaracterisation survives at a THIRD site, with an invented threshold on top.**
> *"IIT, which identifies consciousness with a mathematical measure (integrated information, Φ) that in principle applies to any substrate **meeting the measure's threshold**"*

The known finding covers `:86` only. IIT 4.0 identifies an experience with a maximally irreducible *cause-effect structure*; Φ quantifies its irreducibility and is explicitly not the identity relatum. **And IIT has no threshold** — any maximum of Φ > 0 is conscious. This is in §1.3's contribution list, the second place an IIT referee reads. **Third site of a twice-repaired defect; neither prior review found it.**
**Repair:** mirror `:834` — *"…which identifies an experience with a maximally irreducible cause-effect structure specifiable in principle on any substrate…"*

**B15 ⭐⭐ — [IIT] the exclusion flank: FMT scores itself ● on the Boundary Problem (`:826`) while its own results generate a plurality-of-experiencers problem it never answers.**
The paper states in its own voice: `:630` *"A recurrent network cannot be made return-free at all — one can only choose which of its subsets sit inside a returning component"*, and `:999` reports that opening the global loop *"leaves two and three smaller closed self-consistent systems respectively still standing."* ⇒ **By FMT's own account, closed self-referential loops are ubiquitous in any intact recurrent cortex.** IIT invented exclusion precisely to answer why there is one experiencer rather than many overlapping ones — and the paper praises that postulate as *"the strongest existing treatment"* of the boundary requirement at `:98`. FMT offers no counterpart anywhere.
**The referee's sentence:** *"The theory rates itself ● on Boundary while possessing no analogue of exclusion; on its own §8.9 result it predicts a crowd of simultaneous experiencers in every intact brain."*
**Cheapest repair, using only existing commitments** (one paragraph, §7.2's IIT entry or after `:516`): closure alone is never sufficient — **both** thresholds of §3.7.3 must be met, and the smaller closed components of `:999` fail the architectural threshold (they run no generated EWM/ESM pair). One experiencer per *running simulation*; simulations are individuated as concrete generated processes over the global read/write channel (§3.6.1), not as subset-relative measures. Two experiencers therefore require either substrate partition (split-brain, §5.2) or ESM forking (DID, §6.2) — **exactly the two cases the theory already treats.**

**B16 ⭐⭐ — [PP] the "FMT is PP with new labels" objection is now fully assemblable FROM THE PAPER'S OWN CITATIONS, and the theory's registered standing reply is absent from §7.2.**
A Friston-school referee assembles it: self-referential closure is in-house (*"Beautiful Loop"*, `:875`); criticality is in-house (Tucker, Luu & Friston 2025, cited approvingly at `:656` and `:905`); altered states are in-house (REBUS, `:60`, `:913`, `:929`); the self-model is in-house (Seth's interoceptive territory, conceded at `:851`); and `:851` concedes FMT *"can adopt PP's prediction-error machinery wholesale."* **Every load-bearing element has an active-inference counterpart cited by this manuscript.** The only stated defence is `:875`'s single clause plus `:889`'s combination argument, which is aimed at MDM/SMT, not active inference.
⚠ **And `didactic-patterns.md` #36 — the weather-simulation three-step, MG-authored, marked *"paper — the standing reply to 'isn't FMT just predictive processing?'"* with placement explicitly assigned to the §7 PP entry — never made it into §7.2.** §3.4.3's weather simulation serves the general closure argument; it is never turned against PP where the objection lives.
**Repair, two sentences at `:851`/`:875`:** (i) deploy #36 — PP's prediction machinery run over a world-model is weather forecasting, real computation no one undergoes; the reference being the self-model, and closure carrying it across frames, are what PP does not supply; (ii) state that active inference holds each element *severally* (Beautiful Loop the closure, Tucker et al. the criticality, REBUS the altered states) but no active-inference account combines them with the real/virtual two-level ontology — which PP cannot supply, since by its proponents' own statement (`:851`) it is not a theory of what makes a state conscious.

**B17 — `:849` [HOT] claims exactly what §3.4.3 concedes the paper cannot do.**
> `:849`: *"…explaining **why** self-representation produces phenomenality through the virtual qualia framework."*

Against `:304` (*"does not claim to **prove** that self-referential closure must produce phenomenality"*), `:334` (*"argued for and not derived"*), `:833` (the ◐ is carried *because* the step is a commitment). The HOT paragraph faults HOT for *"why does higher-order representation produce phenomenality?"* — the very question FMT answers only by an argued-for identity, as `:342` admits both theories do. **§7.2 claims for FMT the exact explanatory step §3.4.3 disclaims, on the exact point where it faults the rival.**
**Repair:** *"…embeds it in the richer four-model architecture and offers an argued — not derived (§3.4.3) — account of why self-representation constitutes phenomenality, a bridging commitment of the same kind HOT carries via the transitivity principle; where the two genuinely part is stated below."*

**B18 — `:368` vs `:608` [Illusionism] — the paper asserts as fact in §3.4.5 a claim about Frankish that §4.2.5 concedes Frankish rejects.**
`:368`: *"Strong illusionism generates no such obligation, because on its account there is no fact of the matter about whether the system 'really' experiences."*
`:608`: *"…whether strong illusionism generates a parallel obligation is contingent on whether quasi-phenomenal states suffice for moral status — **which Frankish argues they can**."*
`:368` makes the moral-patient contrast the **entire** cash value of FMT's difference from strong illusionism (*"What makes the commitment non-trivial is its practical consequence"*) — so the contradiction lands on the load-bearing sentence. An illusionist referee quotes `:608` against `:368` and concludes the sole stated practical difference evaporates by the paper's own admission.
**Repair at `:368`:** *"Whether strong illusionism generates a parallel obligation is disputed — Frankish argues quasi-phenomenal states can ground moral status (§4.2.5) — but on FMT the obligation follows from a fact about the system, not from a further ethical decision about how to treat states that misrepresent themselves. The difference in grounding survives even if the practical verdicts converge."*

### Rival-panel SHOULD-FIX

`:835` the Combination-Problem footnote attributes to IIT a problem its proponents claim exclusion dissolves (Tononi & Koch 2015 state outright IIT is not panpsychism and experiences do not combine) — and the paper's own `:814` rule requires contested ratings to be noted · `:839`/`:843` **Aaronson is cited only for intractability; his actual contribution — the expander-graph reductio — is never stated, and FMT's ready answer goes unused** (the heteronomy trichotomy excludes exactly such systems — see U5) · Table 5 `:830` gives FMT ● on Causal Role while `:1056` concedes the position *"occupies contested ground"*; IIT's ◐ on Causal Role is uncontested-noted though its proponents would claim ● · `:104` *"IIT's qualia space"* is IIT-3.0 vocabulary; 4.0 says Φ-structures · **`:342`/`:847`/Table 5 characterise GNW's Hard-Problem stance three incompatible ways, none of them Dehaene's** — Dehaene (2014) claims the problem will *evaporate*, an identity claim structurally parallel to FMT's own · **Mashour appears nowhere in the manuscript** though Mashour, Roelfsema, Changeux & Dehaene (2020, *Neuron*) is the modern canonical GNW statement and has a developed rival account of anaesthetic unconsciousness · Table 1 `:176` operationalises *"Becomes conscious"* exclusively via ignition/P3b — the marker of the access transition `:382` says consciousness does not require, so FMT's predicted below-broadcast state is undetectable on FMT's own table · `:1017`–`:1019` OQ4 is billed as *"the sharpest architectural test"* then concedes the contrast rests on a *"strict reading"* PP practice does not hold · **Lau's perceptual reality monitoring is unengaged** while §6.0 builds its machinery and OQ7 (`:1029`) proposes a GAN-style discriminator gate — which is Lau's 2019/2022 theory, GAN analogy included; a Lau-school referee reads it as reinventing PRM without attribution · `:56` *"Dennett's illusionism (which denies qualia are real)"* drops the qualifier `:86` and `:366` both carry (*"as traditionally conceived"*) — same-pattern-different-site · **`:949`, `:961` attribute to IIT and GNW predictions about DID alter switching and lucid-dream onset that neither has published** — FMT's extrapolations stated as the rivals' commitments; one word each fixes it (*"would presumably locate"*) · `:973` *"standard functionalism predicts the encoding transfers with the structure"* is contestable — functionalism is precisely the view on which implementation varies freely · `:853` the AST distinction is answered only by list-recitation; the sharp answer (AST posits a represented schema of *one process*; FMT's closure is a *structural condition on the whole model economy*) is never given · `:29` vs `:851` — §1 lists PP among frameworks competing *"for explanatory primacy"* over consciousness while §7.2 states with the proponents' own words that PP is not a consciousness theory.

### UNDER-SOLD — where the paper is stronger than it says

- **U1** — the weather-simulation discriminator (#36) is the registered strongest reply to the most dangerous objection and is not in §7.2. *(= B16.)*
- **U2** — **FMT's *actual* empirical disagreement with HOT is never stated.** `:390` commits FMT to phenomenal experience below first-order self-observation — **a direct denial of Rosenthal's transitivity principle**. That is a genuine, principled, in-principle-testable divergence, far stronger than `:849`'s "richer architecture".
- **U3** — **Anton's syndrome is FMT's answer to the misrepresentation/empty-HOT problem** (Block's critique) and the connection is never drawn, though the clinical case is in hand at `:802`.
- **U4** — **Graziano's social-attribution machinery converges with FMT's redeployment** and the convergence is unclaimed, though the paper claims RIFT and Beautiful Loop as support. This one is older and closer; not claiming it reads as avoiding the nearest neighbour.
- **U5** — **FMT has an answer to Aaronson's expander that IIT lacks** — the heteronomy trichotomy excludes high-Φ trivial systems by construction; IIT must bite the bullet. A clean comparative advantage sitting unused two sections away.
- **U6** — **`:427` derives working-memory span from channel rank; GNW takes workspace capacity as a brute empirical constant.** `:847` would be strengthened by one clause.

### Rival panel — VERIFIED FAIR (do not re-check)

IIT §7.2 core `:843`–`:845` (cause-effect-structure identification in IIT's own terms; Φ correctly cast as quantifier; the interventional-TPM reply to Barrett & Mediano; the concession paragraph is accurate and generous) · the unfolding argument `:859`–`:865` (target stated correctly — it catches IIT *and* FMT; epistemic-not-architectural force acknowledged; unbounded-substrate concession made) · GNW empirical record `:847` (ignition/P3b track record praised above FMT's own; COGITATE evenhanded; the shared-limitation admission is exemplary) · PP generosity `:851`, `:913`, `:929`, `:935`–`:939` (the genuine Hohwy & Seth fragment; REBUS credited with one-step derivation) · illusionism ontology `:366`–`:368` first half, `:604` · Dennett credit `:354` · RPT `:855` · **Pinto reinterpretation `:666`, `:915` — the audit's repair held and is exemplary** · Safron/IWMT `:879` — *"the strongest comparative writing in the paper."*

---

## Agent 5 — citation audit of the two previously-unreviewed ranges

**Plain verdict: two-way existence checking is nearly clean, but four fresh support-failures survive — one of them (Tagliazucchi 2016) at three sites including the showcase convergence table.**

### BLOCKERS

**B19 ⭐ — `:455`, `:465` (Table 3), `:476` — Tagliazucchi et al. (2016) credited with criticality signatures it does not contain.**
Claims: `:455` *"Tagliazucchi et al. (2012, 2016) showed criticality signatures in waking fMRI and under LSD"*; Table 3 `:465` *"2016 | Tagliazucchi et al. — LSD and criticality"*; `:476` lists it among sources where *"the signatures are already routinely measured"* — the signatures being σ, DFA α and avalanche statistics.
The listed 2016 entry (`:1562`) is *"Increased Global Functional Connectivity Correlates with LSD-Induced Ego Dissolution"*, Curr Biol 26(8):1043–1050 (verified via Crossref + abstract). **It measures global functional connectivity density and modular/rich-club disruption — none of the three named signatures, no power laws, no branching ratio, no LRTCs.** Same defect class as the audit's Hengen & Shew finding.
**Repair:** cite **Tagliazucchi, Carhart-Harris, Leech, Nutt & Chialvo (2014)**, *"Enhanced repertoire of brain dynamical states during the psychedelic experience"*, *Hum Brain Mapp* 35(11):5442–5456, `10.1002/hbm.22562` — explicitly framed as movement toward criticality. ⚠ **It is psilocybin, so the "under LSD" wording must change**, or additionally cite **Atasoy et al. (2017)**, *Sci Rep* 7:17661, `10.1038/s41598-017-17546-0` (LSD, connectome harmonics tuned toward criticality). At `:476` simply drop Tagliazucchi — Priesemann + Algom & Shriki carry it. If 2016 is displaced everywhere, remove or repurpose entry `:1562` so it does not become a reverse orphan.

**B20 — `:410` — Carhart-Harris et al. (2014) cited for the hierarchical visual progression, which the Entropic Brain paper does not contain.** *(§3's agent flagged this as an unverified pointer; this agent verified it against the Frontiers full text — the lead was correct.)*
The paper has **no phosphene→geometric→complex→scene account, no V1/V2/V3 hierarchy, no dose-dependent visual progression.** Reviewer 4's S3 flagged the ordering as *uncited* at `:726`–`:733`; here it is worse — cited to a source that lacks it.
**Repair:** attach CH2014 to the permeability/entropy half only; source the progression from **Klüver (1966) + Bressloff et al. (2002)** (both already in the list) and add **Kometer & Vollenweider (2018)**, *Curr Top Behav Neurosci* 36:257–282, `10.1007/7854_2016_461`. **One fix serves this site and `:726`–`:733`.**

**B21 — `:1021`** — *(= B11; third independent route to the same defect.)*

**B22 — `:466` (Table 3) — a quoted title with no authors and no reference entry: the only cited-but-not-listed orphan in the file.**
Row: *"2022 | 'Self-organized criticality as a framework for consciousness' (review)"*. The work is real — **Walter, N. & Hinterberger, T. (2022)**, *Front. Psychol.* 13:911620, `10.3389/fpsyg.2022.911620` (Crossref-verified) — but appears nowhere in the reference list. **Same gap class as the audit's "Siclari 2021" finding: the existence gate checks the list, not narrative/table citations.**

### Citation SHOULD-FIX

`:905` *"Ketamine, which preserves criticality markers"* is uncited, and the evidence in the sentence's own citations (Casali 2013; Casarotto 2016) is **PCI — which the paper itself rules is not a criticality measure at `:480`**. Self-contradiction plus unsupported claim · `:907` Atasoy et al. (2016) does not claim harmonic modes are *"selected near criticality"*; that reading belongs to Safron (2020) / Atasoy (2017) · `:945` Reinders et al. (2008) is **single-authored** (Crossref-verified) so "et al." is wrong, **and it is a review, not a demonstration** → replace with **Reinders et al. (2006)**, *Biol Psychiatry* 60(7):730–740, `10.1016/j.biopsych.2006.02.019` · `:1013`/`:1364` **Kleiner (2024) is actually Kleiner & Ludwig** (`10.1007/s11229-024-04503-4`, *Synthese* 203(3):89) — the reference drops the co-author, and *"category theory"* mischaracterises the paper · `:1029` the layer-5 corticostriatal fact belongs to **G.M.G. Shepherd (2013)**, *Nat Rev Neurosci* 14(4):278–291 — **a different Shepherd from the listed 2011 cortical-evolution paper** · `:771`/`:1128` *"(New York Declaration on Animal Consciousness, 2024)"* has no matching key; the entry is alphabetised under **Andrews, K., Birch, J., Sebo, J. & Sims, T. (2024)** — **the only reverse-orphan-shaped defect in a full two-way sweep of all 249 entries** · **reference-list alphabetisation: 24 breaks** at `:1140`, `:1148`, `:1160`, `:1186`, `:1208`/`:1210`, `:1242`, `:1254`, `:1270`, `:1280`, `:1290`, `:1302`, `:1318`, `:1322`, `:1350`, `:1354`, `:1370`–`:1376`, `:1398`, `:1436`/`:1438`, `:1500`, `:1502`–`:1504`, `:1526`–`:1528`, `:1540` — journals catch this mechanically · `:929` *"anosognosia has a standing predictive-processing treatment"* is true but uncited → **Fotopoulou (2014)**, `10.1111/jnp.12010` · `:1418` Long et al. (2024) author order wrong — Birch and Chalmers are 9th/10th · `:1019` *"depersonalization-derealization disorder shows partial dissociation"* uncited in the sharpest-test section → Sierra & David (2011).

### Citation VERIFIED CORRECT — web-verified this session, do not re-check

`:340` **Janik, Sayigh & Wells (2006)** — identity information in frequency contour with voice features removed, synthetic-whistle playback, 14 dolphins: exactly as characterised, and it is load-bearing for §3.4.3's criterion · `:340` **King & Janik (2013)** · `:957` **Voss et al. (2009)** — *"three lucid dreams from three participants"* is exact (3 of 20 trained subjects, one episode each) · `:957` **Baird, Mota-Rolim & Dresler (2019)** — the review does carry both the saccadic-artifact caution and non-replication; the hedge is faithful · `:1039` Butlin et al. (2025), Birch (2025), Schwitzgebel (2025) all exist as listed · `:366` Graziano (2024) *eNeuro* 11(10) exists · `:1029` Gershman (2019), **Oorschot (1996)** (2.79 M striatal / ≈30 k output, rat — arithmetic checks), Howes & Kapur (2009), Deperrois et al. (2022).
Characterisations judged accurate against the sources: the full `:354` postdiction cluster (Kolers & von Grünau 1976, Geldard & Sherrick 1972, Eagleman & Sejnowski 2000, Libet 1979 — contested and properly hedged, Dennett & Kinsbourne 1992, Bartlett 1932, Schacter & Addis 2007, Hassabis 2007) · `:146` Metzinger 2003 / Damasio / Seth 2021 / Kriegel & Williford · `:162` Näätänen 2007 · `:168` Scoville & Milner 1957 + Milner 1962 · `:184`/`:196` Tsuchiya 2015 · `:227` Reber / Fiser & Aslin / Öhman & Mineka · `:423` Stringer 2019 + Zheng & Meister 2025 (⚠ one-line caution: Z&M's "inner brain" is their *low*-rate side, so a referee who knows the paper may quibble with the "inner dimensionality" phrasing — substance fine) · `:427` Miller 1956 / Cowan 2001 · `:433` Boly 2012 · `:439`/`:520` Wolfram 2002, Langton 1990 · `:476`/`:478` Hardstone 2012, Clauset 2009, Touboul & Destexhe 2017 · `:482` Tononi 2004, Albantakis 2023, C_N 1994 · `:498` Aru 2020 · `:504` Baylor 1979/1980, Kenet 2003, Merabet 2004 · `:522` Toker 2026 · `:524` Mago 2025 · `:526` Ölveczky 2005, Chew 2019, Maye 2007 · `:1066` Jiruska 2013 and Kramer 2012 · `:913` REBUS, Klüver 1966, Bressloff 2002 · `:917` Fox 2005 / Northoff 2006 / Dehaene & Naccache 2001 / Rameson 2010 · `:935` Nour 2016 · `:945` Reinders 2003, Schlumpf 2014 · `:955` LaBerge 1985 · `:965` Kriegeskorte 2008 · `:995` Kanders 2017 · `:1015` Hameroff & Penrose 1996 + Tegmark 2000. Bibliographic details spot-verified for ~45 entries.
**Not independently verifiable:** Gruber 2026a–d internals (self-cites); Algom & Shriki 2026 and other 2026-dated entries; the Bieberich DOI check remains open as already recorded.

> **This agent's own process note, and it generalises the headline:** three of its four blockers are the same disease the two Fable reviews named — a repaired defect class whose unswept siblings survive. **The sweep-by-pattern rule applies to citation repairs too: when a fabricated number is deleted, the sentence it propped up must be re-sourced or deleted with it.**

---

## Agent 6 — prose register / AI-tell pass (whole file)

**Verdict: the banned-phrase layer is essentially clean — two passes of enforcement worked. What remains is one systemic copyedit blocker, one voice break, one Abstract grammar slip, and a posture problem concentrated in §8.9.**

### BLOCKERS

**B23 ⭐ — systemic mixed British/American spelling, reaching into the Abstract.**
The split tracks edit generations: the recent principle statements, §3.6.1, §6.0, the unfolding passage and §8.9 are British; the older body is American. `:17` opens the Abstract British (*"Open-ended computation allows free **modelling**"*) while `:58` a few lines later has *"self-**modeling**"*. A referee reads this as multiple hands; a copyeditor bounces it.

**Counts re-measured in the main loop, reference list stripped, 50,059 body words.** ⚠ The agent's `organised`/`analysed` rows were **artifacts** — those patterns also match *organism* and *analysis*, which are dialect-neutral. Corrected table:

| BrE | count | AmE | count |
|---|---|---|---|
| modell* | 33 | model(ing/ed/er) | 89 |
| behaviour* | 5 | behavior* | 31 |
| programme* | 6 | program* | 36 |
| realis* | 4 | realiz* | 35 |
| characteris* | 10 | characteriz* | 24 |
| specialis* | 1 | specializ* | 4 |
| normalis* | 1 | normaliz* | 3 |
| homogenis* | 2 | — | 0 (BrE-only) |

The AmE base is otherwise locked: `anesthe*` 33/0, `color` 7/0, `gray` 4/0, `generaliz*` 15/0, `recogniz*` 3/0, `center` 2/0, `favor` 3/0.
**Repair: normalise to American throughout** (the dominant convention, and the one the anaesthesia/colour vocabulary is already locked to) — `modeling, behavior, program, realized, characterized, specialized, normalizes, homogenizes`. Mirror into `latex/paper.tex`. If the target venue mandates BrE the sweep flips direction instead — **decide once, apply everywhere.**

**B24 — `:845` — authorial "We" three times in a single-author paper.**
> *"**We** nonetheless regard IIT's central diagnosis … as substantially correct … **We** depart from IIT on what the irreducible structure is … **We** share IIT's insistence on recurrence …"*

The paper's authorial voice is singular everywhere else — *"the present author's judgment"* (`:814`), *"I claim no priority"* (`:1021`), *"is, I believe, internally consistent"* (`:1056`). The reader-inclusive "we" at `:84`, `:128`, `:362` is conventional and fine; **`:845` is the only place the author speaks in the plural.**
**Repair:** *"The present account nonetheless regards… and adopts it"* / *"FMT departs from IIT on…"* / *"The theory shares IIT's insistence on recurrence…"*

**B25 — `:15` (Abstract, sentence four) — a category error cannot "seek".**
> *"…reframes the Hard Problem as a category error **that seeks** phenomenal properties where they do not exist."*

A grammatical-agency slip in the fourth sentence of the Abstract is the cheapest thing a referee can hold against the prose.
**Repair:** *"…reframes the Hard Problem as resting on a category error: phenomenal properties are sought at a level where they do not exist."*

### Prose SHOULD-FIX

`:255` *"To put it precisely:"* — throat-clearing, the one live instance of that family (§3 was never register-reviewed) · `:247` *"The reader should consistently map…"* — reader-management · `:368` *"This is not a minor difference:"* + rhetorical escalation; the paragraph already lands on *"The same physics, the same behavior, but different ethics."* · `:508` triple hedge, the third repeating the first · `:767` vs `:955` the same transition is *"extended consciousness"* and *"simply extended consciousness"*; §3.5's ladder has no bare "extended" rung · `:582` vs `:761` **"dreaming" is defined twice with different apparent extensions** — §4.2.3 makes it a technical whole-kind term, §6.3 re-derives it with no pointer · `:889` a lecture on how theory-evaluation works, immediately before doing it · `:997`/`:999`/`:1003` **"banked" ×3 — project-internal crucible vocabulary presented as a status a journal reader cannot look up**; `:997`'s partial gloss does not license the bare reuse · `:997` *"Fifth, and reported because it did not fully succeed:"* — narrates the document's own reporting decision · `:999` *"held identical across arms to seventeen decimal places"* — float64 equality wearing a costume *(also §8–11 S4)* · **`:999` posture: the eighth-result paragraph is a single ~1,500-word block whose tail is methods scoping, inside a section that announces itself as a summary — the "student proving to the teacher" failure in its purest form.** ⚠ The τ_syn clause inside that block is MG-approved text; restructure around it or get a ruling · `:1037` *"a concrete deliverable, not an abstract philosophical claim"* — corporate register + not-X-but-Y for rhythm · `:72` vs `:1070` **the modelling-error humility paragraph appears twice, near-verbatim** — stated twice it stops being a limitation and becomes a performance of modesty; keep `:1070` · `:1064` the *"language linearizes"* limitation asserts an untestable humility and duplicates the Gödel limitation at `:1062` · `:526` *"This is the correct reading of 'creative' exploration"* — self-certifying · **acronyms unexpanded on first use: PCI used `:154` before its `:160` expansion; DFA bare at `:174`/`:194` (expanded only at `:476`); BIS (`:195`) and 5D-ASC (`:198`) never expanded; REBUS (`:60`) never expanded; LZc (`:415`) never paired with its long form** · **cross-reference style: 26 `§N` vs 98 `(Section N)`**, the `§` form clustering in recently added passages · `:1078` *"the reader is invited to compare"*.

### DENSITY REPORT — the gate PASSES

Sliding window **400 words / step 100 / flag at 4.0× baseline**, the five-pattern antithesis set taken verbatim from simbook's `check_prose_register.py`, references excluded.
- **Baseline 6.29 constructions / 1,000 words** (315 matches in 50,059 words). Gate = 25.2/1,000w, i.e. >10 in one 400-word window.
- **Flagged windows at 4.0×: ZERO.**
- Sub-threshold peaks, orientation only: **3.18× at `:332`–`:336`** (the §3.4.3 close — five oppositions carrying the constitutive-vs-epistemic contrast the section exists to draw; **cut none**); **3.18× at `:137`–`:146`** (definitional contrasts, content); **2.78× at `:851`** (the PP comparison paragraph, 7 constructions in one very long line — if any single passage gets a manual trim, this is the one).
- ⚠ **Observation, not a gate finding, and it is MG's call:** the paper's *baseline itself* is ~2.8× the English book's 2.23/1,000w, so a self-normalising gate structurally cannot fire on it. *"rather than"* appears **168** times, *"not merely"* 22. Ambient style load: **846 em-dashes** (~1 every 59 words), `genuine/genuinely` 36, `precisely` 17, `exactly` 17.

### Prose VERIFIED CLEAN — zero hits, swept whole-file

**"load-bearing"** in every form incl. "carries the load" — **0** (the S309 repair held) · **the "bite" family** — **0** · throat-clearing ("worth + gerund" all eight verbs, "the key point is", sentence-initial "Importantly,"/"Crucially,") — 0; the review-1 `:406`/`:419` instances are gone · empty superlatives — 0 (the three literal "deepest" uses are recursion-depth, not the tell) · empty-praise predicates — only `:128`, already found; `:560` *"do genuine causal work"* inspected and **kept** (the same sentence cashes it out) · canned aphorisms — 0; review 1's `:891` aphorism is gone · revision-history narration — 0 · strategy-narration — 0 new · "four modules" — only `:15`'s pre-emption · **CLOSURE vs "return" — compliant throughout** · tense — no drift · first person — singular and consistent except `:845`.

---

## ⛔ SESSION LIMIT — four agents died mid-flight (limit resets 04:20 Europe/Vienna)

Same shape as S310, different cause: **the session usage limit, not Fable credits.** The Fable probe at the start was correct and is not the lesson here. **The lesson is that a seven-agent wave plus a three-agent verification wave exceeds one session's budget** — commission the verification wave only after the review wave has been banked, or split across sessions.

**Died, and what each had done — do NOT restart these from zero:**

| agent | state at death |
|---|---|
| `.tex` content-equivalence audit | ⭐ **Had completed the hard part.** Dying output: *"The full-body alignment is done: 416/~525 paragraphs match exactly, the rest are mostly renderer artifacts plus ~15 real leads. Now I verify each lead against the actual sources."* **The ~15 leads were never named.** Re-run reproduces the alignment cheaply; the verification is what is owed. |
| adversarial refutation of the four structural blockers (B7, B15, B16, B17) | Dying output: *"The Boundary Problem definition and split-brain treatment are now clear. Now the didactic-patterns file for Finding 3, and the .tex mirror check for Finding 1."* ⇒ it had **finished its reading for B15** and reached no verdict. **No verdict was returned for any of the four.** |
| §3 argument-validity second lens | died with no partial output |
| citation-replacement verifier | **never reported failure — status unknown.** Do not relaunch blindly; check for a completion notification first, or duplicate work results. |

⚠ **Per the S310 process note — a dying agent's partial output is not to be discarded unread — both partials above are recorded verbatim rather than summarised.**

⛔ **CONSEQUENCE FOR THE FOLD-IN: `B7`, `B15`, `B16`, `B17` are UNVERIFIED.** They are the four most expensive findings in this review (two propose new paragraphs; one renames a core theoretical term across multiple sites). **They must survive an adversarial pass before any of them is folded in.**

---
---

# WAVE 2 — VERIFICATION. This is where the review paid for itself.

## Agent 8 — adversarial refutation of the four most expensive findings

**Commissioned to REFUTE, defaulting to refuted on uncertainty. Result: 2 of 4 refuted, 1 confirmed with a flawed repair, 1 confirmed outright.**

### ❌ B15 (IIT exclusion flank) — **REFUTED. Do not add the paragraph.**
Both quotations are **accurate as strings but out of the context claimed**. `:999`'s *"leaves two and three smaller closed self-consistent systems still standing"* is about **the model connectome** of §8.9, and the same paragraph pre-empts the over-reading: *"This is a claim about graph structure and not about dynamics… It says nothing about whether the surviving closed components do anything the theory cares about… scoped to one connectome family."* `:630` sits in §4.4's discussion of what closure-removal experiments can establish, not intra-brain phenomenology.
**The multiplicity inference requires closure to be sufficient, and the paper denies this explicitly:** `:516` *"The Class 4 regime is necessary but not sufficient; the four-model architecture is necessary but not sufficient. Together they are sufficient."* `:302`: *"If level-specific properties were sufficient for phenomenality, every running program would have qualia. They do not."* Split-brain is handled at `:666`, DID at `:757`. The ● at `:826` answers Boundary **as §2.3 defines it** (`:96` — *"what delineates conscious from non-conscious processing"*), not as a uniqueness theorem; `:845` explicitly *declines* IIT's exclusion-based commitment on the record.
⛔ **And the proposed repair would have introduced two commitments the paper deliberately does not make:** that the smaller closed components generally run no EWM/ESM pair (`:225` says the brain runs *"an effectively uncountable number of overlapping models"*), and that DID forking yields **simultaneous** experiencers — which `:757` contradicts (**alternation**, not concurrency).
**Optional, if anything:** one clause at `:845` — *"what individuates an experiencer on this account is not maximal Φ but a running four-model simulation: closure and Class 4 dynamics alone, being insufficient (§3.7.3), never multiply subjects within an intact substrate."*

### ❌ B17 (`:849` claims what §3.4.3 disclaims) — **REFUTED.**
`:304` reads in full: *"The argument does not claim to **prove** that self-referential closure must produce phenomenality — it claims that… this is **the most parsimonious explanation for why** certain computations have an inside and others do not."* ⇒ **The very sentence cited as the disclaimer itself claims an explanation-why.** `:849` asserts exactly what `:304` asserts and contradicts only what `:304` never claimed.
⚠ **The finding's quotation was also misattributed** — *"argued for and not derived"* is at `:338`, not `:334`. The paper maintains argued/derived as a **term of art** throughout (`:338`, `:520`, `:833`, `:845`), and within that vocabulary "explaining why" and "deriving" are different claims.
**Optional cosmetic only:** `:849` → *"…arguing **why** self-representation produces phenomenality…"* to echo the paper's own vocabulary.

### ◐ B7 (evolutionary forcing) — **PARTIALLY CONFIRMED, and the proposed repair was WRONG.**
`:522` — **which the finding never quoted** — already glosses the trichotomy provenance-neutrally: *"must do so in the service of **autonomous self-modeling**… Nothing **recruits** its universality for autonomous self-modeling."* The finding's own proposed word is already the paper's verb. `:634` (§4.4) and `:977` (§8.7) are likewise functional, with no evolution clause.
⇒ *"The AC programme fails its own prerequisite by definition"* is **false** — the operative definition is functional. What survives is a **labelling vulnerability**: a referee can quote `:518` + `:520`'s *"selected to use"* against `:977`.
⛔ **The proposed gloss is dangerous: "supplied by evolutionary forcing in biology and BY DESIGN in an artificial substrate" — because a laptop is also designed.** What excludes the laptop is that nothing *in its own operation* recruits its universality for self-modelling.
**Corrected wording:** *"**Third — autonomous recruitment.** An autonomous, self-referential, resource-constrained system that uses that layer for self-modeling is driven toward criticality and held there… In biology the recruiting pressure is evolutionary selection; an artificial substrate must have the recruitment engineered in and then sustained by its own dynamics — what excludes the laptop is not provenance but that nothing in its own operation recruits its universality for self-modeling."*
Keep `:520`'s closing sentence (the cortical automaton *"forced… by evolutionary demand"*) — that biological-causal story is load-bearing and untouched.
**Sites:** `.md` `:518`, `:520`, `:995`; `.tex` `:666`, `:668`, `:1246`. (`:522`/`tex:670` already conforms.)
⭐ **Site the finding MISSED: `:845` / `tex:1070`** — FMT characterised as *"**evolved**-closure-gated updating"* bakes provenance into the IIT comparison and undercuts the substrate-neutrality claim two clauses earlier in the same sentence. → *"autonomously recruited, closure-gated"*.

### ✅ B16 (PP "new labels" + missing pattern #36) — **CONFIRMED. This is the one that warrants its full repair.**
Every "in-house counterpart" attribution checks out at source: Beautiful Loop at `:875`; Tucker, Luu & Friston 2025 at `:656` and `:905`; REBUS at `:851` and `:929`; Seth at `:851` — *"precisely the territory FMT formalizes as the ESM"*; and `:851` does say FMT *"can adopt PP's prediction-error machinery wholesale"*.
**Pattern #36 is genuinely absent from §7.2** — every "weather" occurrence is §3.4.3/§3.4.4 (`:302`–`:352`) plus one incidental at `:634`. §3.4.3's three stages make the *closure* argument; #36's device is different and **PP-specific**.
**And the registry is an unexecuted MG directive:** `didactic-patterns.md` marks #36 *"paper — the standing reply to 'isn't FMT just predictive processing?'"*, MG-authored 2026-08-10, and states outright that *"The FMT master's §7 PP entry currently argues only that PP is scope-limited… That is a correct but **defensive** reply, and it does not discriminate."*
**Repair constraints:** use the three-way formulation (world-model prediction unexperienced → self-model prediction experienced → closed self-model prediction experienced *and continuous*); place at `:851` adjacent to the "missing top floor" sentence; **cross-reference §3.4.3 rather than re-running the three-stage weather argument** — the two devices share the vehicle but not the point, do not merge them; mirror into `paper.tex` near `tex:1070`ff.

> **The lesson, and it is the session's most valuable:** two findings that read as solid were built on quotes that were verbatim-accurate and context-false, and a third's repair would have re-admitted the very counterexample it was written to exclude. **An adversarial pass on the expensive findings is not optional.**

---

## Agent 7 — verification of every proposed replacement citation

⛔ **Three of the audit's proposals were wrong and would have shipped.**

| # | audit proposed | verdict |
|---|---|---|
| 1 | Reinders 2006 = `10.1016/j.biopsych.2006.02.019` | ⛔ **WRONG PAPER — that DOI is Farber et al., "Acute D2/D3 Dopaminergic Agonism", Biol Psychiatry 60(6):630–638.** Correct: **`10.1016/j.biopsych.2005.12.019`**, Reinders et al. (2006), *Biol Psychiatry* 60(7):730–740, PMID 17008145 — symptom provocation, 11 DID patients, state-specific subjective/cardiovascular/rCBF responses. |
| 2 | Toker et al. 2022 for ketamine criticality at `:905` | ⛔ **NO KETAMINE CONDITION.** Full text searched: conditions are waking, generalized seizure, GABAergic anaesthesia, psychedelic. All three "ketamine" hits are in the reference list. Use **Maschke et al. (2024)**, *Commun Biol* 7:946, `10.1038/s42003-024-06613-8` — propofol, xenon **and ketamine**; *"consciousness was retained only during ketamine anesthesia (in the form of vivid dreams)"*; measures avalanche criticality, chaoticity and criticality-related metrics. Exactly the sentence's claim. |
| 3 | Tagliazucchi 2014 as "movement toward criticality" under LSD | ◐ **OVERSTATED and it is PSILOCYBIN.** Its own words: the brain resides *"in (or at least near to) a critical point"* and the question is *"whether changes… are **consistent with** a displacement from this critical point"*. Hypothesis-and-consistency, not demonstration. ⇒ **Atasoy et al. (2017)** is the clean LSD citation: *"the frequency distribution of the active repertoire of brain states under LSD closely follows power-laws indicating a **re-organization of the dynamics at the edge of criticality**."* |

**Confirmed sound:** Tagliazucchi 2012 (`10.3389/fphys.2012.00015` — *"close to the critical point of a second order phase transition"*, keeps the waking-fMRI half of `:455`) · Walter & Hinterberger 2022 (`10.3389/fpsyg.2022.911620`, 71-publication systematic review — row characterisation fair, **entry missing entirely**) · Kometer & Vollenweider 2018 (`10.1007/7854_2016_461` — carries the taxonomy **and** the cortical-hierarchy linkage; ⚠ the **dose-ordering is not verifiable from accessible text**) · Fotopoulou 2014 (⚠ pages **1–19**, not 1–17) · Shepherd 2013 `10.1038/nrn3469` · Kleiner **& Ludwig** 2024 (⚠ "category theory" is a mischaracterisation — "functor" appears 0×; the framework is topological/metric/order structures) · Long et al. author order (Birch and Chalmers are **9th and 10th**) · NY Declaration — **correct as is**.

⭐ **TWO COLLATERAL CONTENT ERRORS surfaced during citation verification — neither was in any prior finding:**
1. **`:410` and `:729` map geometric form constants to "V2/V3-level" — Bressloff et al. (2002) derive them from *V1*.** Abstract verbatim: *"a theory of their origin in visual cortex (**area V1**)"*. The manuscript contradicts the source it would cite. → *"phosphenes and geometric form constants (V1-level; Bressloff et al., 2002) through complex imagery (higher visual areas)"*.
2. **`:1029` "deep layers 4–6… project to striatum" contradicts Shepherd 2013, which explicitly excludes layer 4:** *"Layer 4 stellate cells… having only local axonal projections"*; corticostriatal sources are IT-type in **5A/5B/6** and PT-type in **5B**. → *"deep-layer pyramidal neurons — IT-type in layers 5A/5B/6 and PT-type in layer 5B (Shepherd, 2013)"*.

Also: **Klüver 1966 supports the four form constants only, not the staged progression.** The canonical progression source is **Siegel & Jarvik (1975)**, in Siegel & West (Eds.), *Hallucinations*, Wiley, pp. 81–161.

### READY-TO-APPLY citation table

| site | citation to use | what the sentence must say |
|---|---|---|
| `:455` | Tagliazucchi et al. (2012) + Atasoy et al. (2017) | *"Tagliazucchi et al. (2012) showed criticality signatures in waking fMRI; connectome-harmonic dynamics re-organize toward the edge of criticality under LSD (Atasoy et al., 2017)"*. **Do NOT say Tagliazucchi 2014 demonstrated movement toward criticality.** |
| `:465` Table 3 | *"2017 \| Atasoy et al. — LSD, connectome harmonics at the edge of criticality"* | the row must name work that actually claims criticality |
| `:466` Table 3 | add reference entry for Walter & Hinterberger (2022) | row fair once the entry exists |
| `:476` | replace Tagliazucchi 2016 → **Maschke et al. (2024)** (or Tagliazucchi 2012) | *"routinely measured"* — Maschke measures exactly these metrics in this context |
| `:410`, `:729`/`:733` | *(Klüver, 1966; Siegel & Jarvik, 1975; Kometer & Vollenweider, 2018)* — **drop Carhart-Harris 2014** | form constants → Klüver; staged progression → Siegel & Jarvik; area-specific mechanisms → Kometer & Vollenweider. **Fix V2/V3 → V1.** State the staging as the theory's reading, not as demonstrated. **One set serves both sites.** |
| `:905` | **Maschke et al. (2024)** | ketamine retained consciousness with near-critical dynamics; propofol/xenon distanced from criticality |
| `:907` | keep Atasoy 2016 for the harmonic basis; add Atasoy 2017 for near-critical selection | attribute the metastable/phase-locked reading to Safron 2020, not Atasoy 2016 |
| `:929` | add Fotopoulou (2014), pages **1–19** | *"a standing predictive-processing treatment as aberrant predictive coding"* |
| `:945` | *(Reinders et al., 2003, 2006; Schlumpf et al., 2014)* — **drop the 2008 review**; DOI **`10.1016/j.biopsych.2005.12.019`** | the 2008 paper is single-authored and a review; it demonstrates nothing. Fix `:1506` to "Reinders, A.A.T.S. (2008)" if it stays for any other purpose |
| `:1013`/`:1364` | Kleiner **& Ludwig** (2024) | *"mathematical structures of experience spaces"*, not "category theory" |
| `:1029` | Shepherd (**2013**), `10.1038/nrn3469` | IT-type layers 5A/5B/6 + PT-type 5B — **not "deep layers 4–6"** |
| `:1418` | full author list, or "Long, R., Sebo, J., Butlin, P., et al." | current entry fabricates an order |

**New reference entries required:** Atasoy et al. (2017) · Kometer & Vollenweider (2018) · Siegel & Jarvik (1975) · Maschke et al. (2024) · Walter & Hinterberger (2022) · Fotopoulou (2014) · Reinders et al. (2006) · Shepherd (2013).

---

## Agent 9 — §3 second lens: ARGUMENT VALIDITY

⚠ **UNVERIFIED — single agent, no adversarial pass.** Given that this session's adversarial pass refuted 2 of 4 findings that read as equally solid, **these must be attacked before any of them is folded in.**

**Verdict: §3's skeleton is sound at the closure core and the channel identification; four load-bearing moves fail as stated.**

- **AV-1 `:204`/`:233`** — *"Nothing in the taxonomy is posited"* overstates. The **explicit pair is contained in Principle 3's own formulation**, which already names both a self- and a world-model; only the implicit pair is genuinely derived. The `:233` relabeling reply is valid *as a reply* but is a definitional victory. Also `:233`'s reafference premise is over-broad (*"any system that acts must predict the sensory consequences of its own actions"* — bacteria act). Repair is wording-level; `:225`'s *"four is the floor"* already sits at the honest altitude.
- **AV-2 `:255`/`:380`** — the regress argument **proves too much or too little**. It blocks only *total, exact* self-inclusion; read generally it would also block the ESM, which the theory celebrates. The general inaccessibility actually follows from the **definitional identification** of experience with the generated models — legitimate, but a different and weaker support than advertised. **The second pairing (explicit↔phenomenal) is never delivered** by the generative relation. And `:380`'s *"cannot be conscious"* is a non-sequitur from a premise about being *represented as content*; the correct support (the level argument) sits two sentences away.
- **AV-3 `:324`–`:326`** — the *"no residual"* premise is **false on the paper's own process ontology** (`:374`: *"constitutively processual — they exist in the doing, not in the blueprint"*), since the doing/description gap is generic. ⚠ **And the score/symphony analogy actively arms the objection it was meant to disarm** — a symphony is not self-referentially closed, yet score ≠ performance. `:332` patches by assertion. **What actually carries the argument is `:336`** — the content-level no-factorization argument, which is specific to closure and not circular. **The `:334` concession IS correctly placed** (commissioned question answered) — the defect is upstream.
- **AV-4 `:516` vs `:518`** ⭐ — *"Together they are sufficient"* (two conditions) contradicts *"a three-part condition"*, **and the contradiction survives B7's rename.** Read synchronically the third leg adds nothing beyond threshold two; read etiologically it contradicts `:144`, §4.4 and §8.7. The laptop is over-determined as an exclusion — what excludes an idle laptop is that no self-referential simulation is running, i.e. **threshold two**, so `:518`'s *"the laptop fails the third"* misassigns the work. **Repair must be made together with B7:** state that the third leg is not an additional condition but the second threshold seen from the dynamics side.
- **AV-5 `:443` + `:417`** ⭐ — **asymmetric evidence accounting.** `:443` discharges *every currently possible null* (no task of the required depth exists) while §8.9's medium-task positives are counted as support. Heads the theory wins, tails does not count — **the confirmation-you-cannot-fail structure, in a paper with a desk rejection for "predictions too general" already on record.** Same shape at `:417`, whose monotonicity falsifier is qualified *"absent ceiling effects"* with no independent ceiling criterion. **Repair: use the ordinal demand-graded prediction the paper already has at `:1001`**, so shallow nulls and medium positives sit on one curve and both count.

**Should-fix (8):** `:282` *"however functionally enriched"* contradicts the `:372` decompiler · unstated Alexander's-dictum premise; causal exclusion never addressed · `:348` frame-discreteness is an empirical commitment presented as given · `:386`–`:398` ladder rungs individuated by stipulation, and `:398`'s *"not discrete stages"* dissolves the integer rungs `:396` relies on · `:423` "self-consistency" is a **dangling pointer** — §3.4 never defines the term · `:488` extends S10: the independence exhibit is question-begging without a stated closure criterion (the safe one: autoregression returns *output as data*; closure requires the *self-model's content* to enter the *world-model's update rule* — **not** "no weight write-back", since human closure at `:423` is explicit-level state feedback) · `:342` *"the gap is narrower"* needs its premise stated · `:534` converts an objection into confirmation with no discriminator.

**Under-claimed (3):** `:427`'s rank derivation predicts capacity *conservation* across taxa with wildly different neuron counts — a non-obvious quantitative invariance, currently unclaimed (⚠ verify the avian working-memory literature before citing) · `:402`'s base-case regress would give the implicit cells a second independent track and blunt AV-1's circularity charge · `:340`'s disconnection-control criterion is a second operational handle for Table 1b's weakest row.

**Valid as written (do not re-check):** `:423` separability (argued, not asserted — both corners independently instantiable) · `:334`'s conditionalization · **`:336` — "the strongest single argument in §3"** · `:304`–`:314` Stage 1→2→3 · `:402` · `:429`–`:433` · `:472` finite-size objection · `:480` PCI-is-not-criticality · `:486` seizure negative control · `:441` one-directionality · `:259` — **the two-routes concession does NOT weaken the pairing** (commissioned question answered: no) · `:362` · `:526`.

---

## Agent 10 — adversarial pass on the five §3 argument-validity findings

**ALL FIVE REFUTED.** Combined with wave 2's 2-of-4, **seven of the nine "deep" findings this review produced did not survive verification.**

| finding | verdict | why it failed |
|---|---|---|
| **AV-1** *"nothing is posited"* | **REFUTED** | P3 *is* flagged as the posit in its own sentence (`:138`: *"argued for rather than derived"*), and deriving contents from a **disclosed axiom** is not positing. The finding's standard would make every axiomatic system's theorems "posited". The *"relabels"* charge severs `:233` from **the sentence immediately before it**, which supplies exactly the non-emptiness argument alleged missing. And the reafference quote was **clipped** — the full sentence ends *"…to distinguish self-generated from externally generated signals at the substrate level."* |
| **AV-2** regress proves too much | **REFUTED** | The paper scopes the regress to the total case in **both** cited locations, with emphasis in the original (`:255` *"the **entire** structural substrate"*; `:380` *"wherever the **entire** substrate would have to appear as content"*). `:259` re-derives the general case from *"the generative asymmetry"* — the word "regress" does not appear there. And `:380`'s *because*-clause attaches to the generative-asymmetry point, not the regress. **The finding attacked an attribution the paper does not make.** |
| **AV-3** "no residual" / score analogy | **REFUTED** | `:324` glosses "no residual" **in the same sentence** as descriptive accessibility of computed content — a different sense from `:374`'s processual point, which the finding substituted. And the paper draws the score/music distinction itself **six lines later** at `:332`: *"**unlike the score/music case**, the asymmetry here is not merely one of medium but of closure."* |
| **AV-4** `:516` vs `:518` ⭐ | **REFUTED — dissolved by the sentence's own syntax** | `:518` reads *"the **computational prerequisite** is a three-part condition"*. The trichotomy is a decomposition of **one of the two thresholds**, not a third list member. Comparing a threshold count (2) with a within-threshold decomposition (3) is an arithmetic category error. |
| **AV-5** asymmetric evidence | **REFUTED** | The reconciling graded prediction exists and is **symmetric**: `:997`'s easy-task **absence is itself a passed risky test** — had easy tasks shown a band advantage, the specificity claim fails. And the program publishes its own failures: result five is reported *"because it did not fully succeed"*, and `:999` states closure-necessity *"has been falsified five times in this program."* **A structure that cannot fail does not publish decisive-gate failures.** |

⛔ **RANKED BY DAMAGE IF FOLDED IN WRONGLY — read before touching §3:**
1. **AV-4 is the most dangerous.** Its repair would weaken `:516`, **the theory's only sufficiency statement**, or promote the trichotomy to a third threshold — which would *create* the §4.4/§8.7 contradiction the finding falsely diagnoses. **The repair manufactures the disease.**
2. **AV-1** — gutting the *"relabels"* reply concedes the four-model derivation, the paper's central structural claim; a careless re-scope of the reafference sentence risks **re-admitting the three-model alternative**.
3. **AV-2** — would break the correct total-case/general-case division on which the Hard Problem treatment rests.
4. **AV-5** — would remove a confirmed interaction prediction and misrepresent a program that publishes its own failures.
5. **AV-3** — stylistic dilution of an already triple-hedged section.

**What survives: three OPTIONAL one-clause hedges, none blocking deposit** — reafference scope at `:233`, the score-analogy qualifier echoed at `:326`, and an independent ceiling criterion at `:417` (the one real, small completeness gap: 5-HT2A occupancy PET measured independently of the entropy outcome). **⚠ Also confirmed: B7's rename stands, and "the contradiction survives the rename" is false — with the rename, nothing etiological remains in the condition.**

---

# ⭐ THE SESSION'S LESSON, and it is worth more than any single finding

**Seven of nine deep findings were refuted on verification.** The failure mode was identical almost every time: **a quotation that is verbatim-accurate and context-false** — severed from a gloss in the same sentence, a scoping clause in the same paragraph, or a distinction the paper draws a few lines later.

Two of the proposed repairs would have actively damaged the paper:
- the IIT-exclusion paragraph would have committed FMT to **simultaneous** DID experiencers, which §6.2 denies;
- the "by design" gloss for the prerequisite would have **re-admitted the laptop**, the very counterexample the leg exists to exclude;
- and AV-4's repair would have weakened the theory's only sufficiency statement to fix a contradiction that does not exist.

⇒ **Adversarial verification is not a luxury pass on a finished review — on this manuscript it is where most of the value is.** A finding stated with line numbers and a quote still has roughly a one-in-three survival rate. Budget for the verification wave from the start, and never fold a "deep" finding in unattacked.

---

## Agent 11 — `.tex` content-equivalence audit (full, scripted)

⚠ *I stopped this agent in error, misreading a quiet stretch as a stall; it was doing final verification. Resumed with context intact rather than re-run.*

**Verdict: the mirror is structurally faithful — nothing missing or added at paragraph granularity in either direction — but it carries 2 garbled-rendering blockers VISIBLE IN THE CANONICAL PDF, 1 dropped claim-qualifier, 1 claim-nuance divergence, and a 10-site missing-possessive family, all traceable to hand-edited `\citet` usage.**

Alignment: 572 md blocks vs 573 tex, **478 exact-equal** after normalisation; the remaining 63 hunks each verified. All others are renderer artifacts.

### BLOCKERS — all `.tex`-side

**T1 — `tex:643` renders "Aru, Suzuki, and Aru et al. (2020)".** md `:498` reads *"Aru, Suzuki, and Larkum (2020)"*; the tex spells out the author list **and then calls `\citet`**, which renders its own author list. **Verified present in the canonical PDF.**
→ `Aru, Suzuki, and Larkum (\citeyear{AruSuzukiLarkum2020})`

**T2 — `tex:1103` renders "Laukkonen, Friston, and Laukkonen et al. (2025)"** — garbled **and** the possessive is lost. md `:875` is correct. **Verified in the canonical PDF.**
→ `Laukkonen, Friston, and Chandaria's (\citeyear{Laukkonen2025})`

**T3 — `tex:271` Table 1b silently drops `; one-directional`.** md `:194` ends *"Necessary, not sufficient**; one-directional**."* The tex cell ends *"Necessary, not sufficient."* — **a real content loss**, and one-directionality is load-bearing scoping that md `:174` spells out as *"the relation runs one way only"*.

**T4 ⭐ — `tex:244` reasserts the requirement framing the v14 restructure demoted.** md `:174` folds the Class-4 clause into the definition as descriptive apposition (*"the virtual system **operating** at or near the edge of chaos"*); the tex keeps it as a separate later sentence reading *"The virtual system **must operate** at or near the edge of chaos."* Git shows **both files were edited differently in the same commit** (`bad457af`, the AIW-138 v14 restructure) — hand-drift, not staleness. **This is the criticality-is-an-effect ruling leaking back in through the mirror.**

### SHOULD-FIX

**S-T1 — missing-possessive family, 10 sites.** md writes *"X's (year) noun"*; tex uses bare `\citet{}`, rendering ungrammatical *"X (year) noun"*. **The file already contains the correct idiom** (`\citeauthor{Key}\textquotesingle s (year)`, used at the Pinto, Bressloff, Schurger, Libet and Birch sites), so this is mechanical: `tex:99`, `485`, `592`, `614`, `1099`, `1103`, `1105`, `1150`, `1349` (×2) — against md `:58`, `:368`, `:455`, `:470`, `:871`, `:875`, `:877`, `:913`, `:1082` (×2). Four confirmed in the PDF.

**S-T2** — 3 possessive-avoidance rephrases where the tex was hand-written rather than mirrored (md `:879` ×2, `:907`) · **S-T3** — "Section 6.0" cross-refs: the tex renders §6.0 as an **unnumbered** `\subsection*`, keeps `Section~6.0` at `tex:750` pointing at a number that exists nowhere in the built PDF, and silently rewrites three others to `Section~6)`. **Root cause is md-side: a "6.0" label LaTeX cannot produce.** · **S-T4** — `tex:411` renders the cf.-clause dangling outside the parenthesis → `(\citealp{Kawakita2025}; cf.\ \citealp{Kriegeskorte2008})` · **S-T5** — `tex:531`/`533` splits a single md paragraph in two.

### Verified equivalent — no action

**Presence and order: NONE missing or added in either direction at paragraph granularity.** Cleared as false alarms: the AI declaration, the companion-paper tail, all three figure captions, the §3.1.1 `description` environment.
**Numbers, statistics, DOIs: NO mismatches.** All 12 approximation tildes match site-by-site; every §8.9 banked numeral byte-identical modulo math markup; all σ/α/τ thresholds match; **448 tex `\cite*` instances, 0 without a same-work md counterpart.**
**Structure:** 80 body headings both sides, 3 figures, 5 tables, 2 footnotes + 3 table-notes, 249 reference entries 1:1 (bib holds 267; 18 uncited = the known orphan set).

**Notes:** the canonical PDF is one build behind the current `.tex` (still renders the pre-repair "weak illusionism") — **but T1/T2 were verified present in both the current source and the PDF, so they are not stale-build artifacts.** ~14 literal Unicode em-dashes in the tex against its `---` convention (cosmetic). md reference list has 4 alphabetical inversions — cosmetic only, since the rendered bibliography is plainnat-sorted.
