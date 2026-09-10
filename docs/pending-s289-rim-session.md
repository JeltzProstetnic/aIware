<!-- Action: reference -->
<!-- Tracked-by: AIW-126 (the RIM revision) — the only item here still open -->
<!-- S290 CLOSED: section 1 (AIW-157 citation labels) DONE, gate green. Section 3 (AIW-133 Schoff vs SB-HC4A) DONE, verdict do-not-cite, see docs/decisions.md + docs/aiw133-schoff-cru-cosmology-analysis.md. Section 2 partially done — see docs/pending-rim-s290-remaining.md for what AIW-126 still owes. Kept for the section-4 lesson only; do NOT re-present sections 1 or 3. -->
# S290 is the RIM session — MG, 2026-08-06

MG set this directly at the end of S289: *"fold in and do it first thing next session, next session is rim
session."* The fold is done in the backlog; this file is the brief.

---

## 1. FIRST — the 9 citation labels (`AIW-157`), before any reframing

`pytest scripts/test_build_rim.py` is **red**, and it is red because the paper is wrong. Nine bibitems in
`paper/intelligence` have three or more authors but carry a two-author in-text label:

| Label as written | Authors in the bibitem |
|---|---|
| Balboni & Naglieri, 2021 | 3 |
| von Stumm & Chamorro-Premuzic, 2011 | 3 |
| Cacioppo & Jarvis, 1996 | 4 |
| Duckworth & Kelly, 2007 | 4 |
| Hilger & Basten, 2020 | 4 |
| Jaeggi & Perrig, 2008 | 4 |
| Murayama & Hofe, 2013 | 4 |
| Ziegler & Bühner, 2012 | 4 |
| Sternberg & Preiss, 2021 | 6 |

**How to fix it, and the constraint that matters:** `CLAUDE.md` forbids editing `.tex` directly — fix the `.md`
and regenerate. **Gate: the test must go green before anything else is touched.** Do not `xfail` it.

**Why it was invisible:** the test lived in gitignored `tmp/`, so it had not run in months. `AIW-145` moved it
into tracked `scripts/` on 2026-08-06 and it failed on the first run. **RIM's preprint is already public**
(`10.5281/zenodo.20125096`), so these nine are out in the world — which is the argument for doing them first
rather than rolling them into a big revision that may not land for weeks.

## 2. Then the revision proper (`AIW-126`)

Full scope is in the backlog item; the load-bearing parts:

- **(a) Reframe the third pillar** — "motivation as the third column of intelligence" → **consciousness /
  free-modelling**, per current FMT. MG S268: the motivation frame is outdated. This is the substantive change
  and everything else is bookkeeping around it.
- **(b) Remove the stray front-matter metadata block** (Target journal / Paper type / Status / Previous
  submissions) — it currently renders *into the paper body*.
- **(c) Fold in:** `AIW-81` (Fable corrections), `AIW-86` (COGITO — Brose 2010 + Schmiedek 2020, see
  `docs/pending-rim-cogito-citations.md`, both PDFs filed and read; plus the Bach/Dörner prior-art in
  `drafts/rim-priorart-convergence.md`), and the **Edwards & DeYoung (2026)** "consistent with" cite in §7.1
  (`drafts/rim-edwards-deyoung-cite.md` — drafted, awaiting the go).
- Target journal: **Journal of Intelligence** (MDPI) — Wittmann's recommendation. `AIW-132` (P1) is the
  cognitive-ability-pluralism evidence sift feeding the same reframe; check whether it should run first.

**Build + gate:** `python3 scripts/build_rim_pdf.py` (moved out of `tmp/` on 2026-08-06 — the old path is
dead). `pytest scripts/test_build_rim.py` is the citation gate. `pytest scripts/ -m "not slow"` for the rest.

## 3. Also newly actionable — `AIW-133` is no longer blocked

The item read *BLOCKED on the PDF* for over a week. **It is not.** MG downloaded it 2026-08-06 and it was
sitting in gitignored `literature/fulltext/` unregistered, so nothing surfaced it. Verified and indexed in
`literature/INDEX.md` on 2026-08-06:

`literature/fulltext/Schoff2026-cosmic-compiler.pdf` — Schoff, N.P.J. (2026), *The Cosmic Compiler: The Theorem
of Necessary Existence and the Topological Proof Against the Null State*, 4 pp, ResearchGate publication
**408082009**. The task is to compare its argument to SB-HC4A.

⚠ **Self-published grey literature** — no journal, no DOI, affiliation is the author's own archive. MG's read
was "short, strange, but probably correct." If anything from it is cited, that provenance rides along; the
honest-convergence rule applies regardless of how congenial the argument is. This is cosmology, not RIM — take
it only if the RIM work finishes early.

## 4. Standing lesson from S289, worth one line

A gitignored file is invisible until something indexes it. Two separate failures this session had the same
shape: four "lost" scripts that were actually recoverable (`git log --all -- <path>` finds force-added files
that were later deleted), and a PDF that had been downloaded but never registered. **Before declaring a `tmp/`
or `fulltext/` file missing, look.**
