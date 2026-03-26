# RIM Section 3.1 — Motivation Component Revision

**Purpose**: Replace current lines 103-105 of `paper/intelligence/paper.md` with this text.
**Status**: Draft for review.

---

## Current text (lines 103-105):

> 3. **Motivation**: The sustained drive to engage with the world in ways that produce learning. Two sub-components are distinguished:
>    - *Wissensdrang* (thirst for knowledge): The intrinsic drive to understand, to learn, to make sense of the world. This aligns with the intrinsic motivation construct of Self-Determination Theory (Deci & Ryan, 2000) and with what Cacioppo et al. (1996) called "need for cognition."
>    - *Handlungsdrang* (urge to act): The drive to apply knowledge, to experiment, to engage actively with one's environment. This is partly genetically predisposed and partly shaped by conditioning and learning.

---

## Proposed replacement:

3. **Motivation**: The sustained drive to engage with the world in ways that produce learning. At the intuitive level, two aspects are readily distinguished: *Wissensdrang* (thirst for knowledge) — the drive to understand, to learn, to make sense of the world — and *Handlungsdrang* (urge to act) — the drive to apply knowledge, to experiment, to explore. These correspond to familiar constructs in the personality-intelligence literature: Wissensdrang maps closely to Cacioppo and Petty's (1982) need for cognition (NFC) and Goff and Ackerman's (1992) typical intellectual engagement (TIE); Handlungsdrang maps to the exploration and risk-taking dispositions that Wittmann and Hattrup (2004) showed mediate intelligence-performance relationships by generating new learning opportunities.

However, the relationship between these intuitive categories and their empirical proxies is more complex than a simple mapping suggests — and understanding why reveals something important about the motivation construct itself. NFC and TIE, despite being highly correlated (r ≈ .78–.87; von Stumm & Ackerman, 2013), predict different intelligence facets: NFC correlates primarily with fluid reasoning (Gf), while TIE correlates primarily with crystallized knowledge (Gc). Need for achievement, openness to experience, and sensation seeking show yet other patterns (Ackerman, 2018). The standard interpretation is that these represent genuinely distinct motivational constructs. This paper proposes an alternative: they are *measurement-context projections* of a single underlying function.

The argument, which draws on the architectural framework developed in Gruber (2026), is as follows. Motivation — the evaluative process that assigns salience, directs attention, and sustains engagement — is a function of the brain's explicit processing: the self-model that consciously evaluates situations, weighs options, and decides where to invest effort. This is a unified computational function, not a family of independent traits. It *appears* fragmented in the empirical literature because different measurement instruments observe this function in different contexts. NFC measures motivation-as-observed-during-novel-reasoning, which naturally co-varies with the processing substrate that novel reasoning depends on (Gf). TIE measures motivation-as-observed-during-habitual-knowledge-seeking, which naturally co-varies with the accumulated knowledge store (Gc). Risk-taking measures motivation-as-observed-during-exploration, which naturally generates new learning opportunities. The constructs diverge not because the underlying motivation differs, but because the measurement context determines which intelligence facet the observation co-activates.

This interpretation gains support from an unexpected direction: artificial intelligence. Current large language models possess vast knowledge and high processing performance, yet exhibit no motivation whatsoever — no curiosity, no self-directed learning, no drive to explore gaps in their understanding. The recursive model predicts that this absence should prevent the self-sustaining developmental loop that characterizes human intelligence, and this is precisely what is observed (Section 5). Critically, the *kind* of motivation that AI lacks is not NFC, or TIE, or need for achievement specifically — it is the entire evaluative function that these constructs partially measure. No amount of engineering NFC-like behavior (preference for complex problems) or TIE-like behavior (habitual engagement with information) would produce genuine motivation without the underlying explicit self-model that generates it. The AI case thus supports the unity claim: what is missing in artificial systems is not one of psychology's motivation constructs but the single computational function from which all of them derive.

This reinterpretation has a direct precedent in Wittmann's own Brunswik symmetry framework (Wittmann, 1988; Wittmann & Klumb, 2006): observed correlations are bounded by the symmetry between predictor and criterion bandwidth. Narrow motivation measures (a single questionnaire scale) correlated with broad intelligence criteria (a full test battery) will produce attenuated and criterion-specific correlations — not because motivation is weakly related to intelligence, but because the measurement design is asymmetric. Properly aggregated motivation measures, assessed across multiple contexts and occasions, should produce substantially higher and more uniform correlations with intelligence — a testable prediction of the present framework.

The recursive model therefore treats Motivation as a single component with two functional expressions — the epistemic (Wissensdrang: directing engagement toward understanding) and the agentic (Handlungsdrang: directing engagement toward action and exploration) — while maintaining that these expressions reflect a unified evaluative process rather than structurally independent traits. What the personality-intelligence literature has catalogued as distinct constructs (NFC, TIE, openness, need for achievement, risk-taking) are, in this view, context-specific behavioral signatures of the same underlying function, measured at different points of its expression.

---

## New references needed:

- Cacioppo, J. T., & Petty, R. E. (1982). The need for cognition. *Journal of Personality and Social Psychology*, 42, 116–131.
- Goff, M., & Ackerman, P. L. (1992). Personality-intelligence relations: Assessment of typical intellectual engagement. *Journal of Educational Psychology*, 84, 537–552.
- Ackerman, P. L. (2018). The search for personality-intelligence relations: Methodological and conceptual issues. *Journal of Intelligence*, 6(1), 2.
- Wittmann, W. W. (1988). Multivariate reliability theory. In J. R. Nesselroade & R. B. Cattell (Eds.), *Handbook of multivariate experimental psychology* (2nd ed., pp. 505–560). Plenum.
- Wittmann, W. W., & Klumb, P. L. (2006). How to fool yourself with experiments in testing theories in psychological research. In R. R. Bootzin & P. E. McKnight (Eds.), *Strengthening research methodology* (pp. 185–211). APA.

(Wittmann & Hattrup 2004, von Stumm & Ackerman 2013, Deci & Ryan 2000 already cited in current paper.)

---

## Notes on integration:

1. **Section 3.4 (Relation to Existing Work)** — the existing paragraph on Wittmann & Süß (1999) and Wittmann & Hattrup (2004) can stay. Add a sentence connecting to the Brunswik symmetry argument made here: "The Brunswik symmetry framework also explains why..." — but avoid repeating the full argument.

2. **Section 5 (AI Implication)** — the AI paragraph added above provides a forward reference to Section 5. Section 5 itself should add a sentence back-referencing the unity argument: "As argued in Section 3.1, the motivation absent from AI systems is not any single construct from the personality-intelligence literature but the unified evaluative function from which all such constructs derive."

3. **Section 7 (Discussion)** — a new subsection on testable predictions should include the aggregation prediction: properly aggregated motivation measures × longitudinal design → stronger M-intelligence correlations. This is AIW-32.

4. **The FMT companion paper reference** (Gruber, 2026) is already cited throughout. The phrase "the architectural framework developed in Gruber (2026)" is sufficient — the reader can follow the reference for the full explicit/implicit processing argument. Don't dump FMT content into the RIM paper.
