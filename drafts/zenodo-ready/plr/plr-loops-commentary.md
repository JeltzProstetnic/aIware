# What the loop carries: Comment on "Loops all the way up: Recurrency as an implementation-first primitive for consciousness" by Zefan Zheng et al.

**Matthias Gruber**\
Independent researcher · ORCID 0009-0005-9697-1665 · research@matthiasgruber.com

2026-10-19 · Preprint, version 2

**Keywords:** recurrency; causal closure; self-model; unfolding argument; artificial consciousness

---

Zheng et al. (2026) propose recurrency as the implementation-level feature that the major theories of consciousness share, and map four nested levels of it (cellular, local inter-areal, global, lateral) onto conscious state, phenomenal content, access and phenomenal character. They also state what the synthesis leaves open. Their conclusion offers depth of causal closure as "a conceptual discriminator rather than an operational one" and adds: "Specifying where along this continuum causal closure becomes sufficient, and by which measure, is a question that the present framework poses rather than answers."

The Four-Model Theory (FMT; Gruber, 2026) offers one candidate answer: recurrency becomes consciousness-relevant when the loop re-conditions a model of the world that contains a model of the system itself, and the self-model's output changes the system's next state. The reasons for it can be found in the target article's own text.

## 1. The depth criterion turns on what the loop does

The glossary defines depth of causal closure as "the degree to which the successive states of a system are determined by its own current and preceding states relative to exogenous drive". The conclusion then excludes spinal arcs, basal-ganglia loops and "reflex arcs or spinal central-pattern generators". Their loops count as shallow because "activity returns to the circuit without iteratively re-conditioning the originating population, and states remain largely determined by immediate sensory input, with neither the capacity to sustain internally-generated perceptual hypotheses against ambiguous evidence, nor to maintain representations decoupled from the present stimulus."

Central pattern generators do not fit the glossary measure. They produce rhythmic motor patterns "in the absence of sensory or descending inputs that carry specific timing information" (Marder & Bucher, 2001). In an isolated preparation under tonic drive, the timing of each next state is set by the circuit's own trajectory, which is deep closure as the glossary defines it. What excludes the generator is the second half of the quoted sentence: it sustains no perceptual hypothesis and holds no representation of anything.

One of the two formalisations the glossary names draws the same line. Non-trivial information closure treats closure as trivial when system and environment are independent, and counts it only when the system's own dynamics carry information about the environment's dynamics (Chang et al., 2020). An isolated generator scores zero on it. That measure excludes the generator by asking whether the closed dynamics encode the environment, which is a question about modelling.

The same holds at the top of the scale. The thresholds named for the global level are "working memory, flexible rule-switching, and offline simulation", which describe what the loop computes. The authors set computation aside on purpose ("What differs across theories is the computation performed by recurrent architectures", §3.2), yet the discriminator meant to say which recurrence counts is stated in terms of it. Hence a plain question to the authors: in the conclusion's criterion, does the depth measure do the work, or does the content of the loop?

If the content does, the criterion has to say which content. A world-model alone does not meet FMT's condition. FMT's standard example is a weather simulation, which models a world and has no perspective from which it encounters itself (Gruber, 2026, §3.4.3). The proposed criterion adds one condition: a self-model inside the world-model, whose output enters the system's next update. It is offered as a candidate answer to the question the conclusion poses. Like the target article, it does not claim to bridge the explanatory gap.

## 2. A repair to the reply to the unfolding argument

Section 3.3.2 accepts the second premise of the unfolding argument (Doerig et al., 2019), that "a feedforward system can replicate the input-output function of any recurrent system", and answers with cost: an unfolded network "would face prohibitive constraints in weight, size, processing time, and energy consumption". It adds a second answer, that an unfolded network "would also have different reactions to interventions, dynamic stimuli or neural feedback loops", and that equivalence is "even less clear if output of the network acts on the stimulus itself." Both answers hold. FMT gives the first in the same form, as a claim about cost under a bounded budget, and does not claim that recurrence computes anything a feedforward system cannot compute in principle (Gruber, 2026, §7.2).

One sentence in the same paragraph departs from the premise just accepted: "Recurrent Neural Networks (RNNs), while powerful in solving problems their unfolded cousins cannot, are hindered by computational issues like vanishing/exploding gradients". Read as a claim about which functions each class can compute, it contradicts premise 2, and the work cited for it (Bengio et al., 1994) concerns how hard such networks are to train, not what they can compute.

Two readings rescue the sentence. On the first, "cannot" means cannot within a physical budget, which is the authors' own cost argument. On the second, it refers to closed-loop operation over an open-ended horizon. Basri et al. (2026) argue that the approximation theorems guarantee a feedforward match only on compact domains, so they do not cover a system whose output depends on an unbounded input history. Rewriting the sentence in either form makes the section consistent with its own premise. Rapid plasticity has been argued to break the functional equivalence on separate grounds (O'Reilly-Shah et al., 2026), and either rewrite could cite it as an independent reason.

## 3. Self-modelling as a dimension across the four levels

Box 3 grounds the "I" in brain-body loops: heartbeat-evoked responses and vagal, gut and respiratory traffic. The work it draws on supports a narrower reading. Bodily signals have been proposed as the frame for a first-person perspective (Park & Tallon-Baudry, 2014), and heartbeat-evoked responses in the default network covary with how self-related a spontaneous thought is, along separate "I" and "Me" dimensions (Babo-Rebelo et al., 2016). On that evidence the visceral loop supplies input that a self-representation uses. There is also a reason the body comes first. For a recurrent network coupled to a body, that body is the most persistent, most controllable and most informative regularity in its input, so the first stable attractor such a network forms is expected to model it. Early nervous systems fit this order: nerve nets of the cnidarian kind coordinated a body without representing it (Keijzer et al., 2013), and the first representations brains formed would then have been of the body they coordinated. Nothing in Box 3 or in the four levels requires the system to represent itself. Self-directed modelling appears in Table 1 as two of nine entries, the self-organising meta-representational theory (Cleeremans et al., 2020) and attention schema theory (Graziano & Webb, 2015).

Self-modelling could instead be treated as a dimension that cuts across the four levels: at any level, the returning activity may or may not carry a model of the system that generates it. FMT distinguishes two scopes of model, the world and the system itself, each in an implicit and an explicit mode, which gives four model kinds, and locates self-referential closure where the self-model and the world-model each enter the other's update (Gruber, 2026). These are kinds of model in one substrate, not separate modules, and none of them corresponds to one of the four levels of recurrency.

The dimension can be examined with the methods of Table 2. Its "Artificial systems" row compares recurrently closed systems with feedforward ones. A further contrast would hold closure depth fixed and vary only whether a self-model's output is written back into the system's next state. A depth-only criterion classifies the two systems alike; the proposed criterion does not. Which classification the perturbational and counterfactual signatures of Table 2 track is then an empirical question.

## 4. Two points of disagreement

Box 4 states that current AI systems "lack physical recurrency, as they are operated on von Neumann architectures, which are inherently feed-forward systems", and that large language models "merely simulate recurrence as part of their computations without embodying it in their hardware structure", citing Aru et al. (2023) among others. On that standard any recurrent network run on a digital computer only simulates recurrence, whatever it computes. FMT disagrees. It takes the relevant feedback to be the one the system runs on its own states, and counts a mapping as an implementation only if that feedback makes a counterfactual difference to what the system does next (Chalmers, 1996; Gruber, 2026, §7.2). A recurrent network executed on clocked hardware meets that condition at the level of its state variables.

Two questions follow. First, a von Neumann machine is feedforward only within a clock cycle. Across cycles each machine state is computed from the previous one and held in latches, which are themselves feedback circuits, and by the glossary's definition that is recurrency. Which loops does Box 4 count? Second, Section 3.4.4 and the "Artificial systems" row of Table 2 classify artificial systems by perturbational and counterfactual tests, and a simulated recurrent network can pass or fail those tests. Where Box 4 and Table 2 disagree about a system, which governs? The framework's "recurrency-constrained multiple realisability" points to the test, Box 4 to the hardware. If the hardware criterion governs, the framework rules out FMT's position that a simulated closed architecture can be an implementation, and for a system that passes the perturbational tests neither account at present has an experiment that would decide between the two readings.

The same box says that the emergence of conscious states depends on "the dynamical regimes that these recurrent circuits support, rather than on recurrency alone", and does not specify the regimes. Criticality plays no part anywhere in the framework, and the predictions of Table 2 do without it. FMT agrees that they can. It characterises the regime by what it does, open-ended modelling, and treats near-critical dynamics, whose evidence and open controversies Wilting and Priesemann (2019) review, as a signature some brains show while doing it, not as a condition for consciousness. Criticality data therefore cannot decide between the two accounts in either direction.

## 5. Conclusion

The conclusion of the target article asks which closure counts and by which measure. Its own wording of the depth thresholds, and the formalisation its glossary names, already answer partly in terms of what the loop represents. The criterion proposed here makes that explicit and adds one condition: the loop carries a self-model whose output changes the system's next state. The perturbational and counterfactual tests the authors specify in Table 2 are the means of checking it.

---

**AI-use statement.** Drafting of this comment was assisted by Claude (Anthropic). The author is responsible for all content and claims.

## References

Aru, J., Larkum, M. E., & Shine, J. M. (2023). The feasibility of artificial consciousness through the lens of neuroscience. *Trends in Neurosciences*, 46(12), 1008–1017. https://doi.org/10.1016/j.tins.2023.09.009

Babo-Rebelo, M., Richter, C. G., & Tallon-Baudry, C. (2016). Neural responses to heartbeats in the default network encode the self in spontaneous thoughts. *Journal of Neuroscience*, 36(30), 7829–7840. https://doi.org/10.1523/JNEUROSCI.0262-16.2016

Basri, J., BarAvi, P., & Hemmo, M. (2026). Functionalist theories of consciousness: Unfolding, substitution and the indeterminacy of function by the physics of the brain. *Consciousness and Cognition*, 145, 104121. https://doi.org/10.1016/j.concog.2026.104121

Bengio, Y., Simard, P., & Frasconi, P. (1994). Learning long-term dependencies with gradient descent is difficult. *IEEE Transactions on Neural Networks*, 5(2), 157–166. https://doi.org/10.1109/72.279181

Chalmers, D. J. (1996). Does a rock implement every finite-state automaton? *Synthese*, 108(3), 309–333. https://doi.org/10.1007/BF00413692

Chang, A. Y. C., Biehl, M., Yu, Y., & Kanai, R. (2020). Information closure theory of consciousness. *Frontiers in Psychology*, 11, 1504. https://doi.org/10.3389/fpsyg.2020.01504

Cleeremans, A., Achoui, D., Beauny, A., Keuninckx, L., Martin, J.-R., Muñoz-Moldes, S., Vuillaume, L., & de Heering, A. (2020). Learning to be conscious. *Trends in Cognitive Sciences*, 24(2), 112–123. https://doi.org/10.1016/j.tics.2019.11.011

Doerig, A., Schurger, A., Hess, K., & Herzog, M. H. (2019). The unfolding argument: Why IIT and other causal structure theories cannot explain consciousness. *Consciousness and Cognition*, 72, 49–59. https://doi.org/10.1016/j.concog.2019.04.002

Graziano, M. S. A., & Webb, T. W. (2015). The attention schema theory: A mechanistic account of subjective awareness. *Frontiers in Psychology*, 6, 500. https://doi.org/10.3389/fpsyg.2015.00500

Gruber, M. (2026). The Four-Model Theory of Consciousness: A simulation-based framework unifying the hard problem, binding, and altered states. *Zenodo* preprint. https://doi.org/10.5281/zenodo.18669891

Keijzer, F., van Duijn, M., & Lyon, P. (2013). What nervous systems do: Early evolution, input–output, and the skin brain thesis. *Adaptive Behavior*, 21(2), 67–85. https://doi.org/10.1177/1059712312465330

Marder, E., & Bucher, D. (2001). Central pattern generators and the control of rhythmic movements. *Current Biology*, 11(23), R986–R996. https://doi.org/10.1016/S0960-9822(01)00581-4

O'Reilly-Shah, V. N., Selvitella, A. M., & Schurger, A. (2026). A caveat regarding the unfolding argument: Implications of plasticity. *Neuroscience of Consciousness*, 2026(1), niag027. https://doi.org/10.1093/nc/niag027

Park, H.-D., & Tallon-Baudry, C. (2014). The neural subjective frame: From bodily signals to perceptual consciousness. *Philosophical Transactions of the Royal Society B*, 369(1641), 20130208. https://doi.org/10.1098/rstb.2013.0208

Wilting, J., & Priesemann, V. (2019). 25 years of criticality in neuroscience — established results, open controversies, novel concepts. *Current Opinion in Neurobiology*, 58, 105–111. https://doi.org/10.1016/j.conb.2019.08.002

Zheng, Z., Chis-Ciure, R., Waade, P. T., Eiserbeck, A., Aru, J., Andrillon, T., Jarraya, B., Melloni, L., Northoff, G., Rosas, F. E., & Dwarakanath, A. (2026). Loops all the way up: Recurrency as an implementation-first primitive for consciousness. *Physics of Life Reviews*, 58, 360–381. https://doi.org/10.1016/j.plrev.2026.07.006
