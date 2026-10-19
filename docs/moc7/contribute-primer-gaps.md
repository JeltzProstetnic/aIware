# Contributor primer — open placeholders and decisions (2026-10-16)

Page: `wiki/contribute/index.md` (draft, not linked from the wiki index or the Zenodo record yet).
Sources: crucible `README.md`, `docs/milestones.md`, `docs/evidence-map.md`, `docs/implementation-plan.md`,
`docs/moc7-demo-description-2026-09-28.md`, `docs/pending-platon-scale-kit.md`, `backlog.md`, the named
`docs/design/*-prereg.md` and `docs/results/*` files; aIware `project-reference.md`, `wiki/`.

## 1. Placeholders in the page — who fills each

| Placeholder | Owner | Note |
|---|---|---|
| `{{TBD-crucible: registration link (GitHub issue template + form)}}` | crucible | Needs the public repo first. |
| `{{TBD-crucible: public repo URL}}` | crucible | Used 2×. crucible is `LicenseRef-Proprietary`, has no LICENSE file, and is private today. |
| `{{TBD-crucible: registration form URL}}` | crucible | Non-GitHub fallback. |
| `{{TBD-crucible: install instructions}}` | crucible | `pyproject.toml` workspace; the repro README says `source packages/crucible/.venv/bin/activate`, which is not an outsider recipe. |
| `{{TBD-crucible: exact command …}}` for CRU-70 | crucible | `repro/cru70_return_latency.py` exists (19 s on CPU). It needs a seed-block CLI argument. Per the repro README rule, repro scripts must not be refactored, so add a wrapper instead. |
| `{{TBD-crucible: public path to docs/design/*-prereg.md}}` | crucible | The pre-registrations have to be public for "registered" to mean anything to an outsider. |
| `{{TBD-crucible: VRAM per network size for this kit}}` (KIT-S0) | crucible | Measured costs exist only for the *feedback-line* kit (22k neurons ≈ 12.2 GB host / 16.2 GB GPU). The page does not attribute those numbers to the scale kit. |
| `{{TBD-crucible: falsifier — …not yet formally pre-registered}}` (KIT-S1) | crucible | The size axis has a stated question but no pre-registration and no falsifier. |
| `{{TBD-crucible: stated hypothesis}}` (R1) | crucible | The kit doc states the stakes (σ ≈ 1 on a reactive controller hurts criticality as a discriminator) but gives no directional hypothesis. |
| `{{TBD-crucible: falsifier, …event definition (CRU-192)}}` (R1) | crucible | CRU-192 is `[>]`. Owed: an event definition, an estimator that holds up under subsampling, a positive control, and a red-team. |
| `{{TBD-crucible: data-return spec}}` | crucible | The page proposes JSONL with provenance and health fields, modelled on the kit's own rows (`weight_growth`, `rate`, `free_rate` per arm). |
| `{{TBD-crucible: upload channel}}` | crucible | Options: a PR to a results repo, a Zenodo community, or Nextcloud accounts as used for the current collaborator. |
| `{{TBD-crucible: code licence}}` | crucible / MG | — |
| `{{TBD-MG: data licence}}` | MG | CC BY 4.0 would match the wiki. |
| `{{TBD-MG: co-authorship rule …}}` | MG | The threshold for authorship versus acknowledgement. The page states credit in the result document as the floor. |

## 2. Decisions MG must make before the page goes live

1. **Disclosure conflicts with open-sourcing.** crucible deliberately sent the outside collaborator an *obfuscated* kit: docstrings stripped, `esm` renamed to `pop_d`, and a leak gate (CRU-138, CRU-185). A public repo plus this page undoes that strategy. Decide whether open-sourcing supersedes it, or whether the kits stay obfuscated and only replication scripts go public.
2. **The page discloses unpublished crucible results**: CRU-70 numbers, CRU-78 falsified-then-PARTIAL, the kit seed-sweep null, and the CRU-83 Gate A figure (92.4%, *p* = 0.0001). Approve or strike each before publication.
3. **The outside collaborator is not named**, and KIT-S0 is described only as "being run by one outside collaborator". `pending-platon-scale-kit.md` §5(g) (telling him what the collaboration is) is still open. Answer it before the page mentions his runs publicly.
4. **Seed-block allocation** is presented as the planned mechanism. Confirm it, or replace it.
5. **Voice**: `wiki/STYLE-GUIDE.md` requires third person. This page uses second person for instructions ("you register") because it is a how-to. Accept the exception or rewrite.
6. **Navigation**: the page has no `article_number`, and `wiki/index.md` and the mkdocs nav do not yet link a "Contribute" section. That needs an infrastructure hand-off, and a line in the Zenodo description.
7. **Admonition**: the "Start here in 3 steps" box is the only `!!!` admonition in the wiki. It is enabled in the spec's `markdown_extensions` and is not collapsible, so it complies, but it is a first.

## 3. Inconsistency found in crucible (not fixed, read-only)

- `crucible/docs/implementation-plan.md` line 37 still says *"Near-criticality (necessary, not sufficient)"*. This contradicts MG's S329 ruling (criticality is a signature, never a requirement), which `evidence-map.md` already carries. The page follows S329. → crucible inbox.

## 4. Which experiments suit outside contributors, and why

| ID | Verdict | Why |
|---|---|---|
| **CRU-70** (return latency) | **Best first task** | It has a pre-registration with a numeric falsifier, pure numpy, a 19 s CPU run and a single script. Useful contributions: independent replication on fresh seeds, and a *pre-registered* version of the size-matched null, which was added post hoc and decides the 60/40 attribution. |
| **CRU-78** (self-block localization + vacuity control) | **Good** | It is pre-registered, the falsifier fired, and the vacuity control (CPU, 128 configs) produced PARTIAL. Replicating the control is cheap and settles a contested reading. The full grid needs a GPU. |
| **KIT-S0** (learning-rate health grid) | **Good once the code is public; needs a big GPU** | It is calibration with a clear health rule and already packaged as a run-only kit. Contributors with ≥ 30,720-neuron capacity extend a curve the project cannot measure itself. |
| **KIT-S1** (size axis, body prediction) | **After pre-registration** | It is null so far on typical seeds and its trivial alternative is named. It needs a falsifier written before outsiders run it. |
| **R1** (reactive-controller criticality baseline) | **After CRU-192** | It suits robotics students and discloses no code. It is blocked until the event definition exists, because the naive σ reads ≈ 1 on any smooth trace. |
| CRU-83 (M1s3 sufficiency) | Not suitable | This is the core open target, gated on unpopulated §5.1 predictions, which is a design dependency. |
| CRU-176 (self-recognition) | Not suitable | The apparatus question is unresolved. Needs more seeds plus a design decision. |
| CRU-210 (forward-prediction boundary) | Not suitable | The design is not written yet. |
| CRU-76 (selective suppression) | No | Killed pre-build by red-team. Listed on the page for transparency only. |
| Robot / MoC7 demo work | No | It needs the in-house WAVEGO hardware and cockpit. |
