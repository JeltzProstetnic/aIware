# AIW-179 / AIW-156 — cosmology md↔tex↔pdf drift: diagnosis

Investigated 2026-08-24. Read-only except this file. No `--canonical` was passed; no committed
`.tex` or `.pdf` was touched; nothing was committed. Builds went to `tmp/build-cosmology/<paper_id>/`.

---

## Verdict (one paragraph)

**The defect AIW-179 describes no longer exists, and the guard is now protecting the wrong file.**
Both cosmology papers build end-to-end from their own `.md` (this validates AIW-156's third script —
`SUCCESS` on both, zero LaTeX errors, zero undefined references). `paper/cosmology/sb-hc4a.tex`
regenerates **byte-identically** from its `.md` (sha256 `acc165a0…`), and
`paper/cosmology_formal/sb-hc4a-formalization.tex` now regenerates with a **10-insert/10-delete diff
that is one paragraph's line-wrapping and nothing else** — same byte count (141,014 both), and
whitespace-insensitive comparison is *identical*. The 357/119 divergence S293 recorded was real, was
diagnosed correctly (the `.md` moved ahead, the `.tex` was never regenerated), and was **repaired at
S300** by commit `b5efa1c4` on MG's explicit go — the backlog entry for AIW-179 already says so; only
`CLAUDE.md` and AIW-156 still describe the old state. What is *actually* broken now is one file down:
**`paper/cosmology/sb-hc4a.pdf` is three commits stale against its own `.md`/`.tex`** (66pp/189,487
chars committed vs 68pp/196,817 chars built), missing §7.0's terminology note, the AIW-188 Φ-composition
definition and the AIW-184 jointness clauses. And the single load-bearing premise behind the guard is
false for this pipeline: **neither paper contains a `\cite` command or a `.bib` file**, so the
Session-106 bibtex-`???` mechanism cannot occur here at all.

---

## Divergence inventory

### Paper 3 — `paper/cosmology/sb-hc4a.{md,tex,pdf}`

| Artifact | Committed | Regenerated from `.md` | Class |
|---|---|---|---|
| `.tex` | sha256 `acc165a076be…cb17` | sha256 `acc165a076be…cb17` | **none — byte-identical** |
| `.pdf` | 66 pp, 189,487 chars | 68 pp, 196,817 chars | **(d) stale** |

The `.tex` has **zero** divergence. The `.pdf` is the defect.

`git log` shows why: the PDF was last committed in `4d4e65f9` (2026-08-08). The `.md` and `.tex` then
advanced together through three further commits **the same day** — `9c84be9e`, `f11dac3f`, `ccc5ff99` —
and the PDF was never rebuilt. Commit `ddc20a1c` (2026-08-12) names this out loud: *"The cosmology MAIN
paper has ~23h of pre-existing source/PDF drift from 8 August that predates this session and is
untouched."*

`check_md_pdf_drift.py` against the **committed** PDF returns 14 segments; against the **freshly built**
PDF it returns 8, all 8 in the documented false-positive classes (`∫`→`R`, `w₀wₐCDM` subscript split,
math extraction, the email/Abstract join). The 6 extra segments are the real gap, and every one of them
is `md-only` — **there is no `pdf-only` content whatsoever**. Specifically absent from the committed PDF:

- **§7.0 "A Note on Terminology"** — the whole section (AIW-162, `f11dac3f`). Consequence: the committed
  PDF still says "simulation" **22** times where the `.md` and the fresh build say it **9** times. The
  retired terminology is live in the published artifact.
- **The AIW-188 Φ-as-composition definition** plus the capacity answer to the redescription objection
  (`ccc5ff99`) — `redescription` appears 1× in `.md` and fresh PDF, **0×** in the committed PDF.
- **The AIW-184 jointness / minimality clauses in §6.5** (`9c84be9e`) — `jointness` 1× in `.md` and fresh
  PDF, **0×** in the committed PDF. These are the clauses the S296 handover calls *load-bearing*, "must
  travel with every restatement", without which the postulate is a refuted local-hidden-variable model.

Classification: **(d) stale — the `.md`/`.tex` side is CORRECT.** How I know: the `.tex` regenerates
byte-identically from the `.md`, so `.md` and `.tex` cannot disagree; the fresh PDF built from that
`.tex` matches the `.md` to within the documented extraction artifacts; and every divergent segment is
present on the source side and absent on the PDF side, never the reverse. There is nothing the PDF
knows that the source does not.

### Paper 6 — `paper/cosmology_formal/sb-hc4a-formalization.{md,tex,pdf}`

| Artifact | Committed | Regenerated from `.md` | Class |
|---|---|---|---|
| `.tex` | 141,014 bytes | 141,014 bytes | **(a) formatting noise, from a (b) hand-edit** |
| `.pdf` | 47 pp, extracted-text sha `882d4c59370a` | 47 pp, extracted-text sha `882d4c59370a` | **none — text-identical** |

The entire `.tex` diff is one paragraph in the James–Stein/Tsang passage, re-wrapped:

```
-on top of it, not something Tsang proves. Second, the
-classical James-Stein estimator uses the harmonic prior ‖θ‖\^{}(2−d),
+on top of it, not something Tsang proves. Second, the classical
+James-Stein estimator uses the harmonic prior ‖θ‖\^{}(2−d), which is the
```

`diff <(tr -s ' \n' ' ' < committed) <(tr -s ' \n' ' ' < regenerated)` → **identical**. Zero content
difference; zero words gained or lost.

**Class (a) at the surface, but it is the fingerprint of a class (b) breach**, and the breach is
locatable to the commit:

- **`ea9213f8` (2026-08-12, AIW-209)** inserted the Tsang re-attribution *directly into the generated
  `.tex`* with hand-chosen line breaks. Its own commit message calls the file *"the hand-maintained
  `.tex`"* — which is true of `paper/full/` and `paper/intelligence/`, and **false of
  `cosmology_formal`, which is md-generated.** That mislabel is the root cause: the file was edited
  under the rules of a different paper.
- **`ddc20a1c` (2026-08-12)** is a second instance — reference/DOI fixes hand-applied to the `.tex`
  ("The cosmology_formal `.tex` was STILL missing Boyle+Finn and the three Gruber DOIs after the `.md`
  had them"). It left no trace only because its wrapping happened to coincide with pandoc's.

Both hand-edits were *content-correct* — the `.md` carries the same fixes, which is why regeneration
now reproduces them. The pipeline rule was broken; the paper was not damaged.

### What resolved the original 357/119 divergence

`b5efa1c4` (2026-08-10, S300) — `.tex` only, +359/−121, no `.md` change. Its commit message: *"6 —
cosmology_formal regenerated on MG's go. `.tex` 8→9 modules, James-Stein 0→12 hits; `.pdf` 45pp→47pp,
zero `???`."* The backlog entry for AIW-179 records the same event and the command used
(`build_cosmology_pdf.py paper6 --canonical`). Sampling the diff confirms it is a regeneration: the
abstract flips "Eight"→"Nine" formalization modules and the James–Stein Inadmissibility Conjecture
enters as item (4) with everything after it renumbered — i.e. `.md` content that had never reached
the `.tex` since Session 210 (`019c4999`).

---

## Answers to the three decision questions

**1. Is the committed `.tex` reachable from the `.md`, or is the `.md` now the stale artifact?**

Reachable, and the `.md` is authoritative — for both papers, without qualification. paper3 is
byte-exact. paper6 is exact modulo one paragraph's line breaks. **The `.md` was never the stale side.**
S293's open question ("either it was hand-edited or it predates a pandoc change") resolved to a third
answer that S300 established: the `.md` moved ahead and the `.tex` was simply never regenerated, with
the James–Stein module absent from the `.tex` from Session 210 onward while the `.md` carried it.

**The pipeline breach is real and is located above:** `ea9213f8` and `ddc20a1c`, both 2026-08-12, both
editing a *generated* `.tex` by hand, the first under the explicit misapprehension that it was
hand-maintained. Neither introduced wrong content. The durable fix is not a revert — it is making
`cosmology_formal`'s status unambiguous where a session will read it, because `paper/full/` and
`paper/intelligence/` genuinely *are* hand-maintained and the two regimes sit side by side.

**2. What makes `--canonical` non-destructive?** — see the numbered procedure below.

**3. What is lost if someone runs `--canonical` today?** — see the loss list below.

---

## Reconciliation procedure

Steps 1–6 are the standing pre-flight. Steps 7–8 are paper6; steps 9–11 are paper3, which is the one
that actually changes anything.

1. **Confirm the worktree is clean for the four canonical paths** and that both PDFs are intact LFS
   objects, not phantom modifications:
   `git status --porcelain paper/cosmology paper/cosmology_formal`
   `git lfs ls-files -l | grep sb-hc4a` — the listed sha must equal `sha256sum` of the worktree file.
   (Verified today: `91eb501f…` for paper3, `d1131064…` for paper6, both matching `HEAD`'s LFS pointer
   `oid`, both objects present locally. **The S293 trap is gone** — `git checkout HEAD -- <pdf>` now
   restores real PDFs for *both* papers, not a 131-byte pointer. Back up with `cp` anyway: the checkout
   depends on the LFS object still being fetchable, and `cp` does not.)
2. **`cp` both canonical PDFs and both canonical `.tex` to a dated backup outside the paper dirs**, e.g.
   `tmp/canonical-backup-<date>/`. This is the only step that protects against the script's
   write-then-report-FAILED behaviour, and it costs nothing.
3. **Unicode-header pre-check.** Any `.md` edit that added maths notation must be covered before the
   build, because the script writes the PDF *before* it prints `FAILED`. Today both headers are
   sufficient: `grep -c '^!' ` on both fresh logs returns **0**.
4. **Build into `tmp/` first, always** — `python3 scripts/build_cosmology_pdf.py --keep-aux` (no
   `--canonical`). Confirm `SUCCESS` for both papers *and* independently confirm `grep -c '^!' <log>`
   is 0. The exit status alone is not a safe signal.
5. **Diff the tmp `.tex` against the committed `.tex` with `--no-color`.** This repo sets
   `color.diff = always`; a diff piped into a `^+`/`^-` grep matches nothing and reports a false
   all-clear. Use `git --no-pager diff --no-color --no-index <committed> <tmp>`. Confirm the only
   surviving hunks are whitespace by re-diffing through `tr -s ' \n' ' '`.
6. **Run the drift check against the tmp PDF, not the canonical**, passing paths explicitly because the
   `--paper cosmology` default is still wrong (AIW-180, below):
   `python3 scripts/check_md_pdf_drift.py --md paper/cosmology/sb-hc4a.md --pdf tmp/build-cosmology/paper3/sb-hc4a.pdf`
   Expect 8 segments and 4 REFERENCE ORDER warnings, all documented false positives.
7. **paper6 — decide the one paragraph explicitly.** The only divergence is line-wrapping in the
   Tsang/James–Stein paragraph. Either accept regeneration (recommended: it restores the file to
   generator output and removes the last trace of the hand-edit) or leave `paper6` alone entirely. There
   is no content at stake either way, so this must not be allowed to block paper3.
8. **paper6 — if regenerating:** `python3 scripts/build_cosmology_pdf.py paper6 --canonical`, then
   verify the rebuilt PDF's *extracted text* is unchanged (`fitz`, compare a sha of the concatenated
   page text — today both sides are `882d4c59370a`). Byte-inequality of the PDF is expected and
   meaningless; text-inequality would be a red flag. Note the PDF re-enters LFS as a new object that
   must push to **both** remotes.
9. **paper3 — the real work. Rebuild the PDF, and only the PDF.** The `.tex` is already byte-identical,
   so `--canonical` cannot change it; the operation is purely "catch the PDF up to its own source".
   Before running it, get MG's go, for the reason S300 already established: these artifacts carry a
   Zenodo DOI lineage and AIW-158 records a prior session deciding canonical PDFs were deliberately not
   rebuilt. This is the same class of decision MG was asked for on paper6, and it was worth asking then.
10. **paper3 — run it:** `python3 scripts/build_cosmology_pdf.py paper3 --canonical`. Never the bare
    invocation, which rebuilds **both** papers canonically. Then confirm `sha256sum` of the `.tex` is
    still `acc165a0…` (it must not have moved), and confirm the PDF is 68 pp.
11. **Post-conditions before committing anything:** re-run step 6 against the new canonical PDF; run
    `python3 scripts/verify_references.py --check --paper cosmology` (offline gate); run
    `bash scripts/check-pdf-overflow.sh` on the build log; run `pytest scripts/test_build_cosmology.py -q`
    (11/11 today). Record in the commit message that the PDF moved 66→68 pp and which three commits'
    content it absorbed.

### Three fixes that would make `--canonical` structurally safe rather than procedurally safe

- **The script writes the PDF before it reports `FAILED`.** pdflatex continues past
  `! LaTeX Error: Unicode character …`, so a header gap destroys the canonical and *then* prints an
  error. The fix is to build into a temp dir unconditionally and promote on success — which would make
  `--canonical` a copy operation rather than a redirect, and would retire the whole backup ritual.
- **No gate is wired in.** `build_cosmology_pdf.py` runs neither `check-pdf-overflow.sh` nor
  `check_md_pdf_drift.py`. paper6 currently emits **12 `Overfull \hbox`**, four of them over 10 pt
  (14.36, 12.59, 11.69, 11.53) — `check-pdf-overflow.sh`'s 2 pt threshold would reject that build. This
  is pre-existing (the committed PDF has the same boxes, its text being identical), not something a
  canonical run would introduce, but it means the paper has never passed the project's own overflow gate.
- **A bare invocation still rebuilds both papers canonically.** Requiring an explicit `paper3`/`paper6`
  argument alongside `--canonical` would remove the largest remaining foot-gun.

---

## Loss list — what `--canonical` destroys if run today

**Content lost: none.** This is the finding that most changes the picture, and it is worth stating
plainly: there is **no content on either paper's `.tex` or `.pdf` side that does not also exist in its
`.md`**. Both `.tex` files regenerate (byte-exactly for paper3; whitespace-only for paper6), and the
drift check against the committed paper3 PDF returns **zero `pdf-only` segments**. The guard is
protecting artifacts, not text.

What *is* destroyed, precisely:

1. **`paper/cosmology/sb-hc4a.pdf` — the byte-exact copy of the published Zenodo v4 artifact**
   (version DOI `10.5281/zenodo.21844284`, published 2026-08-08; changelog
   `docs/zenodo-changelog-cosmology-v4.md`). I searched every PDF under `tmp/`, `drafts/` and `docs/`
   newer than 2026-08-01 by sha256: **no copy exists anywhere in the worktree.** It survives only in git
   LFS history, so an uncommitted overwrite is undone by `git checkout HEAD --` and a committed one is
   recoverable from `4d4e65f9`, but the repo would stop holding the published bytes at their canonical
   path. This is the item the guard is really defending.
2. **13 occurrences of the retired "simulation" wording**, plus the rest of the pre-AIW-162/184/188
   phrasing, disappear from the canonical PDF. This is *desired* — the source deliberately purged it —
   but it means the visible before/after is large (66→68 pp) and should not be mistaken for corruption.
3. **`paper/cosmology_formal/sb-hc4a-formalization.pdf` — byte-exact copy of published Zenodo v3**
   (`10.5281/zenodo.21909371`, concept `10.5281/zenodo.21843693`, per `ddc20a1c`). Lower risk: extracted
   text is identical on both sides, and a byte-copy does survive at
   `tmp/build-cosform/sb-hc4a-formalization.pdf` — though `tmp/` is gitignored, so that is not durable.
4. **The last physical trace of the `ea9213f8` hand-edit** in `paper/cosmology_formal/…tex` (one
   paragraph's line breaks). Losing it is the point of regenerating; recording that it happened, and
   where, is why this document exists.
5. **Nothing at all from `paper/cosmology/sb-hc4a.tex`** — regeneration is byte-identical, verified by
   sha256 twice (a build on 2026-08-10 and today's).

**Not on this list, and the guard's stated rationale is wrong about it:** the Session-106
bibtex-`???` failure. Both generated `.tex` files contain **0** `\cite` commands and **0**
`\bibliography`/`thebibliography` environments — the references are plain prose emitted from the `.md`
— and both fresh logs report **0** undefined references after two pdflatex passes. There is no bibtex
pass in this pipeline to omit, so the mechanism that cost Session 106 a day **cannot fire here**. The
backlog's AIW-179 entry already states this; `CLAUDE.md`'s guard text does not.

---

## Tracking conflicts found — reported, not reconciled

Per the data-integrity rule these are surfaced rather than edited. Three canonical files disagree
about the same facts:

- **`CLAUDE.md` (Build Infrastructure table)** says `build_cosmology_pdf.py` is *"guarded S300 but never
  run"*, *"End-to-end build still unvalidated (AIW-156)"*, and *"Do not pass `--canonical` until
  `AIW-179` is settled"*. **`backlog.md`'s AIW-179 entry** says the opposite on all three: *"✅
  REGENERATED S300 ON MG'S GO (2026-08-10, '6. go'). `python3 scripts/build_cosmology_pdf.py paper6
  --canonical`"*, and *"This also fully validated AIW-156's third script end-to-end."* The backlog is
  corroborated by commit `b5efa1c4`; `CLAUDE.md` is stale.
- **`backlog.md` AIW-156** still reads *"(3) `build_cosmology_pdf.py` — NOT RUN"* and *"What remains
  for this item: an end-to-end build validation of (3) into `tmp/`, which is blocked behind AIW-179"*.
  The block is gone and the validation is done: today's run built both papers into
  `tmp/build-cosmology/`, `SUCCESS` both, 0 LaTeX errors, 0 undefined refs, `git status` on both paper
  directories unchanged.
- **`AIW-179` is still `- [ ]` open** while its own body reports the work completed and MG-approved.
- **`AIW-180` is confirmed still open** — `check_md_pdf_drift.py`'s `PAPERS["cosmology"]` still resolves
  to `tmp/build-cosmology/sb-hc4a-S293.pdf`. A fresh, correct target now exists at
  `tmp/build-cosmology/paper3/sb-hc4a.pdf`, and the canonical PDF will be the right default once step 10
  is done.
- **`docs/pending-s294-cosmology.md`** still lists AIW-179 as open item 2 with the 357/119 description.
- **`paper/cosmology/sb-hc4a.formatting-rules.md`** documents the build as bare
  `pandoc … --pdf-engine=pdflatex -o …pdf`, while `docs/pending-cosmology-followups.md` says to use
  `scripts/build-md-pdf.sh` and `CLAUDE.md` says `build_cosmology_pdf.py`. Three documented commands for
  one paper; `build_cosmology_pdf.py` is the one with the guard and the tests.

`docs/pending-cmb-analysis.md` was read and is unrelated to this defect (Planck SOC analysis programme,
AIW-63/AIW-03).

---

## Evidence index

| Claim | Command |
|---|---|
| Both papers build end-to-end | `python3 scripts/build_cosmology_pdf.py --keep-aux` → SUCCESS ×2 |
| paper3 `.tex` byte-identical | `sha256sum paper/cosmology/sb-hc4a.tex tmp/build-cosmology/paper3/sb-hc4a.tex` → `acc165a0…` twice |
| paper6 `.tex` whitespace-only | `git --no-pager diff --no-color --no-index …` → 10/10, one paragraph; `diff <(tr -s ' \n' ' ' …)` → identical |
| paper6 PDF in sync | `fitz` extracted-text sha `882d4c59370a` on both |
| paper3 PDF stale | 66 pp/189,487 chars vs 68 pp/196,817; drift 14 vs 8 segments; `simulation` 22 vs 9 |
| No bibtex exposure | `grep -c '\\cite'` → 0; `grep -ci undefined <log>` → 0 |
| paper6 overflow | 12 `Overfull \hbox`, max 14.36 pt |
| LFS integrity | `git lfs ls-files -l` sha == worktree `sha256sum` == `HEAD` pointer `oid`, both PDFs |
| Guard tests | `pytest scripts/test_build_cosmology.py -q` → 11 passed |
