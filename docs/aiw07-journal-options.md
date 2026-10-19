# AIW-07 — Is there a realistic journal for the FULL FMT paper?

Research note, 2026-09-29 (S324). Research only — nothing submitted, nobody contacted.
Inputs: `paper/full/four-model-theory-full.md` (v16), `backlog.md` (AIW-07, AIW-46, AIW-130, AIW-149),
`docs/decisions.md` (S274 slice strategy; "coordinate system" reframe; S297 timing; AIW-36 **no APC money**;
S324 **no work toward journals that rejected us**), `paper/jaic/journal-guidelines-jaic.md`.

**Measured size of v16 (2026-09-29):** 52,659 words of body (everything before `## References`),
59,796 words in total, **322 reference entries**, ~160 pp built. For scale: that is 2.6× PhiMiSci's hard
ceiling, 3.8× BBS's, 5.9× JCS's, and roughly 7× what a normal theory article is.

---

## 1. Verdict

1. **Full paper (52.7k words / 322 refs): no realistic journal.** No peer-reviewed journal checked will review 160 pages as one article. The few with no *stated* cap (Biosystems, JAIC, Synthese, Mind and Matter) still work to 15–40 printed pages in practice, and a 160-page single-author submission from an unaffiliated author is a desk-reject on length alone. The book/monograph (AIW-149) is the only venue that carries the full text intact, and the Zenodo preprint remains its citable form.
2. **Best home for a condensed *whole-theory* version: *Philosophy and the Mind Sciences* (PhiMiSci)** — no APC (diamond OA), **double-blind review** (the reviewers cannot see that the author is unaffiliated), theoretical articles in scope, and a hard ceiling of 20,000 words, so a ~12–15k framework paper is a legitimate submission. Main risk: its AI-use clause (see §4).
3. **Runner-up for a condensed version: *BioSystems*** (Elsevier) — free on the subscription route, "full-length articles… irrespective of length", explicitly theoretical, and it publishes unconventional consciousness theory. Single-blind, so the affiliation is visible; a biology/information-science framing is required.
4. **The best odds of any single submission stay with the existing JAIC slice (AIW-130)** — Kanai's journal, free, single-blind, "completing ICCR". Do **not** send the full or condensed whole-theory paper to JAIC as well: that would compete with, and could kill, the slice lane.
5. Every paid-APC venue is out under the AIW-36 ruling (Entropy CHF 2,600; Frontiers ~US$3k; PLOS ONE $2,477; RSOS ~£1.4k, discretionary waiver only), and the five rejecting journals are excluded under S324.

---

## 2. Comparison table

Everything was checked 2026-09-29. "Site" means the journal's own page was fetched. "Search" means Springer, T&F, MIT and MDPI returned 403 to direct fetches, so the figure comes from search excerpts of the official guideline page (URL given). Treat those rows as needing one click to confirm before any build work.

| Venue | Scope fit | Length limit | Full paper fits? | Review / affiliation | Cost to us | Standing | Source |
|---|---|---|---|---|---|---|---|
| **PhiMiSci** | Good: philosophy × mind sciences, theoretical articles invited | "Most 4,000–10,000"; **>20,000 words not considered** | **No** (2.6× over) | **Double-blind**, max 2 rounds | **€0** (diamond OA, CC-BY) | Well regarded in consciousness philosophy (Metzinger/Wiese circle); Scopus indexing not verified | Site: philosophymindscience.org/index.php/phimisci/about/submissions |
| **BioSystems** (Elsevier) | Fair–good: "theoretical, computational… link biology, evolutionary concepts, information sciences"; published Miller/Baluška/Reber on AI consciousness, vol. 247 (2025) | "Full-length articles… irrespective of length" | Formally yes; in practice no | Single-blind (Elsevier default) | **€0** subscription route (OA US$3,010, which we skip) | Scopus/WoS, IF ~2; mid-tier, open to heterodox theory | Search: sciencedirect.com/journal/biosystems/publish/guide-for-authors |
| **JAIC** (World Scientific) | Good for the AC angle ("Assessing AI Consciousness" section) | No published cap; articles ~14 pp typical (vol. 7) | Formally yes; in practice no. **Already reserved for the AIW-130 slice** | **Single-blind**; independent author OK | **€0** subscription route (OA $2,000, which we skip) | Scopus; young and low-citation, but the EiC (Kanai) is the right reader | Stored guideline file (S216 from WS pages); site 403 today |
| **Synthese** (Springer) | Fair: philosophy of science/mind; the "coordinate system" angle fits better than "theory" | No cap; "typically 15–30 printed pages" | No | **Double-blind** | €0 subscription route | High (WoS, top-20 general philosophy); high desk-reject rate | Search: link.springer.com/journal/11229/submission-guidelines |
| **Minds and Machines** (Springer) | Good for AI + consciousness | No cap found; "important articles exceeding normal length may appear" | No | Springer; model not confirmed | €0 subscription route | WoS, IF ~4.7 (Q2 AI) | Search: link.springer.com/journal/11023/submission-guidelines |
| **Mind and Matter** (Imprint) | Fair: interdisciplinary mind–matter research, theoretical OK | No cap; "as concise as possible" | Unlikely | Editorial pre-screen, then peer review | **€0** traditional (OA £950, which we skip) | Small. Editorial office is IGPP Freiburg (parapsychology institute), which is a **reputational association risk** for FMT | Site: mindmatter.de/journal/mminstruct.html |
| **Phenomenology & the Cognitive Sciences** | Weak: phenomenology-centred | Special issues run 7.5–9k; regular cap not found | No | **Double-blind** | €0 subscription | WoS, respectable | Search: link.springer.com/journal/11097/submission-guidelines |
| **Philosophical Psychology** (T&F) | Fair | Cap not retrieved (site 403) | No | **Double-anonymised**, 2 referees | €0 subscription | WoS, respectable | Search: tandfonline.com/journals/cphp20 |
| **Cognitive Systems Research** (Elsevier) | Fair (cognitive architectures) | **3,500–10,000 words** excl. refs | No | Single-blind | €0 subscription | Scopus/WoS, mid | Search: sciencedirect.com/journal/cognitive-systems-research/publish/guide-for-authors |
| **New Ideas in Psychology** (Elsevier) | Good for new theory ("original theoretical papers") | **7,500 words**, exceptions possible | No | Single-blind | €0 subscription | WoS, mid | Search: sciencedirect.com/journal/new-ideas-in-psychology/publish/guide-for-authors |
| **Theory & Psychology** (Sage) | Fair | 5–8k, **max 10,000 incl. refs** | No | Sage | €0 subscription | WoS, mid | Search: journals.sagepub.com/author-instructions/tap |
| **Neural Computation** (MIT) | **Poor**: wants mathematical/computational results, not verbal theory | Cap not retrieved | No | — | €0 | High | Search: direct.mit.edu/neco/pages/submission-guidelines |
| **J. Theoretical Biology** | **Poor**: mathematical biology | — | No | — | €0 subscription | High | Not fetched; scope mismatch judged from known remit |
| **BBS** target article | Ideal format for a rival theory with commentary; extremely selective | **≤14,000 words**; optional **1–2k-word proposal** first, plus 20–30 suggested commentators and a ~500-word rationale | No | Editor-triaged, then refereed | €0 | Top tier | Site: cambridge.org/core/journals/behavioral-and-brain-sciences/information/author-instructions/preparing-your-materials |
| **Frontiers in Psychology** (Theor. & Phil.) | Good (Hypothesis & Theory type) | **12,000 words** (H&T); Conceptual Analysis 8,000 | No | Named reviewers | **APC ~US$3k** → **out** (AIW-36) | Scopus/WoS; mixed reputation | Site: frontiersin.org/…/theoretical-and-philosophical-psychology/for-authors/article-types |
| **Entropy** (MDPI) | Good for information-theoretic consciousness | No hard cap | Formally yes | Single-blind | **CHF 2,600** → **out** | Scopus/WoS; MDPI reputation mixed | Search: mdpi.com/journal/entropy/apc |
| **PLOS ONE** | Poor (not a theory venue) | — | — | — | **US$2,477** (hardship PFA exists) → **out** | — | Search: plos.org/fees |
| **Royal Society Open Science** | Weak–fair | — | — | — | APC ~£1,400 (Jan-2024 figure), discretionary waiver only → **out** unless the waiver is granted | High | Search: royalsocietypublishing.org/rsos/pages/charges, …/waivers |
| *Excluded (rejected us):* NoC, PLREV, NBSR, C&C | — | — | — | — | — | — | S324 |
| *Excluded (length):* JCS | — | **9,000 incl. refs** | No | — | — | — | AIW-46 |
| **Monograph (AIW-149)** | Full unification intact | None | **Yes** | Not journal peer review. An academic press (e.g. Springer/Palgrave, MIT, Imprint Academic) would referee the proposal | ISBN; €0 via KDP; a press route costs nothing but time | Citable; affiliation irrelevant | backlog AIW-149 |

---

## 3. What the top two would need

### A. PhiMiSci — condensed whole-theory paper ("the chart, filled once")

- **Length:** from 52.7k to **≤15k words, including notes** (the ceiling is 20k; stay well under it so the length is never the objection). References from 322 to about 80–100.
- **Keep:** the 8 requirements as a *coordinate system* the field can fill, the comparative scoring matrix vs IIT/GNW/HOT/PP/AST/RPT (with status tags, and the FMT-specific cells published openly), FMT as **one filling** of the chart, and 2–3 sharp falsifiable predictions (two dials / time dilation).
- **Cut to a pointer (cite the Zenodo concept DOI 10.5281/zenodo.18669891):** the in-silico section, the formalization companion, the clinical sweep, the cosmology/RIM tie-ins, and most of the convergence evidence.
- **Format:** PhiMiSci template, abstract ≤200 words, **fully anonymised**. That includes self-citations to the Zenodo preprints ("Author, 2026" or third person) and **no author name in the file metadata**.
- **Cover-letter angle (S274 + the "coordinate system" reframe):** *"We propose a shared coordinate system for comparing theories of consciousness. Eight requirements, each tagged by current status, give the field a way to read off its consensus core and its live disputes. We fill the chart once, with a self-model architecture, to show that it discriminates, and we publish the cells where that filling is most exposed."* Never write "a new unifying theory that outperforms IIT and GNW". The paper is infrastructure, and the theory is the worked example.
- **AI-use disclosure:** mandatory, and it must be true. See risk R2.

### B. BioSystems — longer condensed version (~20–25k)

- **Length:** its "irrespective of length" rule permits more than PhiMiSci, but a 20–25k-word ceiling keeps review feasible. It is the only venue where the in-silico section and the criticality material can stay in.
- **Framing:** biology and information science. Consciousness is presented as the output of a self-modelling biological information system operating in a critical dynamical regime, and the paper leans on the criticality, neuronal-avalanche and in-silico material that a philosophy venue would cut. Present FMT as an **instantiation** of existing frameworks (self-model theory, predictive processing, criticality), with the scoring matrix as a comparison aid, not a verdict.
- **Format:** Elsevier template, single-blind, subscription route (do **not** tick OA, which costs US$3,010), highlights plus a graphical abstract.
- **Cover letter:** point to BioSystems' own record of publishing integrative consciousness theory (Miller et al. 2025, vol. 247), the concrete falsifiable predictions, and the runnable in-silico tests.

---

## 4. Risks

- **R1: Length is the binding constraint, not the venue.** Any condensed version needs roughly a 70% cut, and that is the hard part. The unification that didactic pattern #28 names as FMT's strength does not survive a cut to journal length. That is why the book (AIW-149) is the full-length home, and why the full paper should not be sent to any journal as it stands.
- **R2: The PhiMiSci AI clause.** Its guidelines say *"extensive use of AI-based tools for generating substantial article content is strongly discouraged"* unless the tools are part of the research design, and disclosure is mandatory. This project's drafting pipeline is heavily AI-assisted, so an honest disclosure could itself trigger a desk reject. **MG must decide this before any PhiMiSci build.** Options: rewrite the condensed version substantially by hand, or choose BioSystems/JAIC, whose policies require disclosure but do not discourage use.
- **R3: Prior-publication and optics conflicts.** The condensed paper, the JAIC slice and the NoC-lane material overlap. Keep each piece's contribution distinct (anti-salami rule, S274). Also check each venue's preprint and book policy against AIW-149 before the monograph goes out (the Kleiner question in AIW-149).
- **R4: Single-blind venues (BioSystems, JAIC, Mind and Matter) expose the unaffiliated author.** Double-blind (PhiMiSci, Synthese, P&CS, Phil Psych) removes the one factor S274 identified as decisive. That is why PhiMiSci ranks first despite its cap.
- **R5: Synthese is double-blind and prestigious, but its desk-reject rate is high and it expects analytic-philosophy argument, not a 30-page architecture.** It is plausible only for a narrow philosophical slice (e.g. the Bezugssystem regress argument).
- **R6: Reputational association.** Mind and Matter's editorial office sits at IGPP (a parapsychology institute). Publishing FMT there could colour how mainstream consciousness scientists read it.
- **R7: Unverified figures.** Several limits and APCs came from search excerpts because publisher sites returned 403 (flagged "Search" in the table). Scopus indexing of PhiMiSci and the BBS fee position were not confirmed. Re-check the chosen venue's live guideline page before building.
- **R8: Timing (S297).** Journal submissions land around MoC7, not before, so a fast desk reject cannot precede the conference. Preprints can go ahead now.

**Recommended sequence:** JAIC slice (AIW-130) first, as the best-odds single submission. Then the PhiMiSci condensed framework paper, *if* MG accepts the R2 disclosure; otherwise the BioSystems version. The full paper goes into the monograph (AIW-149), and the Zenodo concept DOI remains the canonical full text.
