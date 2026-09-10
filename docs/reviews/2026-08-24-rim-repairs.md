<!-- Action: present -->
# RIM citation repairs — execution record (2026-08-24)

Executes `docs/reviews/2026-08-24-rim-review.md`. Ten repairs applied, **each in both**
`paper/intelligence/paper.md` **and** the hand-maintained `paper/intelligence/paper.tex`
(confirmed hand-maintained via `.claude/knowledge/publication-build.md:299` — "RIM has no
md→tex generator"). Canonical `paper/intelligence/paper.pdf` **not touched** (blob
`73f526ca…` identical to HEAD).

---

## Gates

| Gate | Result |
|---|---|
| `python3 scripts/verify_references.py --check` | exit 1, **0 `rim:` problems**. All 4 reported problems are `noc:` (`Hameroff1996`, `Wigner1962` not in manifest; `Penrose1994`, `Wigner1961` in manifest but no longer in paper) — a concurrent agent's in-flight NoC edits, not mine. RIM's 97 manifest entries are unchanged: no reference added, none orphaned. |
| `.venv/bin/python -m pytest scripts/test_build_rim.py -q` | **14 passed in 0.02s**, exit 0. |
| LaTeX compile (isolated `tmp/agent-rim-build/`, since removed) | 2× `pdflatex -halt-on-error` → exit 0, PDF produced, **0 errors, 0 undefined citations**, 1 Overfull \hbox of 0.94pt at lines 416–417 (pre-existing, in §8, below the project's 2pt gate, not in any edited passage). |
| `python3 scripts/check_md_pdf_drift.py --paper rim` | **now FAILS (exit 1), by design** — 57 drift segments, every one traceable to one of the ten repairs, nothing unexpected. The canonical PDF is deliberately stale and must be rebuilt (`python3 scripts/build_rim_pdf.py`) before any republish / Zenodo v4. |

---

## Verifications performed before inserting anything

| Source | How verified | Verdict |
|---|---|---|
| Andrzejewski et al. (2024), *J. Intelligence* 12(12), 130 | PMC11676032 fetched | **Confirmed.** *d* 0.21–0.91; raw-score R² .908 (2005) → .901 (2011) → .892 (2018); "confidence intervals of R² values overlapped, showing no nominally significant findings"; authors interpret as "increasing ability differentiation and specialization in the general population". |
| Oberleiter et al. (2024), *Intelligence* 107, 101867 | Salzburg PURE record — **full abstract verbatim** (ScienceDirect 403) | **Confirmed.** "two population-representative Germanophone samples (N = 1267) across six measurement-invariant intelligence subscales from 2005 to 2024… substantial declines in single-factor analysis-based g assessments (ΔR2 range: ‐.037 to -.066)… meaningful test score increases in all domains (d range: 0.18 to 1.24)… may be a consequence of increasing ability differentiation in the general population." Crossref confirmed 8 authors / vol 107 / art 101867 / 2024. |
| Heckman (2006), *Science* 312(5782), 1900–1902 | **Primary PDF read in full** (jenni.uchicago.edu, all 3 pages) | **Confirmed and decisive.** No "age 27" and no "age 7" anywhere. p.1901 verbatim: "The Perry intervention group had IQ scores no higher than the control group by age 10. Yet the Perry treatment children had higher achievement test scores than the control children because they were more motivated to learn. In followups to age 40, the treated group had higher rates of high school graduation, higher salaries, higher percentages of home ownership, lower rates of welfare assistance as adults, fewer out-of-wedlock births, and fewer arrests than the controls." |
| Bratsberg & Rogeberg (2018), *PNAS* 115(26) | Europe PMC REST `abstractText` verbatim | **Confirmed.** "…finds no evidence for prominent causal hypotheses of the decline implicating genes and environmental factors that vary between, but not within, families." Elimination of between-family explanations, not of genetic explanations as a class, and not confirmation of a mechanism. |
| Wicherts et al. (2004), *Intelligence* 32(5), 509–537 | Two independent search retrievals of the abstract text (ScienceDirect / ResearchGate / Semantic Scholar all blocked or elided) | **Confirmed.** Five tests: Dutch WAIS 1967–1999, Dutch DAT 1984–1995, Dutch RAKIT 1982–1993, reanalyses of Must/Must/Raudik (Estonia) and Teasdale/Owen (Denmark). "measurement invariance with respect to cohorts is untenable… uniform measurement bias in some, but not all subtests." Exactly one Wechsler battery, and it is the **adult** scale. |
| Gardner (1983) / (1999) | Multiple convergent secondary sources | **Confirmed.** *Frames of Mind* (1983) = seven; naturalist added in *Intelligence Reframed* (1999) → eight; existential floated as a tentative ninth in the same book. |
| Macnamara & Burgoyne (2023), *Psych. Bull.* 149(3–4) | **Primary PDF text extracted and read** | **Confirmed.** Abstract verbatim: "Across all studies, we observed a small overall effect: d̄ = 0.05, 95% CI = [0.02, 0.09], which was nonsignificant after correcting for potential publication bias." So 0.05 is the **raw** estimate. |
| von Stumm, Hell & Chamorro-Premuzic (2011), *PPS* 6(6) | Search retrieval of abstract/method description | **Confirmed.** Path models on a meta-analytically derived correlation matrix; outcome is **academic performance**. No childhood→adult design, no adult outcome. |
| Murayama et al. (2013), *Child Development* 84(4) | **Primary PDF text extracted**, abstract verbatim | **Confirmed.** "six annual waves (Grades 5 through 10; Mage = 11.7 years at baseline; N = 3,530)", outcome = growth in mathematics achievement. Participants never reach adulthood. |
| Wittmann & Klumb (2006) six sources | `docs/wittmann-materials-summary.md:62–73` (project's own primary read, Figure 10.6 p.196) | **Confirmed.** Six = range restriction, unreliability of treatment, unreliability of criterion, construct asymmetry of treatment, construct asymmetry of criterion, negative sampling error. |

**Nothing was inserted that did not check out.** No replacement citation was weakened for lack of
verification. No new bibliography entry was needed (`Oberleiter2024` was already in the paper and
cited in §7.3; Gardner 1999 is referred to by year in prose rather than as a new `\bibitem`, which
avoids adding an unmanifested reference — `docs/reference-manifest.json` is out of this agent's
write scope and `--update` needs network).

---

## The ten repairs

### 1. §3.3 `paper.md:145` / `paper.tex:173` — Andrzejewski inversion

**Before**
> Even more striking is the dissociation reported by Andrzejewski et al. (2024): IQ scores rose while *g* — the general factor extracted from the correlation matrix — simultaneously declined. This dissociation is inexplicable under static-trait models but directly predicted by the recursive framework. Teaching to the test inflates Performance scores (narrow task-specific knowledge) without engaging the recursive loop. The result is higher scores on standardized measures with lower capacity for the self-directed, generalizable learning that the recursive loop produces. IQ goes up; intelligence, properly understood, goes down.

**After**
> A related pattern appears in the recent Austrian record, though it is a weaker result than it first looks. Oberleiter et al. (2024), comparing two population-representative Germanophone samples (N = 1267) across six measurement-invariant subscales from 2005 to 2024, report substantial declines in single-factor *g* assessments (ΔR² between −.037 and −.066) alongside meaningful score increases in every domain (*d* between 0.18 and 1.24); Andrzejewski et al. (2024) report the same direction over a shorter window (2005–2018), where the change (R² from .908 to .892) was not statistically significant. What declines in these records is the strength of the positive manifold — the inter-correlation among subtests — and not the level of any measured ability: every domain gained. Both sets of authors read the pattern as increasing ability differentiation in the general population. The recursive model does not predict that decoupling in advance and does not claim it as support. What it adds is a candidate mechanism for the differentiation: a loop engaged unevenly across content would produce increasingly asymmetric individual profiles while every subtest mean rises. Section 7.3 states the subtest-level test that would tell such an account from its competitors.

Conservative as instructed: "even more striking", "directly predicted", the teaching-to-the-test
mechanism and "IQ goes up; intelligence goes down" are all gone rather than transferred to
Oberleiter. Andrzejewski is retained **and labelled non-significant** (which removes its use as
support, correctly, and keeps its `\bibitem` cited so `test_build_rim` stays green). Crucially the
sources' own interpretation — increasing ability differentiation — is now stated as theirs, and the
recursive reading is offered as a *candidate mechanism for* that differentiation rather than as a
rival to it. Note Oberleiter's authors give the same differentiation reading, so this is now
honest about both.

### 2. §7.3 `paper.md:371` / `paper.tex:402` — Wicherts is not a Wechsler finding

**Before** … Wicherts et al. (2004) showed that **the Wechsler scales** are not measurement invariant over time …
**After** … Wicherts et al. (2004) showed that **cohort gains on five intelligence batteries from three countries, including the Dutch WAIS,** are often not measurement invariant …

Also applied the presentational fix the audit's withdrawal note asked for, separating Oberleiter
from the non-invariance claim so it is not read as a second non-invariance result:

**Before** "A secular change not carried by the common factor is what Oberleiter et al. (2024) report, and it is what the recursive model expects…"
**After** "Oberleiter et al. (2024) report something different from a failure of invariance — score gains across measurement-invariant subscales accompanied by a weakening common factor — and that is what the recursive model expects…"

### 3. §6.4 `paper.md:289` / `paper.tex:317` — the Heckman age comparison

**Before** … shows returns that grow over time — larger effects at age 27 than at age 7 — not because initial cognitive gains persist (they often fade), but because motivational and self-regulatory gains compound through subsequent learning.
**After** … shows returns that grow over time. The Perry treatment group had IQ scores no higher than the control group by age 10, yet in follow-ups to age 40 showed higher rates of high school graduation, higher salaries, higher rates of home ownership, lower rates of welfare assistance and fewer arrests. Heckman attributes the divergence not to persisting cognitive gains — those faded — but to the treated children being "more motivated to learn," a motivational and self-regulatory gain that compounds through subsequent learning.

The replacement is stronger than the original, because Heckman's own causal gloss ("because they
were more motivated to learn") is exactly the paper's claim, in his words.

### 4. §7.2 prediction 1 `paper.md:333` / `paper.tex:363` — the unsupported "existing evidence"

**Before** … Existing evidence supports this (von Stumm et al., 2011; Murayama et al., 2013), but more long-term longitudinal studies are needed.
**After** … The existing evidence stops short of this. Von Stumm et al. (2011) is a meta-analysis of academic performance, built on a meta-analytically derived correlation matrix drawn largely from concurrent student samples; Murayama et al. (2013) follows six annual waves from Grade 5 to Grade 10 (mean baseline age 11.7) with mathematics achievement as the outcome. Both establish that motivational variables predict school-age achievement beyond intelligence, and neither carries a childhood-to-adult design or an adult outcome. The prediction over adult achievement is therefore open, and testing it requires longitudinal data of a length the literature does not yet have.

Chose the audit's second option (keep the adult framing, declare the evidence absent) over the
first (retreat to school-age outcomes): a genuinely open prediction is the stronger asset, and both
citations survive in place doing accurate work, so neither `\bibitem` is orphaned.
`\citet` → `\Citet` at sentence start in the `.tex`, matching the file's existing convention for
`von`-prefixed names.

### 5. §2.5 `paper.md:77` / `paper.tex:102` — Gardner's count

**Before** Gardner (1983) proposed eight (later nine) relatively independent intelligences: linguistic, logical-mathematical, spatial, musical, bodily-kinesthetic, interpersonal, intrapersonal, naturalist, and (tentatively) existential.
**After** Gardner (1983) proposed seven relatively independent intelligences: linguistic, logical-mathematical, spatial, musical, bodily-kinesthetic, interpersonal and intrapersonal. A naturalist intelligence was added in 1999, bringing the count to eight, with an existential intelligence floated tentatively as a ninth.

### 6. §3.3 `paper.md:141` / `paper.tex:169` — Bratsberg & Rogeberg scope

**Before** … *within families* — ruling out genetic explanations and confirming environmental causation.
**After** … *within families* — a design that rules out explanations resting on changing between-family composition, including the prominent genetic ones, and is consistent with environmental causation.

### 7. §5.2 `paper.md:229` / `paper.tex:257` — the one BARRIER sentence → PRICE form

**Before**
> …the operational knowledge becomes part of the active processing. **Current LLMs cannot do this.** External scaffolding systems can modify the instructions given to an LLM (analogous to updating a set of rules the system follows), but such modifications do not integrate into the system's processing in the way that learned strategies integrate into human cognition. The system must be restarted with new instructions, at which point it is, in a meaningful sense, a new system — one that has no continuity of experience with its predecessor.

**After**
> …the operational knowledge becomes part of the active processing, and stays there. Current language models do the first half of this: a strategy derived at one turn conditions the model's outputs at later turns of the same context, with no external scaffolding and no restart. What they do not do is the second half. The strategy is held in the context rather than written back into the system, so its life is the life of that context; when the context ends, so does it, and the next session starts where the last one started. External scaffolding can carry a strategy forward by modifying the instructions given to the model, but the cost of maintaining it then sits outside the system rather than inside it, and each restart produces, in a meaningful sense, a new system — one that has no continuity of experience with its predecessor. The human case is one in which the strategy is retained; the machine case is one in which it is rented.

**Also repaired, same finding, `paper.md:223` / `paper.tex:251`** — the audit's minimal repair for
this finding names both lines:
**Before** Their capability is static, **entirely determined by training**, with no endogenous drive to extend it.
**After** Their capability is **static across sessions — whatever adaptation occurs within a context does not carry beyond it —** with no endogenous drive to extend it.

In-context learning now concedes the capability and prices it; no "X cannot do Y" remains in §5.

### 8. §7.2 prediction 7 `paper.md:345` / `paper.tex:375` — "six sources" naming five

**Before** (range restriction, unreliability of both treatment and criterion, lack of construct symmetry, and negative sampling error)
**After** (range restriction, unreliability of both treatment and criterion, lack of construct symmetry **on both the treatment and the criterion side**, and negative sampling error)

Count of six is correct in the source; the enumeration was undercounting. Fixed the enumeration,
not the number.

### 9. §6.1 `paper.md:253` / `paper.tex:280` — Macnamara *d* = 0.05 mislabelled

**Before** (*d* = 0.05 **after correction for publication bias**)
**After** (*d* = 0.05, **a result that became non-significant once publication bias was accounted for**)

The "financial ties" clause is verbatim accurate and was left alone.

### 10. Abstract word count — **NOT repaired, by instruction**

328 words by `str.split()` (the audit says 321; tokenizer difference only). MDPI *Journal of
Intelligence* Instructions for Authors: abstract "should be a total of about 200 words maximum".
**60–64% over.** Not touched — cutting the abstract is an author decision about venue, and it is
entangled with ruling question 2(ii) below, which also proposes an abstract edit. Related, from
the audit and still true: **no `journal-guidelines-jintelligence.md` exists in the repo**
(`paper/jaic/journal-guidelines-jaic.md` is the only stored guidelines file), while `CLAUDE.md`
requires reading the target journal's guidelines before building submission artifacts.

---

## Two questions needing the author's ruling

### Q1 — §7.2 prediction 5 contradicts §5.2/§5.3 and has no disconfirmer

**The contradiction, precisely.** §5.2 (`paper.md:225`) states the model's AI claim as a *denial of
sufficiency*: supplying an intrinsic drive to a system that *does* have persistent state and
self-modification "will not, by itself, produce a self-sustaining developmental trajectory." §5.3
(`paper.md:239`) then states that this narrow claim is the **only** thing the recursive model
claims about artificial systems: "What the recursive model does claim about artificial systems is
the narrower thing stated in Section 5.2." Prediction 5 (`paper.md:341`) states a claim of the
opposite shape — a *route* claim: "the path to artificial general intelligence runs through
motivation engineering, not merely through scaling Knowledge and Performance." §5.2 says motivation
engineering is not sufficient; prediction 5 says it is the road. §5.3 says the narrow claim is all
the model claims; §7.2 lists the broad one.

**Separately, prediction 5 is unfalsifiable as written.** "Functional motivation analogue" has no
independent definition and the prediction carries no criterion: a system that fails to
self-develop confirms it, a system that succeeds is said to have acquired an analogue. This is the
exact failure `.claude/knowledge/prediction-framing.md` records for the earlier AI predictions.
The text reads as pre-revision material that the §5 rewrite replaced and the prediction list never
caught up with.

**Option (a).** Delete prediction 5 and replace it with the §5.2 experiment, stated with its
disconfirmer: a persistent-state, self-modifying agent given an intrinsic drive should explore and
improve on the distribution it explores *without* open-ended cross-domain compounding; observed
open-ended compounding disconfirms the model's claim about M. Effect: §7.2 becomes consistent with
§5.2/§5.3, and the prediction gains a falsifier. Cost: the paper stops asserting anything about
the route to AGI.

**Option (b).** Keep the AGI-route claim but demote it out of the numbered prediction list into an
explicitly labelled conjecture, and amend §5.3 to acknowledge that the author holds a broader view
about the AGI route that the model does not entail. Effect: the author's actual belief survives in
print. Cost: §5.3's "the narrower thing is all we claim" sentence loses its force, and the
conjecture is still unfalsifiable — it is just no longer mislabelled as a prediction.

**Answerable as:** *"Replace prediction 5 with the §5.2 experiment and its disconfirmer — yes/no?
If no: demote it out of the numbered list as a labelled conjecture — yes/no?"*

### Q2 — §7.3's disconfirmer was already passed, and the abstract spends prediction 7

**(i) The §7.3 disconfirmer.** `paper.md:373` gives two limbs. Limb 1 — "simulation-loaded and
retrieval-loaded subtests show statistically indistinguishable secular trajectories once the
classification is fixed in advance" — **was already passed by the data the partition was built
from**: `paper.md:359` has just shown the two classes' secular trajectories differ, using Flynn &
Weiss's Table 2, and the classification was not fixed in advance of that table. `paper.md:363`
says so itself: "Three predictions follow, none of them yet tested against a classification fixed
in advance." So limb 1 cannot disconfirm anything, and it contradicts the correct statement ten
lines above it. Limb 2 (the reversal falling on retrieval-loaded content) is genuinely
forward-looking and is unaffected.

**Answerable as:** *"Restate limb 1 over a held-out record — a different test family, or another
country's standardisation series — where 'fixed in advance' can actually be met (yes), or simply
delete limb 1 and keep only the reversal limb (no)?"*

**(ii) The abstract vs prediction 7.** The abstract (`paper.md:23`) calls the attenuation account
established: "an interpretation **supported by** Brunswik symmetry analysis, which predicts that
the modest motivation-intelligence correlations **are** measurement artifacts rather than evidence
of weak association." Prediction 7 asserts the same thing flatly mid-paragraph (`paper.md:345`:
"The modest correlations **are**, in large part, measurement artifacts") — and then two paragraphs
later (`paper.md:347`) designates it the thing at risk: if symmetric aggregation still yields
*r* ≈ .30, "**then the attenuation account is wrong**." An untested prediction with a stated
disconfirmer is the paper's strongest asset in §7; the abstract spends it by calling it support.
§3.1 already says the right thing ("The unity claim has to be carried by evidence that can come
apart").

**Answerable as:** *"Rewrite the abstract clause into at-risk form — 'an interpretation the
framework puts at risk: Brunswik symmetry analysis implies the modest correlations may be
measurement artifacts, and §7.2 states the aggregation result that would show they are not' — and
delete the flat assertion at `paper.md:345` (yes/no)?"* Note this edit lands in the abstract, so it
interacts with the 328-word overrun in repair 10 — if the abstract is being cut for MDPI anyway,
both changes should be made in one pass.

---

## Deliberately not repaired

Everything below is in the audit but outside the assigned repair list. None of it was touched.

| Audit finding | Why not repaired here |
|---|---|
| 12 — §1 and §6.5 promise disconfirmation criteria that predictions 1–6 and 8 do not carry | Not assigned. Also entangled with Q1 (fixing prediction 5 changes the count) and with `prediction-framing.md`'s warning against a fixed numbered list. Needs an author decision on whether to attach criteria or cut the weak predictions into a "further consequences" paragraph. |
| 13 — §6.1 cites Chase & Simon (1973) for chunking circumventing WM limits, then §6.2 names grandmaster chess as the case where WM *is* the binding constraint | Not assigned. **CONFIRMED and cheap**; recommend it for the next pass. The fix is either a different example in §6.2 or saying the constraint at that level is accumulated pattern knowledge — which is what Chase & Simon actually show. |
| 14 — "curiosity" may not be among Wechsler's 1943 terms | SUSPECTED; primary is paywalled. Requires the 1943 PDF. |
| 15 — Wittmann & Hattrup (2004) "mediates" claim (asserted twice, `paper.md:101` and `:157`) | SUSPECTED; primary unreachable. Wittmann is the paper's acknowledged reader, so this is the highest-risk unverified claim in the manuscript. |
| 17 — §7.3's "11.70 to 21.50" Performance range has its upper bound set by a bracketed Flynn & Weiss *estimate* that the next sentence disclaims | Not assigned. **CONFIRMED**; measured range excluding brackets and Coding is 11.70–15.90. Cheap fix, recommend for the next pass. |
| 18 — "LLMs process millions of tokens per second" (`paper.md:213`) | SUSPECTED; not assigned. Off by 1–3 orders of magnitude for a single deployed instance; the point survives at "thousands". |
| 19 — Miller (1956) cited for WM capacity 7 ± 2 | SUSPECTED (reviewer risk); not assigned. |
| 20 — "polythetic" (§7.1) is formally inconsistent with the abstract's multiplicative K × P × M notation | SUSPECTED; not assigned; needs an author call on the notation. |
| 21 — smaller items (uncited chunk claim at `:261`; "until now" priority claim at `:389`; "cannot restart the recursive loop" barrier form at `:253`; unverified .87 endpoint at `:95`; "three decades" vs Schmidhuber 1991 at `:23`; Boring-not-Sternberg tautology at `:389`; unverified Wittmann & Süß / Wittmann 1988 figures) | Not assigned. Note `:253`'s "cannot restart the recursive loop" is a second barrier-form sentence in the same paragraph I repaired for Macnamara — flagging it since repair 7 was about exactly this form. |

## Follow-on required before publishing

1. **Rebuild the canonical PDF.** `paper/intelligence/paper.pdf` is now stale against both `.md`
   and `.tex`; `check_md_pdf_drift.py --paper rim` fails accordingly. Run
   `python3 scripts/build_rim_pdf.py` (bibliography is an inline `thebibliography`, so no bibtex
   pass is needed). The edited `.tex` compiles clean, verified in an isolated tmp dir.
2. **Zenodo v3 is out in the world with all ten defects.** A v4 with these repairs is the point of
   the exercise.
