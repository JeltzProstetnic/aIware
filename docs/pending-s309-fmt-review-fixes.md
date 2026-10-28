<!-- Action: reference -->
<!-- Tracked-by: AIW-236, AIW-229, AIW-193, AIW-156, AIW-210 -->
> ⚠ **DEMOTED TO REFERENCE 2026-08-25 (S310). §1 IS SUPERSEDED — do not act on it.**
> The Fable review it asks for **has now been run once and incompletely** (credits exhausted mid-run).
> The live handover is **`docs/pending-s310-review-resume.md`**.
> **§2–§5 below remain accurate and useful** — in particular §5 on what RIM and cosmology each need first,
> and the four process lessons in §3, which S310 earned a fifth time.

# FMT v15 — everything is folded in. Two things stand between here and the deposit.

**MG's sequence, unchanged:** *"finish all doable work on FMT, then publish FMT then on RIM and then on
main cosmology paper same two steps, each step with a final fable review."*

**Where that stands:** FMT step 1 is **done**. The Fable review **ran, v15 failed it, and the whole
failure is now folded in** — 17 blockers and 167 should-fixes, in both the `.md` and the hand-maintained
`.tex`. RIM and cosmology are untouched on purpose; FMT has right of way.

---

## ⛔ 1. TWO THINGS LEFT, AND THE FIRST IS A DECISION FOR MG

### (a) The four publish-gate acks — MG must rule

MG's rule, verbatim 2026-08-25: ***"defer only things that makes our work more efficient if deferred."***
That rule is already applied, and it is what took the list from **nine to four** — five of the nine
turned out to be finished rather than deferrable. Each survivor has an actual efficiency reason.

```bash
PUBLISH_GATE_ACK=AIW-229,AIW-210,AIW-193,AIW-156
```

| ID | Why deferring is genuinely cheaper — or why it is not a defer at all |
|---|---|
| **AIW-229** | Fixing it means rebuilding the **cosmology** canonical PDF, a step-3 operation with its own traps: that PDF is a **raw blob under an LFS-active `.gitattributes`, so `git checkout` restores a 131-byte pointer rather than the file** — back it up with `cp` — and `build_cosmology_pdf.py` overwrites the canonical *even when it prints FAILED*. Mixing that into an FMT publish buys nothing. |
| **AIW-193 (d)** | The DREAM database analysis — 505 participants, real work, feeding a **book** decision (`AIW-190`), not a paper claim. MG already called it *"a side-quest against the v15/MoC7 deadline"*. Doing it now blocks the deposit for something that changes no sentence in v15. |
| **AIW-156** | The unrun third validation **is** the cosmology build. Same reasoning as `AIW-229`; belongs to step 3. |
| **AIW-210** | ⚠ **Not a defer.** The source is already fixed and v15 *is* the fix. Acking it is closing it. |

⚠ **Re-derive rather than paste.** Run `python3 scripts/publish_gate.py 10.5281/zenodo.18669891` first —
the list shrank three times this session (9 → 7 → 5 → 4) as items were verified closed.

### (b) The full Fable review — MG-directed, and the reason is now stronger than when he asked

MG, 2026-08-25: ***"definitely needs a full fable review later."*** The manuscript has taken **184 edits**
since the last review, so this is not a formality — it is re-reviewing a substantially different
document. Run it the way it was run before, because that worked: **six read-only agents, five section
ranges plus one whole-paper cross-section pass**, each given
`docs/reviews/2026-08-24-fmt-citation-audit.md` and `docs/reviews/2026-08-24-fmt-v15-fable-review.md` so
nothing already repaired gets re-found.

**Hand the new review these two rulings so it cannot re-litigate them:**
- **Criticality is an effect** (MG 2026-08-25). The requirement is open-ended Class 4 computation.
- ⛔ **"We DO address all"** (MG 2026-08-25). The Introduction's addresses-all-eight claim is **ruled and
  rejected as a finding** — do not let a reviewer weaken it again.

---

## 2. What landed, and the state of the artifact

| item | commit | state |
|---|---|---|
| `AIW-194` recall tag → §6.0, as requirement-plus-prediction | `879a7604` | ✅ |
| `AIW-220` closure vocabulary (Groups B+D; A+C deliberately kept) | `aa92e7c4` | ✅ closed on MG's ruling |
| `AIW-232` τ_syn scope clause → §8.9 | `aa92e7c4` + repair | ✅ |
| `didactic-patterns.md` pattern #34 Maquet repair | `2cf614cd` | ✅ |
| The Fable review (6 agents) | `ac325c14` | ⛔ found 17 blockers |
| All 17 blockers folded in | `a2be9fb9`, `17472fa3` | ✅ |
| 167 should-fixes folded in, mirrored to `.tex` | `aef1bfe1` | ✅ |
| `AIW-204`, `AIW-231`, `AIW-211`, `AIW-161`, `AIW-144` closed on verification | — | ✅ |

**Artifact state: 147 pp · 463 tests pass · reference gate 249 refs all verified · 0 undefined
citations · 0 undefined refs · 0 overfull hboxes · 0 LaTeX errors · drift 34 segments against a 33
baseline.** The 142 pp baseline was rebuilt from its own source — the S308 handover's "140 pp" was wrong.

⚠ **`docs/zenodo-changelog-fmt-v15.md` is current and declares `v15`.** The guard fails closed on a
missing declaration but will happily pass a **stale body**, so if anything further changes in the paper,
change the changelog too.

---

## 3. Four process lessons this session earned, in the order they cost the most

1. ⭐ **A defect class is not closed when the instances someone happened to grep are closed.** Three
   earlier repairs had been applied at some of their sites and not all, and the unrepaired sites were
   still in the publish candidate. **Sweep by pattern across the whole file, never by line number.**
2. **An approved clause is approved for its content, not for its fit with the paragraph it lands in.**
   The τ_syn clause was pasted verbatim as instructed, and the verbatim paste is what created an apparent
   self-contradiction with its own paragraph.
3. **Verify against the extracted PDF text, not the `.tex`** — and expect two false-negative classes that
   both fired tonight: typographic apostrophes (`’` vs `'`) and page numbers interleaving mid-phrase.
   Search short fragments.
4. **Trust the machinery over your own edit.** The test suite caught a banned phrase one repair had just
   introduced (`criticality requirement`, `AIW-138`); the build caught two LaTeX defects the mirror
   script introduced; the drift checker caught an md↔tex wording divergence. All three were mine.

---

## 4. Still open on FMT beyond the review

- **`AIW-234`** — the reference gate still substitutes silently: when a printed DOI fails to resolve,
  `crossref_candidates()` falls through to a title query and returns whatever ranks first, **with no
  record that the DOI failed.**
- **⚠ Duplicate backlog entries — reported, not reconciled.** `AIW-231`, `AIW-204` and `AIW-210` each
  appear **twice**, once `[x]` and once `[>]`/`[ ]`. The gate reads the open one, which is why the list
  did not shrink on its own. Two entries disagreeing about whether the same item is done is a tracking
  conflict; picking one is how a real remainder gets erased. **Needs a deliberate pass, not a guess.**

---

## 5. RIM and cosmology — untouched, and what each needs first

**RIM.** Before its own Fable review: the abstract is **348 words** and **no
`journal-guidelines-jintelligence.md` exists in the repo** — fetch and store the target journal's
guidelines before trimming toward a number nobody has verified. Predictions 1–4, 6 and 8 still lack
disconfirmers (MG's call how many are needed). §7.3's **15.90** came from an audit record, not a direct
read of Flynn & Weiss Table 2. ⚠ **RIM's concept DOI is not FMT's** — pass `ZENODO_CONCEPT_DOI`
explicitly or the deposit lands in the wrong record.

**Cosmology.** Read `docs/reviews/2026-08-24-cosmology-drift.md` first; it overturns what `CLAUDE.md`
currently says. ⚠ **A tracking conflict is open here too and must go to MG rather than be silently
reconciled:** `CLAUDE.md` says `build_cosmology_pdf.py` was never run and `--canonical` is blocked;
`backlog.md`'s `AIW-179` says it *was* run canonically at S300 on MG's go; `AIW-156` still reads "NOT
RUN". **Three canonical files disagree.**
