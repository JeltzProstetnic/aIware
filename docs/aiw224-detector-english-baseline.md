<!-- Action: reference -->
<!-- Tracked-by: AIW-223, AIW-224 -->
# AIW-224 — the English false-positive baseline, measured

**Measured:** 2026-08-24, WSL, RTX 4090 · **Harness:** `scripts/detector_scan.py` + `scripts/detector/`
**Detector:** Binoculars (Hans et al., ICML 2024, arXiv:2401.12070), observer `tiiuae/falcon-7b`,
performer `tiiuae/falcon-7b-instruct`, bf16, 320-word chunks, 512-token window.
**Raw reports:** `docs/detector-results/2026-08-24-*.md` · **Calibration:**
`docs/detector-results/2026-08-24-control-en-calibration.json`

**What this is.** A *personal false-positive rate*: how often a perplexity-family detector flags
prose that is certainly by this author and certainly predates any usable LLM. It is a property of his
style, not of any paper. **What it is not:** not a probability, not a percentage of anything, and not
a verdict. A Binoculars score is a ratio of two cross-entropies and is not calibrated to a probability.

---

## 1. The English control now exists

The gap that blocked `AIW-223` is closed. Corpus definitions are in `scripts/detector/corpora.json`;
the provenance and date evidence for every file is in `docs/aiw224-control-corpus-inventory.md`.

| corpus | what it is | files | chunks | words extracted |
|---|---|---|---|---|
| `control-en` | narrative + essay register, 2011–2018 | 3 | **319** | 102,594 |
| `control-en-academic` | PhD thesis + earliest FMT statement, 2009–2016 | 2 | **88** | 28,211 |
| `control-de-narrative` | *Ringe des Lebens* I–III, 2016–2018 | 3 | 1,124 | — |
| `control` (unchanged) | 2015 German monograph | 1 | 284 | — |

Every item is datable from document-internal metadata at least two independent ways. **Mtimes were not
used and are worthless here** — the FMS estate was bulk-ingested in 2026, so 2007 documents carry 2026
mtimes.

**The harness's own extractor agrees with the inventory's independent `python-docx` walk** to within
2–5% on the three English books, which closes open item F of the inventory. The one larger divergence
is the PhD thesis (26,528 vs 23,174 words), where the harness keeps short technical lines the
inventory's ≥15-word paragraph filter dropped.

**Roots are absolute paths outside the repository** (`/mnt/wsl/data8tb/__FMS__/…`, `/mnt/c/Dropbox/…`).
Copying ~100k words of MG's published novels and books into a repo with a public filtered mirror would
be a licensing and privacy problem for no measurement gain. The cost is that the manifest is
WSL-specific; on another machine the roots resolve to nothing and the CLI says so rather than quietly
scoring less.

---

## 2. The baseline

`control-en`, n = 319 chunks:

| min | p05 | q1 | **median** | q3 | p95 | max | mean | sd |
|---|---|---|---|---|---|---|---|---|
| 0.8872 | 0.9320 | 0.9636 | **0.9837** | 1.0059 | 1.0321 | 1.0802 | 0.9836 | 0.0313 |

**The three books agree with each other**, which is what makes this usable as a baseline rather than an
average over incompatible things:

| source | n | median | min |
|---|---|---|---|
| The Billion Year Countdown (novel, EN) | 149 | 0.9876 | 0.9110 |
| 8PWC Kuen (instructional, EN) | 96 | 0.9836 | 0.9116 |
| 8PWC Safety and Security (essay, EN) | 74 | 0.9730 | 0.8872 |

**Flag rates at the published thresholds:**

| threshold | source | control chunks flagged |
|---|---|---|
| 0.8536 | Binoculars published **low-FPR** threshold | **0 of 319 — 0.0%** |
| 0.9015 | Binoculars published **accuracy** threshold | **2 of 319 — 0.6%** |

⚠ **Resolution floor: 1/319 ≈ 0.31%.** A rate below that is not resolvable by this corpus, so the
0.0% row means "no chunk fell below", not "the rate is zero". The published low-FPR threshold was
itself chosen at a 0.01% FPR, which **no corpus of this size can confirm** — and the report says so
rather than quoting it.

---

## 3. The NeurIPS workshop paper against it

`drafts/neurips-ai-and-the-self-2026.md`, n = 8 chunks, median **1.0414**.

- **0 of 8 chunks flagged at every threshold tested**, including both published ones and thresholds
  tuned to flag 1% and 5% of his own control.
- The paper's median sits at the **97th percentile of his own English control distribution** — it
  scores *less* machine-like than 97% of his certainly-human English prose.

This reproduces, against a proper same-language same-author control, what the German monograph run
suggested on 2026-08-23 (96th percentile). **The earlier number carried a language-mismatch warning
that this one does not.** ⚠ n = 8 is eight chunks; the paper is short. The claim this supports is "no
chunk of it looks anomalous against his own baseline", not a rate.

---

## 4. ⚠ MG's hypothesis comes out backwards — and then splits

The hypothesis on record was *the more rigorous a text, the less detectable it is*. The measurement
runs the other way, and the research doc had already suspected it would.

| threshold | `control-en` (narrative) | `control-en-academic` |
|---|---|---|
| 0.9015 — published accuracy | 2 of 319 — **0.6%** | 7 of 88 — **8.0%** |
| 0.9113 — set to flag 1% of narrative control | 3 of 319 — 0.9% | 9 of 88 — **10.2%** |
| 0.9307 — set to flag 5% of narrative control | 16 of 319 — 4.7% | 25 of 88 — **28.4%** |

The academic corpus median (0.9507) sits at the **13th percentile** of the narrative control.
**Rigorous prose is more exposed, not less.**

**But the effect is not "academic register". It is the dissertation specifically:**

| source | n | median |
|---|---|---|
| Dissertation, *Discrete Simulation Based Optimization* (2009–16) | 83 | **0.9471** |
| Holomatic Self Model Theory (2014) — the earliest written FMT | 5 | **0.9830** |

**His own theory prose sits at the narrative baseline.** The gap is between the *thesis* and everything
else, not between "academic" and "narrative". That matters directly for the papers: an FMT paper is
theory prose, so the exposure it inherits is closer to the 0.6% row than to the 8.0% row.

⚠ **Do not over-read this.** Holomatic is **5 chunks** and resolves nothing on its own; the whole
academic corpus resolves no finer than ~1.1%, so 8.0% is seven chunks. The direction is clear and
consistent across four thresholds; the magnitude is not. And the thesis differs from the books in
register, subject matter, genre convention *and* decade at once — this measurement cannot say which of
those is doing the work.

---

## 5. One defect found and fixed in the harness

`--calibration <out>/<slug>.json --save-calibration` **silently destroyed the calibration it had just
written.** `main()` writes the calibration first and the report second, and
`--corpus control-en --out tmp/detector --calibration tmp/detector/control-en.json` — the obvious thing
to type — aims both at one path. The run printed success. The next run would have read a file with no
`scores` key and scored the artifact against nothing.

Fixed at argument level in `scripts/detector_scan.py`: the collision is now a usage error (exit 2)
raised **before** a 7B pair is loaded for a result that cannot be kept. Two tests pin it — the
collision is refused, and the ordinary same-directory layout still works.

---

## 6. What is still open

1. **Gmail is deferred**, as the inventory recommended: ~20,000–50,000 words of pre-2022 English,
   the smallest source at the highest handling cost and the only real privacy exposure. Route is
   Google Takeout → mbox → header-date filter → hard de-quoting → privacy scrub, and it must land
   outside git.
2. **`.odt` is not a supported suffix**, so the SiRO tutorial (2009, ~2,500 words English) and the
   *Future Spinoffs* stories (2007–08, ~26,800 words German) are excluded. Adding a reader is a small
   job; it was not worth doing for 10% more academic English.
3. **Hand the harness to the fleet.** MG's stated end state is that this runs fleet-wide, and it has
   not started. The manifest's absolute roots are the thing to reconsider first.
4. **What the thesis effect actually is** — register, subject, genre or decade — is a real question the
   corpus cannot currently answer. The cheapest discriminator available is more of his own pre-2022
   *theory* prose, which is exactly what Gmail and the 2015 German material would supply.
