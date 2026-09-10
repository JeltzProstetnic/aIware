<!-- Action: reference -->
# Verification: model-based vs model-free RL literature vs FMT's "recency/priority override"

**Session:** S300 · **Date:** 2026-08-10 · **Backlog:** `AIW-202` (positioning ×4)
**Status of this file:** verification report. Every citation below was checked against a publisher page, DOI resolution, PubMed, PMC, or an open preprint. Anything not so checked is marked **UNVERIFIED**.

**What was being verified.** `backlog.md` (AIW-202) and `.claude/knowledge/didactic-patterns.md` (pattern block, lines ~610–630) record a positioning risk in these words:

> "*Explicit deliberation overriding a recency-weighted habit* is **model-based versus model-free reinforcement learning**, a large and well-developed literature (Daw, Dolan, Doll, Gläscher and others) that has described exactly this arbitration since the mid-2000s. Stated as-is, a reviewer answers it in one line. **FMT's differentiator must be step (i): that the override works by RE-INSTANTIATING THE PHENOMENAL VALUE, not by retrieving an abstract state-value.**"

The names Daw, Dolan, Doll, Gläscher were recorded from background knowledge and flagged `⚠ VERIFY the model-based/model-free citations before any use`. They are now verified. **The four names are correct and the papers exist as remembered.** The positioning risk is real, and it is worse than the note assumes — see §E.

---

## A. Citation block (verified — ready to paste)

All entries below confirmed against PubMed/PMC/publisher. DOIs resolve.

### A.1 The foundational model-based / model-free set

Daw, N. D., Niv, Y., & Dayan, P. (2005). Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control. *Nature Neuroscience*, 8(12), 1704–1711. https://doi.org/10.1038/nn1560 · PMID 16286932
— *Paywalled at publisher; abstract verified via PubMed. An author copy is publicly posted at matt.colorado.edu.*

Daw, N. D., Gershman, S. J., Seymour, B., Dayan, P., & Dolan, R. J. (2011). Model-based influences on humans' choices and striatal prediction errors. *Neuron*, 69(6), 1204–1215. https://doi.org/10.1016/j.neuron.2011.02.027 · PMID 21435563 · PMCID PMC3077926
— *Free full text via PMC.*

Gläscher, J., Daw, N., Dayan, P., & O'Doherty, J. P. (2010). States versus rewards: Dissociable neural prediction error signals underlying model-based and model-free reinforcement learning. *Neuron*, 66(4), 585–595. https://doi.org/10.1016/j.neuron.2010.04.016 · PMID 20510862 · PMCID PMC2895323
— *Free full text via PMC.*

Doll, B. B., Simon, D. A., & Daw, N. D. (2012). The ubiquity of model-based reinforcement learning. *Current Opinion in Neurobiology*, 22(6), 1075–1081. https://doi.org/10.1016/j.conb.2012.08.003 · PMCID PMC3513648
— *Free full text via PMC. Author copy also at princeton.edu/~ndaw/dsd12.pdf.*

**Note on the remembered author lists.** All four are exactly as recorded in the project note — including the five-author order on Daw et al. 2011 (Daw, Gershman, Seymour, Dayan, Dolan) and the four-author order on Gläscher et al. 2010 (Gläscher, Daw, Dayan, O'Doherty). No correction needed. "Dolan" in the project's four-name list is Raymond J. Dolan, who appears as last author on Daw et al. 2011 (and see Dolan & Dayan 2013, §B).

### A.2 The contemporary challenge to that set

Feher da Silva, C., Lombardi, G., Edelson, M., & Hare, T. A. (2023). Rethinking model-based and model-free influences on mental effort and striatal prediction errors. *Nature Human Behaviour*, 7(6), 956–969. https://doi.org/10.1038/s41562-023-01573-1 · PMID 37012365
— *Paywalled; abstract verified via PubMed. Preprint: bioRxiv 2022.11.04.515162, "A new take on model-based and model-free influences on mental effort and striatal prediction errors."*
— **Correction to a common misattribution: Montague is NOT an author.** The author list is Feher da Silva, Lombardi, Edelson, Hare (Zurich Center for Neuroeconomics). If the project has this filed with Montague, fix it.

### A.3 Episodic / sampling-based control — the literature that matters most for FMT (see §E)

Lengyel, M., & Dayan, P. (2007). Hippocampal contributions to control: The third way. In *Advances in Neural Information Processing Systems 20* (NIPS 2007). — *Open access via NeurIPS proceedings. Page numbers not shown on the proceedings landing page; cite by volume.* **UNVERIFIED: exact page range.**

Gershman, S. J., & Daw, N. D. (2017). Reinforcement learning and episodic memory in humans and animals: An integrative framework. *Annual Review of Psychology*, 68, 101–128. https://doi.org/10.1146/annurev-psych-122414-033625 · PMID 27618944
— *Author copy at gershmanlab.com/pubs/GershmanDaw17.pdf (PDF text extraction failed in this session — abstract not quoted verbatim below).* **UNVERIFIED: verbatim internal quotes.** Bibliographic details verified.

Bornstein, A. M., Khaw, M. W., Shohamy, D., & Daw, N. D. (2017). Reminders of past choices bias decisions for reward in humans. *Nature Communications*, 8, 15958. https://doi.org/10.1038/ncomms15958 · PMID 28653668 · PMCID PMC5490260
— *Open access. Preprint: bioRxiv 033910.*

Bornstein, A. M., & Norman, K. A. (2017). Reinstated episodic context guides sampling-based decisions for reward. *Nature Neuroscience*, 20(7), 997–1003. https://doi.org/10.1038/nn.4573 · PMID 28581478
— *Paywalled at Nature (fetch blocked by IdP redirect this session); bibliographic details verified via PubMed listing and eScholarship record (escholarship.org/uc/item/6v92r19q).* **UNVERIFIED: verbatim abstract.**

Mattar, M. G., & Daw, N. D. (2018). Prioritized memory access explains planning and hippocampal replay. *Nature Neuroscience*, 21(11), 1609–1617. https://doi.org/10.1038/s41593-018-0232-z · PMID 30349103
— *Paywalled; abstract verified via PubMed. Preprint: bioRxiv 225664. Code: github.com/marcelomattar/PrioritizedReplay.*

### A.4 Prior art for the *proposed differentiator* (outside RL — see §E)

Damasio, A. R. (1996). The somatic marker hypothesis and the possible functions of the prefrontal cortex. *Philosophical Transactions of the Royal Society of London B: Biological Sciences*, 351(1346), 1413–1420. https://doi.org/10.1098/rstb.1996.0125 · PMID 8941953

Gilbert, D. T., & Wilson, T. D. (2007). Prospection: Experiencing the future. *Science*, 317(5843), 1351–1354. https://doi.org/10.1126/science.1144161 · PMID 17823345

Kahneman, D., Wakker, P. P., & Sarin, R. (1997). Back to Bentham? Explorations of experienced utility. *The Quarterly Journal of Economics*, 112(2), 375–406. https://doi.org/10.1162/003355397555235

Peters, J., & Büchel, C. (2010). Episodic future thinking reduces reward delay discounting through an enhancement of prefrontal-mediotemporal interactions. *Neuron*, 66(1), 138–148. https://doi.org/10.1016/j.neuron.2010.03.026 · PMID 20399735

Dayan, P., & Berridge, K. C. (2014). Model-based and model-free Pavlovian reward learning: Revaluation, revision, and revelation. *Cognitive, Affective, & Behavioral Neuroscience*, 14(2), 473–492. https://doi.org/10.3758/s13415-014-0277-8 · PMID 24647659
— *Paywalled at Springer; abstract + Fig. 1 caption verified via PubMed listing. Author copy at gatsby.ucl.ac.uk/~dayan/papers/dayber14.pdf.* **This is the single most important citation in this report — see §E.2.**

### A.5 The arbitration set, the successor representation, and the dichotomy critiques

Full verified citations with quotes are given inline in the sections where they are argued, rather than duplicated here:

- **Arbitration mechanisms → §B.6–B.12:** Lee, Shimojo & O'Doherty 2014; Kim et al. 2019; Keramati, Dezfouli & Piray 2011; Pezzulo, Rigoli & Chersi 2013; Kool, Gershman & Cushman 2017; Kool, Cushman & Gershman 2016; Held et al. 2026; Boureau, Sokol-Hessner & Daw 2015; Otto et al. 2013 (*Psych. Sci.*); Otto et al. 2013 (*PNAS*); Tricomi, Balleine & O'Doherty 2009; Dolan & Dayan 2013.
- **Recency/priority near-misses → §C:** Miller, Shenhav & Ludvig 2019; Mattar & Daw 2018; Hardwick et al. 2019; Logan 1988; Bouton 2021.
- **Successor representation → §D.3:** Dayan 1993; Momennejad et al. 2017; Russek et al. 2017; Gershman 2018; Carvalho et al. 2024.
- **Dichotomy critiques → §D.4–D.5:** Collins & Cockburn 2020; Akam, Costa & Dayan 2015; Feher da Silva & Hare 2020; Miller, Shenhav & Ludvig 2019; Miller, Ludvig, Pezzulo & Shenhav 2018; Moskovitz et al. 2024; Collins 2025/26; **Mattar & Daw 2026**.

### A.6 Supporting / architecture citations

Daw, N. D., & Dayan, P. (2014). The algorithmic anatomy of model-based evaluation. *Philosophical Transactions of the Royal Society B*, 369(1655), 20130478. https://doi.org/10.1098/rstb.2013.0478 · PMID 25267820

Gershman, S. J., Markman, A. B., & Otto, A. R. (2014). Retrospective revaluation in sequential decision making: A tale of two systems. *Journal of Experimental Psychology: General*, 143(1), 182–194. https://doi.org/10.1037/a0030844 · PMID 23230992

---

## B. The arbitration mechanisms, per account (with verbatim quotes)

**Headline: the field has NOT settled its own arbitration story.** Four incompatible answers are in print, and the most recent evidence attacks the two most popular ones. This matters for positioning — see §E.

### B.1 Uncertainty (Daw, Niv & Dayan 2005) — the original account

> "However, such a surfeit of control raises an additional choice problem: how to arbitrate between the systems when they disagree."
> "We suggest a Bayesian principle of arbitration between them according to uncertainty, so each controller is deployed when it should be most accurate."
> — *abstract, verified via PubMed*

**Arbitrating variable: relative uncertainty of each controller's value estimate.** Whichever system is currently more confident takes control. Note that the paper frames the whole problem exactly as FMT does — "how to arbitrate between the systems when they disagree" — in 2005.

### B.2 Trial number / amount of training (Gläscher, Daw, Dayan & O'Doherty 2010)

Their hybrid model does *not* use uncertainty. It uses a fixed decay over the session:

> "The relative weighting is expected to change over time; indeed, given suitable prior expectations, there are normative proposals for determining how (Daw et al., 2005)"
> "Following Camerer and Ho (1998), we characterize the form of this change with an exponential function: *w*_t = *l* × *e*^−*kt*  where *w*_t is the trial-specific weight term for trial number *t*, and *l* and *k* are two free parameters describing the form of the exponential decay (*l*: offset, *k*: slope)."
> — *verified via PMC2895323*

**Arbitrating variable: trial index — i.e. accumulated training.** Model-based control dominates early and decays toward model-free as experience accumulates.

**⚠ DO NOT MISREAD THIS AS RECENCY.** A first pass over this paper reads the exponential decay as "recency." It is not. The weight is a function of *how many trials have elapsed in the session*, not of *how recently a particular outcome was experienced*. This is the exact conflation §C warns about, and the project must not repeat it.

### B.3 Uncertainty *plus* cost-benefit (Doll, Simon & Daw 2012)

> "Given estimates from both systems, one favorable strategy is to select the least uncertain among them."
> "A recent theory framed arbitration more explicitly in terms of the costs (time) and benefits (better reward harvesting) of performing model-based evaluation."
> — *verified via PMC3513648*

**Arbitrating variables: uncertainty, and separately the time-cost/benefit of deliberating.** By 2012 the review is already presenting two competing arbitration stories side by side rather than one settled one.

### B.4 The integration story was openly unfinished (Daw & Dayan 2014)

> "Here, we study the realization of MB calculations, and the ways that this might be woven together with MF values and evaluation methods. **There are as yet mostly only hints in the literature as to the resulting tapestry, so we offer more preview than review.**"
> — Daw & Dayan (2014), *Phil. Trans. R. Soc. B* 369(1655):20130478, abstract, verified via PubMed 25267820

The two architects of the framework describing their own integration account as "more preview than review." This is a direct, quotable admission that the arbitration mechanism was not settled as of 2014.

### B.5 The cooperative alternative — model-based *trains* model-free (Gershman, Markman & Otto 2014)

This is not arbitration at all; it is a different architecture.

> "Some evidence suggests that control can be shifted between these systems using neural or behavioral manipulations, but other evidence suggests that the systems are more intertwined than a competitive account would imply. In 4 behavioral experiments, using a retrospective revaluation design and a cognitive load manipulation, we show that human decisions are more consistent with **a cooperative architecture in which the model-free system controls behavior, whereas the model-based system trains the model-free system by replaying and simulating experience**."
> — Gershman, S. J., Markman, A. B., & Otto, A. R. (2014). *J. Exp. Psychol. Gen.*, 143(1), 182–194. https://doi.org/10.1037/a0030844 · PMID 23230992 — *abstract verified via PubMed*

**⚠⚠ This is FMT's step (iii) verbatim.** The project's mechanism reads: "cognition adjudicates and assigns credit; **the implicit side then complies**." Gershman, Markman & Otto say the model-based system trains the model-free system by *replaying and simulating experience* — and they say it about human data, in 2014, using a retrospective-revaluation design. The FMT claim that "the implicit side complies" is not novel; it is the Dyna-in-humans result.

### B.6 Reliability (Lee, Shimojo & O'Doherty 2014) — the explicit arbitration paper

Lee, S. W., Shimojo, S., & O'Doherty, J. P. (2014). Neural computations underlying arbitration between model-based and model-free learning. *Neuron*, 81(3), 687–699. https://doi.org/10.1016/j.neuron.2013.11.028 · PMID 24507199 · PMCID PMC3968946 (free author manuscript)

> "We provide evidence for an arbitration mechanism that allocates the degree of control over behavior by model-based and model-free systems as a function of the **reliability of their respective predictions**."
> — abstract, verified via PubMed

From the body (*medium confidence — automated full-text read of PMC3968946; string-match before quoting in print*):

> "It has been hypothesized (Daw et al., 2005) but never directly tested, that an arbitrator evaluates the performance of each of these systems and sets the degree of control that each system has over behavior according to the reliability of those predictions."
> "The reliability of the model-based (RelMB) is defined as the ratio of the mean prediction and the uncertainty of that prediction for SPE, a variance-to-mean ratio that is formally known as an inverse of the index of dispersion."
> "When PMB is high, control is dominated by the model-based system, whereas when PMB is low, control is dominated by the model-free system."

**Arbitrating variable: relative *reliability*, asymmetrically computed** — Bayesian over state prediction errors for the model-based side, a simpler |RPE|-tracking estimate for the model-free side. **This is NOT the same quantity as Daw 2005's value uncertainty**, and Lee et al. report out-fitting a Daw-style Bayesian-value-uncertainty variant. Two of the field's flagship arbitration papers therefore arbitrate on *different variables*.

*Extension:* Kim, D., Park, G. Y., O'Doherty, J. P., & Lee, S. W. (2019). Task complexity interacts with state-space uncertainty in the arbitration between model-based and model-free learning. *Nature Communications*, 10, 5738. https://doi.org/10.1038/s41467-019-13632-1 — "Participants tended to increase model-based RL control in response to increasing task complexity. However, they resorted to model-free RL when both uncertainty and task complexity were high."

### B.7 Value of information vs. the opportunity cost of time (Keramati; Pezzulo)

Keramati, M., Dezfouli, A., & Piray, P. (2011). Speed/accuracy trade-off between the habitual and the goal-directed processes. *PLoS Computational Biology*, 7(5), e1002055. https://doi.org/10.1371/journal.pcbi.1002055 · **open access CC-BY** · PMC3102758

> "we propose a normative model for arbitration between the two processes that makes an approximately optimal balance between search-time and accuracy in decision making"
> "Having the cost and benefit of deliberation for each action, if the benefit is greater than the cost … the arbitrator will decide to run the goal-directed system for estimating the value of action."
> "For computing the cost of deliberation … assuming that deliberation about the value of each action takes a fixed time, [τ], the cost of deliberation can be quantified as [τ·ρ̄]; where [ρ̄] is the average rate of reward per time unit."
> *(PLOS renders equations as images; symbol names reconstructed from surrounding prose — sentence text high confidence, symbol names medium.)*

**Arbitrating variable: value of perfect information vs. τ × average reward rate.** Note the reward-rate term — Keramati's arbitrator is sensitive to the *global opportunity cost of time*. **Lee's arbitrator has no such term at all.**

Pezzulo, G., Rigoli, F., & Chersi, F. (2013). The mixed instrumental controller: using value of information to combine habitual choice and mental simulation. *Frontiers in Psychology*, 4, 92. https://doi.org/10.3389/fpsyg.2013.00092 · **open access** · PMC3586710

> "mental simulation entails cognitive effort and increases the reward delay, it is activated only when the associated 'Value of Information' exceeds its costs."
> "the MIC calculates the Value of Information (VoI; Howard, 1966) of mental simulation on the basis of **uncertainty and of how much the alternative 'cached' action values differ against each other**."
> *(medium confidence — automated read of PMC3586710)*

**Arbitrating variable: VoI (uncertainty *plus decision conflict*) vs. cognitive effort + temporal discounting.** And note: Pezzulo et al. **deny two separate controllers** — one *Mixed Instrumental Controller* produces both behaviours.

### B.8 Cost-benefit (Kool, Gershman & Cushman) — and their own demolition of the evidence base

Kool, W., Gershman, S. J., & Cushman, F. A. (2017). Cost-benefit arbitration between multiple reinforcement-learning systems. *Psychological Science*, 28(9), 1321–1333. https://doi.org/10.1177/0956797617708288 · PMID 28731839 · *not OA, no PMCID*

> "It is unclear, however, how people choose to allocate control between these systems. Here, we propose that **arbitration occurs by comparing each system's task-specific costs and benefits.** … This suggests that humans adaptively balance habitual and planned action through **on-line cost-benefit analysis**."
> — abstract, verified via Europe PMC. **Body text UNVERIFIED** (publisher 403; author PDF returned only metadata).

Kool, W., Cushman, F. A., & Gershman, S. J. (2016). When does model-based control pay off? *PLoS Computational Biology*, 12(8), e1005090. https://doi.org/10.1371/journal.pcbi.1005090 · **open access CC-BY 4.0** · PMC5001643

> "It is assumed that this trade-off between accuracy and computational demand plays an important role in the arbitration between the two strategies, but we show that **the hallmark task for dissociating model-free and model-based strategies, as well as several related variants, do not embody such a trade-off.**"

**⇒ The 2016 result is a methodological attack on the empirical foundation of the reliability *and* cost-benefit literatures alike: the canonical two-step task does not contain the trade-off the theories are about.**

Held, L. K., Lesage, E., Kool, W., & Braem, S. (2026). When models matter: environmental demand guides the arbitration between model-based and model-free control. *Cognitive, Affective, & Behavioral Neuroscience*, 26(1), 33–42. https://doi.org/10.3758/s13415-025-01350-9 (OA preprint: PsyArXiv 10.31234/osf.io/dezcf_v1) — adds *learned environmental statistics* as a further arbitration input.

### B.9 Opportunity cost of a shared executive resource (Boureau, Sokol-Hessner & Daw 2015)

Boureau, Y.-L., Sokol-Hessner, P., & Daw, N. D. (2015). Deciding how to decide: self-control and meta-decision making. *Trends in Cognitive Sciences*, 19(11), 700–710. https://doi.org/10.1016/j.tics.2015.08.013 · PMID 26483151 · *not OA*

> "We propose that these situations are linked by a strikingly similar core dilemma, pitting the **opportunity costs of monopolizing shared resources such as executive functions for some time, against the possibility of obtaining a better outcome.**"
> — abstract, verified via Europe PMC. **Body text UNVERIFIED** (paywalled).

### B.10 External resource scarcity — load and stress (Otto et al. 2013 ×2)

Otto, A. R., Gershman, S. J., Markman, A. B., & Daw, N. D. (2013). The curse of planning: dissecting multiple reinforcement-learning systems by taxing the central executive. *Psychological Science*, 24(5), 751–761. https://doi.org/10.1177/0956797612463080 · PMC3843765

> "**The factors governing which system controls behavior—and under what circumstances—are still unclear.** … These results demonstrate that competition between multiple learning systems can be controlled on a trial-by-trial basis by **modulating the availability of cognitive resources**."

Otto, A. R., Raio, C. M., Chiang, A., Phelps, E. A., & Daw, N. D. (2013). Working-memory capacity protects model-based learning from stress. *PNAS*, 110(52), 20941–20946. https://doi.org/10.1073/pnas.1312011110 · PMC3876216

> "We found that **stress response attenuates the contribution of model-based, but not model-free, contributions to behavior.**"

**⇒ Neither load nor stress changes either system's predictive reliability — so a strict Lee/Daw reliability arbitrator does not predict these shifts.** Resource-cost accounts do. This is a live empirical inconsistency, not a stylistic difference.

### B.11 Cumulative training (Tricomi, Balleine & O'Doherty 2009)

Tricomi, E., Balleine, B. W., & O'Doherty, J. P. (2009). A specific role for posterior dorsolateral striatum in human habit learning. *European Journal of Neuroscience*, 29(11), 2225–2232. https://doi.org/10.1111/j.1460-9568.2009.06796.x · PMC2758609

> "In this experiment, we show that **extensive training on a free-operant task reduces the sensitivity of participants' behavior to a reduction in outcome value.** … These results provide evidence for a shift from goal-directed to habit-based control of instrumental actions in humans…"

**Arbitrating variable: amount of training.** No trial-by-trial arbitrator at all — this is the Dickinson/Balleine tradition, a slow structural variable, and it is answering a different question from the computational arbitration models.

### B.12 The field says, in print, that it has not settled this

Dolan, R. J., & Dayan, P. (2013). Goals and habits in the brain. *Neuron*, 80(2), 312–325. https://doi.org/10.1016/j.neuron.2013.09.007 · **OA CC-BY** · PMC3807793

> "One idea is that it should depend on the **relative uncertainties of the systems** …"
> "**Various suggestions have been made for how arbitration should proceed, but this is an area where much more work is necessary.**"
> *(medium confidence — automated read of PMC3807793)*

**This is the single most quotable line in the entire report for FMT's positioning:** the field's two most senior figures, in *Neuron*, stating the arbitration story is unsettled. Pair it with Daw & Dayan 2014's "more preview than review" (§B.4) and Mattar & Daw 2026 (§D.5).

### B.13 Where the accounts contradict each other — the disagreement map

| Account | Arbitrating variable | Contradicts |
|---|---|---|
| Daw, Niv & Dayan 2005 | Bayesian uncertainty over **value estimates** | Lee 2014 (different currency); Gläscher 2010 |
| Gläscher et al. 2010 | **trial number** (fixed exponential decay) | Daw 2005 (not normative) |
| Lee, Shimojo & O'Doherty 2014 | **reliability of prediction errors** (asymmetric) | Daw 2005 (out-fits a value-uncertainty variant); has **no time-cost term** |
| Keramati et al. 2011 | VPI vs **τ × average reward rate** | Lee 2014 (which omits reward rate entirely) |
| Pezzulo et al. 2013 | VoI (uncertainty + **decision conflict**) vs effort+delay | all two-controller accounts — posits ONE controller |
| Kool et al. 2017 | task's **measured** reward advantage | Keramati/Pezzulo (benefit derived from agent's own uncertainty) |
| Kool et al. 2016 | — | **the entire two-step-task evidence base** |
| Boureau et al. 2015 | opportunity cost of **shared executive resources** | reliability accounts |
| Otto et al. 2013 ×2 | externally imposed **load / stress** | strict reliability accounts (which don't predict the shift) |
| Tricomi et al. 2009 | **cumulative training** | all trial-by-trial arbitration accounts |
| Gershman, Markman & Otto 2014 | *none* — cooperative, MB **trains** MF | all competitive-arbitration accounts |
| Hardwick et al. 2019 | **response-preparation latency** | value-weighting/mixing accounts, in kind |
| Bouton 2021 | **context and attention** | recency- and value-based gating alike |
| Miller, Shenhav & Ludvig 2019 | (contingency, habitization) — habit is **value-free** | says the literature has been arbitrating between the wrong two things |
| Feher da Silva et al. 2023 | rejects cost-benefit arbitration outright | Kool 2017; Doll 2012; Daw et al. 2011 striatal result |
| Collins 2025/2026 | neither component is standard RL | all of the above |

**⇒ Sixteen accounts, at least nine mutually incompatible arbitrating variables, and no convergence over twenty-one years.**

### B.14 The 2023 attack on the empirical cornerstone

**The 2023 attack, verbatim:**

> "A standard assumption in neuroscience is that low-effort model-free learning is automatic and continuously used, whereas more complex model-based strategies are only used when the rewards they generate are worth the additional effort. **We present evidence refuting this assumption.** First, we demonstrate flaws in previous reports of combined model-free and model-based reward prediction errors in the ventral striatum that probably led to spurious results. **More appropriate analyses yield no evidence of model-free prediction errors in this region.** Second, we find that task instructions generating more correct model-based behaviour reduce rather than increase mental effort. **This is inconsistent with cost-benefit arbitration between model-based and model-free strategies.** Together, our data indicate that **model-free learning may not be automatic**. Instead, humans can reduce mental effort by using a model-based strategy alone rather than arbitrating between multiple strategies. **Our results call for re-evaluation of the assumptions in influential theories of learning and decision-making.**"
> — Feher da Silva et al. (2023), abstract, verified via PubMed 37012365

Note what this does to the project's named set: it directly targets the ventral-striatal result of **Daw et al. 2011**, one of the four papers the project intended to cite.

---

## C. Is recency, or a priority signal, ever the *arbitrating* variable?

**Answer: NO for recency. NO for priority, in the sense the project needs.** Both terms appear in this literature, but never as the variable that decides *which of the two systems controls behaviour*. The distinction is sharp and the project must state it correctly or a reviewer will.

### C.1 Recency — present everywhere, but *inside* the model-free system

Recency-weighting is constitutive of model-free TD learning: an exponentially-decaying error-driven update *is* a recency-weighted running average, and eligibility traces are literally a recency mechanism. That is **within-system**, not **between-system**. No verified account makes "how recently was this experienced" the arbitrator.

Recency also appears as the *constitutive mechanism of habit itself* — Miller, Shenhav & Ludvig (2019) build habits from "**the direct strengthening of recently taken actions rather than through the encoding of outcomes**" (verified abstract). Again: recency builds one of the systems; it does not referee between them.

**The four near-misses, in descending order of relevance. None is a recency arbitrator, and the project must be able to say why.**

**(i) Miller, Shenhav & Ludvig 2019 — the closest genuine case.** Their habit strength is explicitly recency-weighted *and* it feeds their arbiter (*medium confidence — automated read of PMC6548181*):

> "This action history is tracked by a matrix of habit strengths, Ht, in which Ht(s,a) acts as a **recency-weighted average** of how often action a was taken in state s prior to timepoint t."
> "The arbiter governs the relative influence of each controller on each trial."
> "This calculation represents a push-pull relationship whereby goal-directed control is facilitated to the extent that the **action–outcome contingency** is high, whereas habits are facilitated to the extent that **habitization** is large."

Read precisely: the arbitrating variables are (contingency *g*, habitization *h*), and *h* is a **concentration/inequality statistic over a recency-weighted distribution** — not elapsed time since an experience. A recency-weighted quantity enters the arbitrator; recency is not the arbitrating variable. **This is the nearest thing in print, and it is still not FMT's claim — but it is close enough that a reviewer will raise it.**

**(ii) Mattar & Daw 2018 — "need" is *future* occupancy, not past recency.** (*medium confidence — automated read of PMC6203620*):

> "EVB(sk,ak) = Gain(sk,ak) × Need(sk)"
> "The need term quantifies the number of times the agent is **expected to harvest the gain by visiting the target state in the future.**"
> "the need term is straightforward (it is the SR, which the brain has been proposed to track for other reasons)."

A full-text search for recency-linked wording found no sentence tying *need* to how recently a state was visited; the framing is prospective. **⚠ One-level-down trap:** the SR, when learned by TD, is *estimated* by a recency-weighted update — so recency enters the estimator of need, not the definition of need. Same (a)/(b) confusion, one layer deeper. Do not cite this as a recency mechanism.

**(iii) Hardwick et al. 2019 — arbitration by preparation latency.** Hardwick, R. M., Forrence, A. D., Krakauer, J. W., & Haith, A. M. (2019). Time-dependent competition between goal-directed and habitual response preparation. *Nature Human Behaviour*, 3(12), 1252–1262. https://doi.org/10.1038/s41562-019-0725-0

> "we show that **limiting the time available for response preparation can unmask latent habits** … More extensive practice **reduced the latency** at which habitual responses were prepared, in turn increasing the likelihood of their being expressed."

A real, empirically supported, non-value arbitration variable — **time available within the trial**. Temporal, but not recency of experience. Note it is also incompatible *in kind* with mixing-weight accounts: a habit can be fully formed and never expressed.

**(iv) Logan 1988 instance theory** — *Psychological Review*, 95(4), 492–527, https://doi.org/10.1037/0033-295X.95.4.492 (Crossref-verified). Automatization as a race between an algorithm and retrieval of stored instances; whichever finishes first controls the response. Genuinely "which process controls behaviour is decided by memory-retrieval dynamics," but driven by **practice/frequency** (Logan's power law), outside the RL literature, and **UNVERIFIED** for verbatim quotation (read only via secondary summaries).

**(v) Not arbitration at all — do not cite as such.** The choice-kernel / perseveration term in most fitted RL models *is* an exponentially decaying trace of recent choices, but it is an **additive bias on action values**, not an arbitrator between systems.

**(vi) A rival gating variable that is neither recency nor reliability.** Bouton, M. E. (2021). Context, attention, and the switch between habit and goal-direction in behavior. *Learning & Behavior*, 49(4), 349–362. https://doi.org/10.3758/s13420-021-00488-z · **OA** · PMC8602149 — "Habit learning causes retroactive interference in a way that is reminiscent of extinction: It inhibits, but does not erase, goal-direction in a context-dependent way" (verified via Europe PMC). Contextual reinstatement, not recency.

**⚠ How to harden the negative claim before publishing it.** A negative existence claim cannot be closed by search alone. Three steps would settle it: (1) full-text search for `recen*` adjacent to `arbitrat*` in a full-text index (Europe PMC `FULL_TEXT`, Semantic Scholar, Google Scholar); (2) scan the citing literature of Lee et al. 2014 (~1,000+ citations) and Kool et al. 2017; (3) read Kool, Cushman & Gershman, *Competition and Cooperation Between Multiple Reinforcement Learning Systems* (chapter in *Goal-Directed Decision Making*) — the field's own catalogue of arbitration proposals, and the document most likely to contain an exhaustive list. **It could not be read this session (PDF unreadable) and is the highest-value outstanding check.**

The one place recency-looking machinery appears at the *between-system* level is Gläscher et al. 2010's *w*_t = *l* × *e*^−*kt* — and as established in §B.2, *t* is **trial number**, not recency of a remembered episode. Searches specifically targeting between-system recency arbitration ("arbitration between goal-directed and habitual control determined by recency of experience") returned only uncertainty-based, cost-benefit, speed/accuracy, and partial-observability accounts — no recency arbitrator.

**⇒ This is a genuine gap, and it is worth something to FMT** — but a much smaller something than the project may hope, because of §C.3.

### C.2 Priority — the term exists, and it means something else

Mattar & Daw (2018) is the "priority" paper, and its priority is *not* an arbitrator between systems:

> "We propose a normative theory predicting which memories should be accessed at each moment to optimize future decisions. Using nonlocal 'replay' of spatial locations in hippocampus as a window into memory access, we simulate a spatial navigation task in which an agent accesses memories of locations sequentially, **ordered by utility: how much extra reward would be earned due to better choices**. This prioritization balances two desiderata: **the need to evaluate imminent choices versus the gain from propagating newly encountered information to preceding locations**."
> — abstract, verified via PubMed 30349103

Priority = **gain × need**, and it orders *which memory to replay next* — a scheduling signal inside the deliberative/replay process, not a referee between deliberation and habit. The project's "priority override" is therefore not the same construct, **but the word is taken**, and taken by Daw. Using "priority" without distinguishing it from Mattar & Daw will read as either ignorance or appropriation.

### C.3 The thing that IS the closest prior art — and the project does not currently cite it

The literature's answer to "the older positive signal defeats the more recent negative one" is not an arbitration account at all. It is **episodic/sampling-based control**, and it predicts exactly that dissociation without needing FMT:

> "We provide evidence that decisions are made by **consulting memories for individual past experiences**, and that this process can be biased in favour of past choices using incidental reminders. First, in a standard rewarded choice task, we show that **a model that estimates value at decision-time using individual samples of past outcomes fits choices and decision-related neural activity better than a canonical incremental learning model.** In a second experiment, we bias this sampling process by incidentally reminding participants of individual past decisions. **The next decision after a reminder shows a strong influence of the action taken and value received on the reminded trial.**"
> — Bornstein, Khaw, Shohamy & Daw (2017), abstract, verified via PMC5490260

> "we provide evidence in favour of a more flexible approach, in which **choosers draw on memories for individual instances of relevant previous choices** and use them to predict how the current decision might turn out."
> "choices were better fit by our sampling model than by the learning model (mean log Bayes factor against temporal difference (TD) 8.8867, s.e.m. 1.0811, exceedance probability >0.99)"
> "choices following a memory probe were also **significantly influenced by the much older experience evoked by the probed ticket** (*t*(20)=3.8749, *P*=0.0009)"
> — same paper, verified verbatim

**Read that last quoted line against FMT's signature.** FMT's stated behavioural dissociation is: *an older positive experience defeats a more recent negative one, contrary to recency-weighted associative learning.* Bornstein et al. 2017 report, with a *p*-value, that **a much older experience drives the next choice when it is reinstated** — and they beat the recency-weighted TD model in formal model comparison to show it. The predicted direction is theirs, published, in a Daw-co-authored paper.

Related and equally relevant:
- **Bornstein, A. M., & Norman, K. A. (2017).** Reinstated episodic context guides sampling-based decisions for reward. *Nature Neuroscience*, 20(7), 997–1003. https://doi.org/10.1038/nn.4573 · PMID 28581478 — abstract now verified via PubMed:

> "How does experience inform decisions? **In episodic sampling, decisions are guided by a few episodic memories of past choices. This process can yield choice patterns similar to model-free reinforcement learning; however, samples can vary from trial to trial, causing decisions to vary.** Here we show that **context retrieved during episodic sampling can cause choice behavior to deviate sharply from the predictions of reinforcement learning.** Specifically, we show that, when a given memory is sampled, choices (in the present) are influenced by the properties of other decisions made in the same context as the sampled event. … **This result establishes a new avenue by which experience can guide choice** and, as such, has broad implications for the study of decisions."

**⚠ Read the second sentence against FMT.** Episodic sampling "can yield choice patterns similar to model-free reinforcement learning" — i.e. the *same behaviour*, produced by re-consulting specific episodes rather than by a cached recency-weighted value. And the third sentence says the reinstated context makes choice "**deviate sharply from the predictions of reinforcement learning**." That is FMT's dissociation — an override of what recency-weighted learning predicts, driven by reinstatement of a specific past experience — published in 2017 in *Nature Neuroscience*, and framed as establishing "a new avenue by which experience can guide choice."
- **Lengyel & Dayan (2007)**, "Hippocampal contributions to control: The third way" — episodic control proposed as a *third* controller alongside MB and MF: "We argue here for the normative appropriateness of an additional, but so far marginalized control system, associated with episodic memory… episodic control should be useful in a range of cases characterized by complexity and inferential noise, and most particularly at the very early stages of learning, long before habitization has set in." (verified verbatim, NeurIPS proceedings)
- **Gershman & Daw (2017)**, *Annu. Rev. Psychol.* 68, 101–128 — the integrative review of RL + episodic memory. **UNVERIFIED verbatim quotes** (PDF text extraction failed). Settle by reading the author copy locally with PyMuPDF.

---

## D. Known limits, criticisms, and the successor representation

### D.1 The dichotomy is contested from inside

The project's own named source concedes the problem in its abstract:

> "**Puzzlingly, signatures from these computations seem to be pervasive in the very same regions previously thought to support model-free learning.** Here, we review recent behavioral and neural evidence about these two systems, in attempt to reconcile their **enigmatic cohabitation** in the brain."
> "RPE correlates in the ventral striatum…also show model-based influences."
> "The harder part of this hunt…seems to be for **neural correlates of exclusively model-free signals, which are surprisingly sparse** given the prominence of the model-free DA accounts."
> — Doll, Simon & Daw (2012), verified via PMC3513648

And Daw et al. 2011 itself ends by undermining the clean two-system reading:

> "Contrary to expectations, the signal reflected both model-free and model-based predictions in proportions matching those that best explained choice behavior. **These results challenge the notion of a separate model-free learner and suggest a more integrated computational architecture for high-level human decision-making.**"
> — abstract, verified via PMC3077926

**⇒ Strategic consequence: the project cannot set up "the RL literature" as a unified opponent holding a clean two-system view. It does not hold one, and has not since at least 2011 — by the hand of the same authors.**

### D.2 The 2023 result (see §B.14) goes further

Feher da Silva et al. (2023) find *no* evidence of model-free prediction errors in ventral striatum under corrected analysis, and no support for cost-benefit arbitration. If that holds, the arbitration construct FMT wants to position against is itself under active challenge.

### D.3 The successor representation — verified, and it does NOT "dissolve" the dichotomy

**Citations (all verified via Crossref/OpenAlex/PubMed/PLOS/arXiv):**

Dayan, P. (1993). Improving generalization for temporal difference learning: The successor representation. *Neural Computation*, 5(4), 613–624. https://doi.org/10.1162/neco.1993.5.4.613
— *Closed access; green OA author copy at gatsby.ucl.ac.uk/~dayan/papers/sr93.pdf (a scan).*

Momennejad, I., Russek, E. M., Cheong, J. H., Botvinick, M. M., Daw, N. D., & Gershman, S. J. (2017). The successor representation in human reinforcement learning. *Nature Human Behaviour*, 1(9), 680–692. https://doi.org/10.1038/s41562-017-0180-8 · PMID 31024137 · PMCID PMC6941356 · preprint bioRxiv 10.1101/083824

Russek, E. M., Momennejad, I., Botvinick, M. M., Gershman, S. J., & Daw, N. D. (2017). Predictive representations can link model-based reinforcement learning to model-free mechanisms. *PLOS Computational Biology*, 13(9), e1005768. https://doi.org/10.1371/journal.pcbi.1005768 · PMID 28945743 · **open access CC-BY** · preprint bioRxiv 10.1101/083857

Gershman, S. J. (2018). The successor representation: Its computational logic and neural substrates. *Journal of Neuroscience*, 38(33), 7193–7200. https://doi.org/10.1523/JNEUROSCI.0151-18.2018 · PMID 30006364 · PMCID PMC6096039 · free via PMC

Carvalho, W., Tomov, M. S., de Cothi, W., Barry, C., & Gershman, S. J. (2024). Predictive representations: Building blocks of intelligence. *Neural Computation*, 36(11), 2225–2298. https://doi.org/10.1162/neco_a_01705
— *Closed at publisher; free accepted version arXiv:2402.06590. The definitive modern SR survey (74pp).*

**⚠ CORRECTION TO A LIKELY PROJECT ASSUMPTION — Dayan 1993 makes no MB/MF claim.** Verified abstract:

> "Estimation of returns over time, the focus of temporal difference (TD) algorithms, imposes particular constraints on good function approximators or representations. Appropriate generalization between states is determined by how similar their successors are, and representations should follow suit. This paper shows how TD machinery can be used to learn such representations, and illustrates, using a navigation task, the appropriately distributed nature of the result."

The vocabulary "model-based"/"model-free" does not appear. The 1993 paper is a *function-approximation/generalisation* result; the MB/MF framing was retrofitted onto the SR between 2005 and 2017. **Do not cite Dayan 1993 as the source of a "third way" claim — he did not make one.** (UNVERIFIED: whether the terms appear in the 24-page body; the OA copy is a scan. Settle with a text-layer search of the MIT Press PDF.)

**What the SR literature actually claims — verbatim:**

> "We examine an **intermediate** algorithmic family, the successor representation, which balances flexibility and efficiency by storing partially computed action values: predictions about future events. … These results suggest that the successor representation is a computational substrate for **semi-flexible** choice in humans, introducing a subtler, more cognitive notion of habit."
> — Momennejad et al. 2017, abstract

> "Although computational principles and animal behavior support this dichotomy, **at the neural level, there is little evidence supporting a clean segregation.**"
> — Russek et al. 2017, Author Summary

> "…organizing them within a broader framework for understanding **how the brain negotiates tradeoffs between efficiency and flexibility** for reinforcement learning."
> — Gershman 2018, abstract

**⇒ No verified SR paper says the SR "dissolves" the dichotomy.** The vocabulary is "intermediate," "semi-flexible," "**link**" (Russek's title verb), and "tradeoff." The SR argument is *implementational*: MB-looking behaviour can be produced by MF-style machinery on one substrate. The behavioural distinction survives; the two-separate-neural-systems reading is what's threatened. **If the project writes "the SR dissolves the dichotomy," that is a misattribution and a reviewer will catch it.** The defensible formulation is Russek's: at the neural level there is little evidence of clean segregation.

### D.4 The explicit dichotomy critiques — verified, and they do not agree with each other

Collins, A. G. E., & Cockburn, J. (2020). Beyond dichotomies in reinforcement learning. *Nature Reviews Neuroscience*, 21(10), 576–586. https://doi.org/10.1038/s41583-020-0355-6 · PMID 32873936 · PMCID PMC7800310
— ⚠ *The PMC author manuscript is titled "Beyond **simple** dichotomies in reinforcement learning" (retitled before publication). Cite the Crossref/PubMed form; body quotes pulled from PMC are from the accepted manuscript and may differ in wording.*

> "However, along with many benefits, **this dichotomous lens can distort questions, and may contribute to an unnecessarily narrow perspective on learning and decision-making.** Here, we outline some of the consequences that come from **overconfidently mapping algorithms, such as MB versus MF RL, with putative cognitive processes.**"
> — abstract, verified via PubMed

Akam, T., Costa, R., & Dayan, P. (2015). Simple plans or sophisticated habits? State, transition and learning interactions in the two-step task. *PLOS Computational Biology*, 11(12), e1004648. https://doi.org/10.1371/journal.pcbi.1004648 · **open access CC-BY**

> "We show through simulation that **under certain conditions model-free strategies can masquerade as being model-based.** … We then consider model-free reinforcement learning strategies that exploit correlations between where rewards are obtained and which actions have high expected value. **These generate behaviour that appears model-based under these, and also more sophisticated, analyses.**"
> — abstract, verified

*Note the sting: Dayan is an author both on the paper that invented the SR and on the paper showing the standard task cannot tell the two systems apart.*

Feher da Silva, C., & Hare, T. A. (2020). Humans primarily use model-based inference in the two-stage task. *Nature Human Behaviour*, 4(10), 1053–1066. https://doi.org/10.1038/s41562-020-0905-y · PMID 32632333 · preprint bioRxiv 10.1101/682922 (*title drifted across four preprint versions — cite the published title*)

> "**We also demonstrate that behaviour in the two-stage task may falsely appear to be driven by a combination of simple model-free and model-based learning if purely model-based agents form inaccurate models of the task because of misconceptions.** … Overall, we argue that humans formulate a wide variety of learning models. Consequently, **the simple dichotomy of model-free versus model-based learning is inadequate to explain behaviour in the two-stage task** and connections between reward learning, habit formation and compulsivity."
> — abstract, verified via PubMed

*Akam and Feher da Silva gut the standard task's diagnostic value from opposite directions: model-free can look model-based, and misconceived model-based can look like a mixture.*

Miller, K. J., Shenhav, A., & Ludvig, E. A. (2019). Habits without values. *Psychological Review*, 126(2), 292–311. https://doi.org/10.1037/rev0000120 · PMID 30676040 · PMCID PMC6548181

> "Here, we develop a computational model instantiating this traditional view, in which habits develop through **the direct strengthening of recently taken actions rather than through the encoding of outcomes.** … We suggest that **mapping habitual behaviors onto value-free mechanisms provides a parsimonious account** of existing behavioral and neural data."
> — abstract, verified

Miller, K. J., Ludvig, E. A., Pezzulo, G., & Shenhav, A. (2018). Realigning models of habitual and goal-directed decision-making. In *Goal-Directed Decision Making* (pp. 407–428). Elsevier/Academic Press. https://doi.org/10.1016/B978-0-12-812098-9.00018-8
— *UNVERIFIED: editor list (commonly given as Morris, Bornstein & Shenhav) — Crossref carried none. Free author PDF at kevinjmiller.org.*

> "**several lines of evidence suggest that this mapping is in need of modification and/or realignment.** First, whereas habitual and goal-directed behaviors have been shown to depend on cleanly separable neural circuitry, **recent data suggest that model-based and model-free representations in the brain are largely overlapping.** Second, **habitual behaviors need not involve representations of expected reinforcement (i.e., need not involve RL, model-free or otherwise)** … Finally, **goal-directed decisions may not reflect a single model-based algorithm but rather a continuum of 'model-basedness'.**"
> — chapter abstract, verified from author PDF

*Miller's proposed replacement is a **re-cut of the joint**, not a blurring: value-based (one goal-directed system spanning a continuum of model-basedness) vs value-free (habit).*

### D.5 The 2024–2026 wave — the framework's own architects are walking it back

Moskovitz, T., Miller, K. J., Sahani, M., & Botvinick, M. M. (2024). Understanding dual process cognition via the minimum description length principle. *PLOS Computational Biology*, 20(10), e1012383. https://doi.org/10.1371/journal.pcbi.1012383 · **open access CC-BY**

> "**Thus, while a clean separation between model-based and model-free learning can arise within MDL-C, such a division is not hardwired into the framework.**"

*This is the closest thing to a genuine dissolution: the dual-process structure is **derived** from a compression principle rather than assumed, and MB/MF becomes a special case of the parameter space rather than an architectural primitive.*

Collins, A. G. E. (**2025 or 2026 — see §F.1 discrepancy 1**). A habit and working memory model as an alternative account of human reward-based learning. *Nature Human Behaviour*, 10(2), 357–369. https://doi.org/10.1038/s41562-025-02340-0 · PMID 41249816 · PMCID PMC12932107 · **open access CC-BY 4.0** · epub 2025-11-17

> "Reanalysis and computational modelling of 7 datasets (n = 594) in diverse samples show that in this instrumental context, **reward-based learning is best explained by a combination of a fast working-memory-based process and a slower habit-like associative process, neither of which can be interpreted as a standard RL-like algorithm on its own.** My results raise important questions for the interpretation of RL algorithms as capturing a meaningful process across brain and behaviour."
> — abstract, verified

*Collins escalating her own 2020 critique from "move beyond dichotomies" to "**neither** component is RL."*

Mattar, M. G., & Daw, N. D. (2026). Planning in the brain: It's not what you think it is. *Annual Review of Neuroscience*, 49(1), 435–450. https://doi.org/10.1146/annurev-neuro-102124-015847 · PMID 41990393
— *UNVERIFIED: open-access status (Annual Reviews returned 403). Year note: online-first 2025, cite 2026 per PubMed.*

> "**We argue that advances in both neuroscience and AI suggest that planning is better understood to encompass a broader class of computations where mental simulation supports learning, often well before a decision is needed.** … **temporally abstract representations, such as grid cells, can enable planning without iterative search.** … **This view recasts the brain's planning machinery as a family of learning processes that leverage simulations to build representations and strategies, with forward search as one special case.**"
> — abstract, verified via PubMed

**⇒ This is Daw — co-author of the 2005 paper that founded the arbitration framing — reframing "model-based planning" as *not* forward search, with forward search demoted to "one special case," in 2026.** It is the single most useful citation in this entire report for FMT's positioning, and it postdates everything the project had in mind.

### D.6 The critiques do NOT converge — and that is the strategic fact

| Critique | What it actually attacks | Compatible with the dichotomy being real? |
|---|---|---|
| Akam et al. 2015; Feher da Silva & Hare 2020 | the **task** cannot measure the distinction | **Yes** — methodological only |
| SR set (Momennejad, Russek, Gershman) | the **two-neural-systems** mapping | Yes — behavioural distinction survives |
| Miller et al. 2018/2019 | the **joint is cut in the wrong place** (value-based vs value-free) | No — proposes a replacement taxonomy |
| Collins 2025 | **neither** component is RL | No |
| Moskovitz et al. 2024 | the split should be **derived, not assumed** | Partly — derives it as a special case |
| Feher da Silva et al. 2023 | the **striatal MF prediction error** is an artefact | No — attacks the empirical cornerstone |
| Mattar & Daw 2026 | **"planning" itself** is mis-specified | No |

---

## E. Closing assessment — how much is already claimed

**Blunt version: the overlap is larger than the project note assumes, and the proposed differentiator is the part that is most clearly already claimed.**

### E.1 What is already claimed, item by item

| FMT component (as recorded in `backlog.md` / `didactic-patterns.md`) | Already in the literature? | By whom |
|---|---|---|
| Two systems, one deliberative, one habitual, that can disagree | **Yes, fully** | Daw, Niv & Dayan 2005 — frames it as "how to arbitrate between the systems when they disagree" |
| Explicit deliberation overriding a habit | **Yes, fully** | the entire MB/MF arbitration literature, 2005– |
| "The implicit side then complies" (deliberation retrains the habit) | **Yes, fully** | Gershman, Markman & Otto 2014: "the model-based system trains the model-free system by replaying and simulating experience" |
| Offline replay-and-recombine over stored experience, terminating in a plan ("dreaming") | **Yes, substantially** | Dyna/replay accounts; Mattar & Daw 2018 (prioritised replay for planning) |
| An *older* experience defeating a *more recent* one | **Yes** — with a *p*-value | Bornstein, Khaw, Shohamy & Daw 2017 (*t*(20)=3.87, *P*=0.0009) |
| Behaviour deviating from what recency-weighted RL predicts, because a specific episode was reinstated | **Yes, explicitly** | Bornstein & Norman 2017: reinstated context "can cause choice behavior to **deviate sharply from the predictions of reinforcement learning**" |
| Decisions made by re-consulting *individual episodes* rather than a cached average | **Yes, fully** | Bornstein et al. 2017; Lengyel & Dayan 2007; Bornstein & Norman 2017 |
| **The proposed differentiator: the override works by RE-INSTANTIATING THE PHENOMENAL VALUE, not by retrieving an abstract state-value** | **Yes — and this is the bad news** | see E.2 |
| Recency as the *between-system arbitrator* | **No** — genuine gap, but there is a near-miss | Miller, Shenhav & Ludvig 2019 feed a *recency-weighted* habit-strength statistic into their arbiter (§C.1(i)) — close enough that a reviewer will raise it |
| Reordering / priority inversion against a survival gradient | **Not found as such** — closest neighbours are homeostatic RL (Keramati & Gutkin) and hunger-vs-planning dissociations. **UNVERIFIED**; worth a dedicated search | — |

### E.2 The differentiator is not available in the form the project states it

`didactic-patterns.md` line ~630 asserts:

> "FMT's differentiator must be step (i): that the override works by RE-INSTANTIATING THE PHENOMENAL VALUE, not by retrieving an abstract state-value… empirically approachable — does the override require re-experiencing, or does a retrieved number suffice? **Model-based RL is agnostic there; FMT is not.**"

**The claim "Model-based RL is agnostic there" is false, and the counter-citation is by Dayan himself.**

> "instrumental model-based systems that model the value of an outcome, **based on memory of its hedonic experience, may need to retaste or re-experience outcome again after revaluation in order to update model**."
> — Dayan, P., & Berridge, K. C. (2014). Model-based and model-free Pavlovian reward learning: revaluation, revision, and revelation. *Cognitive, Affective, & Behavioral Neuroscience*, 14(2), 473–492. https://doi.org/10.3758/s13415-014-0277-8 · PMID 24647659 — *Figure 1 caption, verified via PubMed listing*

That is the project's own proposed experiment — *does the override require re-experiencing, or does a number suffice?* — posed as a design consideration in 2014, by the co-author of the framework FMT is positioning against, in a paper whose whole subject is **model-based evaluation that runs on remembered hedonic experience**. The distinction between re-experiencing and retrieving a value is not an FMT innovation; it is a known axis in the Pavlovian revaluation literature.

And outside RL it is older still:
- **Damasio 1996** — somatic markers, where anticipated option-outcome scenarios are marked by re-activated body/emotion states, both covertly and via "the conscious 'qualifying' of certain option-outcome scenarios as dangerous or advantageous" (abstract, verified PMID 8941953).
- **Gilbert & Wilson 2007** — "humans can predict the hedonic consequences of events they've never experienced by **simulating those events in their minds**. Scientists are beginning to understand how the brain simulates future events, how it uses those simulations to **predict an event's hedonic consequences**" (abstract, verified PMID 17823345).
- **Kahneman, Wakker & Sarin 1997** — the decision-utility vs experienced-utility (instant / remembered) distinction, which is precisely "abstract value vs the felt thing," formalised in 1997.
- **Peters & Büchel 2010** — imagining specific future episodes measurably changes choice (delay discounting), with the neural mechanism identified.

⇒ **A reviewer with this literature in hand answers the differentiator in one line, exactly as the project feared — but they answer the differentiator, not just the setup.**

### E.3 Where a genuine differentiator could still lie

Three candidates survive, in descending order of strength. None is currently written down in defensible form.

**i. Recency as the between-system arbitrator (§C.1).** No verified account makes recency the referee. But note the trap: FMT does not actually need recency to *arbitrate* — its story is that a *re-simulated older* value beats a *more recent* one, and Bornstein et al. 2017 already produce that behaviour from episodic sampling with no arbitration at all. **So this gap is only worth claiming if FMT predicts something Bornstein-style sampling does not.** State that difference or drop the claim.

**ii. The reordering / priority-inversion signature.** `didactic-patterns.md` already judges this the stronger signature — "deferral of the MORE SURVIVAL-CRITICAL item (food) for the evolutionarily useless one (the ride)… a priority inversion against a survival gradient." Nothing matching it surfaced in this verification. It is the least-occupied ground FMT holds here. **UNVERIFIED — it deserves its own literature check** (homeostatic RL, sequence/order planning, motivational conflict) before being claimed.

**iii. Necessity, not sufficiency, of re-instantiation.** Dayan & Berridge say re-experiencing *may be needed* to update a model. FMT would have to say something stronger and falsifiable — e.g. that the override *cannot* occur on a retrieved scalar, in humans or in an artificial system, and specify what fails when re-instantiation is blocked. That is a real claim and it is not in the verified literature. It is also a much narrower claim than "the override works by re-instantiating phenomenal value."

### E.4 The one piece of genuinely good news — and it is bigger than expected

The opponent is **not** a settled field, and it is being dismantled from the inside by the very people who built it.

- **Sixteen accounts and at least nine mutually incompatible arbitrating variables are in print (§B.13)**, with no convergence over twenty-one years; the seven critiques do not converge either (§D.6).
- **Dolan & Dayan 2013, in *Neuron*: "Various suggestions have been made for how arbitration should proceed, but this is an area where much more work is necessary."**
- Kool, Cushman & Gershman 2016: the hallmark task for dissociating the two strategies "**do[es] not embody such a trade-off**" — i.e. the canonical evidence base does not contain the thing the theories are about.
- Otto et al. 2013 (*Psych. Sci.*): "**The factors governing which system controls behavior—and under what circumstances—are still unclear.**"
- Daw & Dayan called their own integration story "**more preview than review**" (2014).
- Daw et al. 2011 concluded its own data "**challenge the notion of a separate model-free learner**."
- Doll et al. 2012 called the two systems' coexistence "**enigmatic**" and noted exclusively-model-free neural correlates are "**surprisingly sparse**."
- Akam, Costa & **Dayan** 2015 showed model-free strategies "**can masquerade as being model-based**" in the standard task.
- Feher da Silva & Hare 2020: "**the simple dichotomy of model-free versus model-based learning is inadequate.**"
- Collins & Cockburn 2020 (*Nat. Rev. Neurosci.*): the dichotomous lens "**can distort questions.**"
- Feher da Silva et al. 2023: no model-free striatal prediction errors; cost-benefit arbitration refuted.
- Collins 2025: **neither** component is a standard RL algorithm.
- **Mattar & Daw 2026: "planning" is recast as a family of learning processes "with forward search as one special case."**

**FMT should therefore position against the *unsettledness*, not against a monolith.** The defensible sentence is roughly: *the field posits an arbitration between deliberative and habitual control but has not agreed what arbitrates; its diagnostic task cannot cleanly separate the two; its striatal evidence for the model-free half is contested; and its own architects have recently recast planning itself.* Every clause there is citable from §B and §D.

**What is NOT defensible:** "this is not model-based RL because we re-instantiate phenomenal value" (§E.2), or "the SR dissolves the dichotomy" (§D.3), or any framing that presents the RL literature as holding a clean, confident two-system view.

### E.5 Concrete instructions for the drafting session

1. Cite the four verified foundational papers (§A.1) as the *setup*, never as the opponent.
2. Cite **Gershman, Markman & Otto 2014** and **Bornstein et al. 2017** explicitly and early — they are the nearest prior art, and pretending they are absent is the fastest route to a desk rejection.
3. **Delete or rewrite the sentence "Model-based RL is agnostic there; FMT is not"** in `.claude/knowledge/didactic-patterns.md` (~line 630) and the parallel text in `backlog.md` (AIW-202 block). It is refuted by Dayan & Berridge 2014. ⇒ **This is a required edit, not a suggestion** — it is currently a false claim sitting in a knowledge file that loads every session.
4. **Do not attribute a "third way / dissolves the dichotomy" claim to Dayan 1993.** The 1993 SR paper makes no MB/MF claim at all (§D.3).
5. Fix the **Feher da Silva et al. 2023** author list if it is filed anywhere with Montague — the authors are Feher da Silva, Lombardi, Edelson & Hare.
6. Lead the positioning paragraph with **Mattar & Daw 2026** — it is the most recent, most authoritative, and most favourable framing available, and it postdates everything the project had in mind.
7. Run the outstanding checks listed in §F.

---

## F. Outstanding — what remains UNVERIFIED and what would settle it

| Item | Status | What would settle it |
|---|---|---|
| **Kool, Cushman & Gershman, *Competition and Cooperation Between Multiple Reinforcement Learning Systems* (chapter)** — the field's own catalogue of arbitration proposals | UNVERIFIED (PDF unreadable) | Text-extract `gershmanlab.com/pubs/KoolCushmanGershman_CompCoop.pdf`. **Highest-value outstanding check** — it is the document most likely to contain a recency-based proposal if one exists (§C.1) |
| Gershman & Daw 2017 verbatim internal quotes | UNVERIFIED (PDF text extraction failed) | Read `gershmanlab.com/pubs/GershmanDaw17.pdf` locally with PyMuPDF/`fitz` |
| Body text of Kool, Gershman & Cushman 2017; Boureau et al. 2015; Logan 1988 | UNVERIFIED (paywalled / PDF unreadable) | Publisher or author PDFs through a text extractor. Abstracts are verified |
| All body-text quotes marked *medium confidence* (Lee 2014, Keramati 2011, Pezzulo 2013, Miller 2019, Mattar & Daw 2018, Dolan & Dayan 2013, Collins & Cockburn 2020, Collins 2025/26) | MEDIUM — automated full-text reads, not character-diffed against source | String-match each against the PMC HTML/PDF **before** any goes into a manuscript |
| Keramati symbol names (VPI, τ, ρ̄) | Reconstructed from prose — PLOS renders equations as images | Read the PDF |
| Drummond & Niv 2020, *Current Biology*, "Model-based decision making and model-free learning" (reported 30(15):R860–R865) | UNVERIFIED — search snippet only, publisher 403 | Crossref DOI resolution, or the Niv-lab copy at nivlab.princeton.edu |
| Geerts, Gershman, Burgess & Stachenfeld (2024), *Psychological Review*, probabilistic SR | UNVERIFIED — search snippet only | Crossref/PubMed lookup |

### F.1 Two discrepancies — flagged, NOT silently reconciled

1. **Collins (single-author *Nature Human Behaviour* paper) — year conflict between the two verification passes.** Both agree on volume/issue/pages/DOI/PMID: *Nat. Hum. Behav.* **10(2), 357–369**, https://doi.org/10.1038/s41562-025-02340-0, PMID 41249816, PMCID PMC12932107, **epub 2025-11-17**. One pass dated it **2025** (epub year), the other **2026** (issue year). Both are defensible under different conventions; the project must pick one and apply it consistently. **What settles it:** the year printed on the final issue PDF. Cited as "2025/2026" throughout this file rather than guessing.

2. **A DOI collision that indicates an error.** One pass reported Perez & Dickinson (2020), *Psychological Review* 127(6), 945–971 with DOI `10.1037/rev0000120` — **but that DOI belongs to Miller, Shenhav & Ludvig (2019), "Habits without values."** The Perez & Dickinson entry is therefore wrong in at least its DOI and is marked **UNVERIFIED in full**; it was read only from a search summary. **What settles it:** PubMed PMID 32406713 / Crossref resolution, plus the OA preprint bioRxiv 10.1101/807800. Do not cite Perez & Dickinson from this file.
| Lengyel & Dayan 2007 exact page range | UNVERIFIED | NeurIPS proceedings PDF front matter |
| Whether "model-based"/"model-free" appear in the **body** of Dayan 1993 | UNVERIFIED (abstract confirmed clean) | Text-layer search of the MIT Press PDF (the OA copy is a scan) |
| Editors of *Goal-Directed Decision Making* (Miller et al. 2018 chapter) | UNVERIFIED | Elsevier book landing page or printed front matter |
| Open-access status of Mattar & Daw 2026 | UNVERIFIED (Annual Reviews 403) | Annual Reviews article page or OpenAlex |
| Collins & Cockburn 2020 and Collins 2025 **body** quotes | MEDIUM confidence — fragments only; C&C fragments are from the retitled *author manuscript* | Pull full sentences from PMC7800310 / PMC12932107 before quoting in a publication |
| Geerts, Gershman, Burgess & Stachenfeld (2024), "A probabilistic successor representation for context-dependent prediction," *Psychological Review* | UNVERIFIED — surfaced in a search snippet only | Crossref/PubMed lookup |
| **The reordering / priority-inversion signature** (§E.3.ii) — FMT's least-occupied ground | UNVERIFIED — no dedicated search run | A targeted check against homeostatic RL (Keramati & Gutkin), sequence/order planning, and motivational-conflict literatures. **Recommend this as the next verification task.** |

**Sources blocked during this session** (403 / auth redirect), so nothing was read directly at these publishers: nature.com, link.springer.com, royalsocietypublishing.org, MIT Press Direct, ScienceDirect, Annual Reviews. Verification routed via PubMed, PMC, PLOS, arXiv, bioRxiv, NeurIPS proceedings, Crossref, OpenAlex, and Semantic Scholar. No Wikipedia, blog, or ResearchGate content was used as a source of fact.

