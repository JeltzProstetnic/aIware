<!-- Action: reference -->
<!-- Tracked-by: AIW-289, AIW-286, AIW-130, AIW-278, AIW-279, AIW-280, AIW-281, AIW-284, AIW-290, AIW-291, AIW-105, AIW-120, AIW-292 -->
# Zenodo drafts: readiness plan (2026-10-19)

MG's goal: *"make our paper drafts ready for my review so we can publish zenodo drafts for all"*. I read this as
publishing each draft as a Zenodo preprint, with a Zenodo draft record (not yet published) as the last check
before each DOI is minted.

**What I measured:** `wc -w` on every source. I ran the register checker (`register_gate.problems()`), the
first-deposit guards (`zenodo_first_deposit.scan_frozen_terms` / `scan_dangling_citations`) and the markdown
reference parser on each source, all without writing anything. I also made one read-only Zenodo GET by ORCID: it
returns 9 records (FMT, companion, RIM, cosmology, CMB, three roadmaps, Seth commentary). **None of the drafts below
is on Zenodo.**

**Excluded:** papers already deposited (the 9 above). Also excluded because nothing is drafted yet: PLR commentary
(AIW-228, brief only), Skeptic piece (AIW-294, assessment only), worm paper (AIW-289(3), literature check only),
falsity gradient (AIW-293), and the theory-map wiki page, which goes to the wiki rather than Zenodo.

## 1. Inventory

Columns: **Reg** = register hits · **Refs** = entries the markdown parser finds · **AI** = inline AI-use declaration ·
**288** = grep hits on the master wordings AIW-288 flags ("not binary", "free modelling suffices", "gating"). Each
288 hit still has to be read in context.

| # | Draft (path) | Words | Last review | PDF | Reg | Refs | AI | 288 |
|---|---|---|---|---|---|---|---|---|
| 1 | **No Outside** (book) `drafts/monograph-limits/no-outside-draft-v0.6.md` | 52,210 | Fable v0.4 verify (`verify-fable-v0.4.md`), humor review v0.6 | v0.6, 107 pp, `scripts/build_monograph_pdf.sh` | 0 | 56 | none (correct for a book) | 0 |
| 2 | **Limits Without an Outside** (paper 1) `drafts/papers-book/paper1-draft.md` | 8,996 | `docs/reviews/2026-10-18-opus-referee-paper1-draft2.md` → `…-draft3-changelog.md` | draft 3 | 0 | 53 | yes | 0 |
| 3 | **Operational Detector** (JAIC) `drafts/aiw130-jaic-draft.md` | 10,921 | `drafts/aiw130-PROPOSE.md` (Fable team, S274); edited S332 | md only; figs `figures/aiw130/jaic-fig1–3` | 0 | 33 | yes | 2 |
| 4 | **Pointing Is Not Defining** (Def A) `drafts/papers-moc7/definitions-not-settled.md` | 8,999 | `2026-10-16-fable-referee-definitions-A(-round2).md`, `2026-10-17-fable-citation-audit-definitions-A.md` | yes (2026-10-17) | 0 | 56 | yes | 1 |
| 5 | **Deriving a Definition…** (Def B) `drafts/papers-moc7/deriving-the-fmt-definition.md` | 8,822 | one review (`docs/s334-report.md` §3); `2026-10-17-fmt-definition-vs-C1-C9.md` | no | 0 | 25 | **no** | 0 |
| 6 | **Where the Theories Sit** (theory map) `drafts/papers-moc7/theory-map-paper.md` | 9,999 | fairness review (S334 report §3) | no | 0 | 59 | **no** | 2 |
| 7 | **Silent suffering** (robot plea) `drafts/papers-moc7/robot-consciousness-plea.md` | 5,747 | one review (S334) | no | 0 | 42 | **no** | 0 |
| 8 | **Too Late to Report** (minimal self) `drafts/papers-moc7/minimal-self.md` | 8,873 | one review (S334) | no | 0 | 76 | **no** | 2 |
| 9 | **More Than Computation** (NoC slice) `drafts/aiw130-noc-draft.md` | 8,860 | PROPOSE + S328/S332 edits | md only; `figures/aiw130/noc-fig*` | 1 | 46 | yes | 0 |
| 10 | **Near-criticality…** (eNeuro) `paper/aiw47/aiw47-eneuro-opinion.md` | 3,945 | `docs/aiw47-fable-review.md` | figures only | 3 | 18 | yes | 0 |
| 11 | **Permeability as Directed Information Flow** `paper/fmt_permeability_criticality/fmt-permeability-criticality.md` | 3,646 | none on file | **stale** (PDF 2026-07-06, `.md` 2026-10-07) | 3 | 16 | **no** | 8 |
| 12 | **Qualia privacy** (AIW-105) `drafts/aiw105-qualia-privacy-paper-draft.md` | 4,316 | none (written to await MG review) | no | 4 | **0** (no References heading) | **no** | 0 |
| 13 | **Two Roads to Recursive Closure** (AIW-120) `drafts/aiw120-olinyk-crc-fmt-convergence.md` | 2,397 | none (9 VERIFY items) | no | 8 | **0** ("References cited") | n/a | 0 |

## 2. State, blockers, effort

| # | State | Blocking items | Effort | MG review |
|---|---|---|---|---|
| 1 | v0.6 out for proofread | MG's v0.7 notes (`v0.7-proofread-notes.md`, 6 items so far; first line still reads "Draft v0.3"); W8 D5–D24 as a single question (`s338-decision-triage.md`); feedback from the four readers; **licence vs KDP** (§5). D22 is superseded: no AI declaration in the book (S338) | M | yes: proofread, W8, licence |
| 2 | draft 3, under the 9k cap | MG's read; Breuer full text (AIW-295: §4 premise is stronger than needed, §7 "sets the dynamics aside" is probably overstated, `aiw295-breuer-check.md`); cites No Outside "forthcoming" (fn 1 + reference) until the book has a DOI; the header says "Not for circulation" | S–M | yes: read draft 3, Breuer access |
| 3 | full draft | Open decisions: article type, time dilation, reviewer slates, named neuromorphic examples (`aiw130-PROPOSE.md`; slate confirmed S299). §6 in-silico grounding has no owner. EiC Kanai vs Suzuki is unreconciled (matters for submission, not for Zenodo). No `.tex` build | M | yes: 4 decisions, §6 scope |
| 4 | reviewed, PDF built | **Waiting for Signorelli** (MG 2026-10-18: *"waiting for feedback from others on this first"*). A sole-author DOI now could pre-empt co-authorship. Cites Def B "in preparation". Decision #3, title (`pending-s335-handover.md`). Kripke page and Casali methods are unchecked (S334 report §3) | S | yes: deposit before or after Camilo |
| 5 | draft | Def A first; decision #4, insect wording; "connectome" ×2 (AIW-206 freeze list); AI statement missing; cites Def A "in preparation" | M | yes: #4 |
| 6 | draft, about 2k words over the 6–8k brief | Decision #7 (PRM verdict, frame alignment); **a "Points for MG" section after the References would render into the PDF**; wiki-first (S338); AIW-296 keeps MoC7 paper contents off the wiki until deposit | M | yes: #7, cut |
| 7 | draft v1 | Decision #6 (self-binding, "servitude", title); crucible-robot disclosure under AIW-206; "connectome" ×1; co-author question; header says "not register-gated" (now 0 hits) | M | yes: #6 |
| 8 | draft | Decision #5 (cite the MoC7 talks only after asking the authors: 12 Allen/MoC7 hits; Zahavi); check against the S334 sleep ruling | M | yes: #5 |
| 9 | draft | Thesis vs the S329 ruling (criticality is not required); venue/deadline 2026-12-31 via AIW-292; a preprint may affect a special-issue submission (§5) | M | yes: thesis re-check |
| 10 | manuscript | Anonymised for double blind, so the Zenodo version needs the author block merged back in; 3 register hits | S | yes: venue order (AIW-292) |
| 11 | manuscript; PDF three months behind its source | 3 register hits; 8 "not binary"/"gating" hits against AIW-288; no review; AI statement missing | S–M | light |
| 12 | first draft, July | Predates master v15–v19; 9 VERIFY; 4 register hits; **"decompilation" (its core term) and "connectome" are on the AIW-206 frozen list, 21 hits**, so it needs a crucible ruling or a rewording; add a `## References` heading | M | yes: full read |
| 13 | draft | 9 VERIFY; 8 register hits; Claude co-development circularity; rename the heading to `## References` | S | yes: full read |

## 3. Zenodo gates: what each draft must pass

**Tooling gap (blocks every row).** Neither creation path covers a markdown-born paper end to end:
- `zenodo-upload.sh` only versions an *existing* concept DOI. It runs the changelog guard, `register_gate`,
  `pdf_markup_gate` and `publish_gate`. **Never use it for a first deposit.**
- `zenodo-new-record.py` creates a record and has `--draft`, but it runs **no gates at all**.
- `zenodo_first_deposit.py` creates a record with guards: not already deposited, PDF newer than its `.md`, AIW-206
  frozen terms, dangling "manuscript/forthcoming". It has `--dry-run` **but no draft-only mode**, and it does not run
  the register, markup, reference or overflow gates.
- `register_gate.py` and `publish_gate.py` are keyed by **concept DOI**. A new paper has none, so both exit 2 or 3
  (they fail closed).
- `verify_references.py` parses markdown `## References`, but `PAPERS` has only `rim, cosmology, fmt, fmt_formal,
  rim_formal, cosmology_formal, noc`. **No draft has a `--paper` key.** Each needs a key, for example `nooutside`,
  `paper1`, `jaic`, `defa`, `defb`, `theorymap`, `robot`, `minself`, `nocslice`, `eneuro`, `permeability`,
  `qualia`, `olinyk`, then an `--update` run (network, under tmux) and a reviewed manifest.

**Proposed extension (one session, tests first):** give `zenodo_first_deposit.py` a `--draft` mode (create, upload,
metadata, `prereserve_doi`, no publish) and a `--publish-id`. It should call `register_gate` and `publish_gate` by
**source path** (new `--source` mode in both), `pdf_markup_gate`, `verify_references --check --paper <key>` and
`check-pdf-overflow.sh`. It should also refuse:
- a PDF under 10 KB or without a `%PDF` header (LFS pointer);
- a paper without an AI-use paragraph, and a book that has one (S338 ruling);
- leftover `<!--`, "Points for MG", VERIFY, "Not for circulation".

Retire or wrap `zenodo-new-record.py`. **Expected false positives**, cleared per line through the existing
`--allow-dangling` and a new `--allow-frozen` (line-numbered, after review, never a blanket skip): "manuscript" in AI
statements (JAIC l.210, NoC, eNeuro, Def B header) and "connectome" (Def B, robot plea). Every new artifact also goes
into `register_gate.SOURCES` and `publish_gate.ARTIFACTS` once its concept DOI exists.

**Per-deposit gate list (all drafts):**
1. Register gate, whole body: clear (rows 9–13 currently fail).
2. Reference-existence gate with its own `--paper` key: every row `verified` or `verified-manual`.
3. Publish gate by path: no open backlog item names the file unless acknowledged by ID.
4. PDF markup gate + overflow ≤ 2 pt.
5. First-deposit guards: frozen terms (crucible clearance for unpublished results, AIW-206), no dangling sibling
   citations.
6. AI-use declaration: inline for papers; **none in No Outside** (S338: KDP handles books).
7. Metadata spec (`scripts/zenodo-specs/<name>.json`): title as in the PDF; HTML abstract taken from the paper;
   keywords; `cc-by-4.0` for papers (the tool's default); creator with ORCID; version `v1`; `related`.
   - FMT-derived papers (3, 5, 6, 8, 9, 10, 11, 12): `isSupplementTo` FMT concept `10.5281/zenodo.18669891`.
   - Papers that only cite FMT (4, 7, 13): `references` it.
   - Paper 1: `isDerivedFrom` the No Outside concept DOI.
   - No Outside: `references` FMT and the SB-HC4A concept `10.5281/zenodo.18698605`.
   - These relations are my proposal; MG confirms them once.
8. Changelog `docs/zenodo-changelog-<name>-v1.md` (tracked, S329).

**Traps.** Never rebuild a canonical `paper/*/paper.pdf` for comparison. Build into `tmp/` and promote. The draft
PDFs are `filter=lfs`: on a clone without git-lfs they are 131-byte pointers that would upload "successfully".
`git checkout` cannot restore a raw-blob canonical. Rebuild from the `.md` right before depositing, because a
committed PDF can lag its source (the S293 fmt-formalization case). After publishing, download the file back and
compare its md5 with the local file. Cite the **concept** DOI.

## 4. Recommended order

This follows the S338 work order (No Outside v0.7 → paper 1 → JAIC → PLR → Tier 2 → Skeptic → AIW-288/285; *"items
1–2 wait on MG's reads; work in the meantime goes to 3/4"*):

| Order | Session output |
|---|---|
| **Z1** (now) | Deposit tooling (§3), tests first; `--paper` keys and manifest rows for all 13; metadata specs drafted |
| **Z2** (now) | JAIC (#3) ready for review: md→PDF with figures, 4 decisions listed, 288 hits resolved |
| Z3 (when MG's notes arrive) | No Outside v0.7 ready; licence decision; deposit → book DOI |
| Z4 (after MG's read) | Paper 1 draft 4: Breuer verdicts applied, "forthcoming" → book DOI |
| Z5 | Theory map (#6): decision #7, cut, notes stripped; wiki update after deposit |
| Z6 | Robot plea (#7) + minimal self (#8): decisions #6 and #5, AI statements |
| Z7 (after Signorelli) | Def A + Def B as a pair, cross-citations through pre-reserved DOIs |
| Z8 (after AIW-292 venue ruling) | NoC slice (#9), eNeuro (#10), permeability (#11) |
| Z9 | Qualia privacy (#12) + Olinyk note (#13): VERIFY pass, master check, crucible ruling |

The PLR commentary sits between Z4 and Z5 in the work order. It produces no Zenodo draft yet.

## 5. Per-session deliverable ("ready for MG review")

Each paper session produces, in one folder `drafts/zenodo-ready/<name>/` that is opened for MG:
1. A **clean PDF** built through the gated path (`scripts/build-md-pdf.sh`; `build_monograph_pdf.sh` for the book),
   with every gate in §3 green, or each red item listed by line.
2. A **changelog** `docs/reviews/<date>-<name>-zenodo-ready-changelog.md`: what changed since the last review, with
   ID → status rows as in the paper 1 changelogs.
3. A **decision list** of open MG calls, each with a recommended option, asked one by one at session end.
4. The **metadata spec** JSON, abstract and keywords, for MG to read alongside the PDF.

Nothing is deposited in that session. The deposit follows MG's sign-off, in a short follow-up step.

## 6. Checklist for one deposit

1. `git fetch private && git merge --ff-only private/main`; worktree clean.
2. MG's sign-off on this exact PDF version, recorded in `docs/decisions.md`.
3. Rebuild from `.md` into `tmp/`; confirm the PDF is over 10 KB and starts with `%PDF`; overflow ≤ 2 pt; page count
   plausible.
4. `python3 scripts/register_gate.py --source <md>`: clear.
5. `python3 scripts/verify_references.py --check --paper <key>`: OK.
6. `python3 scripts/pdf_markup_gate.py <pdf>`: clear.
7. Publish gate by path: clear, or `PUBLISH_GATE_ACK=` with each ID named.
8. AI statement present (paper) or absent (book); no `<!--`, "Points for MG", VERIFY or "Not for circulation".
9. Sibling citations point to concept DOIs (none "forthcoming" or "in preparation" unless a DOI is pre-reserved).
10. Spec JSON checked: title = PDF title, abstract current, keywords, licence, related identifiers, ORCID.
11. `zenodo_first_deposit.py <spec> --dry-run`, then `--draft`; open the draft record page and check it with MG.
12. `--publish-id <id>`; record the concept and version DOIs.
13. Download the file back; compare md5; check `access`/`license` on the landing page (polite User-Agent).
14. Same session: add the concept DOI to `register_gate.SOURCES`, `publish_gate.ARTIFACTS`, backlog entry,
    `ABOUT.md`/README table (AIW-254), wiki pointer (AIW-296), `contacts.md` if someone is waiting on it; commit;
    `filtered-push.sh`.

## 7. Risks

- **No Outside before MG's v0.7 notes:** a permanent DOI fixes errors that are still known and open (L1 wording,
  "decidable locally", the six uncited neighbours in notes #2–#3). Deposit only from v0.7.
- **Book licence vs KDP:** MG intends KDP for books (S338). As I understand it, KDP Select requires digital
  exclusivity, which a free Zenodo PDF would break. A CC BY licence would also let anyone resell the book.
  Options: CC BY-NC-ND, or a deposit with restricted files. **Unverified against current KDP terms.**
- **Prior-claim races:** paper 3's triviality move is partly anticipated (Aaronson 2013, Millhouse 2019; Kanai & Ma
  arXiv 2606.15348 is the freshest opponent; `paper3-literature-check.md`). The core of paper 1 is in the book, so
  the book DOI timestamps it. The Skeptic piece carries a high prior-art risk per move (AIW-294). Depositing early
  protects priority only for what is actually in the deposited text.
- **Preprints vs journals:** the Springer titles say a preprint is not prior publication, and Philosophia
  Mathematica (OUP) allows an author's original version (`venues-paper1.md`). Erkenntnis, EJPS, Phil Studies, JGPS,
  Inquiry and Philosophy of Science are **unverified**. JAIC, NoC (special issue), eNeuro and JCS are **unverified**,
  and JCS and eNeuro are double-blind: a named Zenodo preprint is findable by reviewers. Check each venue page before
  depositing anything aimed at it (AIW-292).
- **Def A and co-authorship:** a sole-author DOI before Signorelli answers may close the co-author route MG hopes
  for.
- **Crucible disclosure:** AIW-206 freezes implementation vocabulary, and the robot plea touches the crucible robot.
  A deposit is permanent public disclosure (EPC Art. 54 is the reason for the guard).
- **Master contradictions (AIW-288):** drafts that quote pre-correction readings of the master would cite v19 for
  wording v20 will reverse. Fix them in the draft, citing the corrected reading, or deposit after v20.
- **MoC7 material:** citing unpublished talks or posters (minimal self, theory map, Def A) without the authors'
  consent.
- **Volume:** 13 new DOIs in a few weeks, from a sole author, may read as preprint flooding. The order above spaces
  them by readiness.
