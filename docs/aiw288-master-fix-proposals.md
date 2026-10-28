<!-- Action: reference -->
<!-- Tracked-by: AIW-288 -->
# AIW-288: fix proposals for self-contradictions in the FMT master (v19)

**For MG's review. Nothing in the master or the `.tex` has been edited.**
Date 2026-10-19 (WSL, subagent). Sources: `paper/full/four-model-theory-full.md` (md line numbers below), `paper/full/latex/paper.tex` (tex line numbers; the sentence is the same unless noted). Rules checked against: §3.7.3 l.525 and §4.4 l.639 (four-part sufficient conjunction), §3.5 l.393 (one gate), §3.4.6 l.387 (accessible/accessed), §8.5 l.987 ("basic to simply extended"), `.claude/knowledge/neuroscience-communication.md` (no "gate/gating" for what reaches consciousness), `.claude/knowledge/prose-register.md`, `.claude/knowledge/fmt-misconception-registry.md`.

Priority key: **P-a** contradicts a v19 rule outright; **P-b** collides with a v19 term of art; **P-c** banned word or wording hygiene.

---

## 1. Needs-fix

### A. "Free modelling plus the architecture suffice" (pre-conjunction sufficiency)

v19 rule (§3.7.3 l.525): *"What is sufficient is a conjunction: a system that implements the four models under closure, with free compute, embodiment and at least one pain-pleasure axis, is conscious."*

**A1 — §7.2 Searle, md 883 / tex 1114 — P-a**
- Current: "It contradicts the claim that the right computation is insufficient: on the theory, the architecture with free modeling suffices on any substrate (Section 4.4), and running the computation instantiates the process where a description of it does not (Section 3.4.5)."
- Proposed: "It contradicts the claim that the right computation is insufficient: on the theory, any physical system meeting the sufficient conditions of Section 3.7.3 is conscious, whatever its substrate (Section 4.4), and running the computation instantiates the process where a description of it does not (Section 3.4.5)."
- Why: the two-part sufficiency claim is what §3.7.3 retracts; the replacement points to the conjunction instead of restating it.

**A2 — §4.4, md 657 / tex 830 — P-a**
- Current: "The implication for artificial consciousness is direct: a synthetic system implementing the four-model architecture in the Class 4 regime should produce genuine consciousness."
- Proposed: "The implication for artificial consciousness is direct: a synthetic system that implements the four models under closure, with free compute, embodiment and at least one pain-pleasure axis, is conscious."
- Why: same section, two paragraphs earlier (l.639), states the four-part conjunction; this sentence drops two of its parts.

**A3 — §4.4 (Seth paragraph), md 653 / tex 826 — P-a**
- Current: "Interoceptive-style regulation of a body-model is one route to the ESM; any architecture that sustains self-referential simulation of a modeled body-in-world in the Class 4 regime should qualify, whether the modeled "body" is metabolic tissue or a persistent artificial embodiment."
- Proposed: "Interoceptive-style regulation of a body-model is one route to the ESM; any architecture that sustains self-referential simulation of a modeled body-in-world in the Class 4 regime, with at least one pain-pleasure axis, should qualify (Section 3.7.3), whether the modeled "body" is metabolic tissue or a persistent artificial embodiment."
- Why: "should qualify" reads as a sufficiency claim covering embodiment but omitting the pain-pleasure axis.

**A4 — §8.7 Statement, md 1009 / tex 1262 — P-a**
- Current: "A synthetic system implementing the four-model architecture on a substrate with open-ended (Class 4) computational capability — of which near-criticality is the neural signature — will exhibit consciousness."
- Proposed: "A synthetic system meeting the sufficient conditions of Section 3.7.3 — the four models under closure, free compute in the Class 4 regime, embodiment, and at least one pain-pleasure axis, which may be engineered — will be conscious."
- Why: the implication's own statement is the two-part form; the prediction map (node D8) already follows §3.7.3, so the map is currently stricter than the paper.

**A5 — §8.7 Mechanism, md 1011 / tex 1264 — P-a**
- Current: "Consciousness depends on function — the four models running on a substrate with open-ended (Class 4) computational capability, of which near-criticality is the neural signature — not on material (biological neurons)."
- Proposed: "Consciousness depends on function — the four models under closure, with free compute, embodiment and at least one pain-pleasure axis — not on material (biological neurons)."
- Why: same retired two-part form; the criticality clause is already stated in the Statement and in §3.7.

**A6 — §8.7 Testability, md 1013 / tex 1266 — P-a (new find; also the one-gate rule)**
- Current: "However, intermediate tests are possible: systems with partial implementations (e.g., two models instead of four, or four models without free modeling) should show partial consciousness indicators, detectable through behavioral signatures and neural/computational complexity measures."
- Proposed: "However, intermediate tests are possible: systems with partial implementations (e.g., two models instead of four, or four models without free modeling) should show the component mechanisms of the parts they have and no consciousness, both thresholds being necessary (Section 3.7.3)."
- Why: "partial consciousness" for a system missing a necessary component contradicts both §3.7.3 (each threshold necessary) and §3.5 (phenomenology or none); §8.9, which the next sentence cites, tests component mechanisms, which is what the replacement says.

**A7 — §8.8, md 1019 / tex 1274 — P-a**
- Current: "If the Four-Model Theory is correct, it should be possible to *build* a conscious machine by implementing the specified architecture: four models along two axes (IWM, ISM, EWM, ESM) operating in the Class 4 regime on a substrate of sufficient complexity."
- Proposed: "If the Four-Model Theory is correct, it should be possible to *build* a conscious machine by meeting the sufficient conditions of Section 3.7.3: four models along two axes (IWM, ISM, EWM, ESM) under closure, free compute in the Class 4 regime, embodiment, and at least one pain-pleasure axis."
- Why: two-part form again; the next sentence ("such a system … would *be* conscious") then refers to the conjunction.

**A8 — §10.1, md 1069 / tex 1333 — P-a**
- Current: "The Four-Model Theory provides an engineering specification for artificial consciousness: implement the four-model architecture on a substrate capable of open-ended Class 4 computation — the capability that near-criticality indexes in neural tissue. This is a concrete deliverable, not an abstract philosophical claim."
- Proposed: "The sufficient conditions of Section 3.7.3 double as a specification for artificial consciousness: the four models under closure, free compute in the Class 4 regime, embodiment, and at least one pain-pleasure axis, which may be engineered."
- Why: two-part form; the deleted second sentence is a not-X-but-Y cadence tic (prose register) and invites misreading #6 of the registry (FMT read as a build spec rather than a theory of what consciousness is). The later "built to the theory's specification" (l.1092) and "to the specification" (l.1120) then refer to this corrected text and need no change.

**A9 — §3.2, md 228 / tex 331 — P-c**
- Current: "The 2×2 taxonomy above identifies the *minimum sufficient set* of models for consciousness, not the actual number the brain maintains."
- Proposed: "The 2×2 taxonomy above identifies the *minimum set* of models consciousness requires, not the actual number the brain maintains."
- Why: "sufficient … for consciousness" attached to the four models alone contradicts "the four-model architecture is necessary but not sufficient" (l.525); the sentence's point is the count, which "minimum set" keeps.

### B. "Continuum / graded, not binary" (against the one-gate rule)

v19 rule (§3.5 l.393): *"A system has phenomenology or it has none … Above that gate, consciousness … is graduated along two axes."*

**B1 — §1.3 item 5, md 62 / tex 102 — P-a**
- Current: "The theory defines a principled continuum from simple consciousness (a system that models itself) through triply extended consciousness (a system that models its modeling of its modeling of itself). This provides graded rather than binary criteria for attributing consciousness across species and artificial systems, without ad hoc thresholds."
- Proposed: "The theory sets one criterion for whether a system is conscious at all, self-referential closure, and above it a continuum from minimal through triply extended consciousness (a system that models its modeling of its modeling of itself). This provides one criterion and graded levels above it for attributing consciousness across species and artificial systems, without ad hoc thresholds."
- Why: "graded rather than binary" denies the gate; "simple consciousness" is not a v19 level (§3.5 names minimal and basic).

**B2 — §6.4, md 787 / tex 992 — P-a**
- Current: "The theory's commitments — continuum (not binary), substrate independence, the Class 4 computational regime — predict a **gradient** of animal consciousness determined …"
- Proposed: "The theory's commitments — graduated levels above a single gate, substrate independence, the Class 4 computational regime — predict a **gradient** of animal consciousness determined …"
- Why: direct contradiction of §3.5; the replacement is the wiki's wording (`phenomena/animal-consciousness.md` l.13), and the same section's "The floor" paragraph (l.791) and insect paragraph (l.799) already apply the gate.

**B3 — §6.5 Blindsight, md 818 / tex 1033 — P-a**
- Current: "The theory predicts a gradient, not a binary, so degraded experience in blindsight would be consistent with the framework."
- Proposed: "Above the gate of Section 3.5 the theory grades experience by richness of content, so degraded experience in blindsight would be consistent with the framework."
- Why: the conclusion (degraded experience fits) survives under the one-gate rule because the grading sits above the gate; the "not a binary" premise does not.

### C. "Accessible" in its pre-v19 sense

v19 rule (§3.4.6 l.387): *"Accessible content is poised for report … it is stored on the implicit side, it is not conscious, and it becomes conscious only when a permeability event draws it into the running simulation … Accessed content is in the running simulation."* So "becomes accessible" can no longer mean "becomes conscious", and "inaccessible to experience" now reads as "not even preconscious".

**C1 — §3.6 list, md 417 / tex 551 — P-b**
- Current: "Global increase in permeability — intermediate processing stages (normally implicit) become accessible to the explicit models."
- Proposed: "Global increase in permeability — intermediate processing stages (normally implicit) enter the explicit models."
- Why: the stages become conscious, which v19 calls *accessed*, not *accessible*.

**C2 — §3.6 list, md 420 / tex 554 — P-b**
- Current: "Trained modulation of permeability, enabling selective access to normally implicit processes."
- Proposed: "Trained modulation of permeability, drawing normally implicit processes selectively into the simulation."
- Why: "access to" is ambiguous between the two v19 terms; the meant sense is *accessed*.

**C3 — §6.1, md 742 / tex 939 — P-b**
- Current: "Intermediate processing stages — normally implicit and inaccessible — leak through to the simulation."
- Proposed: "Intermediate processing stages — normally confined to the implicit side — leak through to the simulation."
- Why: keeps the old accessible = conscious pairing that C4–C5 remove; replacement is the wiki's (`mechanisms/variable-permeability.md` l.21).

**C4 — §6.1 dose list, md 744–747 / tex 942–945 — P-b**
- Current (four bullets): "V1-level processing becomes accessible →" · "early visual processing becomes accessible →" · "Higher visual area processing becomes accessible →" · "Full intermediate processing accessible →"
- Proposed: "V1-level processing enters the simulation →" · "early visual processing enters the simulation →" · "Higher visual area processing enters the simulation →" · "Full intermediate processing in the simulation →"
- Why: each step is content becoming conscious (*accessed*), the event §3.4.6 reserves for a permeability event.

**C5 — §6.1, md 749 / tex 948 — P-b**
- Current: "… lower-level (earlier, simpler) processing stages become accessible before higher-level (later, more complex) ones, because the permeability increase propagates up the hierarchy."
- Proposed: "… lower-level (earlier, simpler) processing stages enter the simulation before higher-level (later, more complex) ones, because the permeability increase propagates up the hierarchy."
- Why: as C4.

**C6 — §6.2, md 771 / tex 972 — P-b**
- Current: "… psychedelics globally increase permeability (making the implicit accessible), while anosognosia locally decreases permeability (making a specific aspect of the implicit inaccessible)."
- Proposed: "… psychedelics globally increase permeability (drawing implicit content into the simulation), while anosognosia locally decreases permeability (keeping one domain of it out)."
- Why: the deficit information in the ISM is *accessible* in the v19 sense (stored, preconscious); what anosognosia blocks is its entry into the simulation.

**C7 — §8.2 Mechanism, md 955 / tex 1200 — P-b**
- Current: "This is the exact inverse of the psychedelic mechanism described in Section 6.1: psychedelics make the implicit accessible, anosognosia makes it inaccessible, and the two should interact predictably."
- Proposed: "This is the exact inverse of the psychedelic mechanism described in Section 6.1: psychedelics draw implicit content into the simulation, anosognosia keeps one domain of it out, and the two should interact predictably."
- Why: as C6; this is Prediction 1's own derivation, so the term matters most here.

**C8 — §3.8, md 539 / tex 693 — P-b**
- Current: "The ISM (Implicit Self Model) is **structurally inaccessible** to the ESM (Explicit Self Model)."
- Proposed: "The ISM (Implicit Self Model) is **structurally opaque** to the ESM (Explicit Self Model)."
- Why: ISM content can be accessible and is drawn into the ESM (the anosognosia account depends on it); what the meta-problem needs is that the substrate cannot appear as itself, which the same paragraph already calls "a principled opacity" and §7.4 item 5 calls "the ESM's opacity to its own substrate".

**C9 — §7.2 AST, md 871 / tex 1102 — P-b**
- Current: "… AST's Meta-Problem insight — the ESM's structural inaccessibility to its own substrate — …"
- Proposed: "… AST's Meta-Problem insight — the ESM's structural opacity to its own substrate — …"
- Why: as C8; matches §7.4 item 5 word for word.

**C10 — §3.2/§3.3, md 234 / tex 337 — P-c**
- Current: "… are on the substrate side of the generative divide and therefore not directly accessible to experience."
- Proposed: "… are on the substrate side of the generative divide and therefore never directly experienced."
- Why: "accessible to experience" uses the pre-v19 sense; the claim (stored content is not conscious) is what §3.4.6 says of accessible content.

**C11 — §3.3, md 258 / tex 367 — P-c**
- Current: "The implicit models are structurally inaccessible to direct experience — and this is not a contingent limitation but a consequence of their architectural role."
- Proposed: "The implicit models are structurally excluded from direct experience — and this is not a contingent limitation but a consequence of their architectural role."
- Why: as C10. (The not-X-but-Y tail is pre-existing; left alone to keep the change minimal.)

**C12 — §3.3, md 262 / tex 371 — P-c**
- Current: "… once it resides in the structural substrate, the generative asymmetry renders it inaccessible to direct experience."
- Proposed: "… once it resides in the structural substrate, the generative asymmetry excludes it from direct experience."
- Why: as C10.

### D. Lucid-onset level

**D1 — §6.3, md 783 / tex 986 — P-a**
- Current: "… lucid onset corresponds to the ESM crossing from basic consciousness (experiencing *as* an agent) to extended consciousness (experiencing *that* one is an agent experiencing)."
- Proposed: "… lucid onset corresponds to the ESM crossing from basic consciousness (experiencing *as* an agent) to simply extended consciousness (experiencing *that* one is an agent experiencing)."
- Why: harmonises with §8.5 l.987 ("from basic to simply extended consciousness — a threshold") and with §3.5's definition of simply extended ("aware that it experiences"), which the parenthesis already paraphrases.

### E. "Gate / gating" for what reaches consciousness (banned)

Rule (`neuroscience-communication.md`): *"Never 'gated by' / 'a gate' / 'gating' in this context … Nothing stops any signal from reaching consciousness."* Replacement word used throughout: *selection* / *set*, which §3.6.1 l.438 already uses ("attention selects its occupancy") and which the prediction map adopted (nodes D5, F8). **MG call:** "selection" and the OQ7 paragraph's "filtered" still describe something admitting or excluding content, which the emergence framing of that rule also rejects; if that is too strong, OQ7 needs rewording beyond word swaps.

**E1 — Table 1 Permeability, md 168 / tex 239 — P-c**
- Current: "Low permeability: tight gating preserves simulation coherence (focused waking)."
- Proposed: "Low permeability: narrow selection preserves simulation coherence (focused waking)."
- Why: banned word in the definition of the construct itself.

**E2 — §3.6, md 413 / tex 546 — P-c**
- Current: "… relevant information passes through based on attentional and contextual gating."
- Proposed: "… relevant information passes through according to attentional and contextual selection."
- Why: banned word; §3.6.1 already describes attention as selection into the channel.

**E3 — §3.6.1 Fourth, md 440 / tex 578 — P-c**
- Current: "Section 9 (Open Question 7) asks by what moment-to-moment mechanism permeability is gated; the channel gives that question a shape, since a gate on a narrow path is a far more tractable object than a gate on a boundary of unspecified width."
- Proposed: "Section 9 (Open Question 7) asks by what moment-to-moment mechanism permeability is set; the channel gives that question a shape, since selection on a narrow path is a far more tractable object than selection across a boundary of unspecified width."
- Why: three uses of the banned word in one sentence.

**E4 — §9 OQ7, md 1061 / tex 1321 — P-c** (five edits in one paragraph)
- "**7. The basal ganglia role in permeability gating.**" → "**7. The basal ganglia role in setting permeability.**"
- "… the moment-to-moment *mechanism* by which implicit-to-explicit transfer is gated." → "… the moment-to-moment *mechanism* by which implicit-to-explicit transfer is set."
- "… while the basal ganglia evaluate these candidates against prediction-error signals before gating their entry into the explicit simulation." → "… while the basal ganglia evaluate these candidates against prediction-error signals and select which enter the explicit simulation."
- "If the prediction-error gate is too permissive, …" → "If the prediction-error selection is too permissive, …"
- "… producing hallucinations (false sensory candidates pass gate) …" → "… producing hallucinations (false sensory candidates selected) …"
- Why: the open question is where the master uses the banned word most; the wiki's open-questions page copies it (see §3).

**E5 — §11, md 1116 / tex 1389 — P-c**
- Current: "… and the basal ganglia's potential role as a prediction-error-based permeability gate."
- Proposed: "… and the basal ganglia's potential role in setting permeability through prediction error."
- Why: banned word, repeated from OQ7.

**E6 — §7.2 IIT, md 863 / tex 1094 — P-c**
- Current: "… FMT locates it in that running, substrate-neutral, autonomously recruited, closure-gated updating."
- Proposed: "… FMT locates it in that running, substrate-neutral, autonomously recruited, closed-loop updating."
- Why: the banned word in FMT's own description of what consciousness is.

**E7 — §6.3, md 781 / tex 984 — P-c (lowest; "thalamic gating" is a field term)**
- Current: "… external sensory input is attenuated by thalamic gating and motor output is separately blocked by brainstem-mediated atonia … The gating and the atonia are established sleep physiology; …"
- Proposed: "… external sensory input is attenuated at the thalamus and motor output is separately blocked by brainstem-mediated atonia … The thalamic attenuation and the atonia are established sleep physiology; …"
- Why: the context is sensory signal reaching the simulation, the case the rule names; "attenuated" already carries the physiology.

**E8 — §7.2 Enactivism, md 885 / tex 1116 — P-c (lowest)**
- Current: "… dreaming runs on internally generated input while sensory input is gated and motor output blocked (Section 6.3)."
- Proposed: "… dreaming runs on internally generated input while sensory input is attenuated and motor output blocked (Section 6.3)."
- Why: same as E7, and keeps the two passages consistent.

### F. Mechanism credited for Prediction 1 (and 3)

**F1 — §7.4 item 3, md 917 / tex 1154 — P-a**
- Current: "3. **The redirectable ESM**: Unique mechanism for connecting psychedelics to anosognosia (Prediction 1), for identity-content determination during ego dissolution (Prediction 2), and for the self-referential representational gradient across alter states in DID (Prediction 3)."
- Proposed: "3. **The redirectable and forkable ESM**: Unique mechanism for identity-content determination during ego dissolution (Prediction 2, by redirection) and for the self-referential representational gradient across alter states in DID (Prediction 3, by forking)."
- Why: the derivation lines say otherwise — §8.2 l.955 runs Principle 2 → permeability → Prediction 1 with no redirection step, and §8.4 l.977 runs Principle 1 → forking → Prediction 3. Prediction 1 is already item 4 ("Variable permeability links these phenomena"). The Prediction 3 half is a new find beyond the prediction-map audit.

---

## 2. Fine as is

### "suffic*" (29)
| md | Use | Reason |
|---|---|---|
| 17, 137, 240 | "of sufficient complexity" | Principle 2's regime condition, not a consciousness-sufficiency claim. |
| 156 | "neither necessary nor individually sufficient conditions" | About observables. |
| 176, 196, 448 | "Free modeling is necessary and not sufficient" | States the v19 rule. |
| 207 | "minimum-sufficiency argument" | Names the argument that closure needs four models; no claim that four models suffice for consciousness (contrast A9). |
| 305, 377, 529, 897, 1094 | "sufficiently rich/detailed/complex" | Generic. |
| 422 | "qualitative framework is sufficient to generate the predictions" | Methodological. |
| 525, 639 | the conjunction | Canonical v19 statements. |
| 609, 615, 623, 1021 | recursive depth / elaborated world-model / moral status / intelligent systems | Unrelated to consciousness sufficiency. |
| 649 | "capability alone … does not suffice" | Consistent with §3.7.3. |
| 793 | "rudimentary self-simulation sufficient for phenomenal experience" | Describes basic consciousness, a level already above the gate. |
| 873 | "The two theories conflict on sufficiency" (RPT) | Rejects local recurrence as sufficient; consistent. |
| 911 | "Self-location is necessary but not sufficient" | Consistent. |
| 54 | "Consciousness is identified with the self-referential self-simulation that a cortical substrate sustains when it operates in the Class 4 regime" | Identity statement scoped to cortex, whose bodies supply embodiment and valence; not a substrate-general sufficiency claim. |
| 641 fn | "one functional specification … can be satisfied by more than one physical architecture" | Multiple realizability, not sufficiency. |
| 1092, 1120 | "built to the theory's specification" | Correct once A8 is applied. |
| 1108 | "consciousness is an ongoing self-simulation … running on a substrate capable of open-ended computation" | Restates the §3.1 definition of what consciousness is, not what suffices. |

### "binary / continuum / graded" (6)
| md | Reason |
|---|---|
| 405 | "points along a continuum" sits after §3.5's gate sentence, i.e. above the gate. |
| 911 | "FMT's self-referential closure is a single binary criterion" agrees with the gate; "clean binary" concerns IWMT's substrate stance. |
| 812 | "basic phenomenal consciousness preceding extended" grades above the gate. |
| 987 | "a threshold, not a gradient" (lucid onset) agrees. |
| 413, 426 | "graded filter" / "graded transition zone" describe the permeability boundary, not whether a system is conscious. |

### "accessible / access" (9, plus Block/GNW mentions)
| md | Reason |
|---|---|
| 203 | "empirically accessible" — epistemic. |
| 329 | "symmetrically accessible" to an external observer — epistemic. |
| 387 | The v19 definitions themselves. |
| 543 | "introspective access" — ordinary sense, no term-of-art collision. |
| 601 | "inaccessibility of a capability to architectures" — about capabilities. |
| 635 | "accessible only through instantiation" — epistemic. |
| 763, 765 | "conscious access, on the best available report measure" — Block's access, as the report measure. |
| 1059 | "not directly accessible from external observation" — epistemic. |
| 33, 90, 98, 857, 865, 873 | Block/GNW "access consciousness" — the literature's term, which §3.4.6 splits. |

### "extended" (7)
| md | Reason |
|---|---|
| 357 | Damasio's "extended consciousness" — his term. |
| 389, 399–403 | §3.5's own ladder. |
| 783 (2nd) | "extended ESM operation" — generic for the rungs above basic. |
| 793 | "basic or simply extended" (rodents) — consistent. |
| 808 | Table 4 "mammals (basic to extended)" — a range across species, consistent with l.793's rodents-to-primates span. |
| 812, 867 | Generic "extended rungs". |

### "gate / gating" (7)
| md | Reason |
|---|---|
| 283 | "logic gates" — transistors. |
| 343 | "A gate that a confabulator passes" — a test criterion, not a mechanism on signals. |
| 393 | "Above that gate" — the one-gate classification itself; the wiki uses the same word for it throughout (`mechanisms/graduated-consciousness.md`, `glossary.md`). |
| 579, 581 | Plasticity gating of consolidation (Pawlak & Kerr; Hong et al.) — write-back into the substrate, not entry into consciousness. |
| 595 | "whether motor output is gated" / "two gating regimes" — motor output. |
| 1029 | "self-model-gated planner", "the gate the program treats as decisive", "demand-gated" — in-silico program vocabulary. |

### "redirect*" (6)
| md | Reason |
|---|---|
| 720 | Lists where redirection does work (6.1, 6.2, 8.3) — excludes 8.2, consistent with F1. |
| 767 | Cotard's — redirection, correct. |
| 969, 971, 1078 | Prediction 2 — the one prediction redirection derives. |
| 1082 | "criticality, redirectable ESM, variable permeability" — lists three mechanisms, no attribution. |

---

## 3. Wiki agreement

**Already carries the corrected reading** (the next master version and these pages agree once §1 is applied):

| Item | Wiki pages |
|---|---|
| A (conjunction) | `comparative/further-theories.md` l.31 (Searle, wording reused in A1), `philosophical/substrate-independence.md` l.43 (wording reused in A2), `physical-foundations/two-thresholds.md`, `ai-consciousness/ai-welfare.md` l.35/69/73, `ai-consciousness/llms-not-conscious.md` l.13, `ai-consciousness/engineering-specification.md` l.19 (body), `reference/glossary.md`, `comparative/theory-map.md`, `comparative/vs-iit.md`, `foundations/overview.md` |
| B (one gate) | `mechanisms/graduated-consciousness.md`, `mechanisms/minimal-consciousness.md`, `phenomena/animal-consciousness.md` l.13 (wording reused in B2), `core-architecture/core-definition.md` l.29, `predictions/white-box-trace.md`, `reference/glossary.md` l.96, `open-questions/minimum-configuration.md` l.13. No wiki page says "not binary". |
| C (accessible/accessed) | `basics/phenomenal-consciousness.md` l.38, `comparative/vs-gnw.md` l.39, `mechanisms/variable-permeability.md` l.21 (wording reused in C3) |
| D (simply extended) | `predictions/prediction-4-lucid-dreaming.md` l.21 |
| F (redirection ≠ Prediction 1) | `mechanisms/redirectable-esm.md`, `predictions/prediction-1-anosognosia.md` (both derive P1 from permeability only) |

**Still carries the old reading** — so the backlog note "the wiki already follows the corrected readings" holds only in part. These would need the same edits to match:

| Item | Wiki page and line | Old wording |
|---|---|---|
| A | `ai-consciousness/engineering-specification.md` l.5, l.11 | "four-model architecture on a substrate with free compute" (lead; the body at l.19 is correct) |
| A | `ai-consciousness/ai-welfare.md` l.45 | "implements the four-model architecture in the Class 4 regime would be conscious" |
| A | `limitations/other-minds.md` l.13 | "implement the four-model architecture on a substrate with open-ended (Class 4) computational capability" (copies §10.1) |
| A | `open-questions/multi-level-substrate.md` l.37 | "A digital computer running the right algorithm would be conscious." |
| C | `phenomena/psychedelics.md` l.21–23, 26, 65 | "becomes accessible" (copies §6.1) |
| C | `hard-problem/meta-problem.md` l.17 | "structurally inaccessible" (copies §3.8) |
| D | `phenomena/lucid-dreaming.md` l.5, l.11; `phenomena/sleep.md` l.78 | "basic to extended" (copies §6.3) |
| D | `phenomena/animal-consciousness.md` l.5, 11, 85 | "basic to extended" — a species range, consistent with md 808; no change needed |
| E | `mechanisms/implicit-explicit-boundary.md` l.17, 52; `mechanisms/variable-permeability.md` l.65; `phenomena/meditation.md` l.17, 52 | "attentional and contextual gating" / "selective gating" (copies §3.6) |
| E | `open-questions/overview.md` l.6, 41, 43, 65 | "Permeability Gating", "miscalibrated gate" (copies OQ7) |
| E | `phenomena/sleep.md` l.76; `phenomena/lucid-dreaming.md` l.17; `comparative/further-theories.md` l.33 | "thalamic gating" / "sensory input is gated" (copies E7/E8) |

Also outside the wiki: `.claude/knowledge/fmt-misconception-registry.md` misread #6 still says "necessary+sufficient architecture (free modeling + four-model closure …)", the pre-conjunction form, and misread #1 says "minimum sufficient set" (A9). Neither edited here.

---

## 4. Count summary

| Group | Needs-fix | Fine as is |
|---|---|---|
| A. Sufficiency | 9 (A1–A9) | 29 |
| B. Binary / continuum | 3 (B1–B3) | 6 |
| C. Accessible | 12 (C1–C12) | 9 |
| D. Extended | 1 (D1) | 7 |
| E. Gate / gating | 8 (E1–E8) | 7 |
| F. Redirection credit | 1 (F1) | 6 |
| **Total** | **34** | **64** |

By priority: **P-a 13** (A1–A8, B1–B3, D1, F1), **P-b 9** (C1–C9), **P-c 12** (A9, C10–C12, E1–E8). C4 (four bullets) and E4 (five edits in one paragraph) each count as one item.

Every needs-fix item has a located `.tex` counterpart, found by matching a distinctive phrase of the md sentence; the `.tex` renders dashes as `---` and citations as `\citep{}`, so apply each replacement to both files by hand rather than by string substitution.
