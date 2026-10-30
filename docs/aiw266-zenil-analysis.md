# AIW-266: Zenil's two CA-classification papers vs roadmap Module 2

**Short answer:** Zenil (2010) and Zenil & Villarreal-Zapata (2013) already do the empirical half of Module 2: they classify CA by algorithmic complexity instead of by eye. The 2013 paper also writes Wolfram's classes as a limit function in terms of Kolmogorov complexity. Neither paper supports Module 2's κ column. Both show Class 3 and Class 4 at the same compressibility, and both classifiers rest on thresholds fitted to data. What does separate rule 110 from rule 30 is his 2010 sensitivity coefficient, and that fits Module 2's Class 4/5 split rather than its κ row. The roadmap cites none of this. It also still carries the internal contradiction in §2.4 that the S244 review flagged (E3).

**What was read:** both papers in full, from arXiv PDFs fetched with curl (HTTP 200) and text-extracted.
- Paper A (arXiv:0910.4042) is the typeset *Complex Systems* 19(1) version.
- Paper B (arXiv:1304.2816**v4**, 2018) carries only "H. Zenil" in its running header. It may differ slightly from the published IJBC text co-authored with Villarreal-Zapata.
- The 2022 chapter was **not read**: OpenAlex reports it as closed-access.

## 1. What the papers do

**(A) Zenil 2010, *Complex Systems* 19(1):1–28**
- **Method.** Mathematica `Compress` (Deflate) is applied to the space-time evolution of all 256 ECA, run from a single black cell for 200 steps. The compressed length c is used as the estimate of K (§2, §2.1). The method is also applied to 3-colour CA and to 2-state 3-colour Turing machines (§3.2).
- **Result.** A 2-cluster split "was able to separate cellular automata that clearly fall into Wolfram's classes 3 and 4 from the rest, dividing complex and random-looking cellular automata from trivial and nested ones" (§3.1).
  - Rule 110 (c = 8502) lands inside the same high cluster as rules 30 and 45. Compressed length does **not** separate Class 4 from Class 3.
  - Rule 90, the Sierpiński/nested pattern, has c = 3778 and falls in the low cluster (Fig. 2–4).
- **Transition coefficient C.** This is a compression-based analogue of a Lyapunov exponent (§4–5). It measures the mean change in compressed length across Gray-code-adjacent initial conditions, normalised by runtime.
  - Rule 110 has C ≈ 0.27–0.40. Rules 30 and 1 have C ≈ 0 (Table 2, Fig. 17).
  - "At the right granular level, randomness shares informational properties with trivial systems… a random system is incapable of transmitting or carrying out information" (§5.2).
- **Conjecture.** "A system will be capable of universal computation if it has a large transition coefficient, at least larger than zero… The inverse, however, should not hold" (§5.2.1).
- **Stated limitations**
  - "It is only by running the system that the method is capable of revealing the dynamical properties. This is no different from a manual inspection in that regard" (§5.2.1).
  - Phase transitions are "undecidable" (§5.2).
  - The two main clusters "seem to support Wolfram's… PCE… no essential distinction between the classes" (§6).

**(B) Zenil & Villarreal-Zapata 2013, *IJBC* 23(9):1350159**
- **Formal definition.** A Wolfram class is defined as a limit: W(s) = lim_{i,t→∞} max W(s(i,t)), taken over initial conditions i and runtime t (§3). "W induces a non-effective partition… one can misclassify a computer program for some values i and t but not in the limit."
- **How it is applied in practice.** "Some lossless compression algorithm… a loose upper bound on K. **Thresholds are then trained** to divide W into 4 classes" (§3).
- **Measures.**
  - Normalised block Shannon entropy (§4.1).
  - Normalised compression NC = C(s)/max(C(s), |s|) (§4.2).
  - BDM/CTM, which estimates K from algorithmic probability via the Coding Theorem (§4.3).
  - All three agree: Pearson r = 0.936 (entropy–NC), 0.80 (NC–BDM) and 0.86 (BDM–entropy).
- **Resulting characterisation (§6)**
  - Class 1: asymptotic ratio 0.
  - Class 2: ratio < 1/2.
  - **Class 3: "compressibility ratio 1"; Class 4: "asymptotic compressibility ratio equal to 1".**
  - The paper states that this makes "Wolfram's classification… itself uncomputable in this formal version, a direct inference from the uncomputability of K."
- **Other results**
  - Membership depends on the initial condition. Rule 22 is bistable: symmetric initial conditions give Class 2, others give Class 3 (§3.2).
  - The share of complex rules grows with range and number of colours (§5, §7).

## 2. Overlap with Module 2

Module 2 = `paper/cosmology_formal/sb-hc4a-formalization.md` §2.

**What Zenil already did**
- **The motivation.** Module 2 opens: "classes are assigned by visual inspection… The classes lack formal definitions, the boundaries between classes are imprecise" (L51). That is the stated motivation of both papers.
- **The κ(O) column.** Module 2 defines "the asymptotic Kolmogorov complexity per symbol of the orbit sequence" (L61). Zenil's NC-over-(i,t) limit is the computable proxy for exactly that quantity, with the orbit-vs-initial-condition dependence handled explicitly.
- **The Class 4 vs Class 5 split.** Module 2 separates Class 4 (L76) from Class 5 (L77) by structure/universality rather than by complexity level. Zenil 2010 is the empirical precedent: random behaviour clusters with trivial behaviour on C, and rule 110 separates from rule 30 only on C, not on compressed length.

**What goes beyond Zenil**
- The r(Σ) and u(Σ) columns: reducibility and universality as defining criteria (L65–67, L81–83).
- The split of Wolfram's Class 3 into fractal and random (L53). Paper A partly supports it on single-cell initial conditions, where rule 90 compresses with Classes 1–2. Paper B undercuts it: from typical initial conditions rule 90 lands in C₃,₄ (Table 3 list).
- The Expressibility Ceiling (L89–103).
- Extension to continuous systems (§2.5).

**Where Zenil's results complicate or block Module 2**
1. **The boundary is not sharp.** Zenil's classes come from thresholds fitted to data (B §3), on a continuum of compressed lengths (A Fig. 2). Membership is uncomputable in the limit (B §6; Culik & Yu 1988, which the roadmap also omits even though the parent paper cites it). No compression measure supplies the knife-edge Module 2 asks for at L793.
2. **κ does not separate Class 4 from Class 3.** In B §6, Class 3 and Class 4 differ only in whether the ratio reaches 1 immediately or asymptotically. Both are maximally incompressible in the limit. Module 2's table puts κ(Class 4) strictly between 0 and max (L76–77). Zenil's measurements give Class 4 ≈ max.
3. **κ is a property of (f, s₀), not of f.** Rule 90 is algebraically reducible (L81 uses it), yet NC ≈ 1 from random initial conditions (B). The table mixes columns that describe the rule (r, u) with a column that describes the orbit (κ).
4. **The Expressibility Ceiling contradicts the table** (S244 review item E3, still unfixed). "κ(O) ≤ L/t → 0" (L95) holds for every finite rule with a finite or computable s₀, and so it forces κ = 0 for rule 110. That contradicts κ > 0 for Class 4 (L76).
   - Zenil's "incompressible Rule 30" reflects the limits of Deflate. True K of a single-cell evolution is O(log t).
   - The Corollary (L99) is also false. The trivial shift rule applied to a Martin-Löf-random s₀ has κ = 1. By Brudno's theorem, the complexity rate along almost every orbit equals the metric entropy, whatever the rule's description length.
   - So "Class 5 needs an infinite rule" does not follow. The randomness can come from the initial condition.

## 3. Citation checks

`grep` across the repo (excluding `tmp/`):
- `10.1007/978-3-031-03986-7_8` appears only in `drafts/aiw10-candidate-targets.md:43`, as the outreach hook. It is not in any paper.
- Zenil, BDM, "Coding Theorem", Brudno and Dubacq: **zero hits** in `paper/`.
- Crossref shows the 2022 chapter is **Zenil & Adams** (not "Zenil et al."), in *The Mathematical Artist*, Emergence, Complexity and Computation, pp. 171–190. It is closed-access and was not read, so it may address the question in §5 below.

## 4. Recommended edits to Module 2

All DOIs below are Crossref-verified.

1. **§2.1: add the prior-work paragraph.** Suggested text: "Algorithmic-information classifications already exist. Dubacq, Durand & Formenti (2001) classify rule tables by Kolmogorov complexity. Zenil (2010) and Zenil & Villarreal-Zapata (2013) classify by the compressibility of space-time evolutions, formalising the Wolfram class as a limit over initial conditions and runtime, and show the resulting partition to be non-effective. Culik & Yu (1988) prove membership undecidable. Module 2 does not claim a computable boundary. It proposes rule-level criteria (r, u) that these orbit-level measures approximate."
2. **§2.2 table.** Replace the κ column for Classes 3–5 with a depth-type or sensitivity measure, and state that κ depends on s₀. Two candidates: Bennett logical depth, which was the S244 fix; or Zenil's transition coefficient C, which already separates 110 from 30 empirically.
3. **§2.4.** Withdraw the Corollary and restate the Ceiling as a conjecture about **structured** complexity (depth), not κ. Add Brudno.
4. **§2.3 Class 4/5.** Cite Zenil 2010 §5.2 and §5.2.1: random behaviour patterns with trivial behaviour on C, and the conjectured link between C > 0 and universality.
5. **L793.** Replace "needs a rigorous proof" with a statement that a sharp boundary is provably non-computable, so the target is a definition plus a computable approximation with stated error.

**References to add**
- Zenil, H. (2010). Compression-based investigation of the dynamical properties of cellular automata and other systems. *Complex Systems*, 19(1), 1–28. https://doi.org/10.25088/complexsystems.19.1.1
- Zenil, H., & Villarreal-Zapata, E. (2013). Asymptotic behavior and ratios of complexity in cellular automata. *Int. J. Bifurcation and Chaos*, 23(9), 1350159. https://doi.org/10.1142/s0218127413501599
- Dubacq, J.-C., Durand, B., & Formenti, E. (2001). Kolmogorov complexity and cellular automata classification. *Theoretical Computer Science*, 259, 271–285. https://doi.org/10.1016/s0304-3975(00)00012-8
- Culik, K., II, & Yu, S. (1988). Undecidability of CA classification schemes. *Complex Systems*, 2(2), 177–190. Copy the entry from the parent paper; no DOI was checked.
- Zenil, H., & Adams, A. (2022). Algorithmic information dynamics of cellular automata. In *The Mathematical Artist* (Emergence, Complexity and Computation), pp. 171–190. Springer. https://doi.org/10.1007/978-3-031-03986-7_8. Cite only after reading it.
- *Optional, if BDM or CTM is adopted as the estimator*
  - Soler-Toscano, F., Zenil, H., Delahaye, J.-P., & Gauvrit, N. (2014). Calculating Kolmogorov complexity from the output frequency distributions of small Turing machines. *PLoS ONE*, 9(5), e96223. https://doi.org/10.1371/journal.pone.0096223
  - Zenil, H., Hernández-Orozco, S., Kiani, N. A., Soler-Toscano, F., Rueda-Toicen, A., & Tegnér, J. (2018). A decomposition method for global evaluation of Shannon entropy and local estimations of algorithmic complexity. *Entropy*, 20(8), 605. https://doi.org/10.3390/e20080605
- Bennett, C. H. (1988/1990). Logical depth and physical complexity. In *The Universal Turing Machine: A Half-Century Survey*, 227–258. Oxford UP. https://doi.org/10.1093/oso/9780198537748.003.0008. Crossref gives the 1990 date for the OUP reissue.
- Brudno: Crossref has only the 1978 note: Brudno, A. A., "The complexity of the trajectories of a dynamical system", *Russian Math. Surveys* 33(1), 197–198, https://doi.org/10.1070/rm1978v033n01abeh002243. The full 1983 *Trans. Moscow Math. Soc.* 44:127–151 paper was **not** found in Crossref; verify it separately.

## 5. The follow-up question for Zenil

> "Your 2013 limit characterisation separates Class 3 from Class 4 only by how the compression ratio approaches 1. In your 2010 paper, what pulls rule 110 away from rule 30 is the transition coefficient C instead. Is there a known result, or a counterexample, for the 2010 conjecture that universality implies C > 0 in the limit, computed with an estimator such as BDM that does not depend on the compressor? If it holds, C (not K) would be the candidate for a principled Class 4 boundary."

**Why the papers leave this open**
- Paper A states the conjecture on ECA evidence only. The evidence is rule 110, plus rule 54 as a candidate. It uses Deflate, t = 200 and n = 40, and gives no proof.
- Paper B moves to NC/BDM and to the limit definition but never returns to C. Its 3/4 split is a difference in convergence rate, with fitted thresholds.
- Neither paper asks whether a sensitivity-type quantity has a threshold that survives changes of estimator and of initial-condition enumeration.
- Caveat: the unread 2022 chapter may answer it. The mail can acknowledge that honestly ("if your 2022 AID chapter already settles this, a pointer is enough").
