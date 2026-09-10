# BANC connectome — Track 1 (self-referential-closure probe): RESULTS

Session 229, 2026-06-18. AIW-90. Background-agent run on real public data (no fabrication; agent committed nothing). Scripts + data live in `tmp/connectome-analysis/` (`00`–`06` + `data/banc_626_data.sqlite`). Background: `docs/connectome-fmt-feasibility.md`; plan: `docs/pending-connectome-analysis.md`.

## Data — gatekeeper-free confirmed
- CAVE API = token-gated (dead end, as expected). **Public CC-BY snapshot used instead: Harvard Dataverse `doi:10.7910/DVN/8TFGGB`** — plain HTTPS, no login/token. `banc_626_data.sqlite` (683 MB): table `edgelist_simple` = **10,298,797** directed synapse-weighted edges; table `meta` = **155,952** neurons (region / cell_class / cell_type / neurotransmitter).
- Primary graph: directed, synapse-weighted, self-loops removed, **threshold ≥5 synapses** → **118,593 nodes / 1,388,453 edges**. Robustness reruns at ≥1/3/5/10.

## Results
**Global recurrence (≥5 syn):**
- Giant strongly-connected component = **90,239 nodes (76.1%)**
- **89.9% of edges are recurrent**; feedback : feedforward = **8.9 : 1**
- reciprocal A↔B pairs = 81,680; median loop-closure ≈ **3 hops**

**Targeted (FMT substructures):**
- Central complex: **87.9% in the giant SCC**; recurrent-core directed diameter **14** (deep recursion)
- Mushroom body: **64.9% in giant SCC**, core diameter 11; **KC→MBON→DAN→KC loop is structurally closed** (legs 908 / 87 / 9)

**Null model — 20 degree-preserving rewirings (the decisive, honest part):**
- Giant SCC (z = −64) and feedback fraction (z = −91) are **slightly BELOW null** → the giant recurrent core is **GENERIC to degree/density, NOT a designed feature.** Do NOT quote "76% SCC" as engineered self-reference.
- **Reciprocal A↔B feedback enriched ~63× (81,680 vs ~1,297, z ≈ +3,000)** → direct two-way loops are the ONE closure motif the real wiring builds beyond chance.
- CX-in-core at chance (z = +1.4); MB-in-core mildly enriched (z = +10.5).

## Honest verdict
- The structural **precondition** for self-referential closure is present: a closed, ~3-hop-deep, CX/MB-spanning recurrent core + a structurally closed MB learning loop.
- BUT the gross recurrence (giant SCC, feedback dominance) is a **generic density effect**, at/below the degree-matched null — NOT evidence of designed self-reference.
- The **only above-null closure signal is reciprocal feedback** (~63× enriched). That is the real, defensible finding: direct two-way loops — the minimal substrate for a system receiving its own output back — are a designed feature of the wiring.
- This tests a **precondition only**, NOT any FMT functional prediction; it is **NOT evidence of fly consciousness or of FMT confirmation.** Framing must stay at this level.

## What it means / next
- Not a jackpot, but a clean, rigor-correct first pass with one genuine signal (reciprocal-feedback enrichment). The null-model discipline is exactly what keeps it credible — a reviewer would kill a bare "76% recurrent" claim instantly.
- **The higher-upside test is Track 2 (criticality / edge-of-chaos)** — and the data is already downloaded, so it is unblocked. Track 2 is the one that speaks to FMT's Class-4 pillar.
- Future: the *latest* (post-v626) reconstruction needs a CAVE token (request at `flywire.ai/banc_access`; save to `~/.cloudvolume/secrets/cave-secret.json` as `{"token":"..."}`). NOT needed for v626 work.
- Durability: analysis scripts are in `tmp/connectome-analysis/` (`00`–`06`). If this matures toward a paper, move them to `scripts/connectome/` + a repo (per the "no durable scripts in tmp/" lesson, AIW-80). The 683 MB sqlite stays out of git (re-downloadable from the Dataverse DOI).
