# Other theories' prediction maps: sources and licences (AIW-276)

**Verdict: yes, we may republish the four maps with attribution.** The authors' OSF project, which
holds the maps as JSON files with all their arrows, is licensed CC BY 4.0, and so is the preprint.
The maps built into their CodeSandbox app carry no licence and were not used.

Checked 2026-10-19, at source, without contacting anyone and without saving anything to any server.

## 1. Which maps exist, and where the arrows are

| Theory | Authors' file (OSF `JSON MAPS/`) | Claims | Arrows | Same-level arrows* | In the app (claims only) |
|---|---|---|---|---|---|
| Global Neuronal Workspace Theory (GNWT) | `GNW_network_2026-03-12.json` | 44 | 58 | 3 | 44 |
| Integrated Information Theory (IIT) | `IIT_network_2026-03-12.json` | 40 | 53 | 6 | 41 |
| Perceptual Reality Monitoring (PRM) | `PRM_network_2026-03-12.json` | 37 | 53 | 11 | 37 |
| Recurrent Processing Theory (RPT) | `RPT_network_2026-03-12.json` | 30 | 40 | 6 | 30 |
| HOSS, AI, SOMA, HOROR, NREP | none | — | — | — | 35, 40, 35, 30, 29 |

\* Derived: both ends on the same level. The files themselves draw every arrow alike.

- **The arrows exist, and are obtainable, only in the OSF files.** The app (`src/App.tsx` of
  CodeSandbox `xk29y8`, sha256 `f92a516f…6545845`, unchanged since the 2026-10-18 extraction;
  sandbox updated 2026-09-22) ships nine claim lists and starts every built-in map with
  `edges: []`. The earlier note `drafts/papers-moc7/mudrik-platform-schema.md` was right about the
  app and did not know about OSF.
- **Five more theories in the app (HOSS, AI, SOMA, HOROR, NREP) have claims but no arrows
  anywhere I could find**: not on OSF, not in the preprint, not in the app. A comparison with them
  could only compare claim counts, so they are left out.
- **App claims differ from the OSF files.** Same-wording overlap: GNWT 41 of 44, PRM 33 of 37, IIT
  21 of 40, RPT 17 of 30 (IIT also has 41 claims in the app, 40 on OSF). The app was edited after
  the preprint. The OSF files are the version the preprint analyses: our centrality code
  reproduces **64 of 66** values printed in its results to three decimals. The two that do not
  match are GNWT harmonic centrality, B4 (printed 0.260, file 0.2636) and C2 (printed 0.130, file
  0.1318).
- **Claim IDs and levels** come from the authors' label prefixes (`B4: …`; A core, B–F levels
  1–5). The IIT and RPT core boxes have no prefix; they are the only root without one in each map
  and are shown as A1. The grey box in each file is the core.
- **PRM is Perceptual Reality Monitoring** (preprint p. 23, Figure 5). The README inside the
  authors' code zip calls it "Predictive Processing Model"; the preprint is authoritative.

## 2. Sources

| What | URL | Retrieved |
|---|---|---|
| Preprint | https://doi.org/10.31234/osf.io/kqr87_v1 · page https://osf.io/preprints/psyarxiv/kqr87_v1/ · API https://api.osf.io/v2/preprints/kqr87/ | 2026-10-19 |
| OSF project (linked from the preprint's `node` relation) | https://osf.io/9xug8/ · API https://api.osf.io/v2/nodes/9xug8/ · public, created 2026-03-09 | 2026-10-19 |
| Project files | `theories_of_consciousness-main.zip` (app source + README), `GNWT_A2_Final.pdf`, `IIT_A2_Final.pdf`, `PRM_A2_Final.pdf`, `RPT_A2_Final.pdf` (A2 posters of the maps), folder `JSON MAPS/` | listed 2026-10-19 |
| GNWT map | https://osf.io/download/sd234/ (sha256 `92233a60…a0c4c`) | 2026-10-19 |
| IIT map | https://osf.io/download/cga6z/ (sha256 `6e8c1c7e…2b699`) | 2026-10-19 |
| PRM map | https://osf.io/download/udzjh/ (sha256 `b7954265…e2251`) | 2026-10-19 |
| RPT map | https://osf.io/download/69b2b8c22972741ee15d74db/ (sha256 `edcb2efd…71a21`) | 2026-10-19 |
| App | https://xk29y8.csb.app · metadata https://xk29y8.csb.app/api/v1/sandboxes/xk29y8 | 2026-10-19 |

Raw copies: `drafts/papers-moc7/negro2026-maps/raw/`. Wrapped copies with provenance:
`drafts/papers-moc7/negro2026-maps/negro2026-{gnwt,iit,prm,rpt}.json`. The full hashes are in the
`provenance.sha256` field of each and are checked by `scripts/test_negro2026_maps.py`.

## 3. Licences, verified at source

**Preprint.** `GET https://api.osf.io/v2/preprints/kqr87/?embed=license` →
`relationships.license.data.id = "563c1cf88c5e4a3877f9e96a"`, embedded licence
`"name": "CC-By Attribution 4.0 International"`, licence record
`https://api.osf.io/v2/licenses/563c1cf88c5e4a3877f9e96a/` with
`"url": "https://creativecommons.org/licenses/by/4.0/legalcode"`.
`license_record: {"copyright_holders": [], "year": null}`.

**OSF data (project 9xug8).** `GET https://api.osf.io/v2/nodes/9xug8/?embed=license` → the same
licence, `"name": "CC-By Attribution 4.0 International"`,
`node_license: {"copyright_holders": [], "year": null}`. Files in an OSF project carry the
project's licence; none of the four JSON files states a licence of its own, and none states a
different one. Contributors: Niccolo Negro, Eden Elbaz, Shai Fischer, Maor Schreiber, Liad Mudrik
(the preprint spells the first name Niccolò).

**CodeSandbox app.** The sandbox metadata has no licence field (`/api/v1/sandboxes/xk29y8`: no key
containing "licen"; `package.json` has no `license`; no LICENSE file among the nine modules
`index.html, styles.css, .eslintrc.json, tasks.json, index.tsx, package.json, App.tsx,
tsconfig.json, lab_logo.png`). `App.tsx` contains no licence or copyright line. The zip on OSF has
no LICENSE file either, but as a file of the OSF project it falls under CC BY 4.0. The app as
served on CodeSandbox is therefore all rights reserved by default; nothing from it is used.

**What CC BY 4.0 asks** (Section 3(a), quoted from the licence text the OSF API returns):

> If You Share the Licensed Material (including in modified form), You must: retain the following
> if it is supplied by the Licensor with the Licensed Material: identification of the creator(s)
> of the Licensed Material and any others designated to receive attribution, in any reasonable
> manner requested by the Licensor (including by pseudonym if designated); a copyright notice; a
> notice that refers to this Public License; a notice that refers to the disclaimer of
> warranties; a URI or hyperlink to the Licensed Material to the extent reasonably practicable;
> indicate if You modified the Licensed Material and retain an indication of any previous
> modifications; and indicate the Licensed Material is licensed under this Public License, and
> include the text of, or the URI or hyperlink to, this Public License.

No copyright notice and no disclaimer are supplied with the files, so there is none to retain.

## 4. How the site meets it

Per map (section "Maps of the other theories", `<li id="credit-GNWT">` etc.): the five creators,
the file name linked to its OSF page, the project link, the retrieval date, "Licensed under CC BY
4.0" linked to the licence, the list of changes (claim IDs and levels read from the prefixes,
prefix removed from the text, column layout, same-level arrows dashed, centrality recomputed;
content unchanged), and the wrapped file as download. Above every map the slot title says "map by
Negro et al. (2026), CC BY 4.0"; the footer repeats the credit, project link and licence. The page
says the authors did not build or review it and that the use implies no endorsement (licence
§2(a)(6)), and that the maps come as is, without warranties.

### GNWT colours (added 2026-10-19)

In the authors' GNWT file 43 of the 44 claims are uncoloured (`#ffffff`), so GNWT was the only map
without class colours. The preprint's Figure 3 (p. 14) colours every GNWT box, so the classes were
**transcribed from the preprint's Figure 3**, not assigned by us: 20 cognitive, 5 cognitive and
brain-specific (two-tone boxes, the preprint's "hybrid claims", p. 24), 17 brain-specific,
1 extrapolation (D11), plus the core. Class definitions quoted from the methods (p. 7) and the
per-claim table: `drafts/papers-moc7/negro2026-maps/gnwt-classes.md`. Preprint PDF (CC BY 4.0,
primary file of `https://api.osf.io/v2/preprints/kqr87/`, https://osf.io/download/9stmp/, sha256
`d4eb6785…36ddf7`) saved as `drafts/papers-moc7/negro2026-maps/negro2026-preprint.pdf`.

The raw file is untouched (sha256 still `92233a60…a0c4c`). The wrapped `negro2026-gnwt.json` keeps
it unchanged under `"map"`, adds `"added_classes"`, and records the modification in
`provenance.changes` (now a list; the other three maps carry "Colours as in the file.") and
`provenance.class_colours`. The viewer draws the classes in the shades of the authors' IIT and RPT
files, and the GNWT title line reads "colours added by us (see sources)", linked to the GNWT credit
entry.

## 5. Courtesy

The licence needs no permission. A line in the pending close-out reply to Mudrik telling her the
four maps now sit next to FMT's on the page, with credit, would be a courtesy, not a request.
