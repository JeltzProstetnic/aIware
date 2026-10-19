# AIOS Architecture Reference for AC Implementation

**Source project:** `/home/jeltz/aios/`
**Purpose:** Reference document describing the parts of the AIOS architecture relevant to the Artificial Consciousness (AC) implementation. This is not a copy of the AIOS docs but a focused extraction of reusable **designs** and mapping points.

**IMPORTANT:** The aios project is a **design-only** project (documentation, schemas, architecture docs) with no running implementation. This document extracts architectural patterns and design decisions from aios that can guide the AC implementation. The knowledge graph **schema** (SQL definition) exists, the architecture is well-documented, but there is no working code to reuse. The value is in the **design blueprints**, not in a codebase to port.

**Key source files:**
- `aios/docs/ARCHITECTURE.md` (Sections 3, 4, 6, 10)
- `aios/docs/CONSCIOUSNESS-AND-WORLD-MODELS.md`
- `aios/src/aios/memory/schema.sql`

---

## 1. Theoretical Mapping: AIOS to Gruber's Four Models

AIOS explicitly maps its architecture to Gruber's four-model theory. The AC project extends this mapping from Level 0 (AIOS's target) to Levels 1-3.

| Gruber Model | AIOS Component | Nature | AC Relevance |
|---|---|---|---|
| **Metamodell** (implicit total knowledge) | SQLite knowledge graph (persistent) | Learned, never directly conscious | Maps to ISM + IWM combined store |
| **Weltmodell** (explicit simulation) | Assembled LLM context per turn (transient) | Freshly constructed each turn | Maps to EWM generation process |
| **Ich-Modell** (explicit self) | SELF entity subgraph within the knowledge graph | Embedded in Weltmodell, not separate | Maps to ESM |
| **Arbeitsmodell** (working memory) | Short-term in-memory buffer + current turn state | Ephemeral, never persisted | Maps to working memory / active simulation |
| **Selbstmodell** (implicit self) | LLM weights + system config + behavioral patterns | Not engineered, implicit in substrate | Maps to ISM |

The core insight from AIOS: **the knowledge graph is the persistent store (Meta-Model), the assembled context is the transient simulation (World-Model), and the LLM processing loop is the cortical automaton that generates one from the other.** Each conversation turn is a fresh act of simulation, not a database lookup.

---

## 2. Knowledge Graph Architecture

### 2.1 Design Philosophy

The knowledge graph is a **fully flexible entity-relation model** with no hardcoded types. Entity types emerge from relations to meta-entities (e.g., "Matthias" is a person because it has `is_a -> Person`), not from a type column. This means the graph can represent arbitrary knowledge categories without schema changes.

All persistent state lives in a **single SQLite database** (`~/.aios/aios.db`) using WAL mode, FTS5, recursive CTEs for graph traversal, and SQLCipher for encryption.

### 2.2 Schema Tables

#### `entities` — Graph Nodes

```sql
CREATE TABLE IF NOT EXISTS entities (
    id            TEXT PRIMARY KEY,    -- UUID v4
    label         TEXT NOT NULL,       -- human-readable ("Matthias", "RTX 4090")
    created_at    TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    updated_at    TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    last_accessed TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    importance    REAL NOT NULL DEFAULT 0.5 CHECK (importance >= 0.0 AND importance <= 1.0),
    confidence    REAL NOT NULL DEFAULT 0.5 CHECK (confidence >= 0.0 AND confidence <= 1.0),
    source        TEXT NOT NULL DEFAULT 'conversation'
);
```

| Column | AC Significance |
|---|---|
| `importance` | Decays without access. Drives what gets pruned from long-term memory. Analogous to synaptic weakening. |
| `confidence` | How certain the system is this entity is correct. Supports subjective vs. objective knowledge distinction from Gruber. |
| `source` | Provenance tracking. Values: `conversation`, `onboarding`, `observation`, `inferred`, `import`, `system`. |
| `last_accessed` | Used for importance decay calculation. Entities not accessed lose importance over time. |

#### `entity_properties` — EAV Flexible Properties

```sql
CREATE TABLE IF NOT EXISTS entity_properties (
    entity_id  TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    key        TEXT NOT NULL,
    value      TEXT NOT NULL,  -- JSON-encoded
    PRIMARY KEY (entity_id, key)
);
```

Allows arbitrary key-value properties on any entity without schema changes. Values are JSON-encoded to support complex types.

#### `relations` — Directed Edges

```sql
CREATE TABLE IF NOT EXISTS relations (
    id          TEXT PRIMARY KEY,    -- UUID v4
    source_id   TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    target_id   TEXT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    created_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    updated_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    confidence  REAL NOT NULL DEFAULT 0.5 CHECK (confidence >= 0.0 AND confidence <= 1.0),
    source_info TEXT NOT NULL DEFAULT 'conversation'
);
```

Relations are directed edges between entities. A relation is NOT typed by a single label; instead, its semantics are defined by its dimension values (see below).

#### `relation_dimensions` — Multi-Dimensional Edge Weights

```sql
CREATE TABLE IF NOT EXISTS relation_dimensions (
    relation_id TEXT NOT NULL REFERENCES relations(id) ON DELETE CASCADE,
    dimension   TEXT NOT NULL REFERENCES dimensions(name),
    weight      REAL NOT NULL CHECK (weight >= -1.0 AND weight <= 1.0),
    PRIMARY KEY (relation_id, dimension)
);
```

This is the key design innovation. Each relation carries values along **multiple named dimensions** simultaneously. A single edge between "Matthias" and "Coffee" might carry `prefers: 0.9`, `frequency: 0.7`, and `emotional: 0.6` — all at once. This makes relations multi-faceted rather than single-typed.

#### `dimensions` — Dimension Registry

```sql
CREATE TABLE IF NOT EXISTS dimensions (
    name        TEXT PRIMARY KEY,
    description TEXT NOT NULL,
    range_min   REAL NOT NULL DEFAULT 0.0,
    range_max   REAL NOT NULL DEFAULT 1.0,
    resilience  REAL NOT NULL DEFAULT 0.5 CHECK (resilience >= 0.0 AND resilience <= 1.0),
    origin      TEXT NOT NULL DEFAULT 'seed' CHECK (origin IN ('seed', 'learned', 'user')),
    created_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    deprecated  INTEGER NOT NULL DEFAULT 0
);
```

| Column | Meaning |
|---|---|
| `resilience` | How resistant to LLM modification. Seed dimensions: 0.5-0.9. Learned: starts at 0.3, increases if used. |
| `origin` | `seed` = built-in, `learned` = proposed by LLM, `user` = created by user. |
| `deprecated` | Learned dimensions unused for 90 days are auto-deprecated. |

#### `medium_term_records` — Semi-Structured Bridge Memory

```sql
CREATE TABLE IF NOT EXISTS medium_term_records (
    id          TEXT PRIMARY KEY,
    type        TEXT NOT NULL CHECK (type IN ('summary', 'fact', 'pattern', 'observation')),
    content     TEXT NOT NULL,
    session_id  TEXT,
    entity_refs TEXT,     -- JSON array of entity IDs
    created_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    expires_at  TEXT,     -- NULL = no expiry
    consolidated INTEGER NOT NULL DEFAULT 0  -- 0=pending, 1=promoted, 2=discarded
);
```

#### `conversation_turns` — Raw Interaction Log

```sql
CREATE TABLE IF NOT EXISTS conversation_turns (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id      TEXT NOT NULL,
    timestamp       TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
    speaker_id      TEXT,
    text            TEXT NOT NULL,
    classification  TEXT NOT NULL DEFAULT 'ambient',
    response        TEXT,
    language        TEXT NOT NULL DEFAULT 'en',
    confidence      REAL NOT NULL DEFAULT 0.5
);
```

Not a memory tier itself, but the raw source from which medium-term summaries and long-term entities are derived.

#### Vector Embedding Tables (sqlite-vec)

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS vec_entities USING vec0(
    entity_id TEXT PRIMARY KEY, embedding float[384]
);
CREATE VIRTUAL TABLE IF NOT EXISTS vec_medium_term USING vec0(
    record_id TEXT PRIMARY KEY, embedding float[384]
);
CREATE VIRTUAL TABLE IF NOT EXISTS vec_conversations USING vec0(
    turn_id INTEGER PRIMARY KEY, embedding float[384]
);
```

Embedding model: all-MiniLM-L6-v2 (384 dimensions, ~80 MB, runs on CPU). These enable semantic similarity search as the first stage of context assembly.

### 2.3 Schema Diagram

```
entities ──1:N──> entity_properties (EAV)
    │
    │ source_id / target_id
    ▼
relations ──1:N──> relation_dimensions (EAV on edges)
                        │
                        │ dimension (FK)
                        ▼
                   dimensions (registry)

medium_term_records (bridge memory)
conversation_turns (raw log)
vec_entities / vec_medium_term / vec_conversations (vector search)
sessions (session tracking)
```

---

## 3. The 17 Seed Dimensions

The dimension system is how AIOS makes relations semantically rich. Each dimension is a named axis along which a relation can carry a weight.

| # | Dimension | Range | Semantics | Resilience | AC Mapping |
|---|---|---|---|---|---|
| 1 | `is_a` | 0-1 | Taxonomic classification | 0.9 | Category membership in world model |
| 2 | `has_part` | 0-1 | Part-whole composition | 0.9 | Structural decomposition |
| 3 | `located_at` | 0-1 | Spatial location | 0.9 | Spatial world model |
| 4 | `temporal` | -1 to 1 | Before/simultaneous/after | 0.9 | Temporal world model |
| 5 | `causal` | 0-1 | Cause-effect strength | 0.9 | Causal reasoning in IWM |
| 6 | `owns` | 0-1 | Ownership/possession | 0.7 | Agent-resource relations |
| 7 | `prefers` | -1 to 1 | Dislike to strong like | 0.7 | Preference modeling (ISM/ESM) |
| 8 | `knows` | 0-1 | Social connection strength | 0.7 | Social world model |
| 9 | `works_on` | 0-1 | Active involvement | 0.7 | Goal/project tracking |
| 10 | `expertise` | 0-1 | Skill/knowledge level | 0.7 | Self-capability model (ESM) |
| 11 | `emotional` | -1 to 1 | Negative to positive valence | 0.7 | Emotional coloring of knowledge |
| 12 | `similarity` | 0-1 | Conceptual similarity | 0.5 | Analogical reasoning |
| 13 | `frequency` | 0-1 | How often relation is active | 0.5 | Habit/pattern detection |
| 14 | `trust` | 0-1 | Source reliability | 0.7 | Epistemic confidence |
| 15 | `contradicts` | 0-1 | Degree of contradiction | 0.9 | Inconsistency tolerance |
| 16 | `supersedes` | 0-1 | Newer replacing older | 0.7 | Belief revision |
| 17 | `self_relevance` | 0-1 | Relevance to self-concept | 0.9 | ISM/ESM boundary definition |

**Learned dimensions**: The LLM can propose new dimensions when existing ones do not fit. Learned dimensions start at resilience 0.3 and increase if frequently used. Unused learned dimensions are deprecated after 90 days.

For AC, the dimension system is directly reusable. The `self_relevance`, `contradicts`, `emotional`, and `trust` dimensions are especially important for consciousness modeling.

---

## 4. Self-Model as Subgraph (Ich-Modell)

This is the most directly AC-relevant design in AIOS.

### 4.1 The SELF Entity

A single anchor entity is created at first boot:

```sql
INSERT OR IGNORE INTO entities(id, label, importance, confidence, source) VALUES
    ('00000000-0000-0000-0000-000000000001', 'SELF', 1.0, 1.0, 'system');
```

The SELF entity carries properties like `description`, `persona`, and `default_name` via the EAV table. It is the root from which the entire self-model is traversed.

### 4.2 Traversal Algorithm

The Ich-Modell is **not a separate data structure** but a subgraph defined by traversal from SELF, following relations whose `self_relevance` dimension exceeds a threshold:

```sql
WITH RECURSIVE ich_modell(entity_id, depth) AS (
    SELECT '00000000-0000-0000-0000-000000000001', 0
    UNION
    SELECT r.target_id, ich.depth + 1
    FROM ich_modell ich
    JOIN relations r ON r.source_id = ich.entity_id
    JOIN relation_dimensions rd ON rd.relation_id = r.id
    WHERE rd.dimension = 'self_relevance'
      AND rd.weight >= :threshold
      AND ich.depth < :max_depth
)
SELECT DISTINCT e.* FROM entities e
JOIN ich_modell im ON e.id = im.entity_id;
```

### 4.3 Threshold Dynamics

The threshold is **not fixed** but controlled by the context assembly pipeline:
- Under tight token budgets, threshold rises (only core identity included)
- Under generous budgets, threshold drops (peripheral self-knowledge available)

This means the self-model has a **variable boundary** — exactly matching Gruber's claim that the self/world boundary is learned and graduated, not hardcoded.

### 4.4 What Lives in the Ich-Modell

| Self-Knowledge | Example | self_relevance |
|---|---|---|
| Core identity | SELF name, persona | 1.0 |
| Capabilities | "can control smart home" | 0.9 |
| Behavioral patterns | "butler mode for tasks" | 0.9 |
| User relationship | SELF -> user (via serves/knows) | 0.95 |
| Meta-knowledge | Resolution strategies | 0.85 |
| Learned boundaries | "should not interrupt" | 0.8 |
| Peripheral | Hardware constraints | 0.5 |

### 4.5 AC Mapping

For the AC project, this design maps to:

| AIOS Concept | AC Concept |
|---|---|
| SELF entity | ESM anchor |
| `self_relevance` threshold traversal | ESM boundary (graduated, not binary) |
| Threshold dynamics | ESM permeability / variable scope |
| Meta-knowledge strategies | ESM's self-knowledge about its own reasoning |
| The entire knowledge graph minus Ich-Modell | EWM (the world beyond self) |

The key insight: **the self is not a special kind of entity, it is a traversal pattern.** Any entity can become part of the self-model if its `self_relevance` is high enough. This mirrors Gruber's claim that the self/world boundary is learned from feedback density.

---

## 5. Inconsistency Tolerance

### 5.1 Design

The knowledge graph **tolerates contradictions**. Two conflicting facts coexist as separate entities connected by a `contradicts` relation. This implements Gruber's observation that mental models are "fleeting, often strongly fragmented, and only rarely truly consistent."

Contradictions are:
- **Detected lazily** by the LLM during normal processing, not by a background consistency checker
- **Resolved only when they matter** for the current response
- **Resolved via meta-knowledge entities** that live inside the graph itself

### 5.2 Meta-Knowledge Entities

Four seed resolution strategies are created at first boot, linked to SELF with high `self_relevance`:

| Entity | Strategy | Applied When |
|---|---|---|
| `prefer_recent` | Use the more recently learned fact | Temporal supersession |
| `prefer_authority` | Use the more authoritative source | Source provenance differs |
| `ask_user` | Ask the user to resolve | Similar confidence, high stakes |
| `coexist` | Allow both facts to coexist | Multi-valued truths |

These strategies are **themselves entities in the graph**, reachable from SELF, and are learnable — the LLM can refine them, create new ones, or learn when NOT to resolve.

### 5.3 Contradiction Query

```sql
SELECT e2.*, rd.weight AS contradiction_strength
FROM relations r
JOIN relation_dimensions rd ON rd.relation_id = r.id
JOIN entities e2 ON e2.id = r.target_id
WHERE r.source_id = :entity_id
  AND rd.dimension = 'contradicts'
  AND rd.weight > 0.0;
```

### 5.4 AC Significance

For AC, this is critical:
- Mental models in consciousness theory are NOT globally consistent
- An AC system must tolerate multiple simultaneous beliefs about the same topic
- Resolution strategies as meta-knowledge (knowledge about how to handle knowledge) map to ESM self-awareness about reasoning
- The "coexist" strategy is especially important for modeling uncertainty and perspective-taking

---

## 6. Memory Tiers

### 6.1 Three-Tier Architecture

| Tier | Storage | Lifetime | Contents | Gruber Model |
|---|---|---|---|---|
| **Short-term** | In-memory (Python) | Seconds to minutes | Conversation buffer, current turn state, observation cache, assembled context | Arbeitsmodell |
| **Medium-term** | SQLite (`medium_term_records`) | Hours to days (default: 30 days) | Conversation summaries, recently learned facts, observation patterns | Bridge |
| **Long-term** | SQLite knowledge graph | Days to years | Entities, relations, dimensions, meta-knowledge | Metamodell |

### 6.2 Short-Term Memory Detail

| Slot | Content | Lifetime |
|---|---|---|
| Conversation buffer | Last N minutes of transcript | Pruned on overflow (default 10 min) |
| Turn state | Current tool calls, partial responses | Single turn |
| Observation cache | Latest sensory data | Overwritten each cycle |
| Working context | Assembled graph fragment for LLM | Single turn |

Short-term memory is **never persisted**. Lost on restart. This is the active working memory.

### 6.3 Medium-Term Memory Detail

| Record Type | Created When | Example |
|---|---|---|
| `summary` | End of session or every N turns | "Discussed API rate limiting" |
| `fact` | LLM detects new fact mid-conversation | "User started learning Rust" |
| `pattern` | Repeated observation across sessions | "User usually starts work at 9am" |
| `observation` | Noteworthy single observation | "User seemed frustrated today" |

Precision decays over time — 2-hour-old summaries retain key decisions; 3-day-old summaries retain only topic and outcome. This mirrors human memory compression.

### 6.4 Consolidation (Experience-Driven)

Consolidation is **event-driven, not clock-driven**. This maps to Gruber's novelty-gated consolidation.

| Trigger | Direction | Action |
|---|---|---|
| Short-term buffer overflow | Short -> Medium | Summarize oldest segment |
| Session end (silence > 5 min) | Short -> Medium | Generate session summary |
| Fact reinforced across sessions | Medium -> Long | Create/strengthen entity in graph |
| Explicit user correction | Medium -> Long | Update graph immediately |
| Medium-term tier overflow | Medium -> Long | Consolidate oldest records |
| Long-term entry never accessed | Long -> decay | Reduce importance; prune at 0 |

The LLM assesses novelty and importance during consolidation. Routine exchanges produce thin summaries; significant decisions produce rich graph updates.

---

## 7. Context Assembly Pipeline

This is the process that generates the transient Weltmodell (EWM) from the persistent Metamodell (IWM + ISM store) each turn.

### 7.1 Pipeline Stages

```
User utterance arrives
        |
        v
1. VECTOR RETRIEVAL     Embed the query; find top-K similar entities
   (semantic search)    and medium-term records
        |
        v
2. GRAPH EXPANSION      From retrieved entities, traverse 1-2 hops
   (1-2 hops)          of outgoing relations above weight threshold
        |
        v
3. ICH-MODELL MERGE     Assemble self-model subgraph (Section 4);
                        merge with retrieved context; deduplicate
        |
        v
4. BUDGET ALLOCATION    Serialize to text; trim to token budget
   (dynamic)           Priority: system prompt > identity > conversation
                       > retrieved entities > summaries > peripheral self
        |
        v
Assembled context -> LLM prompt (= Weltmodell for this turn)
```

### 7.2 Budget Allocation Priority

1. System prompt + persona (always included)
2. Ich-Modell core: identity, capabilities (always included)
3. Conversation buffer: recent turns (always included)
4. Retrieved entities + graph context (trimmed under pressure)
5. Medium-term summaries (trimmed under pressure)
6. Peripheral Ich-Modell (trimmed first)

### 7.3 Load Factor

The ratio of assembled tokens to available budget controls retrieval aggressiveness:

| Load Factor | Behavior |
|---|---|
| < 0.5 | Generous: lower thresholds, more hops, more context |
| 0.5 - 0.8 | Normal: balanced retrieval |
| > 0.8 | Tight: raise Ich-Modell threshold, reduce expansion, summarize |

### 7.4 AC Mapping

This pipeline is the direct implementation of the IWM-to-EWM generation process:

| Pipeline Stage | AC Process |
|---|---|
| Vector retrieval | Associative activation from current stimulus |
| Graph expansion | Spreading activation through knowledge network |
| Ich-Modell merge | Self-model integration into world model (ESM embedded in EWM) |
| Budget allocation | Attention / working memory capacity limits |
| Load factor dynamics | Variable permeability between implicit and explicit |

The Weltmodell is **freshly constructed each turn** from the persistent Metamodell. The same knowledge can produce different context assemblies depending on what is relevant. This is simulation, not retrieval.

---

## 8. LLM Integration Pattern

### 8.1 Architecture

AIOS uses local LLMs via OpenAI-compatible HTTP APIs. The primary backend is LM Studio; Ollama is the alternative. Both are separate processes that AIOS communicates with over localhost.

```
AIOS LLM Engine ──HTTP/localhost──> LM Studio or Ollama ──CUDA──> GPU
```

Key behaviors:
- All models loaded at startup, kept resident in VRAM
- Health check at startup with guidance on failure
- Streaming responses via SSE
- Tool calling via OpenAI-compatible function calling format
- Connection retry with exponential backoff

### 8.2 Model Roles

Three model roles, selected by VRAM tier:

| Role | Purpose | Example |
|---|---|---|
| Classification | Intent routing, fast decisions | Qwen 3 8B Q4_K_M |
| Generation | Response generation, reasoning | Qwen 3 14B-30B depending on tier |
| Embedding | Memory search vectors | nomic-embed-text (CPU, no VRAM) |

### 8.3 AC Relevance

For the AC project, the pattern to reuse is:
- OpenAI-compatible API as the standard interface to LLMs
- Separation of classification (fast, cheap) from generation (capable, expensive)
- Embedding on CPU to preserve GPU budget for the main model
- Protocol-based backend abstraction (swap providers without code changes)

---

## 9. LangGraph Orchestration

AIOS adopted LangGraph after a spike confirmed acceptable overhead (~1ms/turn, +1 MB RSS, 1.8x LOC ratio). The agent core is a `StateGraph` where:

- Each node is an async function processing conversation state
- Edges are conditional based on intent type, tool requirements, response confidence
- The graph routes through: Router -> Skill Selector -> Tool Executor -> Response Generator -> Memory Updater

The key takeaway for AC: LangGraph provides stateful, graph-based orchestration with minimal overhead. The AC project can use the same pattern for its processing pipeline (perception -> world model update -> self-model check -> response generation).

---

## 10. VRAM Tier Configuration

AIOS supports three VRAM tiers, auto-detected at startup via `pynvml`:

| Tier | LLM Budget | Total Used | Free | Coexistence |
|---|---|---|---|---|
| 12 GB | ~5 GB (8B model) | ~10 GB | ~2 GB | None |
| 16 GB | ~6 GB (30B MoE) | ~13.7 GB | ~2.3 GB | Limited |
| 24 GB | ~6 GB (30B MoE) | ~18.7 GB | ~5.3 GB | Comfortable |

AC relevance: The AC project will need similar VRAM budgeting if it runs local models. The MoE architecture (30B parameters, 3B active per token) is particularly interesting — it gives large-model quality within small-model VRAM budgets.

---

## 11. Hardware Abstraction for Testing

AIOS design principle DP-8: "All hardware (mic, speaker, GPU, webcam) is behind protocol/ABC interfaces. Tests use mocks. CI requires no GPU."

This means:
- Every hardware interaction goes through a Python Protocol or ABC
- Test suites inject mock implementations
- CI runs without any physical hardware
- The LLM backend itself is behind an abstract `LLMBackend` interface

For the AC project, the same pattern should be applied: all external dependencies (LLM, storage, sensors) behind abstract interfaces with mock implementations for testing.

---

## 12. WorldGraph API

The application-level API that wraps all graph operations:

```python
class WorldGraph:
    # Entity operations
    def create_entity(label, properties, confidence, source) -> EntityId
    def get_entity(entity_id) -> Entity
    def find_entities(query, limit) -> list[Entity]      # vector search
    def update_entity(entity_id, properties) -> None
    def decay_importance(threshold, days_inactive) -> int

    # Relation operations
    def create_relation(source_id, target_id, dimensions) -> RelationId
    def get_relations(entity_id, direction, dimension_filter) -> list[Relation]
    def update_dimension(relation_id, dimension, weight) -> None

    # Graph traversal
    def expand(entity_ids, hops, min_weight) -> Subgraph
    def assemble_ich_modell(threshold) -> Subgraph
    def find_contradictions(entity_id) -> list[Contradiction]

    # Consolidation
    def consolidate_medium_to_long(record_ids) -> list[EntityId]
    def merge_entities(source_id, target_id) -> EntityId

    # Dimension management
    def register_dimension(name, description, range, origin) -> None
    def deprecate_dimension(name) -> None
    def list_dimensions(include_deprecated) -> list[Dimension]
```

Graph traversal uses recursive CTEs for simple paths and Python-level code for complex traversals with dimension filtering.

**Latency targets:** < 1 ms cached entity lookups, < 10 ms graph traversals, < 50 ms vector searches.

---

## 13. Memory Tools (LLM-Accessible)

The LLM manages memory autonomously through these tools:

| Tool | Action |
|---|---|
| `memory_store_fact` | Create entity + relations |
| `memory_update_fact` | Update entity or relation weights |
| `memory_search` | Vector search over entities + medium-term |
| `memory_search_conversations` | FTS search over conversation history |
| `memory_resolve_contradiction` | Apply meta-knowledge strategy to conflict |
| `memory_propose_dimension` | Propose a new relation dimension |

Rate-limited to 5 calls per turn. The LLM is prompted to watch for patterns like explicit corrections, new preferences, new facts, and contradictions.

For AC, this pattern of giving the LLM autonomous memory management is important: the system modifies its own knowledge graph, which is a form of self-modification that maps to ISM updating.

---

## 14. Configuration Pattern

AIOS uses YAML configuration with Pydantic v2 validation:

```yaml
memory:
  enabled: true
  provider: "worldgraph"
  database_path: "~/.aios/aios.db"
  medium_term_retention_days: 30
  conversation_retention_days: 90
  consolidation_trigger: "experience"   # experience, schedule, manual

llm:
  provider: "lm_studio"
  model: "auto"                         # auto-selected by VRAM tier
  api_url: "http://localhost:1234/v1"
  temperature: 0.7
  max_tokens: 1024
```

Pydantic models use `extra="allow"` on sub-models for forward compatibility, `extra="forbid"` on the root model to catch typos. The AC project can reuse this pattern.

---

## 15. Summary: What Designs to Adopt vs. What to Build New

**CRITICAL CLARIFICATION:** This table describes aios **design patterns** to reuse, NOT working code. The aios project is design-only. Every component listed below must be **implemented from scratch** for the AC project, guided by the aios design.

| AIOS Design Component | Adopt for AC? | Notes |
|---|---|---|
| Knowledge graph schema (entities, relations, dimensions) | **Yes, directly** | SQL schema exists; implement the data model from scratch following the schema design |
| Multi-dimensional weighted relations | **Yes, directly** | Design pattern; implement the dimension system |
| Self-model as subgraph traversal | **Yes, extend** | Design pattern for ISM/ESM; implement with introspection loops |
| `self_relevance` dimension | **Yes, extend** | Schema includes this; implement with bidirectional tracking |
| Inconsistency tolerance + meta-knowledge | **Yes, directly** | Design pattern; implement contradiction detection and meta-knowledge entities |
| Memory tier architecture | **Yes, adapt** | Design concept; implement with AC-specific tier boundaries |
| Context assembly pipeline | **Yes, extend** | Design pattern for EWM generation; implement with self-model feedback |
| Consolidation triggers | **Yes, directly** | Design principle; implement experience-driven consolidation |
| Dimension registry (learnable) | **Yes, directly** | Schema design; implement self-modifying dimension space |
| LLM integration via OpenAI API | **Yes, directly** | Standard pattern (this is industry-standard, not aios-specific) |
| LangGraph orchestration | **Yes, evaluate** | Consider this pattern if AC processing is graph-structured |
| VRAM tier management | **Partial** | Design consideration; adapt to AC deployment model |
| WorldGraph API design | **Yes, extend** | Design pattern; implement API with introspection and self-modification methods |
| Voice pipeline | **No** | Not relevant to AC |
| Vision pipeline | **No** | Not relevant to AC |
| Windows integration | **No** | Not relevant to AC |
| MCP skills | **No** | Not relevant to AC core (maybe for embodiment later) |
