# FMT mini-model: requirements from MG's texts

**Date:** 2026-10-27 (aIware S362). **Status:** research input for the crucible/Jülich spec. Nothing here is MG-approved yet.
**Binding spec:** `docs/sources/mg-2026-10-27-fmt-substrate-spec.md` (SPEC), including its Correction (l.16–18) and Core principle (l.21–23).
**Sources:** master `paper/full/four-model-theory-full.md` (M), formalization `paper/fmt_formal/fmt-formalization.md` (F), `.claude/knowledge/fmt-2015-definitions.md` (D15), `fmt-misconception-registry.md` (REG), `didactic-patterns.md` (DP). Line numbers refer to the files as of today.

**In one sentence:** the substrate holds the two implicit models (connectome and weights), and everything else is an *activity pattern that meets the theory's own definition of a model*. So the core deliverable is the method that decides when spiking activity is a model, of what, and of which kind. The network exists to produce such patterns.

---

## 0. Operational definition of an activity-model: requirements from the texts

SPEC l.21: *"the secret is in defining, finding and analyzing spiking activita AS MODELS, thats the trick FMT offers."* The texts already define "model". The instrument has to put that definition into operation; it must not invent its own.

| ID | Requirement | Text (file:line) | What the instrument must do |
|---|---|---|---|
| AM-1 | A model is a state *M* with a mapping *h* to a target *T* that preserves the relations the system acts on, and it can be **evaluated** against *T*, with an error the system can register. | M:152 *"such that M can be evaluated: operating on M yields states that h relates to consequences in T … A structure the system cannot evaluate is a data structure, not a model."* | For each candidate pattern, name *T*, fit *h*, and show that the system's own downstream dynamics use the pattern to anticipate consequences in *T*. |
| AM-2 | Three operational properties: write access, read access and boundary recognition. | M:164 *"(1) write access (updates from new input), (2) read access (evaluation of its own representations), (3) boundary recognition (differential response inside vs. outside the target domain)"* | Three tests per object: it updates when *T* changes, it is read by other activity (causal ablation changes downstream behaviour), and it responds differently to perturbations inside and outside *T*. |
| AM-3 | Being decodable is not enough. The pattern must be computed upon. | M:1087 *"Maintained-and-decodable is therefore demonstrated and computable-upon is not, and the two must not be conflated: the theory's claim is about the second."* | A linear decoder hit is a candidate only. Promote it to a model only after a causal-use test with a passive-delay-line control. |
| AM-4 | Implicit and explicit differ by **mode**: the implicit kind is stored in connectivity and evaluated by substrate processing, the explicit kind is generated as running activity. | M:152 *"stored in connectivity and evaluated by substrate processing, or generated as running activity"*; F:269–274 (implicit = partitions of *W*, explicit = projections of *x(t)*) | Implicit models are read off *W*. Explicit models are read off *x(t)*. Never label a block of *W* as "the EWM". |
| AM-5 | Activity-models are individuated by their **mutual effects**, not by the cells that carry them. Persistence matters, geometry does not. | M:138, M:240 *"persistent activity patterns that survive their own inputs, interact, and compute over one another, individuated by their mutual effects rather than by which cells carry them"*; M:242 *"the claim is persistence, not geometry"* | Track objects across changing cell sets, including travelling waves. Define identity by the object's causal signature. A fixed cell mask is not an identity. |
| AM-6 | Explicit models are **generated, not filled by transfer**, and they vanish when the generating activity stops. | M:178, M:232 *"disrupt the generating process … and the explicit models vanish, while the implicit models persist. Restore the generating conditions and the explicit models reconstitute"* | Validity check: an object must disappear under activity suppression and come back after it, with *W* unchanged. |
| AM-7 | **Self versus world** is set by the target. The self is a proper part of the world (ESM⊆EWM, ISM⊆IWM), and the boundary is not sharp. | M:209; D15:124 (2015 p.266) *"Das Selbstmodell ist ein Teil des Metamodells, welcher nicht scharf davon abgegrenzt ist"*; M:228 *"Real neural models do not respect the world/self boundary — they blend across it"* | Score each object on a continuous scope axis (F:53–60) and do not classify it as either self or world. |
| AM-8 | The self-scope is anchored by the **contingency of the system's own action**, and a self model has to be realistic in proportion to the system. | M:236 *"must predict the sensory consequences of its own actions to distinguish self-generated from externally generated signals"*; M:226 ESM *"generated from the ISM … and current interoceptive and proprioceptive input"*; M:325 *"A position estimate alone is not one"* | Self-scope means the object tracks or predicts reafferent (self-caused) input, proprioceptive or interoceptive. A single low-dimensional state variable does not count as a self model. |
| AM-9 | Self and world models have **the same format**. They differ in target and cost, never in the class of operation available to them. | DP cautions (S299): *"no capability difference exists at all, only cost and target"* | Use one detector for both scopes. Do not build a separate self-model detector. |
| AM-10 | **Robust versus dynamical** (MG's terms, SPEC l.5/12). Robust objects track *"what the body does and sees"*. Dynamical objects do *"active, prospective planning and modeling/simulating for future"*. | Text anchors: EWM is generated from IWM plus *current sensory input (which constrains and updates it)* (M:224); free modelling is *"forward simulation over structured representations of situations other than the present one, recruited by the system itself"* (M:456); dreaming is *"offline replay and recombination … run against candidate courses of action … issues in a plan"* (M:601); the thin input pipe *"servos the high-dimensional inner simulation"* (M:613) | Separate the two kinds by their coupling to *current* input versus their predictive content about *non-present* states. Discriminators are in §3 P3 (inference). |
| AM-11 | Being in the loop is distinct from being explicit. Explicit content outside the self–world loop is preconscious. | M:256, M:391 *"held in an explicit model without entering the self-model's closed loop"* | Add a third label per object: does it enter the self–world mutual update? Use the white-box trace (M:201). |
| AM-12 | "Model" equals the 2015 *Bezugssystem*. Knowledge is information assigned to it. The working model (*Arbeitsmodell*) is what currently occupies the channel. | M:152 fn; M:438; D15:429 | The objects the instrument finds are reference systems. Whatever occupies the restriction at a moment is the working model, and its size limit is a measurable quantity (P4). |
| AM-13 | The four kinds are **extremal points of a continuous model density**, not discrete objects. | M:228; F:41 (*"four regions in a continuous space of modeling activity"*: regions of **model space**, not of the network) | Report a density over (scope, mode, robust↔dynamical). The four labels are corners of that space, not bins to fill. |

---

## 1. Commitments table

| ID | Commitment | Quote (file:line) | Constraint |
|---|---|---|---|
| C1 | The implicit models are physically the connectome and the weights. They are the only substrate-level models. | SPEC:8; M:170 *"stored in physical connectivity (synaptic weights, dendritic morphology)"*; M:513 Level 4 | **MUST** |
| C2 | The explicit models are spiking activity that emerges from the implicit models. | SPEC:9 *"MUST EMERGER FROM implicit models AS ACTIVITY"*; M:172 *"generated electrochemical activity patterns with no permanent physical substrate"* | **MUST**. **MUST NOT** engineer EWM/ESM blocks or readout modules. |
| C3 | Implicit models can be localized. Explicit models cannot. | REG #5; M:209 *"not anatomically localized regions"* | **MUST NOT** assign any area to EWM or ESM. |
| C4 | The body model takes up a large fraction of the cortical surface, not one area. | SPEC:18 *"a good fraction of the total cortical area"* (somatosensory, motor, parietal and insular together) | **MUST**. Areas mean functional differentiation across a large sheet. |
| C5 | Body areas are part of the world-model substrate and are reciprocally wired with the rest of it. | M:209 nesting; D15:124 | **MUST** use reciprocal wiring. **MUST NOT** isolate the body areas. |
| C6 | Embodiment gives the self model its content. The first stable attractor is expected to model the body. | M:531 *"the body is what gives the self model its content … the first stable attractor such a network forms is expected to model it"* | **MUST** have a body with proprioception, interoception and motor output. |
| C7 | Self is separated from world by whether feedback is contingent on the system's own action. | M:236 | **MUST** feed reafferent consequences of motor output back in, and **MUST** also supply external input that is not action-contingent. |
| C8 | Closure means that self-activity and world-activity each enter the other's update rule in one reciprocally wired recurrent substrate. Each frame's output also carries into the next frame. | M:138 *"the self-model and the world-model each entering the other's update rule, as they must when both are activity patterns in one reciprocally wired recurrent substrate"*; M:357 | **MUST** be emergent from recurrence. **MUST NOT** equate closure with weight plasticity: a frozen system keeps closure (M:611). **MUST NOT** implement it as an engineered ESM→rest switch. |
| C9 | Write-back to the weights is the separate "maturing" route, which works through consolidation. | M:234, M:603 | **SHOULD** include online plasticity. The two routes are distinct. |
| C10 | Free modelling means Class-4 capability that the system uses autonomously for its own modelling (capability, free instantiation, autonomous recruitment). | M:452, M:533–537 *"capability, free instantiation, and autonomous recruitment … the laptop fails the third"* | **MUST**: no external script may drive the planning. Recruitment may be engineered in, and must then be *"sustained by its own dynamics"* (M:533). |
| C11 | Criticality is a signature, not a requirement. | M:176 *"criticality is neither necessary nor sufficient, and a conscious system may run subcritically"*; REG #3 | **MUST NOT** tune toward σ=1 as a goal. **SHOULD** report σ only next to a rate-matched surrogate (M:1085). |
| C12 | There is a low-rank read/write channel. Its rank is a capacity parameter, not a criterion. A thalamic realizer is not required. | M:436, M:446 *"Nor is a thalamic relay required"*; M:665 | **SHOULD** make the rank of the restriction an explicit parameter. See OQ-1. |
| C13 | Spiking that is close to biology. | SPEC:10 (refractory period, non-zero resting rate) | **MUST** |
| C14 | Topology: a few ganglia-like I/O networks, then ONE thalamus-like restriction, then a cortical sheet with distinct areas and a large free area. Storage is holographic within each area (patchwork). | SPEC:11; M:695 *"locally holographic within individual Brodmann areas"* | **MUST** (topology). **SHOULD** hold for graceful degradation within areas. Explicit models are *not* patchwork (DP #32). |
| C15 | Permeability is a family of modulatory mechanisms, not one knob. | M:417 | **SHOULD** have at least one neuromodulatory gain channel. |
| C16 | At least one pain-pleasure axis is needed, and it may be engineered. | M:531 | **MUST** for the sufficiency conjunction. An engineered sign is allowed. |
| C17 | Sufficiency is a conjunction: four kinds under closure, free compute, embodiment, and a pain-pleasure axis. | M:531 | Design target only. **MUST NOT** claim consciousness. Tests are mechanism tests (M:1083; REG #6). |
| C18 | Implicit content is learned. Structure may be engineered as evolution engineered it. | M:230; SPEC:5 *"may be engineered to a degree (as evolution did)"* | **MUST** combine engineered priors with learning. Taking human-cortex priors for area sizes and wiring statistics is a **SHOULD**. |
| C19 | Qualia exist at the level of the running loop. Their character is inherited from the architecture of the implicit pathway. | M:295, M:365 *"the signature of which implicit model pathway generated that particular piece of the simulation"* | **MUST NOT** model a "quale variable". **SHOULD** give each input modality its own distinct implicit architecture. |
| C20 | Dreaming and daydreaming are the same machinery running under different gating. | M:601, M:795 (input attenuated at the thalamus, motor output blocked) | **SHOULD** support input attenuation and motor gating as switchable regimes. |

---

## 2. Known misreadings to avoid

1. **Explicit models as regions** (SPEC:5, 13). This is the crucible ClosureBrain error.
2. **The body model as one area or column** (SPEC:16–18).
3. **Four modules** (REG #1). The four are corners of a continuous, overlapping ecology. Four is the minimum, not the count.
4. **Transfer instead of constitution** (REG #2). Explicit activity is *made of* the substrate. Use "transfer" only for permeability.
5. **Criticality as the target** (REG #3). Free compute is the requirement.
6. **Binding as a module to add** (REG #4). There is one substrate, so nothing needs binding.
7. **The build is the theory** (REG #6). The model tests mechanisms and does not build consciousness.
8. **Closure as weight learning, or as a hand-wired loop switch.** See C8 and C9.
9. **Decodable taken as computed-upon** (AM-3).
10. **A self model that is only a position or one state variable** (M:325).
11. **Necessity claims.** Closure is an advantage measured at a budget, never a necessity (M:1083; DP cautions). Also MG's own "no free lunch" (SPEC:5).
12. **A lesion read as a removal.** Recurrent ablations relocate loops (F:605; M:1089, where opening the global loop leaves smaller closed systems). Verify with SCC counts before reading outcomes.
13. **A thalamus treated as theoretically required.** It is SPEC's design choice. The theory requires only a channel (M:665).

---

## 3. Observable predictions for early tests

"Text" means stated or directly implied in the sources. "Inference" means my own reading.

- **P1 The body comes first (text, M:531).** In a body-coupled network, the first stable activity-model should track the body. M:531 says this *"has not yet been measured in spiking networks"*, so it is a genuine first test.
- **P2 Generation versus storage (text, M:232, M:172).** Suppress activity globally, as an anaesthesia analogue. Every explicit object should vanish while *W* stays intact. On restore, the objects should reconstitute from *W* and should not come back from residual activity.
- **P3 Robust versus dynamical (inference from AM-10).** Robust objects should have high information with *current* sensory and reafferent input, follow input changes within short lags, and survive only while that input lasts. Dynamical objects should have low coupling to current input and high information about *future* input or actions or non-present states. They should start internally, and ablating them should change upcoming action choice but leave current tracking unaffected. A further inference from M:607 (the decoupled cascade *"cannot occur unless the explicit models are actively running"*): dynamical objects should need robust objects to be present.
- **P4 Lesioning or attenuating the thalamus-like restriction.**
  - Text: with input attenuated, the explicit simulation runs on internally generated input (M:791 dreams; M:836 Anton's syndrome, a *"simulation running without current input"*). When inner dynamics outstrip the thin pipe, *"the simulation then locks into its own attractor, losing reality-contact"* (M:613).
  - Inference: robust objects lose their tether and decay or drift, while dynamical objects persist and become self-sustaining.
  - Text, conditional on the restriction being the channel (OQ-1): the number of objects held at once scales with the rank of the restriction and not with neuron count (M:440).
- **P5 Lesioning body-model areas.**
  - Text: without the ISM, the ESM *"has no source material"* (M:236). A partial lesion inside an area degrades gracefully (M:695).
  - Text: cut proprioceptive and interoceptive input, and the self-scope attractor *"reshapes around"* the most salient external content (F:405–415, salvia redirection).
  - Text: narrowing what the world model covers degrades the self model in proportion, because O_ESM⊆S_EWM (F:459, F:603).
  - Inference: world-scope objects about the external scene should survive the loss of the self-scope objects. This is the ESM/EWM dissociation (M:1107ff, OQ4).
- **P6 Closure.**
  - Text: the white-box trace. An input signal reaches a self-scope object that enters the world-scope object's update rule and is entered by it (M:201).
  - Text: with closure in place, capability on long-horizon or counterfactual tasks scales with the internal simulation budget, and the scaling stops under ablation (M:623).
  - Text: cut the frame-to-frame carrying of the self-object's own state. Decoding of own elapsed time and action order from self-scope activity should fail, while world-scope external time survives (M:1093).
  - Every closure ablation needs the removal audit (F:605).
- **P7 Criticality (text, M:454).** It may or may not appear, and neither result decides anything. Record σ, DFA α and avalanche statistics as descriptors, each against a rate-matched surrogate.
- **P8 Free modelling (text, M:196).** On novel input of growing compositional depth, an unrolled feedforward model with matched capacity, trained on the system's own history, should fall behind. M:1091 states that no task deep enough has been built yet.

---

## 4. Open questions for MG

1. **Is the thalamus-like restriction the read/write channel of M:3.6.1?** The candidates disagree. M:446 makes frontoparietal feedback the leading realizer and says a thalamic relay is not required. D15:429 records MG on 2026-08-05: *"the thalamus is the Bottleneck's own realizer candidate."* SPEC places the restriction between the I/O networks and the cortex. Should it be the I/O relay, the low-rank channel between explicit activity and substrate, or both?
2. **What does "ganglia-like" mean?** Peripheral sensory and motor ganglia, or basal ganglia as the permeability selector of M:1121 (OQ7)?
3. **How large is the body share?** Which fraction and which area types, and is "free area" defined as cortex with no engineered priors?
4. **Are robust and dynamical two classes or the ends of a continuum?** Does each occur in both self and world scope, or does "dynamical" belong mainly to the free-modelling (dreaming) route?
5. **What exactly is engineered, and what is trained "according to what we know about the human cortex"?** For example laminar motif, area sizes, inter-area wiring statistics, developmental exposure through the body.
6. **Should v1 learn online (maturing) or run with frozen weights (dreaming route only, M:611)?**
7. **How should the pain-pleasure axis be implemented in v1?** For instance a neuromodulatory broadcast with an engineered sign. Is it in scope for the two-day build?
8. **Which body:** a simulated body or the WAVEGO robot, and what counts as interoception?
9. **Should closure be left to emerge from engineered reciprocal wiring alone, or may evolution-like priors specifically favour body↔rest reciprocity?**
10. **What does success look like at two days?** P1 (body attractor first) together with a working detector for robust versus dynamical objects, or something else?
11. **What is the Jülich scale target?** It decides whether a task deep enough for free modelling (P8) can be posed at all.
