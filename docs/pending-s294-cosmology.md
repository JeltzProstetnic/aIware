<!-- Action: reference -->
<!-- Tracked-by: AIW-174, AIW-173, AIW-179 -->
<!-- S296 2026-08-08: AIW-177 CLOSED (all five CRU-81 drafts placed in the master). AIW-174 step 1 DONE
     (entanglement-wedge formalization → drafts/aiw174-entanglement-wedge-postulate.md). -->
# Cosmology — context after the S293 repair and the S295 publish

**SB-HC4A is repaired, reviewed, rebuilt and PUBLISHED.** Canonical
`paper/cosmology/sb-hc4a.{md,tex,pdf}` is current at 66pp, MG-approved.

## The cosmology update is CLOSED (S295, 2026-08-08)

Both steps this file used to carry are done — do not re-run them.

- **Step 1, the 17 references: cleared.** Fourteen were matcher noise; three were real defects
  (`Boyle2018` missing author Finn, `Elze2020` a 2022-title-on-a-2020-slot chimera, `Gruber1968`
  unfindable and MG-replaced with `10.1007/978-1-4899-5424-4_1`). `MAX_UNVERIFIED` is now **0** across
  both papers and may never be raised. Detail: `AIW-172` in `backlog.md`, S295 in the conversation log.
- **Step 2, publish: done.** Zenodo **v4**, version DOI `10.5281/zenodo.21844284`, concept
  `10.5281/zenodo.18698605`, published 2026-08-08. Changelog: `docs/zenodo-changelog-cosmology-v4.md`.

**Not blocking, and still open:** `AIW-174` step 1 is a research programme, not a paper-update task.
§6.5 as published states a conditional result with its condition named.

## Gate state as published (S295)

| Gate | State |
|---|---|
| Citation gate, cosmology | **CLEAN — 145/145**, zero defective, zero needs-review |
| Margins | CLEAN, 66pp, both axes |
| md ↔ PDF drift | 6 segments, all recorded extraction artifacts (see `publication-build.md`) |
| Reference ordering | 4 warnings, all confirmed checker false positives |
| Tests | 158 passed, 6 skipped |

⚠ `check_md_pdf_drift.py --paper cosmology` still points at `tmp/build-cosmology/sb-hc4a-S293.pdf`,
which is stale and will report ~22 phantom segments. Pass `--md`/`--pdf` explicitly against the
canonical PDF until that default is fixed.

## What S293 did, so it is not redone

- **All five S291 criticals repaired**, plus a **sixth reference defect** the whole-paper pass found
  on its own (Easson & Brandenberger is **2001**, JHEP 2001(06) 024 — not 1999/JHEP 9906).
- **Terminology: "Bekenstein saturation" → "holographic saturation" throughout, MG-confirmed.** The
  Bekenstein bound (energy × radius) and the area law ('t Hooft/Susskind, covariant form Bousso 1999)
  are now separated in §5.2 Step 1, and coincide only at the collapse threshold. Do not merge them again.
- **`AIW-174` landed in §6.5** as a *conditional* derivation — see below.
- **§3.1 Axiom 1 is now ARGUED, not asserted** (MG-supplied, S293). It had been a bare claim that
  nothingness is "a Platonic abstraction", which made Axiom 1 look like a contested thesis carried for
  decoration. It now runs on an exhaustive dilemma: any assertion that nothingness is possible must
  either locate it or not. **Located** → fixing it relative to what exists implies a separation, hence a
  dimension, hence a position, hence a property (the Cambridge-property objection is met head-on; vacuum
  decay and the empty possible world are instances). **Unlocated** → the claim becomes "nothing,
  everywhere and everywhen", refuted by the existence of whoever asserts it. No third form exists.
  Plus an independent epistemic line (nothingness is unobservable in principle, since observing it
  requires a spacetime relation to it) and the deflationary last exit. Krauss/Albert corrected — they
  reach OPPOSITE conclusions, and Albert's objection is granted as an instance of the first horn.
  **Do not re-open this as "arguable" — MG settled it and supplied the argument.**
- **Reference budget 50 → 17**, each cleared row naming its evidence in `docs/reference-manifest.json`.

## `AIW-174` — what is actually claimed now

§6.5 no longer says "candidate direction". It states a **conditional derivation**: information
causality's inequality and the holographic bound on the shared locus are *the same inequality* once
*m* is read as locus capacity, so Tsirelson follows via Pawłowski/Uffink — **given the single-locus
decoding postulate**, which is §5.2's ontology applied to entanglement and is named in the text rather
than hidden. The Oughton & Timpson measure-dependence objection is answered from the α = 1
relative-entropy form of the Bekenstein bound.

**Do not upgrade this to an unconditional claim.** The remaining gap is exactly one thing: formalizing
the decoding postulate in entanglement-wedge language (Dong, Harlow & Wall, 2016). Full reasoning,
including the communication-complexity route that **fails at the same joint** and should not be
re-attempted as independent support: `drafts/aiw174-tsirelson-from-capacity.md`.

## MG decisions taken 2026-08-07 (S293) — do not re-ask

1. **Publishing waits for a clean citation gate.** MG chose to hold the Zenodo version until the
   remaining references are verified. **The 17 open references are now the publication blocker.**
2. **`Gruber2015` is 2015.** Settled: the 2016 Lulu printing changed cover art and typos only. Both the
   cosmology and RIM entries now say so, and both manifest rows are `verified-manual`. Closed.
3. **`Gruber2026b` is PUBLISHED on Zenodo** (S293, MG-approved): version DOI
   `10.5281/zenodo.21843694`, **concept DOI `10.5281/zenodo.21843693`** — the concept DOI is what the
   cosmology reference list cites, matching the house convention used for Gruber (2026a). 31pp,
   CC-BY-4.0, linked `isSupplementTo` the FMT concept DOI.
4. **Next session leads with `AIW-174` step 1.**

## Open, in priority order

**⚠ Superseded in part by S296 (2026-08-08) — read this block before the list below.**
- **`AIW-174` step 1 is DONE.** The postulate is stated in entanglement-wedge terms:
  `drafts/aiw174-entanglement-wedge-postulate.md`. Headline: EWR does **not** supply the postulate (at
  pair scale the connectedness condition *is* the conjecture), but the translation caught a
  **refutation-shaped defect** — read distributively the postulate is a local hidden-variable model
  yielding CHSH ≤ 2, so **jointness is load-bearing** and must travel with every restatement
  (`AIW-184`). Also: the pair's ebit sits in the S_bulk term, not the area term; and intra-quantum EWR
  **cannot** non-circularly deliver Tsirelson, so the EW form is the *consistency* home and the
  device-independent skeleton is the *derivation* home.
- **`AIW-177` is CLOSED** — all five CRU-81 drafts placed in the master's `.md` and `.tex`, verified in
  a built PDF. Both warnings were honoured.
- **New this session:** `AIW-184` (P2, the jointness/minimality clauses), `AIW-185` (done — the
  pre-publish open-item gate), `AIW-186` (P2, the vacuity regime, MG-flagged for a deeper discussion),
  and `AIW-166` upgraded P3→P2 with `drafts/aiw166-cosmos-transfer.md`.
- **Versioning, MG-agreed S296:** do **not** cut a cosmology v5 per finding. Accumulate `AIW-174`,
  `AIW-184` and the S290 content items (`AIW-162`/`164`/`166`/`167`) into ONE coherent rewrite.

1. **`AIW-186` (P2)** — the vacuity regime, and MG asked for a deeper discussion of it specifically.
   Its character changed the same evening: the pool-collapse may be the *prediction* (homogeneity),
   not the bug. Aim at the smooth low-entropy **initial** condition, not entropy increase.
2. **`AIW-179` (P2)** — `cosmology_formal`'s `.tex` regenerates with a 357/119 diff from an unchanged
   `.md`; its committed PDF is suspect. Its `∝` unicode gap is already fixed, so the paper builds again.
3. **`AIW-173` (P2)** — the saturation-trigger automaton experiment. Compute is this WSL box (RTX 4090).
4. **`AIW-174` remaining** — steps 2 and 3 (the Jain–Gachechiladze–Miklin polynomial machinery, which
   the S296 note confirms operates at the right device-independent level; and the monogamy step, which
   now has a precise diagnosis — HHM monogamy fails at the *same* area-to-single-locus joint as the
   Tsirelson gap and the recorded communication-complexity dead end. Three failures at one joint.)

## Traps that cost time in S293 — all now in `.claude/knowledge/publication-build.md`

- `build_cosmology_pdf.py` **overwrites the canonical PDF even when it reports FAILED**, and for
  `paper/cosmology/sb-hc4a.pdf` `git checkout HEAD --` used to restore a 131-byte LFS pointer. Back up
  with `cp`. (That path is now a proper LFS object, so checkout is safe again — but verify, don't assume.)
- Any edit adding maths notation needs a `unicode-header.tex` check **before** the build. It halted
  twice in one session (`ⁿ ⁰ ⁴ ₐ`, then `⊗ ‖`).
- `verify_references.py` used to carry a `defective` verdict onto a *repaired* entry forever. Fixed;
  when a defect is genuinely repaired, delete its manifest row and drop the key from
  `TestManifestRatchet.KNOWN_OPEN_DEFECTS`.
