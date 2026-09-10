<!-- Action: present -->
# PLR "Loops all the way up" — commentary deadline and cost

**Research-only agent output, 2026-08-24, WSL.** Nothing was submitted, no editor contacted, no
portal logged into. Companion to `~/social/docs/plr-loops-commentary-assessment-2026-08-21.md`
(which covers *whether* to write it; this covers *by when* and *for how much*).

---

## The two answers

**Deadline:** There is no published deadline — PLR's Guide for Authors does not contain the word
"deadline" or even the word "comment" — but across **209 measured PLR comment/target pairs** the
comment reaches the journal a median of **124 days** after the target goes online, and for
consciousness/neuroscience targets 90% arrive within **188 days**; against this paper's
2026-07-24 online date that puts the working deadline at **end of January 2027**, which is also
the earliest date any PLR commentary round has ever been closed by the authors' reply.

**Cost: €0.** PLR is a hybrid journal whose APC (EUR 4,110 / USD 4,510, Elsevier's own price list
dated 06-Aug-2026) is payable **only if the author elects open access** — and **every one of the
221 comments PLR published between 2018 and 2026 was published on the free subscription route,
with zero Creative Commons licences among them.**

---

# QUESTION 1 — THE DEADLINE

## 1.1 Is there a published deadline? No. (Verified)

I retrieved the full PLR Guide for Authors (60 KB) via a text proxy, since sciencedirect.com
returns 403 to direct fetching.
Source: <https://www.sciencedirect.com/journal/physics-of-life-reviews/publish/guide-for-authors>
(fetched through `r.jina.ai`).

Word-frequency check on the full text:

| term | occurrences |
|---|---|
| `deadline` | **0** |
| `Comment` | **0** |
| `commentar` | **0** |
| `article types` | **0** |

**The Guide for Authors does not mention comments at all.** No comment article type, no comment
policy, no length limit, no deadline. That is a verified negative, not a failure to find.

No call-for-commentaries page exists for this paper that I could locate. Anil Seth's 2026-08-15
statement that it is "open for peer commentary" remains the only signal that a round is open, and
it is third-party.

## 1.2 The empirical window (verified, computed from primary metadata)

**Method.** Pulled all 959 PLR works registered with Crossref since 2018 (ISSN 1571-0645), plus
PubMed history records for 949 of them (947 carry publisher-supplied `received` dates). Matched
comments to their targets by parsing the quoted target title out of the comment title
(PLR's format is `<Comment title>: Comment on "<Target title>" by <Authors>`), with a 0.85
similarity floor. Result: **214 comment→target pairs across 68 targets**, of which **209 pairs
also have a `received` date**, so the lead time can be measured from *submission*, not just from
publication. That distinction matters: it is the submission date the author has to hit.

### Target online → comment RECEIVED at the journal (n = 209, 67 targets)

| percentile | days | months | projected date for this paper |
|---|---|---|---|
| min observed | 7 | 0.2 | — |
| p05 | 48 | 1.6 | 2026-09-10 |
| p25 | 95 | 3.1 | 2026-10-27 |
| **p50 (median)** | **124** | **4.1** | **2026-11-25** |
| p75 | 180 | 5.9 | 2027-01-20 |
| p90 | 247 | 8.1 | 2027-03-28 |
| p95 | 290 | 9.5 | 2027-05-09 |
| max observed | 622 | 20.4 | — |

Cumulative share of comments submitted within N days of the target going online:

```
  30 d ( 1.0 mo):   6 / 209 =  3%
  60 d ( 2.0 mo):  18 / 209 =  9%
  90 d ( 3.0 mo):  41 / 209 = 20%
 120 d ( 3.9 mo):  99 / 209 = 47%
 150 d ( 4.9 mo): 126 / 209 = 60%
 180 d ( 5.9 mo): 157 / 209 = 75%
 240 d ( 7.9 mo): 185 / 209 = 89%
 300 d ( 9.9 mo): 201 / 209 = 96%
 365 d (12.0 mo): 207 / 209 = 99%
```

### Consciousness / neuroscience targets only (n = 80 comments, 25 targets)

Filtered to targets whose titles match `conscious|brain|neur|cogniti|mind|mental|percept|
predictive|psych|self`. This subset is **tighter**, which is the relevant one here:

| statistic | days | projected date |
|---|---|---|
| median | 117 | 2026-11-18 |
| p25 | 86 | 2026-10-18 |
| p75 | 159 | 2026-12-30 |
| **p90** | **188** | **2027-01-28** |
| max observed | 330 | 2027-06-19 |

Representative neuro targets and the span of their comment submissions:

| comments | target online | received between | target |
|---|---|---|---|
| 9 | 2023-07-05 | day 98 – 124 | A systematic framework of creative metacognition |
| 9 | 2024-12-05 | day 7 – 162 | The major-minor mode dichotomy in music perception |
| 8 | 2024-07-31 | day 51 – 160 | The affective grounds of the mind |
| 7 | 2025-02-07 | day 147 – 196 | Dark brain energy |
| 3 | 2025-01-07 | day 53 – 106 | The paradox of the self-studying brain |

### Publication-side figures (for completeness, n = 214)

Target online → comment online: median **132 d**, p75 188, p90 258, range 8–637.

## 1.3 The hard close: the authors' reply (verified)

There is no editorial deadline, but there is a **hard terminator**: once PLR publishes the target
authors' "Reply to comments on …", the round is over.

- **0 of 69** comments in the sample were *received* after their target's reply was published.
  (69 of 209 pairs belong to the 15 sampled targets that have a published reply.)
- Median gap from a comment being received to the reply appearing: **302 days**.
- Reply lead times (target online → reply online, n = 18): **earliest ever 189 d**, p25 343 d,
  median 460 d, max 894 d.

Applied to a 2026-07-24 target: the earliest this round could plausibly close is **2027-01-29**;
the median close would be **2027-10-27**.

## 1.4 Turnaround is fast — being early costs nothing (verified)

From PubMed publisher-supplied history dates (n = 209):

| interval | median | p75 | p90 | max |
|---|---|---|---|---|
| received → accepted | **2 days** | 6 | 8 | 47 |
| received → online | **6 days** | 9 | 14 | — |

A submitted comment is typically online within a week or two. There is no queue to beat and no
penalty for submitting early.

## 1.5 Nothing has been submitted on this paper yet (verified)

Every PLR item registered with Crossref between 2026-07-20 and 2026-08-22 (11 items) was checked.
**No comment on "Loops all the way up" exists yet.** The field is entirely open.

## 1.6 The recommendation

| horizon | date | rationale |
|---|---|---|
| Ideal submission | **by end of Nov 2026** | median of both the full and the neuro distributions |
| Working deadline | **31 Jan 2027** | covers 75% of all comments and ~90% of neuro comments; also the earliest date any round has ever closed |
| Absolute backstop | **~Mar 2027** | p90 overall; beyond this you are in the 10% tail and gambling that the reply has not been commissioned |

## 1.7 How comments are solicited — the prior assessment is CONFIRMED (verified)

PLR Guide for Authors, section **"Submission by invitation"**, verbatim:

> "In principle, papers are written and submitted on the invitation of one of the Editors,
> although the Editors would be glad to receive suggestions. Proposals for review articles
> (approximately 1000–2000 words) should be submitted via the EM system using the article type
> 'Review Proposal.' All submitted papers are subject to a refereeing process."

This **confirms** the assessment's conclusion that PLR commentaries are editor-solicited, and it
also **validates the recommended mitigation**: "the Editors would be glad to receive suggestions"
is the journal's own language. A short pitch to the handling editor is the documented route, not
a workaround.

Two caveats, stated plainly:

- ⚠️ That clause is written about **review articles**, and names a proposal article type
  ("Review Proposal") that is for reviews, not comments. The Guide is silent on comments
  entirely, so **there is no documented unsolicited-comment route and no documented invited one
  either.** *(Inference:* comments follow the same invitation norm — that is the journal's stated
  default for everything.)
- 📌 *(Inference, but a strong one:)* a **median received→accepted time of 2 days**, with several
  comments accepted the same day they arrived, is not consistent with cold submissions entering
  peer review. It is consistent with pre-arranged, editor-invited contributions being checked and
  waved through. This is the quantitative form of the assessment's "cold submission is the
  default-decline path" risk.

## 1.8 Editors and contact route (verified except where marked)

From the PLR editorial board page (retrieved via text proxy;
<https://www.sciencedirect.com/journal/physics-of-life-reviews/about/editorial-board>):

- **Editor-in-Chief: José F. Fontanari, PhD** — University of São Paulo, Institute of Physics of
  São Carlos, São Carlos 13566-590, Brazil. Fields: Biological Physics, Social Physics,
  Population Dynamics, Neural Networks, Artificial Intelligence, Artificial Life.
  Email **`fontanari@ifsc.usp.br`** *(verified from Europe PMC author metadata on his own
  papers, not from the journal page).*
- ⚠️ **Wikipedia is stale.** It still names Leonid Perlovsky as EiC. The board page lists him
  under "**Editor-in-Chief 2003–2024**". Do not address a pitch to Perlovsky.
- **Most likely handling editor** *(INFERENCE — not verified)*: Associate Editor
  **Prof. Cristina Becchio, PhD**, University Medical Center Hamburg-Eppendorf, Department of
  Neurology, Germany — the only Associate Editor whose listed specialism is **"Neuroscience"**.
  Email **`c.becchio@uke.de`** *(verified from Europe PMC open-access records, PMIDs 42150380 and
  39603216 — but her being the handling editor for this specific paper is my inference from field
  match alone).*
- Other neuro-adjacent board members: **Dipanjan Roy** (IIT Jodhpur — Computational/Cognitive
  Neuroscience), **Peng Ji** (Fudan — Brain-Inspired AI), **Jianfeng Zhang** (Shenzhen University
  — Cognitive Neuroscience, Brain-Body Interaction, Interoception, Neural Dynamics).
- ⚠️ **Possible recusal issue worth knowing about:** Jianfeng Zhang's listed fields
  (brain-body interaction, interoception, neural dynamics) sit squarely on the target paper's
  Box 3 territory, and *(inference)* he publishes with Georg Northoff, a target co-author. The
  Guide's recusal rule — editors do not decide on papers "written by family members or
  colleagues" — would apply to him, not to a commenter. Mentioned only so a pitch is not
  misaddressed.
- **Submission portal:** <https://www.editorialmanager.com/PLREV/default.aspx> (the journal's own
  "Submit your article" link). ⚠️ The lowercase `/plrev/` variant of that URL currently displays
  *"Site under development. Do not use for live manuscript submission."* — use the uppercase
  `PLREV` path the journal itself links to.
- Peer review model: single anonymised. Editors make the final decision. One appeal permitted.

---

# QUESTION 2 — THE COST

## 2.1 The answer: nothing

Publishing a comment in PLR on the normal (subscription) route costs **€0**. There is no
submission fee, and the APC is triggered only by electing open access — which no PLR comment has
ever done.

## 2.2 Journal model: hybrid (verified, three independent sources)

| source | finding |
|---|---|
| **Elsevier APC price list** (primary) | Business model: **"Hybrid Open Access"** |
| **OpenAlex** `sources/issn:1571-0645` | `is_oa: false`, `is_in_doaj: false` |
| **DOAJ API** | 0 results for ISSN 1571-0645 (not a DOAJ journal) |
| **OpenAPC** payment records | `is_hybrid = TRUE` |

## 2.3 The APC, exact figures (verified, primary source, 18 days old)

Elsevier's official **Article Publishing Charge (APC) price list**, downloaded as XLSX:

- File: <https://legacyfileshare.elsevier.com/els_com_pricing/article-publishing-charge.xlsx>
- Linked from: <https://www.elsevier.com/about/policies-and-standards/pricing>
- Header: *"Article Publishing Charge (APC) price list \* — All prices excluding taxes.
  **Prices as of date: 06-Aug-2026**"*
- Row 2482, verbatim:

| ISSN | Title | Business model | USD | EUR | GBP | JPY |
|---|---|---|---|---|---|---|
| 1571-0645 | Physics of Life Reviews | Hybrid Open Access | **4510** | **4110** | **3610** | **587340** |

⚠️ **Do not use the OpenAlex figures.** OpenAlex reports USD 4,720 / EUR 4,420 / GBP 3,780 /
JPY 585,420 for this journal — stale relative to Elsevier's own 06-Aug-2026 list. Where they
disagree, the Elsevier list wins.

For reference, actual APCs paid for PLR articles, from the OpenAPC dataset (all four are research
or review articles — **none is a comment**):

| payer | year | amount paid |
|---|---|---|
| Wellcome Trust | 2018 | €3,244.47 |
| Queen Mary, University of London | 2018 | €3,842.85 |
| UCL | 2019 | €3,108.83 |
| UCL | 2019 | €3,088.88 |

## 2.4 Does an APC apply to a COMMENT? No — this is the answer that matters

**(a) The APC is conditional on electing open access.** PLR Guide for Authors, verbatim:

> "**For open access articles**, all authors understand that they are responsible for payment of
> the article publishing charge (APC) if the manuscript is accepted. Payment of the APC may be
> covered by the corresponding author's institution, or the research funder."

Subscription-route publication carries no APC. That is the default and it is free.

**(b) Empirically, no PLR comment has ever been published open access.** I checked the Crossref
`license` field on every PLR item registered since 2018-01-01:

| category | n | carrying a Creative Commons licence |
|---|---|---|
| **Comments** (2018-08 → 2026-08) | **221** | **0** |
| **Author replies to comments** | **20** | **0** |
| Non-comment articles (since 2024 only) | 191 | 50 (26% — CC-BY 38, CC-BY-NC-ND 9, CC-BY-NC 3) |

Regular PLR articles go open access about a quarter of the time. **Comments never do — 0 for 221
across eight years.** Whatever the mechanism, the observed cost of publishing a comment in PLR is
zero, every time, without exception.

**(c) Corroboration that "Comment" is not even an OA-eligible article type at Elsevier.**
Elsevier's Austria agreement page enumerates the article types eligible for OA in hybrid journals,
verbatim:

> "Case reports, Data in Briefs, Full-length articles, Micro-articles, Original software
> publication, Practice guidelines, Protocols, Registered report articles, Registered report
> protocols, Review articles, Replication studies, Short communications, Short surveys, Video
> articles"

**Comment, Commentary, Correspondence, Letter to the Editor and Discussion are all absent.**
*(Inference:* the OA option, and therefore the APC, is probably not offered for comment-type
articles at all — which would explain the 0-for-221. The list itself is verified; the causal
reading is mine.)

## 2.5 Waivers and the Austrian question — does NOT apply to him

An Elsevier–**KEMÖ** (Kooperation E-Medien Österreich) read-and-publish agreement exists and does
cover hybrid journals. Source: <https://www.elsevier.com/open-access/agreements/austria>.

> "This agreement supports corresponding authors … affiliated with a participating Austrian
> institution." · "Eligible corresponding authors do not have to pay an article publishing charge
> (APC)." · Acceptance date must fall between 1 January 2024 and 31 December 2026.

**It does not apply here, for four independent reasons — any one of which is sufficient:**

1. **No qualifying affiliation.** KEMÖ is a consortium of Austrian *academic libraries*. He is
   submitting as an independent researcher under his own name and personal email.
2. **Affiliation is judged on the corresponding author only.** PLR Guide for Authors, verbatim:
   *"Only the corresponding author's affiliation will be used to determine eligibility for a
   publishing agreement, and possible discounts related to it. Affiliations of other co-authors
   are not relevant for eligibility."*
3. **Comment is not an eligible article type** under the agreement (§2.4c above).
4. **The acceptance window closes 2026-12-31.** A comment accepted in 2027 falls outside it
   regardless, unless the agreement is renewed.

⚠️ Do not let an Ivoclar affiliation be used to claim this. It is a Liechtenstein/Austrian
*company*, not a KEMÖ academic member, and using a corporate affiliation to reach for an academic
consortium waiver on a paper published under his own name would be both ineffective and a bad
look. **The subscription route is free, so there is nothing to waive.**

## 2.6 What the free route costs him in non-money terms

- The comment will be **paywalled and not CC-licensed** — he cannot host the version of record on
  his own site, unlike the target article (which is CC-BY).
- Optional paper offprints carry an extra charge (Guide for Authors, "Offprints"). Ignore.
- No submission fee is mentioned anywhere in the Guide. *(Elsevier distinguishes submission fees
  from APCs and only a handful of journals levy one; PLR shows no sign of doing so — verified
  absence in the Guide, not a positive confirmation.)*

---

# What I could NOT establish

Stated plainly rather than hedged:

1. **Whether this specific commentary round has a formal call, an invitation list, or an
   editor-set deadline.** Seth's Bluesky remark is the only evidence a round is open, and he is
   not a PLR editor. Nothing on the journal side announces it.
2. **Who the handling editor for this paper is.** Becchio is my inference from being the only
   Associate Editor whose listed field is Neuroscience. Not verified.
3. **Whether PLR will accept an unsolicited comment at all.** The Guide documents invitation as
   the norm and says nothing about comments. The 2-day median acceptance time argues the pipeline
   is invited. Neither confirms nor rules out a cold route.
4. **Whether comment-type articles are formally barred from the OA option**, as opposed to nobody
   ever choosing it. The 0-for-221 record is decisive about the *outcome*; the *mechanism* is my
   inference from Elsevier's article-type list.
5. **The self-archiving embargo** for posting the accepted manuscript. The Guide contains zero
   occurrences of "embargo" and Sherpa Romeo returned 403 to automated fetching. Unresolved.
6. **Any word limit for a PLR comment.** Not published. Would have to be asked. *(Observationally,
   published PLR comments run roughly 2–5 pages — not measured, an impression from the corpus.)*

**Blocked sources, for the record:** sciencedirect.com returns 403 to direct fetching and serves a
CAPTCHA through a text proxy for most paths (the Guide for Authors and editorial board pages came
through because they were proxy-cached); v2.sherpa.ac.uk returns 403.

---

# Method and reproducibility

Working files are in `tmp/plr-research/` (throwaway):

| file | contents |
|---|---|
| `plr_a.json` | 959 PLR works from Crossref, 2018-01-01 onward |
| `pubmed_hist.json` | PubMed `received`/`accepted` history for 949 PLR articles |
| `pairs.json` | 214 comment→target pairs, publication-date lead times |
| `rows.json` | 209 pairs enriched with submission dates |
| `apc.xlsx` | Elsevier official APC price list, 06-Aug-2026 |
| `gfa.txt`, `eb.txt` | PLR Guide for Authors, editorial board (proxy-fetched) |
| `match.py`, `final.py`, `stats2.py`, `pmall.py` | the analysis |

**Endpoints used:** Crossref REST (`api.crossref.org`), NCBI E-utilities
(`eutils.ncbi.nlm.nih.gov`), Europe PMC (`ebi.ac.uk/europepmc`), OpenAlex (`api.openalex.org`),
DOAJ (`doaj.org/api`), OpenAPC (`raw.githubusercontent.com/OpenAPC/openapc-de`),
Elsevier (`elsevier.com`, `legacyfileshare.elsevier.com`).

**Known limits of the measurement.** Crossref `created` is the DOI registration timestamp, which
for Elsevier tracks online-first publication but is not identical to it (typically within a day).
Title-based matching with a 0.85 floor recovered 214 of 235 non-reply comments; the 21 misses are
comments whose titles carry no parseable quoted target title, and there is no reason to think
they are biased in time. Comments in the last few weeks of the window are under-counted, since a
comment submitted recently may not be registered yet — this biases the measured distribution
slightly *early*, i.e. the real window is if anything marginally longer than reported.
