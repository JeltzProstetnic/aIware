<!-- AIW-269 half (b), AI slice, S323 2026-09-28 subagent. arXiv search was rate-limited (429) mid-run: qualia/sentient/self-model/AI-welfare listings incomplete. Citations unverified by main loop. -->
# AIW-269 literature sweep — slice: AI and machine consciousness

Window: first public 2026-08-26 → 2026-09-28. Swept 2026-09-28 with OpenAlex (date-filtered), Crossref, the arXiv search listing and abstract pages, and web search for PhilPapers/PhilArchive. FMT line numbers refer to `paper/full/four-model-theory-full.md` (v15).
**Coverage caveat:** the arXiv API returned empty bodies, and the arXiv search page returned HTTP 429 part-way through. The "qualia", "sentient", "self-model" and "AI welfare" listing searches therefore never completed, and arXiv coverage for those terms rests on OpenAlex and web search only. I skipped the Zenodo self-deposits (dozens of unreviewed single-author "theories") on purpose.

Each item below was checked against its arXiv abstract page or its Crossref/OpenAlex record for title, authors and date.

---

## A. Self-report, introspection and self-modelling in LLMs

**1. Šekrst, K. — "Who Put the I in AI? Provenance and the Admissibility of Machine Self-Report." arXiv:2609.29494** (v1 submitted 2026-08-24; ID shows it was announced in September).
The paper traces where LLM self-descriptions come from, across 66 Pythia/OLMo-2 pretraining checkpoints, the OLMo-2 post-training stages and four training corpora. It finds that the "I am not conscious" denial formula is almost absent from pretraining text and is installed later in training. Self-reports therefore follow training provenance and question framing, not an inner state.
*Bears on:* l.646, and l.342 ("might report experience while feeling nothing"). It is consistent with FMT's claim that LLM self-talk is not evidence of an ESM.
**Verdict: MUST-CITE.** It is direct empirical support for discounting LLM self-report.

**2. Maczan, J. — "'As a Language Model...': Chat Template Switches LLM Self-Referential Voice and Activation Steering Reproduces It." arXiv:2609.25021** (v1 2026-08-09; announced September).
Across 8 open instruct models, the chat template acts as a switch: with the template, disclaimer voice goes up and experiential "I feel" voice goes down; without it, the reverse. A single activation direction reproduces the effect in 3 models. First-person experiential talk turns out to be a deployment artefact that can be steered.
*Bears on:* l.646. It is consistent with FMT's view that report and self-model can come apart.
**Verdict: MUST-CITE.** Cite it together with #1, as a pair.

**3. Zeng, S., Assis, A. N., & Wang, R. — "Evaluating and Improving LLM Self-Modeling." arXiv:2608.30980** (2026-08-31).
The authors benchmark whether LLMs can predict their own behaviour, for example whether a prompt edit would change their answer. Models show limited skill, and RL improves it. The gains "do not seem to constitute introspection": better self-prediction need not come from privileged access to internal processing.
*Bears on:* l.646 ("the loop closes over the emitted text, not over a self-model"), and the ISM/ESM distinction. It fits FMT's claim that behavioural self-modelling is not a self-model with privileged access.
**Verdict: MUST-CITE.** It is also the obvious prior art on the term "self-modeling" in the AI literature, and FMT should mark the difference in meaning.

**4. Agarwal, A. — "Do Language Models Know Their Own Constraints?" arXiv:2609.22151** (2026-08-26).
LoRA fine-tuning (SFT or GRPO) makes a Llama-3.1-8B model avoid banned items about 90% of the time, but the model loses the ability to list those constraints when asked. Probes and verbal self-report still recover the avoidance item by item. The failure is specific to enumerating the constraints on request.
*Bears on:* §3.6 (implicit/explicit boundary) and §3.8 (l.534 region). A learned behavioural disposition can be present at the substrate level without being explicitly reportable.
**Verdict: NICE-TO-HAVE.** It is a machine analogy for the IWM/ISM-versus-explicit split.

**5. Khadangi, A. — "We Built a Mirror and Mistook It for a Mind: Causal Liability and the Fallacy of AI Consciousness." arXiv:2609.06715** (2026-09-06).
The paper separates phenomenal consciousness, introspective report and human projection, and names the step from first-person LLM text to a phenomenal bearer the "AI Consciousness Fallacy". It then proposes that "liability closure" (a continuing process inheriting constraints from its own discriminations) is necessary and sufficient for minimal subjecthood, and runs an open-weight causal audit.
*Bears on:* l.646 (the verdict on LLMs), and the self-referential-closure criterion (§3.4.3). Its criterion is a rival closure-based sufficiency condition.
**Verdict: MUST-ANSWER (light).** It is a competing "closure" criterion published in the same month. One sentence in §7.3 would separate FMT's closure (self-model and world-model entering each other's update rule) from liability closure.

## B. Indicator frameworks and cross-substrate testing

**6. van Rooyen, P. — "Testing Two-State Access in Brain and Language Model: Human EEG Reproduction, Simulation Audit, and a Proposed Model Assay." arXiv:2609.22300** (2026-09-14). The HTML version carries the title "The Cross-Substrate Access Assay…".
The paper reproduces the GNW two-state (bimodal) access test on open EEG data from 20 participants, where the predictive advantage is small (~0.003 nat/trial). It then calibrates how the test would transfer to LLM representations and sets out five things any cross-substrate indicator test must declare: predictors, fitting, sampling unit, uncertainty target and decision rule.
*Bears on:* l.640 (Beni 2026 on marker circularity, Bayne et al. 2024 on cross-system tests). It gives concrete methodological support for the argument that markers drift across substrates.
**Verdict: MUST-CITE.** Place it next to Beni (2026) at l.640.

**7. Salvi, R. & Wolfson, O. — "Discovering Machine Correlates of Consciousness." arXiv:2608.28824** (2026-08-28). **Excluded as out of window:** the arXiv record says it appeared in the AGI-2026 proceedings (LNAI 16855, July 2026). It defines "machine correlates" as emotion-modulated hardware anomaly signals in Llama models. Listed here only so nobody re-adds it; it is not relevant to FMT's architecture claims.

**8. Kang, B. & Kim, C.-E. — "AI models as consciousness attributors: how LLMs ascribe consciousness to other agents." *Frontiers in Psychology*. doi:10.3389/fpsyg.2026.1926286** (2026-09-03).
The paper treats LLMs as judges of consciousness in others and compares the attribution patterns of nine models with a human reference.
*Bears on:* nothing central. At most it is loosely relevant to the meta-problem (§3.8).
**Verdict: NICE-TO-HAVE, probably skip.**

## C. Architectures that claim sufficient conditions (rival blueprints)

**9. Grinberg, T., Schleisman, K., Laurent, P., Udrea, B., & Myers, M. — "From S3Q Theory to Implementation: Towards an Architecture for Machine Qualia." arXiv:2609.30743** (2026-09-25).
S3Q requires three jointly necessary conditions for qualia: sensorimotor situatedness, internal simulation via a world model, and structural coherence between predictions and observations. The paper maps these onto a five-layer slot-vector pipeline with falsifiable predictions.
*Bears on:* l.979–989 (§8.7–8.8, "Unique? Yes in the specific form … do not provide a specific architectural blueprint"). S3Q is a simulation-plus-world-model blueprint with an implementation spec, which weakens the "only FMT gives a blueprint" framing. It has no separate self-model and no real/virtual level split.
**Verdict: MUST-ANSWER.** Soften the uniqueness line in §8.7, or add S3Q to §7.3 and state the differences: no self-model, no closure requirement, no Class 4 regime.

**10. Starzyk, J. A. & Galus, W. L. — "From Biological Precursors to Artificial Cognition: Consciousness, Embodiment, and the MEM Architecture." arXiv:2609.23828** (2026-09-20).
The paper argues that LLMs, vision-language-action (VLA) models and humanoid embodiment are not sufficient evidence of phenomenal experience. The Motivated Emotional Mind (MEM) architecture adds interoception, regulatory self-monitoring, affect and re-entry. A phenomenal state is defined as recurrently stabilised modal content coupled to an interoceptive representation of the system's own regulatory state.
*Bears on:* l.642 (Seth-style interoceptive grounding treated as one architecture, not a substrate requirement), and l.646. It is consistent with FMT's verdict on LLMs, but it makes interoceptive self-regulation constitutive.
**Verdict: NICE-TO-HAVE.** It is a further blueprint rival and could sit in §7.3 alongside S3Q.

**11. Lee, S., Oh, Y., An, H., Yoon, H., Friston, K. J., & Hong, S.-J. — "Life-inspired interoceptive artificial intelligence for autonomous and adaptive agents." *Nature Machine Intelligence*. doi:10.1038/s42256-026-01296-8** (online 2026-08-26). The abstract could not be retrieved (paywall); the summary rests on title and authors only.
It appears to be a programme for putting interoceptive, homeostatic regulation into AI agents.
*Bears on:* l.642. If interoception can be engineered, Seth's "beast machine" feature is an architectural property rather than a biological one. That is consistent with FMT's reading, but the paper does not test consciousness.
**Verdict: NICE-TO-HAVE.** Read the full text before citing it.

**12. Lahoz-Beltra, R. — "A Spiking Neural Network Model of Elementary Self-Consciousness via Endogenous Default Mode Network Dynamics." arXiv:2609.29984** (2026-09-24).
A 10k-neuron Izhikevich spiking network with a pacemaker subsystem modelled on the default mode network (DMN) produces a baseline "self" rhythm that interacts with sensory perturbations.
*Bears on:* §8.9 (in-silico programme) in a thin way only. There is no self-model content.
**Verdict: NICE-TO-HAVE / skip.**

## D. Emotions and free will touching self-model accounts

**13. Solms, M., Grimbly, S. J., Bassett, B., Boonstra, E., & Hodson, R. — "Inferring Affective Consciousness in an Artificial Agent: A Case Study." arXiv:2609.03883** (2026-09-03).
A simple agent with an affective system that registers "felt uncertainty" about its needs shows hedonic place-preference behaviour, the standard animal marker for feeling, while being fully deterministic. The authors draw implications for the physical basis of consciousness and for the experience of free will.
*Bears on:* §4.2.2, l.562–580 ("felt freedom is what an origin feels like from inside"; the account is "neutral between" determinism and indeterminism), and §6.4 (animal markers). A deterministic system meets the marker and invites talk of experienced freedom. That is consistent with FMT's decoupling of felt freedom from metaphysical freedom, and it shows how behavioural markers mislead across substrates (l.640).
**Verdict: MUST-CITE.** Solms is a prominent affective-consciousness theorist, reviewers will know the paper, and it lands on both §4.2.2 and §4.4.

**14. Zare, M. — "Functional Emotion Without Character: Large Language Models, Aristotelian Disposition, and the Limits of Behavioral Alignment." arXiv:2609.22362** (v1 2026-07-31; announced September).
It models emotions as attractor regions in representational state space. Interpretability evidence shows that LLMs contain emotion-concept representations the model actually uses in its computation, but not subjective feeling or full affective integration.
*Bears on:* l.358 (qualia as implicit-model echoes; affective character). It fits FMT's distinction between functional representation (implicit level) and phenomenal emotion (explicit level).
**Verdict: NICE-TO-HAVE.**

## E. AI welfare and moral status (theory-committing)

- **Goldstein & Lederman, "AI Death"** (*Philosophical Perspectives*, doi:10.1111/phpe.70017, online 2026-09-08), **Goldstein & Lederman, "What does ChatGPT want?"** (*Inquiry*, doi:10.1080/0020174X.2026.2727584, 2026-09-04) and **Chalmers, "What we talk to when we talk to language models"** (*Inquiry*, doi:10.1080/0020174X.2026.2727582, 2026-09-16). **All three are journal versions of PhilArchive preprints from before the window** (AI Death: 2026-03-11; the other two: 2025). They are out of scope under the rule. **Note for the reference list:** if FMT ever cites the preprints, update them to these versions of record. Chalmers' "virtual entity bound to a conversation thread" view of the LLM interlocutor is directly relevant to the l.646 claim that "knowledge resets between interactions".
- **VanRullen, "AI Consciousness and Existential Risk"** (*J. AI & Consciousness*, doi:10.1142/S2705078526500049, 2026-09-23) is the journal version of an arXiv preprint from November 2025 (arXiv:2511.19115, not re-verified here). Out of window.
- **Nothing new found** in the window from Butlin, Long, Birch, Schwitzgebel or Seth. The Butlin et al. TiCS paper (FMT l.1190) has now appeared in print as vol. 30(7), 2026, so the reference could gain volume and issue numbers. No new Seth biological-naturalism paper appeared in the window.

## F. Empty sub-areas

- **Interpretability of self-representation (new, in window):** nothing found. Anthropic's "A global workspace in language models" (J-space, transformer-circuits.pub) is dated **2026-07-06, outside the window**. It is flagged only because it bears directly on l.646 (it reports functions associated with access consciousness in Claude), and an Eleos commentary exists (Butlin, Shiller, Plunkett, Long). Whether v15 already engages it is a question for the main session.
- **World models in AI tied to consciousness:** nothing beyond S3Q (#9).
- **Free will and self-model, non-AI:** nothing in window beyond Solms (#13). *(Christian List, "Can AI systems have free will?", arXiv:2609.15407, is a re-upload of a 2025 Synthese paper, so it is out of window.)*

## Priority summary

| # | Item | Verdict | FMT locus |
|---|---|---|---|
| 9 | S3Q machine-qualia architecture | MUST-ANSWER | §8.7 "Unique?" l.979ff; §7.3 |
| 5 | Khadangi, liability closure | MUST-ANSWER (light) | §3.4.3; l.646 |
| 1+2 | Šekrst; Maczan (self-report provenance and steering) | MUST-CITE | l.646, l.342 |
| 3 | Zeng et al., LLM self-modeling | MUST-CITE | l.646 |
| 6 | van Rooyen, cross-substrate assay | MUST-CITE | l.640 |
| 13 | Solms et al., affective agent | MUST-CITE | §4.2.2; l.640 |
