<!--
DRAFT — AIW-105. Initial draft for MG review and rework. NOT submission-final.
Standalone paper spun out of FMT §3.4.2, §3.4.5, §8.6 (Prediction 5).
"VERIFY:" tags mark citations whose specifics (year/venue/exact claim) the author
should confirm before circulating. See end-of-file reference notes.
Word count target: 2500-4000 (first-draft prose, some author-notes left inline in [[ ]]).
-->

# The Privacy of Qualia as a Decompilation Problem: A Four-Model-Theory Account of Why Absolute Feel Does Not Transfer While Its Structure Does

**Working title alternatives (author pick):** "No Shared Source Code: Qualia Ineffability as Decompilation Difficulty" · "Refractory Encodings, Shareable Structure: An FMT Reframing of Qualia Privacy"

*Matthias Gruber* · ORCID 0009-0005-9697-1665 · [affiliation line TBD]

---

## Abstract

Why can I not convey to you what my red is *like*, even when we agree on every relational fact about colour? The standard framings of qualia privacy and ineffability treat this as a flat mystery — a brute wall between minds — or dissolve it entirely by denying that there is anything determinate to convey. Neither framing predicts anything. This paper develops a third option from the Four-Model Theory of consciousness (FMT). On FMT, phenomenal states are level-constitutive properties of a running self-simulation; the specific state that realises a given quality is encoded *sub-symbolically and idiosyncratically*, shaped by an individual's sensory history and connectome. Cross-subject read-out of the *absolute* encoding would require reverse-inventing a per-brain interpretive language — there is no shared source code to consult — so absolute feel is refractory to transfer. Its *relational structure*, by contrast, is a substrate-independent invariant and is progressively recoverable. The account therefore predicts a **graded, directional asymmetry**, not a uniform blackout: quality-space *structure* is recoverable across subjects (via similarity judgments, representational similarity analysis, functional hyperalignment, and unsupervised Gromov–Wasserstein alignment), individual quality-space *geometry* tracks the individual's connectome and sensory history, yet *absolute per-brain read-out* stays refractory even where structure aligns cleanly. That paired pattern is falsifiable and distinguishes the account from pure pessimism about qualia — pessimism the very alignment results already refute. The proposal is offered as a **complement** to structuralist theories of quality-space, not a rival. Its scope is stated plainly and up front: it explains the ineffability *of report*, not the existence *of feeling*, and does not alter FMT's partial (◐) standing on the Hard Problem.

**Keywords:** qualia, privacy, ineffability, quality-space, representational similarity analysis, hyperalignment, Gromov–Wasserstein alignment, phenomenal concepts, Four-Model Theory

---

## 1. The Puzzle: Privacy and Ineffability, and Why the Standard Framings Stall

Two features of conscious experience have resisted assimilation into the physical story of the brain. **Privacy**: my experiences are, in some strong sense, accessible only to me; you can observe my brain in unlimited detail and still not thereby *have* my experience. **Ineffability**: even I cannot say what my experience is *like* in a way that would let someone who has never had it know. The two are related but not identical. Privacy is about *access* — who can occupy the state. Ineffability is about *transfer* — what can be conveyed in a shared vocabulary. This paper is about the second, and about a specific, gradable version of it.

The canonical dramatisation is Jackson's Mary (Jackson, 1982): a scientist who knows every physical fact about colour vision but has lived in monochrome. On release she sees red, and — the intuition goes — learns something. Whatever she gains, she could not have been *told*; no addition to her physical knowledge would have supplied it in advance. The knowledge argument is usually deployed against physicalism, but strip away that agenda and a smaller, more robust datum remains: there is a stable, cross-culturally recognisable *sense* in which the absolute feel of a first red cannot be handed over in propositions. That datum is what a theory of ineffability owes an account of.

The existing framings stall in opposite directions.

**Brute-privacy / pessimism.** One family treats ineffability as a primitive wall: qualia are intrinsically private, incomparable across subjects, perhaps not even well-defined outside a single mind. This has the virtue of respecting the phenomenology and the vice of predicting nothing. If nothing about my experience can cross to you, then the growing body of results showing that quality-*spaces* align across people should be impossible — and it is not. Colour-similarity structure recovers between pooled groups of observers without shared labels (Kawakita et al., 2025; Watanabe et al., 2026; see §3), though the individual-level structural arm is untested; representational geometry generalises across brains under hyperalignment. Pure pessimism is not merely unmotivated; it is *refuted* by the data the field already has.

**Deflation / illusionism.** The opposite family denies that there is a determinate absolute feel to convey in the first place: the sense that something ineffable is being withheld is itself a misrepresentation (Frankish, 2016). This dissolves the puzzle by dissolving its subject matter. But it pays a price the phenomenology keeps charging back: it must treat the near-universal, stable report of an untransferable *this-ness* as systematic error rather than as a signal about how experience is built. And it, too, makes no positive prediction about *which* aspects of experience should transfer and which should not — it predicts, if anything, that the whole distinction is confused.

Between "nothing transfers" and "there is nothing to transfer" lies the territory the actual data occupy: *some* things transfer — a great deal of relational structure — and *something* stubbornly does not. A satisfying theory of qualia privacy should predict *that* shape: what is shareable, what is refractory, and in which direction the asymmetry runs. The remainder of this paper argues that FMT does exactly this, and that the mechanism is best understood on the model of **decompilation difficulty**.

---

## 2. The FMT Decompilation-Difficulty Account

### 2.1 The relevant FMT commitments, briefly

The Four-Model Theory holds that consciousness is an ongoing self-simulation structured along two dimensions — **scope** (world vs. self) and **mode** (implicit vs. explicit) — yielding **two model classes** (implicit and explicit) each turned on the world and on the self. The implicit model kinds are substrate-level, learned, non-conscious knowledge bases; the explicit model kinds are the transient, virtual simulation those substrates generate and sustain, phenomenal where its content enters the self-model's closed loop. Qualia, on this view, are *level-constitutive* properties of the running explicit simulation — real at the computational level, incoherent at the substrate level, in the way "the value in cell A1" is real for a spreadsheet and incoherent as a claim about transistors. Phenomenal quality is the simulation's own mode of registering its contents — a virtual "sixth sense" internal to the simulation rather than a property of the neurons that run it. (These commitments are argued in the parent FMT paper; this paper takes them as given and asks what follows for *privacy*.)

Two further FMT points do the load-bearing work here.

First, **where qualitative character comes from.** The distinct feel of vision versus hearing, of pain versus warmth, is inherited from the distinct architecture of the implicit model kinds that generate each stream. Each sensory system evolved to transduce a different physical channel and therefore has different connectivity, timescales, and internal structure; the explicit simulation running on top of them inherits those distinctions as qualitative differences. The feel of a quality is, in effect, the *signature of which implicit pathway generated that fragment of the simulation*, as reverberated through the self-referential loop.

Second, **the decompiler thought-experiment.** FMT maintains full supervenience: a complete substrate description entails every phenomenal fact, with no dualism and no strong emergence. So *in principle* a "decompiler" with access to every synaptic weight, connection, and live firing pattern could extract a formal description of the running self-simulation. The parent theory uses this to separate two limits — a *constitutive* one (a description is not an instance; reading the code is not undergoing the experience) and a *practical* one (the extraction is intractable and, crucially, *illegible*). This paper takes up the second limit and shows it is not a footnote but the mechanism of privacy.

### 2.2 Sub-symbolic, idiosyncratic encoding: no shared source code

Here is the core move. In an authored software system, a decompiler is tractable because there was a *source language* — a shared, human-designed abstraction layer — and decompilation is the recovery of that abstraction from a lower-level image. Variable names may be gone, but the type system, the calling conventions, the standard library, the very notion of a "function," are shared priors that make the lifted code legible. Reverse engineering trades on a **common source vocabulary** even when the source itself is lost.

A brain has no such layer. The mapping from substrate state to phenomenal content is not an authored abstraction; it is a **sub-symbolic, self-organised encoding** laid down by one individual's developmental trajectory, sensory history, and connectome. There is no type system, no shared calling convention, no standard library of qualia — the "source" was never written in a common language because it was never *written* at all; it was *grown*. Two brains realising "red" do not run two copies of the same program with different data. They run two different self-organised dynamical systems whose only guarantee of correspondence is the correspondence of the *world they both model* and the *bodies they both regulate*.

Consequently, to read your absolute encoding of red off your substrate, I would have to **reverse-invent a per-brain interpretive language** — reconstruct, from your weights alone, the idiosyncratic mapping your development happened to fix. This is not decompilation against a known source; it is decipherment of a script with a vocabulary of one, whose only Rosetta stone is the shared external world. That is why the *absolute* encoding is refractory to transfer: not because it is metaphysically sealed, but because there is no shared code to compile *to*, and the per-brain code must be re-derived from scratch for every subject and, plausibly, re-derived again as that subject's brain changes.

### 2.3 Absolute vs. relational: why one half is shareable

The refractoriness attaches specifically to the *absolute* encoding — "which of my states is *my* red." It does **not** attach to the *relational structure* — the pattern of similarities and differences among a subject's experiences. Relational structure is, by construction, the kind of thing that survives re-encoding: it is a **substrate-independent invariant**. If red is more like orange than like blue for me, and the same for you, that ordinal fact holds regardless of which absolute states each of us uses to realise the three colours. A relation is recoverable by any procedure that preserves relations, even with no access to, and no agreement about, the absolute terms.

So FMT partitions the phenomenon cleanly:

- **Relational structure** = the organisation of the explicit simulation — *shareable*, because it is an invariant, and recoverable by relation-preserving methods.
- **Absolute encoding** = the specific per-brain substrate realisation of each term — *refractory*, because it is a self-organised code with no shared source, transferable (as FMT argues elsewhere) only by *instantiation*, never by description.

This is the phenomenal-concept strategy (Loar, 1997; Papineau, 2002) given an architectural mechanism. Shareable structure and untransferable encoding are one physical state under two modes of constitution: the relational reading (transfers) and the indexical/realising reading (does not). An explanatory gap appears — the two readings are conceptually isolated — without a metaphysical one. And it reframes Mary precisely: what Mary could have been *told* in advance is the entire relational geometry of colour space (its dimensionality, its neighbourhood relations, its opponent structure); what she could not have been told, and gains only by instantiation, is an *absolute* term of that geometry realised in *her* substrate. Mary's residual is the untransferable half, exactly as the account predicts.

The pay-off is that "ineffability" stops being a wall and becomes a **gradient with a direction**. Which brings us to the empirical content.

---

## 3. The Testable Premise and Concrete Predictions

The reason this deserves a standalone treatment rather than a remark is that the decompilation account makes a *graded, directional* prediction — not a flat mystery. Three claims, each falsifiable, jointly constitute the premise. Where they have already been partly borne out I say so; the novel, still-open content is the *conjunction*, and especially the *paired failure* in Prediction 5c. Predictions 5a and 5c restate the two arms of the parent paper's Prediction 5 (§8.6); Prediction 5b is new here.

### Prediction 5a — Quality-space *structure* is recoverable across subjects

**Claim.** Within a fixed modality, the relational structure of one subject's quality-space aligns with another's *without shared labels*. Similarity judgments yield representational dissimilarity matrices amenable to representational similarity analysis (RSA; Kriegeskorte, Mur, & Bandettini, 2008); functional hyperalignment maps one subject's representational geometry onto another's (VERIFY: Haxby et al., 2011, "A common, high-dimensional model of the representational space in human ventral temporal cortex," *Neuron* — confirm year/venue and that it is the canonical hyperalignment paper); and unsupervised **Gromov–Wasserstein optimal transport** recovers above-chance correspondence between pooled groups of observers over dissimilarity matrices with no shared labels at all (Kawakita et al., 2025; extended to toddlers by Watanabe et al., 2026). The individual-level structural arm is untested.

**Status.** *Partly demonstrated.* Label-free alignment of colour-similarity structure between pooled groups of observers has been reported (Kawakita et al., 2025; Watanabe et al., 2026); the individual-level structural arm is untested; RSA and hyperalignment are established methods with a substantial track record. FMT does not claim these as its own results — it claims they are *what the account predicts*, and it is on the right side of them where pure pessimism is not.

**What would refute it.** If label-free structural alignment within a modality fails to exceed chance across individuals — i.e., if quality-space geometry turns out *not* to be a shareable invariant after all — the shareable-structure half of the account is wrong.

### Prediction 5b — Individual quality-space *geometry* tracks the individual's connectome and sensory history

**Claim.** Because the encoding is grown, not authored, systematic *individual* differences in quality-space geometry should be lawfully related to systematic individual differences in the substrate and in sensory history. Concretely: (a) atypical sensory history predicts atypical geometry in the expected direction — e.g., anomalous trichromats and dichromats should show measurably contracted or reorganised colour-space geometry relative to typical trichromats (VERIFY: cite the psychophysics on colour-space geometry in anomalous trichromacy); congenitally absent or degraded input should reshape the corresponding sub-space; (b) within neurotypical subjects, residual individual differences in quality-space geometry should co-vary with individual differences in the relevant connectivity/representational fingerprint, above chance.

**Status.** *Open, partially anchored.* The direction is consistent with known effects of receptor complement and deprivation on discrimination structure; the *specific* prediction — that fine-grained individual geometry tracks a connectomic/representational fingerprint — is, as far as I know, untested at the resolution FMT needs, and is a clean target.

**What would refute it.** If individual quality-space geometry is *uncorrelated* with individual sensory history and substrate variation — if the geometry floats free of the body that grew it — then the "grown, idiosyncratic encoding" mechanism is wrong, and the account loses its explanation of *why* absolute encodings differ.

### Prediction 5c — Absolute per-brain read-out stays refractory *even where structure aligns*

**Claim (the committed dissociation).** On the *same* data for which unsupervised structural alignment succeeds, a decoder trained to read one brain's *absolute* realising state ("their red," as a substrate state) will fail to generalise to another brain — and this failure will persist *after* the two subjects' quality-spaces have been structurally aligned. Structure travels; the absolute term does not travel with it. The claim is explicitly the *pairing*: alignment succeeds **and** absolute cross-subject decoding fails, on the same modality, same subjects, same session.

**Status.** *Novel and open.* This is the load-bearing, still-untested prediction — the reason the account is not merely a redescription of existing alignment results. Existing work establishes the structural arm at the group level (Prediction 5a); the paired failure of absolute cross-subject read-out is what the decompilation account uniquely stakes.

**What would refute it.** If a cross-subject decoder recovers another brain's absolute realising state *as well as, or better than,* unsupervised structural alignment recovers the geometry, the asymmetry is wrong and the account fails at its core: there would, after all, be a shared enough source to compile absolute feel across brains. [[Author note: operationalising "absolute realising state" without smuggling in relational information is the hard methodological knot — the decoder must be denied the very similarity structure Prediction 5a exploits. Needs a careful design section; flagging for the methods pass.]]

### The shape of the prediction, stated once

Putting the three together: **structure is recoverable, geometry is lawful, absolute read-out is refractory** — a graded asymmetry with a direction (relational → shareable; absolute → sealed), each arm independently falsifiable. That is a positive empirical commitment. Brute pessimism predicts arm 1 fails; deflationism predicts the arm-1/arm-3 distinction is confused; standard functionalism (on which the encoding is exhausted by its functional/relational role) predicts arm 3 fails — that absolute read-out should travel *with* the structure. Only a level-constitutive, grown-encoding account predicts all three as stated: 1 and 2 succeed, 3 refractory.

---

## 4. Relation to Structuralist Theories of Quality-Space: Complement, Not Rival

The claim that the *shareable* part of experience is its relational structure places this account squarely alongside **structuralist theories of quality-space**, and it is important to be explicit that FMT here is offered as a **complement** to that programme rather than a competitor.

Structuralism about qualities — the tradition running through quality-space and state-space treatments of sensory quality (VERIFY: Austen Clark, *A Theory of Sentience*, 2000, for the quality-space framework; VERIFY: Paul Churchland's state-space/"chimerical colours" treatment of colour as position in a neural activation space; VERIFY: Rosenthal's quality-space theory) — holds that the individuating facts about a quality are exhausted by its position in a space of similarity and difference relations. More recent work pushes this into an explicitly relational, even category-theoretic, register (VERIFY: Tsuchiya and colleagues on qualia structure / the structuralist approach to consciousness; confirm the specific papers) and into the higher-order and quality-space-realist neighbourhood (VERIFY: Lau & Michel — confirm which joint or individual works are meant; Michel has quality-space-adjacent work, Lau has higher-order theory).

FMT's contribution to that programme is not to dispute it but to **explain its success and mark its limit** in one architecture:

1. **Why structuralism works.** If quality-space structure is a substrate-independent *invariant* of the explicit simulation, then structuralist methods *should* recover it across subjects, and unsupervised alignment *should* be possible with no shared labels. FMT supplies the mechanistic reason the structural programme keeps succeeding: relational organisation is exactly the part of a grown encoding that survives re-encoding.

2. **Why structuralism does not exhaust the phenomenon.** The absolute realising term — the indexical "*this* one, in *my* substrate" — is precisely what structure leaves undetermined, and (on FMT) it is refractory to transfer for a principled architectural reason (§2.2), not merely absent from the structuralist's bookkeeping. FMT thus predicts a residue that a pure structuralism should expect to keep encountering and being unable to close: the residue is not a failure of the structuralist method but a real, and locatable, feature of how experience is built.

The relationship, then, is division of labour: structuralism owns the shareable half and characterises it well; the decompilation account explains *why* that half is shareable, *why* the other half is not, and *where the seam runs*. Neither is complete without the other, and the account should be read as reinforcing — not undermining — the structuralist result that so much of quality-space *does* transfer. (This is also why the account cannot be a form of pessimism: it *leans on* the very RSA/alignment results a pessimist must deny.)

---

## 5. Honest Limits

This section is deliberately blunt, because the account is easy to over-sell and the over-sell would be false.

**It explains ineffability-of-report, not existence-of-feeling.** Everything above concerns *why phenomenal encodings do not transfer* — why the absolute term of one subject's quality-space cannot be conveyed to another in a shared vocabulary. It says nothing about *why there is something it is like at all*. The decompilation story presupposes that there is a running simulation with an inside; it explains the transfer-resistance of that inside's absolute encodings. It does not explain, and must not be read as explaining, the existence of the inside. A reader who wants to know why closure yields experience rather than mere data will not find the answer here; that question is argued (partially, and by inference to the best explanation) in the parent theory and is untouched by anything in this paper.

**It does not move FMT's Hard-Problem status.** FMT marks its treatment of the Hard Problem as *partial* (◐): the reframing relocates the problem as a category error about levels and narrows it with a mechanism, but it carries a residual bridging commitment it argues for rather than derives. Nothing in the decompilation account changes that mark. Confirming all three predictions of §3 would corroborate the ◐ — it would explain why *report* of absolute feel is refractory — but it would not upgrade the mark to ● (fully addressed). The privacy result is downstream of the two-level ontology, not independent support for it: if the ontology is wrong, the decompilation story loses its footing; if the ontology is right, the decompilation story explains a specific consequence and no more.

**It is a claim about transfer, not about metaphysical sealing.** The refractoriness is *practical-plus-architectural* (no shared source; per-brain code must be re-derived), layered on top of the *constitutive* point that a description is not an instance. It is emphatically **not** the claim that absolute feel is metaphysically private in a way that would resist even instantiation. FMT's own commitment is the opposite: the encoding *can* be transferred — by instantiating the same computation on another substrate — just not *conveyed by description*. The paper explains the failure of the *report* channel, not an in-principle sealing of the state.

**Methodological honesty on Prediction 5c.** The committed dissociation stands or falls on operationalising "absolute realising state" in a way that genuinely excludes the relational information Prediction 5a exploits. If that separation cannot be made clean, the paired prediction is not yet a test but a promissory note. [[Author: this is the single most important thing to get right in a full methods section, and the most likely reviewer target.]]

---

## 6. Conclusion

Qualia privacy has been framed either as a brute wall or as a confusion to be dissolved. Both framings are empirically idle, and the brute-wall framing is worse than idle — it is refuted by the growing evidence that quality-space structure aligns across minds. The Four-Model Theory offers a third framing with empirical teeth. Because phenomenal states are level-constitutive properties of a self-organised, sub-symbolically encoded self-simulation, there is **no shared source code** from which one brain's *absolute* encoding of a quality could be lifted into another; reading it out would require reverse-inventing a per-brain interpretive language. That is why absolute feel is refractory to transfer. But the *relational structure* of quality-space is a substrate-independent invariant, and it is progressively shareable — which is why structuralist methods, from RSA to unsupervised Gromov–Wasserstein alignment, keep succeeding.

The result is a **graded, directional asymmetry** rather than a flat mystery: structure recoverable, geometry lawful, absolute read-out refractory — three arms, each falsifiable, and a committed dissociation (Prediction 5c) that no rival framing predicts. The account is a **complement** to structuralism, explaining both why the shareable half is shareable and why the refractory half is refractory, and locating the seam between them. And its scope is honest: it explains the ineffability *of report*, not the existence *of feeling*, and leaves FMT's Hard-Problem mark exactly where it was — ◐, partially addressed, and no further.

If the field can build the paired test — structural alignment that succeeds alongside absolute cross-subject decoding that fails, on the same modality and subjects — then the oldest intuition about qualia privacy would be recast as a measurable, mechanistic fact about how brains grow their codes, rather than a wall at the edge of the sayable.

---

## Reference notes for the author (not the reference list)

Confident, already in the parent FMT paper:
- **Jackson, F. (1982).** "Epiphenomenal Qualia," *Philosophical Quarterly* 32, 127–136. (Mary / knowledge argument.)
- **Loar, B. (1997).** "Phenomenal States," in Block, Flanagan, & Güzeldere (eds.), *The Nature of Consciousness*. (Phenomenal-concept strategy.)
- **Papineau, D. (2002).** *Thinking About Consciousness*, OUP. (Phenomenal-concepts / type-B physicalism.)
- **Kriegeskorte, N., Mur, M., & Bandettini, P. (2008).** "Representational similarity analysis," *Frontiers in Systems Neuroscience* 2:4. (RSA.)
- **Frankish, K. (2016).** "Illusionism as a theory of consciousness," *JCS*. (Deflation/illusionism.)
- **Kawakita, G., Zeleznikow-Johnston, A., Takeda, K., Tsuchiya, N., & Oizumi, M. (2025).** "Is my "red" your "red"?: Evaluating structural correspondences between color similarity judgments using unsupervised alignment," *iScience* 28(3), 112029. (Group-level, label-free alignment; as cited in the parent FMT paper.)
- **Watanabe, R., Wang, J., Oizumi, M., Saji, N., & Moriguchi, Y. (2026).** "Unsupervised alignment reveals shared but locally refined colour qualia structure from toddlerhood to adulthood," *bioRxiv*. https://doi.org/10.64898/2026.09.14.751604 (as cited in the parent FMT paper.)

**VERIFY: (confirm author list / title / year / venue / exact claim before circulating):**
- **Haxby et al. (2011?)** — canonical hyperalignment paper ("A common, high-dimensional model of the representational space in human ventral temporal cortex," *Neuron*). Confirm year and that this is the right primary cite (vs. Guntupalli et al. 2016 for the searchlight/whole-cortex extension).
- **Austen Clark (2000?)** — *A Theory of Sentience*, OUP. (Quality-space structuralism.) Confirm; distinguish from Andy Clark.
- **Churchland, P. M.** — state-space/activation-vector treatment of colour; "Chimerical Colors" (2005?, *Philosophical Psychology*) and *A Neurocomputational Perspective* (1989). Confirm which to cite for quality-space structuralism.
- **Rosenthal, D. (2010?)** — "How to think about mental qualities," quality-space theory. Confirm as a structuralist anchor if used.
- **Tsuchiya, N., and colleagues** — qualia structure / structuralist (possibly category-theoretic) approach to consciousness (Tsuchiya, Taguchi, Saigo, 2016?; Tsuchiya & Saigo). Confirm the specific paper(s).
- **Lau & Michel** — confirm the intended reference (higher-order / quality-space realism). Hakwan Lau (higher-order theory) and Matthias Michel (quality-space-adjacent work) — decide whether a joint work or two separate cites is meant.
- **Anomalous-trichromacy colour-space geometry (Prediction 5b)** — find and cite the psychophysics showing contracted/reorganised colour-space in anomalous trichromats/dichromats.
- **Gruber (parent FMT paper)** — self-cite for §3.4.2, §3.4.5 (decompiler), §8.6 (Prediction 5), and the ◐ Hard-Problem rating.
