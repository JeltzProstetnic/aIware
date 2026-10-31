> **⚠ STALE CONTENT PACK (S343, 2026-10-20).** The live /moc7/ page has moved on: MG removed the 'Changed since the poster' box, the booklet left Read, and Contribute and map cards were added. infrastructure owns the page. **Never send this file for deployment.** Send infrastructure a diff of the intended change instead (INF-129).

# MoC7 landing update + No Outside subsite — content pack for infrastructure (AIW-297)

Prepared by aIware, 2026-10-18 (S338). Nothing here has been published. **Do not deploy until MG has cleared
the open items at the bottom.**

## Files

| File in this pack | Target URL | Replaces |
|---|---|---|
| `moc7-index.html` | `https://research.matthiasgruber.com/moc7/` (`moc7/index.html`) | the current live page, in full |
| `no-outside/index.html` | `https://research.matthiasgruber.com/no-outside/` (new directory) | nothing (new page; 404 today) |

Both pages use only the existing shared stylesheet (`../style.css?v=20261009b`) and classes already on the site
(`hero`, `event-slot`, `publications`, `compact`, `pub`, `featured`, `pdf-pair`, `pdf-card`, `kit-card`, `kit-sample`,
`with-icon`, `legal-note`, `book-info`, `back`, `links`, `card`). The teaser cards on `/no-outside/` put a `<p>`
inside `.pub`; it renders with body text size. An optional rule such as `.pub p { font-size: 0.95rem; }` would
match `.book-info p`, but nothing requires it.

## Changes to /moc7/ against the live page (fetched 2026-10-18)

1. **Paper card v18 → v19.** Direct download now
   `https://zenodo.org/records/23427746/files/zenodo-fmt-v19.pdf?download=1` (verified 200; file 1,190,573 bytes),
   version DOI 10.5281/zenodo.23427746 shown in the card meta. The featured card keeps the concept DOI
   10.5281/zenodo.18669891 (always newest). JSON-LD gains `"version": "19"`.
2. **"Changed since the poster"** box under the PDF pair, built from `docs/zenodo-changelog-fmt-v19.md`.
3. **Hero slot** in past tense: "presented Thu 15 Oct 2026" (the conference is over; time and corridor removed).
4. **New sections**, in order after "Read": SJÄLV handout; Contribute; In preparation since MoC7; New book teaser.
   "Related papers", the card deck, the link cards and the footer are unchanged.
5. Meta description and og:description mention the booklet.

## Assets to copy into `moc7/`

| Published path | Source (aIware repo, tracked) | Note |
|---|---|---|
| `moc7/sjalv-booklet-A5.pdf` | `drafts/sjalv-print/ccw-sjalv-reading-order-A5.pdf` (4,371,051 bytes) | 12 single A5-landscape pages in reading order, no crop marks, the `ccw` rotation that was printed. Its PDF metadata says author "anonymous"; set it to Matthias Gruber if convenient. Do **not** use the `*-printshop-*` or `*-A4-duplex*` files. |
| `moc7/sjalv-cover.jpg` | render page 1 of the PDF above (about 600 px wide), or crop `drafts/sjalv-print/preview_cover.png` | new thumbnail for the SJÄLV card |
| `moc7/paper-preview.jpg` | optional: re-render page 1 of the v19 PDF | the current thumbnail shows v18's first page |

The booklet's QR code was decoded at build time to `https://doi.org/10.5281/zenodo.18669891` (concept DOI), which
now resolves to v19, so the printed booklets stay correct without a reprint.

`/no-outside/` needs no assets.

## Links to verify after deploy

Checked 2026-10-18 with `curl -L`:

| URL | Status |
|---|---|
| https://doi.org/10.5281/zenodo.18669891 | 200 |
| https://doi.org/10.5281/zenodo.23427746 | 200 |
| https://zenodo.org/records/23427746/files/zenodo-fmt-v19.pdf?download=1 | 200 |
| https://doi.org/10.5281/zenodo.18698605 (SB-HC4A, linked from /no-outside/) | 200 |
| https://doi.org/10.5281/zenodo.21610993 | 200 |
| https://amcs-community.org/events/moc7-2026/ | 200 |
| https://amcs-community.org/wp-content/uploads/2026/10/moc7-booklet-web-full.pdf | 200 |
| https://orcid.org/0009-0005-9697-1665 | 200 |
| https://github.com/JeltzProstetnic/aIware | 200 |
| https://research.matthiasgruber.com/experiments/ | 200 (S341; the student programme moved here from /moc7/contribute/, which 301s) |
| https://research.matthiasgruber.com/no-outside/ | 200 (checked 2026-10-19, S341) |

After deploy, check: `/moc7/sjalv-booklet-A5.pdf`, `/moc7/sjalv-cover.jpg`, `/no-outside/`, and the `../no-outside/`
link from `/moc7/`.

**Contribute link:** in `moc7-index.html` the primer URL is plain text inside a comment-marked `pub-meta`
(`TODO-INFRA`). Turn it into `<a href="https://fmt.matthiasgruber.com/contribute/">` only when the wiki page answers
200. The wiki URL scheme was confirmed on a live page (`/core-architecture/four-model-theory/` → 200), so
`wiki/contribute/index.md` will land at `/contribute/`.

## Outside this pack, for infra to note

- The **homepage** (`/index.html`) also links the v18 PDF (`zenodo.org/records/23217056/files/paper.pdf`). Same
  v18 → v19 swap applies there if MG wants it.

## Sources used

- No Outside teasers: `drafts/monograph-limits/no-outside-draft-v0.6.md` at commit `2d131433`. All six passages
  were checked by script to be verbatim substrings of that file (76–133 words each). Every humor line they carry is
  rated KEEP in `drafts/monograph-limits/humor-review-v0.6.md` (#4 sheep, #8 rabbit/fox, #9 Müller-Lyer,
  #12 "basically", #15 lunch, #34 spacecraft). No REWORD or CUT line is used. Passages under announced v0.7 rewrite
  (Ch 4.5, Ch 5.1, Ch 15 "One limit" and "The limits as refutations", "decidable locally") were avoided.
  Two verbatim alternates, also KEEP: Ch 2 Gabriel's horn ("Rotate the curve" … "though not in Latin.", 142 words,
  #5) and Ch 11 shredder ("Normalization does not imply reversibility." … "has derived it from nothing.", 97 words, #25).
- Book titles in "In preparation": the draft files' own `#` headings (`drafts/papers-book/paper1-draft.md`,
  `drafts/papers-moc7/definitions-not-settled.md`, `theory-map-paper.md`, `minimal-self.md`,
  `robot-consciousness-plea.md`); the robot plea's title is set in title case here (draft: "Silent suffering: a plea
  to consciousness science and robotics").
- SJÄLV facts: `.claude/knowledge/sjalv-booklet-build.md`, `docs/pending-sjalv-manual.md`,
  `docs/pending-sjalv-print-order.md`, `drafts/sjalv-print/build_booklet.py` (back-cover blurb, QR target).
- Contribute: `drafts/contribute-primer/wiki-contribute-index.md`, redacted (below).

## Open items — MG must clear before publishing

1. ~~TODO-D22~~ **Resolved (MG S338):** no AI-use declaration in the book body or on the page. For books, KDP handles it outside the book. Inline declarations are for papers only. The placeholder section was removed from `no-outside/index.html`.
2. **Teaser selection — APPROVED by MG S338 2026-10-19 (all six as drafted).** (Earlier note, MG S338: the sheep passage is the best so far; the rest waits until his v0.6 review is done, he is about halfway).** The v0.6 manuscript is headed "Not for circulation", and MG's proofread of v0.6 is still
   running. Five of the six passages contain humor lines inserted by an agent pass and reviewed by Fable; only the
   sheep line (Ch 2) is MG's own text. MG approves, swaps (alternates above) or drops each passage, and the
   passages are re-checked against the final text before publishing.
3. **Contribute redaction — MG S338: keep redacted for now (crucible open-sourcing is being prepared).** The landing-page section drops every crucible result: no numbers (Spearman values,
   seed counts, attribution splits, run times, network sizes, the 92.4 % CRU-83 figure), no findings (CRU-70
   confirmed, CRU-78 negative falsified and the block-dominance control, KIT-S1 null, CRU-176 inconclusive, the
   count of failed necessity tests). It keeps the invitation, the experiment IDs with their questions, hardware
   needs and the ground rules. MG confirms the redaction, or crucible clears specific results for publication.
   ⚠ **The wiki primer itself still carries all of these results.** It must be redacted the same way, or cleared
   by crucible, before the AIW-296 wiki deploy publishes it. Its first line also says the SJÄLV QR leads to that
   page; the QR leads to the Zenodo concept DOI (`docs/s334-report.md`), so that sentence needs fixing too.
   Registration, repo URL and data-return channel are still `{{TBD-crucible}}` in the primer, so the landing page
   says registration is not open yet.
4. **SJÄLV publication — APPROVED by MG S338 ("P4 ok").** Confirm that the booklet PDF goes online, under the card deck's private-use terms, and
   confirm the artwork credit "AI-generated from the author's brief" (marked `TODO-MG` in the HTML; the source
   record says the drawings came from an external AI model working from MG's brief).
5. **In-preparation list — APPROVED by MG S338 ("P5 ok").** Confirm the six working titles may be listed publicly. Definitions A's title had an
   open keep-or-rephrase question in `docs/pending-s335-handover.md` (Q3, recommendation: keep).
6. **Book blurb — APPROVED by MG S338 2026-10-19.** The three short paragraphs and the one dry line ("The argument covers its author. He looked for an
   exemption and did not find one.") are agent-written in MG's voice; MG edits or approves.
