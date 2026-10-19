<!-- Action: reference -->
<!-- Tracked-by: AIW-257 -->
# Zenodo deposit abstracts — how they are produced, and the defect that made this necessary

**Nothing is pending here.** The S318 blockage cleared and the work is done; this file is the
reference for how a deposit's abstract is produced from now on.

## The defect

A deposit description is built as `<abstract> + <changelog>`, and until S319 only the changelog was
ever rewritten. `scripts/zenodo_metadata.py::apply_version_metadata` split the inherited description
at the first `<h3>Changelog` and re-emitted the head **verbatim**, so the abstract was never
refreshable by the tool that ships revisions. Nothing in a deposit run ever looked at it.

This is the same blind spot the file's docstring already recorded for `title` — the companion's v2
shipping the new title in the PDF and the old one on the record. A field the updater does not name
keeps its old value, and keeping its old value reads exactly like success.

## What was found, S319 2026-09-11

Six multi-version deposits were checked against their source papers. **The two minted by
`zenodo_first_deposit.py` matched at 100%. Four of the four older ones had drifted** — which is the
inheritance hypothesis confirming itself.

| record | drift found |
|---|---|
| `22114974` FMT master v15 | a **v8-era** abstract: *"criticality requirement"*, *"five principles"* (the theory has three, `AIW-138`), qualia as *"digital constructs"*. Its own v15 changelog explained the criticality correction directly beneath an abstract still asserting it. |
| `22132325` cosmology v6 | *"four independently motivated frameworks"* followed by a list of **three**; *"Six weak points"* against the paper's **seven**; *"simulation at criticality"*; predates a whole round of hedging repairs (`structurally identical` → `structurally corresponds to`, Bekenstein → holographic saturation, the Kerr–Newman material and the DESI caveat both absent). |
| `21909371` FMT formalization v3 | criticality as a *"prerequisite"*, where the paper says *"hypothesis … neither a derived consequence of self-referential closure **nor a stated requirement on consciousness**"*. |
| `22128175` RIM v5 | a hand-written summary advertising *"three interdependent dimensions: Cognitive Capacity, Motivational Drive, Recursive Self-Improvement"* — the three-**capacity** framing the current paper exists to **refute** (Motivation is typed as an allocation policy; pattern #39, the observatory). |

All four were corrected in place on 2026-09-11. Editing metadata on a published record does **not**
mint a new version and does **not** change the DOI.

## How to refresh an abstract now

The abstract is **derived from the paper**, never hand-maintained — that is what removes the thing
that drifts.

```bash
python3 scripts/zenodo_abstract.py paper/full/four-model-theory-full.md -o tmp/abstract.html
ZENODO_ABSTRACT=tmp/abstract.html bash scripts/zenodo-upload.sh <pdf>
```

`ZENODO_ABSTRACT` is a **path to an HTML file**, not the text — 2 KB of markup does not survive a
shell variable. Empty or unset means "keep the inherited abstract", and in that case the upload
script now prints `Abstract inherited (N chars) — NOT refreshed from the paper`, with the first
line of what is shipping. The override makes a stale abstract *fixable*; that line is what makes it
*noticeable*.

To edit a published record's abstract without shipping a new version, `POST /actions/edit` → `PUT`
the metadata whole → `POST /actions/publish`. Take `metadata` whole; never PUT a partial payload.
Split the description at the **first** `<h3>` and keep the changelog tail byte-for-byte.

## Guards

- `scripts/test_zenodo_abstract.py` — the generator, plus a per-paper test that every deposited
  paper still yields a usable abstract, plus a check that the FMT abstract has not reacquired any of
  the three `AIW-257` defect strings.
- `scripts/test_zenodo_metadata.py` — the `abstract` override, empty-means-absent, changelog
  non-stacking, and that `zenodo-upload.sh` both reads `ZENODO_ABSTRACT` and reports what it ships.

⚠ A string blacklist is not a drift check. The one that found three of these four was **comparing
each record against its paper**; a blacklist only finds drift already known about. Note also that
*"systems that operate at criticality"* is the paper's own **correct** wording (criticality as the
signature in physical substrate) and is not a defect — a naive grep for `at criticality` flags it.
