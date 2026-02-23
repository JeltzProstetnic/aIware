# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-23T18:00Z (Session 106)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: TDA implementation → preprint comparison

## Preprint vs Local Comparison — RESULTS

| Paper | Preprint | Local | Identical? | Changes since upload |
|-------|----------|-------|-----------|---------------------|
| **FMT** | Zenodo 60pp/18,536w | Local 60pp/18,938w | **NO** (+402 words) | Ellia & Tsuchiya (2025) citation, "principled minimum" §3.2, Gödel fix, DOI links (54 ins, 46 del) |
| **Intel** | PsyArXiv 25pp/8,677w | Local 25pp/8,677w | **YES** (binary identical) | None |
| **Cosmo** | Zenodo 26pp/11,401w | Local 32pp/11,667w | **NO** (+6 pages, +266 words) | Class 4 self-containment fix, Wetterich integration (4 ins, 2 del) |

### Preprint files in tmp/
- `tmp/fmt-PREPRINT-zenodo.pdf` — FMT as published on Zenodo
- `tmp/intel-PREPRINT-psyarxiv.pdf` — Intel as published on PsyArXiv (DOI: 10.31234/osf.io/kctvg_v1)
- `tmp/cosmo-PREPRINT-zenodo.pdf` — Cosmology as published on Zenodo

### User consideration
Intel preprint DOI is version-specific (`_v1`). Uploading a new version changes the DOI. Currently local = preprint, so no update needed unless other changes are desired.

### Rules added this session
- **Canonical PDF protection rule** in publication-workflow.md §5 and MEMORY.md — never overwrite canonical PDFs for comparison
- **Machine vs human review** in publication-workflow.md §5 and TDA §7 — comparisons always as rendered PDFs

## Recovery Instructions
1. Read this file
2. All 6 PDFs already opened for user comparison
3. Canonical PDFs restored from git — verified intact (0 `??` refs)
4. Tests: `pytest tmp/test_build_scripts.py tmp/test_content_integrity.py -v -m "not slow"` → 144 pass
