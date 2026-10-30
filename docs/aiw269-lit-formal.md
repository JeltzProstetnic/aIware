<!-- AIW-269 half (b), formalization slice, S323 2026-09-28 subagent. arXiv API 406; math.DS/cs.IT keyword-only. -->
# AIW-269 literature sweep: formal/mathematical slice (fmt-formalization v4)

Window: first published 2026-08-26 to 2026-09-28. Swept on 2026-09-28.
Sources: arXiv monthly listings for nlin.CG, nlin.AO, nlin.CD, cs.FL and q-bio.NC (Aug + Sep 2026, keyword-filtered), arXiv advanced search with a submitted-date filter (about 30 queries), OpenAlex with a `from_publication_date` filter (12 queries), and the Zenodo API.
Verification: I checked every item's title, authors and first-submission date against its arXiv abstract page, OpenAlex record or Zenodo record. Items first submitted before 2026-08-26 were dropped. One was: Kutrib et al., *Inductive Inference of Cellular Automata*, 2608.24240, submitted 25 Aug.
Tooling caveat: the arXiv export API returned HTTP 406 and search/OpenAlex/Zenodo rate-limited (429) intermittently, so coverage of math.DS and cs.IT (too large to list in full) rests on keyword search only.

**Bottom line: nothing in the window settles, contradicts or pre-empts L1 (closure ⇒ universality), L2 (universality ⇒ criticality), the Zenil (2010) conjecture cited in L2(v), or the E⊥K orthogonality conjecture. No MUST-ANSWER items.** Three items are MUST-CITE, all touching §4.2/§4.4/§4.7, the criticality-operationalization sections.

---

## MUST-CITE

**1. Du, Y., Liardi, A., Rajpal, H., & Jensen, H. J. (2026). Fisher Information Metric as a model-free measure of proximity to criticality in neural systems.** arXiv:2609.07624, submitted 7 Sep 2026.
The paper shows that the Fisher information of a control parameter tracks proximity to criticality across branching, spiking and whole-brain models. The FIM of the *observed branching ratio* peaks where activity growth and decay balance, and the peak's width and height give continuous, model-free readouts without estimating critical exponents.
Bears on §4.2, "Three Candidate Criticality Measures" (σ, λ_max, α, line 263ff), and on the §4.7 local indicator `c_i = 1 if σ_i ∈ [σ_low, σ_high]…` (line ~337). The paper gives a principled, continuous replacement for the hard σ-window threshold, and an information-geometric one, which also fits §2.5. It is a candidate fourth measure, or a way to set σ_low/σ_high.

**2. Carcamo, D. P., & Lynn, C. W. (2026). Emergence of criticality in models of real neurons.** arXiv:2609.09438, submitted 8 Sep 2026.
The authors prove and illustrate that, as N grows, parameters *inferred* from data concentrate near critical points without any fine-tuning. The reason is that small parameter regions near criticality map onto large regions of statistics space. Across mouse recordings, Curie–Weiss fits all collapse onto a **first-order** transition.
Bears on §2.6 "Cautions on Model-Space Estimation", §4.3 "Disambiguating Criticality Types" and §4.4 (line 297). This is a warning the roadmap should state: model-based inferences of "near-critical" are partly an artefact of the inverse problem. That matters for the regional c_i estimation in §4.7 if any σ_i/α_i is obtained by fitting a model rather than counting avalanches directly. The first-order finding also bears on the roadmap's implicit assumption of a continuous transition.

**3. Vock, S., & Meisel, C. (2026). Adaptive self-organized criticality in deep neural networks.** arXiv:2608.28431, submitted 28 Aug 2026.
A purely local homeostatic rule, using only postsynaptic activity, drives deep networks from sub- or supercritical initial conditions to a common critical state, defined by conserved propagation and a vanishing finite-time Lyapunov exponent. Combined with gradient training it counteracts the drift toward supercriticality, and it exposes a competition between dynamical regulation and task optimization.
Bears on §4.4 ("Criticality: A Conjectured, Not Derived, Prerequisite") and Phase 4, "Computational Validation" (line 557). It is a constructive mechanism for an artificial substrate to sit at λ_max ≈ 0, and it is direct evidence that criticality and task performance can trade off. That is consistent with the roadmap's refusal to derive criticality from computational capacity (L2(iv)).

---

## NICE-TO-HAVE

**4. Gupta, C. (2026). Collision-based logic in Lenia and its composition boundary.** arXiv:2609.01348, submitted 1 Sep 2026.
The paper builds an INHIBIT gate from Orbium-glider collisions in fixed-rule Lenia and composes two gates into a correct AND-NOT chain. It explicitly leaves routing or restoring a deflected signal undemonstrated, so universality for continuous CA stays open.
Bears on L2(ii), line 307: *"Universality has been proven only for specific rules (Rule 110, Conway's Life)"*. It could be added as a fresh example that universality in continuous CA is still unestablished despite lifelike Class-4-looking behaviour.

**5. Mayeux, A. (2026). Existence of an infinite family of substrates satisfying all the postulates of integrated information theory, exclusion included, with arbitrarily large integrated information.** Zenodo preprint, doi:10.5281/zenodo.22704537, 2026-09-11. Companion: *A Machine-Checked Formalization of Integrated Information Theory in Lean4*, doi:10.5281/zenodo.22983658, 2026-09-26.
The author proves in Lean 4, against a formalization of IIT 4.0, that a ring of binary XOR units (each XORs itself and its two clockwise neighbours, i.e. a linear/additive CA) is a complex in every state, with Φ growing as 2^(quadratic in n).
Bears on §4.7's C_N/Φ paragraph, where the roadmap already cites Aaronson (2014). This is a machine-checked version of Aaronson's expander objection. It also fits the roadmap's K-vs-Φ distinction: an additive, non-Class-4 CA maximizes Φ, whereas FMT's K is conditioned on criticality. The work is unrefereed and single-author, so cite at most as supporting the Aaronson point.

**6. Stewart, A. (2026). The Internal Contradictions in Integrated Information Theory 4.0.** Zenodo preprint, doi:10.5281/zenodo.22926330, 2026-09-23.
It argues that IIT 4.0's six postulates are jointly unsatisfiable, with exclusion self-contradictory and integration conflicting with composition, and it argues entirely in IIT's own vocabulary.
Relevant only to how the roadmap frames IIT as a rival (§4.7, Albantakis et al. ref). Its claim sits in tension with #5's Lean result, which shows that a system *satisfying* all postulates exists. Neither is refereed, so it is not recommended for citation.

**7. Gómez Calderón, A. M. (2026). Where Do Qualia Enter the Model? A Coq-Verified Analysis of the Non-Derivability of Phenomenology from Functional Structure.** Figshare, doi:10.6084/m9.figshare.33351339.v1, 2026-08-27.
Coq countermodels show that self-modeling, self-reference, reportability and similar properties do not by themselves *entail* phenomenal predicates: two functionally identical models can carry incompatible phenomenal assignments.
Bears on §6.4, "The phenomenal properties exist at m\*". This is a foreseeable referee objection to the fixed-point section. FMT states an identity thesis (Ψ(m\*) = m\* *is* the phenomenal level), not a derivation inside an uninterpreted logic, so the result does not touch the roadmap as written. It may be worth one sentence saying so. Unrefereed.

**8. Qiao, Y., Yu, L., Qiu, R., & Gao, X.-S. (2026). On the Turing Completeness of Transformers and Agents.** arXiv:2609.20335, submitted 17 Sep 2026.
The paper proves that a fixed finite-precision transformer cannot memorize some Turing machines on unbounded inputs, and that a randomly trained infinite-precision one is almost surely not Turing complete. An agent with decision, execution and memory modules is Turing complete.
Bears on L1, line 305, *"deeper recursive self-modeling requires more computational resource… not… universal resource"*, and on §6.5. It is a clean formal example that universality hinges on an external recurrent memory loop rather than on depth.

**9. Wang, W., & Reid, F. (2026). Looped Transformers under the Jacobian Lens: Does the Global Workspace Survive Recurrence?** arXiv:2609.01924, submitted 1 Sep 2026.
Empirically, a workspace-like band forms in both looped and depth-recurrent transformers, but recurrence changes how it is accessed: some architectures rebuild it every loop, others carry it across all recurrences within a sliding window.
Recurrent-vs-feedforward equivalence: relevant to §6.3 (recursive representation). It is empirical rather than a formal equivalence result.

**10. Balduzzi, D. (2026). Gradland: On Phenomenal Experience, Differentiated Across Many Dimensions.** arXiv:2609.09306, submitted 8 Sep 2026.
The paper hypothesizes that Jacobian structure (effective rank, and "cohesion" via Kirchhoff complexity) characterizes phenomenal structure in idealized neural networks, and it reproduces duration, vividness and texture claims.
Bears on §2.5 (bundle geometry) and §4.7 K as a rival differentiation measure. It is by the co-author of the IIT-2008 information-geometric work, so it is worth knowing for positioning.

**11. Dehghani, N. (2026). "More Is Different" in Neural Circuits: Algebraic Emergence of Effective Theories in Canonical Recurrent Motifs.** arXiv:2608.30231, submitted 31 Aug 2026.
A Krohn–Rhodes / transition-monoid analysis shows that composing aperiodic WTA and divisive-normalization updates creates genuinely composite group components (reversible cycles) absent from every generator.
Bears on §7, the category-theoretic architecture: preservation under composition in §7.2, and §7.4. It is a rigorous algebraic example of structure that exists only in the composite.

**12. Riedel, J., Barnes, C. P., & Zaikin, A. A. (2026). Nonlinear regime transitions enable reservoir computation in activator–inhibitor cellular automata.** bioRxiv, doi:10.64898/2026.09.10.750595, 2026-09-13.
A single parameter moves a reaction-diffusion CA across collapsed, structured, saturated and overshooting regimes. The authors relate these regimes to pattern compressibility and to reservoir memory and separability.
Bears on §4.7 K (compression-based complexity) and on the L2(v) compression framing. It is an empirical link between regime, compressibility and computational capacity.

**13. Other dynamics items, one line each:**
- **da Fonseca, Presotto, Oliveira & Leonel**, *First-Order Transition to Chaos with Critical Slowing Down*, arXiv:2609.13614, submitted 12 Sep. A discontinuous integrability-to-chaos transition that still shows diverging relaxation time. Relevant to §4.3: critical slowing down alone does not certify a continuous critical point.
- **Vaidya**, *Learning-Induced Dynamical Transition in RNNs*, arXiv:2609.19288, submitted 16 Sep. A DMFT treatment of learning driving chaos to stability. Relevant to §4.1/§5.1.
- **Singh & Singh**, *Critical initialization destabilizes higher input derivatives*, arXiv:2609.09244, submitted 8 Sep.

Screened and judged to have no bearing: Condrey on Rule 30 constant traces (arXiv:2609.09431); Nersissian on ECA diagonal periods (arXiv:2609.25077, 2609.25078); Game of Life on Archimedean lattices and gliders on the hat/spectre monotiles (arXiv:2608.27622, 2609.22579); Vovk on universal measure of nonrandom objects (arXiv:2609.13513). All are CA/AIT mathematics, but none touches Class-4 classification, universality⇔criticality, or complexity estimators.

---

## Nothing found (sub-areas with no in-window hits)

- **Algorithmic information dynamics / BDM / CTM:** no Zenil-group or other BDM/AID paper in the window. arXiv searches for "block decomposition", "algorithmic information", "algorithmic probability" and the author "Zenil" returned only unrelated hits; OpenAlex returned only mass-generated Zenodo items. **Zenil (2010)'s phase-transition-coefficient conjecture (L2(v)) is unaddressed.**
- **Proofs or refutations linking universality and criticality, and CA class formalization (Wolfram classes, PCE):** none found.
- **Fixed-point or RG formalizations of self-models, Lawvere-style self-reference:** none, apart from #7's negative result. Two "Lawvere" arXiv hits are pure category theory.
- **Category-theoretic models of consciousness:** none. Tangentially, the categorical-probability paper *Statistical models as natural transformations… in Markov categories* (arXiv:2609.22929) exists but does not bear on §7.3.
- **Formal recurrent ≡ feedforward (unfolding-argument) results:** none. #8 and #9 are the closest.
- **Noise warning:** OpenAlex's in-window IIT/consciousness hits are dominated by bulk Zenodo uploads (e.g. the "E8 Intelligence Research" series and dozens of "Algorithmic Complexity of X" records). Apart from #5–#7, none were treated as citable.
