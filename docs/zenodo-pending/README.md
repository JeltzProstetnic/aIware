<!-- Action: act -->
<!-- Tracked-by: AIW-257 -->
# Pending Zenodo description fix — blocked on a Zenodo outage, 2026-09-09

**The correction is prepared and verified; only the push is outstanding.** Zenodo went down
mid-session — `https://zenodo.org/` returned **504 on the unauthenticated front page**, so it is
their outage and not our token or endpoint. The records API had answered normally twenty minutes
earlier in the same session. **Retry, do not re-diagnose.**

## What is wrong on the live record

Record **22114974** (FMT main, concept `10.5281/zenodo.18669891`). Its description is built as
`<abstract> + <changelog v15> + <changelog v14> + …`. The abstract half is a **v8-era text** and
carries three defects, all of which the paper itself fixed long ago:

| defect | live record says | the paper says |
|---|---|---|
| criticality's status | *"Combined with a **criticality requirement** (the substrate must operate at the edge of chaos)"* | the requirement is open-ended Class-4 computation; near-criticality is **the signature it leaves in neural tissue** |
| principle count | *"the theory derives diverse phenomena from **five principles**"* | **three** principles (`AIW-138`, MG-settled 2026-08-03) |
| the virtual domain | qualia are *"**digital constructs**"* | *"patterns that exist at the level of the running computation"* — MG: in a neural net the virtual domain is *"all BUT digital"* |

⚠ **The record's own v15 changelog explains the criticality correction at length**, immediately below
an abstract that still asserts the error. That is the tell, and it points straight at the cause.

## The cause, which is a tooling defect and outlives this fix

`scripts/zenodo_metadata.py::apply_version_metadata` **inherits** the previous description and only
**appends** a changelog block (`out["description"] = f"{desc}\n\n<h3>Changelog {version}</h3>…"`).
Nothing ever refreshes the abstract. So every version since v8 has stacked a fresh changelog onto a
frozen abstract, and no deposit run could have caught it. **This is the same class of defect the
file's own docstring already records** — the companion's v2 shipping the new title in the PDF and the
old one on the record, because `title` was not among the overwritten fields. The abstract is the next
field in that same blind spot. **Fixing the record without fixing the builder means the next version
re-inherits the corrected abstract by luck rather than by design.**

## How to push it

`docs/zenodo-pending/fmt-abstract-v15.html` holds the replacement — 3 paragraphs, 2,236 chars,
generated from `paper/full/four-model-theory-full.md`'s current abstract and checked clean for all
three defect strings.

1. `GET  /api/deposit/depositions/22114974` — take `metadata` whole; never PUT a partial payload.
2. Split `metadata["description"]` at the **first** `<h3>` (that is `_CHANGELOG_MARKER` in
   `zenodo_metadata.py`); the head was 2,901 chars and the changelog tail 24,586.
3. Replace the head with the file's contents. **Keep the entire changelog tail byte-for-byte** — it is
   the version history and it is correct.
4. `POST /actions/edit` → `PUT` the metadata → `POST /actions/publish`.
5. Read the record back and confirm none of `digital`, `five principles`, `criticality requirement`
   appears in the abstract half.

⚠ **Editing metadata on a published record does not mint a new version and does not change the DOI.**

## Also still open under `AIW-257`/`AIW-258`

- **The wiki long tail is `AIW-27` Part 2**, not new work — its re-runnable workflow script has sat
  unrun since a burst rate limit killed it on 2026-07-28. Path in `docs/pending-wiki-refresh.md`.
  The stale RIM title *"Why Intelligence Models Must Include Motivation"* is still in ~10 wiki files.
- **Done this session:** `wiki/llms-full.txt` rebuilt on the current master (983 stale lines replaced
  by 1,620), its site summary re-stated to the ruled position, the link offering the **withdrawn
  PsyArXiv tombstone** as the intelligence paper removed, and `digital constructs` cleared from the
  NoC `.md` + `.tex`, the `cc` variant, `virtual-qualia.md` and the glossary.
