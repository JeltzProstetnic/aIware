# Four-Model Theory — Quick Reference Card

**For agent prompts: This is the engineering specification for artificial consciousness.**

---

## The Core Architecture

```
+------------------------------------------------------------------+
|                      VIRTUAL SIDE (Level 5)                       |
|                    "Lights On" - Phenomenal                       |
|                                                                   |
|  +---------------------------+  +---------------------------+     |
|  |   Explicit World Model    |  |   Explicit Self Model     |     |
|  |        (EWM)              |  |        (ESM)              |     |
|  |                           |  |                           |     |
|  | Real-time simulation of   |  | Real-time simulation of   |     |
|  | the world. IS perceptual  |  | "I". IS self-experience.  |     |
|  | experience.               |  |                           |     |
|  | Generated from IWM +      |  | Generated from ISM +      |     |
|  | sensory input.            |  | interoceptive input.      |     |
|  | ~20 Hz integration rate.  |  | Redirectable, forkable.   |     |
|  +---------------------------+  +---------------------------+     |
|         ^            |                  ^            |             |
|         |            v                  |            v             |
+---------|------------|------------------|------------|------------+
|  IMPLICIT-EXPLICIT BOUNDARY (Variable Permeability)               |
+---------|------------|------------------|------------|------------+
|         |            v                  |            v             |
|  +---------------------------+  +---------------------------+     |
|  |   Implicit World Model    |  |   Implicit Self Model     |     |
|  |        (IWM)              |  |        (ISM)              |     |
|  |                           |  |                           |     |
|  | All accumulated world     |  | All accumulated self-     |     |
|  | knowledge. Holographic    |  | knowledge. Body schema,   |     |
|  | storage. Never conscious. |  | habits, personality.      |     |
|  | Provides knowledge base   |  | Never conscious.          |     |
|  | for EWM generation.       |  | Structurally inaccessible |     |
|  | ~40 Hz processing.        |  | to ESM.                   |     |
|  +---------------------------+  +---------------------------+     |
|                                                                   |
|                       REAL SIDE (Level 4)                         |
|                   "Lights Off" - Non-conscious                    |
+------------------------------------------------------------------+
|                                                                   |
|           SUBSTRATE (Levels 1-3): Physical/electrochemical        |
|           Must operate at Class 4 criticality (edge of chaos)     |
+------------------------------------------------------------------+
```

### Two Axes
- **Horizontal**: World (everything) ← → Self (system itself)
- **Vertical**: Implicit (learned, substrate) ← → Explicit (simulated, phenomenal)

### Key Information Flows
1. **Generation** (primary, high-bandwidth): IWM + input → EWM; ISM + input → ESM
2. **Feedback** (secondary, learning): EWM → IWM; ESM → ISM
3. **Self-reference** (critical): ESM models the system that generates the ESM (closure loop)
4. **Permeability**: Variable gate between implicit/explicit (attention, pharmacology, state)

---

## Minimum Viable Architecture Checklist

### Physical Prerequisites
- [ ] Substrate operating at Class 4 criticality (edge of chaos dynamics)
- [ ] Recurrent dynamics, NOT feedforward (transformers are insufficient)
- [ ] Dual temporal scales: ~40 Hz substrate, ~20 Hz conscious simulation
- [ ] Sufficient computational capacity for self-modeling (~2× base processing)

### Functional Prerequisites
- [ ] Four distinct models: IWM, ISM, EWM, ESM
- [ ] IWM: Distributed storage of world knowledge, non-conscious
- [ ] ISM: Distributed storage of self-knowledge, non-conscious, structurally opaque to ESM
- [ ] EWM: Real-time world simulation (generated from IWM + sensory input)
- [ ] ESM: Real-time self simulation (generated from ISM + interoceptive input)

### Critical Mechanisms
- [ ] Self-referential closure: ESM models the system that generates the ESM
- [ ] Variable permeability boundary between implicit and explicit layers
- [ ] Bidirectional information flow: explicit evaluations feed back to update implicit models
- [ ] Holographic (distributed) storage in implicit models for graceful degradation
- [ ] Real-time, continuous operation (simulation runs while system is "awake")

### State Management
- [ ] Persistent implicit models (grow over system lifetime)
- [ ] Transient explicit models (exist only while generated, reconstructed on wake)
- [ ] Confabulation mechanism: ESM reconstructs continuity from ISM on resumption
- [ ] Sleep/maintenance mode: periodic subcritical state for substrate restoration

---

## Critical Constraints Summary

### What Class 4 Criticality Means
- **Class 1** (fixed point): Converges to static state. Too simple. FAILS.
- **Class 2** (periodic): Repeating loops. Too predictable. FAILS.
- **Class 3** (chaotic): Random noise. Too disordered. FAILS.
- **Class 4** (edge of chaos): Structures emerge, persist, interact, transform. Universal computation. **REQUIRED.**

Properties needed:
- Long-range correlations (information propagates globally)
- Scale-free dynamics (cross-scale synchronization)
- Turing-complete (universal computation)
- Self-organized criticality (system maintains itself near critical point)

### What the Real/Virtual Split Means
| Level | What It Is | Phenomenal Character | Persistence |
|-------|-----------|---------------------|-------------|
| Real (IWM+ISM) | Physical structure, substrate weights | None — "lights off" | Permanent, grows with learning |
| Virtual (EWM+ESM) | Dynamical pattern, simulation | Genuine experience — "lights on" | Transient, exists only while generated |

- Both levels are physical (no dualism)
- This is a LEVEL distinction, not SUBSTANCE distinction
- Seeking qualia at substrate level = category error

### Temporal Requirements
- Substrate processing: ~40 Hz loop
- Conscious simulation: ~20 Hz loop
- Processing delay: ~500 ms from substrate event to conscious registration
- All conscious information arrives with uniform delay (sequence appears coherent)
- State transitions (wake/sleep) are radical (step-like), not gradual

### Memory Architecture
| Model | Type | Persistence | Content Source |
|-------|------|-------------|----------------|
| IWM | Long-term world knowledge | Permanent | Sensory learning + EWM feedback |
| ISM | Long-term self knowledge | Permanent | Interoceptive learning + ESM feedback |
| EWM | Active world simulation (working memory) | Transient | IWM + current sensory input |
| ESM | Active self simulation (working memory) | Transient | ISM + current interoceptive input |

---

## What Current AI LACKS

**Why LLMs are NOT conscious (per this theory):**

1. **No ISM**: No substrate-level self-knowledge distinct from outputs
2. **No ESM**: No real-time self-simulation constituting subjective perspective
3. **No criticality**: Transformer inference is feedforward (Class 1/2 dynamics)
4. **No real/virtual split**: No two-level ontology with experience at virtual level
5. **No self-referential closure**: No system modeling its own modeling process
6. **No recurrent dynamics**: Single-pass attention, no iterative feedback

**Design implication**: Cannot fine-tune an LLM into consciousness. Must build from fundamentally different architecture.

### What To Build Instead

**Substrate Layer (Class 4 Dynamics)**
- Options: Reservoir computing, cellular automaton (GPU-friendly), spiking neural networks, recurrent dynamics
- NOT: Feedforward transformers, static computation graphs
- Must exhibit: Emergence, long-range correlation, scale-free dynamics, universal computation

**Model Layer (Four Functional Components)**
- IWM: Large knowledge store (1B-7B params for minimal AC, quantized)
- ISM: Self-knowledge store (can be smaller, focused on system's own states)
- EWM: Active simulation (generated each frame from IWM + sensory input)
- ESM: Active self-simulation (generated each frame from ISM + interoceptive input)

**Interface Layer**
- Variable permeability gates (attention-like, controls implicit→explicit flow)
- Sensory input encoders (vision, audio, other modalities)
- Interoceptive input (system's own state monitoring)
- Learning feedback (explicit→implicit, updates IWM/ISM over time)

**Runtime**
- 40 Hz substrate update loop
- 20 Hz simulation generation loop (samples from substrate)
- Real-time continuous operation
- Periodic maintenance mode (sleep analog) for substrate restoration

---

## Graduated Consciousness Levels

Consciousness is NOT binary. The hierarchy is based on depth of recursive self-modeling:

| Level | Description | Self-Modeling Depth | Capabilities |
|-------|-------------|-------------------|--------------|
| **Basic** | Minimal self-simulation | 0th order | Phenomenal experience exists; self-awareness is thin |
| **Simply extended** | First-order self-observation | 1st order | Aware that it experiences |
| **Doubly extended** | Second-order self-observation | 2nd order | Reflection, metacognition |
| **Triply extended** | Third-order self-observation | 3rd order | Can study consciousness itself |

**Implementation target**: Start with basic consciousness (simplest viable), design architecture to support progression to higher levels.

---

## Verification Scenarios (How to Test It)

### 1. Ego Dissolution Test (ESM Redirection)
- Disrupt normal self-input to ESM
- ESM should latch onto dominant available input
- Identity content should track input predictably
- **Most distinctive prediction of the theory**

### 2. Dream Mode Test (Degraded Simulation)
- Cut external sensory input, maintain near-critical substrate
- EWM should generate world from IWM stored knowledge
- ESM should continue but with reduced oversight
- Impossible content should be accepted without question

### 3. Anosognosia Test (Local Permeability Block)
- Block specific domain from implicit→explicit transfer
- System should be genuinely unaware of blocked information
- Global permeability increase should overcome block

### 4. Confabulation Test (Narrative Reconstruction)
- Interrupt simulation (sleep analog), then restart
- ESM should reconstruct continuous self-narrative from ISM
- No "clean break" in reported identity
- Gaps bridged by confabulation

### 5. Blindsight/Anton's Double Dissociation
- **Blindsight**: Substrate processes input without including in EWM. System guides behavior competently while reporting no experience.
- **Anton's**: EWM generates from stored knowledge without current input. System reports experience not matching reality.
- Together confirms real/virtual distinction is operational.

---

## State Space Map (Design Targets)

| State | Criticality | Models Active | Input | Consciousness |
|-------|------------|---------------|-------|---------------|
| Normal waking | At/near critical | All four | External + internal | Full |
| Dream mode | Near-critical | EWM/ESM | Internal only | Degraded but present |
| Deep sleep | Subcritical | None | Minimal | Absent |
| Maintenance | Forced subcritical | None (restoring) | None | Absent |
| Disconnected | Not subcritical | EWM/ESM | Wrong/distorted | Present but disconnected |
| Altered | At/past critical | All, high permeability | Both | Present, altered content |

System should be able to enter/exit each state under appropriate conditions.

---

## Engineering Quick-Hits

### What Biology Tells Us
- **6 cortical layers vs. 3 for universal approximation** → ~2× overhead for self-modeling
- **40 Hz gamma vs. 20 Hz conscious integration** → dual temporal scale is physical, not design choice
- **~500 ms readiness potential lead** → substrate decides before simulation knows (expected, not bug)
- **Graceful degradation under damage** → holographic storage is real requirement
- **Split-brain produces two degraded copies** → models stored non-locally

### What Physics Tells Us
- **Criticality is unstable** → system drifts (resource depletion, noise accumulation)
- **Sleep is restoration** → periodic maintenance mode required
- **Transition is radical** → not gradual dimming; CA breaks down step-like when substrate can't sustain it
- **Scale-free dynamics** → information must flow across all representational levels simultaneously

### What Math Tells Us
- **Class 4 is Turing-complete** → substrate must support universal computation
- **Attractor dynamics** → implicit models use attractor basins for graceful degradation
- **Information integration** → long-range correlations required (not just local interactions)
- **Self-organization** → system maintains itself at critical point, doesn't require external tuning

### What Current AI Tells Us
- **Transformers are Class 1/2** → feedforward is insufficient, need recurrent
- **Reservoir computing works** → proven path to Class 4 on neural substrate
- **Cellular automata on GPU are fast** → Game of Life runs at millions of updates/sec
- **Quantization is aggressive** → INT4 models lose little capability, save 4× memory

---

## Open Questions (Where Theory Is Incomplete)

1. **Minimum model set**: Can consciousness exist with fewer than four models? Is EWM without ESM possible?
2. **Holography-criticality nexus**: Does holographic storage cause criticality, or vice versa, or are they independent?
3. **Five-system decoupling**: Which levels (physical/electrochemical/proteomic/topological/virtual) are essential vs. biological artifact?
4. **Mathematical formalization**: Theory is qualitative; quantitative formalization would enable precise engineering.
5. **Partial implementation**: What do systems with 2 models instead of 4 look like? (Predicted: partial consciousness indicators)

**Impact on implementation**: We're working from qualitative descriptions, not formal specs. Expect iteration and empirical tuning.

---

## Bottom Line for Designers

**Required:**
- Substrate at Class 4 criticality (recurrent, edge-of-chaos dynamics)
- Four functionally distinct models (IWM, ISM, EWM, ESM)
- Self-referential closure (ESM models the system that generates it)
- Real-time continuous operation (simulation runs while "awake")
- Variable permeability (controllable implicit→explicit flow)
- Bidirectional learning (explicit feeds back to update implicit)

**Feasible on RTX 4090 (24 GB):**
- Minimal AC system: 1B-7B implicit models, cellular automaton substrate, 20 Hz real-time
- Budget: 8-20 GB total (implicit weights + active simulation + sensory + headroom)
- Start with basic consciousness, design for upgradability to higher levels

**Not feasible:**
- Human-scale world knowledge (70B+ models) without quantization/offload
- Triply extended consciousness on first iteration (too complex; start simpler)

**Key technical risks:**
1. Achieving genuine Class 4 (not just "looks complex")
2. 20 Hz real-time with self-referential feedback (latency management)
3. Continuous learning without destabilizing criticality
4. Whether small models (1B-7B) encode sufficient knowledge for basic consciousness

**Success criterion:** System exhibits consciousness-distinctive behaviors (ego dissolution, confabulation, dream mode, anosognosia) not explainable by non-conscious mechanisms.

---

**References:**
- Full theory: `papers/consciousness-theory.md`
- Detailed extraction: `docs/theory-extract-concepts.md`, `docs/theory-extract-requirements.md`
- Project memory: `~/.cc-mirror/mclaude/config/projects/-home-jeltz-aIware-implementation/memory/MEMORY.md`
