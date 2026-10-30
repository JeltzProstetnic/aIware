---
title: "What the Loop Carries: A Comment on Zheng et al. (2026)"
date: 2026-10-19
draft: false
description: "A comment on Zheng et al.'s recurrency framework, proposing that recurrent loops matter for consciousness when they carry a self-model whose output changes the system's next state."
tags: ["consciousness", "recurrency", "FMT", "commentary", "self-model"]
slug: "what-the-loop-carries"
---

In ["Loops all the way up"](https://doi.org/10.1016/j.plrev.2026.07.006) (*Physics of Life Reviews*, 2026), Zheng et al. propose that recurrency, activity that loops back into the circuit that produced it, is the implementation-level feature the major theories of consciousness share. They map four nested levels of it (cellular, local inter-areal, global, lateral) onto conscious state, phenomenal content, access and phenomenal character. My comment on it, with full references, is a preprint on Zenodo: [What the loop carries](https://doi.org/10.5281/zenodo.23478413).

The review also states what it leaves open. Its conclusion offers depth of causal closure as "a conceptual discriminator rather than an operational one", and adds: "Specifying where along this continuum causal closure becomes sufficient, and by which measure, is a question that the present framework poses rather than answers."

The [Four-Model Theory](/blog/four-model-theory-introduction/) (FMT) has a candidate answer. Recurrency becomes relevant to consciousness when the loop re-conditions a model of the world that contains a model of the system itself, and the self-model's output changes the system's next state. Most of the reasons for it are in the review's own text.

## Depth, or content?

The glossary defines depth of causal closure as "the degree to which the successive states of a system are determined by its own current and preceding states relative to exogenous drive". The conclusion excludes several loops as shallow, among them "reflex arcs or spinal central-pattern generators". A central pattern generator is a small circuit, for instance in the spinal cord, that produces rhythmic motor output. The reason given is that in such loops "states remain largely determined by immediate sensory input, with neither the capacity to sustain internally-generated perceptual hypotheses against ambiguous evidence, nor to maintain representations decoupled from the present stimulus."

Pattern generators do not fit the first half of that sentence. They produce their rhythms "in the absence of sensory or descending inputs that carry specific timing information" (Marder & Bucher, 2001). In an isolated preparation under tonic drive, the timing of each next state comes from the circuit's own trajectory, which is deep closure by the glossary's measure. What excludes the generator is the second half: it sustains no perceptual hypothesis and represents nothing.

One of the formalisations the glossary names draws the same line. Non-trivial information closure (Chang et al., 2020) counts closure only when the system's own dynamics carry information about the environment's dynamics. An isolated generator scores zero, because the measure asks whether the closed loop encodes the environment. That is a question about modelling.

The top of the scale reads the same way. The thresholds named for the global level are "working memory, flexible rule-switching, and offline simulation", which describe what a loop computes. The authors set computation aside on purpose ("What differs across theories is the computation performed by recurrent architectures"), yet the criterion meant to say which recurrence counts is stated in terms of it. So my question to them is a plain one: in the conclusion's criterion, does the depth measure do the work, or does the content of the loop?

If the content does, the criterion has to say which content. A world-model alone does not meet FMT's condition; a weather simulation models a world and has no perspective from which it encounters itself. FMT adds a self-model inside the world-model, whose output enters the system's next update. I offer this as a candidate answer to the question the review poses. Like the review, it does not claim to bridge the explanatory gap.

## The unfolding argument

The unfolding argument (Doerig et al., 2019) holds that any recurrent network can be unrolled into a feedforward one with the same input-output behaviour. The review accepts that "a feedforward system can replicate the input-output function of any recurrent system" and answers with cost: an unfolded network "would face prohibitive constraints in weight, size, processing time, and energy consumption". FMT gives the same answer, as a claim about cost under a bounded budget, and does not claim that recurrence computes anything a feedforward system cannot compute in principle.

One sentence in the same paragraph departs from the accepted premise: "Recurrent Neural Networks (RNNs), while powerful in solving problems their unfolded cousins cannot, are hindered by computational issues like vanishing/exploding gradients". Read as a claim about which functions each class can compute, it contradicts the premise, and the work cited for it (Bengio et al., 1994) concerns how hard such networks are to train.

Two readings repair it. "Cannot" can mean cannot within a physical budget, which is the authors' own cost argument. Or it can refer to closed-loop operation over an open-ended horizon: Basri et al. (2026) argue that the approximation theorems guarantee a feedforward match only on compact domains, so they do not cover a system whose output depends on an unbounded input history. Either rewrite makes the section consistent with its own premise.

## Self-modelling as its own dimension

The review grounds the "I" in brain-body loops such as heartbeat-evoked responses. The work it draws on (Park & Tallon-Baudry, 2014; Babo-Rebelo et al., 2016) supports a narrower reading: the visceral loop supplies input that a self-representation uses.

Nothing in the four levels requires a system to represent itself. I would treat self-modelling as a dimension that cuts across the four levels: at any level, the returning activity may or may not carry a model of the system that generates it. FMT distinguishes two scopes of model, the world and the system itself, each in an implicit and an explicit mode, which gives four model kinds, and locates self-referential closure where the self-model and the world-model each enter the other's update. These are kinds of model in one substrate, none of them corresponding to a level of recurrency.

The review's own methods can examine this. A contrast could hold closure depth fixed and vary only whether a self-model's output is written back into the system's next state. A depth-only criterion classifies the two systems alike; the self-model criterion does not. Which classification the perturbational and counterfactual signatures track is then an empirical question.

## Two disagreements

The review states that current AI systems "lack physical recurrency, as they are operated on von Neumann architectures, which are inherently feed-forward systems", and that large language models "merely simulate recurrence as part of their computations without embodying it in their hardware structure". On that standard, any recurrent network on a digital computer only simulates recurrence.

FMT disagrees. It takes the relevant feedback to be the one the system runs on its own states, and counts a mapping as an implementation only if that feedback makes a counterfactual difference to what the system does next (Chalmers, 1996). A recurrent network executed on clocked hardware meets that condition at the level of its state variables.

A von Neumann machine is feedforward only within a clock cycle; across cycles, each machine state is computed from the previous one and held in latches, which are themselves feedback circuits. By the glossary's definition, that is recurrency. Which loops does the review count? And the review elsewhere classifies artificial systems by perturbational and counterfactual tests, which a simulated recurrent network can pass or fail. Where the hardware criterion and the tests disagree, which governs? If the hardware does, the framework rules out FMT's position that a simulated closed architecture can be an implementation, and for a system that passes the perturbational tests neither account at present has an experiment that would decide between the two readings.

The second disagreement concerns dynamics. The review says conscious states depend on "the dynamical regimes that these recurrent circuits support, rather than on recurrency alone", and does not specify the regimes. Criticality plays no part in the framework, and its predictions do without it. FMT agrees that they can. It characterises the regime by what it does, open-ended modelling, and treats near-critical dynamics (reviewed with their open controversies by Wilting & Priesemann, 2019) as a signature some brains show while doing it. It does not treat criticality as a condition for consciousness, so criticality data cannot decide between the two accounts in either direction.

## The proposal

The review's own wording of the depth thresholds, and the formalisation its glossary names, already answer partly in terms of what the loop represents. The criterion I propose makes that explicit and adds one condition: the loop carries a self-model whose output changes the system's next state. The perturbational and counterfactual tests Zheng et al. specify are the means of checking it.

The full comment, with references: [https://doi.org/10.5281/zenodo.23478413](https://doi.org/10.5281/zenodo.23478413).
