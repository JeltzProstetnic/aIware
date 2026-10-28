# FMT prediction map: hosted viewer (for infrastructure)

**URL:** `https://research.matthiasgruber.com/fmt-map/` (live; the old `matthiasgruber.com/fmt-map/` redirects 301)

Upload the seven files below into that directory, unchanged. The page is static: no server code,
no build step, no cookies, no analytics.

| File | What it is |
|---|---|
| `index.html` | The viewer. Single self-contained page: CSS, data and code are inline. The one external load is the graph library, `cytoscape.min.js` 3.33.1 from `cdnjs.cloudflare.com`, pinned with an SRI hash. |
| `fmt-prediction-map.json` | Download: the map in our own format (64 claims, 101 arrows, all fields; E12, E13, E14, E15 and F11 are proposed predictions, marked as such, not yet in the FMT master). |
| `fmt-prediction-map.platform.json` | Download: the same map in the React Flow format that the Negro et al. app (https://xk29y8.csb.app) opens via its **Load Map** button. |
| `negro2026-gnwt.json`, `negro2026-iit.json`, `negro2026-prm.json`, `negro2026-rpt.json` | Downloads: the maps of Negro, Elbaz, Fischer, Schreiber & Mudrik (2026) for GNWT (44 claims, 58 arrows), IIT (40, 53), PRM (37, 53) and RPT (30, 40). Each holds the authors' OSF file unchanged under `map` and its provenance (source URL, retrieval date, SHA-256, licence) under `provenance`. |

The page links the JSON files by relative path, so they must sit next to `index.html`.

## The other theories' maps

- **Source:** the authors' OSF project https://osf.io/9xug8/, folder `JSON MAPS`, four files dated
  2026-03-12, retrieved 2026-10-19. Raw copies, byte for byte:
  `drafts/papers-moc7/negro2026-maps/raw/`. Sources, licences and the counts are documented in
  `comparison-sources.md` in this directory (a working note, not for upload).
- **Licence:** CC BY 4.0 (OSF project licence, read from the OSF API). The page carries the
  attribution the licence asks for, once per map ("Maps of the other theories") and in the footer:
  creators, link to the file and project, licence link, and a list of the changes made.
- **Not used:** the maps built into the authors' app at https://xk29y8.csb.app. That code has no
  licence, and its claim lists are nodes only; everything here comes from the OSF files.
- **What the page does with them:** a **Map** selector switches between FMT and the four maps, and
  **Compare with** shows a second map beside the first (side by side from 1100 px wide, stacked
  below that). The state is kept in the URL hash, e.g. `#theory=IIT&compare=FMT`. A table
  compares claims, arrows, levels, median and 90th percentile of each centrality, and the top 3
  claims by PageRank.

## Headers

- Serve `.json` as `application/json`. The links carry the `download` attribute, so browsers save them.
- If a Content-Security-Policy is set on that path, it must allow `script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com` and `style-src 'self' 'unsafe-inline'`.

## Wiki link to add

The wiki page `wiki/predictions/prediction-map.md` (article 106, section Predictions) already
links the viewer at `https://research.matthiasgruber.com/fmt-map/`. If the viewer goes to a different URL,
change that link (it appears twice on the page). The viewer links back to the wiki at
`https://fmt.matthiasgruber.com/predictions/prediction-map/`; that assumes MkDocs' default
directory URLs. Adjust `WIKI_PAGE` in `scripts/build_prediction_map_site.py` if the wiki uses
another scheme, and rebuild.

Optional: a link from the matthiasgruber.com research/publications page to `/fmt-map/`.

## Regenerating

These files are generated. Do not edit them here; edit the map or the script, then run

```
python3 scripts/convert_prediction_map.py       # if the map changed
python3 scripts/negro2026_maps.py --wrap        # if a raw file under negro2026-maps/raw/ changed
python3 scripts/build_prediction_map_site.py
pytest scripts/test_prediction_map_site.py scripts/test_negro2026_maps.py -q
```

The test fails while this directory is stale. `comparison-sources.md` is not generated and not part
of the upload.
