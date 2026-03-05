# Analysis: Oizumi, Kanai & Lim — "Principal Bundle Geometry of Qualia"

**Preprint**: DOI 10.31234/osf.io/agupq_v4 (PsyArXiv, Nov 2025, v4)
**Authors**: Masafumi Oizumi (U Tokyo), Chanseok Lim (U Tokyo), Ryota Kanai (Araya, Inc.)
**Analyzed by**: Matthias Gruber, 2026-03-05
**Purpose**: Assess relevance to FMT; identify alignments, tensions, and strategic opportunities

---

## 1. Summary of the Preprint

### 1.1 Core Thesis

Oizumi, Kanai & Lim propose that the *relational structure* of qualia — not their intrinsic nature — can be rigorously characterized using the mathematical framework of **principal bundles** from differential geometry. Their central claim: when a neural encoder learns to process sensory inputs **equivariantly** with respect to a symmetry group G (e.g., translations, rotations), the neural state space Y naturally decomposes into a principal bundle structure consisting of:

- **Orbits** (fibers): submanifolds of Y traced out by applying all elements of G to a given neural state. These encode **qualia attributes** — the continuous, G-variant parameters of a percept (e.g., a cat's spatial location).
- **Quotient space** Q = Y/G (base space): the space of G-invariant identities. These encode **qualia signatures** — the stable identity of a percept regardless of its attributes (e.g., "cat" regardless of where it is).

### 1.2 Three-Level Hierarchy of Qualia

The framework yields a three-level hierarchy:

| Level | Mathematical object | Qualia concept | Example |
|-------|-------------------|---------------|---------|
| 1. Modality | Symmetry group G itself | What kind of sensory world | Vision (SO(2) for hue) vs. audition (R for pitch) |
| 2. Signature | Point in quotient space Q | Invariant identity of a percept | "Cat" vs. "dog" |
| 3. Attribute | Point on an orbit O | Continuous parameters | The cat's location, the hue's angle |

### 1.3 Key Mathematical Results

The paper proves seven propositions (with full proofs in Supplementary Information), establishing a fundamental **duality**:

**Rigid attributes**: The topological (and under stronger conditions, metric) structure of orbits is inherited directly from the symmetry group G. This structure is:
- Universal across individuals (Prop. 2: inter-subject orbit diffeomorphism)
- Rigid — dictated by physics, not learning (Prop. 1: orbit-group diffeomorphism)
- Under orthogonal representations, metrically rigid up to uniform scaling (Props. 3-4)

**Plastic signatures**: The geometry of the quotient space (relationships between signatures) is:
- Not fixed by equivariance alone (Prop. 5: quotient plasticity)
- Person-specific, shaped by learning history (Prop. 6: inter-subject quotient plasticity)
- Internally coherent for a given individual across viewpoints (Prop. 7: intra-subject quotient diffeomorphism)

### 1.4 Compositionality

The framework extends to multiple interacting symmetries:
- **Direct product** G_total = G_1 x G_2: independent/disentangled attributes (e.g., color and pose independently variable)
- **Semidirect product** G_total = G_1 ⋊ G_2: hierarchically entangled attributes (e.g., rotation affects position — the special Euclidean group SE(2))

### 1.5 Empirical Program

They propose a two-stage testing protocol:
- **Stage 1**: Test universality of qualia attributes via Topological Data Analysis (TDA) and Gromov-Wasserstein Optimal Transport (GWOT) — compare orbit structure across subjects
- **Stage 2**: Explore plasticity of qualia signatures via RSA and GWOT — measure inter-individual differences in quotient space geometry

### 1.6 Relationship to IIT

The paper explicitly contrasts with IIT (pp. 16-17). IIT derives qualia structure from *intrinsic* cause-effect structure of recurrent networks. Oizumi et al. derive it from *extrinsic* symmetries of feed-forward equivariant encoders. They note this divergence is most visible in accounts of spatial experience: IIT derives spatial structure from grid-like intrinsic connectivity; the principal bundle framework derives it from translation/rotation groups in the physical input. The authors acknowledge that "clarifying the relationship between IIT's intrinsic causal structures and our framework's group-induced geometric structures remains an important open question."

This is diplomatically significant: Oizumi is IIT's original Phi-measure co-author (Oizumi, Albantakis & Tononi, 2014). This paper represents a *partial departure* from IIT's methodology — not a repudiation, but a complementary approach that tacitly concedes IIT's weakness on qualia structure.

---

## 2. How Oizumi-Kanai Define/Model Qualia Geometrically

Their approach is **structural/relational**, not intrinsic. They explicitly avoid the "what is it like" question (Nagel's framing) and instead ask: "how are qualia *related to each other*?" This is their "structural turn" — citing Kleiner (2024) and Tsuchiya & Saigo (2021).

Key assumptions:
1. **Structure-to-structure correspondence**: The geometry of subjective experience is faithfully mirrored by the geometry of neural representations. This is a working hypothesis, not a proven fact.
2. **Symmetry organizes neural geometry**: The principal bundle structure naturally emerges when networks learn equivariant representations.
3. **Qualia = geometry of the bundle**: Modality = group; signature = base point; attribute = fiber position.

They do NOT claim to explain *why* there is experience. They model the *structure* of experience assuming it exists and corresponds to neural geometry.

---

## 3. What "Symmetry" Means in Their Context

"Symmetry" here refers to **physical transformation groups** acting on sensory inputs — the same symmetry groups from physics that Bruno Gruber works with, though applied at the level of perceptual processing rather than fundamental physics:

- **Translation group** R^2: Objects can appear at any location in the visual field
- **Rotation group** SO(2): Hues are arranged circularly
- **Pitch shift group** R: Musical pitches can be transposed
- **Euclidean group** SE(2) = R^2 ⋊ SO(2): Combined translation and rotation

The key insight: neural systems that learn to extract invariant features from environments with these symmetries naturally develop equivariant representations — and equivariant representations automatically have principal bundle structure. This is not imposed by design; it emerges from the learning pressure to efficiently encode a symmetric environment.

The paper draws heavily from **Geometric Deep Learning** (Bronstein et al., 2017, 2021) and earlier work by W.C. Hoffman (1966-1989) on Lie groups in visual perception. The connection to representation theory of Lie groups (Hall, 2015) and fiber bundle topology (Steenrod, 1999) is rigorous.

---

## 4. Comparison with FMT's Qualia Framework

### 4.1 Points of Alignment

**4.1.1 Qualia are relational/structural, not brute properties**

Both frameworks reject the idea that qualia are irreducible brute facts. FMT places them as constitutive properties of the computational level (virtual models); Oizumi et al. characterize them via relational geometric structure. Neither treats qualia as mysteriously "added on" to physical processing.

**4.1.2 The real/virtual split maps onto the orbit/quotient decomposition**

This is the deepest structural parallel. FMT distinguishes:
- **Implicit models** (IWM/ISM): substrate-level, learned, structural — "lights off"
- **Explicit models** (EWM/ESM): generated, transient, phenomenal — "lights on"

Oizumi et al. distinguish:
- **Orbits** (rigid): Structure inherited from physical symmetries — universal, not learned
- **Quotient space** (plastic): Structure shaped by learning — person-specific

The correspondence is not exact but suggestive:

| FMT concept | Oizumi et al. concept | Alignment |
|-------------|----------------------|-----------|
| IWM/ISM (learned substrate) | Quotient space geometry (learned, plastic) | Both are shaped by experience/learning |
| EWM/ESM (generated simulation) | Orbits (rigid, universal) | Partial: both relate to the "given" rather than "learned" structure of experience |
| Implicit/explicit boundary | No direct analog | FMT-specific |
| Self-referential closure | Not addressed | FMT-specific |
| Virtual qualia (computational level) | Qualia structure (geometric level) | Different ontological claims |

**4.1.3 Both predict universal structure across individuals**

FMT: The computational process (virtual models) has universal properties because it runs on substrates constrained by the same physical laws. The five-system hierarchy produces the same *kind* of experience regardless of specific neural implementation.

Oizumi et al.: Orbit topology is universal across individuals because it is inherited from the symmetry group (Props. 1-4). Two people processing the same physical symmetries have topologically identical (and potentially metrically similar) qualia attributes.

**4.1.4 Both account for individual differences in experience**

FMT: Individual differences arise from different implicit models (different learned knowledge, different ISM content).

Oizumi et al.: Individual differences arise from different quotient space geometry (different learned signature relationships). The "is my red your red?" question becomes empirically tractable.

**4.1.5 Compositionality resonates with FMT's multi-model architecture**

Oizumi et al.'s direct product decomposition (G_1 x G_2 for independent modalities) maps naturally onto FMT's claim that the explicit models integrate information from multiple implicit sources. Their semidirect product (hierarchical entanglement) resonates with FMT's account of how the EWM constructs a unified scene from features processed in different cortical areas — the binding problem.

**4.1.6 Criticality compatibility**

The paper's discussion of approximate/emergent equivariance (pp. 14-15) notes that biological neural systems only exhibit approximate equivariance, emerging from learning under metabolic and wiring constraints. This is compatible with FMT's Class 4 / edge-of-chaos requirement: systems at criticality would be precisely the ones that can learn sufficiently complex equivariant representations while maintaining the coherent dynamics needed for self-simulation.

### 4.2 Points of Tension

**4.2.1 Ontological gap: structure vs. existence**

This is the fundamental tension. FMT claims to *dissolve the Hard Problem* — it explains *why* there is experience (self-referential closure at the computational level). Oizumi et al. explicitly do NOT address the Hard Problem. They assume experience exists and characterize its structure. They adopt a "structural approach" (citing Kleiner, 2024) that sidesteps the Hard Problem entirely.

FMT would say: Oizumi et al.'s framework provides excellent tools for characterizing the *content* of qualia within the EWM/ESM, but says nothing about why there are qualia at all. The principal bundle is the geometry of the simulation's content, not an explanation of the simulation's phenomenality.

**4.2.2 Feed-forward vs. self-referential**

Oizumi et al.'s framework is built on feed-forward equivariant encoders: f: X -> Y maps inputs to neural representations. There is no self-reference, no closed loop, no model-of-the-model. The neural encoder is simply a function from stimulus space to representation space.

FMT *requires* self-referential closure — the ESM models the system that generates the ESM. Without this loop, there is complex information processing but no consciousness. The principal bundle framework would apply equally to a CNN classifying images (which has equivariant structure) and to a conscious brain — it cannot distinguish the two. This is precisely the gap FMT fills.

**4.2.3 Qualia modality vs. qualia existence**

Oizumi et al. claim that the symmetry group G defines the "fundamental nature" of a qualia modality — why vision feels different from audition. But "feels different" presupposes feeling. The group SO(2) can explain why hue is circular and not linear, but not why there is anything it is like to see a hue.

FMT's answer: Hue is circular because the EWM (virtual world model) inherits the rotational symmetry of the physical signal (electromagnetic wavelength) via the processing hierarchy. The *circularity* is structural (and Oizumi et al. characterize it beautifully). The *phenomenality* — the fact that hue is experienced at all — comes from self-referential closure.

**4.2.4 No account of altered states**

Oizumi et al.'s framework is entirely about normal perceptual processing. It has no mechanism for explaining psychedelic states, dreaming, anesthesia, or split-brain phenomena — all of which are central to FMT. The principal bundle structure should *collapse* or *distort* under psychedelic conditions (increased implicit-explicit permeability would disrupt equivariance), but the paper does not address this.

**4.2.5 Static vs. dynamic**

The principal bundle framework is fundamentally static/geometric — it characterizes the *structure* of representation spaces. FMT is fundamentally dynamic — consciousness is a *process*, not a structure. The EWM/ESM are "transient patterns of activity" that are "constructed in real time." The principal bundle describes the geometry of the space in which this process unfolds, but not the process itself.

---

## 5. Could FMT Benefit from Adopting This Mathematical Formalism?

### 5.1 YES — and substantially

**5.1.1 Mathematical formalization of qualia structure within the EWM**

FMT currently describes qualia as "constitutive properties of the computational level" and "the way the generated self-model registers its own states" — but does not provide a mathematical characterization of qualia *structure*. The principal bundle framework could fill this gap precisely:

- The EWM's representational geometry could be formalized as a principal bundle (Y, Q, G, pi)
- Qualia modalities (vision, audition, touch) correspond to different symmetry groups G
- Qualia identity within a modality corresponds to points in the quotient space Q
- Qualia variation within an identity corresponds to movement along orbits O

This would give FMT's "virtual 6th sense" claim mathematical teeth: qualia structure within the EWM is the geometry of the principal bundle induced by the equivariance properties of the implicit-to-explicit encoding.

**5.1.2 Formalization of the implicit/explicit encoding**

The encoder f: X -> Y in Oizumi et al.'s framework maps naturally onto FMT's implicit-to-explicit transfer. The IWM stores learned world-knowledge (the encoder's parameters); the EWM is the active representation (the encoder's output). The equivariance property f(g.x) = rho(g).f(x) formalizes the claim that the explicit model preserves the symmetry structure of the world.

**5.1.3 Rigid/plastic duality maps onto substrate/simulation distinction**

The orbit rigidity = substrate-level constraints (physics determines what symmetries exist).
The quotient plasticity = simulation-level learning (experience determines how signatures relate).
This maps almost perfectly onto FMT's real/virtual split.

**5.1.4 Compositionality for the binding problem**

FMT identifies binding as a core requirement (Section 2.5) and addresses it via the unified simulation (the EWM integrates features into a single scene). Oizumi et al.'s direct product and semidirect product decomposition provides mathematical tools for describing *how* this integration works geometrically — which attributes are independent (direct product) and which are hierarchically entangled (semidirect product).

**5.1.5 Testable predictions**

The principal bundle framework generates *additional* testable predictions beyond FMT's current nine:
- Orbit topology should be identical across subjects (testable via TDA)
- Quotient space geometry should vary with learning history (testable via RSA/GWOT)
- Equivariance should decrease under psychedelics (testable via the G-empirical equivariance deviation measure, G-EED)

These predictions are complementary to FMT's — they test the structural side while FMT's predictions test the dynamical/phenomenological side.

### 5.2 Caveats

**5.2.1 Scope limitation**

The principal bundle framework applies to sensory qualia (vision, audition, touch) where clear physical symmetry groups exist. It is less clear how to extend it to emotional qualia, metacognitive states, or the sense of self — domains where FMT's ESM is most distinctive. What is the "symmetry group" for anxiety or selfhood?

**5.2.2 The feed-forward assumption must be extended**

Directly adopting Oizumi et al.'s framework would require extending it from feed-forward encoders to recurrent/self-referential systems. This is non-trivial. The equivariance property f(g.x) = rho(g).f(x) assumes a well-defined input-output relation; in a self-referential system, the "input" includes the system's own prior state. The geometry may be more complex — perhaps a *gauge bundle* with a connection rather than a simple principal bundle.

**5.2.3 FMT must add, not replace**

The principal bundle framework should be presented as a formalization of qualia *structure within* FMT's virtual models — not as an alternative to FMT's ontological claims. The geometry characterizes *what* qualia look like structurally; FMT explains *why* there are qualia at all.

---

## 6. Strategic Opportunity: Follow-Up with Kanai

### 6.1 Kanai Already Knows About FMT

Ryota Kanai (Araya, Inc.) has been contacted previously about FMT. This preprint creates a natural opening for substantive follow-up because:

1. **Kanai is a co-author** — he is actively invested in this framework
2. **The frameworks are complementary, not competing** — FMT provides the ontological/phenomenological account that the principal bundle framework explicitly lacks
3. **Oizumi's partial departure from IIT** creates intellectual space — Kanai/Oizumi are open to frameworks that go beyond IIT
4. **Concrete mathematical bridge** — FMT's formalization roadmap (paper/fmt_formal/) could directly benefit from principal bundle methods

### 6.2 Talking Points for a Kanai Email

1. "Your principal bundle framework beautifully formalizes the *structure* of qualia. FMT may offer the complementary piece — an account of *why* there are qualia at all (self-referential closure at the computational level)."

2. "FMT's real/virtual split (implicit substrate vs. explicit simulation) maps naturally onto your rigid/plastic duality (orbits vs. quotient space). This structural parallel may not be coincidental."

3. "Your framework applies to equivariant feed-forward encoders. FMT predicts that self-referential closure is what distinguishes conscious qualia from mere representational structure. A CNN has principal bundle geometry too — but no consciousness. The question your framework raises but doesn't answer: what makes *some* principal bundles phenomenal?"

4. "Prediction overlap: your framework predicts equivariance should be testable via G-EED and TDA. FMT predicts psychedelics should disrupt equivariance (by increasing implicit-explicit permeability). These predictions are jointly testable."

5. "Your compositionality section (direct/semidirect products) relates directly to the binding problem — one of FMT's eight core requirements. FMT would predict that the semidirect product structure should collapse or simplify under psychedelic ego dissolution."

### 6.3 Timing and Tone

- **Do not lead with criticism.** The preprint is excellent work. Lead with what it does well and how FMT complements it.
- **Emphasize the mathematical bridge.** Kanai is a scientist; abstract philosophical claims about the Hard Problem will land less well than concrete mathematical connections.
- **Reference the existing contact.** Remind Kanai of the previous FMT correspondence to maintain the relationship thread.
- **Consider whether to wait** until the NoC review status is clearer — an accepted paper gives more credibility.

---

## 7. Citation/Positioning Strategy

### 7.1 Cite in FMT Papers

This preprint should be cited in:

1. **FMT formalization roadmap** (paper/fmt_formal/fmt-formalization.md): As a complementary mathematical framework for formalizing qualia structure. The principal bundle geometry provides exactly the kind of mathematical tools the formalization needs for characterizing the EWM's representational geometry.

2. **Full FMT paper** (paper/full/): In the Structure of Experience section (Req. 4), reference Oizumi et al. as providing mathematical formalization of qualia structure that is *compatible with* FMT's virtual qualia account. Suggested insertion point: Section 2.4 or Section 7 (comparative analysis).

3. **Trimmed NoC paper**: If the NoC review provides an opportunity for revision, adding this citation would strengthen the Structure of Experience discussion.

### 7.2 Positioning

FMT's position relative to this preprint:

> "Oizumi, Kanai & Lim (2025) provide a rigorous mathematical characterization of qualia structure using principal bundle geometry, demonstrating that symmetry groups acting on neural representations induce a three-level hierarchy of qualia modality, signature, and attribute. Their framework elegantly formalizes the *structure* of subjective experience but explicitly does not address *why* there is experience at all. The Four-Model Theory addresses the complementary question: qualia exist because the self-referential closure of the ESM creates a computational level at which phenomenal properties are constitutive. The principal bundle geometry characterizes the *content* of the EWM/ESM — how qualia relate to each other — while the four-model architecture explains why there are qualia to relate. The rigid/plastic duality of orbits and quotient spaces maps naturally onto FMT's substrate/simulation (real/virtual) distinction, suggesting these frameworks may be different mathematical perspectives on the same underlying phenomenon."

### 7.3 Do NOT Frame As

- Do NOT claim the principal bundle framework "supports" or "confirms" FMT. It is independent work with independent assumptions.
- Do NOT claim FMT "subsumes" or "includes" the principal bundle framework. They operate at different levels (ontological vs. geometric).
- Do NOT criticize Oizumi et al. for not solving the Hard Problem — their explicit methodological choice to focus on structure is legitimate and productive.

---

## 8. Key Takeaways

1. **This is the most mathematically rigorous work on qualia structure published recently.** The proofs are clean, the framework is elegant, and the empirical program is concrete. It comes from serious people (Oizumi = IIT's Phi measure; Kanai = Araya/consciousness research pioneer).

2. **It complements FMT perfectly.** FMT's greatest weakness is the lack of mathematical formalization for qualia structure within the virtual models. This framework provides exactly that.

3. **It does NOT compete with FMT.** It doesn't address the Hard Problem, self-referential closure, altered states, or the binding problem as ontological questions. It provides geometry where FMT provides ontology.

4. **The Kanai connection is valuable.** Kanai already knows about FMT. This preprint creates a natural bridge for substantive engagement — not "please read my paper" but "here is a concrete mathematical connection between our frameworks."

5. **The symmetry connection to Bruno Gruber's work is non-trivial.** Oizumi et al. use Lie groups, representation theory, and fiber bundles — the same mathematical language from theoretical physics. Bruno Gruber's work on symmetries in quantum mechanics operates in the same mathematical universe, though at the particle-physics level rather than the neural-representation level. The shared language of group theory creates a familial intellectual resonance.

6. **Citation priority: moderate.** Add to formalization roadmap and full paper at next revision. Not urgent for the NoC submission currently under review.

7. **The feed-forward limitation is the key open question.** Extending principal bundle geometry from equivariant encoders to self-referential systems would be a genuine theoretical contribution. This is where FMT's mathematical formalization could go beyond Oizumi et al.'s framework — and it would be a publishable result in its own right.

---

## Appendix: Bibliographic Details

**Full citation**: Oizumi, M.*, Lim, C., & Kanai, R.* (2025). Principal bundle geometry of qualia: Understanding the quality of consciousness from symmetry. PsyArXiv. https://doi.org/10.31234/osf.io/agupq_v4

*Note: Oizumi and Kanai contributed equally.

**Key references from the preprint relevant to FMT**:
- Kawakita et al. (2025), iScience — "Is my red your red?" using unsupervised alignment
- Kleiner (2024), Conscious. Cogn. — structural turn in consciousness science
- Tsuchiya & Saigo (2021) — relational approach to consciousness
- Higgins et al. (2022), Front. Comput. Neurosci. — symmetry-based representations for AGI
- Hoffman (1966, 1970, 1989) — Lie groups in visual perception (historical precedent)
- Taniguchi et al. (2024) — bidirectional causation between qualia structure and language emergence (Oizumi co-author)
