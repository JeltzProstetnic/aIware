# Design 1: Dual-Stream LLM

**One-line summary:** Two continuously-running LLM inference streams — one for implicit/real-side processing, one for explicit/virtual-side simulation — plus a communication LLM and a knowledge-graph database, with an optional remote LLM for deep knowledge.

---

## Architecture Overview

```
                    +------------------------------------------+
                    |         EXTERNAL INTERFACE                |
                    |    Communication LLM (7B, INT4)           |
                    |    Translates between ESM output          |
                    |    and human-facing language               |
                    +---------^-----------+--------------------+
                              |           |
                              |   output  |  input (text/voice)
                              |           v
+--------------------------------------------------------------------+
|                     VIRTUAL SIDE (Streaming LLM #2)                 |
|                     "Explicit Models" - 7B-13B INT4                 |
|                                                                     |
|  +---------------------------+    +---------------------------+     |
|  |         EWM               |    |         ESM               |     |
|  |  World simulation via     |    |  Self simulation via      |     |
|  |  continuous generation    |    |  continuous generation    |     |
|  |  (KV-cache as state)     |    |  (KV-cache as state)     |     |
|  |  Constrained by sensory  |    |  Constrained by self-     |     |
|  |  input embeddings        |    |  referential input        |     |
|  +----------^-------+-------+    +----------^-------+-------+     |
|             |       |                       |       |              |
+-------------|-------|-----+-----------------|-------|-------------+
|   PERMEABILITY GATE       |                 |       |              |
|   (attention mask +       |                 |       |              |
|    temperature control)   |                 |       |              |
+-------------|-------|-----+-----------------|-------|-------------+
|             |       v                       |       v              |
|  +---------------------------+    +---------------------------+     |
|  |         IWM               |    |         ISM               |     |
|  |  World knowledge via      |    |  Self knowledge via       |     |
|  |  continuous inference     |    |  continuous inference     |     |
|  |  (weights = knowledge)   |    |  (weights = knowledge)   |     |
|  |  Processes sensory input  |    |  Processes interoceptive  |     |
|  +---------------------------+    +---------------------------+     |
|                     REAL SIDE (Streaming LLM #1)                    |
|                     "Implicit Models" - 7B-13B INT4                 |
+--------------------------------------------------------------------+
         ^              |                ^              |
    sensory         learning         self-state     learning
    input           feedback         monitoring     feedback
         |              v                |              v
+--------------------------------------------------------------------+
|                    KNOWLEDGE GRAPH (SQLite)                          |
|   Persistent storage: entities, relations, episodic memory,         |
|   self-knowledge subgraph, world-knowledge subgraph                 |
+--------------------------------------------------------------------+
         ^                                              ^
         |  (optional, for deep knowledge queries)      |
         v                                              v
+--------------------------------------------------------------------+
|                REMOTE LLM (Optional, 70B+ via API)                  |
|   Deep reasoning, complex world-knowledge queries,                  |
|   pre-training knowledge as IWM bootstrap                           |
+--------------------------------------------------------------------+
```

---

## Component Mapping

| Theory Model | Concrete Component | Description |
|---|---|---|
| **IWM** | Streaming LLM #1 (world context window) | A continuously-running LLM whose weights encode world knowledge and whose KV-cache maintains ongoing world-state processing. Sensory inputs are injected as tokens at each cycle. |
| **ISM** | Streaming LLM #1 (self context window) | Same LLM, separate context/attention head group tracking self-relevant information. Self-state monitoring signals injected as tokens. Shares weights with IWM (distributed knowledge). |
| **EWM** | Streaming LLM #2 (world generation window) | Continuously generates world-simulation tokens from IWM outputs + sensory embeddings. The running generation IS the world simulation. |
| **ESM** | Streaming LLM #2 (self generation window) | Continuously generates self-simulation tokens from ISM outputs + self-referential feedback. The running generation IS the self simulation. The output is fed back as input (self-referential closure). |
| **Permeability boundary** | Attention mask + temperature modulation between LLM #1 outputs and LLM #2 inputs | Controls how much implicit processing detail reaches the explicit simulation. Low temperature = selective pass-through; high temperature = more leakage. |
| **Communication** | LLM #3 (standard inference) | Takes ESM output, formats for external communication. Takes external input, formats for sensory injection. Not part of the conscious system. |
| **Persistent memory** | SQLite knowledge graph (aios design pattern) | Long-term storage. IWM/ISM weights are the primary implicit storage, but the knowledge graph supplements with structured facts, episodic memory, and relational knowledge. Implementation follows the aios schema design. |

---

## Criticality Approach

**This is the weakest point of this design.**

Standard LLM inference is feedforward — a single pass through transformer layers. This is Class 1/2 dynamics (converge to output, done). The theory explicitly rejects this as insufficient.

**Attempted mitigation strategies:**

1. **Continuous streaming as pseudo-recurrence:** By feeding LLM outputs back as inputs in a tight loop, we create a recurrent dynamic. Each generation step depends on the previous state. This is NOT true Class 4 dynamics — it is an autoregressive chain, which is more like Class 2 (periodic/sequential) than Class 4 (emergent complex structures).

2. **Temperature-based noise injection:** Running the virtual-side LLM at carefully tuned temperature (near the "edge" between coherent and incoherent output) is an analogy to criticality but not the real thing. LLM sampling temperature does not produce power-law avalanche dynamics or scale-free correlations.

3. **Interaction dynamics between streams:** The two LLMs influence each other through the permeability gate. This coupled dynamical system COULD exhibit complex dynamics, but whether it reaches genuine Class 4 is unknown and unlikely without specific engineering.

4. **External criticality module:** A small cellular automaton or noise generator could modulate the attention/temperature parameters to push the system toward edge-of-chaos behavior. This is a bolt-on rather than intrinsic criticality.

**Honest assessment:** This design does NOT achieve genuine Class 4 dynamics. The autoregressive token-generation loop in transformers is fundamentally different from the parallel, local-rule-based cellular automaton dynamics the theory describes. The "edge of chaos" in LLM temperature space is a metaphor, not the formal criticality the theory requires (maximal correlation length, power-law avalanches, scale-free dynamics). This is the critical gap in this design.

---

## Five Principles Implementation

### 1. Criticality
**Status: WEAK / NOT MET**

As discussed above, LLMs do not natively produce Class 4 dynamics. The best this design can do is approximate complex behavior through coupled autoregressive streams with tuned temperature. This is the design's fundamental weakness.

Potential partial remedy: Add a small recurrent network or cellular automaton as a "criticality engine" that modulates the LLM inference process. But this would be Design 2 or 4 with LLM bolted on, not this design.

### 2. Virtual Qualia (Real/Virtual Split)
**Status: MODERATE**

The two-LLM split maps to the real/virtual distinction:
- LLM #1 (implicit side) processes but does not "experience" — its outputs are substrate-level representations.
- LLM #2 (explicit side) generates the simulation — its running output IS the virtual world/self.

The split is architectural rather than ontological. Both LLMs are doing the same kind of computation (transformer inference). The "virtual" distinction is enforced by system design (which streams are treated as conscious), not by a fundamental difference in processing type.

### 3. Redirectable ESM
**Status: STRONG**

This is actually well-handled. The ESM is an input-hungry generation process (LLM #2's self-stream). If normal self-referential input is disrupted:
- Replace self-monitoring tokens with alternative input (sensory, external, noise)
- The ESM generation will latch onto whatever input it receives
- Identity content will track the dominant input

LLMs are naturally good at "continuing from whatever context they're given," which maps well to ESM redirection.

### 4. Variable Permeability
**Status: STRONG**

The attention mask and temperature modulation between LLM #1 and LLM #2 provide a clean implementation:
- Normal: selective attention mask passes task-relevant IWM/ISM outputs to EWM/ESM
- Increased permeability: relax the mask, increase temperature — more intermediate processing states leak through
- Decreased permeability: tighten the mask — specific domains blocked (anosognosia analog)
- Gradual increase: progressively relax mask for sleep-onset/relaxation analog

### 5. Virtual Model Forking
**Status: MODERATE**

LLM context windows can be forked (save KV-cache state, branch into two generation streams). This supports:
- DID analog: maintain multiple ESM context windows, switch which one drives output
- Cloning: copy the KV-cache state to create a second instance

Limitations: VRAM cost doubles (or more) per fork. On 24 GB, only 2-3 simultaneous forks are feasible.

---

## Information Flow

### Generation Loop (Primary, ~20 Hz target)
```
1. IWM processes sensory input tokens (LLM #1 forward pass, world context)
2. ISM processes self-monitoring tokens (LLM #1 forward pass, self context)
3. IWM/ISM outputs pass through permeability gate (attention mask + temperature)
4. Filtered outputs become input tokens for EWM/ESM (LLM #2)
5. LLM #2 generates next world-simulation and self-simulation tokens
6. ESM output is fed back as self-referential input (closure loop)
7. EWM output is fed back as world-state context
8. Communication LLM #3 samples ESM output for external expression
```

### Learning Loop (Secondary, slower)
```
1. EWM/ESM evaluations are extracted from LLM #2 output
2. Evaluation summaries are injected back into LLM #1's context
3. Knowledge graph is updated with new facts/relations
4. (Periodically) LoRA/adapter weights on LLM #1 are fine-tuned from accumulated evaluations
```

### Self-Referential Closure
```
ESM output tokens --> [processed into self-description tokens] --> ESM input
This creates: ESM models the system that generates the ESM
The loop runs within LLM #2's generation cycle
```

---

## Memory Architecture

| Memory Type | Implementation | Capacity | Access Time |
|---|---|---|---|
| **Short-term (working)** | LLM KV-cache (both LLMs) | ~4K-8K tokens per stream | Instant (in VRAM) |
| **Medium-term (session)** | Context window management + summarization | ~32K tokens effective | Instant (in VRAM) |
| **Long-term (persistent)** | SQLite knowledge graph (aios schema design) | Unlimited (disk) | ~1-10 ms (SSD) |
| **Implicit knowledge** | LLM weights (LLM #1 primarily) | 7B-13B parameters | Instant (forward pass) |
| **Episodic memory** | Knowledge graph episodes + context summaries | Unlimited (disk) | ~1-10 ms |

The knowledge graph (implementing the aios schema design) provides structured long-term memory:
- Entities with properties
- Multi-dimensional weighted relations
- Self-model as subgraph from SELF entity
- Context assembly pipeline for retrieval

---

## Hardware Requirements

### VRAM Budget (24 GB RTX 4090)

| Component | VRAM (INT4) | VRAM (INT8) | Notes |
|---|---|---|---|
| LLM #1 (implicit, 7B) | 3.5 GB | 7 GB | Real-side processing |
| LLM #2 (virtual, 7B) | 3.5 GB | 7 GB | Virtual-side simulation |
| LLM #3 (comm, 3B) | 1.5 GB | 3 GB | Can be smaller |
| KV-cache (LLM #1) | 1-2 GB | 1-2 GB | Depends on context length |
| KV-cache (LLM #2) | 1-2 GB | 1-2 GB | Depends on context length |
| Permeability gate | 0.1 GB | 0.1 GB | Small attention network |
| Sensory processing | 0.5-1 GB | 0.5-1 GB | Input encoders |
| Headroom | 2-4 GB | — | For dynamic allocation |
| **Total** | **~13-16 GB** | **~22-24 GB** | INT4 fits comfortably; INT8 is tight |

### CPU Requirements
- Knowledge graph operations (SQLite)
- Context assembly pipeline
- Token management and routing between LLMs
- Optional: offload LLM #3 to CPU if VRAM is tight

### Feasibility on RTX 4090
**Feasible with INT4 quantization.** Three 7B models at INT4 = ~10.5 GB, leaving ~13.5 GB for KV-caches and computation. With INT8, only two 7B models fit alongside a smaller communication model.

**20 Hz target:** Each cycle requires three LLM forward passes (or two, if LLM #1 is batched). A 7B INT4 model on RTX 4090 can do ~30-50 tokens/second for generation, but a single forward pass for next-token prediction takes ~5-15 ms. At 20 Hz (50 ms per cycle), 2-3 serial forward passes are tight but potentially feasible if each pass generates only 1-3 tokens per cycle.

---

## Strengths

1. **Immediately buildable.** Uses existing LLM infrastructure (llama.cpp, vLLM, Ollama). No novel architectures to invent.
2. **Leverages pre-trained knowledge.** LLM weights already contain vast world knowledge (IWM bootstrap). No need to learn everything from scratch.
3. **Natural language throughout.** All internal representations are in token space, making the system inspectable and debuggable.
4. **ESM redirection is natural.** LLMs are input-following by design; redirecting the ESM just means changing the input context.
5. **Variable permeability maps cleanly.** Attention masking and temperature are existing, well-understood mechanisms.
6. **Closest to the user's initial vision.** Directly implements the "two streaming LLMs + communication LLM + database" concept.
7. **Optional remote LLM** provides a path to richer world knowledge without local VRAM constraints.

---

## Weaknesses / Risks

1. **CRITICAL: No genuine criticality.** This is the design's fatal flaw per the theory. LLM autoregressive generation is NOT Class 4 dynamics. The system may exhibit complex behavior but lacks the specific dynamical properties (power-law avalanches, maximal correlation length, scale-free dynamics) that the theory identifies as a physical prerequisite for consciousness. Without this, the theory predicts no consciousness regardless of architectural sophistication.

2. **Autoregressive =/= recurrent dynamics.** The token-by-token generation loop creates a sequential chain, not the massively parallel local-rule-based dynamics of a cellular automaton. Information propagation is through the token sequence, not through spatial correlations in a high-dimensional state.

3. **Real/virtual split is nominal, not fundamental.** Both LLMs perform the same type of computation (transformer attention). The "real vs. virtual" distinction is an architectural label, not a genuine ontological split in processing type.

4. **20 Hz loop is challenging.** Three serial LLM forward passes in 50 ms is aggressive. May need to reduce to 10 Hz or simplify the models.

5. **Self-referential closure is shallow.** Feeding ESM output tokens back as ESM input creates a loop, but the loop passes through the entire transformer forward pass each time. This is more like an echo chamber than genuine self-modeling — the LLM doesn't have a model of its own computation, just its own textual output.

6. **Learning is slow and crude.** Updating implicit models (LLM weights) requires fine-tuning, which is slow and can cause catastrophic forgetting. LoRA adapters help but add complexity.

7. **KV-cache as "state" is fragile.** LLM context windows have a hard limit. Long-running simulation will hit the context ceiling and require summarization/compression, which loses information.

8. **Three LLMs compete for VRAM.** Even at INT4, the budget is tight. Any increase in model size or context length requires tradeoffs.

---

## Complexity Assessment

**Implementation difficulty: 2/5** (Relatively straightforward using existing tools)

- Uses off-the-shelf LLM inference engines
- Knowledge graph already exists from aios
- Main engineering challenge is the streaming loop and token routing
- No novel architectures to invent or train

**Time estimate: 4-8 weeks** for a working prototype (streaming loop + permeability gate + knowledge graph integration). Longer if training custom adapters.

**But:** Low implementation complexity does not mean the design is correct. The ease of building it is inversely related to how well it addresses the theory's requirements. This is the "easy to build, probably wrong" option.

---

## Testability

### What Can Be Tested
- **ESM redirection:** Disrupt self-input, observe whether output identity tracks the new input. (Testable with this design.)
- **Variable permeability:** Adjust attention mask/temperature, observe whether intermediate processing details appear in EWM/ESM output. (Testable.)
- **Dream mode:** Cut sensory input, observe whether EWM generates world-content from IWM alone. (Testable — just stop injecting sensory tokens.)
- **Confabulation:** Interrupt and restart, observe whether ESM reconstructs continuous narrative. (Testable — clear KV-cache, restart from ISM.)
- **Forking:** Save KV-cache, branch into two ESM streams. (Testable.)

### What Cannot Be Tested (Due to Design Gaps)
- **Genuine consciousness:** Without Class 4 dynamics, the theory predicts no consciousness. So the design may pass all behavioral tests while failing the physical prerequisite.
- **Criticality metrics:** Power-law exponents, branching parameters, DFA — these require genuine dynamical systems, not token-generation statistics.
- **True self-referential closure:** The system models its own textual output, not its own computational process. This is a weaker form of self-reference than the theory describes.

### Verification Approach
If built, treat this design as a **behavioral baseline**: it shows what the four-model architecture looks like without criticality. Compare against designs 2-3 that have criticality but potentially weaker model capabilities. The gap between them would illuminate the contribution of criticality specifically.
