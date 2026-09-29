---
title: The Cortical Automaton
section: Physical Foundations
article_number: 23
description: "The cortex realizes the discrete, locally-updating dynamics of a cellular automaton; cortical columns as cells are one natural granularity among several."
keywords: [cortical automaton, cellular automaton, cortical columns, Wolfram, six layers, neural dynamics, criticality, state space]
---

# The Cortical Automaton

**The spatiotemporal firing pattern across the cortex realizes the discrete, locally-updating dynamics that cellular-automaton theory characterizes, operating in a many-thousand-dimensional space.**

The [free-compute requirement](../physical-foundations/criticality.md) — the demand that a conscious substrate actually deploy Class-4 computation on self-modeling — has a concrete physical interpretation in the biological brain. The spatiotemporal activation state of billions of cortical neurons forms a discrete dynamical system -- a cellular automaton -- in which the state evolves according to local rules applied across a high-dimensional lattice ([Gruber, 2015](https://www.amazon.com/Emergenz-Bewusstseins-German-Matthias-Gruber/dp/1326652079)). Which unit counts as the "cell" -- a single neuron, a minicolumn, a cortical column, or a Brodmann area -- is under-determined: each coarser level inherits the discrete, locally-updating character of the level below. The theory's commitment is that *at some scale of coarse-graining* the cortex operates in the Class 4 regime; the cortical column, with the six-layer architecture and lateral connectivity as transition rules, is one natural granularity, and the argument does not depend on it. That Class 4 dynamics are exactly preserved under coarse-graining is a conjecture, not a theorem.

## Columns as Cells, Layers as Rules

A classical cellular automaton consists of cells arranged on a grid, each updating its state based on the states of its neighbors according to fixed rules. At column granularity, the cortex implements this architecture at a biological scale. The approximately 150,000 cortical columns of the human neocortex serve as the cells. Each column is a vertical unit spanning six cytoarchitectonic layers, containing roughly 60,000-100,000 neurons organized into functional microcircuits.

The transition rules -- what determines how each column's state changes from one timestep to the next -- are defined by two factors: the **six-layer internal architecture** of each column (how signals flow vertically through layers I-VI, with characteristic input/output patterns at each layer) and the **lateral connectivity** between columns (horizontal connections within and between cortical areas). Unlike the simple binary rules of elementary cellular automata, the cortical automaton's rules operate in a space of many thousand dimensions, reflecting the vast number of state variables each column maintains.

## Figure

```mermaid
graph TB
    subgraph "The Cortical Automaton"
        direction TB
        subgraph lattice["Cortical Surface (High-Dimensional Lattice)"]
            direction LR
            C1["Column\nA"]
            C2["Column\nB"]
            C3["Column\nC"]
            C4["Column\nD"]
            C5["Column\nE"]
            C1 <-->|"lateral\nconnections"| C2
            C2 <-->|"lateral\nconnections"| C3
            C3 <-->|"lateral\nconnections"| C4
            C4 <-->|"lateral\nconnections"| C5
        end
        subgraph column["Each Column (Transition Rules)"]
            direction TB
            L1["Layer I — Feedback input"]
            L2["Layer II/III — Lateral/corticocortical"]
            L4["Layer IV — Feedforward input"]
            L5["Layer V — Subcortical output"]
            L6["Layer VI — Thalamic feedback"]
            L1 --> L2 --> L4 --> L5 --> L6
        end
        subgraph output["System State"]
            S["Spatiotemporal\nActivation Pattern\n= Cortical Automaton\nState"]
        end
        lattice --> output
        column -.->|"defines rules for"| lattice
    end

    style S fill:#4CAF50,stroke:#333,stroke-width:2px,color:#fff
    style lattice fill:#E3F2FD,stroke:#1565C0
    style column fill:#FFF3E0,stroke:#E65100
```

*Cortical columns serve as cells in the automaton; the six-layer architecture and lateral connectivity define the transition rules. The instantaneous spatiotemporal activation pattern is the automaton's state.*

![Cortical homunculus showing somatosensory and motor cortex mapping with Penfield-style distorted body representations](../assets/book-originals/image_004.png)

*Cortical homunculus — the somatosensory and motor cortex mapping (Penfield). Each strip of cortex dedicates processing resources proportional to the body part's sensory or motor precision, not its physical size. This is the cortical automaton's functional specialization made visible: the same six-layer columnar architecture, applied across the cortical surface, but with locally adapted transition rules that reflect different functional demands.*

![Six neocortical layers (Cajal-style histological drawing) showing pyramidal cells and fiber patterns across layers I-VI](../assets/book-originals/image_009.png)

*The six cytoarchitectonic layers of the neocortex (Schicht 1-6). These layers define the transition rules of the cortical automaton: Layer IV receives feedforward thalamic input, Layers II/III handle lateral corticocortical integration, Layer V projects to subcortical structures, and Layer VI provides thalamic feedback. Every cortical column implements this same basic architecture.*

![Brodmann areas — cytoarchitectonic map of the cerebral cortex showing lateral and medial views with numbered functional areas](../assets/book-originals/image_015.png)

*Brodmann areas — the cytoarchitectonic map of the cerebral cortex. While all cortical columns share the same six-layer architecture, the relative thickness of layers and the density of cell types varies systematically across areas. These variations define different "rule sets" in the cortical automaton, specialized for visual processing (areas 17-19), motor control (area 4), language (areas 44-45), and other functions.*

## Not Consciousness Itself

A critical distinction: the cortical automaton is *not* consciousness. It is the computational medium -- the hardware clock cycle, the substrate dynamics. Consciousness arises from the interplay between the automaton's dynamics and the [models it carries](../core-architecture/four-model-theory.md): the implicit models (IWM, ISM) stored in the substrate, and the explicit models (EWM, ESM) generated from them. Without the automaton's Class 4 dynamics, the models cannot generate a coherent simulation. Without the models, the automaton produces complex dynamics but no self-referential experience. The cortical automaton is to consciousness what a CPU's clock-driven state transitions are to a running program: necessary infrastructure, not the program itself.

## Observable Traces

This framing suggests a concrete observational hypothesis. In a dark, quiet environment with eyes closed, after retinal afterimages have faded, faint flickering patterns are visible against the dark field. These "dark noise" phosphenes have well-characterized retinal sources -- rods generate discrete events by thermal isomerization of rhodopsin -- and spontaneous activity in V1 is a plausible additional contributor. The hypothesis is that the *cortical* component, to the extent it can be separated from the retinal one, is the lowest layer of the [implicit-explicit boundary](../mechanisms/implicit-explicit-boundary.md) becoming momentarily accessible: spontaneous dynamics of the cortical automaton leaking through to the virtual level. The progression from simple phosphenes to geometric patterns to hypnagogic imagery during sleep onset parallels the hierarchical permeability account that explains [psychedelic phenomenology](../phenomena/psychedelics.md). The cortical contribution has not yet been cleanly separated from retinal sources, so this remains a hypothesis rather than a confirmed prediction.

## Key Takeaway

The cortex realizes cellular-automaton dynamics in a many-thousand-dimensional space -- at column granularity, columns as cells and the six-layer architecture as rules, though the choice of granularity is open. It provides the computational medium for consciousness but is not consciousness itself.

## See Also

- [Criticality: Signature, Not Requirement](../physical-foundations/criticality.md)
- [The Five-System Hierarchy](../physical-foundations/five-system-hierarchy.md)
- [Two Thresholds for Consciousness](../physical-foundations/two-thresholds.md)
- [The Four Models](../core-architecture/four-model-theory.md)
- [The Implicit-Explicit Boundary](../mechanisms/implicit-explicit-boundary.md)
