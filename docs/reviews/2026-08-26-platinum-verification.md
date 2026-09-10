<!-- Action: reference -->
<!-- Tracked-by: AIW-241 -->
# RIM Platinum — citation verification batch (S313, 2026-08-26)

Four parallel Fable agents, each on a non-overlapping source set, each required to state what it had
actually read and to label any abstract-only verdict as such. Commissioned by the Platinum proposal's
execution step 2: **nothing reaches the Platinum draft unverified.**


---

## Agent A — the three occupants (Kanfer & Ackerman, Shenhav, Kurzban)

# Platinum verification — §3.4 adjacency occupants ("motivation as resource allocation")

Verified 2026-08-26 (WSL, Fable subagent). Method: Crossref DOI resolution, PMC full texts,
Cambridge Core, OpenAlex, Semantic Scholar API, Kanfer–Ackerman lab page (gatech), and full-text
extraction of a secondary source (Russell & Kuhnert 1992, *Leadership Quarterly*) for K&A 1989.
Every quote below is copied from a fetched source, with location. Items I could not see are
marked **UNVERIFIED** with what would settle them.

---

## 1. Kanfer & Ackerman (1989)

### (a) Bibliographic truth — CONFIRMED (one addition)
Crossref (`10.1037/0021-9010.74.4.657`) and Kanfer's own lab page
(kanfer-ackerman.gatech.edu/publications/) agree:

> Kanfer, R., & Ackerman, P. L. (1989). Motivation and cognitive abilities: An
> integrative/aptitude-treatment interaction approach to skill acquisition.
> *Journal of Applied Psychology, 74*(4), 657–690. https://doi.org/10.1037/0021-9010.74.4.657

Discrepancies vs. claimed cite: none, except the claim omitted **issue 4** — add it.
(Some CVs append "[Monograph]" to this article; I could not verify that label — omit it.)

### (b) What it actually claims — CONFIRMED IN SUBSTANCE, but **primary verbatim text UNVERIFIED**
The paper is paywalled everywhere I could reach: PsycNet full-text and landing pages are
JS-gated, the abstract is "elided by publisher" in Semantic Scholar, `abstract_inverted_index`
is null in OpenAlex, DTIC's related tech report (ADA224569) bot-blocks, no open mirror found.
**I have not read one sentence of the primary text.** What would settle it: PsycNet/library
access to `psycnet.apa.org/fulltext/1989-41520-001.pdf`.

Content is nevertheless firmly established by convergent secondary sources, chiefly Russell &
Kuhnert (1992), *Leadership Quarterly* 3(4), full text extracted locally (ou.edu/russell/pdf/LQ91b.pdf):

> "Kanfer and Ackerman (1989) proposed a model for skill acquisition that simultaneously
> integrates cognitive abilities, self-regulatory processes, and information processing
> demands." (p. 338)

> "Distal motivational processes are conceived in terms of traditional expectancy theory (VIE)
> terms (Vroom, 1964). These processes capture individuals' initial motivational processes in
> the allocation of scarce cognitive resources among tasks, i.e., how they decide to do one
> thing vs. another. Proximal motivational processes capture the ongoing motivational
> activities of self-regulat[ion]…" (p. 338, quoting/paraphrasing K&A's framework)

> "…simple training in goal setting may serve to either (1) redirect cognitive resource
> allocation by changing initial decisions to engage in a task (distal motivational processes)
> or (2) reactivating or amplifying self-regulation activities (proximal motivational
> processes)." (p. 348, attributed to K&A 1989)

Multiple independent sources (PubMed abstract of the 1996 JAP follow-up, GWU review) add: the
learner's limited **attentional resources are divided between on-task, off-task, and
self-regulatory uses** during learning, and self-regulation itself consumes attention. So the
claimed content "motivation as the allocation of limited attentional resources during skill
acquisition" is an accurate one-line gloss. The famous formula "motivation = direction,
intensity, and persistence of attentional effort" is widely attributed to this paper but I
could not verify it against the primary page — do not quote it verbatim without checking.

### (c) Timescale — SEPARABILITY SURVIVES, WITH A PHRASING WARNING
What is allocated is **concurrent attentional capacity during task engagement** — a momentary,
within-task resource. That supports the paper's claim. Two adversarial edges, neither fatal:

1. **The distal component is a between-task, prospective allocation** — "how they decide to do
   one thing vs. another" via expectancy theory. That is a longer-than-momentary allocation of
   effort *across tasks*, though still on the scale of task episodes, not development.
2. **The framework is explicitly longitudinal across practice**: it tracks allocation demands
   through Anderson's three phases (declarative → compilation → procedural) over hours-to-weeks
   of practice, and Russell & Kuhnert (1992, p. 341) even bolt Kegan's *adult-development* model
   onto K&A precisely because K&A itself does NOT cover developmental change — indirect but
   nice evidence that contemporaries read K&A as not making developmental-allocation claims.

Nothing in any source has K&A allocating **offline simulation time in an explicit self-model
across developmental time**. Verdict: the separability claim holds, but write it as
"allocation of concurrent attentional resources during task engagement (tracked across
practice)", not "purely momentary" — the distal/expectancy component is the surface a hostile
reviewer would push on.

### (d) Psychometric consequences — **DANGER: the flat "none" claim is FALSE here**
K&A 1989 is an **aptitude–treatment interaction** paper: its central deliverable is a set of
predictions about **when ability–performance correlations hold**, moderated by motivational
resource allocation and practice phase (e.g., goal assignment during early, resource-hungry
practice hurts low-ability learners). The surrounding Ackerman program it builds on says
explicitly (Russell & Kuhnert 1992, p. 338): "initial performance differences between high and
low cognitive ability individuals decrease, and **correlations between cognitive skills tests
and task performance attenuate over time** (Ackerman, 1987; Hulin, Henry, & Noon, 1990)."

So: K&A DO derive measurement-relevant consequences (ability–performance correlation dynamics,
ATIs) from the allocation idea. What they do NOT derive: consequences for the measurement of
the allocated quantity itself — nothing on attenuation of a *trait* under narrow measurement,
nothing on a consistency-vs-level decomposition. **The paper must scope its claim to exactly
that**, or §3.4 hands a referee a counterexample. (Note the correlation-attenuation quote is
attributed to Ackerman 1987 / Hulin et al. 1990, not to K&A 1989 itself — cite accordingly.)

**Verdict: CONFIRMED (bibliographic + substance), with (d) scoping required and primary-text
quotes UNVERIFIED.**

---

## 2. Shenhav, Botvinick & Cohen (2013)

### (a) Bibliographic truth — CONFIRMED
Crossref (`10.1016/j.neuron.2013.07.007`):

> Shenhav, A., Botvinick, M. M., & Cohen, J. D. (2013). The expected value of control: An
> integrative theory of anterior cingulate cortex function. *Neuron, 79*(2), 217–240.
> https://doi.org/10.1016/j.neuron.2013.07.007

Discrepancies: none. (Claimed cite gave only "Neuron"; volume 79(2), 217–240 now pinned.)
Note it is framed as a theory of **dACC function**, not of motivation per se.

### (b) Actual claims (full text via PMC3767969)
The dACC computes the **expected value of control** and specifies "the identity and intensity
of the desired control signal"; intensity is "the degree to which the parameter is displaced
from its default value". Formally:
EVC(signal, state) = Σᵢ Pr(outcomeᵢ | signal, state)·Value(outcomeᵢ) − Cost(signal),
with an "intrinsic cost to engaging control itself, which scales with the intensity of the
signal required". "Control allocated by expected-value optimization" is an accurate gloss.

### (c) Timescale — SEPARABILITY HOLDS
Full-text check (PMC): allocation is moment-to-moment and monitoring-driven —
> "This continues until a change in the current state — detected through monitoring — indicates
> that the previously specified control signal is no longer optimal (either in terms of its
> identity or intensity), and a new signal should be specified."
Trial-to-trial adjustment and within-episode persistence are covered; **no developmental or
offline-simulation allocation claims found**. Adversarial residue: EVC's "identity" dimension
includes choosing *which* task-set to control, i.e., near-term task selection — like K&A's
distal edge, still episodic, not developmental.

### (d) Psychometrics — CONFIRMED ABSENT
Full-text check found no individual-differences, test-correlation, reliability, or measurement
derivations. (Caveat: verified against the PMC author-manuscript text via extraction, not a
line-by-line read of all 24 pages.)

**Verdict: CONFIRMED on all four counts.**

---

## 3. Kurzban, Duckworth, Kable & Myers (2013)

### (a) Bibliographic truth — CONFIRMED (one structural note)
Crossref (`10.1017/S0140525X12003196`) + Cambridge Core:

> Kurzban, R., Duckworth, A., Kable, J. W., & Myers, J. (2013). An opportunity cost model of
> subjective effort and task performance. *Behavioral and Brain Sciences, 36*(6), 661–679.
> https://doi.org/10.1017/S0140525X12003196

Author names as printed: Robert Kurzban, Angela Duckworth, Joseph W. Kable, Justus Myers —
matches the claim exactly (Duckworth without middle initial, as printed). **BBS structure:
pp. 661–679 is the target article only**; issue 36(6) continues with ~2 dozen open peer
commentaries and the authors' response. Citing 661–679 cites the target article — correct for
the paper's purpose, but if §3.4 leans on the *debate*, the commentaries/response need their
own locus.

### (b) Actual claims (full text via PMC3856320; abstract via Cambridge Core)
Abstract: "certain computational mechanisms, especially those associated with executive
function, can be deployed for only a limited number of simultaneous tasks **at any given
moment**. Consequently, the deployment of these computational mechanisms carries an
opportunity cost – that is, the next-best use to which these systems might be put."
Sect. 2.3.1: "the allocation of mental processes to a task carries opportunity costs equal to
the value of the next-best use of those mental processes."
Sect. 2.3.2: "the sensation of 'mental effort' is **the output of mechanisms designed to
measure the opportunity costs** of engaging in the current mental task."
So "felt effort as the opportunity-cost readout of allocation" is accurate ("output" is their
word; "readout" is a fair gloss). Context checked: these sentences carry their surface meaning
— the model is explicitly a cost-benefit alternative to resource depletion.

### (c) Timescale — SEPARABILITY HOLDS
The simultaneity constraint ("at any given moment") makes the allocation intrinsically
momentary; within-session fatigue is explained by time-on-task cost-benefit dynamics
(Sect. 2.4.3), **not** by any longer-store depletion — and no developmental or
offline-simulation allocation appears anywhere in the target article.

### (d) Psychometrics — CONFIRMED ABSENT (and quotably so)
No trait-measurement, test-correlation, or attenuation derivations in the target article —
notable given Duckworth (of grit/self-control psychometrics) is a coauthor. Caveat: verified
against the PMC author-manuscript via extraction; the commentaries (not checked one by one)
may contain psychometric points, so scope the paper's claim to the target article.

**Verdict: CONFIRMED on all four counts.**

---

## Bottom line for §3.4

- The three sources jointly occupy: allocation of **concurrent attention / control intensity
  within task episodes**, priced by expected value or opportunity cost, with felt effort as the
  cost signal. None allocates offline simulation time in an explicit self-model across
  developmental time. **The separability claim survives adversarial reading.**
- Two mandatory precision fixes: (i) K&A's *distal* component is a prospective between-task
  allocation and the framework spans practice phases — phrase the shared ground as "concurrent
  attentional/control resources during task engagement", not "purely momentary"; (ii) the
  "no psychometric consequences" claim is **false for K&A if stated flatly** — K&A's whole ATI
  program derives ability–performance-correlation consequences. Scope it: none of the three
  derives consequences for the measurement of the allocated disposition itself (attenuation
  under narrow measurement, consistency-vs-level).
- Open verification debt: K&A 1989 primary text unread (paywalled everywhere) — any verbatim
  K&A quote in the draft must wait for PsycNet access.

Sources: api.crossref.org (3 DOIs) · pmc.ncbi.nlm.nih.gov/articles/PMC3767969 (Shenhav full
text) · PMC3856320 (Kurzban full text) · cambridge.org/core (Kurzban abstract/pages) ·
kanfer-ackerman.gatech.edu/publications · ou.edu/russell/pdf/LQ91b.pdf (Russell & Kuhnert 1992,
extracted locally) · api.openalex.org, api.semanticscholar.org (K&A abstract unavailable).

---

## Agent B — the field's own witnesses (Meehl, Borsboom, Eronen & Bringmann, van der Maas)

# RIM §2.7 witness verification — four psychology-internal sources

Verified 2026-08-26. Method: Crossref (api.crossref.org) for bibliography; full-text PDFs read directly for Meehl 1978 (errorstatistics.com mirror, 29 pp), Borsboom et al. 2004 (dennyborsboom.com author copy, 11 pp, page images read), van der Maas et al. 2006 (gwern.net mirror, 20 pp, text-extracted); Eronen & Bringmann 2021 full text via PMC (PMC8273366, open access), with a second character-exact quote-verification pass. No verdict below is abstract-only.

---

## 1. Meehl (1978) — CONFIRMED; intended use partially faithful, one caveat

**Bibliography (Crossref + PDF title page):**
Meehl, P. E. (1978). Theoretical risks and tabular asterisks: Sir Karl, Sir Ronald, and the slow progress of soft psychology. *Journal of Consulting and Clinical Psychology, 46*(4), 806–834. DOI: 10.1037/0022-006X.46.4.806
(a) Discrepancies: none. All fields match exactly.

**What Meehl actually argues:** Theories in soft psychology (clinical, counseling, social, personality, community, school) are non-cumulative — they are neither refuted nor corroborated, they just fade. He gives two causes: 20 intrinsic subject-matter difficulties, and — his main target — reliance on null-hypothesis significance testing, which subjects theories to only "feeble risk" (his phrase, p. 821-822 area) instead of Popperian grave danger of refutation.

**Strongest verbatim line (p. 807):**
> "I do not think that there is any dispute about this matter among psychologists familiar with the history of the other sciences. It is simply a sad fact that in soft psychology theories rise and decline, come and go, more as a function of baffled boredom than anything else; and the enterprise shows a disturbing absence of that cumulative character that is so impressive in disciplines like astronomy, molecular biology, and genetics."

**Abstract (p. 806), also quotable:**
> "Theories in 'soft' areas of psychology lack the cumulative character of scientific knowledge. They tend neither to be refuted nor corroborated, but instead merely fade away as people lose interest."

**Bonus — a construct that died without being typed either way (p. 807, on "level of aspiration"):**
> "It did not get integrated into the total nomological network, nor did it get clearly liquidated as a nothing concept. It did not get killed or resurrected or transformed or solidified; it just kind of dried up and blew away."
This is the single best Meehl passage for a construct-typing critique specifically: a construct whose referential status was never settled in either direction.

**(b) Faithfulness:** Faithful as a witness that soft-psychology theorizing is non-cumulative and that constructs are never referentially settled. A stretch if cited as a critique of construct-typing per se — Meehl's diagnosis is methodological (significance testing + feeble tests), not that psychology types its constructs wrongly.

**(c) Cuts against:**
- Section "16. Open Concepts" (p. 815) DEFENDS loose constructs: "the unavoidability of open concepts in social and biological science" — he calls psychologists who "view open concepts as somehow methodologically sinful" victims of "cultural lag." Meehl explicitly says the difficulty "occurs not because psychologists are intellectually lazy or sloppy... Rather, it arises from the intrinsic nature of the subject matter." If §2.7 argues psychology's constructs are ill-formed, Meehl is a hostile witness on that exact point: he thinks open concepts are legitimate and the sin lies in weak testing.
- Meehl co-invented construct validity (Cronbach & Meehl 1955); he is reformist, not abolitionist. He also lists 20 intrinsic difficulties precisely "lest you think that I am beating up on the profession."

---

## 2. Borsboom, Mellenbergh & van Heerden (2004) — CONFIRMED; intended use faithful

**Bibliography (Crossref + PDF):**
Borsboom, D., Mellenbergh, G. J., & van Heerden, J. (2004). The concept of validity. *Psychological Review, 111*(4), 1061–1071. DOI: 10.1037/0033-295X.111.4.1061
(a) Discrepancies: none. (Crossref renders "Van Heerden"; the paper byline is "Jaap van Heerden" — lowercase "van" is correct in the reference.)

**Claimed content "validity-as-existence-and-causation" — VERIFIED, verbatim (p. 1061, right column):**
> "Thus, a test is valid for measuring an attribute if and only if (a) the attribute exists and (b) variations in the attribute causally produce variations in the outcomes of the measurement procedure."

Abstract variant (p. 1061): "A test is valid for measuring an attribute if (a) the attribute exists and (b) variations in the attribute causally produce variation in the measurement outcomes." Preceding sentence (p. 1061): "If something does not exist, then one cannot measure it. If it exists but does not causally produce variations in the outcomes of the measurement procedure, then one is either measuring nothing at all or something different altogether."

**Directly useful for the paper's predicts-without-referring distinction (p. 1065):**
> "If no attribute answers the referential call, the test is not valid for measuring that attribute, no matter how useful the test may be for prediction or selection or how well it may fulfill other functions."
And (p. 1063): "The attribute to which the psychologist refers must exist in reality; otherwise, the test cannot possibly be valid for measuring that attribute."

**(b) Faithfulness:** Fully faithful. This is exactly the validity-as-existence-and-causation paper, and it explicitly severs validity from predictive utility — which is the hinge §2.7 apparently needs.

**(c) Cuts against:**
- The claim is CONDITIONAL. Borsboom et al. are realists who never assert that psychological attributes in general fail to exist; they redefine what validity would require. Citing them as evidence that constructs ARE invalid/fictitious would be an overreach — they are witnesses for the STANDARD, not for any verdict under it.
- p. 1065 warning, relevant if RIM says tests "measure" a non-referring construct: "To state that one measures an attribute but that the attribute does not exist is not to put forward some sophisticated philosophical position but to make an empty gesture to evade the difficulties involved." Safe phrasing: the test *predicts* without *measuring*; unsafe phrasing: the test *measures* a construct that doesn't exist.

---

## 3. Eronen & Bringmann (2021) — CONFIRMED; intended use faithful with a fence

**Bibliography (Crossref + Europe PMC, PMC8273366, PMID 33513314):**
Eronen, M. I., & Bringmann, L. F. (2021). The theory crisis in psychology: How to move forward. *Perspectives on Psychological Science, 16*(4), 779–788. DOI: 10.1177/1745691620970586
(a) Discrepancies: none.

**What they actually argue (full text, PMC):** Psychology's replication crisis sits on a deeper theory crisis; developing good theories is extremely hard for three reasons: (i) lack of robust phenomena to constrain theories; (ii) construct-validity problems; (iii) psychological interventions are "fat-handed," blocking causal inference. They explicitly pick up Meehl 1978 as their starting point (their gloss, quote-verified: "Meehl pointed out that psychological scientists are fond of developing new theories, but instead of resulting in cumulative theoretical progress, these theories tend to just come and go").

**Key verbatim line for §2.7 (section "Psychological Constructs and Epistemic Iteration"; character-verified in context):**
> "As construct validation of this kind is hardly ever done, the result is that psychological science is permeated by numerous psychological constructs of unknown validity."
Context (immediately preceding, ties them to Borsboom's criterion): "…establishing validity requires showing that variation in the attribute of interest is actually causing the variation in the test scores."

**(b) Faithfulness:** Faithful as a witness to a live, field-internal theory crisis, and they explicitly operate with the causal (Borsboom-style) validity criterion — so the two witnesses chain together. Note the operative word is "unknown" validity, not "absent" validity.

**(c) Cuts against (character-verified, Discussion):**
> "However, we by no means intend to suggest that theorizing in psychology is hopeless or a waste of resources or that we should return to a kind of behaviorism in which theories about mental processes are rejected as unscientific."
They frame the obstacles as "challenges that need to be met," recommend iterative construct validation, and cite ongoing research programs as exemplary. If §2.7 uses them for "the field itself admits constructs are of unknown validity" — clean. If it slides toward "the field admits its constructs are broken" — they preemptively repudiate that reading in the same paper.

---

## 4. van der Maas et al. (2006) — CONFIRMED bibliographically; intended use faithful ONLY in conditional form

**Bibliography (Crossref + PDF):**
van der Maas, H. L. J., Dolan, C. V., Grasman, R. P. P. P., Wicherts, J. M., Huizenga, H. M., & Raijmakers, M. E. J. (2006). A dynamical model of general intelligence: The positive manifold of intelligence by mutualism. *Psychological Review, 113*(4), 842–861. DOI: 10.1037/0033-295X.113.4.842
(a) Discrepancies: none. Six authors, all University of Amsterdam, order confirmed.

**Abstract (verbatim, from PDF):**
> "The positive manifold is often explained by positing a dominant latent variable, the g factor, associated with a single quantitative cognitive or biological process or capacity. In this article, a new explanation of the positive manifold based on a dynamical model is proposed, in which reciprocal causation or mutualism plays a central role. It is shown that the positive manifold emerges purely by positive beneficial interactions between cognitive processes during development. A single underlying g factor plays no role in the model."

**The exact passage the paper's template rests on (General Discussion, p. 855–856; page-break stitched "…latent factor, but" → "what about…"):**
> "The positive manifold, g, and general intelligence are often viewed as synonymous. We have shown that positive manifold does not necessarily imply a single quantitative latent factor, but what about in the case of general intelligence? Of course, this depends on one's definition of general intelligence. If we equate general intelligence with g, then the mutualism model does not support general intelligence. … Given this interpretation of general intelligence, there is nothing wrong with using the g factor as a summary or psychometric index variable (e.g., in prediction), as long as we do not assume that this variable relates to a single underlying quantitative process or capacity. In this view, the g factor is not advanced as an explanatory variable."

**(b) Adversarial test of "explains why a construct that does not refer still predicts":**
- The mechanism IS there, verbatim: within the mutualism model there is no single underlying capacity, yet the g index remains legitimate "e.g., in prediction." The positive manifold (hence predictive power) is generated by mutualistic interactions, not by a referent of "g." So as a TEMPLATE — a formally worked-out case where an index predicts although nothing answers its referential call — the use is faithful.
- BUT the authors do NOT claim g does not refer *simpliciter*. Their claim is model-relative and explicitly hedged: "does not necessarily imply a single quantitative latent factor" (p. 855); and in the falsification discussion (p. 856): "It is not easy to falsify explanations of the positive manifold. It is also quite possible that a full explanation of intelligence data requires elements of all three explanations." They present mutualism as an alternative explanation with a research program, not a refutation of g theory. (Also note p. 849: the phrase "in which psychometric g does not exist" occurs there, but it describes a special block-diagonal variant resembling multiple-intelligences — do NOT quote that line as the paper's thesis.)
- Safe §2.7 phrasing: "mutualism shows HOW a non-referring construct COULD still predict" / "demonstrates that the positive manifold does not require a common cause." Overreach phrasing: "mutualism showed that g is not a thing." The first is the source; the second is not.

**(c) Cuts against:**
- The falsifiability concession above (alternative, not refutation; pluralism about explanations).
- The model is technically EQUIVALENT to the hierarchical factor model under some parameterizations ("under certain choices of M, the covariance structures associated with the hierarchical factor model and the mutualism model are technically equivalent," p. 849) — i.e., the data at issue cannot decide between g-realism and mutualism. That equivalence is a double-edged sword: it licenses "predicts without referring" as a live possibility, but blocks any claim that psychometrics' construct was shown wrong.
- Later empirical literature contests it in both directions: a paper titled "Dynamic mutualism versus g factor theory: An empirical test" exists (seen in search listings, ScienceDirect/Intelligence; content UNVERIFIED here — its verdict would need its own check before mention). Recommend §2.7 not lean on mutualism being empirically vindicated, only on its existence as a formal demonstration.

---

## Cross-cutting note for §2.7

The four witnesses chain cleanly IF each is held to its actual claim: Meehl (theories non-cumulative; constructs never referentially settled) → Borsboom et al. (validity = existence + causal production; prediction ≠ validity) → Eronen & Bringmann (constructs of UNKNOWN validity; explicit heirs of both Meehl and the causal criterion) → van der Maas et al. (a worked formal model where prediction survives without a referent). The section collapses only if it makes any of them say "constructs are fictions": Meehl defends open concepts, Borsboom et al. are conditional realists, Eronen & Bringmann explicitly deny hopelessness, van der Maas et al. keep g as a legitimate index and concede the data may not discriminate. "Unknown validity," not "known invalidity," is the strongest claim the field's own authorities license.

---

## Agent C — the empirical exhibits (Melby-Lervag, Ritchie & Tucker-Drob, Salthouse, Schaie)

# Platinum verification — RIM exhibit set C (WM training / education / Salthouse–Schaie)

Verified 2026-08-26 (Fable subagent). Sources: Crossref API, NCBI E-utilities (verbatim PubMed abstracts), PMC full texts (verbatim XML/HTML for the two meta-analyses), publisher records. Every number below was seen in the source named; anything not seen is marked UNVERIFIED.

---

## 1. Working-memory-training nulls (Melby-Lervåg & Hulme / Melby-Lervåg, Redick & Hulme)

### Which papers exist (all Crossref-verified)

1. **Melby-Lervåg, M., & Hulme, C. (2013). Is working memory training effective? A meta-analytic review. *Developmental Psychology, 49*(2), 270–291. https://doi.org/10.1037/a0028228** (Epub 2012 May 21; cite 2013.)
2. **Melby-Lervåg, M., Redick, T. S., & Hulme, C. (2016). Working memory training does not improve performance on measures of intelligence or other measures of "far transfer": Evidence from a meta-analytic review. *Perspectives on Psychological Science, 11*(4), 512–534. https://doi.org/10.1177/1745691616635612** — ⚠ the subtitle "Evidence From a Meta-Analytic Review" is part of the official title (PubMed/SAGE); Crossref truncates it. Include it.
3. Melby-Lervåg, M., & Hulme, C. — "There is no convincing evidence that working memory training is effective: A reply to Au et al. (2014) and Karbach and Verhaeghen (2014)." *Psychonomic Bulletin & Review, 23*(1), 324–330. https://doi.org/10.3758/s13423-015-0862-z — ⚠ year discrepancy: Crossref dates it 2015 (online), the issue is 2016. If cited, use 2016 with the issue pagination (APA rule), or "2015/2016" note.

### Which one to cite for "WM training does not transfer"

**Cite #2 (2016).** It is the paper whose title literally is the claim, it supersedes 2013 (87 publications / 145 comparisons vs 23 studies / 30 comparisons), and it is the one that isolates **treated** controls — which is where the null actually lives.

### The actual numbers (2016, Table 1 & 2, extracted verbatim from PMC4968033 XML)

Hedges's *g*, [95% CI], immediate posttest:

| Outcome | vs treated controls | vs untreated controls |
|---|---|---|
| **Nonverbal abilities (Gf proxy)** | **0.05 [−0.02, 0.13]**, k=67, n.s. | **0.20 [0.11, 0.28]**, p<.01 |
| Verbal abilities | 0.05 [−0.07, 0.17], n.s. | 0.03 [−0.09, 0.14], n.s. |
| Word decoding | 0.08 [−0.09, 0.24], n.s. | 0.01 [−0.16, 0.17], n.s. |
| Reading comprehension | 0.15 [0.03, 0.27], p<.05 (becomes trivial after removing one anomalous study) | 0.12 [−0.07, 0.31], n.s. |
| Arithmetic | 0.06 [−0.08, 0.19], n.s. | 0.12 [0.01, 0.23], p<.05 |
| Verbal WM (near/intermediate) | 0.31 [0.19, 0.42], p<.01 | 0.42 [0.24, 0.61], p<.01 |
| Visuospatial WM | 0.28 [0.16, 0.40], p<.01 | 0.51 [0.34, 0.69], p<.01 |
| Criterion (trained task) | 0.80 [0.62, 0.97], p<.01 | 1.88 [1.33, 2.42], p<.01 |

Delayed posttest, nonverbal abilities: treated **−0.05 [−0.21, 0.11]** (k=12), untreated 0.03 [−0.22, 0.28] (k=7). I.e., at follow-up the point estimate against treated controls is *negative*.

Additional verified findings (2016, verbatim abstract + full text): mediation analyses show WM gains uncorrelated with far-transfer magnitude; publication-bias analysis finds "no evidential value" in the treated-control studies; well-powered treated-control studies (k=34 meeting minimum N) give g = 0.01 on nonverbal ability.

### 2013 paper — abstract-only verdict

Verbatim abstract conclusion (PubMed efetch): "there was no convincing evidence of the generalization of working memory training to other skills (nonverbal and verbal ability, inhibitory processes in attention, word decoding, and arithmetic)" — near-transfer verbal-WM gains "were not sustained at follow-up."
**Effect sizes with CIs from the 2013 paper: UNVERIFIED.** Closed access (APA PDF behind Incapsula bot-wall, Semantic Scholar/Unpaywall report CLOSED, no PMC deposit). What would settle it: institutional access to *Developmental Psychology* 49(2). This does not block the draft: use the 2016 numbers, which are verified and stronger.

**Verdict: CONFIRMED** (2016 paper carries the claim, with verified numbers). Caveat for fairness: the null is a *treated-control* null; against untreated controls the Gf effect (g = 0.20) is significant — this is exactly the Au et al. (2015) counter-meta's territory, and the paper should not phrase the exhibit as "zero effect ever measured."

---

## 2. Ritchie & Tucker-Drob — education raises intelligence

**Ritchie, S. J., & Tucker-Drob, E. M. (2018). How much does education improve intelligence? A meta-analysis. *Psychological Science, 29*(8), 1358–1369. https://doi.org/10.1177/0956797618774253** (Crossref + PubMed verified; PMC6088505.)

Verbatim abstract headline: "142 effect sizes from 42 data sets involving over 600,000 participants … approximately **1 to 5 IQ points for an additional year of education**."

Per-design estimates (verbatim from PMC full-text HTML; the paper prints SE and p, **not** per-design CIs — bracketed CIs below are *my* ±1.96·SE computation, label them as derived if used):

- **Control prior intelligence:** 1.197 IQ pts/yr (SE = 0.203, p = 3.84×10⁻⁹) [derived CI 0.80–1.60]. Outcome tested at mean age 63.5.
- **Policy change (compulsory schooling, IV):** 2.056 IQ pts/yr (SE = 0.583, p = 4.23×10⁻⁴) [derived CI 0.91–3.20]. Outcome mean age 47.9.
- **School-age cutoff (regression discontinuity):** 5.229 IQ pts/yr (SE = 0.530, p = 6.33×10⁻²³) [derived CI 4.19–6.27]. Outcome mean age **10.4**.
- **Overall:** 3.394 IQ pts/yr (SE = 0.503, p = 1.55×10⁻¹¹) [derived CI 2.41–4.38].

Verified caveats that matter for RIM:
- **Cutoff-design durability is explicitly unknown**: "we did not identify any studies that tested whether these effects persisted into adulthood. These estimates should thus be regarded with caution" (verbatim). The 5-point end of "1–5" is the child-age, caution-flagged end. The cutoff design is also achievement-heavy (achievement tests 6.231 vs 3.839 pts for other tests; moderator 2.471, SE 0.524, p<.001).
- **Fluid vs composite:** in the control-prior-intelligence design, composite tests show larger effects than fluid tests (moderator −0.689, SE 0.234, p<.001; reported as 1.876 pts composite vs 0.836 pts fluid — the 1.876/0.836 split was extracted via a summarization pass over PMC and matches the verified moderator coefficient, but treat the two split values as second-pass numbers).
- **Effect shrinks with age of outcome** in that design: −0.026 IQ pts per year of age (SE = 0.012, p = .029); 2.154 pts at age 18 → 0.485 pts at age 83 (verbatim).

**Verdict: CONFIRMED with a magnitude warning.** If the paper's contrast concerns *fluid* intelligence in *adults*, the honest education number is ≈0.8–1.2 IQ pts (≈0.05–0.08 SD) per year, not 3.4 and certainly not 5. Quote "1–5 points" only with the design breakdown.

---

## 3. Salthouse (2009)

**Salthouse, T. A. (2009). When does age-related cognitive decline begin? *Neurobiology of Aging, 30*(4), 507–514. https://doi.org/10.1016/j.neurobiolaging.2008.09.023** (Crossref + PubMed verified; PMC2683339.)

Verbatim abstract claim: retest (practice) effects mask decline in longitudinal data; three retest-estimation methods plus animal and neurobiological evidence "converge on a conclusion that **some aspects of age-related cognitive decline begin in healthy educated adults when they are in their 20s and 30s**."

Note the hedges Salthouse himself carries: "some aspects," and the primary data are cross-sectional comparisons (18–60) with modeled retest corrections. Do not paraphrase him as "cognition declines from 27" without the "some aspects" qualifier.

**Verdict: CONFIRMED.**

---

## 4. The rebuttals (the "disagreement is the exhibit")

The target article drew four published commentaries in the same issue plus an author reply — all Crossref/PubMed-verified:

- **Schaie, K. W. (2009). "When does age-related cognitive decline begin?" Salthouse again reifies the "cross-sectional fallacy". *Neurobiology of Aging, 30*(4), 528–529. https://doi.org/10.1016/j.neurobiolaging.2008.12.012** — the Schaie rebuttal proper.
- **Nilsson, L.-G., Sternäng, O., Rönnlund, M., & Nyberg, L. (2009). Challenging the notion of an early-onset of cognitive decline. *Neurobiology of Aging, 30*(4), 521–524. https://doi.org/10.1016/j.neurobiolaging.2008.11.013** — ⚠ **not Schaie's group**: this is the Stockholm/Umeå Betula group. If the draft says "the Schaie group," that is a misattribution for this one; there are two independent rebuttals.
- Finch, C. E. (2009). The neurobiology of middle-age has arrived. *Neurobiology of Aging, 30*(4), 515–520. (Commentary, largely sympathetic on neurobiology.)
- Abrams, L. (2009). Exploring the generality of retest effects. *Neurobiology of Aging, 30*(4), 525–527.
- **Salthouse, T. A. (2009). Responses to commentaries by Finch, Nilsson et al., Abrams, and Schaie. *Neurobiology of Aging, 30*(4), 530–533. https://doi.org/10.1016/j.neurobiolaging.2009.01.004.**

### What the disagreement turns on (verified from PMC full texts of Schaie's commentary and Salthouse's reply, and Nilsson et al.'s abstract)

- **Schaie:** the "cross-sectional fallacy" — inferring within-person age *changes* from between-person age *differences* is invalid unless environments are stable and successive birth cohorts perform identically at the same age (citing Ryder 1965; Schaie 1965). Cohort differences, not practice effects, are "the major cause" of the cross-sectional/longitudinal discrepancy; 14-day retest intervals cannot estimate practice effects; longitudinal data show several domains "stable over the 20–60 year age range."
- **Nilsson et al. (verbatim abstract):** "Salthouse claims that cognitive aging starts around 20 … He dismisses longitudinal data, which typically show the cognitive decline to start much later, around 60 years of age … We challenge Salthouse's strong claim on four accounts."
- **Salthouse's reply (via PMC2923813):** he denies dismissing longitudinal data — "my primary proposal is that researchers need to be careful in the interpretation of both cross-sectional and longitudinal data"; both design types carry confounds (cohort effects vs retest effects), "no consensus is currently available regarding the best method for estimating retest effects," and the question is which confound better explains the discrepancy.

**Fair no-side statement of the exhibit:** cross-sectional data show monotonic decline on fluid-type measures from the mid-20s; longitudinal data show stability to ~60; each camp attributes the discrepancy to the other design's confound (retest/practice effects inflating longitudinal trajectories vs cohort effects inflating cross-sectional differences), and both sides agree the raw data patterns themselves are not in dispute — only their causal reading. That is a defensible, verified characterization. **Verdict: CONFIRMED** (with the Nilsson-is-not-Schaie's-group correction).

---

## Adversarial check on the load-bearing contrast ("education moves Gf / WM training doesn't")

The contrast is real but **design-asymmetric**, and the draft must not present it as a clean same-ruler comparison:

1. **Control-condition asymmetry (the loudest confound).** The WM-training null holds against *treated* controls (g = 0.05 n.s.); against *untreated* controls WM training shows a significant g = 0.20 on nonverbal ability. Education designs have no treated-control arm at all — there is no "placebo schooling." If one insisted on the untreated-control ruler for both, ~15 hours of WM training (g ≈ 0.20 ≈ 3 IQ pts) would look *bigger* than a year of schooling (≈0.08 SD ≈ 1.2 pts in the adult fluid estimate). The contrast survives only via the argument that expectancy/placebo cannot plausibly explain education effects measured decades later in natural experiments, whereas it demonstrably inflates WM-training effects. That argument is good — but the paper must make it, not assume it.
2. **Outcome constructs differ.** WM far-transfer outcomes are almost purely fluid (matrix-type). Education effects are largest on composite/achievement measures and smallest on fluid tests (0.836 pts/yr, control-prior design). On the shared construct (adult Gf), the education effect is ~1 IQ pt/yr — nonzero, CI excludes zero, direction confirmed — so the qualitative contrast stands, but quoting 3.4 or 5 pts against the WM null overstates it by 3–5×.
3. **Dose is wildly different.** ~1 school year (~1,000 h) vs typically a few weeks (~10–20 h) of WM training. Per-hour, the two literatures are not obviously different; the honest framing is "sustained, content-rich instruction at massive dose moves fluid scores a little and durably; brief process-training moves them not at all against matched controls."
4. **Durability asymmetry cuts in the paper's favor.** WM-training near-transfer fades and far transfer is −0.05 at delayed posttest; education effects persist across the lifespan (though decaying −0.026 pts/yr of age). This is the cleanest, verified leg of the contrast.
5. **Age ranges differ** (education outcomes at mean ages 63/48/10 by design; WM training spans children-to-elderly) — a minor confound relative to 1–3, but worth a clause.

**Verdict on the contrast: CONTRAST-CONFOUNDED as a naive numbers-vs-numbers claim; DEFENSIBLE if stated as: adult-Gf education effect ≈1 pt/yr with CI excluding zero and lifelong persistence, vs WM-training treated-control far transfer ≈0 (CI [−0.02, 0.13], negative at follow-up), with the treated-control logic spelled out.**

---

## Age-norming claim ("age-normed IQ defines away the raw-decline question")

How norming actually works (consistent across multiple secondary descriptions of WAIS-IV; **not verified against the Pearson technical manual itself**): the normative sample (2,200 adults, ages 16–90) is split into 13 age bands; raw scores convert to scaled scores (M = 10, SD = 3) *within the examinee's own age band*; FSIQ is a deviation score relative to same-age peers. Consequence: the same raw score earns a higher scaled score at older ages; an average-for-80 performance yields IQ 100 regardless of raw level.

**Assessment: fair, with one required nuance.** It is true by construction that an age-normed IQ *cannot express* raw decline — the score answers "how do you stand among age-mates," so population-typical decline is invisible in it. But "defines away" should not imply concealment: the raw decline is *documented inside the norming tables themselves* (that is why the age bands exist), and the cross-sectional gradients Salthouse analyzes come from exactly such standardization data. Suggested phrasing: age-norming *relocates* the raw-decline question from the score to the norm tables; the IQ metric is silent on it by design. If the draft needs a citable anchor beyond textbook descriptions, cite the WAIS-IV Technical and Interpretive Manual (Wechsler, 2008, Pearson) — UNVERIFIED here (manual not accessible), so either obtain it or anchor the point on Salthouse (2009)'s use of standardization samples instead.

---

## Discrepancy ledger (everything found, however small)

1. MLRH 2016 full title includes the subtitle "…: Evidence From a Meta-Analytic Review" — Crossref drops it; include it.
2. MLH 2013: Epub 2012, print 2013 — cite 2013. Effect sizes from this paper UNVERIFIED (closed access); use 2016.
3. PBR reply: online 2015 vs issue 2016 (23(1):324–330) — pick one convention and note it.
4. "Schaie-group rebuttal": Schaie 2009 (528–529) is his alone; Nilsson/Sternäng/Rönnlund/Nyberg (521–524) are the Betula group, not Schaie's. Two rebuttals, don't merge them.
5. Salthouse reply exists and is citable: "Responses to commentaries by Finch, Nilsson et al., Abrams, and Schaie," 30(4):530–533 — if the paper stages the debate, cite it so the exchange is complete.
6. Ritchie & Tucker-Drob print SEs, not CIs, for the headline estimates — any CI given in the draft must be flagged as computed from SE (or drop CIs and give SE/p as printed).
7. Salthouse's claim is "some aspects … in their 20s and 30s" — not "cognition declines from the 20s." Keep his own hedge.
8. Schaie's 2009 affiliation on the commentary is University of Washington (not Penn State) — irrelevant for citation but avoid asserting affiliation in prose.

---

## Agent D — the open citation debts (von Stumm & Ackerman, Dignath & Buttner, Wittmann 1988)

# Platinum Verification — Item D: Three Open Citation Debts (RIM)

Verified 2026-08-26 via Crossref API, OpenAlex API (abstract_inverted_index), and publisher pages (SpringerLink). Every number below was seen in the cited source's own metadata or abstract unless explicitly labelled secondary.

---

## 1. von Stumm & Ackerman — the r ≈ .30 — **CONFIRMED**

**Bibliography (exact):**
von Stumm, S., & Ackerman, P. L. (2013). Investment and intellect: A review and meta-analysis. *Psychological Bulletin*, *139*(4), 841–869. https://doi.org/10.1037/a0030746

- Volume/issue/pages confirmed from OpenAlex biblio record (139, 4, 841–869); DOI and journal from Crossref. Crossref issue date 2013-07; OpenAlex lists publication_year 2012 (advance-online) — the citable year is **2013**.
- Reachable: yes. APA PsycNet DOI resolves; abstract fully retrievable via OpenAlex. Primary-source verification of the abstract achieved; full text is paywalled (APA).

**What the .30 actually is (from the abstract, seen verbatim via OpenAlex):**
- Meta-analysis of **112 studies, 236 coefficients, N = 60,097**.
- The correlation is between **"investment traits"** (34 trait constructs classified into 8 categories — e.g., need for cognition, typical intellectual engagement, openness-type traits) and **"indicators of adult intellect"** — a composite category including **crystallized intelligence (Gc), academic performance (e.g., GPA), college entry tests, and acquired knowledge**.
- Exact abstract wording: *"Meta-analytic coefficients ranged considerably, from 0 to .58, with an average estimate of .30."*

**Precision notes for the P7 falsification criterion:**
1. The published number IS .30 — but it is the **grand average across 236 heterogeneous coefficients** (all investment traits × all intellect markers pooled), not a single trait–knowledge correlation. The abstract explicitly says the strength **"differs across trait scales and markers of intellect"** with a range of 0–.58.
2. If P7's criterion is stated as "investment traits correlate with knowledge/Gc at r ≈ .30 on average," that is faithful. If it is stated as a correlation with *knowledge specifically*, the .30 is the pooled average across ALL intellect markers, not the knowledge-only estimate — the paper reports finer-grained coefficients per trait category and per marker in its tables (not visible in the abstract; UNVERIFIED at that granularity from here). If the paper's text needs the knowledge-specific value, someone must read the article's tables.
3. Discrepancy from the task description: none in substance. "r ≈ .30" is exactly what the abstract publishes as the average estimate.

---

## 2. Dignath & Büttner — SRL intervention meta-analysis — **CONFIRMED** (which of two 2008 papers matters)

**The wanted paper (matches "school-based, primary vs secondary"):**
Dignath, C., & Büttner, G. (2008). Components of fostering self-regulated learning among students. A meta-analysis on intervention studies at primary and secondary school level. *Metacognition and Learning*, *3*(3), 231–264. https://doi.org/10.1007/s11409-008-9029-x

- Verified directly on the SpringerLink article page (title, authors, journal, vol 3, pp. 231–264, published 01 Nov 2008). Issue 3 from OpenAlex biblio. Reachable: yes (SpringerLink; abstract public, full text paywalled).

**Effect sizes (from the publisher-page abstract, quoted):**
- Corpus: *"49 studies conducted with primary school students and 35 studies conducted with secondary school students; analyzing 357 effect sizes altogether."*
- *"The average effect size was 0.69."* (overall, across outcome categories)
- Outcome categories analysed separately: **academic performance, strategy use, and motivation**. Per-category and per-school-level effect sizes exist in the paper but are not in the abstract — UNVERIFIED at that granularity from here; reading the article's Tables would settle it.

**Moderators reported (from abstract):**
- Interventions had *"higher effects when conducted by researchers instead of regular teachers"*;
- *"higher effects when conducted in the scope of mathematics than in reading/writing or other subjects"*;
- *"the theoretical background on which the training programme is based, as well as the type of instructed strategy led to differential effects at both school levels"* (i.e., theoretical framing — e.g., (socio-)cognitive vs metacognitive vs motivational — and strategy type moderate outcomes, differentially by school level).

**Alternatives — do NOT confuse:**
- **Dignath, C., Büttner, G., & Langfeldt, H.-P. (2008).** How can primary school students learn self-regulated learning strategies most effectively? A meta-analysis on self-regulation training programmes. *Educational Research Review*, *3*(2), 101–129. https://doi.org/10.1016/j.edurev.2008.02.003 — **primary school ONLY** (a companion analysis). Verified via Crossref + OpenAlex biblio; abstract not retrieved. Cite this only if the claim is specifically about primary-school interventions.
- **Dignath & Büttner (2018)**, *Metacognition and Learning* — an observation study of teachers' promotion of SRL, **not** an intervention meta-analysis. Wrong paper for a "training works" claim.
- If the paper's claim is "SRL interventions work at both primary and secondary level, mean d ≈ 0.69, with moderators" → the **2008 Metacognition and Learning** paper is the one wanted.

---

## 3. Wittmann, W. W. (1988) — Brunswik symmetry — **CONFIRMED as a reachable English-language book chapter** (content characterization partly SECONDARY)

**Bibliography (exact, per the Springer chapter page — primary source):**
Wittmann, W. W. (1988). Multivariate reliability theory: Principles of symmetry and successful validation strategies. In J. R. Nesselroade & R. B. Cattell (Eds.), *Handbook of multivariate experimental psychology* (2nd ed., pp. 505–560). Plenum Press. https://doi.org/10.1007/978-1-4613-0893-5_16

**What it IS:** a book **chapter** (Chapter 16) in the 2nd edition of the Nesselroade & Cattell handbook, Plenum Press, New York (Springer now hosts it, "Springer, Boston, MA"). It is in **ENGLISH** — the worry that it might be an unobtainable German-language item is unfounded. Verified directly on the SpringerLink chapter page: title, author, editors, year, pages 505–560, DOI.

- ⚠ Page-range variance in the wild: the Springer chapter page says **pp. 505–560**; at least one citing article (J. Intelligence 2021, PMC7838820) lists "pp. 505–552". Use the publisher's 505–560. Also note some reference lists invert the editor order to "Cattell & Nesselroade" — the Springer page gives **Nesselroade & Cattell**.
- **Reachable:** yes — SpringerLink sells/serves the chapter (abstract publicly visible; full text paywalled). A full-text PDF also circulates on ResearchGate (Wittmann uploaded it). This is NOT a secondary-citation-only item.

**What it establishes (two evidence layers, kept separate per the standing rule):**
- *Primary (seen on the Springer chapter page):* only the abstract opening — "Reliability is one of the most basic concepts of science and a prerequisite for scientific work" — plus the title itself, which carries "Principles of Symmetry and Successful Validation Strategies."
- *SECONDARY (from the open-access J. Intelligence article PMC7838820, which quotes/summarizes Wittmann 1988):* Wittmann developed the symmetry principle as "an adaption of Brunswik's lens model": a true correlation between two hierarchically organized constructs is unbiasedly represented by the observed correlation **iff** (a) measurements correspond to the intended level of generalization and (b) the chosen levels of generalization are **symmetrical** for both constructs; consequently *"an observed correlation underestimates the true correlation ... if operationalizations from different levels of generalization or with dissimilar task contents are correlated."* Aggregation raises reliability, and reliability bounds validity — hence aggregation-level matching between predictor and criterion is the operative methodological rule. **This characterization is consistent across multiple citing sources but has not been verified against the chapter's own full text from here.** If a specific sentence in RIM leans on a specific Wittmann-1988 claim, the chapter full text (ResearchGate PDF) should be read once before submission.

**The known trap, restated:** the *empirical* WMC→intelligence→knowledge→complex-problem-solving path analyses belong to **Wittmann & Süß (1999)** (in Ackerman, Kyllonen & Roberts, *Learning and Individual Differences: Process, Trait, and Content Determinants*, APA) and to the Singapore 2002 ICAP paper — NOT to Wittmann (1988). The 1988 chapter carries the **methodological principle** (symmetry + aggregation), not the empirical M→K→performance results. Any RIM sentence citing "Wittmann (1988)" must be a methods/principle claim only.

---

## Summary table

| Item | Verdict | Key fact |
|---|---|---|
| von Stumm & Ackerman (2013), Psych Bull 139(4), 841–869, 10.1037/a0030746 | **CONFIRMED** | Average meta-analytic estimate is exactly .30 (range 0–.58; 112 studies, 236 coefficients, N=60,097) — between investment traits and pooled adult-intellect markers (Gc, GPA, entry tests, knowledge), not knowledge alone |
| Dignath & Büttner (2008), Metacog. & Learning 3(3), 231–264, 10.1007/s11409-008-9029-x | **CONFIRMED** | Overall mean ES 0.69 across 357 effect sizes (49 primary + 35 secondary studies); moderators: deliverer (researcher>teacher), subject (math>reading/writing), theoretical background, strategy type. Don't confuse with the primary-only ERR 2008 companion or the 2018 observation study |
| Wittmann (1988), in Nesselroade & Cattell (Eds.), Handbook of Multivariate Experimental Psychology (2nd ed., pp. 505–560), Plenum, 10.1007/978-1-4613-0893-5_16 | **CONFIRMED (bibliography, primary); content characterization SECONDARY** | English-language chapter, fully reachable via SpringerLink/ResearchGate — not an obscure German item. Carries the symmetry/aggregation *principle*; the empirical path results belong to Wittmann & Süß (1999) / ICAP 2002 |
