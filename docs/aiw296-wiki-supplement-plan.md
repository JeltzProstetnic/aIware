<!-- Tracked-by: AIW-296 -->
# AIW-296: wiki supplement, gap analysis and edit plan

**Prepared:** 2026-10-18 (S338, WSL, subagent). **Scope:** this is a plan only. Nothing under `wiki/` has been edited.
**Baseline:** 126 markdown pages (incl. `assets/book-originals/INDEX.md`) plus `STYLE-GUIDE.md` and `INFRASTRUCTURE-SPEC.md`. Highest `article_number` is 101.
FMT v19 is live at `10.5281/zenodo.23427746`. The wiki footer cites the concept DOI `10.5281/zenodo.18669891`,
which resolves to v19, so no footer link changes. `python3 scripts/build_llms_full.py --check` already reports
**STALE** before any wiki edit, because the master changed after the last rebuild.

**Verdict:** the S326/S334 passes brought the comparative pages for RPT, HOT and the closure falsifier up to date.
Everything else that v19 changed is either missing or contradicted. The worst errors are in the core pages: the
two-threshold "together sufficient" claim, the definition of consciousness as an "ability", and "not binary".

Status key: **missing** = not in the wiki; **stale** = the wiki says something the new state contradicts;
**present** = already carried; **hold** = must not go public yet (see §4). Size: S ≤ 1 h, M = half a day, L = a day or more.

## 1. Item table

| # | Item | Source (file, section) | Target wiki file(s) | Status | Proposed change | Size |
|---|---|---|---|---|---|---|
| W01 | One gate: a system has phenomenology or none; without it no term of the family applies | changelog "Minimal consciousness and the two axes"; master §3.5 l.393, Table 1 note l.162; decisions S334 D2 | `mechanisms/graduated-consciousness.md`, `reference/glossary.md` (Graduated Consciousness), `phenomena/animal-consciousness.md` | stale | Replace "not binary" with: one gate, then graded on two axes above it. Rewrite the lead, the Key Takeaway and the glossary entry to match. | M |
| W02 | Minimal consciousness, the floor: rudimentary closure, the present moment with a primordial pain or a nothingness, no reflection, no past or future, no discernible qualia, unreportable by definition | master §3.5 l.395; decisions S334 D2 | NEW `mechanisms/minimal-consciousness.md`; `graduated-consciousness.md` (new level below basic, figure); `glossary.md` (new entry); `open-questions/minimum-configuration.md` | missing (named only in `vs-hot`) | New page (outline §3). Add a fifth level to the graduated page and its figure. Reword minimum-configuration so basic is no longer called the minimal level. | L |
| W03 | Two level axes: richness of content × depth of recursion | master §3.5 l.393, l.405 | `graduated-consciousness.md`; `core-architecture/two-axes.md` (See Also only) | stale | `graduated` l.47 makes richness a product of recursion. State the two axes as independent, with the master's example (a non-lucid dream is rich and shallow). **Name collision:** `two-axes.md` already means scope × mode. Call these the "level axes" and add one disambiguating sentence on both pages. | S |
| W04 | Basic consciousness restated: same recursion depth as the floor, discernible content, reportable only through a rung above | master §3.5 l.397 | `graduated-consciousness.md`, `animal-consciousness.md` | stale | Replace the basic-level text with the master's wording. Move the fish example to the floor (W06). | S |
| W05 | Terminology: "minimal consciousness" in English; "sentience" only as the animal-welfare cross-reference; never "awareness" for the floor; unrelated to the clinical minimally conscious state | master §3.5 l.393, Table 1 l.162; decisions S334 (English label) | new minimal page, `glossary.md`, `ai-consciousness/ai-welfare.md` (next to Birch's sentience framework, l.23) | missing | One terminology paragraph on the new page. One sentence in ai-welfare mapping Birch's sentience to the floor. Add the MCS disclaimer. | S |
| W06 | Floor candidates: fish, amphibians, possibly insects; an insect brain with rudimentary closure has at least minimal consciousness | master §6.4 l.791, l.799 | `animal-consciousness.md` (l.55, l.63–64 figure, l.95), `graduated-consciousness.md` l.21 | stale | Fish/reptiles move from "boundary zone, uncertain" to floor candidates. Insects become "minimal, if a closed loop is present", not "basic, if present". | M |
| W07 | Sleep: deep NREM probably absent (unconsciousness); light NREM the reportable state closest to the floor; NREM dreaming assigned to non-deep NREM; up-states do not sustain the simulation | changelog "Sleep"; master Table 4 l.697–698, §6.3; decisions S334 | `phenomena/sleep.md` (l.40 figure node, l.71) | stale | Rewrite l.71 and the NREM node from "brief up-state dreaming" to the master's two rows. Cite Siclari et al. 2017, 2018. | S |
| W08 | Accessible vs accessed: the access–phenomenality identity holds for accessed content (in the running simulation); accessible content is preconscious, on the implicit side, until a permeability event (Dehaene et al., 2006); felt self-initiated retrieval is agency attribution | changelog "Accessible versus accessed"; master §3.4.6; decisions S334 D2c | `mechanisms/implicit-explicit-boundary.md` (new paragraph), `basics/phenomenal-consciousness.md` (FMT note after l.34), `glossary.md` (new entry), `mechanisms/variable-permeability.md` l.23–25, 44, 46 | missing; term collision in variable-permeability | Add the split where permeability is explained. In variable-permeability, "processing becomes accessible" now reads as "preconscious" under the v19 terms; change it to "enters the simulation". | M |
| W09 | Recursion depth converts presence into reportability, not access; overflow = thin self-model with too little recursion above it | master §3.4.6; changelog | `comparative/vs-gnw.md` l.39 | present (partial) | The "thin simulation running below the depth" sentence is already there. Change "without full access" to "without reportability" and link W08. | S |
| W10 | Consciousness is the process; the capacity is named separately (*Bewusstheit* / *Bewusstsein*, Gruber 2015 p. 57) | changelog "Consciousness as process"; master §3.1, Table 1 l.162; decisions S334 C1–C9 gap 1 | `core-architecture/core-definition.md` (l.5, l.11, l.17), `glossary.md` (no Consciousness entry exists) | stale | Rewrite the bold summary and description to the master's process definition. Add a "Capacity and process" paragraph quoting the 2015 split. Add a Consciousness entry to the glossary. Page is embedded in `llms-full.txt`. | M |
| W11 | Sufficient conditions are a conjunction: four models under closure + free compute + embodiment + at least one pain-pleasure axis. Free modelling and the architecture are each necessary, not sufficient | changelog "Sufficient conditions"; master §3.7.3 l.525, §4.4 l.639 | `physical-foundations/two-thresholds.md` (l.5, 11, 13, 44–46), `glossary.md` l.73, `reference/key-figures.md` l.251, `foundations/overview.md` l.23, `phenomena/animal-consciousness.md` l.53, `philosophical/substrate-independence.md` l.35; also `llms-not-conscious.md` l.13, `engineering-specification.md`, `ai-welfare.md` l.35 (Batch D) | stale | Retitle the "Together Sufficient" section; state both thresholds as necessary and the four-part conjunction as sufficient. Add Requirements 5–6 (embodiment, valence axis) to the engineering specification. Fix every "jointly sufficient" listed in §2. | L |
| W12 | Engineered valence is allowed (presetting the sign shortcuts selection); embodiment is required for natural emergence, not for existence; locked-in from birth sits near the floor | master §3.7.3 l.525; decisions S334 | `engineering-specification.md`, `substrate-independence.md`, new minimal page | missing | One paragraph each. On the minimal page, the locked-in case illustrates the floor. | S |
| W13 | What counts as a self model: a model of the system itself, however simple; a position estimate alone is not one; a SLAM robot vacuum fails (position-only self, no implicit/explicit split, fixed algorithm, no free compute) | changelog "What counts as a self model"; master §3.4.3, §3.5 l.395, §6.4 | `core-architecture/explicit-self-model.md` (short paragraph); new white-box page (worked example) | missing | State the criterion once on the ESM page. Use the vacuum as the worked negative on the new page. | S |
| W14 | White-box decision procedure: where connectome, weights and running system are inspectable, trace an input to the self model closed with the world model; non-inspectable systems get behavioural analysis only. New falsification criterion | changelog "Consciousness in non-reporting systems"; master Table 1b l.201, §4.4, §6.4 | NEW `predictions/white-box-trace.md`; `limitations/other-minds.md` (l.33 "four partial responses" → five); `animal-consciousness.md` (Boundary Problem, Batch A links only) | missing | New page (outline §3). Add a fifth response to other-minds that points to it. | M |
| W15 | Principle 3 as identity: phenomenality *is* closure (no longer "arises where") | changelog "Principle 3 as identity"; master §3, §3.4 | `core-architecture/self-referential-closure.md` l.23; `comparative/vs-rpt.md` l.47; `comparative/vs-hot.md` l.35, l.83; theory-map draft ("Experience arises where…") | stale | Replace the law-like verbs with the identity wording; quote the master's Principle 3. | S |
| W16 | Refutation conditions for the bridge: functional twin (return-free, same functions within the same resource bound) as the primary refuter; two human dissociations; in-vivo disruption tests the markers, in-silico closure-off ablation tests the premise (71.5–74.0% connectome cost) | changelog "Refutation condition for the bridge" + "premise test"; master §4.4 | `hard-problem/dissolution.md`, `self-referential-closure.md` | missing (the 71.5–74.0% figure appears only in `vs-iit` l.39, for unfolding) | Add a "What would refute the bridge" section to dissolution; one sentence and a link in self-referential-closure. Only the published §8.9 numbers. | M |
| W17 | Panpsychism: FMT requires no micro-experience and cannot exclude it; if panpsychism holds, closure is what forms a subject from it, so FMT would answer the combination problem; IIT criticisms unchanged | changelog "Panpsychism"; master §4.1, §4.2.5, §4.3, Table 5 note | `philosophical/process-physicalism.md` l.17, l.62; `philosophical/weak-emergence.md` l.29, l.84; `basics/panpsychism.md` (FMT note); `comparative/vs-iit.md` l.29, l.31; `comparative/scoreboard.md` l.31 | stale | Replace the flat denials with the master's wording. Keep the IIT criticisms. | M |
| W18 | Table 1b closure falsifier reworded (disrupt the loop itself; metacognitive disruption alone does not test closure) | changelog "Self-referential closure falsifier"; decisions S334 | `comparative/vs-hot.md` l.43 | present | None. | — |
| W19 | RPT: recurrence absorbed; local-recurrence sufficiency contradicts Principle 3; decider | changelog "RPT"; master §7.2 | `comparative/vs-rpt.md` | present (commit 30627097) | Only the W15 verb fix at l.47. | — |
| W20 | HOT: higher-order representation = extended rungs; minimal and basic are phenomenal without one | master §7.2 l.867 | `comparative/vs-hot.md` l.5, l.87 | present | Only the W15 verb fix. | — |
| W21 | Six further comparisons: information closure theory, perceptual reality monitoring, Conscious Turing Machine, minimal phenomenal experience, Searle's biological naturalism, enactivism | changelog "Six further comparisons"; master §7.2 | NEW `comparative/further-theories.md`; `phenomena/meditation.md` (MPE note); `comparative/self-modeling-tradition.md` (Metzinger MPE answer) | missing (0 wiki hits for Searle, enactivism, CTM, PRM) | New page with one section per theory: absorbed, conflict, decider. Add MPE ("selfless" = no represented self; the floor keeps an implicit self/world boundary) to meditation and the Metzinger section. | L |
| W22 | Free-modelling falsifier: robust consciousness where a fixed lookup reproduces the system's behaviour on novel input | master Table 1b l.196; decisions S331/S332 | `physical-foundations/criticality.md` or `two-thresholds.md` | missing (pre-v18 carry-over) | Add the falsifier and the novel-input probe in two sentences. | S |
| W23 | Criticality residues by role (S329: free modelling causes the signature; criticality is neither necessary nor sufficient; universal computation without criticality, Siegelmann & Sontag 1995, Maass 1996) | decisions S329, S332 (role test); master §3.7 l.446–448, l.529, l.937, §8.5 | `criticality.md` l.21; `predictions/confirmed.md` l.17; `phenomena/lucid-dreaming.md` l.5, 11, 23, 98; `predictions/prediction-4-lucid-dreaming.md` l.21, 96; `phenomena/sleep.md` l.11, 77; `two-thresholds.md` l.17 | stale | Align with the master's wording (§2, items 8–9). Keep descriptive uses ("drops out of criticality under anesthesia"). Add the "neither" sentence and the two citations to criticality.md. | M |
| W24 | Theory map (AIW-281, wiki first per the S337 order) | `drafts/papers-moc7/theory-map-wiki.md`; brief `docs/papers-moc7/theory-map-brief.md` | NEW `comparative/theory-map.md` (article 102) | missing (draft ready) | Publish the draft after four fixes: identity wording; "the architecture with free modelling suffices on any substrate" → W11 conjunction; Metzinger row "Selfless MPE (open)" → the v19 answer; American spelling ("modeling", "minimization") to match the wiki. Open decision 7 (PRM verdict) is settled by the v19 §7.2 PRM entry. | M |
| W25 | Definitions A, "Pointing Is Not Defining" | `drafts/papers-moc7/definitions-not-settled.md`; brief | — | hold | Title only, as "in preparation", if MG clears it for the wiki (§4). | — |
| W26 | Definitions B, "Deriving a Definition of Consciousness from Reference Systems" | `drafts/papers-moc7/deriving-the-fmt-definition.md` | — | hold | Same. The capacity/process content reaches the wiki from the master via W10, not from this draft. | — |
| W27 | Minimal self, "Too Late to Report" | `drafts/papers-moc7/minimal-self.md` | — | hold | Same. The draft still says the floor persists through most of sleep, which the S334 ruling superseded, so do not copy from it. | — |
| W28 | Robot plea, "Silent suffering" | `drafts/papers-moc7/robot-consciousness-plea.md` | — | hold | Same. | — |
| W29 | Prediction map (Negro et al. format, 55 nodes, 84 edges) | `drafts/papers-moc7/fmt-prediction-map-spec.md`, `.json` | — | hold | Nothing until MG has decided the route into Mudrik's programme (AIW-276). | — |
| W30 | Category theory not advertised until D1 has a result | decisions S334 | `formal/formalization.md` | present | Wiki has no category-theory claim. None. | — |
| W31 | S335: the implicit/explicit level distinction is at its core a didactic cut, not an absolute ontology | decisions S335; `docs/monograph-paper-correction-candidates.md` items 1, 3a | `core-architecture/real-virtual-split.md` l.5, 13, 101; `reference/glossary.md` l.33; `open-questions/implicit-models-virtual.md` l.13; `ai-consciousness/engineering-specification.md` l.33 | stale, **gated** | Drop "not a metaphor" and "foundational ontological"; state the split as the theory's chosen cut, with real explanatory power, whose boundary is semipermeable. Ask MG first (§4). Scope is implicit/explicit only: whether the cut also covers the substrate/computation distinction (`two-level-ontology.md`) is unruled (candidate 3a, triage D12). | S |
| W32 | No Outside (monograph) | `docs/papers-book/paper1-brief.md`; decisions S335–S337 | `limitations/inside-modeling-godel.md` (See Also), `index.md` | hold | Pointer only, after the Zenodo deposit. | — |
| W33 | S336 outside-view ruling | decisions S336 | — | hold | Monograph content. The wiki's closure pages ("no vantage point external to the loop") are consistent with it. No change. | — |
| W34 | AIW-285 candidates: description vs instance (§3.4.5), "substrate has no experience" vs stored structure (3g) | `docs/monograph-paper-correction-candidates.md` items 2, 3, 3g | `hard-problem/virtual-qualia.md`, `dissolution.md` l.11, `category-error.md` | hold | Do not touch until MG approves the items and the master carries them. | — |
| W35 | Bibliography for the new material | master reference list | `reference/bibliography.md` | missing (0 hits for each) | Add verbatim from the master list: Blum & Blum 2022; Chang et al. 2020; Metzinger 2020; Searle 1980, 1992; Thompson 2007; Varela, Thompson & Rosch 1991; Dehaene et al. 2006; Siclari et al. 2017, 2018; Siegelmann & Sontag 1995; Maass 1996; plus the theory map's own citations (Laukkonen et al.; Aru, Suzuki & Larkum; Safron; Bayne et al. 2020; Lau on reality monitoring). | S |
| W36 | Index | — | `index.md` l.163–171 | stale | Comparative section lists 5 of 9 pages (`vs-hot`, `vs-rpt`, `self-modeling-tradition`, `cogitate` missing). Add them and the four new pages. | S |
| W37 | Infrastructure handoff text | master title; S329 | `wiki/INFRASTRUCTURE-SPEC.md` l.82 (footer title "A Criticality-Based Framework"), l.103 (llms.txt block "operating at criticality") | stale | Correct both and tell infrastructure that the deployed footer and `llms.txt` may carry the old wording. | S |

**Counts:** missing 11 (W02, W05, W08, W12, W13, W14, W16, W21, W22, W24, W35) · stale 13 (W01, W03, W04, W06,
W07, W10, W11, W15, W17, W23, W31, W36, W37) · present 5 (W09 partial, W18, W19, W20, W30) · hold 8 (W25–W29,
W32–W34) · new pages 4.

## 2. Stale lines, most wrong first

1. **Two thresholds called sufficient.** v19 replaced "together they are sufficient" with a four-part conjunction.
   This is the theory's strongest stated commitment, and it appears on the pages crawlers read first.
   - `physical-foundations/two-thresholds.md:5` — "Both necessary, jointly sufficient."
   - `physical-foundations/two-thresholds.md:11` — "Both are necessary; neither is sufficient; together they are sufficient."
   - `physical-foundations/two-thresholds.md:13` — "two independent thresholds that jointly constitute the necessary and sufficient conditions for consciousness"
   - `physical-foundations/two-thresholds.md:46` — "the Class 4 regime plus the four-model architecture is not merely necessary but *sufficient* for consciousness"
   - `foundations/overview.md:23` — "Neither alone is sufficient; together they are." (in `llms-full.txt`)
   - `reference/glossary.md:73` — "Neither alone is sufficient; together they are sufficient."
   - `reference/key-figures.md:251` — "Neither threshold alone is sufficient; together they are."
   - `ai-consciousness/llms-not-conscious.md:13` — "two independent, jointly sufficient conditions for consciousness"
   - `core-architecture/core-definition.md:17` — "The definition has three components, each necessary and jointly sufficient:"
   - `philosophical/substrate-independence.md:35` — "a synthetic system implementing the four-model architecture in the Class 4 regime should produce genuine consciousness"
   - `phenomena/animal-consciousness.md:53` and `ai-consciousness/ai-welfare.md:35` state only necessity and are not wrong; fix them in the same pass so they mention the conjunction.
2. **Consciousness defined as an ability.** MG ruled that the master must not treat consciousness as a capacity.
   - `core-architecture/core-definition.md:11` — "**Consciousness is the ability of an entity to create a model of itself, relate that model to itself, and interact with it**" (in `llms-full.txt`)
   - `core-architecture/core-definition.md:5` — description: "Consciousness is the ability to create a self-model…"
3. **"Not binary" against the one-gate rule.**
   - `mechanisms/graduated-consciousness.md:11` — "**Consciousness is not binary — on or off — but graduated**"
   - `mechanisms/graduated-consciousness.md:74` — "Consciousness is not a binary property but a continuum determined by the depth of recursive self-modeling."
   - `reference/glossary.md:93` — "Consciousness is not binary but graduated: basic (minimal self-simulation), …"
   - `phenomena/animal-consciousness.md:95` — "a continuum determined by the depth of self-modeling, not a binary property"
   - `mechanisms/graduated-consciousness.md:47` — "More recursion means deeper self-reference, which means a richer experiential domain." (richness is the other axis)
4. **Flat panpsychism denials,** the same sentences v19 replaced in the master.
   - `philosophical/process-physicalism.md:17` — "No fundamental experiential property. No panpsychist micro-experience."
   - `philosophical/weak-emergence.md:29` — "Weak emergence dissolves it. There are no micro-experiences to combine."
   - `comparative/vs-iit.md:29` — "FMT avoids panpsychism entirely through weak emergence"
   - `comparative/scoreboard.md:31` — "FMT is non-panpsychist, so the Combination Problem does not arise for it"
   - `philosophical/process-physicalism.md:62` (caption) — "it requires no micro-experiences and faces no Combination Problem" (first half is correct; the second needs the v19 conditional)
5. **Principle 3 in its old law-like form.**
   - `core-architecture/self-referential-closure.md:23` — "phenomenology arises where the modeling closes on itself" (the old Principle 3 verbatim; in `llms-full.txt`)
   - `comparative/vs-rpt.md:47` — "FMT's third principle places phenomenality where the modeling closes on itself"
   - `comparative/vs-hot.md:35` — "FMT explains *why* self-representation produces phenomenality … arising when self-referential closure…"
   - `comparative/vs-hot.md:83` — "phenomenality arises earlier, from the closure of a rudimentary self-model with the world model"
6. **Deep NREM dreaming.**
   - `phenomena/sleep.md:71` — "Deep NREM pushes the system predominantly subcritical: consciousness is mostly absent, apart from brief dreaming during cortical up-states, when the explicit simulation transiently switches on."
   - `phenomena/sleep.md:40` (figure) — "NREM Sleep … Simulation mostly collapsed (brief up-state dreaming)"
7. **Floor placement of animals and the "minimal level".**
   - `phenomena/animal-consciousness.md:64` (figure) — "Fish / Reptiles — Boundary zone — Uncertain"
   - `phenomena/animal-consciousness.md:63` (figure) — "Insects — Open: closed self-referential loop? — Basic, if present"
   - `mechanisms/graduated-consciousness.md:21` — "A fish navigating a reef likely operates at this level" (basic)
   - `open-questions/minimum-configuration.md:23` — "posits basic consciousness as the minimal level"
8. **Criticality as a condition, by role (S329/S332).**
   - `physical-foundations/criticality.md:21` — "uses that layer for self-modeling is driven toward criticality and held there" (master l.529: "plausibly shows as near-critical dynamics … the requirement is the recruitment, and the operating point is its signature")
   - `predictions/confirmed.md:17` — "all agents abolishing consciousness do so by pushing the substrate below the criticality threshold" (master l.937: "by abolishing free modeling … in cortex this shows as a push below the critical band"; in `llms-full.txt`)
   - `phenomena/lucid-dreaming.md:11` (also l.5, 23, 98) — "Lucid dreaming occurs when the substrate reaches sufficient criticality during REM sleep for the ESM to activate fully"
   - `predictions/prediction-4-lucid-dreaming.md:21` (also l.96) — "occurs when the substrate reaches sufficient criticality for the ESM to cross from basic to extended self-awareness"
   - `phenomena/sleep.md:77` (also l.11) — "REM periodically re-approaches the threshold for conscious simulation"
   - `physical-foundations/two-thresholds.md:17` — "Below the threshold … its dynamics fall out of the critical regime."
9. **Term collision with the v19 accessible/accessed split.**
   - `mechanisms/variable-permeability.md:23` (also l.24–25, 44, 46) — "**V1-level** processing becomes accessible". Under v19, "accessible" means preconscious, which is the opposite of what the page says.
10. **Level distinction stated as absolute ontology** (gated, W31).
    - `core-architecture/real-virtual-split.md:13` — "This division is not a metaphor. It is the foundational ontological distinction of the Four-Model Theory"
    - `reference/glossary.md:33` — "The foundational ontological division."
    - `open-questions/implicit-models-virtual.md:13`; `ai-consciousness/engineering-specification.md:33` — "must constitute genuinely distinct ontological levels"
11. **Infrastructure text.**
    - `wiki/INFRASTRUCTURE-SPEC.md:82` — footer title "The Four-Model Theory of Consciousness — A Criticality-Based Framework" (master title: "A Simulation-Based Framework Unifying the Hard Problem, Binding, and Altered States")
    - `wiki/INFRASTRUCTURE-SPEC.md:103` — llms.txt: "four nested models … operating at criticality (edge of chaos)"

## 3. New pages

**N1 — `wiki/comparative/theory-map.md`** (article 102; source `drafts/papers-moc7/theory-map-wiki.md`)
1. Lead: most theories describe one part of FMT's architecture; FMT keeps their mechanisms and rejects specific sufficiency, ontology and substrate claims.
2. Reference architecture: wired band, channel, running band, closure loop, ladder, opacity, free-modeling field, substrate independence.
3. Figure (the D1 Mermaid map) with caption, plus the 18-row summary table linking the `vs-*` pages.
4. "What the pattern shows": mechanisms kept, sufficiency claims rejected, ontology/substrate claims rejected.
5. "Which disagreements can be tested": one decider per theory, the loop-splitting complication, Key Takeaway and See Also.

**N2 — `wiki/comparative/further-theories.md`** (article 103; source master §7.2, the six v19 entries)
1. Lead: six theories the 1:1 pages do not cover, each in the absorb / conflict / decider form.
2. Information closure theory (Chang et al. 2020) and the Conscious Turing Machine (Blum & Blum 2022).
3. Perceptual reality monitoring (Lau): source attribution fails before experience, dreaming as the everyday case.
4. Minimal phenomenal experience (Metzinger 2020): "selfless" read as no represented self; the floor keeps an implicit self/world boundary.
5. Searle's biological naturalism and enactivism (Thompson 2007; Varela, Thompson & Rosch 1991): substrate and internal-model disputes, decidable only with a built system; figure, Key Takeaway, See Also (N1).

**N3 — `wiki/mechanisms/minimal-consciousness.md`** (article 104; source master §3.5 l.393–397, §3.7.3 l.525, §6.4 l.791, Table 1 l.162)
1. Lead: the one gate, and minimal consciousness as the floor of both level axes.
2. What the floor contains: the present moment with a primordial pain or a nothingness; what it lacks; why it is unreportable by definition.
3. The level axes (richness × recursion) and how basic consciousness differs from the floor (content, not depth).
4. Terminology: sentience as the animal-welfare counterpart; not "awareness"; not the clinical minimally conscious state; below what report and PCI detect.
5. Candidates and edge cases: fish, amphibians, possibly insects; locked-in from birth; the non-report signature (link N4); figure, Key Takeaway, See Also.

**N4 — `wiki/predictions/white-box-trace.md`** (article 105; title "Deciding Consciousness Without Report: The White-Box Trace"; source master Table 1b l.201, §3.4.3, §4.4, §6.4)
1. Lead: a verdict does not need report where the system can be inspected.
2. The procedure: follow an input through the running system to a self-model component that enters the world model's update rule and is entered by it.
3. What counts as a self model; the SLAM vacuum as the worked negative (position-only self, no implicit/explicit split, fixed algorithm, no free compute).
4. Scope: artificial systems now, nervous systems as connectomes become inspectable, behavioural analysis only otherwise.
5. Falsification criterion (the new Table 1b one) and how it differs from the bridge refuters (link `dissolution.md`); figure, Key Takeaway, See Also.

Optional: add N1 and N3 to `ARTICLES` in `scripts/build_llms_full.py`. That changes the builder, so
`test_article_numbers_match_frontmatter` must keep passing.

## 4. Must not go public yet

| Item | Reason |
|---|---|
| Definitions A, Definitions B, minimal self, robot plea: anything beyond the title | Undeposited drafts. Definitions A went privately to Signorelli as a possible co-author (sent 2026-10-17), and the venue is undecided (AIW-292). Publishing the content would pre-empt both. Titles may appear as "in preparation" only if MG says so: he cleared exactly that for the MoC7 landing page (AIW-297, pick 4), not explicitly for the wiki. |
| Prediction map (spec, JSON, centrality results) | Built for submission to Mudrik's programme (AIW-276). The platform's import schema has not been checked, and MG has not decided the route. |
| Crucible results beyond what v19 and the companion publish, incl. CRU-70/CRU-78 | Disclosure freeze (S335 #10). The contribute primer is held for this reason. Only the published §8.9 figures (71.5–74.0%, 12.0–14.0%) may be used. |
| The crucible robot's hand-set hunger, fear and pain, and the planned closure (robot plea COI section) | Unpublished crucible design detail. |
| No Outside content, incl. the S336 outside-view rulings and D1 (a readable static trajectory has an inner world) | Not deposited. v0.7 waits for MG's proofread, and the D22 AI-use declaration is still missing. Pointer only after the deposit. |
| AIW-285 correction candidates (description vs instance; "substrate has no experience" → stored structure; two-level-ontology scope) | MG approves each item first, and they go into the next FMT version together with AIW-288. The wiki follows the master. |
| S335 didactic cut (W31) | MG's ruling is on record, but the master still says "two-level ontology", and the paper consequences await item-by-item approval. **One question for MG:** may the wiki state the ruling ahead of the master, restricted to the implicit/explicit cut? Until he says yes, W31 stays out of the batches. |

## 5. Batches (≤4, no file in two batches)

Run them one after another, or in parallel and rebuild `llms-full.txt` once at the end. No batch edits
`wiki/llms-full.txt`. Each batch fixes every listed item that falls in its files, including items that belong to another
batch's theme (for example, A writes the glossary entries for W08 and W14).

**Batch A — what consciousness is: definition, gate, levels, floor, sufficiency, sleep, animals.**
Items W01–W07, W10, W11 (its share), W12 (substrate-independence), W22, W31 glossary line only if MG says yes.
Files: `core-architecture/core-definition.md`, `mechanisms/graduated-consciousness.md`, NEW `mechanisms/minimal-consciousness.md`,
`physical-foundations/two-thresholds.md`, `foundations/overview.md`, `reference/glossary.md`, `reference/key-figures.md`,
`open-questions/minimum-configuration.md`, `phenomena/animal-consciousness.md`, `phenomena/sleep.md`,
`philosophical/substrate-independence.md`, `core-architecture/explicit-self-model.md` (W13 criterion), `core-architecture/two-axes.md` (W03 disambiguation).

**Batch B — the bridge, panpsychism, access, criticality residues.**
Items W08, W15 (closure page), W16, W17 (non-comparative pages), W23.
Files: `core-architecture/self-referential-closure.md`, `hard-problem/dissolution.md`, `philosophical/process-physicalism.md`,
`philosophical/weak-emergence.md`, `basics/panpsychism.md`, `basics/phenomenal-consciousness.md`,
`mechanisms/implicit-explicit-boundary.md`, `mechanisms/variable-permeability.md`, `physical-foundations/criticality.md`,
`predictions/confirmed.md`, `phenomena/lucid-dreaming.md`, `predictions/prediction-4-lucid-dreaming.md`.

**Batch C — comparisons.**
Items W09, W15 (comparative pages), W17 (`vs-iit`, `scoreboard`), W21, W24.
Files: NEW `comparative/theory-map.md`, NEW `comparative/further-theories.md`, `comparative/vs-iit.md`, `comparative/vs-rpt.md`,
`comparative/vs-hot.md`, `comparative/vs-gnw.md`, `comparative/scoreboard.md`, `comparative/self-modeling-tradition.md`,
`phenomena/meditation.md`.

**Batch D — non-reporting systems, AI pages, housekeeping (runs last, because the index lists A's and C's new pages).**
Items W11 (AI pages), W12 (engineering spec), W13 (worked example), W14, W35, W36, W37, W31 (if MG says yes).
Files: NEW `predictions/white-box-trace.md`, `ai-consciousness/llms-not-conscious.md`, `ai-consciousness/engineering-specification.md`,
`ai-consciousness/ai-welfare.md`, `limitations/other-minds.md`, `reference/bibliography.md`, `index.md`,
`wiki/INFRASTRUCTURE-SPEC.md`, and only if MG approves W31: `core-architecture/real-virtual-split.md`, `open-questions/implicit-models-virtual.md`.

Every batch follows `wiki/STYLE-GUIDE.md` (template, one figure per page, footer, `description` + `keywords`
frontmatter, 400–800 words), reuses the canonical language pinned in `docs/pending-wiki-refresh.md` (SMoC as candidate;
free compute as the requirement, criticality as its signature), checks the six misreadings in
`.claude/knowledge/fmt-misconception-registry.md`, and runs the register sweep in `.claude/knowledge/prose-register.md`
on the new prose. Quote the master; do not paraphrase the v19 rulings from `decisions.md` where the master has the wording.

## 6. After the edits

1. Rebuild the crawler file: `python3 scripts/build_llms_full.py` (it embeds `index.md`, the 11 pages in `ARTICLES`,
   and the FMT master verbatim; never hand-edit `wiki/llms-full.txt`).
2. Check staleness: `python3 scripts/build_llms_full.py --check` must exit 0. It currently exits 1 (STALE) before any edit.
3. Run the guard: `pytest scripts/test_build_llms_full.py -v`. `pytest scripts/ -k llms` selects the same 8 tests,
   including `test_committed_file_is_up_to_date` and `test_article_numbers_match_frontmatter`.
4. Check the internal links of the new pages (relative paths), then file the deploy inbox item for infrastructure
   (`mkdocs.yml` lives there), naming the new pages and the W37 footer/llms.txt correction.
