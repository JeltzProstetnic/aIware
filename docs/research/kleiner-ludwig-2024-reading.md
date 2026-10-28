# Kleiner & Ludwig (2024) no-go theorem, and the qualia-structure reification question

Research note, 2026-10-23. Sources were read in full from primary text: the Europe PMC full-text XML of PMC11671748, Kleiner's Substack via its API, and Sampson's Substack. Quotes are verbatim.

## 1. Bibliographic check (VERIFIED via Crossref + Europe PMC)

Kleiner, J. & Ludwig, T. (2024). "The case for neurons: a no-go theorem for consciousness on a chip." *Neuroscience of Consciousness*, 2024(1), niae037. doi:10.1093/nc/niae037. Open access (CC BY), PMC11671748, published online 26 Dec 2024. The arXiv precursor has a different title: arXiv:2304.05077, "If consciousness is dynamically relevant, artificial intelligence isn't conscious". The OUP site serves the article under two article IDs (/7774373 and /7933504), and Kleiner's post links to /7933504. I did not check whether that is a version change.

## (a) Premises and conclusion

**Informal argument (Introduction):** (A1) "Verification of processing units ensures that any dynamical effects that change the computational dynamics of a processing unit are precluded or suppressed." (A2) "If consciousness is dynamically relevant, and AI systems are conscious, then there are dynamical effects that change the computational dynamics of an AI system." (A3) "AI systems run on processing units." (C) "If consciousness is dynamically relevant, AI systems cannot be conscious."

**Formal setup ("Formal preliminaries", "Dynamical relevance"):**
- Υ is the class of "reference theories" (neuroscience, chemistry, computer science, physics).
- T_F is a "fundamental reference theory" with T_F < T for every T in Υ, read "for all practical purposes" as quantum theory.
- k* is the real dynamics.
- M* is the "true" theory of consciousness, with k_{M*}|_{T_R} = k*|_{T_R}.
- **Definition 1:** "Consciousness is dynamically relevant according to M with respect to T_R iff S is conscious in k_M ⇒ k_M|_{T_R} ≠ k_{T_R}." This must hold "for all dynamical trajectories k_M of M". Gloss: "if S is conscious according to a ToC M, then the dynamical evolution as specified by M differs from the dynamical evolution as specified by the underlying neuroscientific theory alone."
- **Definition 2:** "Consciousness is dynamically relevant (CDR) only if it is dynamically relevant according to the 'true' ToC M* with respect to some reference theory T_R ∈ Υ." Formally this is stated as "only if", but it is used as the definition. Only *some* T_R is needed.
- **Verification premises ("Functional and postsilicon verification"):** Eq. (1), functional verification: k_{T_F}|_{T_comp} = k_{T_comp}. Eq. (2), postsilicon verification: k*|_{T_comp} = k_{T_comp}. T_comp is "Gödel–Church–Turing computation", specified by the Instruction Set Architecture (ISA).
- **Definition 3:** an AI system is conscious only if there is at least one k_{T_comp} in which it is conscious. AI consciousness is thus "determined by facts on the computational level and above".
- **Lemma 5:** "Dynamical relevance passes downward."
- **Theorem 4:** "If consciousness is dynamically relevant, then AI systems are not conscious."

**What is excluded:** systems running on "CPUs, GPUs, TPUs, or other processors that 'have been designed and verified in the lab'", whatever the architecture: "What sets AI systems apart … is not the specific computational architecture … architectures that closely resemble the mammalian brain's computational structure can arguably also be used". The paper treats the following as open or partial loopholes ("Objections"):
- imperfect verification (judged unlikely to suffice, because deviations are random);
- verified probabilistic processing, where consciousness "may determine how the probability distributions … are sampled, but it cannot change them";
- quantum computing, if consciousness is tied to measurement.

The theorem does not exclude determinism as such: "Our result is fully compatible with deterministic systems." What blocks consciousness is being "'locked into' a formal system".

**What the theorem assumes about theories:** nothing beyond dynamical relevance (DR). The authors do not establish DR. They argue for it ("Is dynamical relevance plausibly true?") on the ground that measures of consciousness need it: "consciousness must make a difference to the data".

## (b) Who escapes, and where a self-modelling functionalist theory sits

- **Substrate-dependent views** (biological naturalism) escape by scope, not by denying DR. The paper says "our result presumes verification … substrate-dependent views of consciousness target biological substrates, where no process akin to verification exists." Separately, such views "do not imply dynamical relevance" because "enabling condition" and "grounding" relations "are not included in the definition".
- **Theories whose mathematics adds no dynamics** escape because DR is false for them. The example is IIT's formalism ("Current theories"): "according to IIT's mathematics, consciousness is not dynamically relevant … No change whatsoever is introduced to these dynamics". The authors read IIT's *metaphysics* and GNW as implying DR. Their GNW reasoning is that having a workspace "makes a difference to a system's information processing architecture and, a fortiori, to the system's dynamics."
- **Functionalism, computationalism, self-model or process theories:** the paper never discusses these by name. Its only related statement is that a ToC positing "a specific cognitive function that would be absent if systems did not possess consciousness" is DR ("Dynamical relevance of consciousness"). Kleiner's Substack draws the decisive line:
  - "a supervenience theory postulates consciousness as dynamically irrelevant to a theory of the supervenience base";
  - DR applies when "a theory of consciousness postulates … a brain function that neuroscience doesn't know."
- **My inference (not stated by the authors):** take a substrate-neutral theory on which consciousness *is* a self-modelling process that is fully specified in the system's own computational description and adds no dynamics beyond it. Such a theory is DR-irrelevant with respect to that description, so it falls *outside* the theorem's antecedent, and AI consciousness stays open under it. Two caveats:
  - Definition 2 needs DR with respect to only *some* reference theory. The theory must therefore deny that conscious trajectories deviate from *any* correct reference description, not only from the computational one.
  - On the authors' own framing, denying DR has a price: they argue that measurement relies on DR. Kleiner's Substack partly softens this. Conscious and unconscious systems still evolve differently under supervenience theories ("there is a difference … simply because the activity of the brain function makes a difference").
- **Related preprint:** Mallavarapu, A. & Percy, C. (2026), "A No-Go Theorem for Process Theories of Consciousness", PsyArXiv, doi:10.31234/osf.io/w3n6v_v1, posted 10 Aug 2026. It argues that theories identifying consciousness with temporally extended processes (it names "global broadcasting, recurrent processing, predictive updating, computation") conflict with local determinism plus difference-making, so "consciousness must therefore be attributed to a system's present state." It targets process theories directly. I read only the Crossref abstract: full text UNREAD, not peer-reviewed.

## (c) Kleiner's Substack clarification

Johannes Kleiner, "On our No-Go Theorem for AI Consciousness," 3 Mar 2025, https://johanneskleiner.substack.com/p/on-our-no-go-theorem-for-ai-consciousness. This is the only substantive post. The only other post is a "Coming soon" placeholder dated 26 Feb 2025. It replies to Justin T. Sampson, "Go or No Go," 3 Feb 2025, https://sampsonetics.substack.com/p/go-or-no-go, which Sampson later revised, saying he had "unintentionally oversimplified" the paper.

What the post adds:
1. **DR is compatible with causal closure.** "consciousness can be physical and also dynamically relevant." The simplest example is "a brain function that neuroscience doesn't know." The post offers an informal definition: DR holds "iff the theory of consciousness changes the dynamics of some reference theory in the natural sciences when systems are conscious."
2. **DR is not the conscious-versus-unconscious contrast.** "it is *always* the case that conscious systems evolve differently than unconscious systems, independently of what consciousness is taken to be". This is why a reference theory is needed, and why supervenience theories come out DR-irrelevant.
3. **The simulation question.** If consciousness is DR with respect to a neuroscientific theory, a faithful GPU simulation of that theory is not conscious, by contraposition. Footnote 6 extends this via Lemma 5: any program "is always dynamically reducible to the machine code".
4. **The theorem is "a first step, not a final answer."** Sampson's later term "dynamical involvement" is welcomed for DR-irrelevance with respect to physics.

## (d) Reification worry for qualia structures

**Result: no paper found that states the worry in the requested form.** By that form I mean: report-derived structure as a property of the method or of pooled between-subject data rather than of an individual's experience, put in terms of the g-factor or ergodicity critique (Borsboom, Molenaar).

Nearest material, all VERIFIED via Crossref/OpenAlex/full text:
- **Kawakita, Zeleznikow-Johnston, Takeda, Tsuchiya & Oizumi (2025)**, *iScience* 28(3), 112029, doi:10.1016/j.isci.2025.112029. They aggregate across participants ("to estimate a group-level color similarity structure") because each participant gave "only 162 at most" pairs, and state: "we did not address the problem of one-to-one alignment at the individual level". They estimate that over 4,000 trials per person would be needed. This is a sample-size limitation, not a reification argument.
- **Togashi, Yotsumoto, Hiramatsu, Tsuchiya & Oizumi (2026)**, bioRxiv, doi:10.64898/2026.02.13.705699 (preprint). This is the empirical follow-up: 4,371 ratings × 11 individuals, aligned individual to individual. Some participants with normal FM-100 scores "failed to align with either cluster", showing "idiosyncratic structures". This partly answers the pooling worry empirically, but does not frame it as reification.
- **Kob (2023)**, *Neurosci Conscious* niad011, doi:10.1093/nc/niad011. Raises method worries: Tversky's context-dependence of similarity, and that subjects may "misintrospect their own phenomenal metrics". It does not raise pooling.
- **Isaac (2025)**, *Phil Mind Sci* 6, doi:10.33735/phimisci.2025.11773. Its abstract says the method succeeds "by rendering structural relations … behaviorally manifest … exposing them to intersubjective comparisons". This is relevant, but I could read only the abstract (the full text sits behind a bot wall), so how fully it treats the worry is UNVERIFIED.
- **No hits on these questions:** Lyre (2022, doi:10.1093/nc/niac012); Kleiner & Ludwig (2024, *Synthese* 203:89, doi:10.1007/s11229-024-04503-4; full text grepped for average/population/artefact, none found); Fink, Kob & Lyre (2021, doi:10.33735/phimisci.2021.79). Kleiner (2024, *Conscious Cogn* 119:103653, doi:10.1016/j.concog.2024.103653) is paywalled and was not read: UNVERIFIED.

**Searched:** Crossref, OpenAlex, Europe PMC full texts, and web searches for qualia structure / quality space combined with pooled, group-level, individual, measurement artefact, ergodicity, Molenaar, Borsboom, reification.
