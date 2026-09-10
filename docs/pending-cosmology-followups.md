<!-- Action: reference -->
<!-- Tracked-by: AIW-81 (RIM half), AIW-84 (D&N experiment), AIW-85 (§6.5 QEC) -->
# Cosmology follow-ups — handoff after SB-HC4A v3 publish (Session 220, 2026-06-11)

**SB-HC4A v3 is PUBLISHED.** Version DOI `10.5281/zenodo.20643614`; concept DOI `10.5281/zenodo.18698605` (auto-resolves to latest). Two correction rounds + author-driven reframe + D&N expansion are in `paper/cosmology/sb-hc4a.md` (50 pp, canonical PDF updated). Full Fable analyses (basis for the items below): `docs/fable5-fmt-analysis/fable-*.md`.

> **STATUS S291 (2026-08-07): items 1 and 3 are DONE.** Item 1 (`AIW-81` RIM half) was fully applied this
> session — see `docs/pending-rim-s290-remaining.md`. Item 3 (`AIW-85` §6.5) was applied to
> `paper/cosmology/sb-hc4a.md`: the 17-particle anchor excised with its withdrawal stated, and the
> holographic-QEC pointer added with three verified references. **Only item 2 (`AIW-84`, the Day & Night
> numerical experiment, P3) remains open in this file.** Note for whoever runs it: `sb-hc4a.tex` is a stale
> pandoc artifact — the `.md` is the single source and the build is `scripts/build-md-pdf.sh`.
>
> **S291 late: item 2 (`AIW-84`) is superseded by `AIW-173`**, which restates the same experiment with the
> boundary export-channel design the Fable sweep recommended. Work `AIW-173`, not `AIW-84`. And note the
> paper itself is now BLOCKED from publishing by `AIW-172` — see `docs/pending-s292-worklist.md`.

## 1. RIM half of AIW-81 — P1, the priority (NOW UNBLOCKED) — ✅ DONE S291
The user (2026-06-11) deferred RIM to "the sessions AFTER SB-HC4A new version is published" — that condition is now met.
- Distil `docs/fable5-fmt-analysis/rim-analysis.md` (reposition vs van der Maas mutualism + Dickens–Flynn; lead with Brunswik-symmetry P7 + consistency-over-intensity P8; cut the consciousness-dependency + grading polemic).
- Apply to `paper/intelligence/` (.md + build), rebuild (gated wrapper), review, republish to **OSF `kctvg`**.
- Same workflow as this cosmology pass: Fable drafting agents (disjoint spans → own tmp files) → integrate → `build-md-pdf.sh` → yellow-highlight review → publish.

## 2. AIW-84 — Day & Night numerical experiment (P3)
Per `docs/fable5-fmt-analysis/fable-day-night-saturation.md`. Run B3678/S34678 vs GoL (vs **Critters**, the reversible block-CA) in Golly/lifelib: 1024² torus, ≥20 i.i.d. ρ=0.5 seeds, 10⁵ steps; observables = block entropy S_k, order parameter φ=⟨|m_i|⟩, coarsening length L(t)~t^(1/z), activity, structure census, preimage/Garden-of-Eden census. SUPPORT (S1–S4) / REFUTE (R1–R3) criteria in the file. Outcome → 4-panel figure → upgrade §5.4/§9.7 to a citable partial demonstration of the **saddle-instability half** of Weak Point 7 (NOT the holographic half), or a standalone companion note ("Order from saturation in a self-complementary cellular automaton"). Pilot (Fable, this session) already shows the headline effect but is unverified — needs a production rerun.

## 3. AIW-85 — §6.5 formal home → holographic QEC (P3) — ✅ DONE S291
Per `docs/fable5-fmt-analysis/fable-discrete-stein-formalization.md`. Verdict: James–Stein is the wrong tool for the one-locus entanglement claim — keep §6.5 demoted (already is). Optional improvement: a 1-sentence pointer that the natural formal home is **holographic quantum error correction** (HaPPY / entanglement-wedge reconstruction), where "joint decoding beats product decoding" is already a theorem; and **excise the "17 Standard-Model particle types → d≥3" anchor** (no support in any candidate formalization). Standalone open math (not needed for the paper): discrete-Stein admissibility ⇔ simple-random-walk recurrence on median graphs / CAT(0) cube complexes; decisive entry problem = Conjecture A (admissibility of the rounded MLE on Zᵈ, d≥3).

## Reference: publishing a cosmology version
`zenodo-upload.sh` is now generalized (backward-compatible). Cosmology:
`ZENODO_CONCEPT_DOI=10.5281/zenodo.18698605 ZENODO_VERSION=vN ZENODO_CHANGELOG=<changelog.md> bash scripts/zenodo-upload.sh <pdf>`
Build: `bash scripts/build-md-pdf.sh paper/cosmology/sb-hc4a.md tmp/build-cosmology/out.pdf -H paper/cosmology/unicode-header.tex` (gated; overflow-checked). NEVER recompile `paper/cosmology/sb-hc4a.pdf` in place — build into `tmp/`, then copy on approval. Pre-integration backup of the v2-era source: `tmp/cosmology-drafts/_sb-hc4a.md.bak-preintegration` (throwaway; the published v3 is canonical).

## Also flagged (not cosmology, from session start)
- `conversation-log.md` lags ~6 sessions (last real entry ~S213, HEAD at S219/220) — wants a backfill.
- AIW-78 (LFS phantom-mods on canonical PDFs) — `sb-hc4a.pdf` reconciled to LFS this session by the v3 commit; `sb-hc4a-formalization.pdf` still a phantom.
