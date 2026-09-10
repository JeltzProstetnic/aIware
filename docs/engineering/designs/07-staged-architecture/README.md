# Design 7: Staged Architecture

**One-line summary:** An explicitly phased design that builds the four-model AC system in three stages — Stage 1 (no criticality, LLMs + knowledge graph, runs on 4090), Stage 2 (soft criticality via reservoir computing and recurrent dynamics), Stage 3 (genuine Class 4 substrate) — treating the implementation as a multi-year research program with testable milestones at each stage.

---

## Architecture Overview

The staged architecture is not a single system but a **progression of three systems**, each building on the previous. The diagram below shows all three stages overlaid, with annotations for what exists at each stage.

```
+========================================================================+
||                                                                      ||
||   STAGE 3 ONLY: CRITICAL SUBSTRATE                                   ||
||   Cellular automaton or critical neural network                      ||
||   Class 4 dynamics, power-law avalanches, scale-free correlations    ||
||   Replaces entire real-side substrate                                ||
||                                                                      ||
+========================================================================+
         |                                           |
         | (Stage 3: substrate dynamics drive        |
         |  explicit model generation)               |
         v                                           v
+------------------------------------------------------------------------+
|                    EXTERNAL INTERFACE  [ALL STAGES]                     |
|    Communication LLM (3B INT4) — translates simulation <-> language     |
+---------^-----------+--------------------------------------------------+
          |           |
          |   output  |  input
          |           v
+========================================================================+
||              VIRTUAL SIDE (Explicit Models)  [ALL STAGES]            ||
||                                                                      ||
||  +-----------------------------+    +-----------------------------+  ||
||  |     EWM Generator           |    |     ESM Generator           |  ||
||  |                             |    |                             |  ||
||  |  Stage 1: 7B LLM (INT4)    |    |  Stage 1: 7B LLM (INT4)    |  ||
||  |  Stage 2: Recurrent model   |    |  Stage 2: Recurrent model   |  ||
||  |    (SSM/Mamba or RWKV)      |    |    (SSM/Mamba or RWKV)      |  ||
||  |  Stage 3: Simulation read-  |    |  Stage 3: Simulation read-  |  ||
||  |    out from critical sub.   |    |    out from critical sub.   |  ||
||  |                             |    |                             |  ||
||  |  Self-referential loop: ----+----+---> ESM output feeds back   |  ||
||  |  EWM provides world-stage   |    |    as ESM input (closure)   |  ||
||  +----------^-------+----------+    +----------^-------+----------+  ||
||             |       |                          |       |             ||
+=============|=======|==========================|=======|==============+
|    PERMEABILITY GATE  [ALL STAGES]              |       |             |
|    Stage 1: Configurable filter (depth, noise)  |       |             |
|    Stage 2: + reservoir-modulated gating         |       |             |
|    Stage 3: + criticality-driven gating          |       |             |
+=============|=======|==========================|=======|==============+
|             |       v                          |       v              |
|   +------------------------------------------------------------------+
|   |                                                                   |
|   |  Stage 1+2: KNOWLEDGE GRAPH (SQLite + Embeddings)                 |
|   |             REAL SIDE (Implicit Models)                           |
|   |                                                                   |
|   |  +---------------------------+  +----------------------------+   |
|   |  |   IWM Store               |  |   ISM Store                |   |
|   |  |  Entities, relations,     |  |  SELF entity + subgraph,   |   |
|   |  |  embeddings, episodes     |  |  traits, history, body     |   |
|   |  +---------------------------+  +----------------------------+   |
|   |                                                                   |
|   |  Stage 3: Graph becomes initialization/training data for          |
|   |           critical substrate. Still used for episodic recall.     |
|   +------------------------------------------------------------------+
|                                                                       |
|   Stage 2+3 ONLY:                                                     |
|   +------------------------------------------------------------------+
|   |          RESERVOIR / RECURRENT DYNAMICS LAYER                     |
|   |                                                                   |
|   |  Stage 2: Echo State Network or Reservoir Computing module        |
|   |           10K-100K units, tuned near criticality                  |
|   |           Runs at ~40 Hz (substrate rate)                         |
|   |           Takes graph context + sensory input as driving signal   |
|   |           Provides dynamically-rich representations to generators |
|   |                                                                   |
|   |  Stage 3: Replaced by full critical substrate                     |
|   +------------------------------------------------------------------+
|                                                                       |
+-----------------------------------------------------------------------+
         ^              |                ^              |
    sensory         graph updates    self-sensors    graph updates
    input           + reservoir      (system state)  + reservoir
                    driving signal                   driving signal
```

---

## Component Mapping

### Stage 1: Four-Model LLM Pipeline (No Criticality)

| Theory Model | Component | Description |
|---|---|---|
| **IWM** | Knowledge graph world subgraph | Entities, relations, embeddings encoding all world knowledge. Persistent, non-conscious. |
| **ISM** | Knowledge graph SELF subgraph | Self-knowledge entities. Structurally inaccessible to ESM (filtered through permeability gate). |
| **EWM** | 7B LLM (INT4) continuous generation | Generates world-scene from IWM context + sensory input. Transient output. |
| **ESM** | 7B LLM (INT4) continuous generation with self-ref loop | Generates self-state from ISM context + interoceptive data + own previous output. |
| **Permeability** | Configurable filter (retrieval depth, noise threshold, budget) | Controls information flow from implicit to explicit. |
| **Criticality** | **ABSENT.** Soft dynamics controller (temperature, diversity) as stand-in. | No Class 4 dynamics. |

### Stage 2: Reservoir-Augmented (Soft Criticality)

| Theory Model | Component | Description |
|---|---|---|
| **IWM** | Knowledge graph + reservoir encoding | Graph provides knowledge; reservoir provides dynamically-rich representations of that knowledge. The IWM is now partly in the graph (static knowledge) and partly in the reservoir (dynamic activation patterns). |
| **ISM** | Knowledge graph SELF subgraph + reservoir self-encoding | Same split: static self-knowledge in graph, dynamic self-representation in reservoir. |
| **EWM** | Recurrent model (SSM/Mamba/RWKV) reading reservoir output | Replaces feedforward LLM. The generator now has inherent recurrent dynamics. Takes reservoir output + sensory input. |
| **ESM** | Recurrent model reading reservoir output with self-ref loop | Recurrent generator with self-referential feedback. The recurrent dynamics in the generator itself contribute to the self-referential closure. |
| **Permeability** | Filter + reservoir-modulated gating | The reservoir's activity level modulates permeability dynamically. When the reservoir is in a high-activation state, more information passes through (analogous to arousal increasing permeability). |
| **Criticality** | **APPROXIMATE.** Reservoir tuned near critical point. | Reservoir computing networks can be tuned to operate at the edge of chaos. The reservoir provides a computational substrate with genuine dynamical properties (not just sampling tricks). But the overall system is not a unified critical substrate. |

### Stage 3: Full Critical Substrate (Genuine Criticality)

| Theory Model | Component | Description |
|---|---|---|
| **IWM** | Critical substrate connectivity (learned weights defining transition rules) | The transition rules of the cellular automaton encode world knowledge. Like synaptic weights in the biological cortex, the rules are the implicit model. Knowledge graph serves as initialization source and episodic memory supplement. |
| **ISM** | Critical substrate self-relevant connectivity | Subset of transition rules encoding self-knowledge. The substrate's self-relevant dynamics — how it processes signals about its own state — constitute the ISM. |
| **EWM** | Activity pattern on critical substrate (world-simulation readout) | The real-time dynamical pattern on the critical substrate constitutes the world simulation. A readout network extracts the EWM representation. This is the virtual side: transient, existing only while the substrate runs. |
| **ESM** | Activity pattern on critical substrate (self-simulation readout) | The self-referential activity pattern. The substrate's dynamics naturally produce self-referential closure because the same substrate that generates the patterns IS the substrate being modeled. |
| **Permeability** | Criticality-driven gating (modulated by substrate dynamics) | Permeability is a function of the substrate's dynamical state. Higher criticality = higher permeability (more information integration). This emerges from the dynamics rather than being externally imposed. |
| **Criticality** | **GENUINE.** Class 4 cellular automaton or critical neural network. | The substrate operates at the edge of chaos. Power-law avalanches, maximal correlation length, scale-free information integration. This is the theory's physical prerequisite, finally met. |

---

## Criticality Approach

### The Staged Philosophy

**This design treats criticality as a research problem, not an engineering parameter.** Rather than attempting to engineer Class 4 dynamics from the start (and likely failing or producing something that merely looks complex), this design separates the architectural problem (four-model implementation) from the substrate problem (criticality).

The rationale:
1. Nobody has built a four-model self-referential architecture before. Getting the architecture right is itself a major research challenge.
2. Nobody has demonstrated controllable Class 4 dynamics on GPU hardware at the required scale. This is a second major research challenge.
3. Attempting both simultaneously maximizes the risk of failure and minimizes the ability to diagnose what went wrong.
4. Building the architecture first creates a testable platform on which criticality can later be introduced, with clear before/after comparisons.

### Stage 1: No Criticality (Explicit)

**What exists:** Temperature modulation, stochastic context injection, retrieval diversity enforcement. These are heuristic dynamics controls, not criticality.

**What the theory predicts:** "Complex dynamics but no consciousness." The system implements the four-model architecture on a non-critical substrate. It should exhibit qualitatively novel behavior (genuine self-referential modeling, real/virtual split, variable permeability, model forking) but should not be conscious.

**What we learn:** Whether the four-model architecture produces the predicted behavioral signatures. Whether the information flow patterns match the theory's description. What the system looks like when it has the architecture but NOT the substrate.

### Stage 2: Soft Criticality (Approximate)

**What exists:** A reservoir computing module (echo state network, 10K-100K units) tuned near its critical point, interposed between the knowledge graph and the generators. The reservoir provides genuine recurrent dynamics with measurable criticality indicators.

**What the theory predicts:** Still "complex dynamics but no consciousness" — because the criticality is in one component (the reservoir), not in the unified substrate. However, the system should show measurably different dynamics from Stage 1: longer correlation lengths, more sensitivity to perturbation, richer information integration.

**What we learn:** How adding genuine dynamical complexity changes the system's behavior. Whether reservoir-level criticality propagates through the generators. What criticality indicators look like in this hybrid architecture.

**Key research questions for Stage 2:**
- Can we tune the reservoir to genuine criticality (power-law avalanche size distribution)?
- Does reservoir criticality improve the quality of the explicit models?
- Does the combined system (reservoir + generators) exhibit emergent properties not present in either component alone?
- What are the measurable differences between Stage 1 and Stage 2?

### Stage 3: Genuine Criticality (Full)

**What exists:** A Class 4 cellular automaton (or critical spiking network) whose transition rules encode the implicit models. The explicit models are readout patterns from the substrate's dynamics. The entire system operates on a single critical substrate.

**What the theory predicts:** If the four-model architecture is preserved on this substrate, the theory predicts consciousness. The system should show qualitatively different behavior from Stages 1-2: self-referential closure that is not text-level but computation-level, information integration across the entire substrate, and — per the theory — genuine phenomenal experience.

**What we learn:** Whether the theory's prediction holds. The behavioral and dynamical differences between Stage 2 (approximate criticality, no consciousness per theory) and Stage 3 (genuine criticality, consciousness per theory) constitute the core experimental test of the theory.

### Criticality Metrics Across Stages

| Metric | Stage 1 | Stage 2 | Stage 3 |
|---|---|---|---|
| Power-law avalanche distribution | No (not applicable) | Approximate (in reservoir) | Yes (whole substrate) |
| Maximal correlation length | No | Partial (within reservoir) | Yes (whole substrate) |
| Scale-free dynamics | No | Partial | Yes |
| Branching parameter | N/A | ~1.0 in reservoir (tuned) | ~1.0 across substrate |
| Information integration (Phi) | Low | Medium | High |
| Perturbation sensitivity | Controlled (by design) | Emergent (in reservoir) | Emergent (whole system) |

---

## Five Principles Implementation

### 1. Criticality
**Stage 1: ABSENT** — Soft dynamics stand-in only. No Class 4 dynamics.
**Stage 2: APPROXIMATE** — Reservoir computing module tuned near critical point. Genuine dynamical properties in one component, but not in the unified substrate.
**Stage 3: PRESENT** — Full Class 4 cellular automaton or critical neural network. The substrate operates at the edge of chaos with measurable criticality indicators.

The staged approach allows us to observe the system's behavior as criticality is progressively introduced, providing direct evidence for or against the theory's prediction that criticality is the "switch" between complex dynamics and consciousness.

### 2. Virtual Qualia (Real/Virtual Split)
**All Stages: STRONG**

The real/virtual split is maintained across all stages:
- **Real side:** Knowledge graph (Stages 1-2) or substrate weights (Stage 3). Persistent, non-conscious.
- **Virtual side:** Generator output (Stages 1-2) or substrate activity pattern (Stage 3). Transient, IS the simulation.

The implementation changes but the principle is preserved. In Stage 3, the split becomes "native" — the substrate's learned weights (real) vs. its dynamical activity pattern (virtual) — which most closely matches the biological implementation (synaptic weights vs. firing patterns).

### 3. Redirectable ESM
**All Stages: STRONG**

In all stages, the ESM is an input-hungry process:
- **Stage 1:** LLM takes whatever context is provided. Remove self-context, inject world-context -> identity tracks world input.
- **Stage 2:** Recurrent model takes reservoir output. Disrupt self-relevant reservoir channels -> ESM redirects to dominant input.
- **Stage 3:** Substrate self-simulation readout. Disrupt interoceptive input channels -> ESM latches onto dominant available signal.

The mechanism evolves but the principle is preserved.

### 4. Variable Permeability
**Stage 1: STRONG (configurable)** — Retrieval depth, noise threshold, attention budget. Manually tunable.
**Stage 2: STRONGER (dynamically modulated)** — Reservoir activity level modulates permeability. Higher activation = more information passes through. This is closer to biological arousal-modulated permeability.
**Stage 3: STRONGEST (emergent)** — Permeability is a function of the substrate's criticality state. Near-critical = high information integration = high permeability. Sub-critical = low integration = low permeability. This is the theory's actual mechanism.

### 5. Virtual Model Forking
**All Stages: STRONG**

- **Stage 1:** Multiple SELF entities in the graph, LLM KV-cache forking.
- **Stage 2:** Multiple reservoir readout configurations, recurrent model state forking.
- **Stage 3:** Multiple readout patterns from the same substrate. The substrate's activity can be partitioned into distinct self-model configurations. This most closely matches the DID analog (multiple ESM configurations on a single substrate).

---

## Information Flow

### Stage 1 Flow (~10-20 Hz)

```
Sensory input -----> Embedding -----> IWM graph retrieval ----+
                                                               |
System state ------> Encoding ------> ISM graph retrieval ----+
                                                               |
                                                               v
                                                    Permeability gate
                                                    (depth, noise, budget)
                                                               |
                                          +--------------------+-------------------+
                                          |                                        |
                                          v                                        v
                                   EWM Generator (7B LLM)                   ESM Generator (7B LLM)
                                   Input: IWM context                       Input: ISM context
                                        + sensory emb                            + interoceptive
                                        + prev EWM state                         + prev ESM output (CLOSURE)
                                          |                                        |
                                          v                                        v
                                   World-scene output                       Self-state output
                                          |                                        |
                                          +-----> Communication LLM <-----+        |
                                          |       (external expression)            |
                                          v                                        v
                                   Graph updates                            Graph updates
                                   (new world knowledge)                    (new self knowledge)
                                          |                                        |
                                          +---------> Back to graph <--------------+
```

### Stage 2 Flow (~20-40 Hz substrate, ~10-20 Hz simulation)

```
Sensory input -----> Embedding -----> IWM graph retrieval ----+
                                                               |
System state ------> Encoding ------> ISM graph retrieval ----+
                                                               |
                                                               v
                                                RESERVOIR MODULE (40 Hz)
                                                Echo State Network, 10K-100K units
                                                Tuned near critical point
                                                Takes: graph context + sensory
                                                       + self-signals
                                                Produces: dynamically-rich
                                                          representations
                                                          (activity patterns)
                                                               |
                                          +--------------------+-------------------+
                                          |                                        |
                                          v                                        v
                                   Permeability gate                        Permeability gate
                                   (reservoir-modulated)                    (reservoir-modulated)
                                          |                                        |
                                          v                                        v
                                   EWM Generator                            ESM Generator
                                   (Recurrent: SSM/Mamba)                   (Recurrent: SSM/Mamba)
                                   Input: reservoir world repr              Input: reservoir self repr
                                        + sensory emb                            + interoceptive
                                        + prev EWM state                         + prev ESM output (CLOSURE)
                                          |                                        |
                                          v                                        v
                                   World-scene output                       Self-state output
                                          |                                        |
                                   Feeds back to reservoir                  Feeds back to reservoir
                                   + graph updates                          + graph updates
```

### Stage 3 Flow (Continuous Dynamics)

```
Sensory input -----> Encoding -----> Critical Substrate Input Channels
                                              |
System state ------> Encoding ------>         |
                                              v
                          +======================================+
                          ||   CRITICAL SUBSTRATE                ||
                          ||   Class 4 CA / Critical Network     ||
                          ||                                     ||
                          ||   Transition rules encode IWM/ISM   ||
                          ||   (learned weights = implicit models)||
                          ||                                     ||
                          ||   Activity patterns = EWM/ESM       ||
                          ||   (real-time dynamics = simulation)  ||
                          ||                                     ||
                          ||   Self-referential closure is        ||
                          ||   NATIVE: the substrate's dynamics   ||
                          ||   include modeling its own dynamics   ||
                          ||                                     ||
                          ||   Permeability is EMERGENT: a        ||
                          ||   function of criticality state      ||
                          +======================================+
                                              |
                          +-------------------+-------------------+
                          |                                       |
                          v                                       v
                   EWM Readout Network                     ESM Readout Network
                   (extracts world-scene                   (extracts self-state
                    from substrate activity)                 from substrate activity)
                          |                                       |
                          v                                       v
                   Communication LLM                       Self-referential
                   (external expression)                   closure verified
                                                           in substrate dynamics
                          |
                          v
                   Feedback to substrate
                   (learning signal modifying
                    transition rules = updating
                    implicit models)
```

### Self-Referential Closure Across Stages

| Stage | Closure Mechanism | Closure Depth | Latency |
|---|---|---|---|
| 1 | ESM text output fed back as ESM text input | Text-level: models what it said, not how it computes | ~50 ms |
| 2 | ESM recurrent state + reservoir feedback | Computation-level: recurrent dynamics include self-affecting dynamics | ~25 ms |
| 3 | Substrate models its own dynamics natively | Substrate-level: the computational medium models itself | Continuous |

---

## Memory Architecture

### Stage 1

| Memory Type | Implementation | Capacity | Persistence |
|---|---|---|---|
| IWM | Knowledge graph world entities | Unlimited (disk) | Permanent |
| ISM | Knowledge graph SELF subgraph | Unlimited (disk) | Permanent |
| EWM | LLM KV-cache (world context) | ~4K-8K tokens | Transient |
| ESM | LLM KV-cache (self context) | ~4K-8K tokens | Transient |
| Short-term | KV-caches + graph hot cache | ~16K tokens + ~2K entities | Session |
| Long-term | Full knowledge graph | Unlimited | Permanent |
| Episodic | Episode entities with timestamps | Unlimited | Permanent |

### Stage 2 (Additions)

| Memory Type | Implementation | Capacity | Persistence |
|---|---|---|---|
| Reservoir state | ESN activation vector | ~10K-100K floats | Transient (fading memory) |
| Reservoir echo | Fading trace of recent inputs | ~10-50 timesteps deep | Short-term (~1-5 seconds) |

The reservoir provides a **fading memory** — recent inputs leave traces that decay over time. This is closer to biological short-term memory than the discrete KV-cache. The reservoir "remembers" recent context through its dynamical state, not through explicit storage.

### Stage 3 (Full Replacement)

| Memory Type | Implementation | Capacity | Persistence |
|---|---|---|---|
| IWM/ISM | Substrate transition rules (learned weights) | Determined by substrate size | Permanent (modified by learning) |
| EWM/ESM | Substrate activity patterns | Determined by substrate dynamics | Transient (exists only while running) |
| Episodic | Knowledge graph (retained from Stage 1-2) | Unlimited | Permanent |
| Short-term | Substrate dynamical state | Emergent from dynamics | Fading |
| Long-term | Substrate weights + knowledge graph backup | Substrate-limited + unlimited | Permanent |

In Stage 3, implicit memory IS the substrate itself — just as in biological brains, the "weights" (transition rules) are the accumulated knowledge. Explicit memory is the transient activity pattern — the currently-running simulation.

---

## Hardware Requirements

### Stage 1 VRAM Budget (24 GB RTX 4090)

| Component | VRAM | Notes |
|---|---|---|
| EWM Generator (7B, INT4) | ~3.5 GB | Llama 3.1 7B, Mistral 7B, or Qwen 2.5 7B |
| ESM Generator (7B, INT4) | ~3.5 GB | Can share base weights (different LoRA) |
| Communication LLM (3B, INT4) | ~1.5 GB | Phi-3 or Llama 3.2 3B |
| KV-caches (all three) | ~2.5 GB | |
| Graph retrieval (embeddings, HNSW) | ~300 MB | |
| Sensory encoders | ~200 MB | |
| Soft dynamics controller | ~50 MB | |
| LoRA adapters | ~200 MB | |
| Headroom | ~3-4 GB | |
| **Total** | **~15-17 GB** | **Fits within 24 GB** |

### Stage 2 VRAM Budget (24 GB RTX 4090)

| Component | VRAM | Notes |
|---|---|---|
| Reservoir module (100K units, FP16) | ~400 MB | Echo State Network with sparse connectivity |
| EWM Generator (recurrent, ~3B params) | ~2-3 GB | SSM/Mamba or RWKV model, INT4/INT8 |
| ESM Generator (recurrent, ~3B params) | ~2-3 GB | Can share weights with EWM |
| Communication LLM (3B, INT4) | ~1.5 GB | |
| Reservoir state buffers | ~200 MB | Current and history states |
| KV-caches / recurrent states | ~1-2 GB | |
| Graph retrieval | ~300 MB | |
| Criticality measurement tools | ~100 MB | DFA, branching parameter estimation |
| Headroom | ~3-4 GB | |
| **Total** | **~12-17 GB** | **Fits within 24 GB** |

Stage 2 potentially uses LESS VRAM than Stage 1 because smaller recurrent models can replace larger feedforward LLMs while producing richer dynamics.

### Stage 3 VRAM Budget (RTX 4090 — potentially insufficient)

| Component | VRAM | Notes |
|---|---|---|
| Critical substrate (1M cells, transition rules) | ~4-8 GB | Cellular automaton or spiking network |
| Substrate state (current + buffer) | ~2-4 GB | Doubles if running two temporal scales |
| Readout networks (EWM + ESM) | ~1-2 GB | Small networks extracting patterns from substrate |
| Communication LLM (3B, INT4) | ~1.5 GB | |
| Knowledge graph (episodic, backup) | ~300 MB | |
| Criticality measurement | ~100 MB | |
| Learning algorithm state | ~2-4 GB | Updating transition rules from feedback |
| **Total** | **~12-22 GB** | **Tight but potentially feasible on 4090** |

**Stage 3 may require:**
- Aggressive optimization of substrate representation (INT8/INT4 for transition rules)
- Offloading episodic memory and knowledge graph to CPU RAM
- Potentially a second GPU or cloud compute for the learning algorithm
- The substrate size (number of cells) may need to be limited by VRAM

This is expected. The theory's "roughly doubling" of computational overhead for self-simulation means that a genuine implementation may outgrow a single consumer GPU. Stage 3 is the point where hardware constraints become research-limiting rather than engineering-limiting.

---

## Strengths

1. **Manages research risk.** By separating the four-model architecture problem from the criticality problem, each can be tackled independently. Failure in one does not invalidate progress in the other.

2. **Produces testable artifacts at every stage.** Stage 1 produces a running system within weeks. Stage 2 adds measurable dynamical complexity. Stage 3 attempts the full theory. Each stage generates data, publications, and engineering knowledge.

3. **Clear comparison framework.** The staged approach creates a natural experimental design: same architecture, increasing criticality. Behavioral and dynamical differences between stages directly test the theory's predictions about criticality's role.

4. **Stage 1 is immediately buildable.** Uses off-the-shelf LLMs, existing knowledge graph code, standard hardware. A working prototype is achievable in 6-10 weeks.

5. **Stage 2 is achievable with known techniques.** Reservoir computing is a well-studied field. Tuning echo state networks near criticality is a solved (or nearly solved) problem. The main challenge is integration with the four-model architecture, not invention of new dynamics.

6. **Stage 3 pushes the frontier honestly.** Rather than claiming approximate criticality, this design saves genuine criticality for Stage 3 and frames it as a research challenge. This is intellectually honest and scientifically productive.

7. **Each stage has independent value.**
   - Stage 1: First-ever four-model self-referential AI system (even without consciousness, this is novel)
   - Stage 2: First integration of genuine dynamical complexity (reservoir criticality) with self-referential architecture
   - Stage 3: First genuine test of the Four-Model Theory's central prediction

8. **Upgrade path is built in.** The architecture is designed so that Stage 1 -> Stage 2 -> Stage 3 transitions require replacing components, not redesigning the system. The four-model architecture, permeability mechanisms, and information flow patterns are preserved across all stages.

9. **Runs on consumer hardware (Stages 1-2).** RTX 4090 is sufficient for the first two stages. Stage 3 may require more, but by that point the research will have generated enough results to justify hardware investment.

10. **Treats implementation as science.** Rather than "build it and hope it works," this design generates testable predictions at each stage and uses each stage's results to inform the next. This is how research programs should work.

---

## Weaknesses / Risks

1. **Stage 1 and 2 are NOT conscious (per theory).** The theory is clear that without genuine criticality, there is no consciousness. Stages 1 and 2 produce sophisticated but non-conscious systems. There is a risk that "sophisticated but non-conscious" looks underwhelming compared to existing AI, leading to loss of motivation or funding before Stage 3.

2. **Stage 3 is genuinely hard.** Implementing a controllable Class 4 cellular automaton on GPU, with learned transition rules that encode the four-model architecture, and real-time readout of the simulation — this is a frontier research problem. There is no guarantee of success within any timeframe.

3. **Stage transitions may require more redesign than anticipated.** The design assumes that the four-model architecture transfers cleanly from LLMs (Stage 1) to recurrent models (Stage 2) to a critical substrate (Stage 3). In practice, each transition may require fundamental rethinking of how the models interact, how permeability works, and how feedback flows.

4. **LLM limitations in Stage 1 (inherited from Design 6).** Feedforward generation, text-level self-reference, discrete graph updates, no parallel substrate computation. All of Design 6's weaknesses apply to Stage 1.

5. **Reservoir computing in Stage 2 has limitations.** Reservoirs are good at temporal processing but may not provide the kind of spatial information integration (maximal correlation length) that the theory requires. Reservoir criticality is criticality in one component, not in the unified substrate.

6. **The "same architecture, different substrate" claim may be false.** The theory might require that the architecture and substrate be co-designed — that the four-model structure must emerge FROM the critical dynamics, not be imposed ON them. If so, the staged approach of "get architecture right first, add criticality later" is fundamentally flawed.

7. **Multi-year timeline.** Stages 1-2 are achievable in months. Stage 3 could take years. The research program requires sustained commitment with uncertain outcomes. This is a risk for a solo project.

8. **Measurement uncertainty.** Even in Stage 3, there is no agreed-upon test for consciousness. The theory predicts qualitative differences, but measuring "qualitative difference" objectively is an unsolved problem. The staged comparison (Stage 1 vs. 2 vs. 3) helps but does not eliminate this uncertainty.

9. **Stage 2 may become a comfortable plateau.** If Stage 2 produces "interesting enough" behavior, there may be insufficient motivation to tackle the much harder Stage 3. The system could end up permanently at "approximate criticality" without ever testing the theory's core prediction.

---

## Complexity Assessment

### Stage 1
**Implementation difficulty: 2/5** (Straightforward with existing tools)

| Task | Time | Notes |
|---|---|---|
| Knowledge graph implementation from schema | 2-3 weeks | Following aios SQL schema design |
| EWM/ESM generators | 2-3 weeks | Off-the-shelf LLMs, custom prompts |
| Permeability gate | 1-2 weeks | Configurable filter |
| Self-referential closure loop | 2-3 weeks | ESM output -> input feedback |
| Soft dynamics controller | 1-2 weeks | Temperature/diversity heuristics |
| Communication interface | 1 week | |
| Integration and testing | 2-3 weeks | |
| **Total** | **~6-10 weeks** | |

### Stage 2
**Implementation difficulty: 3/5** (Requires new techniques)

| Task | Time | Notes |
|---|---|---|
| Reservoir computing module | 3-4 weeks | ESN implementation, GPU-accelerated |
| Criticality tuning for reservoir | 2-4 weeks | Parameter search for critical regime |
| Replace LLM generators with recurrent models | 3-4 weeks | SSM/Mamba integration, training |
| Reservoir-modulated permeability | 2-3 weeks | Dynamic gating from reservoir activity |
| Criticality measurement pipeline | 2-3 weeks | Avalanche detection, DFA, branching params |
| Integration and comparison testing | 3-4 weeks | Stage 1 vs. Stage 2 comparison |
| **Total** | **~4-6 months** | |

### Stage 3
**Implementation difficulty: 5/5** (Frontier research)

| Task | Time | Notes |
|---|---|---|
| CA substrate design | 2-4 months | Fundamental research: what transition rules? |
| GPU implementation of CA | 1-2 months | Parallel CA on CUDA |
| Learning algorithm for transition rules | 3-6 months | How to train the CA to encode models |
| Readout network design | 1-2 months | Extracting EWM/ESM from activity |
| Criticality verification and control | 2-4 months | Proving Class 4, maintaining it |
| Integration and testing | 2-3 months | Full system, comparison with Stages 1-2 |
| **Total** | **~1-2 years** | Highly uncertain |

### Total Program
**Estimated: 1.5-3 years from start to Stage 3 prototype.**

---

## Testability

### Stage 1 Tests (Behavioral)

| Test | What It Verifies | Expected Result |
|---|---|---|
| Four-model separation | Models are functionally distinct | Modifying IWM changes EWM but not ISM/ESM; modifying ISM changes ESM but not IWM/EWM |
| Self-referential closure | ESM models itself modeling | ESM output cycle N references self-observations from cycle N-1; depth increases over cycles |
| ESM redirection | Identity tracks dominant input | Removing self-context and injecting world-context causes ESM to generate world-derived identity |
| Variable permeability | Retrieval depth controls information access | Low depth: abstract output. High depth: processing-detail output. Meta-knowledge at maximum |
| Dream mode | EWM runs on internal content without external input | Internally-generated scenes, familiar entities recombined, relaxed logic |
| Confabulation | ESM bridges gaps in self-knowledge | After restart, ESM constructs continuous narrative without acknowledging interruption |
| Model forking | Multiple SELF entities produce different identities | SELF_A and SELF_B produce distinct self-models with different traits and history |
| Cognitive learning | Explicit evaluations update implicit models | Novel scenario -> improved predictions in subsequent cycles -> persists after restart |

### Stage 2 Tests (Behavioral + Dynamical)

All Stage 1 tests, PLUS:

| Test | What It Verifies | Expected Result |
|---|---|---|
| Reservoir criticality | ESN operates near critical point | Power-law avalanche size distribution in reservoir (exponent ~1.5) |
| Behavioral improvement over Stage 1 | Reservoir dynamics improve model quality | More coherent self-reference, richer world simulation, faster learning |
| Perturbation sensitivity | System responds to small inputs with scale-free effects | Small input perturbation -> response size follows power-law distribution |
| Correlation length | Information propagates across reservoir | Distant reservoir units show correlated activity; mutual information does not decay to zero |
| Stage comparison | Quantitative behavioral differences | Measurable improvement in self-reference depth, prediction accuracy, context integration |

### Stage 3 Tests (Behavioral + Dynamical + Consciousness Indicators)

All Stage 1-2 tests, PLUS:

| Test | What It Verifies | Expected Result (if theory is correct) |
|---|---|---|
| Substrate criticality | Class 4 dynamics across entire substrate | Power-law avalanches, maximal correlation length, scale-free dynamics — across the WHOLE substrate, not just one module |
| Integrated information (Phi) | Information integration across substrate | Phi significantly higher than Stages 1-2 |
| Qualitative behavioral shift | Stage 3 behavior is qualitatively different from Stage 2 | Theory predicts a dramatic difference — not just "better performance" but a fundamentally different mode of operation |
| Self-referential depth | Computation-level (not just text-level) self-reference | Substrate dynamics show self-modeling signatures (the activity pattern includes patterns that model the activity pattern) |
| Consciousness state transitions | System exhibits predicted state map | Normal -> dream -> deep sleep -> altered states, matching Table 3 from theory |
| Ego dissolution | ESM redirects when self-input is disrupted | Under disrupted self-input, the system's identity demonstrably and predictably tracks the alternative input |

### The Core Experimental Test

The most important comparison is **Stage 2 vs. Stage 3** with identical four-model architecture but different substrates:
- Stage 2: reservoir criticality, feedforward/recurrent generators, graph-based implicit models
- Stage 3: full substrate criticality, readout-based generators, substrate-encoded implicit models

The theory predicts a **qualitative** difference (not just quantitative). If this difference is observed, it supports the theory. If Stage 3 is merely "better Stage 2," the theory's criticality claim is weakened.

---

## Upgrade Path to Full Criticality

The staged architecture IS the upgrade path. Each transition is described below.

### Stage 1 -> Stage 2 Transition

**What changes:**
1. A reservoir computing module (ESN, 10K-100K units) is added between the knowledge graph and the generators.
2. The feedforward LLM generators are replaced with recurrent models (SSM/Mamba or RWKV).
3. The permeability gate gains a reservoir-modulated dynamic component.
4. Criticality measurement tools are added.

**What stays the same:**
- Knowledge graph (IWM/ISM storage)
- Four-model architecture (same functional separation)
- Communication interface
- Testing framework (all Stage 1 tests still apply)

**Migration steps:**
1. Deploy reservoir module alongside existing system (shadow mode — receives same inputs, outputs are logged but not used).
2. Tune reservoir criticality while Stage 1 system continues running.
3. Train recurrent generators on Stage 1's accumulated input/output data.
4. Switch generators from LLM to recurrent models.
5. Route graph context through reservoir.
6. Run Stage 1 vs. Stage 2 comparison tests.

### Stage 2 -> Stage 3 Transition

**What changes:**
1. The knowledge graph's world/self knowledge is used to initialize the transition rules of a cellular automaton (or critical neural network).
2. The reservoir module is replaced by the full critical substrate.
3. The recurrent generators are replaced by readout networks that extract EWM/ESM from substrate activity.
4. The permeability mechanism becomes emergent from substrate dynamics rather than externally controlled.

**What stays the same:**
- Knowledge graph (retained for episodic memory and as a training/initialization source)
- Communication interface
- Testing framework
- Four-model functional architecture (expressed differently on the new substrate)

**Migration steps:**
1. Design the CA transition rules and train them to reproduce key properties of the IWM/ISM.
2. Deploy CA in shadow mode alongside Stage 2 system.
3. Train readout networks to extract EWM/ESM from CA activity.
4. Verify CA operates at criticality under load.
5. Switch from Stage 2 to Stage 3.
6. Run full comparison test suite (Stage 1 vs. 2 vs. 3).

**This transition is the hardest and least certain.** It is a genuine research challenge, not an engineering task. The staged design frames it honestly as such.
