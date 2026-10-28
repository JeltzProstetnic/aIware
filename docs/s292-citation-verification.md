<!-- Action: reference -->
<!-- Tracked-by: AIW-170, AIW-171, AIW-172 -->
# S292 — independent verification of the S291 citation findings

The S291 defect lists were agent-reported. The S292 work order required each one to be
re-verified before it is fixed, not fixed on trust. This is that record: what was checked,
against what, and what the check returned. Every row below was resolved this session against
Crossref, arXiv or the source PDF — not against the S291 report.

Machine gate: `scripts/verify_references.py` (`AIW-170`), manifest `docs/reference-manifest.json`.

## RIM

| # | S291 claim | Verdict | Evidence |
|---|-----------|---------|----------|
| C1 | `Gignac & Zajenkowski (2024), Intelligence, 104, 101802` is a chimera | **CONFIRMED** | Crossref title-match score 1.0 → Oberleiter, Fries, Dejardin et al. (2024), *Intelligence* **107**, 101867, DOI 10.1016/j.intell.2024.101867 |
| C2 | `Huang, C. (2024), Educational Psychology Review, 36(1)` is a chimera | **CONFIRMED** | Crossref 1.0 → Vu, Scharmer, van Triest, van Atteveldt & Meeter (2024), *Educational Psychology* **44**, 136–170, DOI 10.1080/01443410.2024.2307960 |
| C3 | `Balboni, Ferrandi & Naglieri (2021)` is single-authored Sternberg | **CONFIRMED** | Crossref → Sternberg, R. J. (2021), *J. Intelligence* **9**(4), 58 |
| C4 | McGrew (2009, p. 1) "standard reference point" is fabricated | **CONFIRMED — and worse than reported** | Full-text search of the article PDF: "standard reference point" occurs **zero** times. The only occurrence of "reference point" is on **article p. 9**, inside a **quotation from Jensen** that McGrew reproduces, and it refers to **Carroll's 1993 monograph**, not to the CHC model. So the manuscript mis-words a quote, mis-pages it, mis-attributes it to McGrew rather than Jensen, and re-points it at the wrong object. |
| C5 | §3.1's NFC→Gf / TIE→Gc dissociation is reported opposite to source | **CONFIRMED in substance, with a correct replacement available** | See below. |
| C6 | Wechsler (1944, p. 3) quote is inexact | **CONFIRMED** | Source reads "the **aggregate or** global capacity of **the individual** to act purposefully…"; the manuscript has "the global capacity of **a person** to act purposefully…" inside quotation marks. Two silent alterations. |
| C7 | Rosenthal (2002) is in the reference list but never cited | **REFUTED AS STATED — a different defect is present** | `paper.tex:304` *does* cite it: `\citep{Rosenthal2002}`. The same sentence in `paper.md:277` does not. This is **md↔tex drift**, not an orphan reference, and it is the failure mode the work order warns about (RIM has no md→tex generator). |

### C5 in detail — the judgement call reserved for MG

The manuscript (§3.1) states: *"NFC and TIE, despite being highly correlated (r ≈ .78–.87; von Stumm
& Ackerman, 2013), predict different intelligence facets: NFC correlates primarily with fluid
reasoning (Gf), while TIE correlates primarily with crystallized knowledge (Gc)."*

Three separate problems, and one of them is good news:

1. **The within-trait claim is false.** Schweitzer, Lindenberg, Fleischhauer & Enge (2025),
   *Journal of Intelligence* 13(11), 142, DOI 10.3390/jintelligence13110142 — a multi-level
   meta-analysis — gives NFC–Gf *r* = .19 and NFC–Gc *r* = .24. NFC does **not** correlate
   primarily with Gf; it correlates slightly more with Gc. The Fable agent was right about this.
2. **The between-trait dissociation is real.** Same source, verbatim: *"NFC (r = 0.19) was more
   strongly related to Gf than TIE (r = 0.12; F(1, 12.10) = 5.04, p = .045) whereas TIE (r = 0.35)
   was more strongly associated with Gc than NFC (r = 0.24; F(1, 13.10) = 10.70, p = .006)."*
   The dissociation the paper needs exists and is statistically tested — it is a **contrast between
   the two traits**, not a claim about where each trait's own strongest loading sits.
3. **The correlation is attributed to the wrong paper.** The *r* ≈ .78–.87 NFC–TIE range is reported
   *in* Schweitzer et al. as a summary of prior work; the .78 figure originates with **Woo, Harms &
   Kuncel (2007)**. von Stumm & Ackerman (2013) is an investment-traits meta-analysis whose headline
   estimate is an average investment–intellect coefficient of .30 — it is not the source of either
   the NFC–TIE intercorrelation or the Gf/Gc split.

**Consequence for the work order.** Option (a) — "find a correct illustration" — is available and
does not require softening the abstract: the unity-of-motivation claim keeps a concrete, correctly
sourced empirical illustration if §3.1 is restated as the between-trait contrast Schweitzer et al.
actually test. Whether to take that route, or (b) soften the abstract, or (c) let prediction 9's
matched-*k* contrast carry it alone, is MG's call and is not decided here.

## Cosmology

All five verified this session against Crossref/arXiv directly.

| Manuscript entry | Verdict | What the record says |
|---|---|---|
| `Rubio, J., & Dunningham, J. (2020) … arXiv:2007.04849` | **CONFIRMED defective** | arXiv:2007.04849, "Physics-inspired forms of the Bayesian Cramér-Rao bound", is by **Mankei Tsang**, sole author. Title correct, authors wrong. |
| `Boyle, L., & Turok, N. (2022b) … Physics Letters B, 849, 138442` | **CONFIRMED defective** | *Phys. Lett. B* **849**, 138442 is dated **2024**, DOI 10.1016/j.physletb.2024.138442. Authors and title correct, year wrong. |
| `Konopka, T., Markopoulou, F., & Smolin, L. (2008) … PRD 77(10), 104029` | **CONFIRMED defective** | *Phys. Rev. D* **77**, 104029, "Quantum graphity: A model of emergent locality", is **Konopka, Markopoulou & Severini**. Smolin is not an author. |
| `Bisio, A., D'Ariano, G. M., & Tosini, A. (2015) … Annals of Physics, 368, 177–190` | **CONFIRMED defective — three-way chimera** | *Ann. Phys.* **368**, 177–190 is **Bisio, D'Ariano & Perinotti (2016)**, "Quantum cellular automaton theory of light". The *title* in the manuscript entry belongs to a third paper: **Brun & Mlodinow**, *Phys. Rev. A* **102**, 062222 (2020). Author list, year, title and venue each come from somewhere different. |
| `Rowland, E. (2006). Wolfram's classification and its extensions. NKS Conference Proceedings.` | **CONFIRMED defective** | No such title is findable. Rowland's actual 2006 paper is **"Local Nested Structure in Rule 30", *Complex Systems* 16, 239–258** — which does support the §64 claim about nested/fractal patterns deserving separate classification. Substance survives; the citation does not. |

## What this exercise says about the gate (`AIW-170`)

The gate caught C1–C3 mechanically, from a different route than S291 used (Crossref
title-matching rather than manual lookup), and it caught Rubio→Tsang and Boyle's year on its own.

It also failed twice, and both failures are now fixed and regression-tested:

- **`Konopka2008` passed as `verified`.** The adjudicator compared only the *first* author, and the
  defect is in position three. Comparing the full surname roster is now part of adjudication
  (`test_a_wrong_coauthor_is_caught`). Crossref author truncation is treated as absence of
  evidence, not as a mismatch.
- **`Gruber2015` and `Gruber2026` are cited in both papers**, and a flat manifest namespace gave
  one row to two different entries — so one paper would silently inherit a verdict the other
  earned. Manifest rows are now namespaced by paper (`rim:` / `cosmology:`).

Neither failure was visible from the passing test suite until a test was written for it. That is
the same lesson one level down: a check that has never been shown to fail has not been shown to work.
