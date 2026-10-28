# RIM adversarial review — `paper/intelligence/paper.md` (+ mirrored `.tex`)

Reviewed 2026-08-24. Source of truth: `paper.md`. Every defect below was checked against the
hand-maintained `paper.tex` as well — **all of them are present in both files**, so every repair is a
two-file repair. All line numbers are `paper/intelligence/paper.md`.

Read first (so nothing here is a re-discovery): `docs/pending-rim-s290-remaining.md`,
`docs/pending-rim-verification-debt.md`, `docs/pending-s289-rim-session.md`,
`docs/s292-citation-verification.md`. The S291/S292 repairs all hold — Jussim & Harber, the Wechsler
1944 quote, the NFC/TIE dissociation, the Rosenthal md↔tex drift, and the Coding/Bratsberg
constraints are correctly carried. What follows is new.

---

## Verdict

**Six citations already sitting in the manuscript say something their source does not, and every one
of them fails in the same direction — toward more support than exists.** The worst is §3.3, which
presents
Andrzejewski et al. (2024) as reporting a "striking" dissociation that is "directly predicted by the
recursive framework"; the source explicitly reports that change as **not statistically significant**
(R² .908 → .892) and interprets it as *increasing ability differentiation*, not as intelligence
declining. Heckman (2006) is credited with an age-27 vs age-7 comparison that does not occur anywhere
in the article. Wicherts et al. (2004) is described as a finding about "the Wechsler scales" when it
is a five-battery, three-country study of which one battery is Wechsler — a narrowing that happens to
make it fit §7.3's WISC argument better than the source licenses. §7.2's prediction 1 claims existing
support from two studies (von Stumm et al. 2011, Murayama et al. 2013), neither of which has an adult
outcome or a childhood-to-adult design. And Bratsberg & Rogeberg (2018) is credited with "ruling out
genetic explanations" where the authors claim only to rule out changing between-family composition.
This is not a formatting
problem — it is the same failure mode `docs/pending-rim-verification-debt.md` says generalises
("verify citations that are already in the manuscript, not only the ones being added"), and it
survives every gate the project owns, because the gates check that keys resolve to real works and
never that the sentence matches the source. RIM is already public as Zenodo v3, so these are out in
the world. Separately and independently: §2.5 attributes eight intelligences to Gardner (1983), which
proposed seven — the single fastest credibility hit in the paper.

---

## Findings

### 1. §3.3 — a non-significant trend is reported as a finding, and the source's own interpretation is inverted. **CONFIRMED**

> "Even more striking is the dissociation reported by Andrzejewski et al. (2024): IQ scores rose
> while *g* — the general factor extracted from the correlation matrix — simultaneously declined.
> This dissociation is inexplicable under static-trait models but directly predicted by the recursive
> framework. Teaching to the test inflates Performance scores (narrow task-specific knowledge)
> without engaging the recursive loop. The result is higher scores on standardized measures with
> lower capacity for the self-directed, generalizable learning that the recursive loop produces. IQ
> goes up; intelligence, properly understood, goes down."

`paper.md:145` (`paper.tex:180`)

Verified against the primary (PMC11676032, open access, abstract read verbatim). Andrzejewski et al.
(2024), *J. Intelligence* 12(12), 130, report:

> "our analyses revealed positive Flynn effects across all domains of the IQ test (Cohen's *d* from
> 0.21 to 0.91) but a trend toward decreasing strength in the positive manifold of intelligence (R²
> from .908 to .892), **though these changes were not statistically significant**."

Three separate defects in one paragraph:

- **The dissociation is non-significant.** The paper calls it "the dissociation reported by" and
  "even more striking" than the Flynn reversal. The source calls it a non-significant trend. The
  magnitude is a drop of 0.016 in R² — 1.8% relative.
- **It is a manifold-strength change, not a decline in *g*.** "the general factor … simultaneously
  declined" reads as a decline in general ability. What weakened is the *inter-correlation* among
  subtests. Every domain gained.
- **The source's interpretation is the opposite of the paper's.** Andrzejewski et al. conclude the
  pattern reflects "increasing ability differentiation and specialization in the general population."
  The paper converts that into "lower capacity for the self-directed, generalizable learning" and
  "intelligence, properly understood, goes down." Nothing about teaching to the test appears in the
  source.

**Minimal repair — and it is cheap, because the substantial version of this result exists and the
paper already cites it.** Oberleiter et al. (2024) — same group, same country, longer window
(2005–2024), N = 1267 — report "**substantial** declines in single-factor analysis-based *g*
assessments (ΔR² range: −.037 to −.066)" alongside "meaningful test score increases in all domains"
(verbatim, publisher abstract). That is two to four times the size of Andrzejewski's non-significant
−.016 and it is not hedged. Move the empirical weight to Oberleiter, state the result as *manifold
weakening / increasing ability differentiation*, and drop "even more striking", "directly predicted",
the teaching-to-the-test mechanism and the "IQ goes up; intelligence goes down" line. If Andrzejewski
is kept, label the trend non-significant — which removes its use as support, correctly.

### 2. §7.3 — Wicherts et al. (2004) is not a finding about "the Wechsler scales". **CONFIRMED**

> "Subtest score changes cannot be read as changes in a latent ability without invariance testing:
> Wicherts et al. (2004) showed that **the Wechsler scales** are not measurement invariant over time,
> and that the observed pattern of subtest gains is not what a change in common-factor means would
> produce."

`paper.md:371` (`paper.tex:399`)

Wicherts et al. (2004) tested measurement invariance across cohorts in **five datasets from three
countries**: the Dutch WAIS (1967–1999), the Dutch Differential Aptitude Test (1984–1995), the Dutch
children's battery RAKIT (1982–1993), a reanalysis of Must, Must & Raudik's Estonian data, and a
reanalysis of Teasdale & Owen's Danish conscription data. **Exactly one of the five is a Wechsler
scale**, and it is the adult scale, not the WISC on which §7.3's whole partition rests. The paper
converts a broad cross-battery result into a Wechsler-specific one — a narrowing that makes the
citation fit the argument better than the source licenses, and one that a reviewer checking the
methodological constraint will look up first because the constraint is load-bearing for the section.
Flynn and Weiss themselves state it correctly at their p. 219: "Wicherts et al. (2004) have shown
that IQ gains from one time to another are **often** not factor-invariant."

**Minimal repair.** "Wicherts et al. (2004) showed that cohort gains on five intelligence batteries,
including the Dutch WAIS, are often not measurement invariant, and that the observed pattern of
subtest gains is not what a change in common-factor means would produce."

**Withdrawn, and recorded so nobody re-raises it.** I initially read the following sentence —
"A secular change not carried by the common factor is what Oberleiter et al. (2024) report"
(`paper.md:371`) — as reversed, on the grounds that Oberleiter's title advertises
*measurement-invariant* score changes. **That suspicion is wrong and the paper is right.** The
publisher abstract, obtained verbatim, reads: "we examined performance changes in two
population-representative Germanophone samples (N = 1267) across six measurement-invariant
intelligence subscales from 2005 to 2024. Our analyses revealed substantial declines in single-factor
analysis-based g assessments (ΔR² range: −.037 to −.066)… **Despite this decrease in the positive
manifold strength, we observed meaningful test score increases in all domains** (d range: 0.18 to
1.24)." "Measurement-invariant" there describes the subscales as a design precondition; the finding
is gains alongside a weakening manifold, which is fairly paraphrased as a change not carried by the
common factor. The only residual issue is presentational: placing Oberleiter directly after the
Wicherts non-invariance sentence invites the reader to take it as a second non-invariance result,
which it is not. One clause separating the two claims would fix it.

### 3. §6.4 — the Heckman age comparison does not exist in the cited article. **CONFIRMED**

> "Heckman's (2006) analysis of early childhood interventions, including the Perry Preschool Project,
> shows returns that grow over time — larger effects at age 27 than at age 7 — not because initial
> cognitive gains persist (they often fade), but because motivational and self-regulatory gains
> compound through subsequent learning."

`paper.md:289` (`paper.tex:318`)

Primary source read in full (Heckman 2006, *Science* 312(5782), 1900–1902). **The strings "27" and
"7" as ages do not occur in the article.** The comparison Heckman actually draws is age 10 (Perry
treatment and control equal on IQ) versus age 40 (graduation, earnings, home ownership, welfare,
arrests — citing Schweinhart et al. 2005, *Lifetime Effects… Through Age 40*). The "age 27" figure
looks conflated with the earlier Schweinhart, Barnes & Weikart (1993) *…Through Age 27* report,
which is not the cited work. The general gloss — cognitive gains fade, non-cognitive gains persist —
is a fair reading of Heckman; the specific numbers are not his.

**Minimal repair.** Replace with "equal IQ by age 10 but large differences in life outcomes at
age 40", or drop the numbers and keep the qualitative claim.

### 4. §7.2 prediction 1 — neither supporting citation supports the prediction. **CONFIRMED**

> "**Motivation predicts long-term intellectual development beyond IQ**: Measures of intellectual
> curiosity and learning drive, assessed **in childhood**, should predict **adult** intellectual
> achievement (education, creative output, problem-solving ability) beyond what childhood IQ
> predicts. Existing evidence supports this (von Stumm et al., 2011; Murayama et al., 2013)…"

`paper.md:333` (`paper.tex:369`)

- **von Stumm, Hell & Chamorro-Premuzic (2011)** (primary read): a meta-analysis of **academic
  performance**, built on a meta-analytically derived correlation matrix from predominantly
  concurrent/cross-sectional student samples (GPA composites). No childhood-to-adult longitudinal
  design and no adult-achievement outcome. The same source is also glossed at `paper.md:153` as
  showing that curious individuals "develop greater knowledge and skill **over time**" — also not
  what the meta-analysis tests.
- **Murayama et al. (2013)**: the PALMA study, six annual waves, Grade 5 → Grade 9/10, mean baseline
  age 11.7, outcome = growth in **mathematics achievement**. Participants never reach adulthood.

So the one prediction the paper claims already has evidence has none of the stated shape.

**Minimal repair.** Either restate the prediction over school-age outcomes (which both sources do
support), or keep the adult framing and say the evidence is absent — a genuinely open prediction is
stronger here than a supported-looking one that collapses on inspection.

### 5. §2.5 — Gardner (1983) proposed seven intelligences, not eight. **CONFIRMED**

> "Gardner (1983) proposed eight (later nine) relatively independent intelligences: linguistic,
> logical-mathematical, spatial, musical, bodily-kinesthetic, interpersonal, intrapersonal,
> naturalist, and (tentatively) existential."

`paper.md:77` (`paper.tex:102`)

*Frames of Mind* (1983) proposed **seven**; naturalist was added in *Intelligence Reframed* (1999),
making eight, with existential floated in the same book as a tentative ninth ("8½"). The sentence
attaches the count eight — and the naturalist item — to the 1983 book. This is the single fastest
credibility hit in the paper: it is the one fact in §2 that every reader of *Journal of Intelligence*
already knows, it sits in a section whose whole job is to show the author has read the field, and it
is checkable in five seconds.

**Minimal repair.** "Gardner (1983) proposed seven relatively independent intelligences: linguistic,
logical-mathematical, spatial, musical, bodily-kinesthetic, interpersonal and intrapersonal; a
naturalist intelligence was added in 1999, with existential floated tentatively as a ninth."

### 5b. §3.3 — Bratsberg & Rogeberg does not "rule out genetic explanations". **CONFIRMED**

> "Bratsberg and Rogeberg (2018), analyzing Norwegian military conscript data, demonstrated that IQ
> scores rose and then declined across birth cohorts *within families* — **ruling out genetic
> explanations and confirming environmental causation**."

`paper.md:141` (`paper.tex:176`)

Primary read (PNAS 115(26), open access). The authors' own scope is narrower in both breadth and
certainty. Significance statement: "…reflect environmental factors and not **changing composition of
parents**, which in turn rules out several prominent hypotheses for retrograde Flynn effects."
Abstract: "…finds **no evidence for** prominent causal hypotheses of the decline implicating genes
**and environmental factors that vary between, but not within, families**."

A within-family design eliminates explanations that work through *which kinds of families exist* in
each cohort — some genetic (dysgenic differential fertility), some purely demographic (immigration).
It does not eliminate genetic explanations as a class, and "no evidence for" is elimination of
alternatives, not confirmation of a mechanism. The paper's title does say "environmentally caused",
which is why this is a stretch rather than a fabrication — but "ruling out genetic explanations" is
the single sentence in §3 most likely to draw a hostile reviewer in an intelligence journal, and it
is not needed: the recursive model's argument runs on the within-family reversal itself.

**Minimal repair.** "…rules out explanations resting on changing between-family composition,
including the prominent genetic ones, and is consistent with environmental causation."

### 6. §5.2 — "Current LLMs cannot do this" is a barrier claim and is false as written. **CONFIRMED**

> "A human learner who discovers a more effective reasoning strategy can immediately apply it to
> subsequent problems within the same cognitive session — the operational knowledge becomes part of
> the active processing. **Current LLMs cannot do this.** External scaffolding systems can modify the
> instructions given to an LLM … but such modifications do not integrate into the system's
> processing…"

`paper.md:229` (`paper.tex:257`)

In-context learning is exactly the capability being denied: a strategy derived at turn *n* of a
session conditions the model's outputs at turn *n+k* of the same context, with no external
scaffolding and no restart. The paragraph then argues against a different thing — externally
modified instructions — as if that were the only route. The paper is otherwise scrupulous about the
price-not-barrier form (§5.1 explicitly retracts "artificial systems have no motivation at all";
§5.3 pre-concedes its own conjecture is refutable). This sentence is the one place it reverts.

**Minimal repair — the licensed price form.** "In current LLMs a strategy discovered mid-session
persists only for the life of that context: it conditions later turns but is not written back into
the system, so it does not survive the session, and the next session starts from the same place as
the last. The human case is one where the strategy is retained; the machine case is one where it is
rented." Same for `paper.md:223`, "Their capability is static, **entirely determined by training**"
— in-context adaptation and tool use are counter-examples; "static across sessions" is the defensible
form.

### 7. §7.2 prediction 5 contradicts §5.1–§5.3 and is unfalsifiable as written. **CONFIRMED**

> "**AI systems will not exhibit self-directed intellectual development until they have functional
> motivation analogues**: This is a prediction about the future trajectory of AI development. It
> implies that the path to artificial general intelligence runs through motivation engineering, not
> merely through scaling Knowledge and Performance."

`paper.md:341` (`paper.tex:373`)

Against §5.3 (`paper.md:239`): "**What the recursive model does claim about artificial systems is the
narrower thing stated in Section 5.2**: that supplying an exploration drive is not the same as
supplying the M component." And §5.2 (`paper.md:225`) states the sharp, buildable version: supplying
an intrinsic drive to a system that *does* have persistent state and self-modification "will not, by
itself, produce a self-sustaining developmental trajectory."

So §5.2 predicts motivation engineering is **not sufficient**; prediction 5 says the path to AGI
"runs through motivation engineering". §5.3 says the narrow claim is the model's only AI claim; §7.2
lists the broad one. Prediction 5 also has no operationalisation, no criterion, and no independent
definition of "functional motivation analogue" — any system that fails confirms it, any that succeeds
is said to have acquired one. This is precisely the failure `prediction-framing.md` records ("AI
predictions were metaphysical, not empirical"; "insufficient operationalization… 'too general' was
accurate"). Prediction 5 looks like the pre-revision text that §5 was rewritten to replace and the
list was not updated with it.

**Minimal repair.** Delete prediction 5 and replace it with the §5.2 experiment, stated with its
disconfirmer: a persistent-state, self-modifying agent given an intrinsic drive should explore and
improve on its explored distribution without open-ended cross-domain compounding; open-ended
compounding disconfirms the model's claim about M.

### 8. §7.3 — half the disconfirmation criterion has already been satisfied by the data used to build the partition. **CONFIRMED**

> "The prediction is disconfirmed if simulation-loaded and retrieval-loaded subtests show
> statistically indistinguishable secular trajectories once the classification is fixed in advance,
> or if the reversal falls on retrieval-loaded content while simulation-loaded scores hold."

`paper.md:373` (`paper.tex:401`)

The section's own second paragraph (`paper.md:359`) has just shown the two classes' secular
trajectories differ, using the Flynn & Weiss table the partition was built from. The classification
was not fixed in advance of that table. So the first limb cannot disconfirm anything — it was
already passed by the evidence that motivated it. Only the second limb (the reversal) is genuinely
forward-looking, and the section elsewhere says so ("Three predictions follow, none of them yet
tested against a classification fixed in advance"). The disconfirmation sentence contradicts that
correct statement.

**Minimal repair.** Drop the first limb, or restate it over a *held-out* record (a different test
family, a different country's standardisation series) where the fixed-in-advance condition can
actually be met.

### 9. Abstract asserts as established what §7.2 designates an open, disconfirmable prediction. **CONFIRMED**

Abstract (`paper.md:23`, `paper.tex:48`):
> "— an interpretation **supported by** Brunswik symmetry analysis, which predicts that the modest
> motivation-intelligence correlations reported in the literature **are** measurement artifacts
> rather than evidence of weak association."

§7.2 prediction 7 (`paper.md:345`) flatly asserts the same thing mid-paragraph — "The modest
correlations **are**, in large part, measurement artifacts" — and then, two paragraphs later
(`paper.md:347`), makes it the thing at risk: "If motivation aggregated symmetrically over that
design … still correlates with intelligence at approximately the *r* ≈ .30 currently reported, **then
the attenuation account is wrong**."

An untested prediction with a stated disconfirmer is the paper's strongest asset here; the abstract
spends it by calling it support. §3.1 already says the right thing ("The unity claim has to be
carried by evidence that can come apart"). The abstract and the two flat assertions in P7 are what
disagree.

**Minimal repair.** Abstract: "— an interpretation the framework puts at risk: Brunswik symmetry
analysis implies that the modest motivation-intelligence correlations may be measurement artifacts,
and §7.2 states the aggregation result that would show they are not." Delete the flat assertion at
`paper.md:345`.

### 10. §7.2 prediction 7 — the parenthetical names five sources while claiming six. **CONFIRMED**

> "…demonstrated that for any observed effect size in psychological research, there are **six**
> sources of underestimation (range restriction, unreliability of both treatment and criterion, lack
> of construct symmetry, and negative sampling error) against only two sources of overestimation
> (range enhancement and positive sampling error)."

`paper.md:345` (`paper.tex:375`)

Verified twice: against the primary chapter (Wittmann & Klumb 2006, pp. 185–211, full text read —
"There are six dangers of underestimating a true effect and only two dangers of overestimating it",
Figure 10.6), and against the project's own summary of Wittmann's materials
(`docs/wittmann-materials-summary.md:62–73`). The six are: range restriction, unreliability of the
**treatment**, unreliability of the **criterion**, lack of construct symmetry of the **treatment**,
lack of construct symmetry of the **criterion**, negative sampling error. The paper carries the
"of both treatment and criterion" qualifier on *unreliability* and drops it from *construct
symmetry*, so the list reads as five. The number six is right; the enumeration undercounts.

**Minimal repair.** "…(range restriction, unreliability of both treatment and criterion, lack of
construct symmetry on both the treatment and the criterion side, and negative sampling error)".

### 11. §6.1 — *d* = 0.05 is the uncorrected estimate, not the bias-corrected one. **CONFIRMED**

> "Macnamara and Burgoyne (2023), in a comprehensive meta-analysis, found that growth mindset
> interventions produced negligible effects on academic achievement (*d* = 0.05 **after correction
> for publication bias**)…"

`paper.md:253` (`paper.tex:283`)

Primary read (Psych. Bull. 149(3–4), 133–173). *d̄* = 0.05, 95% CI [0.02, 0.09], *p* = .004 is the
**raw** overall effect and is nominally significant. A separate trim-and-fill analysis imputing ~10
missing studies is what renders it non-significant. As written, the paper implies 0.05 is what
survived correction.

**Minimal repair.** "…negligible effects on academic achievement (*d* = 0.05, a result that became
non-significant once publication bias was accounted for)". The "financial ties" clause is verbatim
accurate — keep it.

### 12. §1 promises disconfirmation criteria the predictions do not carry. **CONFIRMED**

`paper.md:43`: "Section 7 … states its testable predictions **and their disconfirmation criteria**".
`paper.md:305` repeats it: "with the falsifiers of Sections 7.2 and 7.3 attached."

Audited across the nine numbered predictions: **explicit disconfirmation criteria exist for
predictions 7 and 9 only**; prediction 6 carries an implicit one (5-year vs 1-year effect sizes).
Predictions 1–5 and 8 have none. The length distribution tells the same story — P1–P6 average 55
words, P7–P9 average 338. The short six are the "too general" ones, which is the exact reason
`prediction-framing.md` records for the NoC desk rejection, and RIM has three desk rejections
already. `prediction-framing.md` also warns specifically against a numbered fixed count ("'Nine
predictions' invites 'your prediction #3 is wrong, so your theory is wrong'"); §7.2 presents exactly
that.

**Minimal repair.** Either attach criteria to 1–6 and 8, or cut the weak ones into a short
"further consequences" paragraph and reserve the numbered list for the three that carry falsifiers —
and soften §1 and §6.5 to match whatever is true afterwards.

### 13. §6.1 and §6.2 contradict each other on chess, ten lines apart. **CONFIRMED**

`paper.md:255`: "expertise routinely allows individuals to circumvent apparent working memory limits
through chunking and automatization (**Chase & Simon, 1973**)" — Chase & Simon is *Perception in
chess*.

`paper.md:261` and `paper.md:267`: "This difference matters at the extremes — … in competitive chess
at the **grandmaster** level"; "At the extremes — … or tasks requiring exceptional processing
capacity (theoretical physics, **grandmaster-level chess**) — Performance does become the binding
constraint."

The paper cites the founding study of chess expertise for the claim that chunking circumvents WM
limits, then names grandmaster chess as the paradigm case where WM capacity is the binding
constraint. A reviewer who knows the expertise literature will read this as the paper refuting itself
with its own citation.

**Minimal repair.** Replace the chess example in §6.2 with one that is not the subject of the §6.1
citation, or keep chess and say the constraint at that level is accumulated pattern knowledge — which
is what Chase & Simon show and what the recursive model would want anyway.

### 14. §2.4 — "curiosity" appears not to be one of Wechsler's 1943 terms. **SUSPECTED**

> "…identifying **persistence, curiosity, and goal orientation** as essential components of
> intelligent behavior (Wechsler, 1943)."

`paper.md:71` (`paper.tex:96`)

The quotation itself ("We cannot expect to measure total intelligence until our tests also include
some measures of the non-intellective factors") is confirmed across independent secondary sources at
Wechsler 1943, p. 103 — the primary is paywalled and was not reached. But the term list is not: every
account of the 1943 paper found uses **drive, persistence, will, temperament, interest/zest, goal
awareness**. "Curiosity" surfaces in a *different, later* Wechsler paper (1950, *American
Psychologist*, "Cognitive, Conative, and Non-Intellective Intelligence"). Marked SUSPECTED because it
rests on absence-of-evidence from secondary sources.

**Minimal repair.** Get the 1943 PDF and quote his own list, or drop the enumeration and keep only
the verified quotation.

### 15. §3.1 and §3.4 — the Wittmann & Hattrup risk-taking mediation claim may not be in the source. **SUSPECTED**

`paper.md:101`: "Handlungsdrang maps to the exploration and risk-taking dispositions that Wittmann
and Hattrup (2004) showed **mediate** intelligence-performance relationships by generating new
learning opportunities."
`paper.md:157`: "Wittmann and Hattrup (2004) further showed that risk-taking — a motivational
disposition — **mediates** the relationship between intelligence and performance in dynamic systems."

Bibliographic details confirmed (*Systems Research and Behavioral Science* 21(4), 393–409). The
primary was not reachable. Every secondary account describes risk-aversiveness being used to explain
a **gender difference** in Tailorshop performance (women invested less in risky strategies; riskier
strategies "create a learning environment with greater opportunities to discover and master the
rules") — an explanation of a group difference, not a fitted intelligence → risk-taking → performance
mediation. The claim is made twice and is doing real work in §3.1 (it is what grounds
*Handlungsdrang* empirically).

**Minimal repair.** Get the paper. If it is the gender-difference result, restate as "consistent
with" and describe what was actually found. Wittmann is the paper's acknowledged reader — this is the
citation most likely to be checked by someone who knows.

### 16. Abstract is 321 words against the target journal's ~200-word limit. **CONFIRMED**

`paper.md:23`. Declared target (`paper.md:12`, metadata comment) is *Journal of Intelligence* (MDPI),
whose Instructions for Authors state the abstract "should be a total of about 200 words maximum".
321 words is 60% over. Given three prior desk rejections, a format-noncompliant abstract is a cheap
way to earn a fourth. Note also: **no `journal-guidelines-jintelligence.md` exists in the repo** —
`paper/jaic/journal-guidelines-jaic.md` is the only stored guidelines file, and `CLAUDE.md` requires
reading the target journal's guidelines before building submission artifacts.

### 17. §7.3 — the quoted Performance-subtest range rests on an estimate the next sentence disclaims. **CONFIRMED**

> "gains ranging from **11.70 to 21.50** points across the five Performance subtests … The gains for
> Object Assembly and Picture Arrangement are Flynn and Weiss's own estimates rather than
> measurements … **the argument here does not rest on them.**"

`paper.md:359` (`paper.tex:389`)

Checked against the primary — `literature/fulltext/FlynnWeiss2007.pdf`, Table 2, p. 215. The five
Performance subtests over 1947.5–2001.75 (SD = 15): Picture Completion 11.70, Block Design 15.90,
Object Assembly **[17.35]**, Coding 18.00, Picture Arrangement **[21.50]**. The upper bound of the
quoted range **is** the bracketed Picture Arrangement estimate. Excluding both bracketed values and
Coding (which §7.3 excludes on its own grounds), the measured simulation-loaded Performance range is
11.70–15.90 — below Coding, the one subtest the partition cannot accommodate.

Everything else in that paragraph is exact against Table 2 and verified: Similarities 23.85,
Vocabulary 4.40, Arithmetic 2.30, Information 2.15, Comprehension 11.00, Full Scale 16.83–17.63 over
54.25 years, Coding 18.00, Digit Span 1.00 IQ point 1972–2002, the bracketing of OA and PA, and
Flynn's "spectacles provided by science" attribution. One nuance: Flynn and Weiss's visual-media
account of the Coding gains is hedged in the source ("**Perhaps** the speeded-up tempo…"); the paper
says "attribute", which is firmer than the original.

**Minimal repair.** State the measured range and the estimated range separately: "11.70 to 15.90 on
the two Performance subtests the WISC-IV retained, with Object Assembly and Picture Arrangement
estimated at 17.35 and 21.50 by Flynn and Weiss because the WISC-IV retained neither."

### 18. §5.1 — "LLMs process millions of tokens per second". **SUSPECTED**

`paper.md:213` (`paper.tex:241`). Set against a single human's working memory, this is off by one to
three orders of magnitude for any single deployed model instance: a served model produces tens to
low hundreds of tokens/s per stream, and a few thousand aggregate on one accelerator with batching.
"Millions per second" is a cluster-wide aggregate across many concurrent users — not the quantity the
sentence is comparing. The point survives at "thousands of tokens per second"; the inflated figure is
the kind of thing an AI-literate reviewer will use to discount the whole §5.

### 19. §5.1 — Miller (1956) cited for a working-memory capacity of 7 ± 2. **SUSPECTED (reviewer risk)**

`paper.md:213`. Miller's paper is about the coincidence between the span of absolute judgment and the
span of immediate memory, and he was cautious about "7" as a constant. The modern estimate for
working-memory capacity with rehearsal and chunking controlled is ~4 ± 1 (Cowan, 2001, *BBS* 24).
Citing Miller alone for a WM capacity figure in a paper submitted to an intelligence journal is the
kind of dated attribution reviewers in that field flag reflexively — and §6.1/§6.2 build a
quantitative argument on chunk counts.

### 20. §7.1 — "polythetic" is formally inconsistent with the model's own multiplicative notation. **SUSPECTED**

`paper.md:317`: "In a polythetic class, members share most but not all defining properties, and **no
single property is necessary or sufficient** for membership. Multiple K × P × M configurations can
produce equifinal outcomes…"

Under a product, every factor *is* necessary — a zero on any component collapses the whole. The
abstract's headline notation "(Knowledge × Performance × Motivation)" therefore asserts the opposite
of the polythetic claim made five lines later. §7.4 pre-concedes the model is not formally specified,
which blunts this, but the notation is in the abstract and the polythetic claim is load-bearing for
"why early IQ is a poor predictor".

Separately and minor: the *term* "polythetic" is Sneath's (1962), popularised by Sokal & Sneath
(1963); Beckner (1959) wrote "polytypic". Citing Beckner for the concept is conventional in the
literature, so this is low-severity — but it is wrong as an attribution of the word.

### 21. Smaller items

| Where | What | Status |
|---|---|---|
| `paper.md:261` | "one person can hold, roughly, one more chunk of information in mind than another" — a quantitative claim about the 25th–75th percentile of WM capacity, with no citation, in a paragraph that carries the §6.2 argument. | uncited |
| `paper.md:389` | "whose specific consequence for the treatment of motivation has not been systematically examined **until now**" — a priority claim that §2.6 (Carr & Dweck 2019; Ackerman 2018) and §3.4 (Dörner, Bach, Sun, Sloman & Croucher, van der Maas, Dickens & Flynn) already partly concede. *Theory & Psychology* desk-rejected this paper with "argument not new"; this sentence invites that response again. | SUSPECTED over-claim |
| `paper.md:253` | "changing beliefs about intelligence … **cannot restart the recursive loop**" — the model absorbs the null result of mindset interventions by asserting a barrier. Reads as an immunising move, and it is a barrier-form sentence in a paper otherwise disciplined about price-form. | SUSPECTED |
| `paper.md:95` | "NFC and TIE correlate at *r* ≈ .78–.87 (Woo et al., 2007; Schweitzer et al., 2025)". Schweitzer's own text confirms the range and attributes it to Woo et al.; Woo et al.'s primary was unreachable and every secondary account of it reports only *r* = .78. The .87 endpoint is currently unverified against Woo. | unverified endpoint |
| `paper.md:23` | "a separate research tradition has spent **three decades** engineering intrinsic motivation into artificial agents" — the paper's own earliest cite in that tradition is Schmidhuber (1991), 35 years back. | trivial |
| `paper.md:389` | "intelligence is what intelligence tests measure … (Sternberg, 1985)" — the tautology is canonically Boring (1923); Sternberg critiques it. | trivial |
| `paper.md:149`, `paper.md:349` | Wittmann & Süß (1999) "≈50% of variance … intelligence-as-knowledge as the strongest direct predictor" and Wittmann (1988) "Extraversion predicted the mean … Neuroticism the intraindividual standard deviation" — both chapters unreachable behind paywalls; the ~50% figure has weak secondary corroboration ("~51%"), the Eysenck example has none at all. Prediction 8's methodological model rests entirely on the second. | UNVERIFIED |

---

## Diagnostic tools — what each one said

**`python3 scripts/verify_references.py --check`** — exit 0, and **clean for RIM**:

```
2 reference problem(s) across 709 entries:
  - noc:Penrose1994 is marked needs-review: Crossref disagrees on: first author, year, volume
  - noc:Wigner1961 is marked needs-review: Crossref disagrees on: year
```

Both hits are in the NoC paper, not RIM. All 97 `rim:` manifest entries are `verified` (72) or
`verified-manual` (25). **Note what this does and does not buy**: the gate confirms the cited work
*exists* with the stated authors/year/venue. Findings 1–4 above are cases where the work exists,
the bibliographic details are right, and the *sentence* misstates it. The gate cannot see that —
which is `AIW-170`, already tracked.

**`python3 scripts/check_md_pdf_drift.py --paper rim`** — exit 0:

```
OK — paper.md and rim-paper.pdf agree on prose.
```

Verified this is a real check and not a vacuous pass: `tmp/rim-paper.pdf` exists and is byte-identical
to the committed `paper/intelligence/paper.pdf` (md5 `93ba8be8d689dbb878afd1b04d89a5cf`, both dated
2026-08-07 18:17). So `.md`, `.tex` and the shipped PDF are in sync — confirmed independently by
locating each defect above in `paper.tex` by hand.

**`.venv/bin/python -m pytest scripts/test_build_rim.py -q`** — exit 0:

```
14 passed in 0.04s
```

**0.04 s is the finding.** These are not build tests — nothing is compiled. Reading
`scripts/test_build_rim.py`: 13 of the 14 are unit tests of the cite-key extractor against synthetic
`.tex` fixtures (natbib optional args, `\citealp`, `\citeyear`, starred forms, capitalised forms);
the 14th, `test_real_rim_paper_passes`, asserts the real `.tex` has zero citation issues, where
"issue" means a `\cite` key with no `\bibitem`, a `\bibitem` never cited, or a 3+-author bibitem whose
label uses `&` instead of "et al.". It does not build the PDF, does not check `.md`↔`.tex` agreement,
and does not look at what any sentence claims. The suite is green and every finding above is invisible
to it. The build script's own name (`build_rim_pdf.py`) is not exercised anywhere in it.

**Bonus, not requested:** `python3 ~/simbook/scripts/check_prose_register.py paper/intelligence/paper.md`
→ `baseline 4.95 per 1k, 0 register hit(s), 0 dense window(s)`. **The prose register is clean.** I
read `prose-register.md` and swept by hand as well — no throat-clearing, no strategy-narration, no
revision-history narration, no "load-bearing", no "bite". The genuine-caution constructions the file
says to keep ("consistent with", "we do not claim", stated disconfirmers) are present and correct.
Register is not this paper's problem.

---

## Checked and found clean — coverage

Verified against primary sources unless noted.

- **Flynn & Weiss (2007) Table 2, every number.** Read directly from
  `literature/fulltext/FlynnWeiss2007.pdf`, p. 215. Similarities 23.85, Vocabulary 4.40, Arithmetic
  2.30, Information 2.15, Comprehension 11.00, Coding 18.00, Full Scale 16.83–17.63 over 54.25 years,
  Digit Span 1.00 IQ point across 1972–2002 and "not one of the 10 core subtests", the bracketing of
  Object Assembly [17.35] and Picture Arrangement [21.50] as estimates, and the "view the world
  through the spectacles provided by science" quotation — **all exact**. Only the range framing
  (finding 17) and the firmness of "attribute" are at issue.
- **Brose et al. (2010).** Read `literature/fulltext/Brose2010.pdf` in full. 101 younger + 103 older
  adults, ~100 occasions, confirmed part of the COGITO Study. Younger adults' motivation factors
  (effort, enjoyment) positively correlated with WM performance; older adults' correlations "not
  reliably different from zero"; heterogeneous within-person covariance structures; 21% of older
  adults excluded for not varying on motivation items. **Both places the paper cites it — §3.3 and
  prediction 8 — describe it accurately, including the careful "among participants whose motivation
  varied" qualifier.** This is the best-handled citation in the paper.
- **Edwards & DeYoung (2026).** Publisher page reached. Journal, title, DOI `10.65550/001c.162975`,
  year all correct; NLSY79 *n* = 11,914 and NLSY97 *n* = 7,008 exact; "specific abilities have 30–57%
  of the importance of *g*" verbatim; "held even between siblings" confirms the within-family framing.
  The two qualifications the paper attaches are appropriate.
- **Schweitzer et al. (2025).** PMC full text reached. Vol. 13(11), art. 142, four authors. Verbatim:
  "NFC (*r* = 0.19) was more strongly related to Gf than TIE (*r* = 0.12; F(1, 12.10) = 5.04,
  *p* = .045) whereas TIE (*r* = 0.35) was more strongly associated with Gc than NFC (*r* = 0.24;
  F(1, 13.10) = 10.70, *p* = .006)." **All four correlations and both significance tests exact**,
  and §3.1's careful "neither trait is Gf-specific" gloss is right. The S292 repair holds.
- **von Stumm & Ackerman (2013).** Author repository reached: 112 studies, 236 coefficients,
  N = 60,097, coefficients "ranging from 0 to .58, with an average estimate of .30". Exact.
- **Vu et al. (2024).** β = 0.176 (achievement → later motivation) vs β = 0.096 (motivation → later
  achievement), ratio 1.83 — "about twice", right direction. Secondary sources only (publisher 403).
- **Ackerman (2018, p. 9).** Open-access full text reached; quotation verbatim and the page number
  correct.
- **Canivez & Youngstrom (2019).** Full article reached; all three claims (Carroll/Horn irreconcilable
  on *g*; poor CFA fit for CHC batteries; weak incremental validity of broad abilities) check out
  against the text.
- **Hilger et al. (2020).** Direction verified: higher intelligence → **greater** temporal stability
  (lower variability) of brain network modularity. §7.1's characterisation is right, as is Hilger
  et al. (2017) and Schultz & Cole (2016), whose titles state the claims made of them. The S291
  Hilger repair holds.
- **Nusbaum & Silvia (2011).** Correct paper of the two 2011 Nusbaum & Silvia papers (the *PID* 51(5)
  O/I paper, not the *Intelligence* 39(1) divergent-thinking one); the Openness-predicts-creativity /
  Intellect-predicts-Gf dissociation matches.
- **Pietschnig & Voracek (2015).** Verbatim abstract obtained via the Crossref-deposited text: "271
  independent samples, totaling almost 4 million participants, from 31 countries… estimated 0.41,
  0.30, 0.28, and 0.21 IQ points annually for fluid, spatial, full-scale, and crystallized IQ test
  performance". **Every number in §7.3 matches exactly** — 271, 31, 0.41 fluid, 0.30 spatial, 0.21
  crystallized.
- **Sundet et al. (2004).** Publisher PDF read directly. Verbatim: "a language, mathematics, and a
  Raven-like test together with a combined general ability (GA) score… From the early 1970s, the
  secular gains in GA were almost exclusively driven by gains on the Raven-like test. However, even
  the means on this particular test stopped to increase after the mid to late 1990s." §7.3's
  description is accurate; the only slip is "late 1990s" for the source's "mid to late 1990s", which
  is immaterial.
- **Oberleiter et al. (2024).** Full author list, journal, volume 107, article 101867 and the
  substantive finding all confirmed against the publisher abstract (see the withdrawal note under
  finding 2). The characterisation in §7.3 is fair.
- **Ackerman & Heggestad (1997)** Openness–Gf .08 vs Openness–Gc .30 — consistent across independent
  secondary sources; primary not reached.
- **Wechsler (1940) and (1943)** confirmed as two distinct real publications with the same title
  (*Psych. Bull.* 37, 444–445 and *J. Abn. Soc. Psych.* 38, 101–103). **Wechsler (1944, p. 3)**
  definition verbatim correct — the S291 repair of that quote holds.
- **Cronbach (1949)** for maximum vs typical performance, **Frank (1962)** for C = S × D
  (Agis, Baden-Baden, formula confirmed in German sources) — both correct.
- **Schmidhuber (1991), Oudeyer & Kaplan (2007), Pathak et al. (2017), Friston et al. (2015),
  Sloman & Croucher (1981), Bach (2009, 2015), Dörner (1999), Dörner & Güss (2013), Sun (2009)** —
  bibliographic details and the claims made of them in §3.4 and §5.1 all check out. §5.1's
  concession that "the usual form of the claim, that artificial systems have no motivation at all, is
  false" is correct and is the paper's best paragraph.
- **van der Maas et al. (2006), Dickens & Flynn (2001), Savi et al. (2019)** — §3.4's descriptions
  match the sources. "It is two decades old" (van der Maas 2006 → 2026) is right.
- **Hassabis et al. (2007), Schacter & Addis (2007), Bartlett (1932)** — §7.1's characterisations
  match, including the "lacking spatial coherence" detail.
- **Jussim & Harber (2005)** — §6.3 now states their actual conclusion (small effects, accuracy
  rather than self-fulfilment, dissipation rather than accumulation) and explicitly flags the tension
  with §6.4. The S291 repair holds and this is now one of the paper's strongest passages.
- **The Bratsberg & Rogeberg *subtest* constraint** from `pending-rim-verification-debt.md` is
  honoured — §7.3 attributes the three-subtest structure to the Norwegian archive and Sundet et al.
  (2004) and casts the differential reversal as the open test, exactly as the constraint requires.
  (This is a different matter from finding 5b, which is about how §3.3 describes what the within-family
  design rules out.) **The Coding exclusion** is declared in advance with its cost stated, as
  required. Neither has drifted.
- **Reference list mechanics.** 97 entries, all cited in the body; no orphans; APA alphabetisation
  correct throughout including the `van`/`von` block and the single-author-before-multi-author rule
  for Ackerman, Cacioppo, Hilger, Rosenthal, Sternberg and Wechsler; every in-text `et al.` label
  matches its entry's author count.
- **The AIW-126b metadata block** does not render — it is an HTML comment in the `.md` and a `%`
  comment in the `.tex`. Confirmed fixed.

## Not checked

- **Wittmann & Süß (1999)**, **Wittmann (1988)** and **Wittmann & Hattrup (2004)** could not be
  reached in full text (two APA/Plenum book chapters and a Wiley article, all paywalled). Findings 15
  and the last row of section 21 record what that leaves unverified. These three are the citations
  most likely to be checked by a reader who knows the material, since Wittmann is thanked in the
  Acknowledgments.
- **Wechsler (1943)** primary is paywalled; the quotation is confirmed only by convergent secondary
  sources (finding 14).
- I did not rebuild any PDF. `paper/intelligence/paper.pdf` was not touched.

## One process note, not a paper defect

Everything in findings 1–5b was invisible to all three gates, and would have stayed invisible: the
works exist, the bibliographic details are right, the keys resolve, the `.md` and `.tex` agree, and
the prose register is clean. The gap between "the reference is real" and "the sentence is true of it"
is `AIW-170` and is already tracked — this review is a fifth independent demonstration of it
(after Hilger, Jussim & Harber, McGrew and the three S291 chimeras). The cheapest partial guard
available is a per-claim ledger: for each sentence that attaches a *number, a significance verdict or
a study design* to a citation, one line recording the verbatim source text it came from. Findings 1,
3, 4, 5b and 11 are all cases where such a line could not have been written without the defect
becoming obvious.
