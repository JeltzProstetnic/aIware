Action: reference
Tracked-by: AIW-72, AIW-73

# GAN Investigation — Cortex/Basal Ganglia Adversarial Dynamics

Session 213 ran 3 parallel research agents. Results below.

## Verdict

**Genuine theoretical advance, not just vocabulary reframing.** The GAN framing fills three specific gaps in FMT:

1. **Permeability mechanism underspecification.** FMT's permeability construct describes states (psychedelics = high, anosognosia = low) without specifying a real-time mechanism for moment-to-moment permeability decisions. The GAN framing converts this state variable into a dynamic process: basal ganglia RPE gating at the implicit-explicit boundary.

2. **Schizophrenia absent from explanatory range.** FMT covers psychedelics, anesthesia, DID, anosognosia, sleep — but not schizophrenia. The GAN interpretation provides: discriminator miscalibration → aberrant salience → unchecked generator output → hallucinations (false sensory candidates pass gate) + delusions (false world-model updates carry false RPE). Three-symptom-cluster mapping: positive = discriminator too permissive; negative = discriminator too conservative; cognitive = discriminator noisy.

3. **New testable prediction.** Psychedelic content should not just increase in quantity (permeability alone predicts this) but should specifically violate normal salience/reward hierarchies — inappropriately salient stimuli, unexpected associative connections. Testable via reward-valence ratings of psychedelic imagery in dose-response paradigms.

## Correct FMT Mapping

- **Generator**: IWM + ISM (implicit substrate, Level 4 topology), producing candidate model updates
- **Discriminator**: Basal ganglia dopaminergic RPE as primary evaluator at permeability gate; ESM self-referential feedback as secondary structural discriminator once candidates enter simulation
- **Training signal**: RPE = gap between expected and received reward/evidence

NOT: cortex = generator, basal ganglia = discriminator (this would violate the five-level hierarchy — basal ganglia operate at Levels 3-4, not Level 5 where explicit models are constituted).

## Key Literature

| Paper | Finding | Relevance |
|-------|---------|-----------|
| Gershman (2019) "The Generative Adversarial Brain" *Frontiers in AI* | Brain learns via adversarial framework; discriminator failure → hallucinations/delusions | Direct theoretical precedent for biological GAN |
| Deperrois et al. (2022) "Learning cortical representations through perturbed and adversarial dreaming" *eLife* | PAD model: REM sleep implements adversarial training for semantic representations | REM as discriminator (re)training — extends FMT's sleep account |
| Benjamin & Kording (2023) "A role for cortical interneurons as adversarial discriminators" *PLOS Comp Biol* | PV+ interneurons as discriminators; wake=Hebbian, sleep=anti-Hebbian | Specific circuit for discrimination within cortex |
| Gershman (2021) "From internal models toward metacognitive AI" *arXiv* | Discriminator as confidence monitor → metacognition | ESM's metacognitive capacity as discriminator output |
| Deperrois et al. (2024) "How Adversarial REM Dreams May Facilitate Creativity" | REM adversarial dreaming → creative insights | GAN + creativity + dream phenomenology |
| Benios & Gershman (2021) "Modeling the Hallucinating Brain" *arXiv* | GANs model hallucinations as discriminator failure | Schizophrenia mechanism support |

## Compatibility with FMT

- **Criticality**: No conflict. GAN requires edge-of-chaos for generator to produce varied candidates while discriminator can evaluate coherently. Mutual reinforcement.
- **Real/virtual split**: Compatible if discriminator operates at the permeability boundary (pre-virtual), not on already-virtual representations.
- **Self-referential closure**: Compatible. ESM self-referential loop is the *result* of the GAN process, providing stability to accepted candidates.
- **Adversarial vs cooperative**: "Biological GAN" is evocative but the mechanism is closer to actor-critic RL than true adversarial training. Use "competitive selection" not "adversarial training" for precision.

## Recommended Integration

Incorporate as **mechanistic elaboration of permeability** in §9 (Open Questions) or §10 (Discussion), not as a 6th principle. Candidate text: "One candidate mechanism for the variable permeability construct is the dopaminergic prediction-error gating of corticobasal ganglia-thalamo-cortical loops — a biological selection architecture that in its functional structure resembles the generator-discriminator dynamic of generative adversarial networks, though implemented as cooperative actor-critic dynamics rather than adversarial training."

## Psychedelics under GAN

5-HT2A agonists disrupt discriminator threshold → content that would normally be rejected (low-reward, low-salience implicit patterns) passes gate → characteristic psychedelic quality of unexpected associative connections and inappropriately salient stimuli. This converts FMT's correlation-based anosognosia prediction into a mechanistically grounded one.

## Additional Neuroscience Evidence (Agent 3)

**6-layer cortex = two stacked 3-layer circuits — SUPPORTED.** Shepherd (2011, *Frontiers in Neuroanatomy*, PMC3102215) argues the ancestral 3-layer cortex (olfactory, hippocampal) was elaborated into 6-layer neocortex as two integrated subsystems:
- **Superficial (layers 1-3):** Receives cortico-cortical input (top-down feedback). Outputs to other cortical regions. = prediction/generation layer in PP terms.
- **Deep (layers 4-6):** Receives primary thalamic input (layer 4 stellate relay). Outputs to subcortical structures including BG (via layer 5 pyramidals). = error/reality layer.

**Critical connectivity asymmetry:** Layer 5 projects to BG; layers 2/3 do NOT project to BG directly. The evaluator (BG) specifically receives input from the deep/feedback subsystem, not the sensory-processing superficial layers. This is structurally consistent with GAN: generator (deep layers, producing descending predictions/action proposals) talks to evaluator (BG).

**Opponent learning with different representations** (eNeuro 2023, PMC9884109): Direct (D1, "Go") and indirect (D2, "No-Go") pathways don't just have opposite signs — they use fundamentally different state representations (Successor Representation vs Individual Representation). This maps onto GANs where generator and discriminator also have architecturally different roles.

**BG as dynamics selector, not gate** (Mannella & Baldassarre, 2015, Biol Cybernetics): BG don't select between cortical modules — they select between cortical *dynamics*. Cortex = dynamical reservoir, BG = selector of which trajectory the reservoir follows. Direct precursor to GAN interpretation.

**BG computational bottleneck** (eNeuro 2024): Striatum ~2.8M neurons → SNr/GPi ~30,000 (100:1 compression). BG output sets basis-function weights on cortical dynamics rather than selecting among them directly.

## Theoretical Clarifications (Session 213, user corrections)

- **Scale symmetry — reframed as computational role asymmetry:** NOT mathematical scale symmetry (renormalization-group type). The real observation: massive parallel generator (cortex, 6-layer, billions of neurons) vs compressed evaluator (BG, 100:1 bottleneck, ~30K output neurons). Neuronal-level scale asymmetry without large-scale topological symmetry. The asymmetry IS the functional point — generator capacity dwarfs evaluator capacity, which is the computational signature of a GAN architecture. Supported by BG bottleneck literature (eNeuro 2024).
- **Hemispheric mirror symmetry — evolutionary redundancy:** Originally mirror redundancy for fault tolerance; late-evolving asymmetries (language, handedness) only possible because organisms large enough that redundancy no longer survival-critical. GAN dynamics may exist across hemispheres but not as a significant inter-hemispheric feature. Not a GAN argument — drop from paper framing.
- **Two-voice phenomenology — GAN echo, not 3-system competition:** User correction: the two voices are the fundamental generate-evaluate tension (generator proposals vs discriminator rejections) echoing up to conscious language processing via the ESM. They're Level 5 phenomena reflecting Level 3-4 adversarial dynamics. Not two brain regions arguing. Hard to prove, keep as illustrative phenomenology only — do not cite as evidence.
- **No standalone paper.** All GAN material integrates into FMT v9 as mechanistic elaboration of permeability. Strategy: settle FMT in published research as deeply as possible. GAN framing grounds the permeability construct in published neuroscience (Gershman 2019, Deperrois 2022, Benjamin & Kording 2023, Shepherd 2011).

## Publishability Assessment (Agent 3)

This is a Theory/Perspectives paper, not empirical. Best venue: *Trends in Cognitive Sciences*, *Neural Networks*, *Current Opinion in Neurobiology*, or *Frontiers in Computational Neuroscience*. Core novelty: (1) formal mapping of deep/superficial laminar circuits onto GAN roles, (2) opponent learning as biological GAN training, (3) BG-as-dynamics-selector as training mechanism. The hemispheric and phenomenological material should be open questions, not evidence.

## Full Additional Literature

| Paper | Finding |
|-------|---------|
| Shepherd (2011) *Front Neuroanat* PMC3102215 | 3-layer → 6-layer cortex evolution; two functional subsystems |
| Opponent Learning eNeuro 2023 PMC9884109 | Direct/indirect pathways use different state representations |
| iScience 2024 Direct/indirect pathways | Pathways antagonistically modulate coding of task-relevant variable |
| Mannella & Baldassarre (2015) *Biol Cybern* PMC4656718 | BG select cortical dynamics, not modules |
| Dual Competition eNeuro 2018 PMC6325557 | Cortex + BG run separate parallel competitions |
| BG Bottleneck eNeuro 2024 PMC12039478 | 100:1 compression, BG output = basis-function weights |
| Alexander & DeLong (1986) | 5 parallel cortico-BG-thalamo-cortical loops |
| Predictive Motor Control GAN bioRxiv 2023 | Explicit GAN framing for cortex-BG motor control (preprint) |

## Open Questions for Next Session

1. Does the "two-voice" survival phenomenon map to adversarial output surfacing to consciousness, or is it simply competing prefrontal evaluations? (Latter is more parsimonious.)
2. **DECIDED: No standalone paper.** All GAN material integrates into FMT v9 — likely §9 (Open Questions) or new §10.x (Discussion). Strengthens the one paper we're fighting to get published.
3. The Deperrois PAD model (REM = adversarial training) connects to FMT's sleep account — potential for extending §6.3 REM rewrite with GAN framing.
4. Where in the paper does GAN material go? Candidate locations: (a) new subsection in §3.6 (implicit-explicit boundary) explaining the mechanism, (b) §9 Open Questions as "candidate mechanism for permeability," (c) §6.2 anesthesia/clinical expanded to include schizophrenia via GAN. User should decide placement.
