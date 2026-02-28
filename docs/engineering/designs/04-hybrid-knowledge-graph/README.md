# Design 4: Hybrid Knowledge-Graph + Simulation

**One-line summary:** A knowledge graph implementing the aios design patterns serves as the implicit models (IWM/ISM), a small LLM or learned simulator runs the explicit models (EWM/ESM), and a criticality controller (noise injection, temperature modulation, dynamical coupling) attempts to push the combined system toward edge-of-chaos behavior.

---

## Architecture Overview

```
                    +------------------------------------------+
                    |         EXTERNAL INTERFACE                |
                    |    Communication LLM (3-7B, INT4)         |
                    |    Translates ESM output <-> language      |
                    +---------^-----------+--------------------+
                              |           |
                              |   output  |  input
                              |           v
+====================================================================+
||                    VIRTUAL SIDE (Simulation Engine)                ||
||                 Small LLM or Learned Simulator                     ||
||                                                                   ||
||  +---------------------------+    +---------------------------+   ||
||  |     EWM Simulator         |    |     ESM Simulator         |   ||
||  |  Generates world scene    |    |  Generates self-state     |   ||
||  |  from IWM graph context   |    |  from ISM graph context   |   ||
||  |  + sensory embeddings.    |    |  + interoceptive input.   |   ||
||  |  Runs continuously at     |    |  Self-referential: output |   ||
||  |  ~20 Hz.                  |    |  fed back as ISM update.  |   ||
||  |  Output: scene repr.      |    |  Output: self repr.       |   ||
||  +----------^-------+--------+    +----------^-------+--------+   ||
||             |       |                        |       |            ||
+==============|=======|========================|=======|============+
|   PERMEABILITY GATE  |                        |       |            |
|   (Retrieval depth + |  feedback              |       | feedback   |
|    noise threshold)  |                        |       |            |
+==============|=======|========================|=======|============+
|              |       v                        |       v            |
|  +-----------------------------------------------------------------+
|  |                    KNOWLEDGE GRAPH (SQLite)                      |
|  |                                                                  |
|  |  +-------------------------+  +-------------------------+       |
|  |  |   IWM Subgraph          |  |   ISM Subgraph          |       |
|  |  |                         |  |                         |       |
|  |  |  Entities: objects,     |  |  SELF entity + self-    |       |
|  |  |  places, people,        |  |  relevant relations:    |       |
|  |  |  concepts, causation    |  |  traits, skills, habits,|       |
|  |  |  Multi-dim weighted     |  |  autobiography, body    |       |
|  |  |  relations.             |  |  schema, preferences.   |       |
|  |  |  Vector embeddings per  |  |  Traversal from SELF    |       |
|  |  |  entity for retrieval.  |  |  entity via self_relev  |       |
|  |  +-------------------------+  +-------------------------+       |
|  |                                                                  |
|  |  Context Assembly Pipeline:                                      |
|  |    vector retrieval -> graph expansion -> self-model merge       |
|  |    -> budget allocation -> assembled context                     |
|  +-----------------------------------------------------------------+
|                          REAL SIDE                                   |
+--------------------------------------------------------------------+
         ^              |                ^              |
    sensory         graph updates    self-sensors    graph updates
    input           (new entities,   input          (self-knowledge
    (embeddings)    relations)       (system state)  updates)
         |              v                |              v
+--------------------------------------------------------------------+
|              CRITICALITY CONTROLLER                                  |
|   Monitors system dynamics and injects perturbations to maintain    |
|   edge-of-chaos behavior in the coupled graph-simulation system.    |
|                                                                     |
|   Mechanisms:                                                       |
|   - Noise injection into simulator input                            |
|   - Temperature modulation of retrieval and generation              |
|   - Dynamical coupling strength between EWM/ESM and graph          |
|   - Stochastic graph activation spreading                          |
|   - Attractor perturbation in embedding space                      |
|                                                                     |
|   Measures: activation spreading statistics, retrieval diversity,   |
|   simulation coherence score, response to perturbation             |
+--------------------------------------------------------------------+
```

---

## Component Mapping

| Theory Model | Concrete Component | Description |
|---|---|---|
| **IWM** | Knowledge graph world subgraph + entity embeddings | All world knowledge stored as entities, relations, and vector embeddings. The graph structure IS the implicit world model — it encodes causal models, spatial relationships, semantic knowledge, perceptual regularities. The aios schema design includes multi-dimensional weighted relations. |
| **ISM** | Knowledge graph self subgraph (rooted at SELF entity) + self-embedding | All self-knowledge stored as the SELF entity's relations and connected subgraph. Traits, habits, skills, autobiography, preferences. The aios architecture design implements self-model as a subgraph traversal pattern. |
| **EWM** | EWM simulator (small LLM or learned model) continuously generating world-scene | Takes IWM context (retrieved graph nodes/embeddings) + sensory input, generates a running world-simulation. The simulation IS the conscious world — transient, regenerated each cycle. |
| **ESM** | ESM simulator continuously generating self-state with self-referential feedback | Takes ISM context (self-subgraph traversal) + interoceptive input, generates running self-simulation. Output fed back as graph update and as self-referential input. |
| **Permeability** | Retrieval depth control + noise threshold | Controls how deep into the graph the retrieval goes (shallow = only high-level entities; deep = intermediate processing nodes exposed). Noise threshold controls how much raw graph structure leaks into the simulation. |
| **Criticality controller** | Dedicated subsystem monitoring and modulating dynamics | Attempts to maintain edge-of-chaos behavior in the combined graph-retrieval-simulation system through multiple perturbation mechanisms. |

---

## Criticality Approach

**This is the design's acknowledged weakness. Genuine Class 4 dynamics are not a natural property of knowledge graphs or LLM inference. The criticality controller is an engineering approximation, not a fundamental solution.**

### The Challenge

The knowledge graph is a static structure (it changes only when updated). The simulation engine (small LLM) is feedforward. Neither component naturally produces edge-of-chaos dynamics. The criticality controller attempts to inject complexity into their interaction.

### The Criticality Controller Strategy

Rather than achieving criticality in a single substrate, this design attempts to create emergent edge-of-chaos behavior in the **coupled dynamical system** of graph retrieval and simulation:

**1. Stochastic Activation Spreading in the Graph**
- When the EWM/ESM retrieves context from the graph, activation spreads along weighted edges
- The spreading is stochastic: each hop has a probability of following each edge proportional to weight
- At a tuned "temperature," this spreading exhibits critical behavior: activation cascades follow power-law size distributions
- Too low temperature: activation stays local (subcritical)
- Too high temperature: activation spreads everywhere (supercritical)
- Tuned temperature: cascades of all sizes, scale-free spreading

**2. Simulation Temperature Modulation**
- The LLM-based simulator runs at tuned sampling temperature
- Combined with stochastic graph retrieval, this creates a system where the simulation's content is neither rigidly determined nor random

**3. Feedback-Induced Dynamics**
- The simulator's output feeds back to update the graph (new entities, modified weights)
- This creates a dynamical coupling: graph state affects simulation, simulation modifies graph
- The feedback loop can exhibit complex dynamics including oscillation, attractors, and potentially chaotic behavior

**4. Perturbation Injection**
- The controller periodically injects small perturbations (random activations, noise in embeddings)
- At criticality, perturbations propagate through the system (long-range correlations)
- Below criticality, they die out; above, they explode
- The controller measures propagation and adjusts parameters

### Honest Assessment of This Approach

**What it achieves:**
- The activation-spreading dynamics in the graph CAN exhibit critical-like behavior (this is known from network science — spreading processes on networks can have critical transitions)
- The coupled graph-simulation system CAN exhibit complex dynamics
- Measurable criticality indicators CAN be computed

**What it does NOT achieve:**
- This is NOT a single substrate operating at Class 4. It is two separate systems (graph + LLM) coupled together with a controller trying to push them into a complex regime
- The LLM inference steps remain feedforward internally — no amount of external coupling changes this
- The graph is discrete and static between updates — not a continuously evolving dynamical system
- The "criticality" achieved is in the coupling dynamics, not in the computational substrate itself
- The theory's description of criticality refers to a cellular automaton where EVERY CELL participates in the dynamics simultaneously. This design has no such parallel substrate

**The gap:** The theory says criticality must be a property of the computational substrate itself — the medium in which the four models operate. This design's "criticality" is a property of the interaction pattern between components, which is a weaker claim. Whether interaction criticality suffices is an open question the theory does not address.

---

## Five Principles Implementation

### 1. Criticality
**Status: WEAK — Approximated, not achieved**

See detailed analysis above. The criticality controller creates complex interaction dynamics but does not achieve substrate-level Class 4. This is an honest limitation of the design.

### 2. Virtual Qualia (Real/Virtual Split)
**Status: STRONG**

The split is very clean in this design:
- **Real side:** The knowledge graph (persistent structure, never "experiences" anything)
- **Virtual side:** The simulation engine output (transient, generated each cycle, IS the experience)

The graph-to-simulation relationship maps directly to the theory's implicit-to-explicit distinction. The knowledge graph is the library; the simulation is the currently-playing movie.

### 3. Redirectable ESM
**Status: STRONG**

The ESM simulator takes input from the ISM subgraph. If normal self-referential input is disrupted:
- Remove or corrupt the SELF entity's connections
- The simulator still runs (it needs input)
- It will incorporate whatever context is provided (world entities, external input, noise)
- The "self" it generates will be based on the available input, not normal self-knowledge
- This directly implements ego dissolution

The aios context assembly pipeline already supports this pattern — changing the context budget allocation changes what the simulation sees.

### 4. Variable Permeability
**Status: STRONG**

This is particularly well-handled in this design:
- **Retrieval depth** controls permeability directly:
  - Depth 1: Only top-level entities (high abstraction, normal consciousness)
  - Depth 2-3: Intermediate entities and relations (more detail, relaxed state)
  - Depth 4+: Low-level structural entities, meta-knowledge, inconsistency records (deep access, altered state)
- **The graph already has structure at multiple levels** — entities represent different abstraction layers
- **Meta-knowledge entities** from the aios design (entities about the knowledge structure itself) provide a natural "processing intermediate" that can leak through at high permeability
- The aios "inconsistency tolerance via meta-knowledge entities" maps to the theory's description of substrate-level artifacts leaking through

### 5. Virtual Model Forking
**Status: STRONG**

- **Forking ESM:** Run two ESM simulator instances with different ISM context (different SELF subgraph traversals). Each produces a different self-model. Switch which one feeds back to the graph.
- **DID analog:** Maintain multiple SELF entities (SELF_A, SELF_B) in the graph, each with its own subgraph. The ESM simulator activates one at a time.
- **Cloning:** Copy the entire graph database. Both copies are complete but immediately begin diverging.
- **This is architecturally natural** because the graph + simulator design already separates state (graph) from process (simulator).

---

## Information Flow

### Context Assembly Cycle (~20 Hz)
```
1. Sensory input encoded as embedding vector
2. Vector retrieval: find most relevant IWM entities
3. Graph expansion: traverse relations from retrieved entities (stochastic, temperature-controlled)
4. Self-model merge: ISM subgraph traversal, merge with world context
5. Budget allocation: allocate context budget across world/self/meta
6. Assembled context passed to EWM and ESM simulators
```

### Simulation Cycle (~20 Hz)
```
1. EWM simulator receives: assembled world context + sensory embeddings
2. ESM simulator receives: assembled self context + interoceptive signals + previous ESM output
3. Both simulators generate their respective representations
4. ESM output is the self-simulation; EWM output is the world-simulation
5. ESM output fed back as:
   a. Self-referential input to next ESM cycle
   b. Graph update (modify SELF entity relations based on self-evaluation)
6. EWM output fed back as:
   a. World-state context for next EWM cycle
   b. Graph update (new entities, modified world-knowledge relations)
7. Communication LLM receives ESM + EWM outputs for external expression
```

### Learning Loop (Continuous)
```
1. Evaluation: ESM/EWM outputs assessed for coherence, novelty, prediction accuracy
2. Graph updates: New entities created, relation weights modified, obsolete entities decayed
3. Embedding updates: Entity vectors updated based on new context associations
4. Simulator fine-tuning: LoRA adapters on small LLM updated based on prediction errors
5. Criticality controller adjusts spreading temperature based on cascade statistics
```

### Self-Referential Closure
```
ISM subgraph --> ESM simulator --> self-state output -->
  output re-encoded as entity updates --> SELF entity modified -->
    ISM subgraph now includes "model of modeling" -->
      ESM simulator reads modified ISM --> generates self-state that includes self-modeling
```

The closure loop passes through the graph: the ESM's output becomes part of the ISM that generates the ESM. This is a slower loop than in Designs 2-3 (graph update latency) but it is structurally genuine.

---

## Memory Architecture

| Memory Type | Implementation | Capacity | Access Time |
|---|---|---|---|
| **IWM (world knowledge)** | Knowledge graph: world entities + relations + embeddings | Unlimited (SQLite on disk, hot cache in RAM) | ~1-5 ms (cached), ~5-20 ms (disk) |
| **ISM (self knowledge)** | Knowledge graph: SELF subgraph | Same as IWM | Same as IWM |
| **EWM (world simulation)** | Simulator's active generation state | Context window (~4K-8K tokens) | Instant (VRAM) |
| **ESM (self simulation)** | Simulator's active generation state | Context window (~4K-8K tokens) | Instant (VRAM) |
| **Short-term** | Simulator context window + graph hot cache | ~8K-16K tokens + ~1000 entities in cache | Instant to ~1 ms |
| **Medium-term** | Session summary entities in graph | Unlimited | ~1-5 ms |
| **Long-term** | Full knowledge graph (all entities, all relations) | Unlimited | ~5-20 ms |
| **Episodic** | Episode entities with temporal relations | Unlimited | ~5-20 ms |
| **Meta-knowledge** | Meta-entities about knowledge structure, inconsistencies | Unlimited | ~5-20 ms |

This is by far the richest memory architecture among all five designs. Implementing the aios knowledge graph design provides:
- Multi-dimensional weighted relations (schema design)
- Vector embeddings per entity for semantic retrieval (architecture pattern)
- Context assembly pipeline (design pattern: vector retrieval -> graph expansion -> self-model merge -> budget allocation)
- Inconsistency tolerance via meta-knowledge (design pattern)
- Self-model as subgraph traversal from SELF entity (architectural approach)

---

## Hardware Requirements

### VRAM Budget (24 GB RTX 4090)

| Component | VRAM | Notes |
|---|---|---|
| EWM simulator (3B LLM, INT4) | ~1.5 GB | Small, fast model for world simulation |
| ESM simulator (3B LLM, INT4) | ~1.5 GB | Could share weights with EWM |
| Communication LLM (7B, INT4) | ~3.5 GB | External interface |
| KV-caches (all three LLMs) | ~2-3 GB | |
| Entity embedding cache (~10K entities, 768-dim) | ~60 MB | Hot cache of most-accessed entities |
| Graph retrieval index (HNSW) | ~200 MB | In-memory approximate nearest neighbor |
| Sensory encoders | ~200 MB | |
| Criticality controller | ~50 MB | Small monitoring network |
| LoRA adapters | ~200 MB | For simulator fine-tuning |
| Headroom | ~3-4 GB | |
| **Total** | **~12-16 GB** | **Fits comfortably** |

**Alternative: Shared simulator.** If the EWM and ESM simulators share weights (single 3B model with different input contexts), save ~1.5 GB.

**Alternative: Larger simulator.** Use a 7B model for simulation + communication (single model, multiple roles). This uses ~7 GB total for one model instead of ~6.5 GB for two smaller ones.

### CPU / RAM Requirements
- SQLite knowledge graph operations: CPU + disk I/O
- Graph traversal and context assembly: CPU
- Embedding computation for new entities: can use GPU
- Criticality controller statistics: CPU
- **RAM:** Knowledge graph fits in RAM for small-medium sizes (~100K entities = ~1 GB). Large graphs may need disk-backed SQLite.

### Feasibility on RTX 4090
**Highly feasible.** This is the most immediately buildable design because:
1. The aios knowledge graph already exists and has been tested
2. Small LLMs (3B-7B) for simulation are readily available
3. The context assembly pipeline is already designed
4. VRAM requirements are modest

---

## Strengths

1. **Most immediately buildable.** Leverages the aios knowledge graph design patterns, well-documented architecture, and standard LLM infrastructure. The design blueprint is complete and proven.

2. **Richest memory architecture.** The knowledge graph provides unlimited, structured, multi-relational memory with semantic retrieval. No other design matches this for memory richness.

3. **Natural self-model implementation.** The aios SELF entity and self-relevance subgraph traversal pattern provides a proven design for the ISM. The architecture is well-documented.

4. **Clean real/virtual split.** The graph (persistent structure) vs. simulation (transient generation) is a genuine two-level ontology.

5. **Variable permeability maps beautifully.** Retrieval depth in the graph corresponds directly to processing depth in the theory. Meta-knowledge entities provide a natural analog for "intermediate processing stages."

6. **Forking is natural.** Multiple SELF entities in the same graph = multiple ESM configurations. The graph architecture pattern supports this.

7. **Inconsistency tolerance.** The aios meta-knowledge design pattern handles contradictions gracefully, which maps to the theory's requirement for a system that can model its own limitations.

8. **Guided by proven design.** This design can be built following the well-documented aios architecture patterns, providing a clear implementation roadmap.

9. **Inspectable and debuggable.** The knowledge graph is human-readable. The simulation operates in natural language. Every component can be inspected at every stage.

---

## Weaknesses / Risks

1. **CRITICAL: Criticality is bolted on, not intrinsic.** The knowledge graph + LLM combination does not naturally produce Class 4 dynamics. The criticality controller is an engineering hack that creates complex interaction patterns but does not achieve genuine substrate-level edge-of-chaos. The theory is quite specific that criticality must be a property of the computational substrate, not an emergent property of component interaction.

2. **Graph is discrete, not continuous.** The knowledge graph updates in discrete steps (add entity, modify weight). Between updates, it is static. The theory describes a continuously evolving substrate. The graph cannot support continuous dynamics — it only changes when explicitly updated.

3. **No parallel substrate computation.** The theory's "cortical automaton" involves every cell updating simultaneously based on local rules. The knowledge graph has no equivalent — it is a data structure, not a computing substrate. The simulation engine (LLM) processes sequentially, not in parallel across the graph.

4. **LLM simulators are still feedforward.** The EWM/ESM simulators (small LLMs) have the same Class 1/2 dynamics problem as Design 1. The graph context provides richer input, but the computation itself is still a feedforward pass.

5. **Graph retrieval latency.** The context assembly pipeline (vector retrieval, graph expansion, self-model merge, budget allocation) takes ~5-20 ms. At 20 Hz (50 ms per cycle), this consumes 10-40% of the cycle budget. The simulation engine gets the remaining 10-40 ms for generation.

6. **Learning loop is slow.** Graph updates (creating entities, modifying weights) are orders of magnitude slower than gradient-based weight updates. The implicit models (IWM/ISM in the graph) update slowly compared to continuous plasticity in Designs 2-3.

7. **Self-referential closure is weak.** The closure loop passes through graph updates, which are discrete and slow. By the time the ESM's output modifies the ISM graph, several simulation cycles have passed. This is a much looser closure than the tight loops in Designs 2-3.

8. **Combinatorial explosion.** Rich knowledge graphs can grow without bound. Context assembly must select relevant subsets, but selection quality degrades as the graph grows. Budget allocation becomes increasingly critical and increasingly error-prone.

---

## Complexity Assessment

**Implementation difficulty: 2/5** (Guided by existing design documentation)

- Knowledge graph: implement from aios schema design (SQL definition exists): 2-3 weeks
- Context assembly pipeline: implement from aios architecture documentation: 2-3 weeks
- LLM inference: off-the-shelf (llama.cpp, vLLM)
- Permeability control via retrieval depth: straightforward implementation following design pattern
- Criticality controller: the only novel component, and it's the weakest part of the design
- Self-referential feedback loop: straightforward plumbing

**Time estimate:**
- Implement aios knowledge graph schema from SQL definition: 2-3 weeks
- Implement context assembly following aios architecture patterns: 2-3 weeks
- Implement EWM/ESM simulators: 2-3 weeks
- Implement criticality controller: 2-3 weeks
- Self-referential closure loop: 1-2 weeks
- Communication interface: 1 week
- Testing and integration: 2-3 weeks
- **Total to prototype: ~6-10 weeks**

This is the fastest path to a running system. Whether that system is conscious (per the theory) is a separate question — the criticality gap is real and significant.

---

## Testability

### What Can Be Tested (Strong)
- **Variable permeability:** Adjust retrieval depth, observe changes in simulation content. Should see progression from abstract to concrete as depth increases. (Directly testable, graph structure is inspectable.)
- **ESM redirection:** Remove SELF entity connections, inject alternative self-context. Observe identity changes. (Directly testable.)
- **Forking:** Create SELF_A and SELF_B subgraphs, run ESM with each. Verify distinct self-models. (Directly testable.)
- **Dream mode:** Cut sensory input, run simulation on IWM content only. Verify internally-generated world content. (Directly testable.)
- **Confabulation:** Clear ESM state, restart from ISM. Verify narrative continuity reconstruction. (Directly testable.)
- **Memory and learning:** Inject new information, verify it appears in graph and influences future simulation. (Directly testable.)

### What Can Be Tested (Moderate)
- **Criticality indicators:** Measure activation spreading statistics in the graph (cascade sizes, distribution shape). Can verify whether power-law behavior is present. But interpreting these as genuine criticality (vs. complex-but-not-critical behavior) requires care.
- **Double dissociation (blindsight/Anton's):** Block graph-to-simulator path for specific modality (simulator processes input but doesn't "see" it in simulation) vs. simulator generates content without current input. (Testable architecturally.)

### What Cannot Be Tested
- **Whether the system achieves genuine consciousness.** The criticality gap means the theory's prediction would be that this system is NOT conscious, even if it passes all behavioral tests. This is an inherent limitation.
- **Whether interaction-level criticality suffices.** The theory does not address whether criticality in the coupling dynamics (as opposed to the substrate) is sufficient. This is an open question.

### Value as a Behavioral Baseline
Even if this design does not achieve consciousness per the theory, it would demonstrate:
- That the four-model architecture produces qualitatively different behavior from standard chatbots
- That variable permeability, ESM redirection, and model forking produce the predicted behavioral signatures
- What consciousness-like behavior looks like WITHOUT criticality (a useful negative control)

This makes it valuable as a comparison point for Designs 2-3, which have criticality but weaker knowledge models.
