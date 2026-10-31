# Two NoC references are wrong, and fixing them edits the manuscript

**For MG. Two decisions, both small. Nothing has been changed in the NoC prose.**

`AIW-213`. Four references in the NoC cut were unverified. **All four are now factually settled and
none came back unresolvable.** Two were repaired this session because they touch no prose. These two
change words in the manuscript, so they are yours.

The NoC cut is heading for a journal submission (`AIW-103`, deadline 31 Dec 2026), which is why they
are worth ten minutes now rather than during a submission scramble.

---

## 1. Wigner — the year is wrong, and so is everyone else's

**Cited in prose at `:268` as "(… Wigner, 1961)".**

The first edition's **own copyright page** says otherwise. The Heinemann scan
(`gwern.net/doc/science/1962-good-thescientistspeculates.pdf`, page 1) reads:

> "William Heinemann Ltd … **First published 1962.** © I. J. Good, **1962**"

Corroborated by the Internet Archive catalogue record ("London: Heinemann, 1962"). The essay runs
**pp. 284–302** in that edition.

**The ubiquitous "1961" is citation propagation** — a wrong year that has been copied between
bibliographies for sixty years. Crossref only holds the 1995 collected-works reissue, which is why
the gate could never settle it either way.

**Proposed list entry:**

> Wigner, E.P. (1962). Remarks on the mind-body question. In I.J. Good (Ed.), *The Scientist
> Speculates: An Anthology of Partly-Baked Ideas* (pp. 284-302). Heinemann.

**What changes:** prose `:268` (`1961` → `1962`), the list at `:751`, the `year` field in
`references.bib:1033`, and the manifest row.

⚠ **One thing to weigh:** citing 1962 is correct but will look wrong to any reviewer who knows the
essay as "Wigner 1961". A one-clause note in the entry would pre-empt that; it costs a line.

---

## 2. Penrose & Hameroff 1994 — that publication does not exist

**Cited in prose at `:485` as "(Penrose & Hameroff, 1994)".**

**No joint Penrose–Hameroff publication dated 1994 exists.** Orch OR was *presented* at Tucson I in
April 1994, but every joint paper is 1995–96. The only 1994 item is Penrose's **sole-authored**
*Shadows of the Mind*, which is not what the citing sentence means (it cites a model of quantum
processes in microtubules).

The NoC entry's own journal, volume and pages uniquely identify:

> Hameroff, S. & Penrose, R. (1996). Orchestrated reduction of quantum coherence in brain
> microtubules. *Mathematics and Computers in Simulation*, 40(3-4), 453-480.
> DOI `10.1016/0378-4754(96)80476-9`

**The master already has this right** (prose `:997`, list `:1282`, with the DOI). **NoC's version is
drift introduced during trimming** — the author order got reversed and the year moved.

**What changes:** prose `:485` (`Penrose & Hameroff, 1994` → `Hameroff & Penrose, 1996`), the list
entry at `:697` replaced with the master's string **and moved to the H position** in the alphabetised
list (`check_md_pdf_drift` checks ordering, so it will fail otherwise), the author order and year in
`references.bib:791`, and the manifest row, which re-keys and auto-verifies off the DOI.

---

## Already done this session, for the record — no decision needed

- **`noc:vonNeumann1932` was correct all along.** Deutsche Nationalbibliothek IDN `361261357`
  confirms Berlin, J. Springer, **1932**, 262 S. Crossref indexes only the 1996 reissue, which was
  the entirety of its objection. Marked `verified-manual` with the catalogue cited.
- **`noc:Gazzaniga1965` was a three-way chimera** and is repaired. The list carried the **title of a
  different 1973 paper by different authors** over a page range that does not exist. The real work is
  *Brain* 88(2), 221–236. ⚠ **Both `references.bib` files already had it right, so the printed PDF
  was never wrong** — a correct `.bib` hid a wrong `.md` until the new `.bib` arm compared them.

The gate is now at **2 unverified, down from 4**, and the ratchet in
`scripts/test_verify_references.py` has been lowered to match so it cannot drift back up.
