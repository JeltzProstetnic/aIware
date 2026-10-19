<!-- Action: reference -->
# RIM rulings — execution record (2026-08-24)

Executes the two rulings left open at the end of `docs/reviews/2026-08-24-rim-repairs.md`
(Q1 prediction 5, Q2 §7.3 limb 1 + abstract) plus the three confirmed leftovers.
Eight edits, **each applied in both** `paper/intelligence/paper.md` **and** the hand-maintained
`paper/intelligence/paper.tex`. Canonical `paper/intelligence/paper.pdf` **rebuilt** (21:06),
identical bytes to `tmp/rim-paper.pdf`.

Nothing outside `paper/intelligence/` and this file was touched. No commit, no push.

---

## Gates — all three green

| Gate | Result |
|---|---|
| `.venv/bin/python -m pytest scripts/test_build_rim.py -q` | **14 passed in 0.03s**, exit 0 |
| `python3 scripts/verify_references.py --check` | **exit 0** — "OK — 710 references (541 verified, 169 verified-manual), all verified and unchanged. 335 printed bibtex citations matched to verified entries." (The 4 `noc:` problems the previous agent saw are gone — that agent's concurrent NoC edits have since settled.) |
| `.venv/bin/python scripts/build_rim_pdf.py` | exit 0, 3× pdflatex, "All citations verified". Wrote `tmp/rim-paper.pdf` + canonical `paper/intelligence/paper.pdf` |
| `python3 scripts/check_md_pdf_drift.py --paper rim` | **exit 0** — "OK — paper.md and rim-paper.pdf agree on prose." |
| LaTeX overflow | One Overfull \hbox of **0.93776pt** at `paper.tex:418--419` — the pre-existing §7.4 one the previous record logged at 416–417 (shifted by my insertion), below the project's 2pt gate. **No new overflow.** |

**One build finding, caught and fixed mid-pass.** The first version of prediction 5's bold title
ended in `self-modification`, which pdflatex cannot hyphenate; it produced a **new** Overfull \hbox
of 5.95987pt at `paper.tex:371--372`, well above the 2pt gate. Retitled to
"Supplying an intrinsic drive to a system with persistent state and **the capacity to modify
itself**…", rebuilt, gone. Recording it because the same trap will fire on any future bold
prediction title containing a long hyphenated compound.

---

## RULING 1 — prediction 5 replaced with the §5.2 experiment

### The replacement, in full (`paper.md:341` / `paper.tex:371`)

> 5. **Supplying an intrinsic drive to a system with persistent state and the capacity to modify
> itself will not, by itself, produce open-ended cross-domain compounding**: The experiment is
> buildable now. Give an agent what deployed language models lack — state that persists across
> episodes and write access to the parameters that generate its behavior — and supply an intrinsic
> reward of the kind described in Section 5.1: prediction error or learning progress in its own
> world model (Schmidhuber, 1991; Oudeyer & Kaplan, 2007; Pathak et al., 2017), with external task
> reward held at zero. Run it against a matched control identical except for that reward. The
> recursive model predicts that the intrinsically driven agent will explore more and will improve
> on the distribution it explores, while the breadth of its competence saturates: performance on
> domains held out from its exploration flattens, and the rate at which it enters new domains
> declines rather than rises with run time. The quantity to track is therefore held-out
> cross-domain performance against run time, not within-domain score. Open-ended compounding
> refutes the prediction — non-saturating gains on held-out domains, with the set of domains the
> agent operates in widening as it runs — and on that outcome the Motivation component contributes
> less than the model claims of it. This is the claim of Section 5.2 and the only claim the
> recursive model makes about artificial systems; none of it turns on the architectural conjecture
> of Section 5.3.

**Before**

> 5. **AI systems will not exhibit self-directed intellectual development until they have functional
> motivation analogues**: This is a prediction about the future trajectory of AI development. It
> implies that the path to artificial general intelligence runs through motivation engineering, not
> merely through scaling Knowledge and Performance.

Notes on the construction:

- **Operationalised, not gestured at.** Three named requirements on the system (persistent state,
  write access to its own parameters, an intrinsic reward with the extrinsic reward at zero), a
  named control (matched, identical but for the reward), and a named dependent variable (held-out
  cross-domain performance against run time — explicitly *not* within-domain score, which is where
  the intrinsic-motivation literature already reports gains and where the prediction would be
  trivially satisfied).
- **The disconfirmer is stated as a positive observation**, not as an absence: open-ended
  compounding refutes it. Absence-of-compounding cannot be the falsifier, since that is the
  prediction.
- **Citations are all existing keys** — `Schmidhuber1991`, `Oudeyer2007`, `Pathak2017`, already in
  the bibliography and already cited in §5.1. No `\bibitem` added, none orphaned, manifest
  untouched.
- **The 2×2 wording rule is respected**: "the Motivation component", never a module count.
- The closing clause pins the prediction to §5.2 and disclaims §5.3, which is what makes §7.2
  internally consistent with §5.3's "the narrower thing is all we claim".

### The AGI-route intuition — kept, relocated, made losable (`paper.md:385` / `paper.tex:416`)

I judged the intuition *did* earn space, but not a second conjecture in §5.3 (that is ruling
option (b), which was rejected, and it would blunt §5.3's "narrower thing" sentence). It went into
§7.4 Limitations — inside the Discussion, as the ruling scoped it — as the last paragraph before
the existing "A final limitation concerns the boundary of the argument":

> The model's claim about artificial systems and the author's expectation about them are different
> things, and the second does not inherit the standing of the first. Section 5.2 states the claim:
> supplying an exploration drive to a system with persistent state and self-modification will not
> by itself produce open-ended compounding. It says nothing about what would. The author expects
> that the route to artificial systems which develop themselves runs through the engineering of
> motivation rather than through further scaling of knowledge and performance. That is a bet and
> not a result, and it is lost if such development appears in a system built by scaling knowledge
> and performance alone, with nothing in it answering to the description in Section 5.1. Nothing in
> Sections 6 or 7 depends on it either way.

It is labelled a bet, it is outside the numbered list, and it has a stated way to be wrong. It also
mirrors the register §5.3 already uses for the architectural conjecture, so it introduces no new
voice.

---

## RULING 2 — §7.3 limb 1 restated over a held-out record; abstract put at risk

### (i) The new §7.3 disconfirmation criterion, in full (`paper.md:373` / `paper.tex:404`)

> The prediction is disconfirmed if simulation-loaded and retrieval-loaded subtests show
> statistically indistinguishable secular trajectories **in a record the partition was not read
> off, with every subtest assigned to a class before its gains are inspected**, or if the reversal
> falls on retrieval-loaded content while simulation-loaded scores hold. **The first limb cannot be
> run on the American Wechsler standardizations reported above: the partition was constructed with
> that table in view, so a separation found there describes the classification rather than tests
> it. What the limb requires is a held-out record — another country's standardization series, or a
> different test family — classified in advance and then examined. The cohort datasets assembled by
> Wicherts et al. (2004) are of the right form, carrying subtest-level scores from three countries
> and compiled to answer a different question.** Competing accounts do not generate the contrast: a
> test-familiarity account predicts gains concentrated on whatever content is most practiced, and a
> nutrition or general-health account predicts a broadly uniform lift.

**Before**

> The prediction is disconfirmed if simulation-loaded and retrieval-loaded subtests show
> statistically indistinguishable secular trajectories once the classification is fixed in advance,
> or if the reversal falls on retrieval-loaded content while simulation-loaded scores hold.
> Competing accounts do not generate the contrast: …

Limb 2 (the reversal limb) is unchanged, as ruled. The new limb 1 now says the same thing
`paper.md:363` already says ("none of them yet tested against a classification fixed in advance"),
so the contradiction ten lines apart is gone.

**Why Wicherts et al. (2004) and not the Norwegian archive.** I nearly named the Norwegian
conscript series as the held-out record and stopped: `paper.md:359` already reports Norway's
differential subtest pattern (Raven-like subtest driving the gains, language and mathematics
contributing little), so Norway is *also* a record the partition was read with in view, and naming
it would have reproduced the exact defect being repaired. Wicherts's cohort datasets are
subtest-level, span three countries, and were compiled for a measurement-invariance question — so
"fixed in advance" can genuinely be met there. It also dovetails with the invariance constraint
stated in the immediately preceding paragraph (`paper.md:371`), which is the same source.

### (ii) The abstract clause (`paper.md:23` / `paper.tex:48`)

**Before**
> … in different contexts — an interpretation **supported by** Brunswik symmetry analysis, which
> predicts that the modest motivation-intelligence correlations reported in the literature **are**
> measurement artifacts rather than evidence of weak association.

**After**
> … in different contexts — an interpretation **offered at risk rather than as a finding**: Brunswik
> symmetry analysis implies that the modest motivation-intelligence correlations reported in the
> literature **may be** measurement artifacts rather than evidence of weak association, **and a
> symmetric aggregation that still returned the currently reported average would refute it**.

One deviation from the ruling's example phrasing, flagged for the author: the ruling's model
sentence ended "…and §7.2 states the aggregation result that would show they are not." I stated the
disconfirming *result* itself rather than pointing at a section number, because abstracts are read
detached from the paper and a bare "§7.2" is dead text in a submission portal or an indexing
service. Same content, no cross-reference. Say the word and it becomes the section pointer.

### (ii-b) The flat assertion at `paper.md:345` / `paper.tex:375` — deleted

**Before**
> The answer lies in Brunswik symmetry (Wittmann, 1988; Wittmann & Klumb, 2006). **The modest
> correlations are, in large part, measurement artifacts.** Motivation is typically assessed with
> single questionnaire scales …

**After**
> The answer lies in Brunswik symmetry (Wittmann, 1988; Wittmann & Klumb, 2006). Motivation is
> typically assessed with single questionnaire scales …

Straight deletion, no replacement connective. The paragraph still closes on its own hedged
statement ("The present model therefore predicts that …"), and the disconfirmer two paragraphs
below (`:347`) is now the only place the claim is settled — which is the point.

### Abstract word count

| | words (`str.split()`) |
|---|---|
| Before | **328** |
| After | **348** |
| Δ | **+20** |

**Not trimmed, by instruction.** For reference: MDPI *Journal of Intelligence* asks for "about 200
words maximum", so the abstract is now ~74% over that target. Untouched otherwise — the only
abstract edit is ruling 2's clause.

---

## The three leftovers

### L1 — the §6.1/§6.2 chess self-contradiction (two edits)

§6.1 cites Chase & Simon (1973) for expertise *circumventing* working memory limits through
chunking; §6.2 then twice named grandmaster chess as a case where working memory *is* the binding
constraint. Chess is the paradigm case Chase & Simon actually studied, so it was the worst possible
example for that role. Reconciled by removing chess from both extremes lists and stating the
correct constraint explicitly, which turns a contradiction into an argument for the paper's own
K-over-P thesis.

**`paper.md:261` / `paper.tex:288`**
- Before: "This difference matters at the extremes — in theoretical physics, in certain forms of
  mathematical proof, **in competitive chess at the grandmaster level**."
- After: "… — in theoretical physics, in certain forms of mathematical proof, **in any task that
  requires holding several unfamiliar relations in mind at once**."

**`paper.md:267` / `paper.tex:294`**
- Before: "At the extremes — individuals with significant cognitive impairments, or tasks requiring
  exceptional processing capacity (theoretical physics, **grandmaster-level chess**) — Performance
  does become the binding constraint. The recursive model does not deny …"
- After: "At the extremes — individuals with significant cognitive impairments, or tasks requiring
  exceptional processing capacity (theoretical physics, **certain classes of mathematical proof**) —
  Performance does become the binding constraint. **Expert chess, which looks like the obvious
  further example, is not one. What distinguishes grandmasters is the store of recognizable
  positions that lets them work around the working memory limit rather than exceed it, which is why
  their advantage in recalling a position all but disappears when the pieces are placed at random
  (Chase & Simon, 1973). That is a difference in Knowledge, not in Performance.** The recursive
  model does not deny …"

Hedge applied deliberately: "**all but** disappears", not "disappears". Chase & Simon (1973) report
the master advantage largely vanishing on random boards; Gobet & Simon (1996) later found a small
residual advantage. The stronger wording would have been a fresh citation defect.

### L2 — the §7.3 "11.70 to 21.50" range (`paper.md:359` / `paper.tex:390`)

- Before: "… and gains **ranging from 11.70 to 21.50 points across the five Performance subtests**,
  against 4.40 points on Vocabulary, …"
- After: "… and gains **across the five Performance subtests ranging from 11.70 to 21.50 points (an
  upper bound that is an estimate rather than a measurement; the largest measured Performance gain
  is 18.00, on Coding, and 15.90 excluding it)**, against 4.40 points on Vocabulary, …"

Took the "state the bound's status inline" option rather than silently substituting a different
range, and gave both defensible numbers so a reader can pick the one that suits the argument. The
next sentence, which already names Object Assembly and Picture Arrangement as the bracketed
estimates, now explains the parenthesis instead of contradicting the clause before it.

⚠ **Provenance flag.** The **15.90** figure is taken from the audit record
(`docs/reviews/2026-08-24-rim-repairs.md`, finding 17: "CONFIRMED; measured range excluding
brackets and Coding is 11.70–15.90"). I did **not** re-open Flynn & Weiss (2007) Table 2 to
re-derive it — the table is paywalled and this pass had no primary access to it. **18.00 on Coding**
and **11.70** are the paper's own already-published figures (`:357`, `:359`). If the author wants
15.90 independently confirmed before a v4 goes to Zenodo, that is a single primary-source check.

### L3 — the second barrier-form sentence (`paper.md:253` / `paper.tex:280`)

- Before: "This is consistent with the recursive model: changing beliefs about intelligence (a
  narrow sub-component of Motivation) without simultaneously addressing Knowledge and operational
  Knowledge **cannot restart the recursive loop**."
- After: "This is consistent with the recursive model: **a belief about intelligence is the cheapest
  part of the loop to move, and moving it alone buys the least. The loop compounds through
  iterations that pay, and an iteration pays through the operational knowledge that makes an
  attempt productive; an intervention that changes what a learner is willing to attempt, without
  changing what the attempt returns, is priced accordingly.**"

PRICE form throughout — a comparative cost-and-return claim, no "X cannot do Y". This was the last
barrier-form sentence flagged in the audit; §5 was cleared in repair 7 of the earlier pass.

---

## What I judged should NOT change, and why

| Item | Why left alone |
|---|---|
| **Abstract length (348 words vs MDPI's ~200)** | Explicitly out of scope. The venue is not settled and the cut is the author's call. Reported, not acted on. |
| **A second AGI-route conjecture inside §5.3** | That is ruling option (b), which the ruling rejected. Adding it there would cost §5.3's "the narrower thing is all we claim" sentence exactly the force the ruling was protecting. The intuition went to §7.4 instead. |
| **§7.3 limb 2 (the reversal limb)** | Ruled unaffected, and it is genuinely forward-looking. Untouched. |
| **The Norwegian conscript archive as limb 1's held-out record** | Rejected on inspection: `:359` already reports its differential subtest pattern, so it is not held out and naming it would have re-created the "satisfied by construction" defect. See ruling 2(i) above. |
| **Substituting 11.70–15.90 as the headline range** | Would have replaced a disclaimed number with a second-hand one and silently dropped Coding's 18.00 from a sentence that says "the five Performance subtests". Stating the bound's status keeps every figure in the paper traceable to the source. |
| **Audit finding 12** (§1 and §6.5 promise disconfirmation criteria that predictions 1–6 and 8 do not carry) | Not in this assignment. Note it is now **narrower than it was**: prediction 5 has acquired a disconfirmer in this pass, so the gap is predictions 1–4, 6 and 8. Still needs an author decision on attaching criteria vs cutting the weak ones into a "further consequences" paragraph — `prediction-framing.md` warns against the fixed numbered list as such. |
| **Audit findings 14, 15, 18, 19, 20, 21 (remainder)** | Unassigned and mostly SUSPECTED-not-confirmed. Finding 15 (Wittmann & Hattrup "mediates", asserted twice at `:101` and `:157`) is still the highest-risk unverified claim in the manuscript, because Wittmann is the paper's acknowledged reader. |
| **`journal-guidelines-jintelligence.md` still absent** | Out of write scope for this pass (not under `paper/intelligence/`). `CLAUDE.md` requires the target journal's guidelines to be read before building submission artifacts, and the only stored guidelines file remains `paper/jaic/journal-guidelines-jaic.md`. |

---

## Follow-on

1. **Zenodo v3 is still out with all ten citation defects plus these two structural ones.** The
   canonical PDF now carries all twelve repairs; a v4 is the point of the exercise.
2. Nothing is committed. My tracked changes are exactly `paper/intelligence/paper.md`,
   `paper/intelligence/paper.tex`, `paper/intelligence/paper.pdf`, plus the build byproducts
   `tmp/build-rim/paper.tex`, `tmp/build-rim/paper.pdf`, `tmp/rim-paper.pdf`, and this report.

⚠ **`git status` also shows changes I did not make** — `paper/full/latex/paper.tex`,
`tmp/build-full/{paper.tex,paper.bbl,paper.pdf,references.bib}` and the untracked
`docs/zenodo-changelog-fmt-v15.md`. Those are the FMT/NoC master, not RIM, and belong to a
concurrent session. **Do not sweep them into a RIM commit** without checking whose they are.
