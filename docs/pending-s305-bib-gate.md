<!-- Action: reference -->
<!-- Tracked-by: AIW-212, AIW-213, AIW-215 -->
<!-- Demoted act -> reference S306 2026-08-23: the .bib arm (AIW-204) shipped, and the four open
     references it named are all factually settled — two landed S306, two are with MG in
     drafts/noc-reference-repairs-for-mg.md. What remains here is reasoning, not a worklist. -->
# S305 — the `.bib` arm of the reference gate, and what it found on its first run

## 1. What was built

The gate parsed each paper's markdown reference list. **The canonical FMT PDF is not built from
that list**: `paper/full/latex/paper.tex` runs `\bibliography{references}` and bibtex resolves
every citation out of `references.bib`. So the artifact that actually ships had never been in
front of the gate, and the two lists drift by construction — S302 established they can drift
into *different works under the same citation key*.

**`verify_references.py` now has a second arm** (`parse_bibtex`, `cited_keys`,
`match_reference`, `check_bib_against_list`, `BIB_SOURCES`), wired into `--check` so it cannot
be run separately and therefore forgotten. Every entry the PDF **cites** must correspond, by
content, to a markdown reference the manifest has already verified, and inherits that verdict.

**Matching is by content, never by key.** The two key spaces are derived independently —
`AlkireHudetzTononi2008` in the `.bib` against `Alkire2008` derived from the `.md` — and a
key-based check reports **45 phantom failures** on a corpus that is largely fine. Author
similarity > 0.85 folded, year equal, title similarity ≥ 0.75, **plus a prefix rule** so a
dropped subtitle still counts as the same work (Myers & Sperry 1958 scores 0.73 on a flat
ratio, below any floor loose enough to be safe).

Re-resolving the `.bib` against Crossref was rejected: it doubles the corpus and the network
cost to verify the same works twice, and produces a second manifest to keep in sync.

`scripts/test_verify_bib_drift.py` — **27 tests**, including a durable guard that fails when a
repo `.bib` feeds a `\bibliography{}` and is not registered.

## 2. What it found — six real defects, in two papers, on the first run

**Class: cited in prose, absent from the reference list.** The PDF prints it; the markdown
source of truth never lists it. An eyeball pass cannot catch this, and none ever did.

| paper | reference | status |
|---|---|---|
| FMT master | Janik, Sayigh & Wells (2006) — dolphin signature whistles, cited at `:340` | ✅ added |
| FMT master | King & Janik (2013) — learned vocal labels, cited at `:340` | ✅ added |
| NoC | Block (2007) — BBS 30(5-6) | ✅ added |
| NoC | Tagliazucchi et al. (2016) — LSD ego dissolution, *cited in prose at `:211` as "(2012, 2016)"* | ✅ added |

⚠ The Tagliazucchi case is the one to remember: the list already carried **Tagliazucchi 2012**
(criticality, *Front. Physiol.*), a genuinely different paper by the same author. Same author,
adjacent year, plausible topic — the shape that reads as covered when it is not.

**Class: wrong content under a correct key.** Repaired in both `.md` and `.bib`:

- **COGITATE 2025** — the NoC entry paired the **preprint title** (*"An adversarial
  collaboration to critically evaluate theories of consciousness"*, which Crossref dates 2023)
  with the **published version's journal and year**. Now the Nature title, with volume, pages
  and DOI, matching the master.
- **Coleman 2014** — subtitle was *"Consciousness, panpsychism, and phenomenal bonding"*;
  Crossref gives the same author/year/journal/volume with *"Panpsychism, Micro-Subjects, and
  Emergence"*. Corrected, DOI added.
- **Milinkovic & Aru 2025** — title truncated to *"Biological computationalism"*; the full
  title is *"On biological and artificial consciousness: A case for biological
  computationalism"*.
- **Kirkeby-Hinrup et al. 2025** — *"The Multiple Generator Hypothesis"* → *"…of consciousness"*.
- **LaBerge 1985** — publisher was Ballantine Books; LCCN 85004691 (already recorded against
  the master's row) gives **J. P. Tarcher** as the 1985 first edition, Ballantine being the
  1986 paperback.

## 3. ⚠⚠ The finding that matters most — the NoC exclusion rested on an unchecked premise

`four-model-theory-noc.md` was on the corpus guard's `KNOWN_UNREGISTERED` list as a *"trimmed
derivative of the master"*. The unstated premise: the master's rows already cover its
references. **The `.bib` arm tested that premise for the first time and it is false.**

Six works its PDF prints are absent from the master entirely — Cybenko 1989, Hornik 1989,
Monti 2010 — and, worse, **three are *different* works from the master's same-author entries**:
Alkire **2000** (master has Alkire 2008), Gazzaniga **1962** (master has 2000), Penrose &
Hameroff **1994** (master has Hameroff & Penrose 1996). Three more disagreed on title.

**This is the paper heading for a journal submission (`AIW-103`, NoC special issue, deadline
Dec 31 2026) — the worst one to have been taking on trust.** It is now registered in both
`PAPERS` and `BIB_SOURCES`, and the stale exclusion comment is replaced with this reasoning.

**The transferable lesson, and it belongs in the exclusion list itself: "derivative" described
the prose, and nobody had checked that it described the bibliography.** Before excluding
anything from a gate, check rather than reason.

## 4. State on exit

- **262 tests pass** (was 235; +27 new). No regressions.
- **All six previously-registered papers are GREEN**: 605 references, 460 verified, 145
  verified-manual. The FMT `.bib` arm passes with **234 printed bibtex citations matched**.
- NoC: 104 references registered, **4 still open** (see below). Manifest is 709 rows.
- `MAX_UNVERIFIED` raised **0 → 4** under the invariant's own documented exception (a
  previously ungated paper joining the corpus, never to absorb a new citation). 30 came back
  needs-review, 26 cleared the same day: **22 by carrying the master's hand verification onto
  entries stating the same thing** (guarded by a 0.90 text-similarity floor — evidence
  transfers only where the two entries make the same claim), 4 by repairing the entry.

## 5. ▸▸ THE FOUR STILL OPEN — two are suspected defects, two need a library

**`noc:Penrose1994` — needs MG, because repairing it edits prose.** The master carries the same
work as **Hameroff & Penrose (1996)**, DOI `10.1016/0378-4754(96)80476-9`, whose suffix encodes
1996. The NoC entry reverses the author order and dates it **1994**, and it is cited in NoC
prose at `:485` as *"(Penrose & Hameroff, 1994)"* — so the fix touches the manuscript, not just
the reference list. Both cannot be right and the master's has a DOI.

**`noc:Gazzaniga1965` — needs the source.** Crossref returns the exact title and author in
*Neurology* at **1973/v23** against the entry's **1965/v15(2), 97-106**. That is evidence the
entry is wrong, not evidence it is right. Do not guess it either way.

**`noc:Wigner1961`, `noc:vonNeumann1932` — pre-DOI originals.** Crossref holds the exact titles
only in the collected-works reissues (1995 / 1996). Existence, title and author are confirmed;
the **original edition's year is not**. Marking these `verified-manual` would mean writing a
note that concedes the one field still unchecked, which is not what the status means.

## 6. Carried forward, unchanged from S303 §5

`AIW-145` violation still live: **`tmp/moc7-poster/` holds durable build assets** (`build.sh`,
figure SVGs) in a throwaway directory, and the poster build overwrites
`drafts/moc7-poster-fig-2x2.svg` from there — it silently reverted a fix mid-session at S303.
Worth moving to tracked `scripts/` plus an assets dir. Not touched this session.

Also unstarted: the **`zenodo-upload.sh` changelog version-string guard** (S303 §2). The script
silently appends whatever sits at `tmp/zenodo-changelog.md`; a version-string match check would
have caught the stale RIM v3 changelog that briefly went live on the FMT roadmap's record.
