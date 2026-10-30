<!-- Action: act -->
<!-- Tracked-by: AIW-204, AIW-193 -->
# `AIW-204` — the FMT reference audit, S302 (2026-08-12, WSL)

**The headline: the gate was right to be red, and for reasons nobody had guessed.** The 65 flagged
references were expected to be 65 false alarms from books Crossref does not index. They were not.
**Three cited works do not exist**, a fourth class of defect was found that no one was looking for —
**the `.md` and the `.bib` disagree about what a citation key means** — and roughly ten more entries
carry wrong metadata.

Prior framing (S300/S301) said the 65 were "triaged one by one and none of them is a bad reference."
**That triage was wrong.** It classified entries by *why Crossref could not confirm them* and inferred
existence from the category. Category is not evidence. This pass checked them against publisher
records instead.

---

## 1. Three references in the FMT master do not exist

Found by four verification passes against publisher records, Crossref, PubMed and library catalogues.

| key | what the master cites | status |
|---|---|---|
| `Heitmann2022` | Heitmann, S. & Bhatt, D. (2022). Closed-eye phosphenes and cortical noise. *Trends in Neurosciences*, 45(10), 725-727. | **NOT FOUND.** No Crossref record, no PubMed record, no exact-title web hit. No such paper. |
| `Siclari2021` | Siclari, F., et al. (2021). The content of dreams decoded from posterior cortical activity during sleep. *NeuroImage*, 224, 117442. | **NOT FOUND.** Article number 117442 belongs to Munsch et al., an unrelated ihMT imaging paper, in *NeuroImage* **225** — not 224. The real underlying work is Siclari et al. **2017**, *Nat Neurosci* 20(6), 872-878 (`10.1038/nn.4545`), already cited in the paper. |
| `Northoff2020` | Northoff, G. (2020). Neuroscience and consciousness: Lessons from Temporo-Spatial Theory of Consciousness. In *The Routledge Handbook of Consciousness*. Routledge. | **NOT FOUND.** The Gennaro-edited handbook has 35 chapters and none is Northoff's; Crossref holds no Routledge chapter of that title; Northoff's own publication page lists none. |

**Where each is cited, and what it costs to remove it:**

- **`Heitmann2022`** — §6-vicinity, the closed-eye phosphene passage: *"...and spontaneous cortical
  activity in V1 and higher visual areas (Heitmann & Bhatt, 2022)."* The claim is uncontroversial and
  a real source exists; the citation must go, and a verified replacement should take its place rather
  than the claim being left bare. **Do not substitute a plausible-looking citation** — that is the
  mechanism that produced this defect.
- **`Siclari2021`** — cited as part of *"(Noreika et al., 2009; Siclari et al., 2017, 2021; Nir &
  Tononi, 2010)"*. **Cheapest possible repair: delete `, 2021`.** The claim is carried by Siclari 2017,
  which is real, already in the list, and is the paper the sentence actually describes.
- **`Northoff2020`** — §7, *"Northoff's (2020) Temporo-Spatial Theory of Consciousness (TTC) links
  consciousness to spatiotemporal dynamics and their relation to self-referential processing."* Two
  real substitutes exist and one is already in the `.bib` — see §2.

⚠ **Reputational note:** Northoff is contact #7 in `contacts.md`, status *Contacted*, flagged as the
**strongest FMT alignment** of any researcher on the list. Citing a chapter of his that does not exist
is the specific kind of error that gets noticed by the one person most likely to read that paragraph.

---

## 2. The bigger finding: `.md` and `.bib` describe DIFFERENT publications under the same key

`CLAUDE.md` declares the pipeline `.md → .tex → .pdf` with the `.md` as source of truth and the `.tex`
hand-ported from it. **The two have silently diverged on at least five keys, and the reference gate has
never looked at the `.bib` at all.**

This matters more than the fabrications: **the canonical committed PDF is built from
`paper/full/latex/paper.tex` + `references.bib`.** The gate parses `paper/full/four-model-theory-full.md`.
So the artifact that gets read has never been checked, and the artifact that gets checked is not the one
that gets read.

| key | `.md` says | `.bib` says | which is right |
|---|---|---|---|
| `Northoff2020` | Routledge handbook chapter (does not exist) | Northoff & Lamme (2020), *Neurosci Biobehav Rev* 118, 568-587, `10.1016/j.neubiorev.2020.07.019` | ✅ **`.bib` — verified real via Crossref** |
| `Safron2020` | title truncated, subtitle dropped | full published title with subtitle, `10.3389/frai.2020.00030` | ✅ **`.bib` — verified real via Crossref** |
| `Dresler2012` | subtitle dropped | full title incl. *": A Combined EEG/fMRI Case Study"*, `10.5665/sleep.1974` | ✅ **`.bib` — verified real via Crossref** |
| `Heitmann2022` / `HeitmannBhatt2022` | *Closed-eye phosphenes and cortical noise*, *Trends in Neurosciences* 45(10), 725-727 | *Closed-eye visual patterns and cortical dynamics*, *Neurosci Biobehav Rev* 132, 37-50 | ❌ **NEITHER EXISTS — see below** |
| `Siclari2021` | *The content of dreams decoded…*, *NeuroImage* 224, 117442 | *Dreaming in NREM sleep…*, *J Neurosci* **41**(43), 9175-9185, year **2021** | ⚠ **both wrong, differently — see below** |

### ⚠ `Heitmann2022` is fabricated on BOTH surfaces, so the shipped PDF carries a phantom citation

Crossref exact-title search returns zero; a Crossref query filtered to *Neuroscience & Biobehavioral
Reviews* for the 2022 window returns zero; and **Stewart Heitmann and Dushyant Bhatt have never
co-authored anything at all** — Heitmann's collaborators are Breakspear, Ermentrout and Truccolo. Two
differently-worded fabrications under one key, which is the signature of a citation invented twice
rather than mis-transcribed once.

**A verified replacement exists for the claim it was supporting** (that cortical activity contributes
to closed-eye phosphene percepts): **Billock, V. A., & Tsou, B. H. (2012). Elementary visual
hallucinations and their relationships to neural pattern-forming mechanisms. *Psychological Bulletin*,
138(4), 744-774, `10.1037/a0027580`** — confirmed against the APA-registered Crossref record. It is a
review of exactly the cortical pattern-forming mechanisms the passage appeals to. **MG's call whether
to substitute it or drop the citation and leave the (already hedged) claim bare.**

### ⚠ `Siclari2021` — the `.bib` names a real paper and misdates it by three years

The work exists: **Siclari, F., Bernardi, G., Cataldi, J., & Tononi, G. (2018). Dreaming in NREM sleep:
A high-density EEG study of slow waves and spindles. *Journal of Neuroscience*, **38**(43), 9175-9185,
`10.1523/JNEUROSCI.0855-18.2018`** (PubMed 30201768). Authors, title, issue and pages match the `.bib`
exactly; **the year (2021 → 2018) and the volume (41 → 38) are wrong.** So the canonical PDF prints a
real paper under a wrong date, while the `.md` prints a paper that does not exist. The key must also be
renamed — `Siclari2021` describing a 2018 work is a trap for the next editor.

⇒ **On the three settled rows the `.bib` is correct and the `.md` is the defective side.** That inverts
the assumption the pipeline rule encodes, and it means repairing the `.md` from the `.bib` is the right
direction of travel for those — not the reverse.

**⇒ ACTION THAT FOLLOWS: the gate's corpus must include `references.bib`.** Checking one of two
divergent sources is a gate that reports green on an artifact nobody ships. Proposed as the immediate
follow-on to this item.

---

## 3. Metadata defects — real works, wrong details

| key | defect | correction |
|---|---|---|
| `Penrose1994` | **author order and year both wrong** | Hameroff, S., & Penrose, R. (**1996**). Same title, *Math. Comput. Simul.* 40(3-4), 453-480, `10.1016/0378-4754(96)80476-9`. Hameroff is first author. Affects `.md`, `.bib` key `PenroseHameroff1994`, and the in-text *"(Penrose & Hameroff, 1994)"*. |
| `Coleman2014` | wrong subtitle **and** wrong issue | *"The Real Combination Problem: **Panpsychism, Micro-Subjects, and Emergence**"*, *Erkenntnis* **79(1)**, 19-44. "Phenomenal bonding" is Goff's term, not this paper's title. Wrong in both `.md` and `.bib`. |
| `Safron2020` | subtitle dropped in `.md` | take the `.bib` version |
| `Dresler2012` | subtitle dropped in `.md` | take the `.bib` version |
| `Aaronson2014` | title truncated | full title is *"Why I Am Not An Integrated Information Theorist (or, The Unconscious Expander)"*, 21 May 2014, `https://scottaaronson.blog/?p=1799` |
| `Bach2026` | **subtitle is not the paper's** | *"Cyberanimism and the software of the mind"* comes from third-party commentary, not from the essay. Published title is *"The Machine Consciousness Hypothesis"*, 16 Jan 2026, CIMC, `https://cimc.ai/cimcHypothesis.pdf` |
| `Anthropic2025` | described as a "Research report" | it is a ~500-word programme-announcement blog post, 24 Apr 2025 |
| `Andrews2024` | **attribution wrong** | the Declaration carries no author line; Andrews, Birch and Sebo are organisers and lead signatories. The site's own recommended citation covers the *Background* document and adds a fourth name, Sims. |
| `LaBerge1985` | year/publisher belong to two different editions | 1985 = J. P. Tarcher (LCCN 85004691); Ballantine = **1986** (ISBN 0345333551). Pick one. |
| `Brodmann1909` | subtitle omitted | acceptable short-title form; no action needed |
| `Gruber2026b` | unpublished manuscript, no public copy | not a defect, but a reviewer-visible weakness: a cited source no reader can obtain |

### ⚠ `Gruber2015` — NOT RESOLVED, and it is MG's to settle
ISBN 9781326652074 resolves to a real Lulu.com record for the right author, **but**: the registered
title is *"Emergenz des Bewusstseins"* — **without the leading "Die"** — and the aggregators disagree on
the year (Open Library says 15 July **2016**; isbnsearch says 20 January **2015**). No library record
exists anywhere; the Deutsche Nationalbibliothek returns zero for this ISBN. **Per the data-integrity
rule this was left untouched: two sources disagree on a fact, so it is reported, not silently picked.**
MG has his own Lulu publication records and can settle both the year and the "Die" in one look.

### Verified clean — 30 entries
`Baars1988` · `Barrett2019` · `Chalmers1996` · `Chalmers2018` · `Damasio1999` · `Damasio2010` ·
`Dehaene2021` · `Dennett1991` · `Frankish2016` · `GodfreySmith2016` · `Goff2019` · `Graziano2013` ·
`Hinton1986` · `Hofstadter2007` · `Huxley1874` · `IITConcerned2025` · `Klver1966` · `Kriegel2006` ·
`Lashley1950` · `Lewis1988` · `Loar1997` · `Lynn2012` · `Metzinger2003` · `Metzinger2009` ·
`Milner1962` · `Nemirow1990` · `Pribram1991` · `Seth2021` · `Strawson2006` · `Weiskrantz1986`

Non-defect observations worth keeping: `Milner1962` has its French accents stripped; `Loar1997`,
`Lewis1988`, `Huxley1874` and `Lashley1950` all have reprints under later years but each entry cites
the original correctly — a reprint under a different year is not a defect and should not be "fixed".

---

## 4. Two gate defects fixed this session (TDD, `scripts/verify_references.py`)

**(a) Interrogative titles were never terminated.** APA replaces the title's closing period with the
title's own punctuation, so `_title` — which looked only for `". "` — swallowed the journal, volume and
pages: *"What is it like to be a bat? Philosophical Review, 83(4), 435-450"*. The inflated string then
scored 0.6-0.86 against Crossref's clean title. **Six correctly-cited references were flagged by this
alone** (Nagel 1974, Van Rullen 2003, Friston 2010, Hengen 2025, Kleiner 2024, Zheng 2025). A parser
defect presenting as a bibliography defect is exactly how a gate earns a reputation for crying wolf.

⚠ **The first fix over-corrected and the corpus caught it** — terminating at the first `?` truncated
two titles with *interrogative openings* (`Tononi2025`, `WagnerAltendorf2024`), both of which had been
`verified` at score 1.0. They regressed to `needs-review` and are now back at 1.0. **The rule that
survives: a `?` or `!` ends the title only when the container follows it** — the captured journal name,
or a capitalised phrase followed by a comma and a volume number. Both failure directions have
regression tests.

**(b) Crossref is not the whole DOI system.** Zenodo, OSF and arXiv register with **DataCite**, so the
gate reported *"no Crossref candidate — check by hand"* for permanently-archived, machine-resolvable
records — including **this project's own published companion paper**. Added `datacite_candidate()`,
consulted only when Crossref settles nothing. A bare `arXiv:NNNN.NNNNN` now resolves through the DOI
arXiv registers for it, `10.48550/arXiv.<id>`.

**(c) New `--only-flagged` mode.** Re-running a full `--update` after a parser change is what demoted
those two clean rows — Crossref's relevance ranking differs between runs. `--only-flagged` re-resolves
the open backlog and **cannot touch a passing row**, which removes that hazard from all future
maintenance passes.

**(d) An incomplete Crossref author roster was being read as evidence of a missing author.** The
adjudicator's own comment said *"Crossref truncation is not evidence"*, but the implementation only
handled an **empty** roster — not the far commoner **truncated** one. Crossref routinely deposits only
the first author: it lists one name for Dehaene & Naccache 2001, one for Tononi & Edelman 1998, one for
Kriegeskorte/Mur/Bandettini 2008, one for Myers & Sperry 1958. Each was flagged for a co-author who is
simply absent from a one-name record. **A roster shorter than the entry's is incomplete, and absence
from an incomplete roster proves nothing.** Where Crossref does hold a full roster the check runs
unchanged, so the defect it was built for — a wrong name at position three, Konopka/Markopoulou/**Smolin**
against the real …/**Severini** — is still caught, and has a test saying so.

**Result: 65 → 14 flagged, zero regressions.** Test suite 216 passed / 1 failed, the single failure
being `TestManifestRatchet` — which *is* the remaining backlog, so the gate and the suite go green
together.

**The 14 that remain are exactly the defect list**, which is the point: the gate now flags problems
instead of flagging its own blind spots. Twelve await the repair pass — `Aaronson2014`, `Andrews2024`,
`Anthropic2025`, `Bach2026`, `Coleman2014`, `Dresler2012`, `Heitmann2022`, `LaBerge1985`,
`Northoff2020`, `Penrose1994`, `Safron2020`, `Siclari2021` — and two are MG's calls (`Gruber2015`,
`Gruber2026b`). Nothing in the flagged set is a false alarm any more.

**111 rows now carry `verified-manual` with named evidence** (77 pre-existing from RIM and cosmology,
34 written this session): publisher catalogues, LCCNs and ISBNs for the books; ACM/MIT Press records and
the authors' own posted PDFs for the chapters and JCS articles; and, for four entries whose DOI resolves
to an exact-title record that Crossref simply has no byline for (`Alnagger2026`,
`COGITATEConsortium2025`, `Llins1998`, `Toker2026`), a note saying precisely that.

---

## 5. The repair pass — APPLIED, both surfaces (MG-authorised 2026-08-12)

Applied to `paper/full/four-model-theory-full.md` **and** `paper/full/latex/{paper.tex, references.bib}`,
including the in-text citations and the citation keys:

| what | change |
|---|---|
| `Penrose1994` → `Hameroff1996` | author order corrected, year 1996, DOI added; key renamed in `.bib` and `\citep`; entry moved from the P section to the H section of the `.md` list; in-text now *(Hameroff & Penrose, 1996)* |
| `Siclari2021` → `Siclari2018` | the real 2018 *J Neurosci* paper, vol 38(43), DOI added; the fabricated `.md` entry replaced outright; in-text *"Siclari et al., 2017, 2021"* → *"2017, 2018"* |
| `Northoff2020` → `Northoff2017` | replaced with the canonical TTC statement, Northoff & Huang 2017, *NBR* 80, 630-645 — which is what the citing sentence actually describes |
| `Coleman2014` | true subtitle *"Panpsychism, Micro-Subjects, and Emergence"*, issue 1 not S1, DOI added |
| `Safron2020`, `Dresler2012` | full published titles restored in the `.md` (the `.bib` already had `Safron2020` right) |
| `Aaronson2014`, `Anthropic2025`, `Bach2026`, `Andrews2024` | correct titles, dates, media types, canonical URLs; the invented *"Cyberanimism"* subtitle removed; the Declaration re-cited to its own recommended form |
| `LaBerge1985` | publisher corrected to J. P. Tarcher (the 1985 first edition) |
| `Gruber2015` | ✅ **no change — the entry was right.** MG confirms the cover carries *"Die"* and 2015 is the first edition (2016 = corrected reissue, new cover + typo fixes). Amazon's listing drops the article, which is why the aggregators disagreed. |

**Six of the repairs then verified automatically against Crossref** — `Coleman2014`, `Dresler2012`,
`Hameroff1996`, `Northoff2017`, `Safron2020`, `Siclari2018` all came back `verified`, which is
independent confirmation that the corrections match the real records rather than merely being different.

**The `.tex` was rebuilt into `tmp/build-full-s302/` (never canonical): `bibtex` clean, zero undefined
citations, 138 pp.** Spot-checked in the rendered PDF: *"(Hameroff and Penrose, 1996)"*,
*"Northoff and Huang (2017)'s Temporo-Spatial Theory"*, the Dresler EEG/fMRI subtitle, and
*"Journal of Neuroscience, 38(43):9175–9185, 2018"* all render correctly.

**Gate state: `--check --paper fmt` reports 2 problems across 230 entries**, down from 65. Both are the
open decisions below. Three stale manifest rows left by the key renames were pruned.

## 6. What is left

1. **`Heitmann2022` — the only fabrication still in the paper.** See §7: the literature does not support
   the sentence as written, so this is a wording decision, not a citation lookup.
2. **`Gruber2026b`** — MG asked whether this is the computational companion. **It is not.** The
   computational companion is **`Gruber2026d`**, published (Zenodo concept `10.5281/zenodo.21610993`).
   `Gruber2026b` is the *mathematical formalization roadmap*, which exists in this repo as
   `paper/fmt_formal/fmt-formalization.{md,pdf}` and has **never been published anywhere** — yet it is
   **cited four times** in the master. Either publish it so the citations resolve, or rewrite those four
   passages. ⚠ Publishing is gated by the `AIW-206` disclosure freeze, though this is theory rather than
   implementation and is probably outside the fence — confirm before pushing.
3. **Add `references.bib` to the gate's corpus.** Still the most valuable follow-on: the `.bib` builds
   the artifact that ships, and this session proved the two surfaces drift apart silently.

## 7. ✅ `Heitmann2022` — RESOLVED by rewording (MG: "reword", 2026-08-12)

**The last fabricated citation is gone from every surface.** The sentence was rewritten rather than
re-cited, because the honest finding was that no source supports it as written.

**As it now stands (`.md` and `.tex`, and it renders correctly in the build):**

> These "dark noise" phosphenes have well-characterized retinal sources: rod outer segments generate
> discrete electrical events by thermal isomerization of rhodopsin, indistinguishable from responses to
> real single photons (Baylor, Lamb, & Yau, 1979; Baylor, Matthews, & Yau, 1980). Spontaneous cortical
> activity in V1 is a plausible additional contributor — ongoing activity there persists and remains
> structured in the absence of visual input (Kenet et al., 2003), and cortically generated percepts arise
> under prolonged visual deprivation (Merabet et al., 2004) — but the relative contribution of retinal
> versus cortical sources remains an active research question.

Three references added, **all three verified against Crossref by the gate on the next run**:
`Baylor, Matthews & Yau 1980` (`10.1113/jphysiol.1980.sp013529`), `Kenet et al. 2003`
(`10.1038/nature02078`), `Merabet et al. 2004` (`10.1097/00041327-200406000-00003`).

**⚠ The proposed replacement was itself wrong and verification caught it.** The recommendation named the
1980 dark-noise paper as *"Baylor, Lamb & Yau"*. Crossref shows the actual author list is **Baylor,
Matthews & Yau** — Lamb is not on it. Lamb is on the *1979* paper. Had that been applied unchecked it
would have replaced a fabricated citation with a malformed one, in the very edit meant to fix
fabrication. **Verify replacements as hard as originals.**

**The `Baylor 1979` claim-mismatch is fixed by the same edit** — the sentence no longer attributes
ganglion-cell firing to it, and now uses each Baylor paper for what it actually reports: 1979 for the
single-photon response, 1980 for the discrete thermal dark events.

**Gate after this edit: 1 problem across 232 entries** — `Gruber2026b`, which is under separate review.

### The original finding, retained because the reasoning is the reusable part

MG asked for a real replacement "if there is one". A dedicated search says the honest answer is no.

**The sentence as written:** *"These 'dark noise' phosphenes have multiple well-characterized sources:
spontaneous retinal ganglion cell firing (Baylor, Lamb, & Yau, 1979), intrinsic retinal noise from
thermal isomerization of rhodopsin, and spontaneous cortical activity in V1 and higher visual areas
(Heitmann & Bhatt, 2022)."*

**Classical psychophysics attributes eigengrau / dark light overwhelmingly to RETINAL sources** — Barlow's
retinal-noise account, and the quantitative match between rod thermal isomerization rates and psychophysical
dark light. No study was found that measures a *cortical* contribution to the normal closed-eye dark-noise
percept. Calling it a "well-characterized source" is an overclaim, which is very likely *why* a citation
had to be invented for it: there was nothing to cite.

**Billock & Tsou (2012) was considered and REJECTED for this slot.** It is real
(`10.1037/a0027580`) but it is about elementary *geometric* hallucinations — Klüver form constants arising
from Turing-type cortical pattern formation. Citing it here would quietly substitute *"cortex can
pattern-form hallucinatory geometry"* for *"cortical noise contributes to eigengrau"*, which it does not
claim. Substituting it would repeat the original error in a more defensible-looking form.

**What the evidence does support**, with verified sources:
- **Kenet, T., Bibitchkov, D., Tsodyks, M., Grinvald, A., & Arieli, A. (2003).** Spontaneously emerging
  cortical representations of visual attributes. *Nature*, 425(6961), 954-956, `10.1038/nature02078` —
  ongoing V1 activity without visual input is real and structured. But anesthetized cat, no perceptual
  report.
- **Merabet, L. B., et al. (2004).** Visual hallucinations during prolonged blindfolding in sighted
  subjects. *J Neuro-Ophthalmol*, 24(2), 109-113, `10.1097/00041327-200406000-00003` — cortically
  generated percepts under deprivation, but onset after ~a day.

**Proposed revision (MG's call):** *"These 'dark noise' phosphenes have well-characterized retinal
sources — spontaneous retinal ganglion cell firing (Baylor, Lamb, & Yau, 1979) and thermal isomerization
of rhodopsin — and spontaneous cortical activity in V1 is a plausible additional contributor: ongoing V1
activity persists and is structured even without visual input (Kenet et al., 2003), and cortically
generated percepts occur under visual deprivation (Merabet et al., 2004). The relative contribution of
retinal versus cortical sources remains an active research question."*

### ▸ And a second defect in the same sentence — a claim-to-source mismatch

**`Baylor, Lamb & Yau (1979)` is cited for "spontaneous retinal ganglion cell firing", but that paper
reports suction-electrode recordings of *rod photoreceptor outer-segment* currents in toad — not ganglion
cells.** Their dark-noise result is the 1980 companion paper, *"Two components of electrical dark noise in
toad retinal rod outer segments"*, *J Physiol* 309:591-621. This is the **claim-to-source** half of the
defect class, which this gate explicitly does not automate — it surfaced only because a human-directed
agent read the cited paper. Worth fixing in the same edit, and worth noting as evidence that existence
checking alone is not sufficient.

⚠ **Do not re-run a bare `python3 scripts/verify_references.py --update --paper fmt`** on this corpus —
use `--only-flagged`. The full re-resolve is what caused the regression documented in §4.
