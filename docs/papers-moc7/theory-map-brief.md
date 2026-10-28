<!-- Action: reference -->
<!-- Tracked-by: AIW-281 (feeds AIW-276, AIW-277; relates AIW-146, AIW-119, AIW-129) -->
# Theory Map — content brief (PREPARATION, not the page)

**Backlog:** `AIW-281`. **Prepared:** 2026-10-16 (Steam Deck 2, research subagent). **Status:** brief for MG review — no prose for publication yet.
**Goal of the eventual artefact:** show visually and in text where 15 major theories of consciousness sit relative to FMT. For each: which parts FMT **absorbs** (and as which model kind, mechanism or level), which it is **compatible / neutral** on, and which it **contradicts**, and why.

**Sources read for this brief:** FMT master `paper/full/four-model-theory-full.md` (§1.3, §3–§3.8, §4.4, §6.0, §7.1–7.4, §8.1–8.9, §10.2); `.claude/knowledge/project-reference.md`; `.claude/knowledge/fmt-misconception-registry.md`; `.claude/knowledge/didactic-patterns.md` (cautions); `wiki/comparative/*` (9 pages); `docs/smoc-middle-layer-draft.md` (AIW-146); `backlog.md` (AIW-119, AIW-129, AIW-146, AIW-276/277/281); `docs/moc7/booklet.txt` + `docs/moc7/gmail-intake.md`.

**Citation tags used below.** **[FMT]** = already in the FMT master reference list (inherited; that list is gated by `verify_references.py`). **[V]** = web-verified this session (title / venue / year / DOI). **[UNVERIFIED]** = not checked in this session; must be checked before any of it ships.

---

## 0. What already exists — extend it, don't duplicate it

| Existing asset | Coverage | Gap the theory map fills |
|---|---|---|
| Master **§7.1 Table 5** (scoring matrix) | FMT, IIT, GNW, HOT, PP, AST and RPT scored against the 8 *philosophical* requirements | It scores how well each theory **answers the requirements**, not which **FMT component** each theory corresponds to. No absorbed / compatible / contradicts axis. |
| Master **§7.2** theory-by-theory | IIT, GNW, HOT, PP (incl. beast machine, REBUS, Beautiful Loop), AST, RPT; unfolding argument | HOT and AST are given only a few lines. The contradictions are stated as "FMT adds X", not as **precise points of conflict with a deciding experiment**. |
| Master **§7.3** | Biological computationalism, structural turn (Ellia & Tsuchiya), Multiple Generator, RIFT, Beautiful Loop, Bach, **IWMT (detailed)** | — |
| Master **§3.4.5** | Illusionism (Frankish) and functionalism — a careful ontological contrast | — |
| Master **§4.4** | Seth's biological naturalism, LLMs, substrate independence | Searle's version is absent. |
| Master **§3.7.1** | DIT (Aru, Suzuki & Larkum) as a candidate mechanism for the Level 4→5 transition | — |
| Master **§3.6.1** | GNW workspace = occupancy of the channel (the *Arbeitsmodell*) | — |
| Master **§3.8** | Meta-problem vs AST | — |
| **Not in the master at all** | **Enactivism (Thompson)**, **Searle**, **ICT (Kanai) as a theory** (only Kanai, Sun & Baltieri 2026 on LLMs is cited), **CTM as a theory** (only CTM-AI 2026 appears, in §8.7), **Metzinger's minimal phenomenal experience**, **Lau's PRM as a theory** (Lau 2022 is cited only for reality-monitoring cues, §6.0) | The theory map would be the first place FMT engages these. |
| `wiki/comparative/` (9 pages, ~9.3k words) | `scoreboard`, `vs-iit`, `vs-gnw`, `vs-hot`, `vs-pp`, `vs-ast`, `vs-rpt`, `self-modeling-tradition` (Metzinger, Damasio, Hofstadter, Graziano, Seth), `cogitate` | Same seven theories as Table 5. Every page has the shape "rival is silent on X; FMT adds X". **No page for** IWMT, DIT, ICT, CTM, illusionism, biological naturalism or enactivism, and **no single map page**. |
| `docs/smoc-middle-layer-draft.md` (AIW-146) | M1–M10 mechanisms, R0–R8 ladder, §3.5.1 positions table (FMT, IIT, GNWT, FEP, HOT, SMT, biological naturalism, illusionism, panpsychism, dualism × Q1–Q7) | That table holds **metaphysical coordinates**. The theory map is the **architectural** counterpart (which component each theory is about). Reuse its M-numbers and R-rungs as the diagram vocabulary rather than inventing new labels. |

### 0.1 Inconsistencies found in existing material — flag before building on it

1. **RPT is called "compatible" (master §7.2; wiki `vs-rpt`). That papers over a real contradiction.** Lamme's RPT holds that *local* recurrence within sensory cortex is sufficient for phenomenal experience, even without access, report or any self-involvement. FMT holds that experience requires the self-model's closure (§3.4.3, Principle 3). The two cannot both be right about a recurrently active V1–V4 with no closed self-model. §3 C4 below sets this out. **The map must label RPT "contradicts on sufficiency".**
2. **HOT: the wiki says higher-order representation is *necessary* for FMT (`vs-hot` "A Concrete Difference"), but the master's §3.5 grants phenomenal experience at the *basic* level**, where the self-model is "rudimentary" and the system is *not yet* "aware that it experiences" (that arrives with simply extended consciousness). Per-state higher-order representation is therefore *not* necessary on the master's account. Only the system-level ESM↔EWM closure is. **MG ruling needed (Q2 in §5).**
3. **PP: the master and the wiki place PP on opposite sides of the implicit/explicit divide.** Master §7.2 says PP's machinery implements "the implicit, predictive layer". Wiki `vs-pp` says "the explicit models are generative, predictive models". Both can be true only if PP machinery runs on both sides. The map needs one statement (Q3).
4. **IIT: master §7.2 says FMT "adopts" IIT's central diagnosis that an experience *is* a maximally irreducible cause-effect structure.** It then locates that structure in a running, substrate-neutral process, which IIT's intrinsic, substrate-bound cause-effect power explicitly is not. A reviewer from IIT will read "adopts" as a misreading of IIT. Suggest **"shares IIT's demand that experience be integrated and intrinsic, and rejects its identification of that structure with the substrate's cause-effect power"** (Q4).
5. Misconception registry, rules a–g, apply throughout. Use **two kinds of models** (never four modules); **free modelling** is the requirement and **criticality only its signature** (S329: never a requirement, nor any reverse or biconditional form); **binding is dissolved**, not solved; **explicit models are not localizable**. Didactic cautions: **PRICE, never BARRIER**. No capability claims on axis A (implicit vs explicit) or axis B (self vs world). These matter here because several "contradictions" tempt sentences like "GNW can't do X without closure".

---

## 1. Master table

**FMT component vocabulary:**
- IWM, ISM, EWM, ESM (§3.2)
- **RV** — real/virtual split (§3.3)
- **VQ** — virtual qualia, level-constitutive (§3.4.1–3.4.2)
- **CL** — self-referential closure (§3.4.3)
- **TE** — temporal echo (§3.4.4)
- **LAD** — graduated / *erweitert* ladder (§3.5)
- **PERM** — permeability (§3.6)
- **CH** — channel / *Arbeitsmodell* (§3.6.1)
- **FM** — free modelling, the Class-4 capability, with criticality as its signature (§3.7, §3.7.3)
- **L1–L5** — five-system hierarchy (§3.7.1)
- **SI** — substrate independence (§4.4)
- **MP** — meta-problem (§3.8)

The SMoC mechanism numbers (M1–M10) are given where they apply.

**Verdict key:**
- **A** = absorbed: FMT contains the claim as one of its components.
- **C** = compatible: FMT doesn't contain it, but it does not conflict.
- **N** = neutral: FMT takes no position.
- **X** = contradicts.

Most theories get **several** verdicts, one per atomic claim. That split is the point of the map.

| # | Theory (key source) | Core claim | FMT component it maps onto | Verdict | Why (FMT ref) |
|---|---|---|---|---|---|
| 1 | **IIT** (Tononi 2004; Albantakis et al. 2023 [FMT]) | Experience = a maximally irreducible intrinsic cause-effect structure; quantity = Φ; exclusion; axioms → postulates | Integration ↔ **CL+FM** (one bound field, §5.1); recurrence ↔ CL; quality space ↔ **VQ** relational structure (§3.4.2, Pred. 5) | **A** integration and recurrence demand. **C** rich quality structure. **X** identity with the substrate's intrinsic cause-effect power. **X** "any Φ>0 complex is conscious". **X** feedforward/digital duplicate verdicts. **N** exclusion as a boundary rule | §7.2 (keeps recurrence, rejects the substrate commitment and "Φ>0 however simple"); §1.3 item 1; §3.4.1 (experience is a property of the running level, not the substrate); unfolding §7.2. FMT's boundary comes from closure plus the two thresholds (§3.7.3), not exclusion |
| 2 | **GNW / GWT** (Baars 1988; Dehaene & Changeux 2011; Mashour et al. 2020 [FMT]) | Conscious = globally broadcast via non-linear ignition in a fronto-parietal workspace; capacity-limited | Workspace = **CH occupancy** (*Arbeitsmodell*, M10); ignition = signature of content entering the closed explicit simulation (Table 1, "becomes conscious" = **PERM** event) | **A** workspace, capacity limit, ignition (as a structure and a marker). **X** broadcast as **constitutive** of experience. **X** "no ignition → no experience" (FMT's basic consciousness without broadcast, §3.4.6). **N** prefrontal anatomy | §3.6.1 ("converge on the structure, diverge on its role"); §7.2; §3.4.6 residual case; Gurnee et al. 2026 LLM workspace = broadcast without closure (§7.2, §4.4) |
| 3 | **PP / active inference / FEP** (Friston 2010; Hohwy & Seth 2020 [FMT]) | Brain minimises prediction error / free energy; perception = controlled hallucination; precision weighting | Inference machinery ↔ **IWM/ISM** dynamics and the generation of EWM/ESM; REBUS precision relaxation ↔ one implementation of a **PERM** change (§1.3 item 4) | **A** prediction-error machinery as implementation. **C** controlled hallucination ≈ the EWM as generated simulation. **N** FEP as a general principle of self-organisation (not a theory of consciousness, per its proponents). **X** only where PP is offered as *sufficient* (Markov-blanket liberality; wiki `vs-pp`) | §7.2 ("complementary… FMT the missing top floor"); §8.2/8.3 distinguishing power vs REBUS; see inconsistency 0.1#3 |
| 3a | **Seth — beast machine / interoceptive inference** (Seth 2021; Seth & Bayne 2022 [FMT]) | Selfhood = control-oriented interoceptive prediction grounded in body regulation | **ISM→ESM** generation from interoceptive input (§3.2 "ESM generated from ISM + interoceptive input"); emotion = self-directed quale (§3.4.4) | **A** the mechanism as one route to the ESM. **X** the biological-naturalist rider (see 14) | §7.2; §4.4 ("a specification of one Class-4-capable architecture, not a substrate requirement") |
| 3b | **Beautiful Loop** (Laukkonen, Friston & Chandaria 2025 [FMT]) | Consciousness = a self-evidencing loop; the generative model includes a model of itself generating the model | **CL** | **A** (convergent). FMT adds RV, the 2×2 and FM | §7.3 |
| 4 | **HOT** (Rosenthal 2005; Lau & Rosenthal 2011 [FMT]; Brown, Lau & LeDoux 2019 [V]) | A state is conscious iff a suitable higher-order representation targets it (transitivity principle); empty HOTs suffice | Higher-order self-representation ↔ **ESM** and the **LAD** rungs (simply / doubly / triply extended = 1st/2nd/3rd-order self-observation); meta-problem partial ↔ **MP** | **A** higher-order self-modelling as the ladder's mechanism. **X** per-state transitivity as the condition of phenomenality (FMT: basic consciousness is phenomenal before first-order self-observation, §3.5). **X** that a HOT alone with no closed simulation suffices (thermostat case, wiki). **N** conceptual vs non-conceptual HOT format | §3.5; §7.2; §3.4.6 (access = recursion depth, not a separate stage); inconsistency 0.1#2 |
| 4a | **Lau — Perceptual Reality Monitoring** (Lau 2022 [FMT]) | Experience occurs when a (non-conscious, prefrontal) higher-order process tags a sensory representation as reliably reflecting the present world | **Source distinguishability**, a requirement FMT places on the architecture (§6.0, "Source distinguishability"); forked vs live runs | **A** the tagging *function* (FMT needs it: without it recall = hallucination). **X** that the tag *constitutes* experience (FMT: closure does). **C** the psychosis reading (cf. §9 OQ7 discriminator miscalibration) | §6.0 (cites Lau 2022 for reality-monitoring cues; "source attribution is the fragile term"); §9 OQ7 |
| 5 | **RPT** (Lamme 2006, 2010 [FMT]) | Stage-3 *local* recurrence (Lamme 2006) in sensory cortex suffices for phenomenal experience; global recurrence plus fronto-parietal involvement adds access/report | Recurrence ↔ the generating dynamics of EWM (Principle 2: "recurrent non-linear dynamics … host a second level", §3.3) | **A** recurrence as necessary (implementation level). **X** *local* recurrence as **sufficient** for phenomenality (FMT needs ESM closure). **X** phenomenal-overflow reading (FMT reframes overflow as a thin ESM, §3.4.6) | §3.3 Principle 2; §3.4.3; §3.4.6. **Master §7.2 and wiki call this "compatible" — correct it (0.1#1)** |
| 6 | **AST** (Graziano 2013; 2024 [FMT]; Wilterson et al. 2020 [V]) | The brain builds a simplified model of its own attention; claims of subjective awareness are that schema's content; deflationary | Attention schema ↔ a component of the **ESM** (the self-model of the selection *into* **CH**, §3.6.1 "attention is selection into the channel"); incompleteness ↔ **MP** | **A** the meta-problem mechanism and the schema as part of the ESM. **C** the attention-control function (Wilterson). **X** deflationism about phenomenality | §3.8; §3.4.5 ("nor is it compatible with deflationary accounts (Graziano, 2024)"); §7.2 |
| 7 | **Self-model theory** (Metzinger 2003, 2009 [FMT]) | Phenomenal self = a transparent self-model; "nobody ever was or had a self"; later, minimal phenomenal experience (MPE) as possibly selfless | **ESM** (transparent = the ESM cannot model its substrate: §3.4.3 observability constraint and §3.8); lineage (§1.3) | **A** self-model as constitutive; transparency ≈ observability constraint. **X** "no selves" if read ontologically (FMT: the self is a *real* virtual process, §3.3/§3.4.6). **X (live)** MPE / "pure awareness" without a self-model vs Principle 3 | §1.3 items 2, 5; §3.1; §7.4 (SMT lacks FM and PERM). MPE is not engaged in the master — see C7 |
| 8 | **IWMT** (Safron 2020 [FMT/V]; Safron et al. 2022 G-SLAM [FMT]) | Consciousness = integrated world-modelling (IIT + GNW + FEP), with integrated selfhood, embodied, near-critical SOHMs | World-model ↔ **EWM**, integrated selfhood ↔ **ESM**, SOHMs ↔ an **FM** signature (§8.1), G-SLAM ↔ one corner (self-location) | **A** world+self modelling as necessary; near-critical signature. **C** formal mechanism (IWMT supplies what FMT lacks). **X (mild)** graded multi-factor demarcation vs FMT's binary closure; inheritance of Φ; embodiment emphasis (a difference of degree) | §7.2 (end); §7.3 (detailed); §8.1; backlog AIW-119 (note sent 2026-07-27) |
| 9 | **DIT** (Aru, Suzuki & Larkum 2020 [FMT/V]; Suzuki & Larkum 2020 [V]) | Consciousness depends on coupling of the apical and basal compartments of L5 pyramidal neurons, regulated thalamocortically; anaesthetics decouple them | **L4→L5 transition** mechanism (§3.7.1 item 5); a realizer candidate for **CH** (thalamocortical relay, §3.6.1 "Fourth") | **A** as a candidate *implementation in cortex*. **N** on whether it is the only realizer (FMT: rank is the constraint, anatomy is not; olfaction counter-case, §3.6.1). **X** only if read as substrate-necessary in general (DIT does not claim this) | §3.7.1; §3.6.1 Fourth |
| 10 | **ICT** (Chang, Biehl, Yu & Kanai 2020 [V]) | Conscious processes are those forming non-trivial informational closure (NTIC) with the environment at a coarse-grained scale; quantitative content and level | **CL** (both make closure the primitive); coarse-grained scale ↔ **L5** virtual level (individuated by mutual effects, §3.3) | **A** closure as primitive and the scale/level move. **X** NTIC as *sufficient* (no self-model required → over-generates, per Safron 2020). FMT's closure is self-referential (ESM ⊆ EWM update rule). **N** the information-theoretic quantities | Not in the master. Backlog AIW-129 ("FMT as the Φ-free patch to ICT"). **Gap** — needs a master paragraph if the map claims it |
| 11 | **CTM** (Blum & Blum 2022 PNAS [V]; Yu et al. 2026 CTM-AI [FMT]) | A formal TCS model on GWT: competition up-tree, broadcast down-tree; "feeling" from predictive dynamics, multimodal *Brainish*, and LTM processors incl. a Model-of-the-World with self | Model-of-the-World incl. self ↔ **EWM ⊇ ESM**; broadcast ↔ **CH**; predictive cycles ↔ IWM learning | **A** the world-model-with-self processor; formal specification as an exemplar. **X** broadcast as constitutive (as with GNW). **X** "all properly organised computing systems" vs FMT's autonomous-recruitment leg (a heteronomous laptop is excluded, §3.7.3). **N** Brainish | §8.7 lists CTM-AI among blueprints lacking closure / Class 4 (check whether that applies to CTM itself — Q6); §3.7.3 |
| 12 | **Illusionism** (Frankish 2016 [FMT/V]; Dennett 1991 [FMT]) | Phenomenal consciousness doesn't exist; quasi-phenomenal states misrepresent themselves; explain the *seeming* | Substrate-level denial ↔ **RV** (no qualia on the real side); introspective mechanism ↔ **MP** | **A** "no phenomenal properties in the substrate" and the meta-problem mechanics. **X** ontology: FMT holds qualia **real at the computational level** (VQ). Not settleable from outside (FMT concedes); the moral-patient consequence differs | §3.4.5 (explicit); §4.2.5 zombies (type-B); §1.3 item 2 |
| 13 | **Biological naturalism — Searle** (Searle 1980 [UNVERIFIED]; 1992 [V]) | Consciousness is caused by specific biological causal powers of brains; a simulation is not a duplication | **SI** | **X** direct contradiction of SI. **C** "brains do it by their biology" as a description of *one* realizer | §4.4 (the burden falls on the biological naturalist, §3.4.3 L342). Searle not cited — add |
| 14 | **Biological naturalism — Seth** (Seth 2025 BBS [FMT/V]) | Consciousness may depend on being alive (autopoiesis, interoceptive self-regulation); computation alone likely insufficient | **SI**; the autonomous-recruitment leg of **FM** (§3.7.3); interoception → **ESM** | **A** the life-like *functional* features (autonomy, self-maintenance, interoceptive self-model) as one route. **X** that biology/life is required | §4.4 ("a specification of one Class-4-capable architecture, not a substrate requirement"); Klatzmann & Doerig 2026 [FMT] testable vs untestable form |
| 15 | **Enactivism** (Varela, Thompson & Rosch 1991 [UNVERIFIED]; Thompson 2007 [V]) | Mind is life-like, embodied, sensorimotor sense-making; deep life–mind continuity; strong strands are anti-representational | Autonomy / autopoiesis ↔ the **FM** recruitment leg ("autonomous, self-referential, resource-constrained", §3.7.3); self/world boundary ↔ **ESM ⊆ EWM** nesting | **C** autonomy and embodiment as conditions on recruitment. **X** anti-representationalism (FMT is a model theory through and through). **X** life–mind continuity *if* it implies all living systems are minded (FMT: R1 organisms such as *C. elegans* lack explicit models; SMoC ladder) | Not engaged in the master (Thompson not cited). Dreams / REM atonia (§6.3) are FMT's best evidence for an internal simulation independent of current sensorimotor coupling |

**Reading of the table, in one sentence:** FMT **absorbs** most theories' *mechanisms* (workspace, recurrence, prediction error, higher-order self-modelling, apical coupling, closure, attention schema). It **contradicts** them mainly on what is **constitutive** or **sufficient** for experience (broadcast, local recurrence, a per-state higher-order representation, Φ>0, NTIC) and on **ontology** (illusionism and AST deny real qualia; biological naturalism denies SI; enactivism denies representation).

---

## 2. The contradictions — precise point, bearing evidence, deciding experiment

The same eight-field format is used for every entry: point · rival claim · FMT claim · evidence that bears · deciding experiment · FMT prediction link · confidence · status of FMT's own position.

### C1 — IIT: what the irreducible structure is
- **Point.** IIT identifies experience with the substrate's intrinsic cause-effect structure. That makes (a) any maximally irreducible complex with Φ>0 conscious, however simple, and (b) a digital (von Neumann) simulation of a brain non-conscious, despite identical function. FMT says the opposite on both: (a) no closure, no experience; (b) a functionally matching implementation in the open-ended regime **is** conscious (§4.4, §8.7).
- **Third disagreement: inactive neurons.** IIT holds that inactive-but-*available* neurons contribute to the cause-effect structure, so silencing currently idle neurons should change experience. FMT locates experience in the running explicit models, so idle units contribute only via the implicit substrate (§3.3). [Tononi, Boly, Massimini & Koch 2016, *Nat Rev Neurosci* — UNVERIFIED]
- **Evidence.**
  - COGITATE (Cogitate Consortium 2025, *Nature*, doi 10.1038/s41586-025-08888-1 [V]): posterior content and sustained responses partly fit IIT. The lack of sustained synchronisation within posterior cortex challenged IIT.
  - The Φ tractability and non-Markovian issues are already in §7.2.
  - The unfolding argument hits both theories (§7.2).
- **Deciding experiment.**
  - (i) **Inactive vs inactivated:** optogenetically silence neurons that are not firing during a percept. IIT predicts a change in experience; FMT predicts none for the current frame.
  - (ii) The **resource-bound unfolding** comparison (§7.2, §8.9): FMT predicts behavioural divergence under a budget, where IIT predicts identical behaviour with different Φ. That one is in-silico, not phenomenal.
- **FMT prediction link.** Pred. 4 (lucid onset in self-model networks vs IIT's posterior Φ increase); Pred. 3 (DID gradient vs IIT's posterior integration differences).

### C2 — GNW (and CTM): is broadcast constitutive?
- **Point.** GNW: experience = global availability after ignition. FMT: experience = the self-model's closure over what the channel holds. Broadcast is the channel's occupancy, and ignition is a **signature** of entry, not the definition (§3.4.6, §3.6.1).
- **Second point.** FMT asserts basic consciousness *without* global broadcast (§3.4.6 residual case). GNW denies conscious experience without ignition.
- **Evidence.**
  - COGITATE: no sustained prefrontal content maintenance and no ignition at stimulus offset — a challenge to GNW [V].
  - No-report paradigms (Tsuchiya et al. 2015 [FMT]).
  - Gurnee et al. 2026 [FMT]: an LLM workspace that is globally available, reportable and ignition-like, with no recurrence → broadcast without closure.
- **Deciding experiment** (already named in §7.2): a manipulation that makes content **globally available without entering the self-model's update rule**. In brains: none exists yet.
  - Candidate: disrupt self-referential (ESM) dynamics while keeping fronto-parietal ignition to a stimulus intact. Use targeted TMS during metacognition (Table 1b), with a dissociation design holding decision criteria fixed (Nakamura, Michel & Lau 2026 [FMT]). FMT predicts experience degrades while the P3b is preserved. GNW predicts experience follows P3b.
  - In silico: §8.9 closure ablations plus Gurnee-style workspace probes.
- **FMT prediction link.** Table 1b "self-referential closure" falsifier; Pred. 4 (GNW predicts prefrontal ignition without a phase transition).

### C3 — HOT: is a higher-order representation *of the state* required?
- **Point.** HOT's transitivity principle: a state is conscious only if represented by a suitable HOT. Misrepresenting or empty HOTs can generate experience by themselves.
  - FMT has phenomenal experience at the **basic** level, with a rudimentary ESM, before any first-order self-observation (§3.5). The condition is system-level closure, not a per-state meta-representation.
  - Conversely, a HOT inside an unclosed system (a monitored simulation, §3.4.3 Stage 2) is not conscious on FMT.
- **Evidence.**
  - Prefrontal-lesion debates: Odegaard, Knight & Lau 2017 [UNVERIFIED]; Boly et al. 2017 [UNVERIFIED].
  - Type-2 decoupling (master §9 OQ text: Rouault et al. 2018; Rahnev et al. 2020 [FMT]): metacognitive efficiency is uncorrelated with first-order d′. FMT reads this as EWM/ESM separability.
- **Deciding experiment.** Selectively abolish metacognitive read-out (M-ratio → 0) while sparing first-order sensitivity, and ask whether *experience* (not confidence) changes.
  - HOT (especially empty-HOT versions) predicts the experience goes or changes.
  - FMT predicts it survives **if** the ESM↔EWM loop is intact. Metacognition is one read-out of the ESM, not the closure itself.
  - **Caveat for MG (Q2):** Table 1b's falsifier says "metacognitive disruption leaves phenomenology intact" *disconfirms* closure. That reads as the opposite prediction. The map cannot go out until this is reconciled — the difference is closure vs read-out.
- **FMT prediction link.** Table 1b closure row; §9 OQ (metacognition reanalysis).

### C3a — Lau's PRM: tag vs closure
- **Point.** PRM: experience = a sensory representation tagged "real / now" by a higher-order monitor. FMT needs that tagging function (source distinguishability, §6.0) but denies it is constitutive. An imagined scene, correctly tagged "not real", is still experienced.
- **Evidence.** Dijkstra & Fleming 2023 [FMT]: reality judgements rest on combined sensory strength. FMT §6.0 uses this to argue source attribution is the fragile term.
- **Deciding experiment.** PRM predicts that a mis-tagged internal representation is experienced *as perception*. FMT agrees for the content's *format* but predicts experience persists when the tag is merely absent (imagery). Weak discriminator — **probably C, not X, on the evidence**. Present it as a near-absorption.

### C4 — RPT: is local recurrence sufficient?
- **Point.** Lamme: stage-3 local recurrence within visual cortex = phenomenal experience, even unreported and unattended. FMT: recurrence hosts the second level (Principle 2), but phenomenality arises only where the modelling closes on itself (Principle 3). A locally recurrent V1–V4 loop with no ESM in its update rule is a simulation with "no inside" (§3.4.3 Stage 1/2). **This is a real contradiction, not a scope difference.**
- **Evidence.**
  - RPT's support: masking; figure-ground modulation lost under anaesthesia (Lamme et al. 1998 [UNVERIFIED]); iconic-memory "overflow" (Sligte et al. 2008 [UNVERIFIED]).
  - FMT's counter-reading of overflow: a thin ESM near threshold (§3.4.6).
- **Deciding experiment.** Find states where local sensory recurrence is preserved but self-model dynamics are abolished. Candidates:
  - (a) the "islands of awareness" question — isolated recurrent cortex: Bayne, Seth & Massimini 2020 *Trends Neurosci* [UNVERIFIED];
  - (b) dissociative or anaesthetic states with preserved figure-ground modulation;
  - (c) in silico, §8.9.

  RPT predicts experience; FMT predicts none. Honest status: **no clean protocol exists yet.** This joins B1 in the SMoC chart ("no accepted protocol for closure").
- **FMT prediction link.** Pred. 2 (identity content tracks input when the ESM is disrupted — RPT is silent); Table 1b closure row.

### C5 — PP/FEP: sufficiency and boundary
- **Point.** Only where PP/FEP is offered as a *theory of consciousness* that needs no self-model or level distinction. Markov blankets apply to thermostats and rocks (Bruineberg et al. 2022 [UNVERIFIED]).
- Hohwy & Seth (2020) [FMT] say PP is not a theory of consciousness. So the contradiction is with *some* FEP authors (Friston's "Am I self-conscious?" 2018 [UNVERIFIED] is actually close to FMT). **Mostly C/A.**
- **Deciding experiments** (already in the master): Pred. 1 fine structure vs REBUS (dose below ego dissolution, lesioned-hemisphere complexity, disconnection vs destruction); Pred. 2 modality-specific tracking vs generic prior relaxation.

### C6 — AST and illusionism: are qualia real?
- **Point.** AST and Frankish say subjective awareness is a schema's or introspection's content with no phenomenal property behind it. FMT says phenomenal properties exist at the computational level (VQ). §3.4.5 concedes the dispute "cannot be settled by empirical observation from outside the system".
- **Evidence.** None decisive by construction. Both sides explain reports.
- **Deciding experiment.** None empirical. The difference is **ethical / practical** (moral patienthood of an architecture-matched artefact, §3.4.5). The map should say so plainly rather than invent a test.
- Graziano's attention-control predictions (Wilterson et al. 2020 [V]) test AST's *mechanism*, which FMT absorbs. They do not test the ontology.

### C7 — Metzinger: selves and minimal phenomenal experience
- **Point.**
  - (a) Metzinger: "no such things as selves" — FMT: the self is real *as a virtual process*. Arguably verbal; label it N/X-verbal.
  - (b) **The substantive one.** Metzinger's MPE programme: "pure awareness", reported as contentless and selfless (Metzinger 2020, *Philosophy and the Mind Sciences* [UNVERIFIED]). If phenomenality occurs with **no self-model**, Principle 3 is false.
- **FMT's available reply** (AIW-280 brief): MPE reports pass through ESM + memory + language. They are post-reflective reconstructions of a thin-ESM state, not evidence of ESM absence.
- **Evidence.** Meditation neurophenomenology. Mago et al. 2025 [FMT] (jhāna shifts toward near-critical dynamics).
- **Deciding experiment.** Neural markers of ESM activity (DMN-independent; FMT disclaims DMN = ESM, Table 1 fn 3) during verified MPE episodes. FMT predicts a minimal but non-zero self-modelling signature; strict MPE predicts none. Measurement is immature — say so.
- **Link.** Pred. 2 (ego dissolution content) is the nearest existing prediction.

### C8 — IWMT: graded vs binary demarcation
- Already handled carefully in §7.3. Mild. The decider is a case with high spatial/temporal/causal coherence plus self-location but **no** self-reference (G-SLAM-like robot, sat-nav). IWMT's graded criterion gives a non-zero degree; FMT gives zero. In silico only.

### C9 — ICT: NTIC vs self-referential closure
- **Point.** NTIC needs no self-model, so any coarse-grained process that predicts its environment well enough would be conscious. FMT's closure requires the self-model to enter the world-model's update rule.
- **Deciding experiment** (in silico, crucible-ready): construct two systems with matched NTIC at a coarse scale, one with and one without a self-model in the world-model's update loop. Compare on FMT's behavioural signatures (§8.9: redeployment, sample efficiency at matched budget). ICT predicts equal consciousness; FMT predicts a difference. **Behaviour does not establish consciousness** — state this, as §8.8 does.

### C10 — Biological naturalism (Searle, Seth) vs SI
- **Point.** Searle: specific biological causal powers are required. Seth: life / autopoiesis / interoceptive self-regulation probably required. FMT: substrate-neutral, regime-required (SMoC §3.5.1: "neutral but not indifferent").
- **Evidence.** Corvid/cephalopod data favour *architecture* independence but are still biological, so they don't decide the question. Seth's BBS target article has a 2026 commentary round (a reply titled "The stuff matters" is reported secondhand [UNVERIFIED]); Kleiner's commentary asks for an explicit definition of the biological property [V via preprint listing].
- **Deciding experiment.** Only an artificial implementation of the full architecture (§8.7, "not currently testable"). Intermediate: Klatzmann & Doerig's (2026) [FMT] testable form — specify which biological property and test whether a non-biological system that has it differs. Partial implementations (§8.7 "two models instead of four") give graded predictions.

### C11 — Enactivism: representation and life–mind continuity
- **Point.** Strong enactivism denies that experience is constituted by internal models. FMT says experience *is* a running internal simulation (EWM/ESM). Life–mind continuity also implies mentality in all living systems; FMT places bacteria, plants and *C. elegans* below the explicit-model rung.
- **Evidence for FMT.** Dreaming under REM atonia; imagery; locked-in patients — rich experience with no ongoing sensorimotor coupling (§6.3). Enactivists reply with sensorimotor *history*, which FMT's implicit models already encode. That reply concedes stored models.
- **Deciding experiment.** Hard. The cleanest discriminator is developmental: experience in a system whose models were never sensorimotor-trained (an artificial agent trained only offline). FMT says possible; enactivism says impossible. Not currently testable.

---

## 3. Candidate diagrams (precise enough to draw)

All three reuse FMT and SMoC vocabulary. Colour key throughout: **absorbed = green**, **compatible = blue**, **neutral = grey**, **contradicts = red** (edge or outline). Keep the dark-mode-safe palette of the wiki figures.

### D1 — FMT architecture with rival theories as overlays (the "where you live in FMT" map)
Base drawing: Figure 1's 2×2, extended downward with the substrate and the regime, and with the closure loop drawn explicitly. The modularism caution applies: draw IWM/ISM as regions of one wired substrate band and EWM/ESM as regions of one running band, not four boxes.

**Nodes — FMT (fixed geometry):**
- `L1-3` substrate band (physical / electrochemical / proteomic)
- `IWM`, `ISM` — bottom band, "wired", inside `L4 topological`
- `CH` — a narrow neck between the bands (the *Arbeitsmodell* / workspace)
- `PERM` gate — on the neck
- `EWM`, `ESM` — top band, "running", `L5`; ESM drawn nested inside EWM
- `CL` loop arrow — ESM → EWM update rule → ESM
- `FM` — a background field under everything: "free modelling (criticality = its signature in some brains)"
- `LAD` — a stack of 3 small rings on ESM (einfach / doppelt / dreifach erweitert)
- `VQ` — a label on the top band only
- `MP` — a dashed opacity line between ESM and ISM

**Edges — FMT:**
- `IWM→EWM` and `ISM→ESM` (*generated from*; never labelled "transfer")
- `EWM/ESM→IWM/ISM` (consolidation, write-back)
- `CH` carries both
- `ESM→EWM` (CL)
- `ESM⇢ISM` (blocked: MP)

**Overlay nodes — theories, placed on the component they claim (colour = verdict on the constitutive claim):**
- IIT → halo over the whole top band + FM field; red outline on the substrate band (identity with substrate cause-effect power)
- GNW → on `CH` (green: structure); red badge "constitutive?"
- CTM → on `CH` + small "Model-of-World ⊇ self" tag on EWM⊇ESM
- PP / FEP → on the IWM/ISM band and the generating arrows; blue
- REBUS → on `PERM`; green
- Beautiful Loop → on `CL`; green
- ICT → on `CL`; green with red "self-model not required" badge
- HOT → on `LAD`; green, with red badge "per-state transitivity"
- PRM → small tag on the ESM/EWM border "source tag"; blue
- RPT → on the generating arrows (recurrence); red badge "local recurrence sufficient"
- AST → on ESM / the attention edge into CH; green, with red badge "deflationary"
- Illusionism → on `RV` line / `MP`; red badge on `VQ`
- Metzinger SMT → on ESM; green; red badge "MPE (selfless)"
- Seth beast machine → on `ISM→ESM` (interoceptive); green; red badge "life required"
- Searle → outside frame, red arrow to `SI` label
- Enactivism → outside frame at the body/world edge; blue arrow to FM "autonomous recruitment"; red badge "anti-representational"
- DIT → at the L4→L5 boundary and the CH neck (thalamocortical); green
- IWMT → large blue halo over EWM+ESM+FM

**Legend sentence:** "Each theory is placed on the part of FMT its central claim is about. Its colour says whether FMT keeps that claim (green), can live with it (blue), takes no side (grey), or rejects it (red)."

### D2 — Layered "which level does each theory address" chart
- **Rows (bottom → top):**
  - R1 substrate / cellular (L1–L3)
  - R2 circuit / connectivity (L4, implicit models)
  - R3 dynamical regime (FM; criticality signature)
  - R4 channel / access (CH, ignition, working memory)
  - R5 running models (EWM / ESM, L5)
  - R6 closure (CL)
  - R7 recursive depth (LAD)
  - R8 phenomenal ontology (VQ vs illusion vs identity)
  - R9 meta-problem (MP)
  - R10 substrate metaphysics (SI vs biology vs life)
- **Columns:** the 15 theories + FMT.
- **Cells:** a filled mark where the theory makes a *claim* at that level, with the verdict colour. Empty = the theory is silent there.
- **Expected visual result:** FMT's column is the only one filled from R2 to R10. GNW clusters at R4; IIT at R3/R8/R10; RPT and DIT at R1–R2/R5; HOT, AST and PRM at R7/R9; illusionism at R8–R9; Searle, Seth and enactivism at R10. That makes the "FMT spans the levels the others each address" claim visible without asserting it. **The risk is that it looks self-serving** — mitigate by marking FMT's own *weak* cells honestly: R1 (no cellular mechanism of its own), R6 (no accepted protocol, SMoC B1), formalisation (a separate column "formal model?" where IIT, CTM, FEP, ICT and IWMT score and FMT does not yet).
- **Data source:** this brief's §1 table, plus a level tag per claim (§4, column `level`).

### D3 — Bipartite claim graph (doubles as Mudrik prediction-map input)
- **Left nodes:** FMT atomic claims (IDs from §4, e.g. `F-CL1`, `F-CH2`). Size = core vs periphery (core = Principles 1–3 and the 2×2 derivation; periphery = mechanisms and predictions).
- **Right nodes:** rival-theory claims (`IIT-1` "experience = substrate's max-irreducible cause-effect structure", `GNW-1` "broadcast constitutive", `RPT-1` "local recurrence sufficient", `HOT-1` "transitivity principle", `AST-1` "awareness = attention-schema content, deflationary", `ICT-1` "NTIC sufficient", …).
- **Edges, typed:** `entails` (green), `compatible` (blue), `contradicts` (red, labelled with the C-number from §2), `implemented-by` (dotted — e.g. `F-CH1 implemented-by DIT-1`).
- **Prediction nodes:** FMT Pred. 1–5 and the Table 1b falsifiers hang off FMT claims with `predicts` edges. Each red edge links to the experiment that would decide it.
- **Layout:** core-periphery, FMT core at the centre (Mudrik's convention). Red edges cross the middle, so the contested ground is visually central.
- **Minimum edge list** (initial, from §1–2):
  - `F-CL1 —contradicts(C4)— RPT-1`
  - `F-CL1 —contradicts(C2)— GNW-1`
  - `F-CL1 —contradicts(C9)— ICT-1`
  - `F-CL1 —entails/≈— BL-1`
  - `F-VQ1 —contradicts(C6)— AST-1, ILL-1`
  - `F-SI1 —contradicts(C10)— BN-S1, BN-Seth1`
  - `F-LAD1 —contradicts(C3)— HOT-1`
  - `F-CH1 —entails— GNW-2 (capacity-limited workspace)`
  - `F-CH3 —implemented-by— DIT-1`
  - `F-PERM1 —implemented-by— REBUS-1`
  - `F-ID1 —contradicts(C1)— IIT-1`
  - `F-MOD1 —contradicts(C11)— ENA-1`
  - `F-P3 —contradicts(C7)— SMT-MPE1`

**Recommendation:** D1 for the wiki and the poster (one picture that people remember). D2 as the paper's main figure (honest, comparative). D3 as the machine-readable artefact for AIW-276/277, with a rendered version as a supplementary figure.

---

## 4. Format, venue, and reusable claim decomposition

### 4.1 Format recommendation
- **Both, wiki first.** A new wiki page `wiki/comparative/theory-map.md` (D1 + the §1 table, linking to the existing `vs-*` pages rather than repeating them). Add four short new pages where the wiki is empty: `vs-iwmt` (from AIW-119), `vs-ict` (from AIW-129), `vs-illusionism-and-biological-naturalism`, `vs-enactivism`. Fix `vs-rpt` and `vs-hot` per §0.1. No exposure risk, and it can go live immediately.
- **Paper second.** A short theory paper, "Where the theories sit: an architectural map of consciousness science from the four-model perspective" (working title), ~6–8k words, D2 + D3 + the contradiction catalogue with deciding experiments.
- **Venue candidates:**
  - **Neuroscience of Consciousness** — fits; but NoC already has the AIW-130 slice in play, and the AIW-149 "superset prejudices subsets" question applies. Ask Kleiner.
  - **Frontiers in Psychology — Consciousness Research** (where ICT appeared; accepts theory/hypothesis articles).
  - **Philosophy and the Mind Sciences** (open access; ran DIT and MPE).
  - **Journal of Consciousness Studies.**
  - **Avoid** pitching it as an FMT promotion piece. Frame it as a *method*: "an architectural coordinate system for comparing theories, demonstrated with FMT as the reference frame". That ties to the MoC7 Comparing Theories session (Dolega's meta-theoretic framework, Yan's common formal idiom) and to SMoC (AIW-146), and is the weaker-defended, more useful position the S285d decision recommended.
- **Sequencing:** the wiki page before any submission; the paper after MG decides AIW-146 §7 (whether SMoC is the parent paper — the theory map may be one of its chapters).

### 4.2 Mudrik claims-as-graphs and the ETH tool — design for reuse
- **Mudrik programme (verified [V]):** "Prediction maps as a gateway to better understand and test scientific theories", Negro, Elbaz, Fischer, Schreiber & Mudrik 2026, OSF preprint. Theories become networks of beliefs (claims + empirical predictions) structured core-periphery, with inferential edges and graph-centrality metrics. The OSF listing mentions a platform for creating or uploading maps. Related: ConTraSt (Yaron et al. 2022 [FMT]). **Next step: fetch the preprint and its upload schema before finalising the column format below** — not done here.
- **ETH Zurich "LLM-based theory tool": UNVERIFIED — could not be identified.**
  - The last MoC7 programme item is a plenary discussion. The last talk is Teodora **Vukovic (University of Zurich, not ETH)**, "An AI-powered Data Science Platform for Multimodal Human Understanding". That is a multimodal data platform, not a theory tool.
  - The ETH speakers in the booklet are Peter Thestrup **Waade** (ETH Zürich, Friday 12:00–12:20, Aud. 3, the last slot of that parallel session: "Towards joint computational modelling of experiential, cognitive and neural dynamics") and Harald **Atmanspacher** (ETH/Essex keynote, dual-aspect monism).
  - A related LLM-pipeline poster (C-test database; LLM screening plus MOSAIC topic map plus a "data-driven causal graph network") is in the booklet, ~line 1590, affiliation not checked.
  - A web search found no ETH theory tool. **MG must say which talk he meant (Q7).**
- **Claim schema (one row per atomic claim; CSV + JSON-LD export):**
  `id | subject | predicate | object | section | claim_type {definition, principle, consequence, mechanism, bridging, prediction, falsifier} | core_periphery {core, periphery} | depends_on [ids] | level {L1..L5, CH, CL, LAD, ontology, metaphysics} | evidence_status {untested, converging, supported, contested} | falsifier (text) | rival_relations [{theory_claim_id, relation, C-id}]`
- Rationale:
  - `depends_on` gives Mudrik's inferential edges.
  - `core_periphery` gives her structure.
  - Triples are what an LLM tool most plausibly ingests.
  - `rival_relations` builds D3.
  - The FMT derivation chains are already explicit in §6.0 and §8.2–8.6 ("Derivation: Principle 2 → … → prediction"), so `depends_on` can be filled from the text, not invented.

### 4.3 FMT atomic claims — draft triple list (section-referenced)
**Core (principles, definition, derivation):**

| id | subject | predicate | object | § | type | depends_on |
|---|---|---|---|---|---|---|
| F-DEF1 | consciousness | is | the ongoing capacity of an entity to create a self-model, relate it to itself, and interact with it | 3.1 | definition | — |
| F-DEF2 | consciousness | is a | process, not a property | 3.1, 4.2 | definition | F-DEF1 |
| F-P1 | open-ended (Class-4-capable) computation | enables | free modelling | 3 (P1), 3.7 | principle | — |
| F-FM1 | free modelling | is necessary but not sufficient for | consciousness | 3.7.3, Table 1b | principle | F-P1 |
| F-FM2 | free modelling | requires | capability ∧ free instantiation ∧ autonomous recruitment | 3.7.3 | principle | F-FM1 |
| F-FM3 | near-criticality | is | a contingent signature of free modelling in some neural tissue (neither necessary nor sufficient for consciousness) | 3.7, Table 1 | consequence | F-FM1 |
| F-P2 | recurrent non-linear dynamics of sufficient complexity | host | a second computational level (persistent patterns individuated by mutual effects) | 3.3 (P2) | principle | F-P1 |
| F-P3 | phenomenology | arises at | the point where the self-model and the world-model each enter the other's update rule (closure) | 3.4 (P3), 3.4.3 | bridging | F-P2 |
| F-2X2 | any conscious system | must model | world and self, at both the stored (implicit) and the generated (explicit) level | 3.2 | consequence | F-P2, F-P3 |
| F-2X2b | the four model kinds | are | the minimum, not the count ("four is the floor") | 3.2 | consequence | F-2X2 |
| F-NEST | ESM ⊆ EWM; ISM ⊆ IWM | (scope is a nesting) | — | 3.2 | definition | F-2X2 |
| F-RV1 | implicit models (IWM, ISM) | are stored in | substrate connectivity and are never directly conscious | 3.2, 3.3 | consequence | F-2X2 |
| F-RV2 | explicit models (EWM, ESM) | are generated from | the implicit models plus current input (constitution, not transfer) | 3.3, 3.6 | consequence | F-RV1 |
| F-SI1 | consciousness | is independent of | substrate material, given the architecture and free modelling | 4.4 | consequence | F-FM2, F-2X2 |
| F-THR | free modelling ∧ four-model architecture | are jointly sufficient for | consciousness | 3.7.3 | principle | F-FM1, F-2X2 |

**Ontology:**

| id | subject | predicate | object | § | type |
|---|---|---|---|---|---|
| F-VQ1 | qualia | are | constitutive properties of the computational level, real there and incoherent at the substrate level | 3.4.2 | bridging |
| F-VQ2 | the substrate (incl. the whole cortical automaton) | is not | conscious | 3.4.2, 3.7.2 | consequence |
| F-VQ3 | relational qualia structure | is | shareable across individuals; absolute encoding is not | 3.4.2, 8.6 | consequence → Pred. 5 |
| F-CL1 | self-referential closure | distinguishes | conscious from non-conscious computation (monitoring without closure does not suffice) | 3.4.3 | bridging |
| F-CL2 | the inside/outside asymmetry created by closure | is | constitutive, not merely epistemic (argued, not derived) | 3.4.3 | bridging |
| F-TE1 | recursion under closure | produces | temporal smearing that constitutes experienced flow | 3.4.4 | mechanism |
| F-ILL1 | FMT | denies | illusionism (qualia are real at the computational level) | 3.4.5 | ontology |
| F-FUN1 | some computational-level properties | are | constitutively processual (exist in the running, not in the description) | 3.4.5 | ontology |
| F-AP1 | access and phenomenal consciousness | are | two level-descriptions of one running process | 3.4.6 | consequence |

**Mechanisms:**

| id | subject | predicate | object | § | type |
|---|---|---|---|---|---|
| F-LAD1 | consciousness | is graded by | depth of recursive self-modelling (basic → simply → doubly → triply extended) | 3.5 | consequence |
| F-LAD2 | basic consciousness | has | phenomenal experience without first-order self-observation | 3.5, 3.4.6 | consequence |
| F-LAD3 | conversion of present content into accessed content | is produced by | added recursive depth, not a broadcast stage | 3.4.6 | mechanism |
| F-PERM1 | implicit→explicit permeability | is | a modulable family of boundary properties (local and global modes) | 3.6, 6.0 | consequence |
| F-CH1 | explicit models | read and write the implicit models through | a low-rank channel | 3.6.1 | mechanism |
| F-CH2 | working-memory capacity | equals | the channel's rank (predicts no scaling with brain volume) | 3.6.1 | mechanism → prediction |
| F-CH3 | the global workspace | is | the channel's current occupancy (*Arbeitsmodell*), not constitutive of experience | 3.6.1, 7.2 | mechanism |
| F-CH4 | attention | selects into | the channel; closure passes back over it | 3.6.1 | mechanism |
| F-CH5 | anaesthesia | abolishes experience by | channel failure with the wired layer intact | 3.6.1, 3.3 | mechanism → prediction |
| F-MP1 | the ESM | cannot model | its own generating substrate (ISM), producing the meta-problem intuition | 3.8 | consequence |
| F-BIND1 | binding | is | dissolved by the shared substrate and its dynamics, not solved by a mechanism | 5.1 | consequence |
| F-SRC1 | the architecture | requires | source distinguishability between live and forked runs | 6.0 | consequence |
| F-FORK1 | the ESM | can be | forked, cloned, redirected, reconfigured | 3.3, 6.0 | consequence |
| F-LLM1 | current LLMs | lack | closure, persistent self-produced implicit-model update, and the open-ended regime | 4.4 | consequence |

**Predictions / falsifiers** (link `predicts` edges):

| id | statement | § | depends_on |
|---|---|---|---|
| F-PR1 | Sub-ego-dissolution psychedelics improve anosognosia awareness, dose-dependently; strongest in disconnection-type cases | 8.2 | F-PERM1 |
| F-PR2 | Ego-dissolution identity content tracks the dominant sensory modality | 8.3 | F-P3, F-FORK1, F-PERM1 |
| F-PR3 | DID alter dissimilarity follows a self-referential > sensorimotor gradient | 8.4 | F-FM1, F-FORK1 |
| F-PR4 | Lucid onset = phase-transition signature originating in self-model networks (a signature prediction; its failure does not refute F-FM1) | 8.5 | F-FM3, F-LAD1 |
| F-PR5 | Unsupervised structural alignment of qualia spaces generalises across individuals; absolute decoding does not | 8.6 | F-VQ3 |
| F-FAL1 | Robust consciousness where a fixed lookup reproduces behaviour on novel input → refutes F-FM1 | Table 1b | F-FM1 |
| F-FAL2 | Disrupting the self-modelling loop degrades experience, not merely report (see §2 C3 caveat) | Table 1b | F-CL1 |
| F-FAL3 | Implicit learning continues under anaesthesia while explicit models are suppressed | Table 1b | F-RV1 |

**Rival claim nodes needed for D3** (to be sourced per theory before encoding): IIT-1 (identity with intrinsic cause-effect structure), IIT-2 (Φ>0 ⇒ some experience), IIT-3 (inactive units contribute); GNW-1 (broadcast constitutive), GNW-2 (capacity-limited workspace); HOT-1 (transitivity principle), HOT-2 (empty HOTs suffice); PRM-1 (reality tag constitutive); RPT-1 (local recurrence sufficient); AST-1 (deflationary schema), AST-2 (schema serves attention control); SMT-1 (transparent self-model), SMT-MPE1 (selfless minimal experience); IWMT-1 (graded multi-factor demarcation); DIT-1 (apical-basal coupling gates consciousness); ICT-1 (NTIC sufficient); CTM-1 (consciousness in any properly organised computing system); ILL-1 (no phenomenal properties); BN-S1 (biological causal powers required); BN-Seth1 (life required); ENA-1 (experience is sensorimotor activity, not internal model); BL-1 (self-evidencing loop constitutive).

---

## 5. Open questions for MG

1. **RPT verdict.** OK to correct master §7.2 and wiki `vs-rpt` from "compatible" to "contradicts on sufficiency (local recurrence), absorbed on necessity (recurrence)"? That is a master edit → a new version.
2. **HOT and the Table 1b falsifier.** (a) Confirm FMT does *not* require a per-state higher-order representation: basic consciousness is phenomenal before first-order self-observation (§3.5). If so, wiki `vs-hot` "necessary" must be fixed. (b) Table 1b says "metacognitive disruption leaves phenomenology intact" falsifies closure, yet FMT also says metacognitive read-out is separable from first-order experience (type-2 decoupling). Is the falsifier about **closure** disruption, not **metacognition** disruption? It needs rewording either way, or HOT people will cite it as FMT agreeing with them.
3. **PP placement.** Does PP machinery implement the implicit layer (master), the explicit models (wiki), or both? One sentence is needed for D1.
4. **IIT "adopts".** Soften §7.2's "adopts IIT's central diagnosis" to "shares IIT's demand for intrinsic, integrated structure; rejects the substrate identification"?
5. **Metzinger MPE.** Is MG content to commit the map to "selfless MPE reports are post-reflective reconstructions of a thin-ESM state" (the AIW-280 line)? Or should the map list MPE as an **open threat** to Principle 3? Honest default: open threat plus the FMT reply.
6. **New master paragraphs.** The map engages theories the master is silent on (ICT, CTM as a theory, Searle, enactivism, PRM, MPE). Add short master paragraphs first (so the map cites FMT, not itself), or let the wiki/paper be the first statement?
7. **Which "ETH Zurich LLM-based theory tool"?** It could not be identified. The last MoC7 talk is Vukovic (UZH, multimodal data platform). ETH talks: Waade (computational modelling of experience–cognition–neural dynamics) and Atmanspacher (keynote). Name or contact needed before AIW-277 can pick an input format.
8. **Mudrik route.** gmail-intake shows Mudrik replied 2026-10-08; whether you met at P56 is unknown. Should the first offer be the 2015 derivation-chain record (as gmail-intake suggests) or this triple list? And may I fetch the OSF preprint/platform schema next?
9. **Paper vs SMoC chapter.** Standalone paper, or a chapter/section of the SMoC middle-layer paper (AIW-146 §7 decision 6 is still open)?
10. **Scope.** Add Damasio, Hofstadter, TTC (Northoff), Solms, Bach, RIFT and the Multiple Generator Hypothesis (already in master §7.3 / wiki) to the map, or keep to the 15 named here?
11. **Tone of D2.** Accept the honesty columns (FMT's empty cells: cellular mechanism, closure protocol, formal model) as the price of a chart that doesn't look self-serving?

---

## 6. Citations verified this session [V]
- Cogitate Consortium (2025). Adversarial testing of global neuronal workspace and integrated information theories of consciousness. *Nature*. doi 10.1038/s41586-025-08888-1
- Negro, Elbaz, Fischer, Schreiber & Mudrik (2026). Prediction maps as a gateway to better understand and test scientific theories. OSF preprint (abstract only; full text not read)
- Blum, L. & Blum, M. (2022). A theory of consciousness from a theoretical computer science perspective: Insights from the Conscious Turing Machine. *PNAS* 119(21). doi 10.1073/pnas.2115934119
- Chang, Biehl, Yu & Kanai (2020). Information closure theory of consciousness. *Frontiers in Psychology* 11:1504. doi 10.3389/fpsyg.2020.01504
- Seth, A.K. (2025). Conscious artificial intelligence and biological naturalism. *BBS*. doi 10.1017/S0140525X25000032
- Aru, Suzuki & Larkum (2020). *TiCS* 24(10), 814–825. doi 10.1016/j.tics.2020.07.006
- Suzuki & Larkum (2020). General anesthesia decouples cortical pyramidal neurons. *Cell* 180(4), 666–676. doi 10.1016/j.cell.2020.01.024
- Brown, Lau & LeDoux (2019). Understanding the higher-order approach to consciousness. *TiCS* 23(9), 754–768
- Lau, H. (2022). *In Consciousness We Trust*. OUP
- Frankish, K. (2016). *JCS* 23(11–12), 11–39
- Wilterson et al. (2020). Attention control and the attention schema theory of consciousness. ***Progress in Neurobiology*** 195:101844 (not PNAS)
- Lamme (2006). *TiCS* 10(11), 494–501
- Safron (2020). *Frontiers in AI* 3:30
- Thompson, E. (2007). *Mind in Life*. Harvard UP
- Searle, J. (1992). *The Rediscovery of the Mind*. MIT Press

**UNVERIFIED — check before use:**
- Tononi, Boly, Massimini & Koch 2016 (*Nat Rev Neurosci*; inactive vs inactivated)
- Searle 1980 (*BBS*, Chinese room)
- Varela, Thompson & Rosch 1991
- Metzinger 2020 (MPE, *Phil. Mind Sci.*)
- Odegaard, Knight & Lau 2017
- Boly et al. 2017
- Lamme et al. 1998
- Sligte et al. 2008
- Bayne, Seth & Massimini 2020 (islands of awareness)
- Bruineberg et al. 2022 (Markov blankets)
- Friston 2018 ("Am I self-conscious?")
- Seth's 2026 BBS reply "The stuff matters" (secondhand)
- The ETH tool (unidentified)
