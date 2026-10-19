<!-- Action: await-user-decision -->

# NoC word ceiling — ground truth from the journal, and where our two numbers came from

**Investigated 2026-08-24.** Evidence for closing the tracking conflict flagged in `AIW-235`.
**Nothing was reconciled.** Neither `journal-guidelines-noc.md` nor
`four-model-theory-noc.formatting-rules.md` was edited. This file is the evidence; the call is MG's.

---

## Verdict in one sentence

The paper has always been submitted to NoC as a **Review Article**, whose limit is **10,000 words**;
its real body is **~9,080 words**, so it is **comfortably inside the limit** — the "10,073" is a
`wc -w` artifact that counts markdown syntax and the title page, and the only genuine mechanical
breach is the **abstract at 277 words against a 250 maximum**.

---

## 1. What the journal actually says (retrieved 2026-08-24)

Two OUP pages carry the article-type limits, in identical wording.

**Source A — https://academic.oup.com/nc/pages/General_Instructions** (retrieved 2026-08-24)
**Source B — https://academic.oup.com/nc/pages/author-guidelines** (retrieved 2026-08-24)

Verbatim, from the *Article Types* section:

> "*Research Article:* Report on important original research relevant to the scope of *Neuroscience
> of Consciousness*, **not normally more than 9,000 words**, with a max. 250 word abstract."

> "*Review Article:* Provide a formal systematic review of recent progress in a particular field
> relevant to *Neuroscience of Consciousness*. Submission **should not normally exceed 10,000 words**,
> with a max. 250 word abstract."

> "*Rapid Communications:* Short articles, **not normally exceeding 3,000 words** (with a max. 250
> word abstract.), presenting timely, original empirical research meriting accelerated publication."

> "*Spotlight Commentary:* Short articles, **max. 1,500 words**, with a max. 100 word abstract,
> providing an informed opinion on specific high profile recent research."

Also present, and **absent from our stored copy**: *Registered Reports* (Stage 1 ≤ 7,000; Stage 2
"should not normally exceed 9,000") and *Methods and Resources Articles* ("should not normally
exceed 7,000 words").

The *Basic Formatting Guide* section repeats the same four headline numbers in a table
(Research 9,000 / Review 10,000 / Rapid 3,000 + 20 refs / Spotlight 1,500 + 10 refs). Our stored
file's table reproduces that table faithfully.

### Answer to Q1 — which type, and what limit

NoC has **no** Opinion, Perspective, Position, Theoretical or Brief Communication type in its
standing article list. A ~10,000-word theory paper has exactly two homes, and the journal
explicitly opens the *Research Article* door to non-empirical work:

> "Original research can be experimental, **theoretical**, conceptual, or methodological in nature."
> — Article Types → Research Article, https://academic.oup.com/nc/pages/author-guidelines,
> retrieved 2026-08-24

So on the journal's own terms both are available:
- **Research Article — 9,000** (theory explicitly admitted)
- **Review Article — 10,000** (but described as "a *formal systematic review*", which this paper is not)

**And the record says this paper has always gone in as a Review Article.** Two on-disk artifacts,
both from the actual submissions:

- `paper/trimmed/noc/SUBMISSION-CHECKLIST.md:4` — `**Article type**: Review Article`, repeated at
  line 43 (ScholarOne form field) and line 57 (`3. Select "Review Article"`). Line 11 records the
  pre-flight check as `**Word count**: 9,176 body words (limit: 10,000)`.
- `correspondence/cover-letter-noc.md:7` — "…for consideration as a **Review Article** in
  *Neuroscience of Consciousness*." This is the cover letter used for submission #2
  (NCONSC-2026-071).

**⚠ Do not confuse this with the 2026-07-30 MG decision.** `docs/session-log.md:882` records
"Art-type=Research Article" — that ruling is about the **AIW-130 NoC slice**
(`drafts/aiw130-noc-draft.md`, 6,247 body words, for the Pinto/Doerig/Dołęga special issue), a
different and much shorter manuscript. It does **not** retype the trimmed FMT paper.

### Answer to Q2 — what the limit counts: **the journal does not say**

Checked three times against the live pages, including a literal yes/no pass:

- Do "excluding" / "exclusive of" / "including" / "inclusive of" / "not including" appear anywhere
  in connection with a word count? **No.**
- Does either page define what counts toward the limit? **No.** Neither abstract, references,
  figure legends, tables, footnotes nor acknowledgements are mentioned as in or out.

A web-search snippet rendered the Research Article line as "…9,000 words, **excluding references**".
**That phrase is not on the page** — it is the search summariser's inference. The only OUP page that
might once have carried different wording, `https://academic.oup.com/nc/pages/Instructions_To_Authors`,
now returns **HTTP 404**. (Direct `curl` of the live pages returns a 5.7 KB JS/Cloudflare shell, so
the WebFetch renderings above are the usable evidence; two independently-prompted passes agreed.)

**Consequence:** there is no journal rule that makes our body-only figure the wrong measurement, and
none that makes it the right one either. The plain reading of "a 9,000-word article" in a journal
that separately caps the abstract at 250 is *main text*. Our body-only count is the defensible
number, and it is the conservative one to plan against.

### Answer to Q3 — hard or advisory: **advisory, and softly worded**

Every long-form type uses **"not normally more than"** / **"should not normally exceed"**. The short
types switch to the harder **"max."** — and note the abstract cap is also **"max. 250 word abstract"**,
i.e. the abstract is worded *more strictly than the body*.

Neither page says anywhere that over-length manuscripts are returned, unsubmitted, or rejected. No
such consequence is stated for length at all.

This is corroborated by our own history: the paper has been bounced by NoC twice, and **neither
rejection mentioned length**. Per `backlog.md:9`, the NCONSC-2026-071 grounds were "(1) definition
departs from standard, (2) predictions too general, (3) REM sleep assumption wrong, (4) needs
stronger integration with existing theories." The one time NoC did bounce us mechanically it was
*unsubmission*, not rejection, and it was for format — PDF-only and missing highlights
(`docs/conversation-log.md:3992`), then dropped tables (`docs/session-log.md:3464`). **Length has
never been the mechanism that failed.** Format has, twice.

---

## 2. Answer to Q4 — provenance of our two numbers

| | `journal-guidelines-noc.md` | `four-model-theory-noc.formatting-rules.md` |
|---|---|---|
| Number | 9,000 (Research Article row) | 9,500 ("Body word limit") |
| Created | commit `83276911`, **2026-03-04** (S134) | commit `4903e782`, **2026-02-19** (S72) |
| Cites a source? | **Yes** — `Source: …/General_Instructions`, `Retrieved: 2026-03-04` | **No.** No source, no date, no journal reference |
| Verdict | **Accurate and still current** | **Unsourced. Matches no NoC article type.** |

**The 9,000 is not stale and not wrong** — I re-verified it against the live page today, 2026-08-24,
and the wording is unchanged from the 2026-03-04 retrieval. What is wrong is the *row being read*:
9,000 is the **Research Article** limit, and `journal-guidelines-noc.md:20` **also** carries
`| Review Article | 10,000 | 250 | n/a |`. The file is not in conflict with the journal at all.

**⚠ `AIW-235` mis-cites this file.** The backlog entry says the ceiling is "**9,000** in
`paper/trimmed/noc/journal-guidelines-noc.md`". The file states a *table of all types*, not a
ceiling for this paper — and the row matching this paper's actual submitted type says **10,000**.
Half the "conflict" is a wrong-row reading, not a data disagreement.

**Where 9,500 plausibly came from.** It matches no NoC limit — not 9,000, not 10,000, not 7,000 or
3,000. It was written on **2026-02-19**, six days after the 2026-02-13 submission that recorded
"9,176 body words (limit: 10,000)". The reconstruction that fits the dates and the arithmetic: it is
a **self-imposed working ceiling** — 9,176 actual, rounded up to a round number, with ~800 words of
deliberate headroom under the real 10,000 — set during a Session-72 infrastructure sweep
("skills, formatting rules, review tool, cleanup") that created the file wholesale. It is a
*drafting budget*, not a journal fact, and nothing in the file ever said otherwise. It is neither a
different article type nor an abstract-excluded variant.

---

## 3. Answer to the measurement question — I counted it myself

**The 10,073 does not measure the body.** Its rule is recorded at
`docs/reviews/2026-08-24-noc-repairs.md:130` — "body (everything before the `References` heading)".
I reproduced it exactly:

```
sed -n '1,546p' four-model-theory-noc.md | wc -w   →   10073
```

That figure is inflated two ways at once:
1. **Raw `wc -w` on markdown** counts `**`, `|`, `##`, `###`, `---` and table separator rows as words.
2. **"Everything before References"** sweeps in the title, byline, ORCID, correspondence line, the
   292-word abstract block, the keywords line, and all five end-matter sections (Acknowledgments,
   Data Availability, Funding, Conflict of Interest, Author Contributions).

Neither is a thing the journal would measure.

### What I measured

Markdown stripped (emphasis, table pipes, heading marks, link syntax, bullets, rules); tokens
counted only if they contain an alphanumeric, so stray em-dashes don't inflate. Body = line 21
(`## 1. Introduction`) through line 516 (end of `## 11. Conclusion`), i.e. §1–§11.
Cross-checked independently by rendering the same span through `pandoc -t plain` and counting that.

| Segment | Words |
|---|---:|
| **Body §1–§11, prose only** (no tables, no figure/table captions) | **8,767** |
| Body + figure/table captions and alt text | 8,837 |
| **Body §1–§11 entire, incl. tables + captions** | **9,080** |
| — of which tables | 243 |
| — of which captions + alt text | 70 |
| — of which footnote definitions | 47 |
| Abstract | 277 |
| Front matter (title, byline, ORCID, correspondence, keywords) | 24 |
| End matter (Ack / Data Avail / Funding / COI / Contributions) | 111 |
| References section (104 entries) | 1,803 |
| Whole file | 11,311 |

Independent pandoc cross-check of the same §1–§11 span: **9,007** (alnum-filtered) / 9,313
(whitespace tokens). My regex path gives 9,080. The two methods agree to within 0.8%.

**Take the body as ~9,080 words** — the higher, conservative figure, tables and captions included.
Under a Word-style count that also tallies standalone punctuation it is 9,404; the true figure sits
in the **9,000–9,400** band on any reasonable rule.

---

## 4. 🟢 The paper is INSIDE the limit — this changes the plan

**As a Review Article — the type it has actually been submitted under, twice — the limit is 10,000
and the body is ~9,080. That is ~920 words of headroom. No trim is required.**

Even the maximal defensible reading — body + abstract + end matter, i.e. *everything except the
title page and the references* — is **9,507**, still under 10,000.

The overage that `AIW-235` reports is an artifact of measuring markdown with `wc -w` against the
wrong article type's row. **There is no length problem to solve.**

If MG instead retypes the paper to **Research Article** (9,000, and the more honest label — this is
a theory paper, not "a formal systematic review", and the journal explicitly admits theoretical work
as original research), then:

- body incl. tables/captions **9,080 → 80 words over**, on an explicitly advisory
  "not normally more than";
- body prose only **8,767 → 233 words under**.

That is a rounding error against a soft ceiling, not a desk-reject risk — and length has never been
the thing NoC bounced us for. A one-paragraph tightening covers it if MG wants the number clean.

---

## 5. ⚠ The real mechanical exposure is the ABSTRACT, not the body

**The abstract is 277 words against a stated "max. 250 word abstract" — 27 over (285 / 35 over on a
Word-style count).** It is worded with the hard "max.", not the soft "not normally", and it applies
identically to Research and Review Articles, so **no choice of article type fixes it**.

This has regressed since submission #1: `SUBMISSION-CHECKLIST.md:11-12` recorded
`**Abstract**: 236 words (limit: 250)` as a passing check. It has since grown by ~41 words.

For a paper that has already been *unsubmitted once* on a mechanical formatting fault and
desk-rejected twice, this is the item that can fail a third submission on a technicality. It is
~27 words of cutting.

---

## 6. Recommendation — for MG's decision, not applied

Both files are individually defensible; the conflict is between **9,500 as a private drafting
budget** and **9,000/10,000 as journal facts**, and it exists because one file doesn't say which it is.

1. **`journal-guidelines-noc.md` — change nothing about the numbers.** Re-verified accurate against
   the live pages on 2026-08-24; bump `Retrieved:` to reflect that. Optionally add the three missing
   types (Registered Reports Stage 1 ≤7,000 / Stage 2 ≤9,000; Methods and Resources ≤7,000), and a
   one-line note that OUP **does not state** what the count includes and uses advisory
   "not normally exceed" wording.
2. **`four-model-theory-noc.formatting-rules.md` — the 9,500 should stop presenting itself as a
   journal limit.** Either relabel it as what the evidence says it is (a self-imposed drafting
   budget with headroom) or replace it with the governing figure once MG fixes the article type.
   It should also name the type, since the type *is* the limit.
3. **MG's actual decision is not a number, it's the article type**: keep **Review Article** (10,000,
   ~920 words of headroom, consistent with both prior submissions and the cover letter) or switch to
   **Research Article** (9,000, ~80 over on the inclusive count, the more honest label for a theory
   paper). Everything else follows.
4. **Correct `AIW-235`'s citation** of `journal-guidelines-noc.md` — it reads the Research Article
   row as though it were this paper's ceiling; the file's Review Article row says 10,000.
5. **Open a separate item for the 277-word abstract.** That is the live mechanical risk, and it is
   independent of how the body question is settled.

---

## Sources

- https://academic.oup.com/nc/pages/General_Instructions — retrieved 2026-08-24
- https://academic.oup.com/nc/pages/author-guidelines — retrieved 2026-08-24
- https://academic.oup.com/nc/pages/Instructions_To_Authors — **HTTP 404**, checked 2026-08-24
- On-disk: `paper/trimmed/noc/SUBMISSION-CHECKLIST.md`, `correspondence/cover-letter-noc.md`,
  `docs/reviews/2026-08-24-noc-repairs.md:130`, `docs/noc-si-cfp-2026.md`,
  `docs/session-log.md:882`, `backlog.md:9`
