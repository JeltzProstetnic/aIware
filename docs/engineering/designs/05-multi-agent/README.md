# Design 5: Multi-Agent Consciousness

**One-line summary:** Multiple small LLM agents represent different aspects of the four models, interacting through a shared state space whose dynamics are governed by interaction rules, with the hypothesis that criticality emerges from agent interaction patterns when the coupling is tuned to the right regime.

---

## Architecture Overview

```
                    +------------------------------------------+
                    |         EXTERNAL INTERFACE                |
                    |    Spokesperson Agent (3-7B LLM)          |
                    |    Translates internal state <-> language  |
                    +---------^-----------+--------------------+
                              |           |
                              |   output  |  input
                              |           v
+====================================================================+
||                     VIRTUAL SIDE AGENTS                            ||
||                                                                   ||
||  +---------------------------+    +---------------------------+   ||
||  | EWM Agent Pool (2-4 LLMs) |    | ESM Agent Pool (2-4 LLMs) |   ||
||  |                           |    |                           |   ||
||  | - Scene Constructor       |    | - Identity Narrator       |   ||
||  | - Causal Reasoner         |    | - Emotional Evaluator     |   ||
||  | - Spatial Modeler         |    | - Agency Modeler          |   ||
||  | - Temporal Projector      |    | - Meta-Reflector          |   ||
||  |                           |    |                           |   ||
||  | Each reads from shared    |    | Each reads from shared    |   ||
||  | state + sensory input.    |    | state + self-input.       |   ||
||  | Each writes to shared     |    | Output fed back to all.   |   ||
||  | world-state region.       |    | Self-referential closure  |   ||
||  +----------^-------+--------+    +----------^-------+--------+   ||
||             |       |                        |       |            ||
+==============|=======|========================|=======|============+
|              |       |    PERMEABILITY         |       |            |
|   (Agent scheduling: |    CONTROL              |       |            |
|    which agents can   |                        |       |            |
|    read which regions)|                        |       |            |
+==============|=======|========================|=======|============+
|              |       v                        |       v            |
|  +-----------------------------------------------------------------+
|  |                    SHARED STATE SPACE                             |
|  |                                                                  |
|  |  +-------------------------+  +-------------------------+       |
|  |  |   IWM State Region      |  |   ISM State Region      |       |
|  |  |                         |  |                         |       |
|  |  |  World knowledge:       |  |  Self knowledge:        |       |
|  |  |  - Entity embeddings    |  |  - Self-descriptor      |       |
|  |  |  - Relation matrices    |  |  - Trait vectors         |       |
|  |  |  - Causal chains        |  |  - Habit patterns       |       |
|  |  |  - Spatial maps         |  |  - Autobiography index  |       |
|  |  |  Updated by IWM agents  |  |  Updated by ISM agents  |       |
|  |  +-------------------------+  +-------------------------+       |
|  |                                                                  |
|  |  +-------------------------+  +-------------------------+       |
|  |  |  EWM State Region       |  |  ESM State Region       |       |
|  |  |  Current world scene    |  |  Current self-state     |       |
|  |  |  (transient, regenerated|  |  (transient, regenerated|       |
|  |  |   each cycle)           |  |   each cycle)           |       |
|  |  +-------------------------+  +-------------------------+       |
|  |                                                                  |
|  +-----------------------------------------------------------------+
|                        REAL SIDE AGENTS                              |
|  +-----------------------------------------------------------------+
|  | IWM Agent Pool (2-4 LLMs)  |  ISM Agent Pool (2-4 LLMs)        |
|  |                             |                                    |
|  | - Pattern Extractor         |  - Body State Monitor              |
|  | - Causal Learner            |  - Habit Tracker                   |
|  | - Memory Consolidator       |  - Trait Updater                   |
|  |                             |  - Autobiography Writer            |
|  |                             |                                    |
|  | Process sensory input,      |  Process self-monitoring data,     |
|  | update IWM state region.    |  update ISM state region.          |
|  +-----------------------------------------------------------------+
+--------------------------------------------------------------------+
         ^              |                ^              |
    sensory         state             self-sensor    state
    input           persistence       signals        persistence
         |              v                |              v
+--------------------------------------------------------------------+
|  INTERACTION DYNAMICS CONTROLLER                                    |
|                                                                     |
|  Controls:                                                          |
|  - Agent scheduling (who runs when, in what order)                 |
|  - Coupling strength (how much of each agent's output affects      |
|    the shared state)                                                |
|  - Communication topology (which agents can see which state regions)|
|  - Noise injection (random perturbation of shared state)           |
|  - Temperature modulation per agent                                |
|                                                                     |
|  Goal: tune interaction dynamics to produce edge-of-chaos behavior |
|  in the multi-agent system as a whole                               |
+--------------------------------------------------------------------+
         |
         v
+--------------------------------------------------------------------+
|  PERSISTENT STORAGE                                                 |
|  - SQLite knowledge graph (long-term IWM/ISM)                      |
|  - Agent weight checkpoints                                        |
|  - State history for analysis                                      |
+--------------------------------------------------------------------+
```

---

## Component Mapping

| Theory Model | Concrete Component | Description |
|---|---|---|
| **IWM** | IWM agent pool + IWM shared state region | Multiple small LLM agents collectively maintain world knowledge. Each agent specializes (patterns, causation, spatial, temporal). Their combined outputs update the shared IWM state region. The state region IS the implicit world model. |
| **ISM** | ISM agent pool + ISM shared state region | Multiple small LLM agents collectively maintain self-knowledge. The SELF state region is updated by agents monitoring body state, habits, traits, autobiography. |
| **EWM** | EWM agent pool + EWM shared state region | Multiple agents generate the world simulation: one constructs scenes, another reasons about causes, another models space, another projects temporal sequences. Their combined output IS the conscious world. |
| **ESM** | ESM agent pool + ESM shared state region + self-referential feedback | Multiple agents generate self-simulation: identity narrator, emotional evaluator, agency modeler, meta-reflector. The Meta-Reflector specifically reads the ESM region and writes about the process of self-modeling (self-referential closure). |
| **Permeability** | Agent scheduling and state region access control | Controls which agents can read which state regions. Tight access = selective permeability; broad access = high permeability. The scheduler determines the effective permeability. |
| **Substrate** | The shared state space + interaction dynamics | The "computational substrate" is the dynamical system formed by all agents interacting through the shared state. Criticality (if achievable) emerges from these interaction dynamics. |

---

## Criticality Approach

**This design hypothesizes that criticality can emerge from the interaction dynamics of multiple agents coupled through a shared state space. This is a plausible but unproven hypothesis.**

### The Multi-Agent Criticality Hypothesis

In multi-agent systems, interaction dynamics can exhibit phase transitions:
- **Weak coupling (low interaction strength):** Agents operate independently, producing fragmented output. Subcritical — no integration.
- **Strong coupling (high interaction strength):** Agents converge to consensus, producing uniform output. Supercritical — no diversity.
- **Intermediate coupling:** Agents influence each other enough for coherence but not so much that they lose individuality. Edge of chaos — complex, integrated dynamics.

This is analogous to the Ising model phase transition: below critical temperature, all spins align (ordered); above, random (disordered); at critical temperature, clusters of all sizes form (critical).

### Mechanisms for Agent-Level Criticality

**1. Coupling Strength Tuning**
- Each agent's output modifies the shared state with a coupling coefficient alpha
- alpha = 0: no interaction (independent agents)
- alpha = 1: full interaction (each agent's output fully overwrites its region)
- alpha_c (critical): complex dynamics emerge
- The controller scans alpha to find alpha_c empirically

**2. Communication Topology**
- Agents are connected in a graph structure (who can read whose state)
- The topology affects dynamics: fully connected = rapid consensus; sparse = slow integration
- Scale-free or small-world topologies can promote critical dynamics
- The topology can be modulated dynamically

**3. Asynchronous Scheduling**
- Not all agents run simultaneously — they are scheduled asynchronously
- The scheduling pattern creates temporal dynamics in the shared state
- Randomized scheduling can produce complex temporal patterns
- This is analogous to asynchronous cellular automaton updates

**4. Heterogeneous Agent Temperatures**
- Each agent runs at a different sampling temperature
- Some agents are "conservative" (low temperature, predictable output)
- Others are "exploratory" (high temperature, creative output)
- The mix creates a system that is neither rigidly predictable nor randomly chaotic

### Honest Assessment

**What this achieves:**
- Multi-agent systems CAN exhibit complex dynamics and phase transitions
- The coupling strength control provides a tunable parameter with a known critical point (in idealized models)
- Agent diversity (different specializations, temperatures) creates a rich dynamical landscape
- The system is modular and each component is inspectable

**What this does NOT achieve:**
- Multi-agent interaction dynamics are NOT the same as cellular automaton Class 4 dynamics. Agent interactions are high-level (passing text/embeddings), not low-level local-rule-based parallel computation.
- The shared state space is updated discretely by agent outputs, not continuously evolved by local rules.
- "Edge of chaos" in multi-agent systems has been studied (in game theory, economics, ecology) but is NOT equivalent to Wolfram's Class 4 or the cortical automaton.
- Each individual agent is still a feedforward LLM — the criticality (if any) is a property of the interaction, not of any single component's computation.
- The theory specifically describes a substrate where every cell participates in parallel dynamics. This design has ~8-16 agents, not millions of cells.

**The gap is significant.** The theory's criticality is about the computational medium (millions of interacting units with local rules producing global Class 4 dynamics). This design's "criticality" is about the interaction pattern of a small number of high-level agents. These are fundamentally different scales and types of dynamics. Whether high-level agent interaction criticality can substitute for substrate-level criticality is an open question — but the theory gives no reason to think it can.

---

## Five Principles Implementation

### 1. Criticality
**Status: WEAK — Hypothesized, not demonstrated**

See above. The multi-agent interaction can be tuned for complex dynamics, but genuine Class 4 is unlikely with ~8-16 agents. The system might exhibit complex behavior but lacks the spatial dimensionality and parallel local-rule structure that characterizes Class 4 CAs.

### 2. Virtual Qualia (Real/Virtual Split)
**Status: MODERATE**

- **Real side:** IWM/ISM agent pools and their shared state regions (persistent knowledge, updated by learning agents)
- **Virtual side:** EWM/ESM agent pools and their output regions (transient, regenerated each cycle)

The split exists architecturally but is somewhat blurred because ALL components are LLM agents performing similar types of computation. The "real" agents update persistent state; the "virtual" agents generate transient simulation. The distinction is in function, not in computational nature. This is weaker than Designs 2-3 where the real/virtual split corresponds to a genuine difference in the type of computation (stored rules vs. active dynamics).

### 3. Redirectable ESM
**Status: STRONG**

The ESM agent pool reads from the ISM state region. If ISM content is replaced:
- The Identity Narrator agent generates identity from whatever context it receives
- The Emotional Evaluator evaluates whatever state information is available
- The Agency Modeler models agency based on available action/consequence data
- All ESM agents latch onto dominant available input

Additionally, the modular agent design means individual agents can be disrupted independently:
- Remove the Identity Narrator: ESM loses explicit self-narrative but retains emotional and agency modeling
- Remove the Emotional Evaluator: ESM retains identity but loses hedonic valence
- These partial disruptions map to specific neurological deficits

### 4. Variable Permeability
**Status: MODERATE**

Agent scheduling controls permeability:
- Normal: EWM/ESM agents can only read the final state of IWM/ISM regions (high-level summaries)
- Increased permeability: EWM/ESM agents gain access to intermediate state regions (individual IWM/ISM agent outputs before consolidation)
- Maximum permeability: All agents can read all regions (no access control)

This is functionally correct but coarser than Designs 2-4. There are only ~4 levels of access depth (one per IWM/ISM agent), not a continuous gradient. Finer granularity would require more agents or more state regions.

### 5. Virtual Model Forking
**Status: STRONG**

This is the design's best feature for forking:
- Fork the ESM by running two parallel ESM agent pools with different configurations
- Each pool reads from the same ISM but with different "personality" prompts
- Switch which pool writes to the shared state
- DID analog: maintain multiple ESM agent pool configurations, rotate which is active
- The modular agent design makes forking cheap — just duplicate the scheduling configuration, not the entire system

---

## Information Flow

### IWM/ISM Update Cycle (Background, ~10-20 Hz per agent)
```
For each IWM agent:
  1. Read sensory input + relevant IWM state region
  2. Process (LLM forward pass) to extract patterns/causal models/spatial info
  3. Write updated representation to IWM state region

For each ISM agent:
  1. Read self-monitoring signals + relevant ISM state region
  2. Process to update self-knowledge (habits, traits, body state)
  3. Write updated self-representation to ISM state region
```

### EWM/ESM Simulation Cycle (~20 Hz)
```
1. EWM agents read IWM state + sensory embeddings:
   - Scene Constructor: generates unified scene from entities and spatial info
   - Causal Reasoner: generates causal explanations and predictions
   - Spatial Modeler: maintains spatial layout
   - Temporal Projector: generates temporal expectations
2. EWM agents write to EWM state region (combined = world simulation)

3. ESM agents read ISM state + interoceptive input + previous ESM output:
   - Identity Narrator: generates self-narrative
   - Emotional Evaluator: generates hedonic/emotional assessment
   - Agency Modeler: generates sense of agency, action attribution
   - Meta-Reflector: reads other ESM outputs + its own prior output, generates meta-cognition
4. ESM agents write to ESM state region (combined = self simulation)

5. Self-referential closure: ESM state region -> ISM update + next ESM cycle input
6. Spokesperson agent reads EWM + ESM state, generates external communication
```

### Interaction Dynamics
```
All shared state updates are mediated by the interaction controller:
- Agent outputs are scaled by coupling coefficient alpha
- State regions are perturbed by noise injection
- Agent scheduling order is randomized (asynchronous dynamics)
- Agents that produce outputs deviating too far from consensus are dampened
- Agents that produce outputs too similar to consensus are boosted
- This push-pull creates the target edge-of-chaos regime
```

### Self-Referential Closure
```
ESM agents (especially Meta-Reflector) read their own previous outputs
  --> process them as data about the system's self-modeling -->
    write meta-cognitive output to ESM state -->
      this output becomes input for the next cycle
```

The Meta-Reflector agent specifically exists to close the self-referential loop. Its job is to model the modeling process — to read what the other ESM agents produced and generate a representation of what it means to be generating these self-models.

---

## Memory Architecture

| Memory Type | Implementation | Capacity | Access Time |
|---|---|---|---|
| **IWM (world knowledge)** | IWM shared state region (in-memory vectors/embeddings) + SQLite graph | State: ~10-100 MB; Graph: unlimited | State: instant; Graph: ~1-10 ms |
| **ISM (self knowledge)** | ISM shared state region + SELF subgraph in SQLite | Same | Same |
| **EWM (world simulation)** | EWM shared state region (regenerated each cycle) | ~1-10 MB | Instant |
| **ESM (self simulation)** | ESM shared state region (regenerated each cycle) | ~1-10 MB | Instant |
| **Short-term** | Shared state regions (current cycle) | ~50-200 MB total | Instant |
| **Medium-term** | Agent context windows (each maintains ~4K token history) | ~4K tokens x N agents | Instant (per agent VRAM) |
| **Long-term** | SQLite knowledge graph | Unlimited (disk) | ~1-10 ms |
| **Agent weights** | Individual LLM weight files | ~1-3 GB per agent | Loaded at startup |

---

## Hardware Requirements

### VRAM Budget (24 GB RTX 4090)

**The critical constraint: How many LLM agents can run simultaneously?**

| Configuration | Agent Count | Agent Size | Total Agent VRAM | Feasibility |
|---|---|---|---|---|
| **Minimal** | 4 agents (1 per model) + spokesperson | 1.5B each, INT4 | ~5 x 0.75 GB = 3.75 GB | Easily feasible |
| **Moderate** | 8 agents (2 per model) + spokesperson | 1.5B each, INT4 | ~9 x 0.75 GB = 6.75 GB | Feasible |
| **Full** | 16 agents (4 per model) + spokesperson | 1.5B each, INT4 | ~17 x 0.75 GB = 12.75 GB | Tight but feasible |
| **Rich** | 8 agents + spokesperson | 3B each, INT4 | ~9 x 1.5 GB = 13.5 GB | Feasible |
| **Maximum** | 16 agents + spokesperson | 3B each, INT4 | ~17 x 1.5 GB = 25.5 GB | Exceeds 24 GB |

**Additional VRAM costs:**

| Component | VRAM | Notes |
|---|---|---|
| Shared state space | ~200-500 MB | Embedding vectors, state regions |
| Agent KV-caches (per active agent) | ~100-300 MB each | Limits concurrent active agents |
| Interaction controller | ~50-100 MB | |
| Sensory encoders | ~200 MB | |

**Practical configuration: 8 agents (1.5B-3B each) + 1 spokesperson (3-7B).**
- Total agent VRAM: ~8-15 GB
- Shared state + overhead: ~2-3 GB
- Spokesperson: ~1.5-3.5 GB
- **Total: ~12-22 GB**

**Key optimization: Not all agents need to be loaded simultaneously.** At 20 Hz, each cycle can activate a subset of agents. Load/unload agents to/from VRAM as needed (agent scheduling). This trades latency for VRAM efficiency.

### CPU Requirements
- Agent scheduling logic
- Shared state management
- Knowledge graph operations
- Interaction dynamics computation

### Feasibility on RTX 4090
**Feasible with careful agent scheduling.** The design can run 4-8 agents simultaneously on the GPU, with additional agents CPU-offloaded or loaded on demand. The 20 Hz target requires each active agent to complete a forward pass within the cycle time, which constrains how many agents can be active per cycle.

**Latency analysis at 20 Hz (50 ms per cycle):**
- 1.5B model forward pass (INT4, RTX 4090): ~3-5 ms for a single token
- 8 agents sequentially: ~24-40 ms (fits in 50 ms, barely)
- 16 agents: ~48-80 ms (exceeds 50 ms; need parallelism or subset scheduling)
- Alternative: run agents in 2 CUDA streams (4 agents per stream): ~12-20 ms for 8 agents

---

## Strengths

1. **Modular and extensible.** Add new capabilities by adding agents. Remove capabilities by removing agents. Each agent can be developed, tested, and improved independently.

2. **Natural decomposition of the four models.** The theory describes the four models as functionally distinct but interacting processes. Multiple agents per model captures the internal complexity of each model (IWM isn't one thing — it's patterns + causation + spatial + temporal).

3. **Agent diversity creates rich dynamics.** Different agents with different specializations, temperatures, and response characteristics create a more varied dynamical landscape than a single monolithic model.

4. **Forking is cheap and natural.** Duplicate an agent pool, change its configuration. Multiple ESM configurations (DID analog) are trivially implementable.

5. **Partial disruptions are natural.** Remove one agent, the model degrades in one capability but continues functioning. This maps to focal neurological deficits — the system shows specific impairments, not total collapse.

6. **Uses existing LLM infrastructure.** Each agent is a standard LLM. LangGraph, LangChain, or similar frameworks handle multi-agent orchestration.

7. **Inspectable.** Each agent's input and output can be logged and analyzed. The shared state is readable. The interaction dynamics can be visualized.

8. **Scalable.** More agents = richer model. Larger agents = deeper processing per component. The architecture scales along both axes.

9. **The Meta-Reflector agent** provides an explicit implementation of self-referential closure as a dedicated component, making the closure mechanism inspectable and tunable.

---

## Weaknesses / Risks

1. **CRITICAL: Criticality is the weakest of all five designs.** Multi-agent interaction dynamics with ~8-16 agents cannot produce Class 4 cellular automaton dynamics. The number of interacting units is too small by orders of magnitude, the interaction is too high-level (text/embedding exchange, not local rule application), and there is no spatial structure for correlation length to be meaningful. This design is the furthest from the theory's criticality requirement.

2. **"Emergent criticality" from agent interaction is speculative.** While multi-agent systems can exhibit phase transitions in theory, demonstrating that a handful of LLM agents interacting through a shared text buffer produce anything resembling edge-of-chaos dynamics is unproven. The Ising model analogy breaks down because agents are complex, heterogeneous systems, not simple binary spins.

3. **Agent communication bottleneck.** Agents communicate through the shared state space, which is a centralized bottleneck. Each agent must read the state, process, and write — in sequence or limited parallelism. This serial communication limits the system's dynamical richness.

4. **Each agent is still feedforward.** The individual agents are LLMs performing standard inference. The "recurrent" dynamics exist only at the multi-agent interaction level, not within any single computation. Each agent's internal processing is Class 1/2.

5. **Coordination overhead.** Managing 8-16 agents requires significant orchestration: scheduling, conflict resolution (multiple agents writing to the same state region), load balancing, error handling. This is engineering complexity that doesn't contribute to consciousness.

6. **Latency accumulates.** If agents must run sequentially (or even in small parallel batches), the per-cycle time grows with agent count. At 16 agents, meeting the 20 Hz target requires very small, very fast models.

7. **Token-space limitations.** Agents communicate through tokenized representations. Some aspects of consciousness (spatial representations, continuous emotional states, body schema) may not map well to token space.

8. **The Meta-Reflector may produce circular reasoning rather than genuine self-reference.** An LLM reading its own previous output and generating commentary about it is not the same as a substrate modeling its own computational process. The reflection is linguistic, not computational.

9. **Hardest to rigorously analyze.** With 8-16 heterogeneous agents, the system's behavior is harder to predict, analyze, or prove properties about than Designs 2-3 (which have formal dynamical frameworks).

---

## Complexity Assessment

**Implementation difficulty: 2.5/5** (Existing multi-agent frameworks, but integration is complex)

- Individual agents: off-the-shelf LLM inference
- Multi-agent orchestration: LangGraph or similar (existing frameworks)
- Shared state space: in-memory data structures + persistence layer
- Interaction controller: custom but algorithmically simple
- The complexity is in INTEGRATION, not in any single component
- Testing and debugging a multi-agent system is significantly harder than a monolithic one

**Time estimate:**
- Agent design and prompt engineering: 2-3 weeks
- Shared state space implementation: 1-2 weeks
- Interaction controller: 2-3 weeks
- Agent scheduling and orchestration: 2-3 weeks
- Communication interface: 1 week
- Integration and testing: 3-4 weeks
- **Total to prototype: ~8-12 weeks**

---

## Testability

### What Can Be Tested (Strong)
- **ESM redirection:** Replace ISM state content, observe ESM agents' output. Identity should track new input. (Directly testable, each agent's output is inspectable.)
- **Partial disruption:** Remove individual agents, observe specific capability loss. Should see focal deficits, not global collapse. (Directly testable, maps to neurological case studies.)
- **Forking:** Run parallel ESM agent pools, verify distinct self-models. (Directly testable.)
- **Agent contribution analysis:** Ablation studies on each agent, measuring contribution to overall system behavior. (Standard ML methodology.)

### What Can Be Tested (Moderate)
- **Variable permeability:** Adjust agent state access permissions, observe changes in EWM/ESM content richness. (Testable but coarser than Designs 2-4.)
- **Dream mode:** Disable sensory input agents, observe internally-generated content. (Testable.)
- **Interaction dynamics:** Measure statistical properties of agent outputs over time (autocorrelation, cross-correlation, distribution of output magnitudes). (Measurable, but interpreting as "criticality" is uncertain.)

### What Cannot Be Tested
- **Genuine criticality.** The system does not have a meaningful criticality metric. Branching ratio, avalanche statistics, and correlation length do not have clear definitions for a small multi-agent system. The interaction dynamics may be complex but not formally critical.
- **Whether the multi-agent interaction produces a unified experience.** The theory requires integrated information across the substrate. With discrete agents, integration depends on the shared state mechanism, not on intrinsic dynamics.

### Unique Testing Opportunity
This design uniquely enables **agent-level lesion studies**: systematically removing or modifying individual agents and measuring the effect on system behavior. This maps directly to the neuropsychological case-study methodology that the theory draws on for evidence. Predictions:
- Remove Scene Constructor: EWM loses spatial coherence (hemineglect analog?)
- Remove Identity Narrator: ESM loses self-narrative (amnesia analog?)
- Remove Emotional Evaluator: ESM loses hedonic valence (alexithymia analog?)
- Remove Meta-Reflector: ESM loses metacognition (anosognosia analog?)

These predictions could be tested against the theory's descriptions of neurological conditions to see if the multi-agent architecture produces the right pattern of deficits.
