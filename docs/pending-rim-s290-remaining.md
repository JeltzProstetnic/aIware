<!-- Action: reference -->
<!-- Tracked-by: AIW-126 (RIM revision), AIW-170 (citation-gate gap) -->
# RIM after S291 — what is done, and the one thing that needs MG

> **SUPERSEDED S291 late (2026-08-07). Historical record only — do NOT act on this file.**
> The Zenodo decision below was answered by MG ("then publish") and then **overtaken**: the S291 Fable pass
> found three Crossref-confirmed chimeric citations, a fabricated quotation and a source contradiction in
> RIM. **RIM is blocked from publishing until `AIW-171` closes.** Current work order:
> `docs/pending-s292-worklist.md`. Defect list: `docs/pending-s291-fable-defects.md`.
> **S292 (2026-08-07): `AIW-171` closed and RIM IS PUBLISHED** — Zenodo v3, version DOI
> `10.5281/zenodo.21841307`. Nothing in this file is actionable.

S290 closed `AIW-157`, `AIW-86`, `AIW-133` and `AIW-158` and landed most of `AIW-126`.
**S291 (2026-08-07) cleared the entire remainder except the Zenodo publish.**

## Done in S291 (do not redo)

1. **`AIW-81` — the Fable corrections to RIM. CLOSED.** The S291 audit found that *none* of it had ever been
   applied: van der Maas / Dickens & Flynn / Savi, Friston, Schmidhuber / Pathak / Oudeyer and Dörner / Bach
   were absent from both `.md` and `.tex`. All are now in, in both files. The two structural rulings MG made
   this session (§6.3 calibrated not cut; consciousness demoted to a boundary condition) are applied.
2. **`AIW-132` — Edwards & DeYoung.** Inserted in §7.1. DOI **verified** (resolves; journal, authors, year and
   both sample sizes confirmed). The published figure is **30–57%**, not the 30–40% in our draft; the source
   figure is what the paper now states.
3. **Verification debt — CLEARED.** See `docs/pending-rim-verification-debt.md`. The Flynn primary was
   obtained via a peer-reviewed route (Flynn & Weiss 2007, *Int. J. Testing* 7(2), Table 2), stored at
   `literature/fulltext/FlynnWeiss2007.pdf` and indexed. **Two published figures were wrong and are fixed.**
4. **Canonical PDF rebuilt.** `paper/intelligence/paper.pdf` — 44 pp, ~17k words, zero overfull boxes, no
   undefined citations or references, citation gate green, 46/46 tests passing.
5. **§7.3's third limb and prediction 8 now read as one programme**, as Fable asked: predictions 7, 8 and the
   §7.3 coupling limb are stated as three read-outs of a single experience-sampling design.

Beyond the handoff, two defective citations were found and corrected (Hilger — fabricated volume/article plus
an inverted claim; Jussim & Harber — cited for the opposite of its conclusion) and prediction 7 was given an
explicit disconfirmation criterion. Full rationale: `docs/decisions.md` S291.

## The one thing that needs MG — the decision this file is waiting on

**Cut a new Zenodo version of RIM?** The canonical PDF now lags the public preprint
(`10.5281/zenodo.20125096`) by the whole revision, including the six S290 preprint-live citation fixes.
MG's S290 ruling was to bundle the corrections with the full revision rather than bump a corrections-only
version — that condition is now met.

**This was deliberately NOT done unprompted.** Publishing is outward-facing and effectively irreversible:
a Zenodo version DOI cannot be withdrawn cleanly, and the revision is substantial enough that MG should read
it first. Publish only on an explicit go.

Command when approved:
`ZENODO_CONCEPT_DOI=<rim concept doi> ZENODO_VERSION=vN ZENODO_CHANGELOG=<changelog.md> bash scripts/zenodo-upload.sh paper/intelligence/paper.pdf`

Also unstarted, and lower priority: republishing to **OSF `kctvg`** (named in the original `AIW-81` spec).

## Two standing constraints for whoever picks this up

- **There is no md→tex generator for RIM.** `scripts/build_rim_pdf.py` only compiles the hand-maintained
  `.tex`. Every content change must be made in **both** `paper.md` and `paper.tex`, or the two drift — which
  is exactly how the six S290 defects got into the published preprint. S291 mirrored every change by hand and
  verified the sync by phrase-level cross-check; there is still no automated guard on this.
- **Verify citations already in the manuscript, not only the ones being added.** S290's lesson was to verify a
  premise before building on it. S291's is that a reference sitting quietly in the bibliography for months can
  be fabricated, and the test suite will not notice (`AIW-170`).
