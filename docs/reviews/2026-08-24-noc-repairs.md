# NoC reference/citation repairs — agent record, 2026-08-24

Scope worked: `paper/trimmed/noc/` only (`.md`, hand-maintained `paper.tex`, `references.bib`).
Nothing under `paper/full/` or `paper/intelligence/` was touched.

**Pipeline fact established before editing:** the NoC `.tex` is **hand-maintained**, not generated.
`scripts/build_noc_pdf.py` *copies* `paper/trimmed/noc/*.tex` and `*.bib` into `tmp/build-noc/` and
runs `pdflatex`+`bibtex`; there is no `.md → .tex` step anywhere in it. So `.md` is the source of
truth and the `.tex` was mirrored by hand, per the project rule.

---

## 1. Edits applied

### A1 — Wigner is 1962, not 1961

| file:line | before | after |
|---|---|---|
| `four-model-theory-noc.md:268` | `…quantum mechanics (von Neumann, 1932; Wigner, 1961) are rejected.` | `…quantum mechanics (von Neumann, 1932; Wigner, 1962) are rejected.` |
| `four-model-theory-noc.md:751` | `Wigner, E. (1961). Remarks on the mind-body question. In I.J. Good (Ed.), *The Scientist Speculates*. Heinemann.` | `Wigner, E.P. (1962). Remarks on the mind-body question. In I.J. Good (Ed.), *The Scientist Speculates: An Anthology of Partly-Baked Ideas* (pp. 284-302). Heinemann.` |
| `references.bib:1040` (entry `@incollection{Wigner1961}`) | `year = {1961},` | `year = {1962},` |

Bibtex **key left as `Wigner1961`** deliberately: the entry is *not cited* anywhere in
`paper.tex`, so the key is inert, and renaming it here would put the NoC key space out of step with
`paper/full/latex/references.bib`, which I may not touch. Flagged below as a cosmetic follow-up.

**Not done, flagged for MG:** the drafts write-up offered a one-clause note in the reference entry
pre-empting a reviewer who knows the essay as "Wigner 1961". That was explicitly put to MG as a
thing to weigh, not part of the repair, so I left it out. One clause, trivially added later.

### A2 — no joint Penrose–Hameroff 1994 exists; it is Hameroff & Penrose (1996)

| file:line | before | after |
|---|---|---|
| `four-model-theory-noc.md:485` | `…quantum processes in microtubules (Penrose & Hameroff, 1994; though see Tegmark, 2000…` | `…quantum processes in microtubules (Hameroff & Penrose, 1996; though see Tegmark, 2000…` |
| `four-model-theory-noc.md` list | entry deleted from the P position (was `:697`) | new entry inserted at the **H** position (`:643`, between Güntürkün 2016 and Hengen & Shew 2025), verbatim the master's string incl. DOI |
| `paper.tex:630` | `\citep{PenroseHameroff1994}` | `\citep{HameroffPenrose1996}` |
| `references.bib` | `@article{PenroseHameroff1994}` at the P position, author order reversed, `year = {1994}`, no DOI | `@article{HameroffPenrose1996}` moved to the H position, `author = {Hameroff, Stuart and Penrose, Roger}`, `year = {1996}`, `doi = {10.1016/0378-4754(96)80476-9}` added |

New list entry text (identical to `paper/full/four-model-theory-full.md:1282`, so the two papers now
carry the same string):

> Hameroff, S. & Penrose, R. (1996). Orchestrated reduction of quantum coherence in brain microtubules: A model for consciousness. *Mathematics and Computers in Simulation*, 40(3-4), 453-480. https://doi.org/10.1016/0378-4754(96)80476-9

The topical `% Quantum consciousness and decoherence` banner comment moved with the entry, so the
bib stays alphabetical by key with its section banners intact.

### B3 — Pinto et al. (2017) presented as FMT's reinterpretation, not their finding

`four-model-theory-noc.md:360` and `paper.tex:471` (final sentence of §6.4 Split-Brain).

- **before:** `Graded rather than binary deficits (Pinto et al., 2017) are consistent with holographic degradation.`
- **after:** `Graded rather than binary deficits (Pinto et al., 2017) are consistent with holographic degradation, though Pinto et al. themselves conclude that callosotomy splits perception without creating two independent conscious perceivers: the theory reinterprets their data rather than inheriting their conclusion.`

`.tex` uses `\citeauthor{Pinto2017}` for the second mention (natbib is loaded — `\citeauthor` was
already in use at line 310). +26 words.

### B4 — Hengen & Shew (2025) re-scoped to what they actually conclude

| file:line | before | after |
|---|---|---|
| `.md:223` / `.tex:304` (table row) | `Hengen & Shew — meta-analysis of 140 datasets confirms criticality` | `Hengen & Shew — meta-analysis of 140 datasets; criticality as a setpoint of brain function` |
| `.md:226` / `.tex:310` | `The later large-scale consolidation (Hengen & Shew, 2025; Algom & Shriki, 2026) confirmed the criticality-consciousness link across 140 datasets.` | `The later large-scale consolidation of 140 datasets (Hengen & Shew, 2025) supports criticality as a setpoint of brain function; the ConCrit framework (Algom & Shriki, 2026) extends that consolidation into an explicit criticality-consciousness account.` |

**⚠ One edit beyond the audit's named lines**, flagged for review and trivially revertible:

| `.md:511` / `.tex:663` (Conclusion) | `The criticality requirement… was independently confirmed by the later empirical consolidation (Hengen & Shew, 2025; Algom & Shriki, 2026).` | `The criticality requirement… converges with the later empirical consolidation (Hengen & Shew, 2025; Algom & Shriki, 2026).` |

Reason: identical defect, identical citation pair — the master's parallel sentence (line 887) is on
the audit's own repair list ("drop 'independently confirmed it'"). Two-word change. The abstract
(`.md:15`) was checked and needs nothing — it already says "converges with… consolidated in 2025-2026".

---

## 2. Sources verified (nothing inserted unverified)

| claim | how verified | result |
|---|---|---|
| Heinemann 1st ed. of *The Scientist Speculates* is **1962** | **Primary record.** Fetched `gwern.net/doc/science/1962-good-thescientistspeculates.pdf` and read the scanned title + copyright pages directly | Title page: `HEINEMANN / LONDON MELBOURNE TORONTO`. Copyright page: **"William Heinemann Ltd … First published 1962. © I. J. Good, 1962. All rights reserved. Printed in Great Britain by The Windmill Press Ltd, Kingswood, Surrey."** The 1961 is unsupported by the edition itself. |
| Wigner essay pages | Same scan, table of contents (printed p. xv) + body pages 298–302 | `7 PHYSICS … 284 / 98 Remarks on the Mind-Body Question: EUGENE P. WIGNER … 284 / 99 … DAVID BOHM … 302`. Chapter body ends p. 301; the editor's addendum to Wigner's chapter runs onto p. 302, where Bohm then begins. **pp. 284-302 is correct.** |
| no 1961 edition elsewhere | Internet Archive advanced search + item metadata `scientistspecula0000irvi` | US Basic Books edition catalogued as **1962** (a second IA record gives a 1963 Basic Books printing). No 1961 record found. A web summary asserted "Heinemann, London, 1961" — **contradicted by the book itself**; this is the propagation. |
| Hameroff & Penrose (1996) metadata | Crossref REST: `api.crossref.org/works/10.1016/0378-4754(96)80476-9` | Title *"Orchestrated reduction of quantum coherence in brain microtubules: A model for consciousness"*; authors **Stuart Hameroff, then Roger Penrose**; *Mathematics and Computers in Simulation* **40(3-4), 453-480, 1996**. Every field of the inserted entry confirmed. |
| Pinto et al. (2017) conclusion | Full abstract read at `academic.oup.com/brain/article/140/5/1231/2951052`; DOI confirmed via Crossref bibliographic query = `10.1093/brain/aww358` | Verbatim closing sentence: *"These findings suggest that severing the cortical connections between hemispheres splits visual perception, **but does not create two independent conscious perceivers within one brain.**"* Title, authors, *Brain* 140(5) 1231–1237 all match the NoC list entry. |
| Hengen & Shew (2025) object and conclusion | Verbatim abstract via Europe PMC REST (`ebi.ac.uk/europepmc/webservices/rest`), metadata cross-checked at Crossref and CoLab | *"…We perform a meta-analysis of **140 datasets** published between 2003 and 2024. We find that a long-standing controversy is the product of a methodological choice with no bearing on underlying dynamics. Our results suggest that a new generation of research can leverage criticality—as a **unifying principle of brain function**…"* **No consciousness conclusion anywhere in the abstract.** *Neuron* 113(16):2582-2598.e2, DOI `10.1016/j.neuron.2025.05.020`. The NoC list entry at `.md:643` is already correct and was not touched. |

---

## 3. Gate + build results

**`python3 scripts/verify_references.py --check` → EXIT 1, 4 problems, all of them the expected
manifest bookkeeping for the repair:**

```
  - noc:Hameroff1996 is not in the manifest — resolve it against Crossref and run --update
  - noc:Penrose1994 is in the manifest but no longer appears in the paper — drop the row…
  - noc:Wigner1961  is in the manifest but no longer appears in the paper — drop the row…
  - noc:Wigner1962  is not in the manifest — resolve it against Crossref and run --update
```

Baseline before my edits was **2** problems — the two `needs-review` rows this task retires
(`noc:Penrose1994`, `noc:Wigner1961`). The bib-drift arm is **clean** (it runs inside `--check` and
reported nothing). `docs/reference-manifest.json` is **outside my write scope and shared with the
two agents editing the other papers**, so I did not touch it. Ready-to-apply patch in §4.

**Other tests** (run from the repo root):
- `pytest scripts/test_content_integrity.py scripts/test_verify_references.py -q` → **113 passed**.
  This includes the `MAX_UNVERIFIED = 2` ratchet, which now sees **0** unverified NoC references.
- `pytest scripts/test_verify_bib_drift.py scripts/test_check_md_pdf_drift.py -q` → 53 passed,
  **1 failed: `TestRealPaper::test_rim_md_and_built_pdf_agree`**. That failure is the **RIM** paper
  ("eight (later nine)", Oberleiter et al.) — the concurrent `paper/intelligence/` agent's in-flight
  edits, not mine. NoC is not covered by `check_md_pdf_drift` (`--paper` choices don't include it).

**Build (into `tmp/` only — no canonical PDF recompiled):** `python3 scripts/build_noc_pdf.py` →
`tmp/noc-paper.pdf`, 40 pages.
- `paper.blg`: **0 bibtex warnings**. `paper.log`: **0 undefined citations**.
- PDF text confirms `(Hameroff and Penrose, 1996)` in prose, the new H-position list entry with its
  DOI, the Pinto hedge sentence, and both re-scoped Hengen & Shew passages.
- **Overfull `\hbox` count unchanged at 7, byte-identical measurements.** Verified by building
  `git show HEAD:` versions of `paper.tex`/`references.bib` into a throwaway `tmp/build-noc-baseline/`
  (since deleted) — same 7 warnings, same pt values, same 40 pages. My longer table cell introduces
  no new overflow.

⚠ `tmp/build-noc/*` and `tmp/noc-paper.pdf` are **legacy-tracked** (they predate the `tmp/` line in
`.gitignore`, so the ignore rule does not cover them) and the verification build modified them. I ran
`git checkout -- tmp/build-noc tmp/noc-paper.pdf` afterwards, so the working tree carries **only** the
three `paper/trimmed/noc/` source changes. Re-run `python3 scripts/build_noc_pdf.py` to reproduce the
build described above. (Separately: those tracked `tmp/` artifacts are an `AIW-145`-shaped leftover —
`git rm --cached` on them would stop every future build dirtying the tree.)

**Word count:** body (everything before the `References` heading) went **10,029 → 10,073 words**
(+44). ⚠ Note it was **already over** both stated ceilings before I touched it — 9,000 for an OUP
*NoC* Research Article (`journal-guidelines-noc.md`) and 9,500 in `four-model-theory-noc.formatting-rules.md`,
which themselves disagree. My +44 does not create the overage but does not help it; the two hedges
are the shortest accurate forms I could write.

---

## 4. Manifest patch — ready to apply, NOT applied

In `docs/reference-manifest.json`, under `"references"`: **delete** `noc:Penrose1994` and
`noc:Wigner1961`, **add** the two rows below. Fingerprints computed with the script's own
`verify_references.fingerprint()` against the repaired `.md`, so they will match `--check` exactly.

```json
"noc:Hameroff1996": {
  "fingerprint": "d11494937ed6ad8f",
  "first_author": "Hameroff",
  "year": 1996,
  "doi": "10.1016/0378-4754(96)80476-9",
  "crossref_title": "Orchestrated reduction of quantum coherence in brain microtubules: A model for consciousness",
  "crossref_first_author": "Hameroff",
  "crossref_year": 1996,
  "crossref_journal": "Mathematics and Computers in Simulation",
  "crossref_volume": "40",
  "title_score": 1.0,
  "status": "verified-manual",
  "confirmed_by": "hand-verification 2026-08-24",
  "note": "Replaces the nonexistent joint 'Penrose & Hameroff (1994)' (former row noc:Penrose1994). Entry text is byte-identical to fmt:Hameroff1996, hence the shared fingerprint. Resolved directly against Crossref api.crossref.org/works/10.1016/0378-4754(96)80476-9: title, author order (Hameroff then Penrose), journal, volume 40, issue 3-4, pages 453-480 and year 1996 all match the entry. Hand-verified rather than auto-verified because _doi() truncates this parenthesised Elsevier DOI to '10.1016/0378-4754(96', so --update cannot resolve it by DOI and silently falls back to a bibliographic query."
},
"noc:Wigner1962": {
  "fingerprint": "0c5e3bd1760282c9",
  "first_author": "Wigner",
  "year": 1962,
  "doi": "10.1007/978-3-642-78374-6_20",
  "crossref_title": "Remarks on the Mind-Body Question",
  "crossref_first_author": "Wigner",
  "crossref_year": 1995,
  "crossref_journal": "Philosophical Reflections and Syntheses",
  "crossref_volume": null,
  "title_score": 1.0,
  "status": "verified-manual",
  "confirmed_by": "hand-verification against the first-edition scan 2026-08-24",
  "note": "Pre-DOI original. Crossref indexes only the 1995 collected-works reissue (10.1007/978-3-642-78374-6_20), which is the whole of its year objection. The Heinemann first edition's own copyright page reads 'William Heinemann Ltd, LONDON MELBOURNE TORONTO ... First published 1962. (c) I. J. Good, 1962' (scan: https://gwern.net/doc/science/1962-good-thescientistspeculates.pdf, PDF p.2). Its table of contents lists item 98, 'Remarks on the Mind-Body Question: EUGENE P. WIGNER', at p.284, with item 99 (Bohm) beginning on p.302; the Wigner chapter plus its editorial addendum runs to p.302. Internet Archive catalogues the US Basic Books edition as 1962 (scientistspecula0000irvi). No 1961 edition record was found in any catalogue; the ubiquitous 1961 is citation propagation. Every field the entry asserts is confirmed against the first edition itself."
}
```

Also worth doing in the same pass: `scripts/test_verify_references.py:934` still carries
`MAX_UNVERIFIED = 2`; with both NoC rows retired the true count is **0**, so the ratchet can be
lowered to 0 to stop it drifting back up.

---

## 5. Could not reach — other agents own these files

Reported, not edited. Each is a confirmed instance of a repair I made in NoC.

| location | what needs doing |
|---|---|
| `paper/full/four-model-theory-full-tracked.md:344` and `:1022` | Wigner `1961 → 1962` in prose and in the reference list (drafts write-up cites these two lines). **Under `paper/full/`.** |
| `paper/full/four-model-theory-full-tracked.md:713` and `:966` | `Penrose & Hameroff, 1994 → Hameroff & Penrose, 1996`, list entry replaced with the master's string and moved to the H position. **Under `paper/full/`.** |
| `paper/full/latex/references.bib:960` (`@incollection{Wigner1961}`) | `year = {1961} → {1962}`. **Under `paper/full/`.** This is the master's shared bib, not NoC's. |
| `paper/cc/four-model-theory-cc.md` | Carries both defects (Wigner 1961, Penrose & Hameroff 1994). **Not** under `paper/full/`, but outside the `paper/trimmed/` write scope I was given, and I had no way to confirm no other agent owns it, so I left it alone. Mechanical: same two substitutions. |
| `docs/reference-manifest.json` | §4 patch. Shared with the concurrent agents — apply once, after they finish. |

Cosmetic, low priority: once the master's bib is editable, both `@incollection{Wigner1961}` keys
(NoC and master) would ideally be renamed `Wigner1962` so the key stops contradicting its own `year`
field. Must be done in both bibs in the same commit or the key spaces diverge.

---

## 6. Findings the audit did not have

**(a) `verify_references.py::_doi()` truncates parenthesised DOIs — and it has already produced one
wrong "verified" row.** The regex is `r"\b10\.\d{4,9}/[^\s,;)\]]+"`; the excluded `)` cuts every
legacy Elsevier PII DOI at the first parenthesis. Measured:

```
10.1016/0378-4754(96)80476-9  -> '10.1016/0378-4754(96'
10.1016/S0010-0277(00)00123-2 -> '10.1016/S0010-0277(00'
10.1016/S0028-3932(02)00158-6 -> '10.1016/S0028-3932(02'
10.1016/0140-1750(87)90034-0  -> '10.1016/0140-1750(87'
10.1016/0010-0285(73)90004-2  -> '10.1016/0010-0285(73'
10.1016/S0160-2896(96)90016-1 -> '10.1016/S0160-2896(96'
```

Six such DOIs exist in the corpus (4 in registered papers: `fmt` ×3, `fmt_formal` ×1, plus the one I
just added to `noc`; 2 more in `docs/references.md`). `crossref_candidates()` fetches the truncated
DOI, gets nothing, and **silently falls back to a bibliographic query** — so the failure is invisible.
Three of the four landed on the right work anyway (`fmt:Dehaene2001`, `fmt:Doyon2003`,
`fmt_formal:Kauffman1987` — the last one's manifest row even carries the full untruncated DOI,
because it came from the Crossref record rather than the parse). **`fmt:Hameroff1996` did not:** its
row is `"status": "verified"` against `"doi": "10.7551/mitpress/6860.003.0045"`,
`"crossref_journal": "Toward a Science of Consciousness"` — the MIT Press *book chapter*, a different
publication from the *Mathematics and Computers in Simulation* article the entry cites, at
`title_score 0.983` ("A Model **of** Consciousness" vs "A Model **for** Consciousness"). That is
precisely the wrong-work-under-a-passing-status class the S302/S305 work exists to catch, and the
DOI truncation is what hid it. Suggested fix: allow balanced parentheses in the DOI body, e.g.
`r"\b10\.\d{4,9}/(?:\([^\s()]*\)|[^\s,;\]])+"`, plus a regression test over all six literals above.
TDD-gated and in `scripts/`, so I did not touch it.

**(b) The NoC `.tex` and `.md` are not the same paper — two citations are in one and not the other.**
1. `.tex` has **zero footnotes** (`grep -c footnote` finds only `\footnotesize`). The `[^quantum]`
   footnote — the whole von Neumann / Wigner / Zurek corollary — exists only in the `.md`. So
   `Wigner1961` sits in `references.bib` **uncited**, never prints in the LaTeX PDF, and my Wigner
   repair reaches the `.docx` route but has nothing to reach in the LaTeX route.
2. `.md:360` cites `(Gazzaniga, Bogen, & Sperry, 1962, **1965**; Gazzaniga, 2000)`; `.tex:471` cites
   only `\citep{Gazzaniga1962,Gazzaniga2000}`. `Gazzaniga1965` — the entry S306 just repaired out of
   a three-way chimera — is **uncited in the `.tex`** and therefore absent from the LaTeX PDF's
   bibliography, while the `.md` list carries it. Left alone deliberately: adding a key to `\citep`
   changes what the printed PDF cites, and I was asked to keep edits minimal. One-line fix if wanted:
   `\citep{Gazzaniga1962,Gazzaniga1965,Gazzaniga2000}`.

**(c) Two contradictory documented build routes for the same paper, producing different manuscripts.**
`four-model-theory-noc.formatting-rules.md:33` states **"No .tex output — this paper goes directly
from .md to .docx"** via bare `pandoc`, yet `scripts/build_noc_pdf.py` builds `.tex → PDF` and
`.tex → .docx`. Given (b), those two `.docx` files differ in content, not just formatting. I checked
the committed `paper/trimmed/noc/four-model-theory-noc.docx`: `word/footnotes.xml` contains the
quantum corollary, so **it came from the `.md`/pandoc route** — but it is dated 2026-03-16 and is
**stale**: it still reads "(von Neumann, 1932; Wigner, **1961**)" and has **no** Gazzaniga 1965 list
entry. It must be rebuilt before submission, and the formatting-rules file should be reconciled with
`build_noc_pdf.py` rather than left contradicting it.

**(d) `paper/trimmed/arxiv/` holds only stale build leftovers.** `paper.aux` still carries
`\citation{PenroseHameroff1994}` and `\bibcite{PenroseHameroff1994}{{65}{1994}…}`. There is no `.tex`
or `.md` source in that directory — just `.aux/.blg/.log/.out`. Harmless, regenerated on any build,
but it will keep matching greps for the retired key. Candidate for deletion.

**(e) Related Pinto usage left in place, for a decision rather than a repair.** `.md:451` /
`.tex:590`, §8.6 Prediction 6: *"**Testability**: High. Pinto et al. (2017) provide preliminary
evidence."* Unlike the §6.4 sentence, this does not assert a conclusion Pinto rejects — their data
genuinely bears on the graded-vs-binary question — so I applied the rule "hedge where the text
attributes to a source a conclusion the source contradicts; report where it is merely ambiguous."
If MG wants it tightened, the shortest form is *"Pinto et al. (2017) provide preliminary evidence of
graded rather than all-or-none division."*

**(f) Bibliographic nit, `fmt_formal` (not touched).** `paper/fmt_formal/fmt-formalization.md:661`
gives Kauffman 1987's journal as *Journal of Social and Biological **Structures*** while the manifest's
`crossref_journal` for that row reads *"…Biological **Systems**"*. The `.md` is right — the journal
was *Structures* until 1998 — so this is Crossref metadata noise, not a paper defect. Recording it
only so a future pass doesn't "fix" the correct side.
