<!-- Action: reference -->
<!-- Tracked-by: AIW-236 — all 17 blockers + 167 should-fixes folded in 2026-08-25 -->
<!-- Tracked-by: AIW-236 -->
# FMT v15 — the mandatory pre-publish Fable review

**Run S309, 2026-08-24.** Six Fable agents, read-only, each given
`docs/reviews/2026-08-24-fmt-citation-audit.md` so nothing already repaired was re-found. Five section
reviewers plus one whole-paper cross-section pass.

---

> ## ✅ STATUS 2026-08-25 — ALL 17 BLOCKERS CLOSED (`ac325c14`, `a2be9fb9`, `17472fa3`).
>
> **MG ruled 2026-08-25: *"criticality is a effect, fix."*** That settled the entire directionality
> cluster in one word — the requirement is open-ended Class 4 computation, criticality is the neural
> effect it leaves — and it is applied at all twelve sites where the two readings disagreed.
>
> **MG also ruled on the `AIW-220` leftovers: *"i have no problem with the word return as long as it is
> not contrary to established subject terms."*** ⇒ **Group C stays as written.** `return-freedom` is
> glossed inline (*"no closed walk anywhere"*) and sits beside the paper's own `acyclicity`, so it does
> not contradict a field term. `AIW-220` is closed.
>
> **Erratum: MG ruled "full package"** — v15's erratum covers every repair in this review and the S307
> package together.
>
> **The last one is closed too.** MG accepted the commitment on the unfolding argument at `:859` —
> *"it commits the paper to defending the demarcation on efficiency grounds - yes"* — so the passage now
> states the target correctly (the argument catches IIT **and** FMT), concedes that its force is
> epistemic rather than architectural, and answers it on cost: unfolding trades a reused loop for
> replicated stages, and §8.9 prices that. Under a resource bound the two systems do not agree on
> behaviour after all. The passage says plainly that this does not *dissolve* the argument — it converts
> an unfalsifiable distinction into an empirical one, and on an unbounded substrate the theory has no
> experiment to offer. **Every figure cited was already in §8.9; no new number was imported.**
>
> **Also closed while here:** the three half-applied repairs, now swept **by pattern** rather than by
> line number, which was this review's headline finding.
>
> ⚠ **One repair of mine was caught by the test suite**, and the catch is worth recording: my Conclusion
> edit wrote *"the criticality requirement"*, which `test_criticality_is_not_called_a_requirement`
> (`AIW-138`) bans by exact string. Replaced with the paper's own established phrase, *"criticality
> commitment"*. The guard did precisely the job it was written for.

## ⛔ ORIGINAL VERDICT (2026-08-24): v15 DOES NOT PUBLISH. Seventeen blockers.

The review did the job it was run to do. **The most useful thing it found is not any single defect but a
pattern: three of the repairs made in earlier sessions were applied at some of their sites and not all
of them, and the unrepaired sites are still in the paper.** A defect class is not closed when the
instances someone happened to grep are closed.

**Three incomplete repairs, each now with named surviving instances:**

| repair | fixed at | still wrong at |
|---|---|---|
| Hengen & Shew credited with the criticality–**consciousness** link (audit finding 9) | `:174`, `:887` | **`:455`, `:470`, `:839`, `:58`** |
| Kawakita group-level vs cross-individual (audit finding 5) | `:298`, `:947`, `:951` | **`:1074` (the Conclusion)** |
| Katlowitz context: sedation → general anaesthesia (audit finding 15) | first half of `:747` | **the tail clause of the same sentence** |

⇒ **Before the next publish attempt, every audit finding should be re-swept by pattern across the whole
file, not by line number.**

---

## The fourteen blockers

### Cluster 1 — criticality directionality (5 blockers, the paper's own stated rule)

The paper states the rule correctly at `:174` and `:441` (*"the relation runs one way only: absent
criticality, no consciousness, never the converse"*) and then breaks it five times.

1. **`:66`** — *"adding a physical **prerequisite** (criticality)"*, contradicting the abstract at `:17`
   (*"near-criticality is the **signature** … rather than the requirement itself"*) and §3.7's own
   heading. "Prerequisite" is the exact word the abstract was written to retract. Also **`:54`**,
   *"(CA at criticality)"*, imports the neural signature into the definition.
2. **`:476`** — *"any manipulation that restores them should restore it"*. The banned converse, stated
   14 lines after the paper disclaims it.
3. **`:455` and `:470`** — *"consciousness tracks criticality"* / *"confirmed the criticality-consciousness
   link"*. Both the Hengen & Shew misattribution **and** a biconditional-shaped verb.
4. **`:486`** — *"'how much brain is conscious' … the Class 4 extent"*, equating critical extent with
   conscious extent.
5. **`:674`** — *"Consciousness tracks the substrate's position relative to the critical point."*

### Cluster 2 — barrier-shaped sentences (3 blockers)

The licensed form is a **price**, never a **barrier**. §4.2.4 states this in the paper's own voice:
*"The theory claims no operation that unconscious processing is barred from."*

6. **`:352`** — *"no blending of frames … Information passes through but does not accumulate"*. A
   capability barrier, and **false of the paper's own chosen example**: a weather simulation is exactly a
   state-carrying system whose every frame depends on the last.
7. **`:560`** — *"it no longer evaluates consequences or adapts its behavior"*. Bars two operations the
   paper itself attributes to the substrate at `:598`.
8. **`:993`, sixth banked result** — *"closure **cannot be removed** … only relocated"*, falsified by its
   own next numbers: return-freedom costs 74.0%/71.5%, which is removal, priced.

### Cluster 3 — factual and attribution errors (4 blockers)

9. **`:368`, `:366` — Frankish's position is inverted.** The text describes **strong** illusionism
   (phenomenality itself is the illusion, quasi-phenomenal states misrepresent themselves) and calls it
   **weak** illusionism, three times, in a named engagement. Weak illusionism grants genuine phenomenal
   properties. Any philosophy referee checks this. The argument survives the relabel unchanged.
10. **`:164`, Table 1** — asserts *"sustained DMN and frontoparietal **co-activation** during rest
    (Raichle et al., 2001)"*. Raichle 2001 contains neither frontoparietal co-activation nor propofol;
    and DMN/frontoparietal are **anticorrelated** at rest per Fox et al. 2005, **which this paper cites
    approvingly at `:899`**. The paper contradicts its own reference list, in the operational-definitions
    centrepiece.
11. **`:859` — the unfolding argument is characterised backwards, twice.** IIT identifies consciousness
    with causal *structure* and explicitly denies the I/O identification; that denial is what the argument
    targets. As written, FMT's claimed escape is the same move IIT makes. The real objection to answer is
    the **epistemic** one: if two systems agree on all I/O, what experiment separates them — and §8.9's
    price results are the available answer.
12. **`:445`** — *"mathematically impossible for criticality to arise from a substrate whose intrinsic
    dynamics are below Class 4"*, with no proof, and **the paper supplies the counterexample 27 lines
    later** at `:472` (a finite Game of Life grid is technically Class 2 yet exhibits Class 4 behaviour).

### Cluster 4 — evidence overreach (2 blockers)

13. **`:747`** — one sentence now says both *"general anaesthesia"* and *"during **sedation**"*, because
    the audit repair fixed the first half only.
14. **`:747`** — *"even as phenomenal consciousness was abolished"*, asserted from a **zero-recall**
    measure. Absence of recall is not absence of experience, and the paper's own Table 4 classifies
    ketamine anaesthesia as *"Present, disconnected"*.

---

### Cluster 5 — back matter, which journals check mechanically (2 blockers)

15. **`:1094` vs `:1015` — the Data Availability statement is false on the paper's own face.** It says
    *"No new data were generated or analysed"*, while §9 reports *"a reanalysis of openly available
    metacognition data … 20 independent perceptual datasets … 2,752 participants … pooled r = −0.03;
    per-dataset median r = −0.14"*. A reanalysis producing pooled statistics **is** analysis. ⚠ **And the
    pooled-r figures are currently uncited, so they read as the author's own** — if they are someone
    else's published reanalysis, that source is missing.
16. **`:1104` vs `:1088` — the generative-AI declaration is weaker than the Acknowledgments.** The
    Acknowledgments admit *"prose drafting from the author's directions"*; the declaration, which is the
    operative statement, says only *"refine editorial presentation"*. One manuscript describing the same
    tool use at two strengths. The declaration must be a superset.

### Cluster 6 — one more barrier, found independently by two reviewers

17. **`:396`** — *"**only a system capable of** modeling its own modeling of its own experience **can
    formulate the question** 'What is consciousness?'"*. Banned barrier form, contradicted by §4.2.4's
    *"Stated as a barrier it is false; stated as a price it is both true"*, **and** by the paper's own
    `:338`, which concedes that any language-model periphery readily confabulates exactly such strings.
    Producing the question is cheap; meaning it is the claim.

---

## ⚠ Where the reviewers DISAGREE — do not treat this file as consensus

**On criticality directionality, the section reviewers and the whole-paper reviewer reached opposite
verdicts, and the disagreement is not resolved here.** The §3 reviewer graded `:455`/`:470`
(*"consciousness tracks criticality"*, *"confirmed the criticality-consciousness link"*) as BLOCKERs on
the grounds that "tracks" is biconditional-shaped. The whole-paper reviewer concluded the opposite —
that *"the one-directionality rule is not violated as a biconditional anywhere"*, reading those
occurrences as descriptive of the empirical literature and paired with the one-directional qualifier
where the theory speaks.

**They agree on the half that matters and is not a judgement call:** Hengen & Shew are credited with a
consciousness conclusion their meta-analysis does not draw, at four sites. That is a misattribution
either way. **The directionality question is a wording call and it belongs to MG.**

---

## ⚠ The one defect this session introduced, and its resolution

**`:993`, the τ_syn scope clause pasted today.** The reviewer caught two real problems, and crucible's
own record (`~/crucible/docs/results/cru69-tau-syn-scope.md`) resolves both:

- **"two of three content conditions" reads as contradicting the same paragraph's "four content
  conditions".** Both numbers are right and they are different measurements: the span-equals-support
  finding ran on four conditions; the τ sweep ran on **three supports — `world`, `world+body`,
  `integrated`**. The paper must say so, or the juxtaposition reads as an error.
- **The third condition's outcome was silently omitted, which reads as selective reporting.** It should
  not have been: at τ = 10, **`world` remains fully adjudicable and every loop arm reaches at
  unchanged cost** (96,000 / 160,000 / 224,000 / 288,000, identical across τ = None, 2 and 10). That is
  a *positive* result and omitting it understated the finding.
- **A third point worth taking:** the clause says the result "reproduces unchanged" without saying what
  it originally ran at. It ran at **τ_syn = None**, no synaptic filter — so this is a genuine robustness
  claim, not a vacuous re-run, and saying so is what makes it one.

⇒ **Lesson, and it is the transferable one: an MG-approved clause is approved for its content, not for
its fit with the paragraph it lands in.** The clause was pasted verbatim as instructed and the verbatim
paste is what created the apparent contradiction. Check approved text against its destination.

**✅ REPAIRED S309 the same session, from crucible's own record.** The clause now names the three
supports the sweep ran, reports that the world support stays adjudicable at unchanged cost, and states
that the campaign originally ran without a synaptic filter — which is what turns "reproduces unchanged"
into a robustness claim rather than a re-run. This is the only blocker on this list that is closed.

---

## Cross-section findings worth carrying (whole-paper reviewer)

- **`:1019` vs `:492`–`:498`** — §9's Open Question 5 states the five-system hierarchy in a **different
  order** than §3.7.1 (electrochemical arising from proteomic+topological rather than from physical),
  and calls the virtual system *"the cortical automaton that hosts the four models"* — but §3.7.1 puts
  the implicit models at Level 4, and §3.7.2 says *"the cortical automaton is not consciousness"*, the
  automaton being medium and the models content.
- **`:48` vs Table 5** — the Introduction says the theory *"addresses all eight"* requirements; the
  paper's own table rates it ◐ (partial) on three, and `:298` insists the Hard-Problem treatment stay ◐.
  In the paper's own vocabulary "addresses" is the ● term.
- **`:1042` vs `:951`** — §10.2 calls Prediction 4 *"achievable with established lucid-dreamer paradigms
  and high-density EEG"*; §8.5 says its testability *"depends on methodological advances … not yet
  mature"*.
- **`:1074` vs `:963`** — the Conclusion says Prediction 5's structural claim *"is already demonstrated"*;
  §8.6 scopes it to the group level and says the individual-level arm *"remains to be tested"*. Same
  hedged-in-body/flat-in-conclusion shape as the gamma case already fixed.
- **`:685` vs `:472`/`:1060`** — Table 4 lets psychedelics be *"At/past critical"* with consciousness
  *"Present, altered"*, while §3.7 and §10.3 make supercritical runaway incompatible with consciousness.
  The intended distinction is presumably slightly-past-critical versus runaway; no text draws it.
- **`:993` vs `:781`** — *"closure necessity … has been falsified five times"* is unqualified. It means
  necessity for input-output **capability**; `:781` asserts necessity for **phenomenality**. A reviewer
  can quote one against the other. Add the qualifier.
- **`:790`** — a cross-reference pointing at Section 7 for the theory-of-mind claim, which lives in §6.4
  and §4.2. Section 7 has no ToM treatment. (The only bad pointer found in a sampled sweep.)
- **`:981`, `:1070`** — *"four nested models"*, but §3.2 says only scope nests; mode is orthogonal.

**Verified clean by the cross-section pass, and worth knowing:** the "virtual" declaration holds
essentially everywhere; every paired number checks (PCI 0.31, σ ≈ 0.98, DFA 0.6–0.9, ~140 datasets,
20 Hz, the §8.9 figures); the global-loop vs region-self-loop closure distinction is maintained where it
matters; the S307 lucid-dream gamma hedge took and is now consistent across §6.3 and §8.5; the
independent-causal-power stance is identical in all four places it appears; and the Abstract's promises
are all delivered by the body.

---

## Should-fix, by section (~50 items — full text in the session record)

Not reproduced in full here; the ones a hostile referee leads with:

- **`:656`** — Gray et al. and Fries proposed gamma synchrony *as* the binding mechanism, and are cited as
  pointing away from "a dedicated binding mechanism". Same inversion class as the Pinto defect.
- **`:789` vs `:683`** — the criticality table's own new evidence is avalanches in **anaesthetized** cat
  cortex, while Table 4 says anaesthesia forces subcriticality. A near-critical unconscious preparation,
  unaccommodated. (Two honest outs exist: anaesthetic identity, and the paper's own Kanders caveat that
  avalanche criticality ≠ edge-of-chaos.)
- **`:843`, `:865`** — "consciousness = Φ" is a characterisation IIT proponents reject, and **`:845`
  states it correctly**, so the paper disagrees with itself.
- **`:923`** — *"IIT, GNW, HOT, PP, and AST are all silent"* on the anosognosia prediction. REBUS derives
  the coarse version in one step. With a desk rejection already on record for "predictions too general",
  an unacknowledged shared prediction is the expensive kind of error.
- **`:761`, `:690`, `:737`** — retrodictions presented as confirmed predictions ("this prediction is
  borne out by…" for NREM dreaming, established decades before the theory).
- **`:206` vs `:215`** — the paper denies scope is orthogonal, then Figure 1's caption asserts "two
  orthogonal axes".
- **`:282` vs `:372`/`:380`** — *"cannot be recovered from any substrate-level description"* against *"in
  principle reconstructable"* and *"the substrate description entails the experience"*. The intended
  distinction (recoverable-as-description vs had-as-instance) is drawn well at `:372`; `:282`'s wording
  contradicts it. **Graded BLOCKER by one reviewer, should-fix by scope — treat as a blocker.**
- **`:700`** — §6.0 is `####` while its siblings §6.1–§6.5 are `###`. Wrong sectioning depth.
- Prose register: **"load-bearing" survives three times** (`:441`, `:522`, `:634`), plus sentence-initial
  *"Crucially,"* (`:406`) and *"Importantly,"* (`:419`), and *"A theory is only as valuable as the
  predictions it generates"* (`:891`).

---

## What needs MG, and what does not

**Does not need MG — mechanical, follows existing rulings:** the three incomplete repairs; the Frankish
relabel; the DMN/Raichle row; "load-bearing" ×3; the two banned adverbs; the §6.0 heading level; the
τ_syn clause repair above.

**Needs MG:**
1. **The criticality wording package.** Five sites, one decision: is criticality a *signature* (abstract,
   §3.7) or a *prerequisite* (`:66`)? The abstract's version is the theory's current position, so this is
   a sweep — but it touches the paper's showcase paragraph and one banked-result gloss.
2. **The unfolding-argument response** (`:859`). Rewriting it means answering Doerig's epistemic dilemma,
   which is a substantive argument, not a wording fix.
3. **Erratum question, still open from the S307 package:** v15 already carries repairs to a published
   v14. Does v15 ship an erratum, or do these ride in v16? No numbers change either way.
4. **Whether to publish v15 at all now, or fold this review in first.** The recommendation is to fold it
   in: fourteen blockers is not a release.
