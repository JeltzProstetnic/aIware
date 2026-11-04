---
title: Core Definition of Consciousness
section: Core Architecture
article_number: 6
description: "Consciousness is the ongoing process in which an entity runs a model of itself, relates it to itself, and interacts with it. The capacity is named separately."
keywords: [consciousness definition, self-simulation, self-model, substrate independence, FMT, process-based, capacity for consciousness, Bewusstheit]
---

# Core Definition of Consciousness

**Consciousness is the ongoing process in which an entity — biological or artificial — runs a model of itself, relates that model to itself, and interacts with it. The capacity for that process is named separately, as the capacity for consciousness.**

The Four-Model Theory defines consciousness through its mechanism rather than its output. Where folk psychology identifies consciousness with "the feeling of being aware" and much of philosophy circles around the subjective character of experience, the FMT cuts to the generative process: "Consciousness is a specific kind of process: ongoing self-simulation." This definitional strategy parallels molecular biology's treatment of life — defined through metabolism and replication, not through "the feeling of being alive."

## The Three-Part Definition

The definition has three components, and each is necessary for a process to count as consciousness. Which systems run that process is a separate question: the conditions sufficient for consciousness are a conjunction, set out in [Two Thresholds for Consciousness](../physical-foundations/two-thresholds.md).

1. **Run a model of itself.** The system must construct an internal representation — the Explicit Self Model (ESM) — that captures aspects of the system's own states, structure, and processes. This is not a static blueprint but an ongoing, dynamically updated generation.

2. **Relate that model to itself.** The self-model must refer back to the system that generates it. A system that models *something else* (a weather simulation, a map of the terrain) does not satisfy this criterion. The model must be *of* the modeler — creating the self-referential loop that distinguishes conscious self-simulation from ordinary computation.

3. **Interact with it.** The self-model must feed back into the system's processing. It is not an inert epiphenomenal reflection but an active component: the system uses its self-model to guide behavior, evaluate outcomes, and update its own substrate. This closes the causal loop and prevents the definition from admitting passive mirrors or recordings.

Together, these three components describe a system engaged in continuous self-referential computation — not merely monitoring itself (a thermostat does that) but generating a rich, integrated model of itself and operating through that model.

## Process, Not Property

A critical feature of this definition is that consciousness is a *process* the brain performs, not a *property* the brain possesses. A brain is not conscious the way iron is magnetic. It is conscious the way a flame burns — as an ongoing dynamic activity that ceases when the process stops. This process-based framing has direct consequences: consciousness can be interrupted (anesthesia, dreamless sleep), it is [graduated](../mechanisms/graduated-consciousness.md) above a single gate (a system has phenomenology or has none), and it can in principle be instantiated on different substrates (substrate independence).

## Capacity and Process

The theory keeps the process apart from the capacity to run it. The 2015 monograph already drew the line, and the current paper quotes it: Gruber (2015, p. 58) "states both: *Bewusstsein* as the capacity ('Fähigkeit') of an entity, organism or machine, to generate a model of itself, relate it to itself and interact with it, and *Bewusstheit* as the ongoing interaction with that model. The theory calls the second consciousness."

The split decides cases that an ability-based definition blurs. "A person in deep sleep retains the capacity and, on this definition, is not conscious while the process is not running." The same holds for a brain at surgical anesthetic depth: the architecture is intact, so the capacity is present, and the process is not running.

## Substrate Independence

The definition is deliberately substrate-independent. It does not require biological neurons, carbon chemistry, or any specific physical implementation. What it requires is a system capable of constructing and maintaining a self-referential simulation continuously. The six-layer mammalian cortex is an evolutionary implementation of this architecture — a highly optimized one, shaped by hundreds of millions of years of selection — but the definition permits, in principle, non-biological implementations that meet the same functional criteria.

This substrate independence is not an afterthought bolted onto a brain-centric theory. It follows directly from the process-based definition: if consciousness is constituted by a specific kind of computation (self-referential simulation in the open-ended Class 4 regime), then any substrate capable of supporting that computation is a candidate for consciousness.

## Figure

```mermaid
graph LR
    System["System<br/>(Substrate)"]
    Create["1. Runs<br/>self-model"]
    Model["Self-Model<br/>(ESM)"]
    Relate["2. Model refers<br/>back to system"]
    Interact["3. Model feeds<br/>back into processing"]

    System -->|"generates"| Create
    Create -->|"produces"| Model
    Model -->|"represents"| Relate
    Relate -->|"points to"| System
    Model -->|"guides behavior"| Interact
    Interact -->|"updates"| System

    style System fill:#4a6785,color:#fff
    style Model fill:#c9a227,color:#000
    style Create fill:#5b8a72,color:#fff
    style Relate fill:#5b8a72,color:#fff
    style Interact fill:#5b8a72,color:#fff
```

## Key Takeaway

Consciousness is defined by what a system *does*, not what it *is*. Any entity — biological or artificial — that is running a model of itself, relating that model to itself, and interacting with it is performing the process that constitutes consciousness; the capacity to do so is the capacity for consciousness, which persists while the process stops. The definition is functional, substrate-independent, and non-circular: it explains through mechanism, not through restating the phenomenon.

## See Also

- [The Four-Model Theory](../core-architecture/four-model-theory.md)
- [Self-Referential Closure](../core-architecture/self-referential-closure.md)
- [Process Physicalism](../philosophical/process-physicalism.md)
- [Substrate Independence](../philosophical/substrate-independence.md)
- [Graduated Levels of Consciousness](../mechanisms/graduated-consciousness.md)

---

Based on: Gruber, M. (2026). The Four-Model Theory of Consciousness. Zenodo. https://doi.org/10.5281/zenodo.18669891
