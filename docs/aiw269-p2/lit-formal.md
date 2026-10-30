<!-- AIW-269 pass 2 (2026-02-17→08-25), formalization slice, S323 subagent. OpenAlex search 429 throughout; math.DS/cs.IT title-screened only. -->
<!-- AIW-269 pass 2, formal slice, window 2026-02-17..2026-08-25. Subagent sweep 2026-09-28. -->
# AIW-269 pass 2: formal/mathematical literature slice (fmt-formalization v4)

**Window:** first published 2026-02-17 to 2026-08-25. Items from 2026-08-26 onward are in `docs/aiw269-lit-formal.md` and are not repeated here.
**Sources:** full arXiv monthly listings (Feb–Aug 2026) for nlin.CG, nlin.AO, q-bio.NC, cs.FL, math.DS and cs.IT, about 7,100 entries, keyword-filtered by title. I also ran arXiv advanced search with a first-submission date filter (18 queries), Crossref with a pub-date filter (16 queries), and web search.
**Verification:** I checked every item below for title, authors and v1 date against its arXiv abstract page or its Crossref/OpenAlex DOI record. I also checked that none of them is in the roadmap's reference list.
**Gaps:** OpenAlex *search* returned 429 on every query ("anonymous search rate-limited"). OpenAlex DOI lookups worked, and Crossref stood in for it. Zenodo was skipped as instructed. In math.DS and cs.IT only titles were screened.

**Bottom line:** there is one MUST-ANSWER item. Roig, Muñoz & Morales give L2 a concrete *restricted* form: approximation-universality has an exact geometric condition, and that condition peaks numerically at λ_max ≈ 0⁻. Nothing touches L1 or E⊥K directly. Seven items are MUST-CITE, clustered on §4.3, §4.7 and §6.5.

---

## MUST-ANSWER

**1. Roig, A., Muñoz, M. A., & Morales, G. B. (2026). Driven criticality links universal computation and optimal representations.** arXiv:2607.21232, v1 23 Jul 2026.
The authors extend fixed-reservoir universality theorems to discrete-time driven reservoirs. They prove that the Neighborhood Separation Property is necessary and sufficient for universal approximation of input–output maps with a polynomial readout. Numerically, the separability index, prediction performance and power-law representation geometry all peak together in a narrow window at input-conditioned λ_max ≈ 0⁻. I read the full text: **no theorem states that NSP ⇒ marginal stability.** The link to criticality is empirical.
*Bears on:* L2 (§4.4, l.307), which invites "a precise restricted form under which they hold". This paper is exactly such a candidate. It differs from the L2 the roadmap states in three ways: (a) universality means *approximation* universality, not Turing universality; (b) criticality means edge of chaos (λ_max), not avalanche σ; (c) the step from universality to criticality is numerical. It also argues for §4.3 option 3 (λ_max primary).
*Action:* add it to L2 as the nearest existing result of L2's shape, alongside Zenil (2010) in L2(v), and state that the missing piece is a theorem NSP ⇒ λ_max → 0. The roadmap's "no result of L2's shape exists" framing is otherwise now out of date. Counterweight: #13 (Du & Wang) finds a forecasting optimum *off* the Lyapunov edge.

## MUST-CITE

**2. Nahum, A., & Roy, S. (2026). The damage spreading transition: a hierarchy of renormalization group fixed points.** arXiv:2603.22439, v1 23 Mar 2026.
Deterministic cellular automata (CA) fall into a strongly and a weakly irreversible phase, and the damage-spreading transition separates them. The paper shows that its critical point contains directed percolation as its first level, with an infinite hierarchy of higher RG fixed points that carry further universal exponents, analysed by field theory and RG.
*Bears on:* §4.3, L2(v) and §6.6. Damage spreading is the CA version of perturbation sensitivity: it is what λ_max measures, and what Zenil's phase-transition coefficient measures. This paper puts it in the directed-percolation / absorbing-state family, which is the same family as avalanche σ. That gives a formal handle on the Kanders et al. (2017) σ-vs-λ question, at least for CA. It also gives §6.6 a worked instance of "RG fixed point" for automaton dynamics.

**3. Jacobus, C. (2026). Finding the Edge of Chaos in a Ferromagnet: Quantifying the "Complexity" of 2D Ising Phase Transitions with Image Compression.** arXiv:2602.15185, v1 submitted 16 Feb 2026 20:45 UTC. That is after the arXiv cutoff, so it was announced 18 Feb and falls inside the window.
The paper defines a structural complexity C_s from lossless compression. C_s is normalised against sorted (ordered) and shuffled (disordered) surrogates and built as the product of distance-from-order and distance-from-disorder. Unlike raw compressed length, C_s peaks sharply at T_c.
*Bears on:* §4.7 K. The roadmap concedes, citing Zenil (2010), that compressed length cannot tell complex from chaotic, and it rescues K only by conditioning on the critical cluster G. A surrogate-normalised measure of this kind is regime-sensitive by construction. It could make K carry regime information on its own, or serve as a check on G. Single author, unrefereed.

**4. Cambrainha, G. G., Castro, D. M., Gollo, L. L., Carelli, P. V., & Copelli, M. (2026). Hierarchical organization of critical brain dynamics.** arXiv:2604.21832, v1 23 Apr 2026.
Phenomenological RG applied to mouse visual cortex and hippocampus shows that signatures of criticality vary systematically along the anatomical hierarchy. The direction of that gradient depends on the measure: static exponents point one way, the dynamic exponent the other, and task engagement modulates both.
*Bears on:* the §4.7 heterogeneity premise (regional c_i), which it supports empirically. It also warns that "σ_i … and/or λ_max,i" in the c_i definition is not innocent: different local criticality markers can rank regions in opposite orders. So E depends on the chosen marker, which is the §4.3 ambiguity reappearing at regional scale.

**5. Xiao, H., Zhao, X., Zhou, H., & Wang, W. (2026). Efficient coding under constraint drives neural systems towards criticality and sloppiness.** arXiv:2605.22598, v1 21 May 2026.
In a Gaussian population-coding model, maximising Fisher information under a resource constraint produces soft modes and diverging correlation length. With spatial structure added, the same optimum unifies statistical criticality (correlation length) with dynamical criticality (critical slowing down, bifurcation).
*Bears on:* §4.4 and §4.3. It is a *different* derivation route to criticality, running through coding optimality rather than the closure ⇒ universality ⇒ Class 4 chain. §4.4 should acknowledge it as the competing, better-developed route. It also partly addresses the §4.3 "which criticality" question.

**6. Barrett, A. B., Milinkovic, B., Mediano, P. A. M., Rosas, F. E., Bor, D., Barnett, L., & Seth, A. K. (2026). Integrated information theory: the good, the bad and the misunderstood.** arXiv:2604.11482, v1 13 Apr 2026.
The paper argues five points about IIT: high Φ ≠ "more consciousness"; Φ should give way to a *suite* of quantities describing states of consciousness in several dimensions; Φ is not well-defined for real physical systems and has never been computed on one; only proxies exist; and IIT needs a continuous-field reformulation.
*Bears on:* the §4.7 C_N/Φ paragraph. A leading IIT-literate group is independently calling for a multi-dimensional replacement of the single scalar, which strengthens the case for the (E, K) plane. It also supports the roadmap's refusal to use Φ as the extent index. Cite it next to Aaronson (2014).

**7. Abadie, V., Hutter, C., & Bölcskei, H. (2026). Recurrent neural networks approximate continuous functions.** arXiv:2606.20325, v1 18 Jun 2026.
The paper proves that a *single* ReLU RNN with fixed weights and fixed hidden dimension uniformly approximates any continuous function on [−1,1], where accuracy is bought by running it longer. Minimax lower bounds show that the runtime cannot be avoided.
*Bears on:* §6.5, which argues from Cybenko (1989) depth that six layers exceed the three-layer minimum. This theorem shows that *recurrence plus time* substitutes for added depth or width. For a recurrent cortex, the depth-counting argument is therefore the weaker framing. It also bears on the recurrent-vs-feedforward question (§6.3).

**8. Bessone, N., & Plantec, E. (2026). Emergent Macro-Criticality from Micro-Critical Agents.** arXiv:2605.01818, v1 3 May 2026.
In multi-agent systems whose agents each run a reservoir, near-critical dynamics *inside* each agent do not produce collective critical avalanches. Scale-free collective behaviour depends on the effective connectivity of the interaction network.
*Bears on:* §4.7. It is a toy model of the distinction the roadmap draws between the local indicator c_i and the extent E = P∞, the percolation of *connected* critical units. It shows that f_crit (option a) and collective criticality can come apart. The model is modest (ALife-style), so cite it briefly.

---

## NICE-TO-HAVE

**9. Sakabe, E. Y., Abrahão, F. S., Hernández-Orozco, S., Gudwin, R., & Zenil, H. (2026). Tighter bounds for algorithmic complexity estimation using a reusable code-based Block Decomposition Method.** arXiv:2606.23471, v1 22 Jun 2026.
This is a conditional BDM ("algorithmic attention") that reuses code across blocks. Exact optimisation is proven NP-hard, and the gains are bounded by algorithmic mutual information. Relevant to §4.7: BDM is an alternative K estimator to LZ, and this is the Zenil-group paper the previous pass reported missing (it predates that pass's window).

**10. Lesmana, N. S., Feng, L., Chen, K., & Lai, C. H. (2026). Self-organization to the edge of ergodicity breaking in a complex adaptive system.** arXiv:2604.15669, v1 17 Apr 2026.
In EvoSK the cascade branching ratio *equals* the spectral radius of the learning Jacobian, so critical branching and marginal stability are one condition. It is a model-class counterpoint to Kanders et al. (2017) in §4.3, showing when σ ≈ 1 and λ ≈ 0 coincide.

**11. Ciccarelli, V. (2026). Weak emergence, ontological hierarchies, and computational equivalence.** *Minds and Machines*, doi:10.1007/s11023-026-09794-9, published 17 Jul 2026.
Combining Bedau's weak emergence with Wolfram's PCE forces a system to "decide" whether its own trajectories are incompressible, which is undecidable. The author calls this the paradox of weak emergence. Relevant to L2(i), where the roadmap already calls PCE a conjecture, and to §6.2, since it is a formal limit on self-access by a different route than O_ESM ⊆ S_EWM.

**12. Egri-Nagy, A., & Nehaniv, C. L. (2026). Measuring the computational power of finite patches of cellular automata.** arXiv:2604.14966, v1 16 Apr 2026.
The paper turns a Game-of-Life patch into a transformation semigroup and measures its computational power with Krohn–Rhodes-style hierarchical decompositions. Relevant to L1: it offers a graded, algebraic measure of computational power, which is the "monotonicity, not universality" claim in L1 made measurable. It pairs with the Dehghani item in the prior pass.

**13. Du, Y., & Wang, X. (2026). Beyond the edge of chaos: stability–expressivity transfer in reservoir forecasting.** arXiv:2607.17909, v1 20 Jul 2026.
The best forecasting spectral radius does *not* coincide with the Lyapunov edge of the isolated, teacher-forced or closed-loop reservoir. Relevant to L2(iv) and §4.4, and it should be cited alongside #1.

**14. Rollier, M., & Baetens, J. M. (2026). Exact Lyapunov spectra of affine cellular automata and the parity rule on networks.** arXiv:2606.14521, v1 12 Jun 2026.
For affine (XOR) rules the spectrum is closed-form: the DFT of the stencil, or the log adjacency spectrum on graphs. It gives §4.2 an exactly solvable λ_max baseline for CA. The affine class is the one that maximises Φ in the Mayeux item of the prior pass.

**15. Topal, I., Poggialini, A., Dal Maschio, M., De Martino, D., Shriki, O., & Lombardi, F. (2026). Scaling and tuning to criticality in resting-state human MEG.** arXiv:2602.17820, v1 19 Feb 2026. Companion: Topal et al., *Early psychosis shows deviations in scaling behaviour within a critical regime*, arXiv:2606.06290.
RG-inspired coarse-graining of human MEG yields scale-invariant variance, covariance spectra and avalanches. Relevant to §4.2 as a candidate fourth measure (phenomenological RG) and to §6.6. Shriki is a ConCrit co-author.

**16. Musat, T. (2026). Neural weight norm = Kolmogorov complexity.** arXiv:2605.10878, v1 11 May 2026.
In fixed precision, the minimal weight norm of a *looped* network that outputs a string equals the string's Kolmogorov complexity up to a log factor. Relevant to §6.5 (complexity cost) and to L1, since universality enters through the loop.

**17. Kanai, R., & Ma, S. (2026). Intrinsic computational functionalism and simulated consciousness.** arXiv:2606.15348, v1 13 Jun 2026. With Ma & Kanai, arXiv:2606.06424.
Input–output canonical functionalism makes lookup tables and *unfolded* systems equivalent. A consciousness-relevant structure must also include internal mechanisms and interventions. This is the recurrent-vs-feedforward (unfolding) objection that the §6.4 closure claim will face. Kanai co-authored the Oizumi et al. (2025) reference the roadmap already cites.

**18. Fang, W., Li, X., Liu, J., Luo, J., Tong, Y., & Xu, K. (2026). Self-referential K-SAT and the finite analogue of Gödel's incompleteness theorem.** arXiv:2607.01671, v1 2 Jul 2026.
A finite self-referential construction in which no evaluator restricted to local subinstances can separate SAT from UNSAT. It is a finite, rigorous analogue of the §6.1 "no outside view" claim.

**19. Devireddy, A. (2026). Phase transitions in complexity: active cell growth, Shannon entropy and Kolmogorov complexity in dependent cell ranges of mobile automata with non-local rules.** *Complex Systems* 35(1), 63, doi:10.25088/complexsystems.35.1.63, 2026-03-15.
BDM and compression metrics detect abrupt "computational phase transitions" as non-locality varies. A minor empirical link for L2(v) and K.

**20. One line each:**
- **Castillo-Ramirez, Vazquez-Aceves & Zaldivar-Corichi**, *A categorical framework for cellular automata*, arXiv:2602.04049 (3 Feb, **before the window**, listed only because §7 has no in-window category-theory hit).
- **Griffith**, arXiv:2604.18635, PID-based integration measures.
- **Kearney**, arXiv:2605.12536, IIT repertoires re-derived from maximum caliber.
- **Langer, van Oostrum & Ay**, arXiv:2608.14165, integrated information in active-inference agents.

All three are IIT formal variants, relevant only to §4.7 positioning.
- **Ren & Feng**, arXiv:2606.10384: near-critical branching in LSTMs depends on capacity.
- **Ge et al.**, *Commun. Biol.* doi:10.1038/s42003-026-10713-y: criticality separates UWS from MCS. This belongs to the criticality slice.

---

## Screened out / boundary notes
- **Just outside the window:** Azizpour, Priesemann, Zierenberg & Levina, *Finite integration time can shift optimal sensitivity away from criticality*, arXiv:2602.09491, v1 10 Feb 2026. It is highly relevant to the σ-*band* of §4.2 and to L2(iv), and worth a manual decision. Nascimento et al., *PRE* doi:10.1103/3lsz-87dd (June 2026), was on arXiv as 2506.14053 in 2025, so it is not new.
- **CA mathematics without bearing on classes, universality or criticality:** Gwozdz, no weakly factor-universal CA (2603.23570); Audouard & Theyssier on Kůrka's dichotomy (2602.20623); Kamilya, Kari & Paturi on non-uniform CA (2605.22762); Pita on ECA causal tiles (2604.00273); Koopmans et al. on predictability (2604.01088); Garrido (*Array*) and Yokota (*Complex Systems*) on ECA and machine learning or reservoirs.
- **Consciousness-formal items judged low quality or out of scope:** 2605.13884 (USK), 2605.00024, 2607.08302, 2603.23539 (PLDR-LLM SOC), the Berdinsky & Ordina SSRN paper (Lawvere and the Absolute), and the Tononi-group chapters 2608.11398 and 2608.24928, which are IIT exposition rather than critique.
- **Nothing found:** proofs or refutations of L1 (closure ⇒ universality); fixed-point or RG models of self-models; category-theoretic or information-geometric consciousness models in the window, including any Oizumi/Kanai bundle follow-up; formal critiques of IIT's *axioms* (Barrett et al. critique Φ's usage, not the axioms); a proof of the Zenil (2010) phase-transition-coefficient conjecture.
