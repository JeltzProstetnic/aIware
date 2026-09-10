# AIW-223 / AIW-224 — Known-human control corpus inventory

**Compiled:** 2026-08-23 · **Scope:** certainly-pre-LLM prose written by Matthias Gruber, for
calibrating a personal false-positive rate on the local Binoculars harness.
**Status:** inventory only. Nothing extracted, nothing moved, nothing committed.

**Dating rule used throughout:** file mtimes are worthless here (the FMS estate was bulk-ingested
in 2026, so 2007 documents carry 2026 mtimes, and the 2018 novel carries 2025 mtimes). Every date
below comes from **document-internal metadata** — OOXML `docProps/core.xml`
(`dcterms:created` / `dcterms:modified` / `cp:revision`), ODF `meta.xml`, PDF `creationDate` +
producer version, or a printed copyright/ISBN line — cross-checked against each other.

Grades: **CERTAIN** = internal metadata and/or publication record puts it pre-2022 beyond doubt.
**LIKELY** = strong circumstantial evidence, no single decisive artifact. **UNVERIFIED** = cannot
date from content.

---

## 0. ⛔ Contamination hazards — read this first

Three traps found. Each would silently poison the baseline.

| Hazard | Detail |
|---|---|
| **`sources/book-2015/Definition of Basic Consciousness.docx` is POST-LLM** | `dcterms:created` **2023-04-26**, modified 2023-04-27, `dc:creator` = `Gruber, Matthias` (corporate `Surname, Firstname` form = Ivoclar workstation). 3,864 words. It sits in a folder named for 2015 and is currently listed under `control-en-unverified`. **It must never enter `control-en`.** The quarantine was right; the reason recorded was wrong. |
| **`~/scifi/manuscripts/*.md` and `~/scifi/translations/**` are LLM-edited** | Git history of that repo: `Session 3: First-pass shortening of all 4 books (-16.7K words)`, `BYC English polish pass: 64 mechanical fixes`, `Session 6: BYC structural edit — 20 of 22 edits, +1,071 words`, plus subagent-produced `band{1,2,3}-english.md`. This applies to **both** the German and the English markdown. ⛔ Never source control text from `~/scifi/manuscripts/` or `~/scifi/translations/`. |
| **`~/scifi/source/` is clean, but only by luck** | `source/band{1,2,3}.txt` and `source/billion-year-countdown/*.txt` were committed once at project setup and only ever *moved* since (`git log` shows two commits, both structural). They are raw extractions of the 2017–2018 originals. Safe — but prefer the FMS `.docx` originals, which carry the metadata that proves the date. |

Also worth stating plainly: **`The Billion Year Countdown` files carry 2025 mtimes** (`.txt` 2025-05-27,
`.pdf` 2025-07-14). Those are re-copies. The document itself is 2016–2018 — see below.

---

## A. English — the corpus that actually matters

Ranked best-first. All sole-authored by MG unless stated.

### A1. ★ The Billion Year Countdown — novel — **42,010 words** — CERTAIN
- **Canonical source:** `/mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx`
  (identical copy at `.../Creative/scifi-billion-year-countdown/_X2/`)
- **Also:** `/mnt/wsl/data8tb/__FMS__/Creative/_Roman/The Billion Year Countdown.pdf` (188pp) ·
  `/mnt/nas/__FMS__/Creative/scifi-billion-year-countdown/` · `/home/jeltz/scifi/source/billion-year-countdown/`
- **Date evidence:** docx `dcterms:created` **2016-10-28T16:05**, `dcterms:modified` **2018-08-05T15:50**,
  `cp:revision` **1947**, `cp:lastPrinted` 2018-08-05. PDF `creationDate` **D:20180805174037+02'00'`,
  producer `PDFCreator 3.1.2.10844` + `iTextSharp 5.5.12 ©2000-2017` (both 2017/2018-era builds).
  `dc:creator` = `Matthias Gruber`.
- **Purity:** pure narrative fiction, sole-authored, no quotation, no boilerplate. **The single best item.**
- ⚠ Extract from the **2018 `.docx` or `.pdf`**, never from `~/scifi/manuscripts/byc.md` (LLM-edited).

### A2. ★ Eight Pattern Wing Chun Kuen — *Theory and formal exercises* — **39,900 words** — CERTAIN
- **Path:** `/mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx`
  (paperback variant alongside, same text)
- **Date evidence:** docx modified **2011-06-13T22:00**; title page reads `by Matthias Gruber` and
  `© 2011 Matthias Gruber. All rights reserved. ISBN: 978-1-4476-7964-6` (published, verifiable).
- **Purity:** sole byline. Instructional non-fiction — expect a meaningful fraction of the word count
  to be TOC entries, technique names, figure captions and tables. Budget ~65–70% running prose.
- **Note on the original-vs-translation question:** the EN docx was finished 2011-06-13 and the DE
  docx 2011-09-24, both branched from the same template on 2011-05-30 → **English was written first**,
  so this is original English, not translated German.
- ⚠ **Do not pool with A2b.**

### A2b. 8PWC Kung Fu — 2nd Edition (EN) — **53,425 words** (Word's count) — CERTAIN — *alternative to A2, not additional*
- **Path:** `.../8PWC BLACK BOOK/2nd Edition/8PWC.hardcover.en.2.Edition.docx`
- **Date evidence:** docx modified **2013-12-19T07:45**; same ISBN/© line as A2.
- ⚠ **Measured: A2b's body text is the same text as A2.** Both walk to 909 body paragraphs, and
  running-prose counts come out at **29,514 (A2b) vs 29,523 (A2)** — a 9-word difference. Word's
  higher `Words` figure for A2b (53,425 vs 39,900) is text-box/table content outside the body flow,
  not new prose. **Pick A2 *or* A2b, never both**, or the same sentences get scored twice and the
  resulting flag rate is fiction.

### A3. ★ Eight Pattern Wing Chun — *Safety and Security* — **19,880 words** — CERTAIN
- **Path:** `/mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx`
- **Date evidence:** docx `created` **2012-06-09T14:34**, `modified` **2013-12-24T00:13**,
  `dc:creator` = `Matthias Gruber`; text opens `© 2012 Matthias Gruber`.
- **Purity:** continuous expository English prose, sole-authored, unpublished manuscript. Very clean —
  **the best-quality English prose after the novel** (essay register, few captions).
- ⚠ Its folder also holds third-party PDFs (CIA/US-Army manuals). Take **only `8PWCS.docx`**.

### A4. PhD thesis — *Discrete Simulation Based Optimization* (TU Wien) — **27,836 words** — CERTAIN
- **Path:** `/mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx`
  (PDF: `/mnt/c/Dropbox/DMS-Sync/Academic/ACA-002_PhD-Thesis-Discrete-Simulation-TU-Wien.pdf`, 94pp)
- **Date evidence:** docx created/modified **2016-04-01**; the sibling `Dissertation.Full.odt` carries
  ODF `meta:creation-date` **2009-04-16T11:32** with `editing-duration` PT90H10M32S. Published
  ISBN 978-3838152233; doctorate at TU Wien 2010. Language check: 6,837 EN function-word hits vs 11 DE.
- **Purity:** his own academic English, but contains a literature review, equations, tables and a
  reference list. The harness already strips maths/citations/bibliography — still, expect real yield
  well below the raw count.
- ⚠ **Register caveat:** this is exactly the "rigorous, low-perplexity academic prose" that MG's own
  hypothesis is about. Keep it in its **own sub-corpus** so an academic-register FPR can be read
  separately from a narrative one. That comparison is arguably the most interesting number available.

### A5. SiRO Simulation Tutorial — **3,709 words** — CERTAIN
- **Path:** `/mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/SQSSTutorial.odt`
- **Date evidence:** ODF `meta:creation-date` **2009-07-19T22:29**, `dc:date` 2009-07-22,
  `dc:language` **en-US**, generator OpenOffice.org 3.1; text reads `© 2009 Matthias Gruber, PROFACTOR GmbH`.
- **Purity:** technical tutorial, sole-authored, but interleaved with C# code and step lists. Low yield.

### A6. Holomatic Self Model Theory — **1,657 words** — CERTAIN *(re-graded from UNVERIFIED)*
- **Path:** `/home/jeltz/aIware/sources/book-2015/Holomatic Self Model Theory.docx`
- **Date evidence:** docx `created` **2014-11-10T11:19**, `modified` **2014-12-04T15:19**, `rev` 28,
  `dc:creator` = `Matthias Gruber`. **This resolves half of the `control-en-unverified` quarantine.**
- **Action:** promote to `control-en`; **drop its file-mate** (see §0 — the other one is 2023).

### A7. — co-authored, include only with a flag
| Item | Words | Date | Authorship |
|---|---|---|---|
| IEEE LINDI 2011, *Practical Token Retrieval and Indexing from Binary Data* — `/mnt/c/Dropbox/DMS-Sync/Academic/ACA-010_CAD-Token-Retrieval-IEEE-LINDI-2011.pdf` | ~3,093 | CERTAIN — PDF `creator` = `Certified by IEEE PDFeXpress at 08/04/2011` | **M. Gruber first author**, + R. Geschray, C. Hillbrand |
| IEEE CIG 2006, *Using Wearable Sensors…* — `.../ACA-006_Wearable-Sensors-IEEE-CIG-2006.pdf` | ~3,315 | CERTAIN — TeX PDF `creationDate` 2006-03-27 | **5 authors, MG is third.** ⛔ Recommend exclude. |

### English totals — measured, not estimated

Two columns. **Nominal** = the word count the authoring tool records. **Running prose** = words
living in body paragraphs of ≥15 words, measured directly with `python-docx` / ODF paragraph walk —
this excludes headings, TOC lines, technique names, table cells, captions, code and equation lines,
and is the honest figure for what a style detector can actually chew on.

| # | Item | Nominal | Running prose | Density |
|---|---|---|---|---|
| A1 | The Billion Year Countdown | 42,010 | **46,773** | 96% |
| A2 | 8PWC Kuen (EN, 1st ed) | 39,900 | **29,523** | 97% |
| A3 | 8PWC Safety and Security | 19,880 | **22,801** | 95% |
| A4 | PhD thesis (TU Wien) | 27,836 | **23,174** | 87% |
| A5 | SiRO Simulation Tutorial | 3,709 | **2,482** | 65% |
| A6 | Holomatic Self Model Theory | 1,657 | **1,647** | 97% |
| | **Total (sole-authored, non-overlapping)** | 134,992 | **126,400** | |
| | …narrative/essay register (A1+A2+A3) | | **99,097** | |
| | …academic/technical register (A4+A5+A6) | | **27,303** | |
| A7 | co-authored, if admitted | 6,408 | ~5,500 | |

*(A1 and A3 measure* higher *than the nominal count because the tool-recorded `Words` field is a
stale 2018/2013 save value and tokenises hyphenation and contractions differently. A2 and A4 measure*
lower *because their nominal counts include text-box and table content outside the body flow.)*

**Headline (B):** ≈ **126,400 words of certainly-pre-2022, sole-authored, running English prose.**

At `corpora.json`'s 320-word default that is ≈ **395 chunks**, resolving a flag rate down to about
**0.25%** — well past the ~30k/90-chunk floor the slot's own notes call the minimum, and enough to
state a defensible personal false-positive rate for an English submission. It still cannot confirm
Binoculars' published 0.01% low-FPR threshold; nothing of this size can, and the report should keep
saying exactly that.

---

## B. German — abundant, and much of it new

The existing control is the 2015 monograph alone. There is roughly **five times** that available.

| # | Item | Words | Path (canonical) | Date evidence | Grade |
|---|---|---|---|---|---|
| G1 | *Ringe des Lebens* **Band 1** | 136,991 | `/mnt/wsl/data8tb/__FMS__/Creative/_Roman/Band 1 korrigiert.docx` | created 2017-12-19, modified 2018-01-10; Lulu ID 22274168; ISBN barcode PDF 2017-12-19 | CERTAIN |
| G2 | *Ringe des Lebens* **Band 2** | 120,757 | `.../Band 2 korrigiert.docx` | created/modified 2018-01-13; Lulu 22274328 | CERTAIN |
| G3 | *Ringe des Lebens* **Band 3** | 99,657 | `.../Band 3 korrigiert.docx` | created 2016-10-28, modified 2018-03-04, rev 1933; Lulu 22274333 | CERTAIN |
| G4 | *Die Emergenz des Bewusstseins* (2015 monograph) | 96,948 (docx) / 89,442 (PDF text) | `/home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9.docx` | docx created 2016-05-11; earlier drafts in `alt/` created **2014-10-02**; ISBN 978-1-326-65207-4 | CERTAIN — **already the `control` corpus** |
| G5 | 8PWC Kuen (German edition) | 41,874 | `.../8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.de.docx` | modified 2011-09-24 | CERTAIN |
| G6 | *Die Geheimnisse der Großmeister: Wing Chun im Überlebenskampf* | 28,067 | `/mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC RED BOOK/Die Geheimnisse der Großmeister.docx` | created 2013-05-29, modified **2020-08-03**, rev 219; byline `Matthias Gruber`, `2020` | CERTAIN |
| G7 | *Future Spinoffs / Noch Älter* — 9 short stories + timelines | ~26,800 | `/mnt/wsl/data8tb/__FMS__/Creative/_Roman/Future Spinoffs/Noch Älter/*.odt` | ODF `dc:date` **2007-12-01 → 2008-01-27**, per-file `meta:word-count` | CERTAIN |
| G8 | MSc thesis — *Modulare Delta Algorithmen* (UMIT) | ~17,341 | `/mnt/c/Dropbox/DMS-Sync/Academic/ACA-001_MSc-Thesis-Modulare-Delta-Algorithmen.pdf` | PDF `creationDate` **2007-06-11**, author `Matthias`; ISBN 978-3-639-22928-8; Dipl.-Ing. conferred 2007-06-28 | CERTAIN |
| G9 | *Stories.docx* (spinoff outlines/prose) | 6,414 | `.../Future Spinoffs/Stories.docx` | created 2014-09-01, modified 2014-09-11 | CERTAIN |
| G10 | *Selbstselektion in der Forschung* (essay) | 2,649 | `/mnt/c/Dropbox/DMS-Sync/Academic/ACA-013_Selbstselektion-Forschung.docx` | created/modified **2014-11-04** | CERTAIN |
| G11 | *Erwachen.docx* | 1,877 | `.../Future Spinoffs/Erwachen.docx` | created 2015-03-07, modified 2015-03-09 | CERTAIN |
| G12 | *Schlaf.docx* | 1,022 | `.../Future Spinoffs/Schlaf.docx` | created/modified 2016-10-25 | CERTAIN |

**Co-authored German — flag, do not pool silently:**

| Item | Words | Date | Note |
|---|---|---|---|
| *Schlüsselprinzipien des Acht Pattern Wing Chun* | 48,688 | modified 2013-11-28 | Byline **DI Matthias Gruber + Dr. Sylvia Gruber**. Second author throughout. |
| ASIM 2009 *Evaluierung und Analyse … Simulations Engines* — `.../ACA-007_Anticipatory-Production-Control-Springer-2010.pdf` | ~2,660 | PDF creationDate 2009-09-26 | **Markus Speckle first author**, MG second. (PDF `author` field says `FG Regelungstechnik, Uni Paderborn` — that is the conference *template*, not the writer.) |

**Headline (C):** ≈ **580,400 words of certainly-pre-2022 sole-authored German** (G1–G12 summed),
of which ≈ **483,400 are new** (everything except the 2015 monograph already in `control`). Even at heavy
attrition this is >1,500 chunks — German FPR could be resolved to well under 0.1%.

⚠ Binoculars is English-tuned; more German does not substitute for English. Its value is
(a) tightening the *existing* German baseline, and (b) letting a German-vs-English FPR gap be
measured rather than assumed.

**Excluded German — do not use:**
- *Key Principles* English edition (see A-section note) — translated from the German and co-authored.
- `Matthias/Life.docx` (6,023 "words", 2013) — a chronological life-log skeleton of bare month and
  year headings, not prose. `/mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/Matthias/Life.docx`.
- `sustainable leadership in an agile environment.docx` — 115 words. Too small to matter.

---

## C. (D) What "the billion years countdown book" turned out to be

**Answer:** *The Billion Year Countdown* — a **188-page English science-fiction novel, ~42,000 words**,
sole-authored by MG. It is the standalone sequel to his German *Ringe des Lebens* trilogy, written
in English rather than German. Drafted from **2016-10-28**, finished and typeset **2018-08-05**
(1,947 Word revisions between those dates), self-published via Lulu alongside the trilogy.
Catalogued as DMS `CRE-005`, previously carrying `[unknown-date]`.

It is **the strongest single item in this whole inventory** — long, English, pure narrative prose,
sole-authored, and datable three independent ways (docx metadata, PDF producer-version metadata,
and the Lulu/trilogy publication context).

The DMS catalogue's `[unknown-date]` on `CRE-003` and `CRE-005` can now be filled in: trilogy
2016–2018, sequel 2016–2018.

---

## D. (E) Gmail — what is there and how to get it

**Account:** `jeltz.prostetnic@gmail.com` (also receives the `matthias@matthiasgruber.com` alias,
which is what most pre-2022 mail was *sent as*). All probing this pass was **read-only search**;
nothing sent, drafted, labelled, moved or deleted.

**Date range:** sent mail reaches back to at least **2010-01-07**. Continuous coverage 2010 → present.

**Volume:** a probe for original compositions (`in:sent before:2022/01/01` minus `Re:`/`Fwd:`/`Fw:`/
`AW:`/`WG:`) returned a **full page of 100 covering only Aug 2018 → Dec 2021** — i.e. ~30 originals
per year in that window, with pagination continuing further back. Extrapolated over the ~11.5 years
of history: **roughly 300–400 original sent messages pre-2022**, plus a much larger volume of replies.

**Composition — the honest picture.** The bulk is transactional and low-value: domain renewals,
booking confirmations, support tickets, forwards, and one-word subjects (`convert`, `rest`, `12`,
`11`, `links`). A minority are substantial. Measured examples, all English, all sole-authored:

| Message | Date | MG's own words (quoted thread excluded) |
|---|---|---|
| `Garmin Pilot Feedback` → avionics.europe@garmin.com | 2018-08-24 | ~900–1,200 — structured technical product critique, exactly his natural register |
| `Re: Garmin Pilot Feedback` | 2020-01-30 | several hundred |
| `Re: FW: Europe` | 2018-10-22 | several hundred |
| `Re: Private Aviation` | 2019-07-31 | ~300–500 |

**Realistic yield: on the order of 20,000–50,000 words of English prose pre-2022**, concentrated in
maybe 50–150 messages. Meaningful, but roughly a third of what the documents already give, at
considerably more effort.

**Extraction approach I would use (next pass, not this one):**
1. **Google Takeout → Mail → mbox.** Do not paginate the MCP tool for this; a single Takeout export
   is one operation, is offline afterwards, and preserves `Date:` headers — which are the strongest
   per-item date evidence in the entire inventory (server-stamped, not user-editable).
2. Filter to `From:` MG (both `jeltz.prostetnic@gmail.com` and `matthias@matthiasgruber.com`) and
   `Date:` < 2022-01-01. **Use the header date, never the file.**
3. **De-quote hard** — strip `>`-prefixed lines, `On <date>, X wrote:` blocks, forwarded-message
   bodies, HTML, signatures, and disclaimer footers. Un-de-quoted mail would put *other people's*
   sentences in a corpus whose entire purpose is that it contains only his.
4. Language-detect per message; keep English, park German in a separate corpus.
5. Drop anything under ~150 words — below the harness's 250-unit chunk floor it contributes nothing.
6. **Privacy scrub before anything is written to the repo** (see §E).
7. Split into `control-en-mail-2010-2015` and `control-en-mail-2016-2021` rather than pooling —
   register drifts over a decade, and `corpora.json`'s own note warns against pooling date ranges.

⚠ Because everything runs locally on the 4090 and nothing leaves the machine, mail content in the
corpus is acceptable — but it should live outside git, or in a gitignored path, not in a repo that
has a public filtered mirror.

---

## E. ⚠ Sensitivity flags

- **Ivoclar-corporate: excluded by rule, and one item nearly slipped through.**
  `Definition of Basic Consciousness.docx` carries `dc:creator = "Gruber, Matthias"` — the corporate
  `Surname, Firstname` account form — which is a second, independent reason to keep it out beyond
  its 2023 date. Nothing else in this inventory is Ivoclar-sourced. The FMS `Work/` and
  `Professional/` trees were deliberately not mined.
- **Gmail is personal correspondence.** Pre-2022 sent mail contains bookings, medical/insurance
  admin, financial and legal threads (`Gutachten und Anhänge`, `Rechnungen`, `Mugrauer Consulting AG`),
  and family correspondence. If mail is used, scrub names, addresses, phone numbers, booking and
  account references before it lands anywhere persistent, and never let it into the public mirror.
- **`Gutachten`-type material** (court-expert / forensic assessments) appears in the pre-2022 mail
  stream. Out of scope for a style corpus and legally sensitive — exclude by subject filter.
- **The 8PWC estate contains third-party material** — published Wing Tsun books, CIA/US-Army
  manuals, scraped forum threads under `kkb proof/`. Only the named `.docx` files above are MG's.
- **`_Roman/Research/` and `_X2/`** hold third-party astronomy papers and images used as source
  material. Not prose, not his — excluded.

---

## F. (F) UNVERIFIED / open items

| Item | Why it is not graded CERTAIN |
|---|---|
| DMS `CRE-003` / `CRE-005` recorded `[unknown-date]` | Now resolved to 2016–2018 by document metadata. Worth writing back to the DMS catalogue (cross-project — needs an inbox item, not a direct edit). |
| ~~8PWC 1st vs 2nd edition discrepancy~~ | **RESOLVED by measurement** — running prose 29,523 vs 29,514, same 909 paragraphs. Same body text. Use one. |
| ~~Clean-prose yield of the 8PWC books~~ | **RESOLVED by measurement** — 95–97% of body-paragraph words sit in paragraphs of ≥15 words. The instructional layout inflates the *nominal* count, not the body flow. Densities are in the totals table. |
| Whether the harness's own docx/pdf extractor matches these numbers | The running-prose figures come from a `python-docx` paragraph walk, not from `scripts/detector/`'s extractor. Expect agreement, but the corpus should be re-counted through the real extraction path before any flag rate is quoted. |
| Gmail volume | The 100-result probe hit the page cap; the true pre-2022 original count was not paginated to exhaustion. The 300–400 figure is an extrapolation, explicitly not a count. |
| `~/scifi/source/*.txt` cleanliness | Established from git history (two structural commits, no content commits), not from a byte-diff against the 2018 originals. Prefer the FMS `.docx` and this question disappears. |
| Whether the English 8PWC book had a native-speaker proofreader | The docx `dc:creator` on both language editions is `Craig Lightfoot` — almost certainly the Lulu template's origin rather than a person who touched the text (the *German* edition carries the same creator, so it cannot be an English-language editor). Low risk, but unproven. |

---

## G. Recommended next actions

1. **Fix the quarantine now.** Promote `Holomatic Self Model Theory.docx` (2014-11-10, CERTAIN) into
   `control-en`; **remove** `Definition of Basic Consciousness.docx` from any control slot and record
   `dcterms:created 2023-04-26` as the reason. Retire `control-en-unverified`.
2. **Build `control-en` from A1 + A2 + A3** first — **99,097 words** of narrative/essay-register
   English, ≈ **310 chunks**, all sole-authored, all datable three independent ways. That alone
   unblocks `AIW-224` and resolves a flag rate to ~0.3%.
3. **Keep A4 (+A5, A6) in a separate `control-en-academic` corpus.** Comparing its flag rate against
   the narrative corpus is the direct test of MG's *"the more rigorous a text the less detectable"*
   hypothesis — and per the research doc it may come out backwards.
4. **Refresh the German `control`** with G1–G3 and G6–G8 to push the German baseline below 0.1%.
5. **Defer Gmail** to a follow-up pass via Takeout. It is worth doing, but it is the smallest source
   with the highest handling cost and the only real privacy exposure.
