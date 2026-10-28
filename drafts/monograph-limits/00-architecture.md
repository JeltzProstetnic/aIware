<!--
META
status: architecture for first draft (S335, 2026-10-18)
owner: Matthias Gruber (author); drafted by Bartl from MG's Perplexity thread of 2026-10-18
sources: docs/sources/perplexity-2026-10-18/short-answer.md (full thread, 7 user turns incl. the final "instantiation is not needed" turn)
         docs/sources/perplexity-2026-10-18/claude-code-brief-fmt-physics.md (Perplexity brief + correction ledger)
         paper/full/four-model-theory-full.md (FMT v19: §3.3, §3.4.1–3.4.6, §3.6, §3.8, §4.2.2, §10.3)
         paper/cosmology/sb-hc4a.md (SB-HC4A v8: §2.3–2.5, §3.1–3.3, §4.2, §6.3–6.4, §7.3, §8.4, §9.5)
         .claude/knowledge/fmt-2015-definitions.md (Bezugssystem chain, regress, falsity principle)
         2015 book pp. 16–18 (truth, "auch die Mathematik ist im Grunde eine Sprache"), 89–92 (Gödel, serialization),
         101–102 (Turing, halting problem of serialization), 266–267 (induction/deduction, unserializable models)
-->

# No Outside — architecture of the monograph

**Working title:** *No Outside: The Limits of Mathematics and Logic From Any First-Person Perspective*

## 1. The thesis in one paragraph

Mathematics and logic are languages in which self-modeling observers serialize the regularities of their
world-models. Every observer that uses them is a proper part of what it describes, runs on fewer resources than
the whole, and cannot represent the apparatus that generates its own representations. From these three facts —
**embedding, resource deficit, and the absence of the generator** — follow all the limits that matter:
incompleteness and undecidability, the uncomputable continuum, the impossibility of certifying randomness or
independence from inside an experiment, the inability to tell surplus structure from world structure, the
failure of first-person evidence to discriminate between hypotheses about one's own origin, and finally the
dependence of the very distinction between *a description* and *an instance* on the side of the generating
relation from which it is drawn. "First-person perspective" means **any** embedded perspective — human, animal,
machine, or a creature inside a structure laid out statically on a disk. The limits are not human weaknesses.
The core two (no perspective holds its own current generation, as a whole, as content; no part can certify its
own description of the whole complete) hold for every perspective there can be, because there is no perspective
from outside; capacity, irreducibility and incompleteness hold wherever their conditions hold (S336 hole 5).

**The unifying principle, stated once and used in every chapter: the generator never appears completely in
what it generates** (corrected after writer B: arithmetization shows a formal system *can* represent its own
proof relation; what fails is complete appearance with consistency kept). A reference system cannot be content of itself (the regress); a formal system cannot contain a
complete and consistent account of its own derivations (Gödel); a computation cannot shortcut itself (Turing,
irreducibility); an observer cannot step outside the causal web to randomize (measurement independence); the
update cannot appear as an object, only as order (time); a self-model cannot represent, as a whole and as cause, the substrate producing
it (FMT's unrepresentable apparatus, §4.2.2); and a mind cannot weigh hypotheses about its own generator
(Boltzmann). FMT already carries this principle at organism scale (§3.3 regress, §3.8 meta-problem, §4.2.2 felt
freedom, §10.3 "inherent limits of inside-modeling"); SB-HC4A carries it at cosmic scale (§6.4 inexpressibility,
§9.5 cognitive ceiling). The monograph states it for mathematics and logic, which is where neither paper goes.

**What survives the limits — the positive half, and the book must not end in scepticism:**
1. **Negative results travel between perspectives; positive ones do not** (MG's principle, 2026-08-06:
   *absolute falsehood does not require absolute truth*). An inconsistency between a system and its own admitted
   input is decidable locally and is inherited by every successor system that keeps the input.
2. **Relational structure is shareable; absolute encoding is not.** FMT §3.4.2 says this of qualia (the
   similarity structure of a colour space transfers across brains; which state is *my* red does not). The same
   split holds for mathematics: the relational structure a formalism captures is what different observers can
   share and check; what the symbols *are* — the ontology behind the structure — stays per-perspective.
   Mathematics is the most shareable part of a world-model precisely because it carries structure and drops
   encoding.
3. **Inside a scope, laws are compressed data, not assumptions.** Level-relativity makes a regularity a
   compression valid within a scope; it does not make it a fiction.
4. **Every theory is built on cuts it cannot fully sustain, and the cuts are the price of understanding at all**
   (MG, 2026-10-18, verbatim: *"the level distinction in FMT between implicit and explicit is at its core a
   didactic pattern, not an attempt at absolute truth. the level distinction imports the semipermeable boundary
   (thereby contradicting itself) for the explanatory power it lends that would otherwise be inaccessible, not
   unlike a physical theory needs to separate time and space, or my cosmology theory needs to separate the
   boundaries from their projections. humans cannot understand absolute truths due to their limited brains that
   are embedded in what they try to understand."*). The book applies its thesis to its own author's theories:
   FMT's implicit/explicit levels, physics' time/space split, SB-HC4A's boundary/projection split, and the
   description/instance distinction are each a cut that an embedded mind must make to understand anything, and
   each is contradicted somewhere by the theory that makes it (a level boundary that is permeable is not a clean
   level boundary). Using a cut is not the error; mistaking it for the world is — the same reification error as
   Chapter 1's patch error, now admitted from inside. This is the book's honesty about itself, and it must be
   stated as a position, never advertised.

## 2. Voice, register, format — binding for every writer

- **Author voice:** Matthias Gruber (MG), first person singular used sparingly ("I"), as in the SB-HC4A paper.
  English. Direct, technical, dry. No ego, no Spock, no grandiosity. MG is a pure intuitionist (architectural
  intuition over notation): carry arguments in concepts and concrete examples; formulas only where they are the
  clearest statement (Bell's measurement independence `P(λ|x,y) = P(λ)` is one of the few earned).
- **Banned register** — read `/home/jeltz/aIware/.claude/knowledge/prose-register.md` in full before writing.
  In short: no self-narration of the document ("This chapter argues…", "As we will see", "Read together",
  "We now turn to"); no throat-clearing ("It is worth noting", "Importantly,", "Crucially,"); no "load-bearing";
  no "bite"; no not-X-but-Y pairs for rhythm (test: does the sentence say the same thing with the pairing
  removed? then cut it); no rule-of-three triads for rhythm; no empty superlatives ("the deepest lesson");
  no pre-answering hypothetical critics inline; no narrating revisions; no advertising the text's own honesty
  or care ("stated carefully here"). Epistemology is this book's **subject matter** — argue it; never lecture
  the reader on how science or credibility works.
- **Length and posture:** every "necessary", "fundamental", "must" gets its reason in the same paragraph or is
  deleted. One example per point. Cut what performs competence.
- **Genuine caution is content and stays:** "consistent with", "I do not claim", stating what would refute a
  claim, bounding a result once and flatly.
- **No process meta:** no mention of Perplexity, Claude, AI, compaction, "the conversation", "the thread".
  The objections Perplexity raised are presented as objections (in the third person: "One reply is…", "The
  standard answer is…"), and answered or conceded on their merits.
- **FMT discipline (hard):** say "two kinds of models / model kinds", never "four modules". Criticality is a
  signature, never a requirement for consciousness. Never "epiphenomenon" for qualia without "side effect"
  gloss. No capability barrier between conscious and unconscious processing (price, never barrier). Do not
  claim any particular simulation is conscious. Do not claim FMT has been empirically confirmed.
- **Citations:** use only the works in §5 below, in author–year form (Gödel, 1931). Never invent a citation, a
  page number, a quotation, or a result. If an argument wants support not in §5, write it without the citation.
  Self-citations: Gruber (2015) = *Die Emergenz des Bewusstseins*; Gruber (2026a) = FMT v19; Gruber (2026b) =
  SB-HC4A v8.
- **Format:** Markdown. `# Chapter N — Title`, `##` sections, no deeper than `###`. No bullet-list chapters —
  prose; lists only for genuine enumerations. No bold-for-emphasis inside running prose except a defined term at
  first use. Target 2,800–3,500 words per chapter.

## 3. Chapter plan

### Front matter (writer A)
- Draft blockquote: `> **Draft v0.1 (2026-10-18). Not for circulation.**`
- **Preface** (~600 words): the origin question in MG's words, rendered as prose — *do we know that mathematics is
  a language, that a mathematical model describes what its author thinks he is talking about, that it uncovers
  logic hard to see by intuition, and that it imports two kinds of error: ordinary modeling error, and the error
  of patching the mathematics with new objects whenever it gets stuck?* State what the book claims in four or
  five plain sentences (thesis §1). State the scope: "first-person" = any embedded perspective. No chapter
  roadmap prose ("Chapter 3 shows…") — instead end with a short plain table of contents line or nothing.

### Part I — Mathematics as a language of models

**Chapter 1 — Is Mathematics a Language?** (writer A)
- Mathematics is a language with a built-in proof checker (Gruber 2015 p.18: *"auch die Mathematik ist im Grunde
  eine Sprache, wenn auch eine sehr streng geregelte"* — in algebra 1+1 can be 0 or 10 depending on the system).
  The checker is its power: one cannot say anything whatever in it. It also fixes which questions can be asked:
  whoever's toolkit is differential equations sees dynamical systems everywhere.
- The 2015 epistemic chain, compactly: data → information (codeable) → knowledge (information assigned to a
  reference system) → meaning (relation to a chosen reference system). **Bezugssystem = model** (2015 p.21). So a
  mathematical statement has meaning only relative to a model; the formalism is a serialization of model
  structure (2015: communication is serialization; the receiver reconstructs the model). Didactic pattern #40:
  there is more meaning than meaning — the number 1.2 has many meanings across contexts, *c*-the-physical-
  constant almost none; a corpus of mathematics written by model-bearing systems is a record of their model
  structure.
- Two error types (MG's original question). (i) Ordinary modeling error — every model simplifies (FMT §10.3
  "every model has modeling error"). (ii) Patch error — adding objects to rescue a formalism: epicycles;
  renormalization (Dirac's objection, Feynman's "dippy process" — keep as attributed remark, no citation);
  Lakatos's monster-barring (Lakatos 1976); Duhem–Quine (auxiliary assumptions); Redhead's surplus structure
  (Redhead 1975). Known in philosophy, rarely taught.
- **The correction that sharpens MG's claim instead of weakening it:** a patch does not poison the consistency of
  the mathematics — complex numbers are a conservative extension of the reals, consistent if the reals are. The
  damage happens in the **mapping** from formalism to world: once a patch is in, the formalism no longer tells
  which of its structures belong to the world and which to the representation. **First limit, stated here:** no
  formalism certifies its own ontological reading. Only conceptual analysis or experiment sorts surplus from
  structure, and both are done from a perspective.
- Close on the methodological consequence for any science of the mind: get concepts and their logic right,
  then formalize; every new mathematical object either predicts something new or is labelled bookkeeping
  (state flatly, one sentence, no lecture).

**Chapter 2 — Counting and Its Imports** (writer A)
- Only the natural numbers count. Every extension imports a mini-model with its own rules (MG: "complex numbers
  are not numbers and also not number pairs; they are objects under different rules of computation; mini
  models"). Negatives model debt or direction; rationals model division of wholes; reals model an idealized
  continuum (Dedekind cuts, uncountably many); complex numbers model rotation-and-scaling (pairs of reals with a
  multiplication rule; equivalent to 2×2 rotation-scaling matrices).
- The ladder gets *worse* upward in a specific sense: almost all real numbers are uncomputable (Turing 1936
  defined computable numbers as those whose digits an algorithm can produce; the computable reals are
  countable). If the world is a computation (SB-HC4A), the continuum is the largest imported fiction in physics,
  larger than *i*. MG's point "driven ad extremum" and agreed: aim the critique at the reals.
- **Numbers are algorithms.** A computable number is an algorithm (Turing 1936). Multiplying by e^{iθ} is a
  rotation operator in the costume of a number. MG: "some numbers are actually algorithms; multiplying by them
  does more than multiplication; algorithms and numbers are exchangeable, so we trick ourselves even more."
  Correction to keep: an algorithm that represents a value is not identical to the value under every
  interpretation; multiplying by an encoded constant is not free computation (precision, access, encoding and
  decoding cost). The trick is real where the costume hides the operation, not because numbers and programs
  are the same thing.
- **The complex-number case study, done right.** (a) Real-valued formulations of quantum theory: Renou et al.
  (2021) showed that real quantum theory with the standard tensor-product composition makes predictions that
  experiment rejects; later real-vector-space formulations with a modified composition rule reproduce complex
  quantum theory (Hoffreumon & Woods, 2025). (b) Those formulations still carry an operator J with J² = −I —
  multiplication by *i* renamed. So the represented structure (a generator of rotation in a two-dimensional
  state plane) survives every change of notation, and the notation never says whether that structure is
  fundamental or emergent from oscillators. (c) MG's reading: in a cellular-automaton world with holographic
  emergent spacetime, continuous rotation and phase need not exist at the bottom — only oscillators and discrete
  cycles ('t Hooft 2016; continuous rotational symmetry broken at lattice scale, recovered approximately at
  large scale). The disagreement then is continuous phase vs discrete cycles — an argument against the
  continuum, the chapter's own target, and not an argument that interference phenomena are fictions.
- Close: the costume problem in one sentence — a formalism that works hides which of its objects are the world
  and which are the costume; the only remedy is to keep asking of each object what it predicts.

**Chapter 3 — Why Mathematics Works Where It Works** (writer A)
- Wigner (1960), "unreasonable effectiveness". MG's answer: we live in a subset of the universe in which simple
  logic works — otherwise there would be no brains that survive by predicting likely futures — while that subset
  leaves enough complexity and uncertainty for success and failure to mean anything. Anthropic selection on the
  observer, not on the mathematics.
- Second factor: selection on the mathematics — mathematicians have explored a vast range of consistent
  structures and we remember those that fit (coverage plus survivorship).
- Third factor, FMT's: mathematics serializes world-model regularities; it works on what world-models were built
  to compress, and it is silent beyond the scope of the compression. "Unreasonable" becomes "reasonable within
  scope".
- Fourth: the cognitive ceiling (SB-HC4A §9.5). If observers are Class 4 systems, the most complex pattern they
  can detect or formalize is Class 4 (Class 4 = the expressibility ceiling of finite rules, SB-HC4A §2.4). A world
  that exceeded it would appear Class 4 to them. The success of mathematics therefore cannot certify that the
  world is mathematical; it certifies that the world, *as accessed by such observers*, is compressible to their
  ceiling. State MG's own concession from §9.5: "I do not know how to resolve this objection from within. I am
  not sure it can be resolved from within." — as a position, not a quote of a paper.
- Tegmark's Mathematical Universe Hypothesis (Tegmark 2008) as the opposite pole — every consistent structure
  exists — and why the perspective argument does not need it (selection, not admission; SB-HC4A §3.2).
- Example that little logic produces quantum-like structure: the spacing statistics of the Riemann zeta zeros
  match eigenvalue statistics of random Hermitian matrices, the statistics of chaotic quantum systems without
  time-reversal symmetry (Montgomery 1973; Odlyzko 1987). MG: very little logic can lead to our universe given
  the correct implementation. Concede: primes are static, and "given the correct implementation" is where the
  content of the claim lives.

### Part II — Logic seen from inside

**Chapter 4 — The Base Case: Where Logic Comes From** (writer B)
- The regress argument (2015 p.21–22 → FMT §3.6): knowledge is information assigned to a reference system; a
  reference system is built from prior assignments; the regress ends only in a layer never assigned by
  interpretation — grown by plasticity and selection. That layer is implicit. Logic and its axioms are no
  exception: the explicit rules of inference are serializations of implicit competences that were never derived.
- Axioms are not self-evident truths; self-evidence is how a consolidated implicit model presents in the
  explicit layer (FMT: consolidation, the Scribe; implicit models resist explicit revision). Kant's a priori
  ("water is wet", "the bachelor is unmarried", 2015 pp.16–17) relocated: analytic truths are agreements of a
  language community, relative to usage — 2015's own argument (14 billion people in the 23rd century).
- Induction and deduction (2015 pp.266–267): induction derives a theory from observations (the poisonous-mushroom
  case — learned from a third person's death, because a deadly poison permits no reinforcement trial);
  deduction applies the theory to a new case; post-hoc rationalization belongs to the same machinery. Logic
  as a cultural formalization of an animal capacity — syntax "invented" by deriving rules from a naturally grown
  language.
- **Consequence:** a system whose entire content is assigned at run time has no base case (FMT §3.6). There is no
  logic without a non-logical ground, and no observer has access to its ground as content.
- Keep: the 2015 decoupling of knowledge from truth — knowledge is information assigned to a reference system,
  accurate or not; false knowledge exists. Do NOT mention any internal contradiction of the 2015 book (MG
  ruling S288).

**Chapter 5 — The Limits on Any Embedded Description** (writer B; recast S336 hole 5)
- Generalize SB-HC4A §6.4 from "physical theories of the universe" to **any description made by any observer
  that is part of what it describes**:
  0. **Unconditional core** — (i) no perspective holds its own current generation, as a whole, as content, ever;
     (ii) no part can certify its own description of the whole complete (checking would require holding the
     remainder). Hold in a small, simple world.
  1. **Capacity** (world-conditional: wherever the whole is incompressible) — a proper part cannot store a
     complete description of an incompressible whole (Kolmogorov 1965; Chaitin 1966; counting argument).
  2. **Irreducibility** (world-conditional: wherever a describer does irreducible work; "no general shortcut"
     only for the idealized unbounded describer, finite describers hand back to capacity) — where no shortcut exists, a subsystem holding the exact rule obtains the future only by
     running it, more slowly than the whole runs itself (Wolfram 2002; Class 4; Rule 30 vs Rule 90, SB-HC4A §2.3).
  3. **Incompleteness** — formal systems expressive enough for arithmetic cannot prove all truths about
     themselves and cannot prove their own consistency (Gödel 1931); Turing's halting problem (Turing 1936).
     2015 pp.89–90: the limits are inherited upward by expressive power — mathematics, algorithmics, natural
     language. Classification of cellular automata into behavioural classes is itself undecidable (Culik & Yu
     1988).
  4. **Constitutive** (its own kind, not about information) — a description of a process, however complete, is
     not an instance of it (FMT §3.4.5; SB-HC4A §6.4). Flag that Chapter 14 returns to the constitutive limit and finds it perspectival — state that as a
     forward claim in one plain sentence, no "as we will see".
- **Against the mystical reading (MG 2015 p.92, keep the spirit, drop the sneer):** Gödel says nothing mysterious
  about brains. Humans are inconsistent and make errors; Gödel constrains consistent formal systems. The limit
  that applies to observers is structural (0 unconditionally; 1, 2 under their conditions; 4), not a hidden super-power.
- **The halting problem of serialization (2015 p.102):** whether a mental model can be serialized can only be
  judged by trying; success answers the question, failure does not. *We cannot decide in advance whether we will
  be able to explain what we think.* And some models are too complex, too multimodal or too individual to
  sequentialize at all (2015 p.267: the untranslatable joke). FMT §10.3: language linearizes non-linear
  phenomena. Mathematics is the most disciplined serialization and inherits the same limit.
- Quasi-infinity (SB-HC4A §4.2) as the observer's condition: effectively unbounded from inside, finite in
  accessible information from any point.

**Chapter 6 — Falsity Without Truth** (writer C)
- MG's principle (fmt-2015-definitions.md §3, the parts marked as standing — do NOT touch the deferred
  monograph-correction material): a reference system can be shown inconsistent with its own admitted input
  without any privileged reference system existing. Falsity is a within-system-against-input relation: cheap,
  locally decidable, inherited by every successor that keeps the input. Truth would need a standpoint outside
  all reference systems, and there is none.
- Flat earth → roughly a ball → "it could still turn out to be a 6D cube with a 3D ball sub-object" (MG):
  subsumption does not make flat true again; successor frameworks inherit the refutation.
- It is a gradient, not a binary: falsehoods are more resistant to revision than truths. Two independent
  mechanisms: (a) evidential — a refutation is pinned by one contradiction, a positive claim is exposed to every
  better-fitting competitor; (b) social ratchet — a falsity ruling accumulates a justificatory apparatus; undoing
  it is "a second conversion of already 180° changed knowledge". Prediction: resistance scales with the cost of
  the original conversion — continental drift and *H. pylori* were cheaply rejected and came back.
- FMT reading: falsity rulings get consolidated into the implicit layer (reflex: "that was debunked"); positive
  models are held explicitly and provisionally.
- Logic's place in this: negation and inconsistency are what logic can carry between perspectives. Every
  perspective can verify that a given perspective contradicts its own input; no perspective can verify that a
  model is the world. Popper is the obvious neighbour — state the difference: the asymmetry here is derived from
  the reference-system architecture, not adopted as a methodological rule. (Popper may be named without a
  citation-list entry only if §5 has it — it does: Popper 1959.)
- Paradox handled gracefully: a degree-of-agreement measure gives the liar an intermediate value instead of
  diverging (2015 — may be mentioned without page cite as "a measure of agreement between reference systems").

**Chapter 7 — The Apparatus That Cannot Appear** (writer C)
- FMT §3.4.3 observability constraint: the explicit self-model's horizon is bounded by the explicit world-model;
  no internal vantage describes the system's processing without that description being part of what is
  processed. §3.8 meta-problem: the implicit models generating the simulation are not part of it. §4.2.2: the
  simulation models world, body, others and self — and not the apparatus generating it (didactic pattern #37:
  "the one thing missing from your world").
- Felt freedom (FMT §4.2.2): a choice whose cause cannot appear is assigned to the self, where the regress
  ends; felt freedom is what an origin feels like from inside. Scope guard: whether the system *is* free is a
  physics question FMT declines; the account is neutral between determinism and indeterminism.
- **Extension proposed in this book (mark it in the text as a proposal, plainly): felt logical necessity has
  the same structure.** An inference's generator — the implicit competence that performs it — cannot appear in
  the scene in which its conclusion appears. The conclusion therefore presents as compelled by the content
  itself ("it follows"), not as produced by an apparatus. Necessity is what an inference feels like when its
  producer is absent. This explains why logical truths feel as if they hold from no perspective at all, while
  being produced by one. Bound it: it explains the phenomenology of necessity, not the validity of any
  inference; validity is assessed by the falsity criterion of Chapter 6 (a valid rule never takes true input
  to contradiction).
- Self-reference paradoxes (liar, Gödel sentence) as the formal shadow of the architecture: a system that tries
  to make its own current generation into content produces either incompleteness or contradiction.
- The cognitive ceiling again (SB-HC4A §9.5) as the apparatus-limit at cosmic scale: the model might be the
  shape of our cognition projected; the theory predicts its own potential unfalsifiability — either its best
  confirmation or its strongest objection, undecidable from inside. Close with FMT §10.3: any theory of
  consciousness generated by a conscious system carries a residual blind spot — and the same holds for any
  logic generated by a logician.

**Chapter 8 — Useful Contradictions: The Cuts Every Theory Needs** (writer G)
- Opens from MG's statement (§1 point 4) as the author's own position, in his voice.
- A cut is a separation a theory introduces so a limited, embedded mind can hold the domain at all: time vs
  space in physics (the signature's minus sign is the residue of the cut, Chapter 11 returns to it); boundary
  vs projection in SB-HC4A (substrate vs decompressed interior, §6.2, §8.2–8.3); implicit vs explicit in FMT
  (§3.3, §3.6) — and the cut imports a semipermeable boundary (permeability, §3.6), which contradicts the
  cleanness of the levels it separates. The theory keeps both because the explanatory power (anosognosia,
  psychedelics, the meta-problem) is unavailable without the cut — anaesthesia is accounted for by stored vs
  running within one level (structure spared, activity suppressed; S336 hole 4), not by the cut's level reading — and the phenomena
  at the boundary (leaks: blind-spot filling, phosphenes) are unavailable without the permeability.
- A cut is a didactic pattern in the strict sense: a device for understanding, judged by what it lets a mind
  see, not by whether the world has the seam. Relation to Chapter 1: a patch is an object added to rescue a
  formalism; a cut is a separation added to make a domain thinkable. Both are legitimate tools and both become
  errors when reified.
- Why the cuts contradict themselves, and why that is expected rather than a defect: an embedded observer with
  fewer resources than the whole (Chapter 5) must compress; compression by separation leaves a residue where the
  separated parts interact; the residue shows up in the theory as a boundary that is both there and permeable.
  Absolute truth would require no cut, which would require the whole as content — impossible for a part
  (Chapter 5, capacity; Chapter 7, the apparatus). "Humans cannot understand absolute truths due to their
  limited brains that are embedded in what they try to understand" — and the same holds for any embedded mind.
- How to use a self-contradicting cut without being misled: keep the contradiction visible; state for each cut
  where it fails (FMT's open question 1 — "are all four models virtual?" — is that statement for the
  implicit/explicit cut); never derive a conclusion that depends on the cut being absolute. The falsity criterion
  (Chapter 6) still applies: a cut is rejected when predictions that depend on it contradict input, not because
  it has a seam.
- Consequence carried into Chapter 14: description vs instance is also a cut, and its perspectival character
  (Chapter 14) is the same phenomenon.
- Do NOT write "FMT's levels are false" or "FMT is just a metaphor": the claim is that the level distinction is a
  cut whose explanatory power is real and whose absoluteness is not claimed. Predictions built on it stand or
  fall by experiment.

### Part III — Physics from inside

**Chapter 9 — Compressed Data Is Not an Assumption** (writer D)
- MG's suspicion, stated at full strength: the laws we have — GR, QM, locality, reversibility, probability
  conservation — describe our level only; GR is incomplete; QM matches reality within its scope "but only for
  that scope"; QM is a probability calculus without ontology (QBism; Hardy 2001 axioms — QBism may be named
  without citation). MG's sharper wording in the source: QM "is not a physical theory".
- The reply that must be absorbed: "X only holds at our level" does not make X an assumption, and an assumption
  is not thereby false. A law that holds at our level is compressed data. The fallacy is reification —
  mistaking the compression for the fundamental thing — and using it is not the fallacy. Discard every
  level-bound regularity and a substrate theory has nothing left to reproduce and becomes as untestable as the
  theories it criticizes.
- The productive programme: list the regularities observed at our level; deny that any is fundamental; find a
  substrate that reproduces them. That is exactly the SB-HC4A method (Class 4 by elimination, SB-HC4A §3.2–3.3,
  conditional on substrate determinism).
- Precision about QM: non-relativistic QM is mathematically consistent; the infinities live in QFT; not
  predicting GR is incompleteness, not inconsistency — MG conceded this ("what I meant to say"). Keep MG's
  stronger point: matching reality closely within a scope tells us nothing about how wrong a theory is
  fundamentally, until a deeper theory shows where the scope ends.
- Bridge to Chapter 10: the remaining question is what an embedded observer can and cannot establish about the
  substrate *by experiment* — and experiments are performed from inside.

**Chapter 10 — Randomness, Independence, and the Observer Inside the Experiment** (writer D)
- **Ontic vs effective randomness** (SB-HC4A §2.3–2.4): a deterministic finite rule cannot produce output more
  complex than itself; Class 4 rules produce effective randomness (Rule 30, used as a pseudorandom generator).
  An embedded observer has fewer resources than the computation it is part of, so — **structural limit** — it
  can never distinguish ontic randomness from the effective randomness of an irreducible deterministic
  substrate. Quantum randomness can be read as effective ('t Hooft 2016).
- **Measurement independence.** Bell-type reasoning needs `P(λ|x,y) = P(λ)`: settings uncorrelated with the
  hidden state. This is not an assumption of "true randomness" and determinism alone does not violate it.
  QM does not require true randomness either (Bohmian mechanics, many-worlds are deterministic). MG's point:
  we have no certified true randomness with which to randomize experiments that probe randomness-dependent
  theories, and no way to know how tightly we are coupled to any quasar. Cosmic Bell tests (Rauch et al. 2018)
  exclude classes of recent common-cause explanations under stated assumptions — not every common dependence.
  **First-person limit, stated:** no observer can certify, from inside, its independence from the system it is
  part of. Balance: the inability to certify independence is not evidence of coupling, and a theory permitted to
  fit arbitrary setting–state dependence predicts nothing. A specific superdeterministic model can be testable
  (Hossenfelder & Palmer 2020). Wheeler's one-electron idea — a historical possibility (Feynman's Nobel lecture
  1965 records it, with his objection about electron/positron abundance), not a measured coupling.
- **Locality and its price.** If spacetime is an emergent projection of a lower-dimensional computation, cells
  adjacent in the substrate need not be adjacent in emergent spacetime; locality at our level is no evidence of
  locality at the bottom — Bell's nonlocality option, the route SB-HC4A takes (holographic nonlocality, not
  setting–state fine-tuning; SB-HC4A §6.5, §8.4). Economy: with a nonlocal projection, superdeterminism is not
  also needed.
- **No-signalling** is measured at our level, not provable as fundamental (MG: without a GUT we cannot know
  information transfer is impossible). A lattice gives a preferred frame, so faster-than-light influence need
  not create paradox. Bancal et al. (2012): a specified class of models explaining Bell correlations by
  finite-speed hidden influences predicts correlations usable to signal faster than light. Scope it: this
  constrains that class, not every nonlocal projection. Result: a fork that makes the substrate view testable —
  finite-speed influences imply in-principle signalling, a genuinely nonlocal projection implies none.
- **CA physics status, fairly:** D'Ariano & Perinotti (2014) derive the Dirac equation from quantum cellular
  automata under unitarity, locality, homogeneity and discrete isotropy (the automata are already quantum; free
  fields); 't Hooft's (2016) CA interpretation: classical states evolving by permutations, QM as a tool — his
  own verdict that a convincing model is still lacking; Wolfram (2002) programme. Free fields from automata: done.
  Interacting fields with gravity: no programme has it. Turing completeness guarantees that Bell-violating
  behaviour *exists* in some automaton, not that random rules produce it (countably many finite rules;
  existence is cheap, the minimal natural rule is the problem).

**Chapter 11 — Time Without a Clock** (writer D)
- MG's claims: time is not obviously a dimension; "we all move at c through spacetime" is an asymmetry that
  should make us reconsider an egocentric view of time; the metric signature is an assumption needed for GR;
  dynamics are not fundamental, they emerge as a point of view after the fact.
- Corrections to absorb: (a) the four-velocity has magnitude c by construction (differentiation by one's own
  proper time) — a bookkeeping tautology, exactly the kind of formal artefact the book warns about, and
  undefined for photons. (b) The signature predates GR (Maxwell's wave operator, Minkowski 1908); it is the
  geometric form of an invariant speed. A substrate with bounded update speed gives a dependency cone; that is
  not by itself Lorentz symmetry (D'Ariano & Perinotti need further assumptions and a limit). So the signature is
  a trace of bounded information speed *at our level*, which is consistent with MG's view, not against it.
  (c) One time dimension: with more than one, the governing equations become ultrahyperbolic and prediction
  fails (Tegmark 1997) — MG's own anthropic argument applied: predicting brains need one time direction.
- **In a computation, time is not a dimension; it is the update.** Space is the lattice; treating time as a
  fourth axis is a representation; the minus sign is what remains of time's difference from space.
- **The arrow is inherited and coarse-grained** (SB-HC4A §8.4; FMT §3.4.4): reversible substrate, arrow from
  boundary condition plus coarse-graining (Albert 2000, Past Hypothesis); the cognitive arrow is inherited from
  the thermodynamic one — one arrow, the modeler inside the layer that has it.
- **Felt order is constructed** (FMT §3.4.4): postdiction — colour phi (Kolers & von Grünau 1976), cutaneous
  rabbit (Geldard & Sherrick 1972), flash-lag (Eagleman & Sejnowski 2000); Dennett & Kinsbourne (1992): no fact of
  the matter about substrate finish lines. Each frame of the simulation assigns order to its content; order
  answers to coherence, not arrival.
- **Becoming is irreducibility seen from inside** (SB-HC4A §8.4): the whole block can satisfy a timeless
  fixed-point condition while, because Class 4 dynamics admit no shortcut, an embedded observer can apprehend the
  block only by living through it. Barbour (1999) as neighbour.
- **Reversibility, probability, J — corrected:** normalization of probability does not imply reversibility (two
  inputs to one output conserve total probability and lose information). For a finite autonomous deterministic
  total state, trajectories end in cycles and the update is bijective on the cycle — a fact about the total
  state, not about an observer's coarse variables. J as ontology ("rotation in state space is fundamental") can
  be rejected; J as compression of measured interference, phase relations and E = hf is data. Stone's theorem
  (Stone 1932) is conditional on a strongly continuous one-parameter unitary group; it derives no fundamental
  time and no clock. Reversibility ≠ time-reversal symmetry. MG explicitly never questioned apparent local
  reversibility at our level — keep that.
- **Three properties no observer can check (S336 hole 6, new section before the closing one):** substrate
  reversibility (follows from determinism + finiteness), determinism (Ch 10), finiteness (Ch 12) and measurement
  independence (Ch 10) are undecidable from inside; SB-HC4A keeps reversibility, determinism and MI as declared
  architectural choices justified by what they buy, not findings.

### Part IV — The inside of a structure

**Chapter 12 — Infinity and Quasi-Infinity** (writer E)
- There is not the smallest piece of evidence that physical infinity exists (MG). An idealization using infinite
  objects is not refuted by that, nor confirmed by its usefulness — both halves.
- Quasi-infinity (SB-HC4A §4.1–4.2): effectively unbounded for any internal observer, finite information from any
  point; three bounding surfaces (horizons, the Planck floor, curvature termini). It is the only infinity an
  embedded observer can have.
- MG's "Möbius-like quasi-infinite grid with co-evolving rules", no beginning or end. Consequences to state
  honestly: finite-but-unbounded deterministic systems end in cycles (Chapter 11); co-evolving rules need
  meta-rules and the regress has to stop in a fixed logic (the base case of Chapter 4 again, at cosmic scale);
  "any large grid produces our world by chance" — most rules settle into Class 1/2, and countable rules vs
  uncountable infinite configurations are different objects to count.
- Many-worlds: MG rejects it ("infinity times infinity", unscientific). Balance: its defenders say it removes
  the collapse postulate rather than adding structure, and that branch counting is ill-defined; its real
  difficulties are the Born rule and the preferred basis; the "unscientific" charge applies equally to any
  interpretation that predicts no deviation from QM, the CA interpretation included. Do not assert that
  finite Hilbert dimension makes branches finite (unjustified without a definition of branching).
- Nothingness (SB-HC4A §3.1): something exists; a located nothing is a something; an unlocated nothing is
  refuted by whoever asserts it — the observer as counterexample. Connects: the boundary is never an element of
  the domain (SB-HC4A §5.3, §9.5).

**Chapter 13 — The Evidential Poverty of the First Person** (writer E)
- MG: the Boltzmann brain is one of the most consistent and logical theories in physics; our own point of view
  allows no proof against solipsism and no outside view of anyone else's qualia; our local, temporally finite
  existence may be one temporary thought of a larger Boltzmann-brain mechanism, instantiated similarly for every
  conscious observer.
- What first-person experience establishes: that at least one experience occurs. It cannot select between an
  embodied history, a simulation, a thermal fluctuation, or a timeless instantiation — each can be stipulated to
  include that experience. Inability to disprove solipsism limits discrimination; it is not evidence for a
  mechanism.
- Canonical Boltzmann brains (observers fluctuating out of a thermal bath) vs MG's broader "temporary thought of
  a larger mechanism" — the latter is a hypothesis about nested or timeless instantiation, not a thermal model.
- Carroll (2017): cognitive instability — a theory making our evidence overwhelmingly unreliable undermines its
  own justification. Elga (2025) disputes that this settles it. Our universe
  is far more ordered than a lone observer needs — the standard argument against pure chance; note it is itself
  an observer-measure argument.
- **FMT's diagnosis — the book's contribution in this chapter:** the first person cannot weigh hypotheses about
  its own generation because the generator is exactly what a self-model cannot represent (Chapter 7). The
  evidential poverty is the unrepresentable apparatus once more. Every theory that counts observers across a
  space no inhabitant can reach (canonical thermal Boltzmann, Tegmark, many-worlds weighting, "everything occurs
  somewhere", cross-cycle counts) owes an **observer measure**: what implements observers, which histories occur,
  how occurrences are weighted. Theories applied from inside owe none; they are tested by refutation against
  admitted input (Ch 6). Cost: excess order then refutes nothing about our origin, only a hypothesis that brings
  its own measure (S336 hole 1).
- Other minds (FMT §3.4.3): doubting an architecturally matched artifact's report while crediting a human's needs
  an independent reason — the general problem of other minds, identical for every human but oneself.

**Chapter 14 — The Worm on the Disk** (writer F)
- MG's thought experiment: reproduce the whole life of *C. elegans* in silico; however often it is instantiated,
  in whichever direction run, and even if every time step is laid out statically on a storage medium — *if* it
  has consciousness, interrogating it at any point yields a spacetime-like experience like ours. Dynamics are not
  fundamental; logic might be all you need. (The example is conditional — never assert the worm simulation is
  conscious; and in FMT terms a worm may sit at minimal consciousness at most — do not adjudicate.)
- Separate the cases precisely: a live implementation; different execution schedules (faster, slower, paused —
  invariance if all dependencies are preserved); reverse enumeration (reading states in reverse external order
  does not reverse the temporal content inside each state — "I remember A and now see B" keeps its content
  wherever it is read); an actually inverted physical computation (a different operation); a static encoding.
  "Interrogating" needs definition: reading a stored answer, executing a continuation, perturbing an
  implementation are different operations.
- The implementation problem: Putnam (1988) and Searle — under a gerrymandered mapping any physical system
  implements any automaton; Chalmers (1996b, "Does a rock implement every finite-state automaton?") answers with
  counterfactual-supporting causal structure. Egan's *Permutation City* (1994, the dust theory) is the fiction that
  took MG's thesis seriously. Tegmark (2008) again.
- **MG's final position (the climax, state it at full strength):** instantiation is not needed. FMT is a theory
  on our plane of existence, not a fundamental one. The static layout on a disk is not conscious from our point of
  view — it is a sequence of bits. On its own plane, any interaction with another conscious creature in that plane
  ends with both confirming to each other that they are conscious and experience time. Their memories,
  conversations and succession are internally ordered regardless of whether, or in which order, anyone reads the
  disk. Calling it "merely a description" assumes the ontological distinction under dispute. If the relational
  structure suffices, the disk is unnecessary too: it encodes the world rather than bringing its consciousness
  into existence. Consciousness could belong to a structured world intrinsically, with execution one way that
  world appears from another level.
- **The book's resolution of the constitutive limit (Chapter 5):** *description* vs *instance* is itself drawn from a
  side of a generating relation. For an observer to whom the structure is content (us, reading the disk), it is a
  description. For an observer whose frame the structure is (the worm, the creatures), it is the world. FMT's
  "reading the code is not having the experience" (§3.4.5) is true for the reader, and says nothing about the
  creature for which the code is not read but lived. The constitutive limit is real and perspectival: no
  perspective can have another perspective's inside as content.
- **What remains owed — the burden, stated as the open problem of the book:** which structures have an inside.
  The triviality objection: if any structure under some reading has an inside, then any bit string under a
  gerrymandered reading contains every mind. **Answer (S336 hole 2 + D1, mark the positive part as a proposal):**
  readings from outside the universe are not readings — a free mapping is a dictionary that exists nowhere, and
  the outside view draws no distinctions. From a third-person view within the world the question splits.
  (1) Description length is in-world bookkeeping: it locates WHERE a structure resides (the random file's
  dictionary is itself a physical object; the worm is stored in it, badly compressed, not in the noise); kin to
  SB-HC4A §6.3 and Chalmers's counterfactual criterion. The threshold and language constant only shift the
  bookkeeping. (2) Whether what is found has an inside is decided by FMT's architecture (world- and self-model
  closed on each other) in a realized, readable trajectory (D1: rule + initial state = potential only; the
  printed trajectory, even found by chance, has an inner world; no host execution needed).
- **FMT tension, state plainly:** FMT v19 says experience is "constitutively processual — in the doing, not the
  blueprint". On MG's final position, "process" means the internal dependency structure of the world in which the
  doing is done, not execution on a host. That reading is compatible with SB-HC4A §8.4's timeless fixed-point
  block. The phenomenality bridge (closure = phenomenality) is unchanged; what changes is what "running" means.
  Mutual confirmation between creatures does not prove phenomenality — but that is no special objection to their
  situation; it is the other-minds problem every observer already has.

**Chapter 15 — What Travels Between Perspectives** (writer F)
- Collect the limits as one: the generator cannot appear in what it generates (list each instance in a short
  paragraph, not a bullet list).
- What travels: (1) falsity (Chapter 6); (2) relational structure (FMT §3.4.2 analogue — mathematics is the
  shareable relational structure of world-models; its ontology is the untransferable encoding); (3) compressions
  within scope (Chapter 9); (4) the cuts themselves, used knowingly (Chapter 8). What does not travel: truth from no perspective; the inside of another perspective;
  the generator.
- Mathematics and logic, finally placed: they are the best tools embedded observers have for sharing structure
  and detecting contradiction; they cannot certify their own ontological reading, their own completeness, or the
  world's mathematical nature; the unconditional core holds for every perspective, because no perspective is
  outside, and the conditional limits wherever their conditions hold (S336 hole 5).
- End on one concrete sentence, not an aphorism. No "the deepest lesson".

## 4. Corrections ledger — claims the source dialogue got wrong (writers must not reintroduce)

From `claude-code-brief-fmt-physics.md` §"Correction ledger" plus these:
- Complex numbers are consistent; the issue is reification, not inconsistency.
- "Experiment rules out real QM" is too strong (composition-rule dependent).
- J is an algebraic encoding of *i*; Stone's theorem is conditional; neither is a derivation of time.
- Normalization ≠ reversibility. Finite cycles: bijective on the total state only.
- Dependency cone ≠ Lorentz symmetry.
- Bancal et al. constrains a class of finite-speed models only.
- Universality ≠ probability that random data implement anything; countable rules vs uncountable configurations.
- Bell: "everything with a shared deterministic past is statistically correlated" is false; determinism alone
  does not violate measurement independence.
- "A universe needs dynamics" is not an argument against a static structure (SB-HC4A §8.4 already allows a
  timeless block).
- Finite Hilbert dimension does not make many-worlds branches finite without a definition of branching.
- QM is consistent; incompleteness ≠ inconsistency.
- The metric signature predates GR.

## 5. Permitted references (author–year; writers use only these)

Albert, D. Z. (2000). *Time and Chance.* Harvard University Press.
Bancal, J.-D., Pironio, S., Acín, A., Liang, Y.-C., Scarani, V., & Gisin, N. (2012). Quantum non-locality based on finite-speed causal influences leads to superluminal signalling. *Nature Physics* 8, 867–870.
Barbour, J. (1999). *The End of Time.* Oxford University Press.
Bennett, C. H. (1973). Logical reversibility of computation. *IBM Journal of Research and Development* 17, 525–532.
Carroll, S. M. (2017). Why Boltzmann brains are bad. arXiv:1702.00850.
Chaitin, G. J. (1966). On the length of programs for computing finite binary sequences. *Journal of the ACM* 13, 547–569.
Chalmers, D. J. (1996). Does a rock implement every finite-state automaton? *Synthese* 108, 309–333.
Cook, M. (2004). Universality in elementary cellular automata. *Complex Systems* 15, 1–40.
Culik, K., & Yu, S. (1988). Undecidability of CA classification schemes. *Complex Systems* 2, 177–190.
D'Ariano, G. M., & Perinotti, P. (2014). Derivation of the Dirac equation from principles of information processing. *Physical Review A* 90, 062106.
Dennett, D. C., & Kinsbourne, M. (1992). Time and the observer. *Behavioral and Brain Sciences* 15, 183–247.
Eagleman, D. M., & Sejnowski, T. J. (2000). Motion integration and postdiction in visual awareness. *Science* 287, 2036–2038.
Egan, G. (1994). *Permutation City.* Millennium.
Elga, A. (2025). Boltzmann brains and cognitive instability. *Philosophy and Phenomenological Research* 111, 127–136.
Feynman, R. P. (1965). The development of the space-time view of quantum electrodynamics. Nobel Lecture.
Geldard, F. A., & Sherrick, C. E. (1972). The cutaneous "rabbit": a perceptual illusion. *Science* 178, 178–179.
Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik* 38, 173–198.
Gruber, M. (2015). *Die Emergenz des Bewusstseins.*
Gruber, M. (2026a). The Four-Model Theory of Consciousness, v19. Zenodo. https://doi.org/10.5281/zenodo.23427746
Gruber, M. (2026b). Emergent spacetime from self-referential computation: a hierarchical cellular automaton framework (SB-HC4A), v8. Zenodo. https://doi.org/10.5281/zenodo.23242055
Hardy, L. (2001). Quantum theory from five reasonable axioms. arXiv:quant-ph/0101012.
Hoffreumon, T., & Woods, M. P. (2025). Quantum theory does not need complex numbers. arXiv:2504.02808.
Hossenfelder, S., & Palmer, T. (2020). Rethinking superdeterminism. *Frontiers in Physics* 8, 139.
Kolers, P. A., & von Grünau, M. (1976). Shape and color in apparent motion. *Vision Research* 16, 329–335.
Kolmogorov, A. N. (1965). Three approaches to the quantitative definition of information. *Problems of Information Transmission* 1, 1–7.
Lakatos, I. (1976). *Proofs and Refutations.* Cambridge University Press.
Minkowski, H. (1908/1909). Raum und Zeit. *Physikalische Zeitschrift* 10, 104–111.
Montgomery, H. L. (1973). The pair correlation of zeros of the zeta function. *Proceedings of Symposia in Pure Mathematics* 24, 181–193.
Odlyzko, A. M. (1987). On the distribution of spacings between zeros of the zeta function. *Mathematics of Computation* 48, 273–308.
Popper, K. R. (1959). *The Logic of Scientific Discovery.* Hutchinson.
Putnam, H. (1988). *Representation and Reality.* MIT Press.
Rauch, D., et al. (2018). Cosmic Bell test using random measurement settings from high-redshift quasars. *Physical Review Letters* 121, 080403.
Redhead, M. (1975). Symmetry in intertheory relations. *Synthese* 32, 77–112.
Renou, M.-O., et al. (2021). Quantum theory based on real numbers can be experimentally falsified. *Nature* 600, 625–629.
Stone, M. H. (1932). On one-parameter unitary groups in Hilbert space. *Annals of Mathematics* 33, 643–648.
Tegmark, M. (1997). On the dimensionality of spacetime. *Classical and Quantum Gravity* 14, L69–L75.
Tegmark, M. (2008). The mathematical universe. *Foundations of Physics* 38, 101–150.
't Hooft, G. (2016). *The Cellular Automaton Interpretation of Quantum Mechanics.* Springer.
Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society* s2-42, 230–265.
Wigner, E. P. (1960). The unreasonable effectiveness of mathematics in the natural sciences. *Communications on Pure and Applied Mathematics* 13, 1–14.
Wolfram, S. (2002). *A New Kind of Science.* Wolfram Media.

All entries are unverified until the citation pass runs.

## 6. Writer assignment

| Writer | Files | Chapters |
|---|---|---|
| A | `01-front-ch01-03.md` | Front matter, Preface, Ch 1–3 (Part I) |
| B | `02-ch04-05.md` | Ch 4–5 |
| C | `03-ch06-07.md` | Ch 6–7 |
| G | `03b-ch08.md` | Ch 8 |
| D | `04-ch09-11.md` | Ch 9–11 (Part III) |
| E | `05-ch12-13.md` | Ch 12–13 |
| F | `06-ch14-15.md` | Ch 14–15 |

Part headings (`# Part I — …`) are written by the writer whose file opens the part (A: Part I; B: Part II;
D: Part III; E: Part IV).
