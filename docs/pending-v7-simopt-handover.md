Action: reference
Tracked-by: AIW-51, AIW-01, AIW-68

# Session 207 Handover — FMT v7 + SimOpt Subproject

**Created:** 2026-05-29 (Session 207)

## What Happened

### FMT Paper → v7 (three edits, .md + .tex synced)
1. **§3.6 Permeability:** Explicitly declared as a family of mechanisms (serotonergic, GABAergic, dopaminergic, etc.), not a single parameter. Predictions concern the structural role, not specific neurochemistry.
2. **§3.7.3 Criticality:** "Computational threshold" → "Computational prerequisite." Added explanation: self-referential simulation is a universal computation, universal computation requires Class 4 dynamics, therefore criticality. The specific regime is substrate-dependent.
3. **§3.4 Stage 3:** Added observability constraint: "the ESM's observational horizon is bounded by the EWM. The explicit self-model cannot see with useful resolution beyond the explicit world model to the implicit substrate that generates it."

### BBS Seth Commentary
- v3 reviewed against v6 terminology, four fixes applied (temporal echo added, permeability as boundary property family, Hard Problem "transforms" not hedges, trimmed to 1000 words)
- Submission kit at `tmp/bbs-submission/` (.docx ready)
- Portal has no "Commentary Proposal (Seth)" article type — email sent to bbsjournal@cambridge.org asking about submission channel
- **Waiting for BBS editorial reply** — deadline Jun 12

### Scott McFarnell
- Replied May 29 — wants gridworld simulation testbed before human subjects
- Proposes survival gridworld comparing FMT vs ACU architectures
- Corrected ACU = "Affective Control under Uncertainty" (not Attention-Consciousness Uncoupling — fix Google Doc)
- Asks about Matthias's coding skills
- **Reply drafted in Gmail** — buys time, flags level mismatch (FMT explains phenomenal consciousness, ACU is phenomenally neutral), mentions 35+ years sim/opt + Claude Code
- ACU researched: one paper (PhilArchive, 7 weeks old, no peer review). Functional architecture for affective agency, NOT a consciousness theory. Phenomenally neutral by design.

### Backlog Changes
- AIW-64/65/66 marked done (already in v6)
- AIW-67 marked done (publisher already correct)
- AIW-57 marked done (ABOUT.md updated — books published, German edition added, v6 label)
- AIW-48 (McFarnell) downgraded P1 → P3

## Next Session Tasks

### Priority A: SimOpt Subproject Setup
- Create subproject under simopt for FMT architectural validation gridworld
- Key experiment: can an FMT agent learn from observing another agent die (third-person perspective projection via ESM), while simpler architectures can't?
- The distinction: FMT agent extracts finer-grained causal structure from observation by replaying sequences through its own self-model step by step, vs flat association learning ("cave = danger") from simpler architectures
- Ablation test: remove ESM → agent should revert to flat association learning
- Reservoir computing substrate for criticality (tunable spectral radius)
- Permeability as gating mechanism on implicit→explicit information flow
- Frame as architectural validation, NOT consciousness detection

### Priority B: FMT Formalization (parallel track)
- Check existing formalization roadmap (`paper/fmt_formal/`) for v7 consistency
- Three formalization targets identified:
  - Permeability family: define boundary, information measure, modulation function
  - Criticality: prove self-referential simulation requires Turing-completeness → Class 4
  - Observability constraint: formalize O_ESM ⊆ S_EWM
- User insight: formalization should translate architectural intuition into notation, not discover new things

### Priority C: Zenodo v7 Upload Planning
- Paper is now v7 with three substantive improvements
- Current Zenodo has v5 (concept DOI: 10.5281/zenodo.18669891)
- BBS commentary references the concept DOI — reviewers would see v5 if they check now
- Upload v7 before BBS submission deadline (Jun 12) if possible

### Priority D: Infrastructure
- `tmp/test_content_integrity.py` deleted — test infrastructure stale. CLAUDE.md build table references nonexistent file. Calibration ranges (word counts, ref counts, canaries) outdated for ~30k word paper.
- Fix Google Doc ACU name error (Affective Control under Uncertainty, not Attention-Consciousness Uncoupling)

## Key Insights from This Session

- FMT's "formalization gap" is narrower than critics claim — the architecture IS the specification, the gap is qualitative→quantitative
- Self-referential closure = observability constraint (ESM bounded by EWM) — simpler and more powerful than fixed-point semantics
- Criticality is a prerequisite derived from universal computation requirements, not a threshold to measure
- Permeability is a family, not a scalar — the structural role unifies diverse neurochemical mechanisms
- A gridworld can test architectural claims (minimum model count, permeability regimes, cognitive learning from observation) but CANNOT test consciousness claims — frame accordingly
- Scott's ACU is not a peer theory to FMT — it's a decision-making framework, not a consciousness theory. Gridworld comparison is asymmetric.
