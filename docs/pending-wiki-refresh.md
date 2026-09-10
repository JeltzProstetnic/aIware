<!--
Action: reference
Tracked-by: AIW-27
-->
# FMT Wiki Refresh — Part 2 handoff (long-tail sweep)

**Created S275, 2026-07-28 (WSL).** Part 1 (10 load-bearing files) is DONE + committed (`0b8c4240`).
This file tracks the remaining lean sweep, which was authored as a workflow but **failed twice on a
server-side burst rate limit** ("Server is temporarily limiting requests · not your usage limit") — 20
agents launched near-simultaneously and all got throttled within ~25–40s. **Zero files were edited; `wiki/`
is clean.** Retry when the transient limit clears — and throttle the launch into 2–3 waves so the burst
doesn't self-trip the limit.

## What's already DONE (Part 1 — committed 0b8c4240, NOT to be redone)
Canonical language pinned across these 10 files — **reuse it verbatim** for the rest:
- **SMoC framing** = "leading *candidate* for a standard model of consciousness; field is pre-paradigm;
  invitation, not verdict." (`index.md`, `foundations/overview.md`)
- **Criticality** = the requirement is **free compute** (Class-4 universal-computation capability *actually
  deployed* for open-ended self-modeling); criticality (σ≈1 / λ≈0 / edge of chaos) is the **dynamical
  signature we measure**, NOT the requirement. Trichotomy: capability + free instantiation + evolutionary
  forcing (paper §3.7.3, §8.9).
- Files: `index.md`, `foundations/overview.md`, `physical-foundations/{criticality, two-thresholds,
  wolfram-classes, cortical-automaton, five-system-hierarchy}.md`, `ai-consciousness/{llms-not-conscious,
  engineering-specification}.md` (registry #6), `reference/glossary.md` (added a **Free Compute** entry).

## Part 2 remaining scope (the workflow)
Lean scope, MG-approved (S275). Workflow script (re-runnable):
`/home/jeltz/.cc-mirror/mclaude/config/projects/-home-jeltz-aIware-wiki/562a26ca-e10d-4907-a0b3-d9c5673472d4/workflows/scripts/fmt-wiki-longtail-sweep-wf_757c240c-b08.js`
Retry: `Workflow({scriptPath: "<above>"})`. It is section-batched (19 fix→verify batches + 1 currency
draft), edits `wiki/*.md` in place, and returns a summary (verify_issues, unresolved_links, residual_flags,
currency_draft). **The 10 done files are excluded from the batches.**

1. **Criticality long-tail** (~30 files w/ passing "requires criticality" mentions): phenomena (anesthesia,
   sleep, lucid-dreaming, split-brain, anosognosia), predictions/confirmed + prediction-4, comparative
   (vs-hot, vs-rpt), formal (holography-criticality, information-theoretic), open-questions/multi-level,
   reference/{key-figures, reading-order}, basics/*. Reframe to free-compute-signature. Keep passing
   descriptive uses ("brain drops out of criticality under anesthesia") — only fix "criticality IS the
   requirement" framings.
2. **Registry #2/#4/#5 compliance** (all 127, surgical): #2 don't let implicit→explicit read as data-transfer
   for how the sim is *generated* (permeability "transfer/surfacing" is fine); #4 binding is *dissolved*
   not solved; #5 localization asymmetry (implicit=structural/localizable, explicit=distributed/non-localizable).
   Registry: `.claude/knowledge/fmt-misconception-registry.md`.
3. **Internal-link audit + fix.** Known-broken (found S275, fix these for sure):
   - `four-models.md` — referenced in `core-architecture/four-model-theory.md` See-Also + `cortical-automaton.md`;
     no such file (the four models live in implicit-/explicit-world/self-model.md). Either create an article-8
     "The Four Models" hub or repoint links.
   - `reference/glossary.md` links to `core-architecture/{iwm,ism,ewm,esm}.md` → real files are
     `implicit-world-model.md`, `implicit-self-model.md`, `explicit-world-model.md`, `explicit-self-model.md`.
   - `foundations/overview.md` See-Also → `intelligence/recursive-intelligence-model.md` → real file is
     `intelligence/overview.md`.
   - `cortical-automaton.md` → `phenomena/psychedelic-phenomenology.md` → real file is `phenomena/psychedelics.md`.
   - `wolfram-classes.md` See-Also → `predictions/criticality-evidence.md` → no such file (fold into
     `predictions/confirmed.md` or drop).
4. **Currency = DRAFTS ONLY (MG reviews before shipping).** Save the workflow's `currency_draft` to
   `drafts/wiki-currency-additions.md`. Topics: published Seth commentary (Zenodo 10.5281/zenodo.20626675),
   RIM PsyArXiv (osf.io/kctvg), 8-language book, type-B physicalism/Mary, three-senses-of-virtual,
   basal-ganglia permeability gating, in-silico component tests (companion "Gruber 2026d" = crucible),
   metacognition double-dissociation.

## On completion
Fix residual broken links the agents couldn't resolve → review verify_issues → save currency draft to
`drafts/` → commit Part 2 → `bash ~/cfg-agent-fleet/setup/scripts/filtered-push.sh` → inbox task to
**infrastructure** to rebuild + redeploy `mkdocs build` (site source is `wiki/`; mkdocs.yml lives in the
infrastructure project, NOT this repo).
