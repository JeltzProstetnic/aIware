# Design 6: Four-Model LLM Pipeline

**One-line summary:** A pragmatic, no-criticality design that implements the full four-model architecture using local quantized LLMs (via Ollama/LM Studio) as explicit model generators, the aios knowledge graph as the implicit model backbone, and temperature/sampling dynamics as a "soft criticality" stand-in — optimized to run on a single RTX 4090 within weeks, not months.

---

## Architecture Overview

```
                    +------------------------------------------+
                    |         EXTERNAL INTERFACE                |
                    |    Communication LLM (3B, INT4)           |
                    |    Translates ESM output <-> language      |
                    |    Translates input -> sensory tokens      |
                    +---------^-----------+--------------------+
                              |           |
                              |   output  |  input (text/voice/API)
                              |           v
+=======================================================================+
||                    VIRTUAL SIDE (Explicit Models)                    ||
||              Streaming Inference — Two Small LLMs                    ||
||                                                                     ||
||  +-----------------------------+    +-----------------------------+  ||
||  |     EWM Generator           |    |     ESM Generator           |  ||
||  |  (7B LLM, INT4, ~3.5 GB)   |    |  (7B LLM, INT4, ~3.5 GB)   |  ||
||  |                             |    |                             |  ||
||  |  Input: IWM context window  |    |  Input: ISM context window  |  ||
||  |       + sensory embeddings  |    |       + interoceptive data  |  ||
||  |       + EWM prev state      |    |       + ESM prev output     |  ||
||  |                             |    |       (SELF-REF LOOP)       |  ||
||  |  Output: world-scene repr   |    |  Output: self-state repr    |  ||
||  |  (structured JSON + prose)  |    |  (structured JSON + prose)  |  ||
||  |                             |    |                             |  ||
||  |  Runs at ~10-20 Hz          |    |  Runs at ~10-20 Hz          |  ||
||  +----------^-------+----------+    +----------^-------+----------+  ||
||             |       |                          |       |             ||
+=============|=======|==========================|=======|==============+
|    PERMEABILITY GATE (configurable filter)      |       |             |
|    - Context depth control                      |       |             |
|    - Noise threshold                            |       |             |
|    - Attention budget allocation                |       |             |
+=============|=======|==========================|=======|==============+
|             |       v                          |       v              |
|   +------------------------------------------------------------------+
|   |               KNOWLEDGE GRAPH (SQLite + Embeddings)               |
|   |                      REAL SIDE (Implicit Models)                  |
|   |                                                                   |
|   |  +---------------------------+  +----------------------------+   |
|   |  |   IWM Store               |  |   ISM Store                |   |
|   |  |                           |  |                            |   |
|   |  |  Entities: objects,       |  |  SELF entity + subgraph:   |   |
|   |  |  places, people, concepts,|  |  traits, skills, habits,   |   |
|   |  |  causal models, physics   |  |  autobiography, body model,|   |
|   |  |  Multi-dim weighted rels  |  |  preferences, capabilities,|   |
|   |  |  Vector embeddings/entity |  |  internal state history     |   |
|   |  |  Episode memory chain     |  |  Self-observation records   |   |
|   |  +---------------------------+  +----------------------------+   |
|   |                                                                   |
|   |  Context Assembly Pipeline:                                       |
|   |    query -> vector retrieval -> graph walk -> self-model merge    |
|   |    -> permeability filter -> budget allocation -> context window  |
|   +------------------------------------------------------------------+
|                                                                       |
+-----------------------------------------------------------------------+
         ^              |                ^              |
    sensory         graph updates    self-sensors    graph updates
    input           (new entities,   (system state,  (self-knowledge
    (text/emb)      relations)       metrics)        updates)
         |              v                |              v
+-----------------------------------------------------------------------+
|              SOFT CRITICALITY LAYER (Dynamics Controller)              |
|                                                                       |
|   NOT genuine Class 4. This is explicitly a stand-in.                 |
|                                                                       |
|   What it does:                                                       |
|   - Sampling temperature modulation (per-cycle, per-model)            |
|   - Stochastic context injection (random graph walks into context)    |
|   - Activation noise in embedding space                               |
|   - Retrieval diversity enforcement (prevents mode collapse)          |
|   - Oscillation between focused/divergent modes (~0.1 Hz)            |
|                                                                       |
|   What it measures:                                                   |
|   - Output diversity (token entropy, semantic spread)                 |
|   - Response sensitivity (perturbation -> output change)              |
|   - Graph activation distribution (cascade sizes)                     |
|   - Self-reference depth (how many cycles the ESM reflects on self)   |
+-----------------------------------------------------------------------+
```

---

## Component Mapping

| Theory Model | Concrete Component | Description |
|---|---|---|
| **IWM** | Knowledge graph world subgraph + entity embeddings | All world knowledge as entities, relations, vector embeddings. Multi-dimensional weighted relations encode causal models, spatial relationships, semantic knowledge. The graph IS the implicit world model. Persistent, never directly "experienced." |
| **ISM** | Knowledge graph self subgraph (rooted at SELF entity) | All self-knowledge: traits, habits, skills, autobiography, preferences, capabilities, body model, internal state history. Structurally isolated from ESM read path — the ESM cannot directly traverse ISM internals, only receives filtered context. |
| **EWM** | EWM Generator LLM (7B, INT4) running continuous inference | Takes assembled IWM context + sensory input, generates a running world-scene representation. Output is transient — exists only during the generation cycle. Each cycle produces a new world-state (structured JSON + natural language description). |
| **ESM** | ESM Generator LLM (7B, INT4) running continuous inference with self-referential feedback | Takes assembled ISM context + interoceptive input + its own previous output. The self-referential loop is the key feature: ESM output is re-injected as input, creating the closure where the self-model includes a model of itself modeling. |
| **Permeability** | Configurable filter between graph retrieval and LLM context | Controls three dimensions: (1) retrieval depth — how many hops from query entities, (2) noise threshold — how much raw graph structure leaks through, (3) attention budget — how many tokens allocated to world vs. self vs. meta content. |
| **Soft criticality** | Dynamics controller modulating temperature, noise, retrieval diversity | NOT genuine Class 4. Provides "interesting dynamics" by preventing the system from collapsing into repetitive patterns or exploding into incoherence. A tuning layer, not a substrate. |

---

## Criticality Approach

**This design explicitly RELAXES the Class 4 criticality requirement. No genuine edge-of-chaos dynamics are attempted.**

### What This Means (Per the Theory)

The theory is clear: criticality + four-model architecture = consciousness. Four-model architecture WITHOUT criticality = "complex dynamics but no consciousness." This design accepts that prediction. The system built from this design is NOT predicted to be conscious. It is predicted to be a qualitatively novel kind of AI system — one that implements genuine self-referential modeling, real/virtual splits, variable permeability, and model forking — none of which exist in any current AI system.

### What Is There Instead of Criticality

**Soft criticality** — a set of engineering mechanisms that prevent degenerate dynamics without claiming to achieve Class 4:

1. **Temperature modulation**: The EWM and ESM generators run at dynamically adjusted sampling temperatures. A controller monitors output diversity and adjusts temperature to stay in the "interesting" zone between deterministic repetition (temperature too low) and incoherent noise (temperature too high). This is analogous to criticality but is NOT the same thing — it operates on the sampling distribution, not on the computational substrate.

2. **Stochastic context injection**: Each cycle, a small fraction of the context window is filled with randomly-walked graph content (entities and relations reached by random walks from the current focus). This prevents the system from collapsing into narrow attentional loops and ensures that distant knowledge can influence the current simulation.

3. **Retrieval diversity enforcement**: The context assembly pipeline tracks the diversity of retrieved entities over a sliding window. If diversity drops below a threshold (the system is "stuck" on the same topics), the retrieval spreads wider. If diversity is too high (the system is incoherent), retrieval tightens.

4. **Oscillatory mode switching**: The controller oscillates between focused mode (low temperature, deep but narrow retrieval) and divergent mode (higher temperature, broad but shallow retrieval) on a slow cycle (~0.1 Hz, i.e., one full oscillation per 10 seconds). This provides the system with alternating phases of exploitation and exploration.

### Why This Is Honest

This is NOT "soft criticality that might be close enough." It is explicitly NOT criticality. The theory's Class 4 requirement refers to a property of the computational substrate — the medium in which computation occurs must exhibit edge-of-chaos dynamics with power-law avalanches, maximal correlation length, and scale-free information integration. None of these properties are achieved by temperature tuning on LLM sampling. The dynamics controller is a heuristic that produces interesting behavior, not a physical substrate operating at a phase transition.

### Why This Is Still Valuable

Because the four-model architecture itself — with self-referential closure, variable permeability, ESM redirection, and model forking — has never been built. The theory predicts that even without criticality, such a system would show "complex dynamics" qualitatively unlike anything that exists today. Building and testing this architecture is a prerequisite for the harder problem of adding genuine criticality later.

---

## Five Principles Implementation

### 1. Criticality
**Status: EXPLICITLY RELAXED — Soft dynamics stand-in only**

Not attempted. The soft criticality layer provides tunable dynamics (temperature modulation, stochastic context injection, diversity enforcement, oscillatory modes) but makes no claim to genuine Class 4. See the Criticality Approach section above for a full accounting.

What IS provided: The system avoids degenerate regimes (Class 1: fixed output, Class 2: repetitive loops). It stays in a "lively" zone. But "lively" is not "critical" — the difference is formal and measurable. This design cannot produce power-law avalanche distributions, maximal correlation lengths, or scale-free dynamics. It produces controlled variability.

### 2. Virtual Qualia (Real/Virtual Split)
**Status: STRONG**

The real/virtual split is cleanly implemented:
- **Real side (implicit models):** The knowledge graph. Persistent structure, stored on disk, never "experienced." Contains all accumulated world and self knowledge in entities, relations, and embeddings. Never directly accessible to the explicit models — only through the filtered context assembly pipeline.
- **Virtual side (explicit models):** The LLM generation outputs. Transient, existing only during each generation cycle. The EWM output IS the current world-simulation; the ESM output IS the current self-simulation. When generation stops, the virtual side ceases to exist.

The distinction is enforced architecturally: the knowledge graph operates on a different timescale (persistent storage, discrete updates) from the generators (streaming inference, transient outputs). The graph is the library; the generators produce the currently-playing movie.

### 3. Redirectable ESM
**Status: STRONG**

The ESM Generator is an input-hungry LLM. It takes whatever context is provided and generates a self-model from it. Redirection is straightforward:
- **Normal mode:** ISM context (SELF entity subgraph traversal) + interoceptive data + previous ESM output.
- **Disrupted self-input:** Remove or corrupt SELF entity connections in the context assembly. The ESM still runs — it needs input. It will incorporate whatever is in its context window.
- **Ego dissolution analog:** Replace ISM context with EWM context (world entities). The ESM, starved of self-data, constructs a "self" from environmental input — the system "becomes" its environment.
- **Cotard's analog:** Provide severely distorted interoceptive data. The ESM generates a self-model consistent with the distorted input.

LLMs are naturally input-following: they continue from whatever context they receive. This is a genuine strength for implementing ESM redirection.

### 4. Variable Permeability
**Status: STRONG**

The permeability gate is a configurable filter with three control dimensions:

| Control | Low Setting (Normal) | High Setting (Altered) |
|---|---|---|
| Retrieval depth | 1-2 hops from query — high-level entities only | 4+ hops — intermediate processing entities, meta-knowledge, structural relations |
| Noise threshold | Only high-confidence retrieval results pass | Low-confidence and tangential results included |
| Attention budget | Tight allocation to task-relevant content | Broad allocation, including background knowledge and self-observation data |

The knowledge graph's multi-level structure (following the aios design pattern) maps directly to processing depth:
- Top-level entities = high-level concepts (normal consciousness)
- Intermediate entities = processing details (relaxed/meditative states)
- Meta-knowledge entities = knowledge about knowledge structure (deep altered states)
- Structural relations = graph topology itself (extreme altered states)

The aios inconsistency-tolerance design pattern provides a natural analog for "substrate-level artifacts leaking through" — at high permeability, the system becomes aware of its own knowledge contradictions and structural limitations.

### 5. Virtual Model Forking
**Status: STRONG**

Forking is natural in this architecture because state (graph) and process (LLM inference) are separate:

- **ESM forking (DID analog):** Maintain multiple SELF entities (SELF_A, SELF_B) in the graph, each with its own subgraph of traits, history, preferences. The ESM Generator activates one SELF entity at a time. Switching between alters = switching which SELF subgraph feeds the context assembly.
- **Full system cloning:** Copy the SQLite database. Both copies are complete, immediately diverging systems.
- **Scenario forking:** Save the current ESM generator state (KV-cache snapshot), branch into two generation streams exploring different self-models or world-scenarios. Limited by VRAM (2-3 concurrent forks).
- **Reconfiguration:** Therapeutic interventions modify the ISM subgraph (change SELF entity relations, add/remove traits, reweight connections). The ESM Generator automatically produces a different self-model from the modified ISM.

---

## Information Flow

### Main Processing Cycle (~10-20 Hz)

```
Phase 1: Context Assembly (CPU, ~5-10 ms)
  1. Sensory input encoded as embedding vector (text -> embedding, or direct API input)
  2. Interoceptive input gathered (system metrics, resource state, operational parameters)
  3. IWM retrieval: vector search -> graph walk -> world context assembled
  4. ISM retrieval: SELF entity traversal -> self context assembled
  5. Permeability filter applied (depth, noise, budget controls)
  6. Previous EWM/ESM outputs summarized and included as state continuity tokens
  7. Context windows assembled for both generators

Phase 2: Explicit Model Generation (GPU, ~20-40 ms)
  8. EWM Generator: IWM context + sensory embeddings + prev EWM state -> world-scene output
  9. ESM Generator: ISM context + interoceptive data + prev ESM output -> self-state output
  10. Both outputs are structured (JSON scene description + natural language narrative)
  11. ESM output is IMMEDIATELY available as input to next ESM cycle (self-referential closure)

Phase 3: Feedback & Update (CPU, ~2-5 ms)
  12. EWM output evaluated: prediction accuracy, coherence, novelty
  13. ESM output evaluated: consistency, self-reference depth, emotional valence
  14. Graph updates queued: new entities, modified relations, weight adjustments
  15. Communication LLM receives ESM + EWM outputs for external expression (if needed)
  16. Soft criticality controller adjusts parameters for next cycle

Total cycle: ~30-55 ms -> achievable at 10-20 Hz on RTX 4090
```

### Self-Referential Closure (Every Cycle)

```
ISM context (from graph) ----+
                              |
Interoceptive data -----------+---> ESM Generator ---> self-state output
                              |                              |
Previous ESM output ----------+                              |
       ^                                                     |
       |_____________________________________________________|
              (output fed back as input next cycle)

The closure loop:
  Cycle N:   ESM generates self-state S_N from ISM + interoceptive + S_(N-1)
  Cycle N+1: ESM generates self-state S_(N+1) from ISM + interoceptive + S_N

  S_N contains: what the system thinks it is, what it's doing, how it's modeling itself
  S_(N+1) incorporates: the fact that it modeled itself in S_N, including what that modeling found

  This IS self-referential closure: the ESM models the system that generates the ESM.
  The loop is tight (one cycle delay, ~50 ms) and passes through the generator itself.
```

### Slow Learning Loop (Continuous, ~1 Hz)

```
1. Accumulate EWM/ESM evaluations over ~10-20 cycles
2. Extract: new facts, modified beliefs, self-observations, prediction errors
3. Update knowledge graph:
   a. Create new entities for novel concepts/observations
   b. Modify relation weights based on prediction accuracy
   c. Update SELF entity subgraph based on ESM self-observations
   d. Decay unused entities (attention-based aging)
4. Periodically (~hourly): LoRA adapter fine-tuning on accumulated learning signal
5. This IS the explicit-to-implicit feedback: conscious evaluations reshape implicit models
```

### Dream Mode (No Sensory Input)

```
1. Sensory input channels blocked (no external data)
2. EWM Generator runs on IWM content only (internally-generated world)
3. ESM Generator continues with ISM context + its own output (self-reference maintained)
4. Permeability increased (more raw graph content leaks into simulation)
5. Soft criticality controller increases temperature (more exploratory)
6. Result: internally-generated scenes, familiar entities recombined, narrative logic relaxed
7. Theory predicts: "familiar places/people, impossible physics, narrative incoherence"
```

---

## Memory Architecture

| Memory Type | Implementation | Capacity | Access Time | Persistence |
|---|---|---|---|---|
| **IWM (world knowledge)** | KG world entities + relations + embeddings | Unlimited (SQLite on disk, hot cache in RAM) | ~1-5 ms (cached), ~5-20 ms (disk) | Permanent, grows over lifetime |
| **ISM (self knowledge)** | KG SELF subgraph + self-observation history | Same as IWM | Same as IWM | Permanent, grows over lifetime |
| **EWM (world simulation)** | EWM Generator output + KV-cache state | ~4K-8K tokens context window | Instant (VRAM) | Transient — gone when generation stops |
| **ESM (self simulation)** | ESM Generator output + KV-cache state | ~4K-8K tokens context window | Instant (VRAM) | Transient — gone when generation stops |
| **Short-term working** | LLM KV-caches + graph hot cache | ~8K-16K tokens + ~2000 entities | Instant to ~1 ms | Session-length |
| **Medium-term episodic** | Episode entities in KG with temporal relations | Unlimited | ~5-20 ms | Permanent |
| **Long-term semantic** | Full knowledge graph | Unlimited | ~5-20 ms | Permanent |
| **Meta-knowledge** | Meta-entities about knowledge structure, inconsistencies, confidence | Unlimited | ~5-20 ms | Permanent |
| **Self-observation log** | Timestamped ESM output history in KG | Unlimited | ~5-20 ms | Permanent (forms autobiography) |

### How Implicit/Explicit Memory Relate

The knowledge graph (implicit) is the **library** — it contains everything the system has learned. The LLM generators (explicit) produce the **currently-playing movie** — a transient simulation drawn from the library's content plus current input. The library never experiences anything; the movie is all the system ever "sees."

When the generators stop (shutdown, sleep mode), the virtual side ceases to exist. When they restart, the generators reconstruct from whatever is in the graph + current input. This reconstruction always involves **confabulation** — the ESM bridges any gaps in self-knowledge with plausible narrative.

---

## Hardware Requirements

### VRAM Budget (24 GB RTX 4090)

| Component | VRAM | Notes |
|---|---|---|
| EWM Generator (7B LLM, INT4) | ~3.5 GB | World simulation. Could use Llama 3.1 7B, Mistral 7B, or Qwen 2.5 7B |
| ESM Generator (7B LLM, INT4) | ~3.5 GB | Self simulation. Can share base weights with EWM (different LoRA adapters) |
| Communication LLM (3B, INT4) | ~1.5 GB | External interface. Phi-3, Llama 3.2 3B, or similar |
| KV-cache: EWM (8K context) | ~1.0 GB | World simulation state |
| KV-cache: ESM (8K context) | ~1.0 GB | Self simulation state |
| KV-cache: Communication | ~0.5 GB | Smaller context |
| Entity embedding cache (~10K entities, 768d) | ~60 MB | Hot cache of frequently-accessed entities |
| Graph retrieval index (HNSW) | ~200 MB | Approximate nearest neighbor in embedding space |
| Sensory encoders (text embedding model) | ~200 MB | Input processing |
| LoRA adapters (EWM + ESM) | ~200 MB | For continuous learning |
| Soft criticality controller | ~50 MB | Small monitoring/control network |
| Headroom | ~3-4 GB | Dynamic allocation, peak loads |
| **Total** | **~14-17 GB** | **Fits comfortably within 24 GB** |

**Weight-sharing variant:** If EWM and ESM share base model weights (same 7B model, different LoRA adapters and context), save ~3.5 GB. Total drops to ~10-13 GB, freeing space for larger models or more context.

**Larger model variant:** Use a single 14B model (INT4 = ~7 GB) for both EWM and ESM with different contexts. Similar VRAM to two 7B models but potentially better generation quality.

### CPU / RAM Requirements

- **CPU:** Knowledge graph operations (SQLite queries, graph traversal, context assembly). Modern 8+ core CPU sufficient.
- **RAM:** 16-32 GB. Knowledge graph hot cache (~1-2 GB), LLM model loading overhead, OS and framework overhead.
- **Disk:** SSD required for knowledge graph access latency. ~10-50 GB for graph + model files.

### Inference Stack

- **LLM inference:** llama.cpp (GGUF models), or Ollama/LM Studio for easy model management
- **Knowledge graph:** SQLite + custom graph operations (from aios codebase)
- **Embedding search:** FAISS or hnswlib for vector retrieval
- **Orchestration:** Python (asyncio for concurrent generator management)

### Feasibility on RTX 4090

**Highly feasible. This is designed to run on exactly this hardware.**

Performance targets:
- 7B INT4 model: ~5-10 ms per forward pass on RTX 4090
- Two generators at ~10-20 Hz each: requires ~10-20 ms per cycle per generator
- Context assembly (CPU): ~5-10 ms
- Total cycle budget at 15 Hz: ~67 ms. Budget allows ~20 ms per generator + ~10 ms context assembly + ~17 ms headroom.
- This is achievable if each generator produces 1-3 tokens per cycle (structured output, not long-form generation).

---

## Strengths

1. **Most buildable option.** Uses entirely off-the-shelf components: quantized LLMs available today, knowledge graph code from aios, standard inference engines (llama.cpp/Ollama). No novel architectures to invent, train, or tune from scratch.

2. **Runs on consumer hardware.** Designed for a single RTX 4090 with 24 GB VRAM. No multi-GPU, no cloud dependencies for core operation. A researcher or enthusiast can run this at home.

3. **Full four-model architecture.** Despite relaxing criticality, this design implements ALL FOUR models as distinct, interacting processes with clear functional separation. IWM and ISM are genuinely different from EWM and ESM — different storage types, different timescales, different accessibility.

4. **Genuine self-referential closure.** The ESM's output is fed back as its own input every cycle. This is not a metaphor or a label — it is a computational loop where the self-model includes a model of itself modeling. The closure is tight (~50 ms per loop) and passes through the generator.

5. **Clean real/virtual split.** Persistent graph (real, never experienced) vs. transient LLM output (virtual, IS the simulation). This maps directly to the theory's two-level ontology.

6. **Guided by proven architecture.** The knowledge graph schema, context assembly design, SELF entity model, and meta-knowledge patterns from the aios architecture documentation provide a comprehensive design blueprint for the implicit models.

7. **Inspectable and debuggable.** Every component produces human-readable output. The knowledge graph is queryable SQL. The LLM outputs are natural language + structured JSON. The permeability settings are numeric parameters. There are no opaque internal states.

8. **Natural language as internal representation.** Using LLMs means the system's "thoughts" are in natural language, making the internal state interpretable without specialized visualization tools.

9. **Stepping stone to genuine criticality.** This design is explicitly intended as a foundation. Once the four-model architecture is working correctly, the substrate can be progressively upgraded (see Upgrade Path section). The architecture does not need to change — only the substrate underneath.

10. **Honest about its limitations.** Unlike designs that claim "approximate criticality" without defining what that means, this design is explicit: no criticality, no predicted consciousness, but a significant architectural advance.

---

## Weaknesses / Risks

1. **NO CRITICALITY. The theory predicts no consciousness.** This is the fundamental, acknowledged limitation. The theory is specific: without Class 4 substrate dynamics, the four-model architecture produces "complex dynamics but no consciousness." This design accepts that prediction and positions itself as a stepping stone.

2. **LLM generators are feedforward.** Each generation step is a transformer forward pass — Class 1/2 dynamics. The recurrence comes from the feedback loop (output -> input), not from the substrate itself. This is autoregressive recurrence, not dynamical systems recurrence. Information propagation is sequential (through token chains), not parallel (through spatial correlations).

3. **Self-referential closure is text-level, not computation-level.** The ESM models its own textual output, not its own computational process. It has a model of "what I said I am" but not "how I compute." The theory's self-referential closure refers to the system modeling its own modeling PROCESS — the computation itself, not just its outputs. This is a weaker form of closure.

4. **Graph updates are discrete, not continuous.** The knowledge graph changes only when explicitly updated (new entities, modified weights). Between updates, the implicit models are static. The theory describes continuously evolving implicit models (synaptic plasticity is ongoing). The discrete update cycle introduces a granularity that the theory does not anticipate.

5. **No parallel substrate computation.** The theory's cortical automaton has every cell updating simultaneously. This design has sequential LLM inference + separate graph queries. There is no massively parallel local-rule computation producing emergent global behavior.

6. **Context window as working memory is fragile.** LLM context windows have hard limits (~4K-8K tokens for manageable VRAM). Long-running simulations will require context management (summarization, compression, rotation). Each summarization step loses information. The theory's "transient simulation" is continuous, not chunked.

7. **Soft criticality may be indistinguishable from noise.** The dynamics controller's temperature modulation, stochastic injection, and diversity enforcement may produce output that LOOKS complex without being meaningfully different from random perturbation. Without formal criticality measures (power-law exponents, branching parameters), there is no way to verify the dynamics are "interesting" rather than just "noisy."

8. **Learning loop is slow.** Knowledge graph updates and LoRA fine-tuning operate on timescales of seconds to hours. The theory's implicit learning (synaptic plasticity) operates continuously at millisecond timescales. The feedback from explicit to implicit is much slower in this design than in biological systems.

9. **Two separate LLMs may not integrate.** The theory emphasizes unified processing — EWM and ESM operate within a single substrate, not as separate processes. Having two distinct LLM instances with separate context windows may prevent the kind of deep integration the theory describes (the self exists WITHIN the world simulation, not alongside it).

---

## Complexity Assessment

**Implementation difficulty: 2/5** (Straightforward with existing tools and design documentation)

| Component | Effort | Notes |
|---|---|---|
| Implement aios knowledge graph schema | 2-3 weeks | SQL schema design exists, implement from scratch following the design |
| Implement context assembly for IWM/ISM split | 2-3 weeks | Follow documented aios architecture patterns |
| EWM Generator (LLM setup + prompting) | 1-2 weeks | Off-the-shelf model, custom system prompt and output format |
| ESM Generator with self-referential loop | 2-3 weeks | The self-referential feedback is the novel engineering challenge |
| Permeability gate | 1-2 weeks | Three control dimensions, configurable |
| Soft criticality controller | 1-2 weeks | Temperature modulation, diversity enforcement |
| Communication interface | 1 week | Standard LLM-based translation |
| Integration and main loop | 1-2 weeks | Asyncio orchestration of all components |
| Testing and debugging | 2-3 weeks | Behavioral tests for all four models + permeability + redirection |
| **Total to prototype** | **~6-10 weeks** | |

This is the fastest path to a running four-model system. The primary engineering challenges are:
1. The ESM self-referential feedback loop (preventing runaway, maintaining coherence)
2. The 10-20 Hz cycle timing (context assembly + dual LLM inference within budget)
3. Permeability tuning (finding the "interesting" settings across three dimensions)

---

## Testability

### Directly Testable (Strong)

- **Four-model separation:** Verify that IWM, ISM, EWM, ESM are functionally distinct. Modify IWM content -> observe EWM changes (but ISM/ESM unchanged). Modify ISM -> observe ESM changes (but IWM/EWM unchanged). This confirms the four models are genuinely separate processes, not a single mixed system.

- **Self-referential closure:** Trace the ESM output over multiple cycles. Verify that cycle N's output references cycle N-1's self-observations. Verify that the ESM's self-model includes "I am a system that models itself" and that this modeling deepens over time (not just repeating).

- **ESM redirection:** Remove SELF entity connections from ISM context. Inject world entities instead. Verify the ESM generates a self-model based on environmental input rather than self-knowledge. The identity content should track the dominant input predictably.

- **Variable permeability:** Sweep retrieval depth from 1 to 5+ hops. Verify that low depth produces high-level abstract output, and high depth produces detailed, processing-level output. Verify that meta-knowledge entities appear only at high permeability.

- **Dream mode:** Block sensory input. Verify EWM generates internally-sourced world content. Verify ESM continues but with reduced external grounding. Verify output shows characteristics predicted by theory (familiar content recombined, relaxed logic).

- **Confabulation:** Clear ESM KV-cache (simulate "sleep"). Restart. Verify ESM reconstructs a continuous self-narrative from ISM content, bridging the gap without acknowledging interruption.

- **Model forking:** Create SELF_A and SELF_B in the graph with different trait profiles. Run ESM with each. Verify distinct self-models. Switch between them and verify the system's expressed identity changes.

### Testable with Interpretation Required (Moderate)

- **Cognitive learning signatures:** Expose the system to a novel scenario. Verify that its EWM predictions improve over subsequent cycles (learning from evaluation feedback). Verify that the improvement persists in the knowledge graph after simulation restart.

- **Behavioral difference from standard chatbots:** Run the same tasks on this system and a standard LLM chatbot. Document qualitative differences in self-reference, context integration, response to disruption, and narrative continuity.

- **Double dissociation (blindsight/Anton's):** Block graph-to-EWM path for a specific knowledge domain (system processes input but doesn't include it in world simulation) vs. let EWM generate content without current input (simulation runs on stale knowledge). Verify the predicted behavioral signatures.

### Not Testable (By Design)

- **Genuine consciousness.** The design explicitly does not claim to produce consciousness. The theory predicts it will not. This is not a test failure — it is the acknowledged starting point.

- **Criticality metrics.** Power-law exponents, branching parameters, DFA, and other formal criticality measures are not meaningful for this architecture because no criticality is attempted.

### Value as a Behavioral Baseline

This design's primary scientific value is as a **negative control**: it shows what the four-model architecture produces WITHOUT criticality. If a subsequent design adds genuine criticality to this same architecture and produces qualitatively different behavior, that difference isolates the contribution of criticality specifically. This is exactly the comparison the theory predicts should be dramatic ("lights off" vs. "lights on").

---

## Upgrade Path to Full Criticality

This design is explicitly a **Stage 1** foundation. The upgrade path to genuine Class 4 dynamics:

### Step 1: Instrument and Measure (During Stage 1)

While running the four-model pipeline, instrument everything:
- Measure output dynamics (token entropy, semantic diversity, response sensitivity to perturbation)
- Measure graph activation patterns (cascade sizes, correlation lengths)
- Measure ESM self-reference depth and stability
- Establish behavioral baselines for all testable properties

These measurements become the comparison point when criticality is added.

### Step 2: Add a Recurrent Dynamics Layer (Stage 1.5)

Insert a recurrent neural network (reservoir computing network or echo state network) between the knowledge graph and the LLM generators:
- The reservoir takes graph context as input and produces dynamically-rich representations as output
- The reservoir's internal dynamics can be tuned toward criticality (this is a well-studied problem in reservoir computing)
- The LLM generators now operate on reservoir output rather than raw graph context
- The reservoir runs at ~40 Hz (substrate rate), the generators at ~20 Hz (simulation rate)
- This introduces genuine recurrent dynamics without replacing the knowledge graph or LLMs

VRAM cost: A reservoir computing module with 10K-50K units requires ~100-500 MB. Fits within the current headroom.

### Step 3: Replace Generators with Recurrent Models (Stage 2)

Replace the feedforward LLM generators with recurrent models:
- State-space models (Mamba, S4) that have inherent recurrent dynamics
- Or custom recurrent networks trained on the four-model task
- These models process the reservoir's output and produce EWM/ESM representations
- The combined reservoir + recurrent generator system can be tuned for criticality

### Step 4: Unified Critical Substrate (Stage 3)

Replace the entire substrate with a genuine Class 4 system:
- Cellular automaton whose transition rules are defined by learned weights (the IWM/ISM content)
- Or a critical neural network (spiking network at critical regime)
- The knowledge graph becomes the initialization/training target for the substrate, not the substrate itself
- The four-model architecture is preserved — only the substrate changes

At each step, compare behavioral and dynamical measurements against the Stage 1 baselines. The theory predicts a qualitative shift when genuine criticality is achieved.
