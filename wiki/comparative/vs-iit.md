---
title: FMT vs. Integrated Information Theory (IIT)
section: Comparative Analysis
article_number: 55
description: "IIT is mathematically rigorous but its panpsychist commitments and intractable Phi represent structural costs FMT avoids."
keywords: [Integrated Information Theory, IIT, Tononi, Phi, panpsychism, combination problem, consciousness, FMT]
---

# FMT vs. Integrated Information Theory (IIT)

**IIT is FMT's most serious competitor -- mathematically rigorous and philosophically ambitious -- but its panpsychist commitments, the unresolved Combination Problem, and the computational intractability of Phi represent structural costs that FMT avoids entirely.**

Integrated Information Theory (Tononi, 2004; Albantakis et al., 2023) and the [Four-Model Theory](../core-architecture/four-model-theory.md) are the two frameworks in contemporary consciousness science that attempt to address the [Hard Problem](../hard-problem/dissolution.md) head-on rather than bracketing it. This makes their comparison especially instructive: both aim at the same target but arrive via fundamentally different routes.

## IIT's Genuine Strengths

IIT brings three substantial contributions to consciousness science that deserve recognition.

**Mathematical rigor.** IIT is the most mathematically developed consciousness theory. Its axioms, postulates, and the Phi formalism provide a precision that most theories -- including FMT in its current form -- lack. The formal apparatus makes IIT's claims testable in principle, even where computation is infeasible in practice.

**Qualia space.** IIT's treatment of experiential structure through a multidimensional qualia space is arguably its greatest achievement. The idea that the quality of an experience corresponds to the shape of the cause-effect structure captures something deep about why red feels different from blue. FMT's account of experiential structure through the [Explicit World Model](../core-architecture/explicit-world-model.md) is less formally developed.

**The exclusion postulate.** IIT provides a principled answer to the [Boundary Problem](../foundations/eight-requirements.md) through the exclusion postulate: the system with maximum Phi defines the boundary of consciousness. This is elegant, even if computationally unrealizable for biological systems.

## IIT's Structural Problems

Three difficulties are not incidental to IIT but follow necessarily from its core commitments.

**Panpsychism.** IIT's axiom-based identification of consciousness with integrated information (Phi) entails that any system with non-zero Phi has some degree of experience. This includes thermostats, logic gates, and simple feedback circuits. IIT's proponents accept this consequence; most neuroscientists find it a reductio ad absurdum. FMT avoids panpsychism entirely through [weak emergence](../philosophical/weak-emergence.md): consciousness arises at a specific computational level when both the [architectural threshold](../physical-foundations/two-thresholds.md) (four models) and [computational threshold](../physical-foundations/criticality.md) (the open-ended Class 4 regime, whose neural signature is near-criticality) are met.

**The Combination Problem.** If fundamental entities have micro-experience, how do these micro-experiences combine into the macro-experience of a human mind? This is not a gap in IIT's development -- it is a structural consequence of panpsychism itself ([Chalmers, 2016](https://consc.net/papers/combination.pdf)). FMT has no Combination Problem because consciousness does not emerge from the combination of proto-conscious elements. It emerges weakly from a substrate that is itself non-conscious, just as a spreadsheet sum emerges from transistors that contain no sum.

**Phi is computationally intractable.** Calculating Phi for a realistic neural system is not merely difficult but computationally intractable (Aaronson, 2014). This means IIT's predictions are often untestable in practice. FMT's predictions -- psychedelics alleviating anosognosia, controllable ego dissolution content, DID alter-switch neural signatures, lucid dream onset as criticality crossing -- require no intractable computation.

## The Divergence Point

FMT adopts IIT's central diagnosis: consciousness is irreducible, integrated, and causally structured, not mere information processing. The divergence lies in what that irreducible structure is and where each theory locates phenomenality. IIT identifies consciousness with intrinsic causal power: a system is conscious to the degree that it has Phi. FMT identifies consciousness with a specific *process* -- ongoing self-simulation across four model kinds in the Class 4 regime. For IIT, consciousness is everywhere Phi is non-zero. For FMT, consciousness is nowhere without the four-model architecture and that regime, regardless of how much information is integrated.

The **unfolding argument** ([Doerig et al., 2019](https://doi.org/10.1016/j.concog.2019.04.002)) holds that any recurrent network can be unfolded into a feedforward network with identical input-output mappings. Its target is any theory on which two systems agreeing in all input-output behavior can differ in consciousness -- IIT, whose feedforward twin has zero Phi, and FMT alike, since self-referential closure is a property of the architecture rather than of the mapping. FMT's reply is that unfolding externalizes the loop: no stage of the unfolded chain models the stages that follow it, so closure is gone. And the two systems agree only in the limit of unbounded resources. Unfolding trades a reused loop for replicated stages; in the theory's model-system results on one connectome family, freedom from any closed path costs 71.5-74.0% of the connectome, against 12.0-14.0% for merely relocating closure. Where a resource bound applies, the unfolded chain and the closed one stop agreeing on behavior. On an unbounded substrate the theory has no experiment to offer.

## Figure

```mermaid
graph TB
    subgraph IIT_PATH["IIT's Route"]
        direction TB
        I1["Axioms<br/>(intrinsic existence, composition,<br/>information, integration, exclusion)"]
        I2["Phi (Φ)<br/>integrated information"]
        I3["Consciousness =<br/>non-zero Φ"]
        I4["Panpsychism +<br/>Combination Problem"]
        I1 --> I2 --> I3 --> I4
    end

    subgraph FMT_PATH["FMT's Route"]
        direction TB
        F1["Self-Simulation<br/>(four-model architecture)"]
        F2["Class 4 regime<br/>(near-criticality is<br/>its neural signature)"]
        F3["Virtual Qualia<br/>(computational-level properties)"]
        F4["Weak Emergence<br/>no Combination Problem"]
        F1 --> F3
        F2 --> F3
        F3 --> F4
    end

    HP["Hard Problem"] --- I3
    HP --- F3

    style IIT_PATH fill:#1a1a2e,stroke:#a4243b,color:#fff
    style FMT_PATH fill:#1a1a2e,stroke:#2d6a4f,color:#fff
    style I4 fill:#6a1b2a,stroke:#a4243b,color:#fff
    style F4 fill:#2d6a4f,stroke:#40916c,color:#fff
    style HP fill:#2d1b69,stroke:#9b59b6,color:#fff
```

*Both theories engage the Hard Problem, through fundamentally different routes. IIT's path leads through panpsychism to the Combination Problem. FMT's path through virtual qualia arrives at weak emergence with no Combination Problem.*

## Key Takeaway

IIT and FMT are the field's two most philosophically ambitious theories. IIT pays for its mathematical elegance with panpsychism, the Combination Problem, and computational intractability. FMT pays for its architectural specificity with limited formal mathematical development -- a gap, not a structural flaw, since formalization can follow.

## See Also

- [Comparative Scoreboard](scoreboard.md)
- [Virtual Qualia](../hard-problem/virtual-qualia.md)
- [The Boundary Problem](../foundations/eight-requirements.md)
- [Weak Emergence](../philosophical/weak-emergence.md)
- [Two Thresholds for Consciousness](../physical-foundations/two-thresholds.md)

---

Based on: Gruber, M. (2026). The Four-Model Theory of Consciousness. Zenodo. https://doi.org/10.5281/zenodo.18669891
