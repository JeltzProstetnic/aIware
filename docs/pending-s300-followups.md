<!-- Action: reference -->
<!-- Tracked-by: AIW-193, AIW-199, AIW-202, AIW-204, AIW-156, AIW-179 -->
# S300 handover — the S299 queue worked out, and all eight decisions answered

> **▸ STATUS: all eight items MG-answered and applied the same session (2026-08-10).** This file is now a
> record rather than a decision queue, hence `Action: reference`. The one live thread it hands forward is the
> **§4.2.3 DREAMING/MATURING re-cut**, unblocked by MG's `AIW-202` ruling — tracked in `AIW-202`, not here.

## 0. One paragraph

S300 took the S299 handover's §2 (queued work), §3 (verification debt) and §5 (the sweep) and worked them to
the end, then MG ruled on the eight items that came out of it and those were applied too. **All four
verification-debt items are cleared**, reports in `docs/s300/`. **Two of them cost the theory a claim**, which
is what verification is for. **§4.2.2 and §4.2.3 gained their unblocked upgrades**, survived a Fable red-team,
and the master builds clean at 138pp.

## 1. The eight decisions and what happened to each

| # | Item | Outcome |
|---|------|---------|
| 1 | `AIW-202` positioning ×4 | **Ruled.** RL: position against the field's unsettledness (16 accounts, 9 incompatible arbitrating variables, 21 years; recency never referees), with **priority inversion** as the unclaimed signature. Naming: *dreaming*-for-the-whole-kind stands on **FMT's own architecture**, not on Domhoff & Fox. **This unblocked the §4.2.3 re-cut.** |
| 2 | The stronger §4.2.2 repair | **Applied.** Felt freedom now runs through the self: the simulation assigns the decision to the self, the regress ends there because what stands behind the self-model is the apparatus, and the choice presents **not as uncaused but as *originating* in the self**. Fixes the objection that no-represented-cause predicts *arbitrary* rather than *free*. Pattern #37's "feels uncaused" is superseded **as a paper formulation**; the spoken form stays book-usable. |
| 3 | Two sweep findings I had deferred | **Applied, and my deferral was the error** — I had deferred to the sweep agent's medium-confidence rating instead of judging them myself. §4.2.4's "requires an explicit world model" was a barrier claim on the axis where the same subsection's body says nothing is barred (now price framing); §3.7.3's bare "Criticality" label violated the registry's standing rule to lead with Class-4 capability. The cross-reference worry was unfounded — §8.9 cites the section, not the label. |
| 4 | The ictal-route fact conflict | **Resolved as UNSETTLED, and neither source was promoted.** Both over-read Meisel et al. 2012, which is a focal-seizure phase-locking study that never says "supercritical" or "hypersynchrony" and does not cover generalized tonic-clonic seizures. Onset is heterogeneous, not hypersynchronous (Truccolo 2011); hypersynchrony dominates late seizure and termination (Jiruska 2013; Kramer 2012); the most direct test finds no pre-seizure supercritical drift (Hagemann 2021). Paper and knowledge file now agree, and both claim less. Three verified references added. |
| 5 | The `.tex` documentation conflict | **Fixed.** `prose-register.md` step 3 said "RIM only — cosmology and FMT build from `.md`", which is false in the dangerous direction: `build_full_pdf.py` only **copies** `paper.tex`, so an FMT edit landing only in the `.md` never reaches the PDF. `CLAUDE.md` was right. |
| 6 | `AIW-179` canonical regeneration | **Done on MG's go.** `.tex` 8→9 modules, James-Stein 0→12 hits; `.pdf` 45pp→47pp, zero `???`. ⚠ **Correction to my own diagnosis:** the committed *PDF* was **not** as stale as the `.tex` — it already said "Nine" and carried all 12 hits. Only the `.tex` was badly stale. `paper3` checked read-only and is in sync. |
| 7 | The `.bbl` count question | **My framing was wrong, and something worse was underneath.** `verify_references.py`'s corpus is `{rim, cosmology}` — it has **never included the FMT master** — so 193 vs 242 was never the same corpus. Two real findings: the committed `paper.bbl` was stale since Session 218 (refreshed), and **the publish-blocking reference gate does not cover the one paper heading for the v15 cut** → filed as **`AIW-204`, P1**. |
| 8 | The REM separability claim | **Softened** in `didactic-patterns.md` where the motor-gating claim is load-bearing. Neither RBD patients (prodromal synucleinopathy) nor Jouvet's lesioned cats are a clean "atonia removed, simulation intact" preparation, and the content evidence splits by sampling method — retrospective studies find large differences, prospective lab studies find none. Also: **do not write "glycinergic"** — glycine alone is insufficient. |

## 2. What shipped in the master

- **§4.2.2 — pattern #37**, "The unrepresentable apparatus", in its MG-approved self-origination form, with the
  physics-vs-consciousness scope guard as its own paragraph.
- **§4.2.3 — the readout/causal-power line** (#13 joined to #35) plus MG's conflation correction.
- **Retired framings removed:** "Principles 4–5"; "no simpler system can replicate"; "requires an explicit
  world model"; bare "Criticality" as the prerequisite label.
- **§6.3 factual error fixed** — atonia gates motor output, not sensory input.
- **§10.3 and §3.7 ictal wording** replaced per item 4.
- **Twelve red-team findings applied**, three severe — including one where the compression of pattern #13 had
  **granted qualia below closure**, against §3.4.2/§3.4.3/§3.5.

## 3. Infrastructure

`AIW-156`: all three recovered scripts now validated. The Tier-4 PDF gate had been **skipping 6 of 11 tests
against a path dead since the `biorxiv/`→`latex/` rename**, reporting green while verifying nothing; fixing
the path exposed two stale baselines. `build_cosmology_pdf.py` is guarded (TDD, 11 failing tests first) so
its default output goes to `tmp/` — a bare invocation would have overwritten both cosmology papers.

## 4. The habit that paid, three times

**Three items turned out to be defects in the tracker rather than the artifact** — v15 member (a) was already
shipped, the Tier-4 gate was silently skipping, and `AIW-179` had a mechanical answer nobody had run. S299
named the defect class as *a correction that reaches the tracker and never the artifact*; **the inverse is
just as common.** Verify a member against the built artifact before working it, not only against the backlog.
