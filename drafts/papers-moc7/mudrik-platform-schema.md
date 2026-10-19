# Prediction-map platform: map-file schema and FMT mapping (AIW-276)

**Verdict:** the platform's map file is plain React Flow JSON with five top-level keys, read straight from the app's source; our FMT map converts to it, loads in the app with all 55 nodes and 84 edges rendered, and survives a Download round trip unchanged.

Established 2026-10-18 in a headless browser (no window, no sign-in, nothing saved to any server).

## 1. Sources

| Source | What it gave | Reliability |
|---|---|---|
| App source, `src/App.tsx` of CodeSandbox `xk29y8` (title "TOC", author Eden Elbaz, created 2025-05-28, last updated 2026-09-22, 2 forks) | `exportNetwork()` and `importNetwork()`: the exact writer and reader of the file | Primary. The sandbox JSON arrived as a network response of the running app (`xk29y8.csb.app/api/v1/sandboxes/xk29y8`), which the earlier curl attempt could not get past Cloudflare. |
| Live export: `mudrik-platform-demo-export.json` | A real Download of the built-in IIT map (41 nodes) | Primary. ⚠ **Its one edge (`IIT-1 → IIT-2`) is a probe edge I drew to capture the edge format. It is not part of the authors' IIT map** — the built-in maps ship with nodes only and `edges: []`. |
| Preprint: Negro, N., Elbaz, E., Fischer, S., Schreiber, M., & Mudrik, L. (2026). *Prediction maps as a gateway to better understand and test scientific theories*. PsyArXiv, posted 2026-03-11. https://doi.org/10.31234/osf.io/kqr87_v1 | Ontology (levels, classes, "in virtue of" relation, solid vs dashed), label convention | Citation verified against Crossref 2026-10-18 (title, five authors, date). |
| GitHub | Nothing: no repository for the platform found (`api.github.com` search, 0 hits) | — |

Runtime facts: React 18.2 + `reactflow` 11.11.4, Create-React-App/TypeScript template. State lives only in the browser's `localStorage` (`theoryNetworks`, `selectedTheory`); the app has no server-side save.

## 2. The schema

Top level (written by Download, required by Load Map):

```json
{ "theory": "IIT", "nodes": [ ... ], "edges": [ ... ],
  "exportDate": "2026-10-18T21:00:56.507Z", "version": "1.0" }
```

`importNetwork()` rejects the file with *"Invalid map file format"* unless `theory`, `nodes` and `edges` are all present and non-empty. `exportDate` and `version` are written but never read.

**Node** (a React Flow node):

| Field | Value |
|---|---|
| `id` | string; built-ins are `<THEORY>-<n>`, user-added `<THEORY>-custom-<timestamp>` |
| `type` | always `"custom"` (the app's only node type: 220 px box, 8 handles) |
| `data.label` | claim text. Built-in convention: the text ends with its reference number(s) in parentheses, `(2)` or `(6;8)` |
| `data.colors` | 1–4 hex colours; more than one renders as a 45° gradient. **This is the only class/category encoding the app has.** Built-in maps are all `#ffffff` |
| `data.color` | legacy single colour, written on export |
| `data.theory` | overwritten with the top-level `theory` on import |
| `data.metrics`, `data.selectedMetric` | cleared on import and export |
| `position` | `{x, y}` in px; the app snaps to a 50 × 35 grid on drag |
| `width`, `height` | measured by React Flow, present on export, optional on import |

Any extra `data.*` keys survive import and Download (the app spreads `...node.data`).

**Edge** (a React Flow edge, as created by `onConnect`):

| Field | Value |
|---|---|
| `id` | `reactflow__edge-<source><sourceHandle>-<target><targetHandle>` |
| `source`, `target` | node ids; arrow points source → target |
| `sourceHandle`, `targetHandle` | one of `top-left`, `top-center`, `top-right`, `bottom-left`, `bottom-center`, `bottom-right`, `left`, `right` |
| `type` | `"smoothstep"` |
| `style` | `{stroke: "#2a2a2a", strokeWidth: 3.5, opacity: 0.9}` |
| `markerEnd` | `{type: "arrowclosed", width: 15, height: 15, color: "#2a2a2a"}` |
| `animated` | `false` |

Edges are imported verbatim (no processing at all).

**Relation vocabulary: there is none.** Every edge is the same untyped arrow. The app has no edge labels, no relation types and no solid/dashed distinction; nor does it have fields for level, claim class, claim kind or references other than the label text.

**Theory slot.** The dropdown offers `RPT, GNW, IIT, PRM, HOSS, HOROR, NREP, AI, SOMA, other`. A file with any other `theory` value still loads and renders, but the dropdown cannot show it or switch back to it, and on page reload the app's `localStorage` check drops it. `other` behaves the same way across a reload (it resets to one blank box) but is at least selectable within the session. So the converter writes `"theory": "other"` by default (`--theory FMT` is available).

**Analyze** computes PageRank, LRC, LRC_NX and Betweenness on the directed source → target graph. The preprint's Harmonic Centrality is not in the app.

## 3. Mapping from `fmt-prediction-map.json`

| Ours | Platform | Loss |
|---|---|---|
| `theory` block | top-level `theory` = `"other"` | Theory name, proponent and layout notes are dropped. The slot is not persistent across reloads (see above). |
| node `id` (`A1`…`F9`) | `id` = `other-A1`; also `data.fmt_id` | none |
| node `text` + `refs` | `data.label` = `"A1: <text> (1;2)"` | none; follows the built-in "(refs)" convention, with our paper label prepended because the app shows no ids |
| node `class` | `data.colors` = one tint per class: cognitive `#9ee7f5` (cyan), substrate-general `#a8e6a1` (green), brain-specific `#f7b6d2` (pink), extrapolation `#fff3a0` (yellow); raw value kept in `data.class` | ⚠ The hues follow the preprint; the exact hex values of its figures are not published, so these are approximations. |
| node `level` | column position (core, L1…L5 left to right, 350 px apart); raw value in `data.level` | ⚠ **Lossy in display.** The preprint draws levels as concentric rings; the app has no level concept and no auto-layout, so levels appear only as columns. A ring layout would need hand placement in the app. |
| node `kind`, `status`, `uniqueness`, `fmt_section` | `data.kind` etc. | Invisible in the app; kept in the file and through Download. |
| edge `from` → `to` | `source` → `target`, handles chosen by relative position | none; direction matches the preprint ("C4 can lead to C3 … arrow from the former to the latter") and the app's centrality code |
| edge `type: in_virtue_of` | (implicit; every arrow) + `data.relation` | none: the platform's only relation is the paper's single "in virtue of" relation |
| edge `style: dashed` | `style.strokeDasharray: "8 6"`; raw value in `data.fmt_style` | ⚠ **Not a platform feature.** React Flow passes `style` to the SVG path, so our 12 same-level edges *do* render dashed, but a dashed arrow drawn by hand in the app is impossible, and another tool reading the file would ignore it. |
| edge `justification` | `data.justification` | Invisible in the app; kept in the file. |
| `references` (10 entries) | — | ⚠ **Dropped.** The app has no reference list; only the numbers survive in labels. Table 1 of the preprint is where they belong. |
| `cross_theory_links` (14) | — | ⚠ **Dropped.** `onConnect` refuses edges between theories; one map holds one theory. |
| `legend`, `status`, `schema` | — | dropped (documentation) |

## 4. Verification (2026-10-18)

- `pytest scripts/test_convert_prediction_map.py` — 18 passed (written first, failed on the missing module, then implemented).
- Load Map with `fmt-prediction-map.platform.json` in headless Chromium: no alert, theory selector shows `other`, **55 nodes and 84 edges rendered, 12 of them dashed**.
- Download straight after: 55 nodes, 84 edges, edges byte-identical to the input, every node `data` key retained, labels unchanged.

Regenerate after any change to the map: `python3 scripts/convert_prediction_map.py`; the test `test_output_file_is_current` fails while the output is stale.
