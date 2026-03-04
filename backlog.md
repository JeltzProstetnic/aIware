# Backlog — aIware

**Shared strategy & targets:** `~/cfg-agent-fleet/cross-project/fmt-visibility-strategy.md`

## Waiting (no action needed — track responses)

| What | Submitted | Expected Response |
|------|-----------|-------------------|
| NoC resubmission (trimmed FMT paper) | Resubmitted Mar 4, 2026 (new submission, not revision). Editor email sent to Andrillon. | ~6 weeks from Mar 4 (mid-April) |
| Phil Psych (intelligence paper) — DESK REJECTED | Feb 23, 2026 | ~~5 months~~ REJECTED Feb 25 |
| Theory & Psychology (intelligence paper, TAP-26-0111) | Feb 2026 | In review — unknown timeline |
| AISB 2026 symposium abstract (FMT + ethics) | Feb 22, 2026 | By Mar 21 (acceptance notification) |
| Bochum "Conscious Mind at 30" poster abstract | Feb 24, 2026 | Before May 30 (registration deadline) |
| Neurophenomenology satellite abstract (Santiago) | Feb 22, 2026 | TBD (remote requested) |
| MetaLab Summer School application (London) | Feb 22, 2026 | Acknowledged Mar 2 (Sarah Kalwarowsky, UCL) — reviewing over coming weeks |
| Outreach emails (13+ researchers) | Feb 14-24 | Ongoing — see strategy file for unified status |

## Open

- [ ] [P1] `AIW-01` **Seth BBS peer commentary** (deadline: June 12, 2026): Paper "Conscious artificial intelligence and biological naturalism" (BBS, April 2025). Submit formal commentary proposal via BBS call. Angle: predictive processing is substrate-neutral math — FMT provides the architectural specification Seth lacks.
- [x] [P1] ~~`AIW-02` **Fix session-context.md / MEMORY.md missing from repo**~~: RESOLVED Session 128 — `session-context.md` tracked in git, on private remote, excluded from public via `.push-filter.conf`. `MEMORY.md` lives in `~/.cc-mirror/` (Claude Code config), correctly not in repo. Both persist across sessions.
- [ ] [P1] `AIW-16` **Digital Minds Fellowship application** (deadline: **March 27, 2026**): Cambridge Digital Minds, Aug 3-9. AI consciousness/welfare research. 15 fellows, fully funded (travel + accommodation + £1,000). Apply at digitalminds.cam/fellowship/.
- [ ] [P1] `AIW-17` **Scott McFarnell SMRI feedback**: He asked for feedback on his SMRI formula (Feb 24 reply, unanswered). Live contact showing reciprocal interest. Read his ACU preprint, provide substantive SMRI analysis.
- [ ] [P2] `AIW-18` **RIM preprint v2 to PhilSci-Archive or Zenodo**: PsyArXiv rejected v2 ("outside scope"). Theory & Psychology in review (TAP-26-0111). Upload v2 preprint to PhilSci-Archive (primary) or Zenodo (fallback).
- [ ] [P1] `AIW-11b` **Pop-sci book — German review pass**: `pop-sci/book-manuscript-de.md` (~2,400 lines, quality revision ~75% complete). Complete remaining ~25% (lines 753-1057 + 1976-2400).
- [ ] [P2] `AIW-03` **Cosmology paper to SSRN**: Submit SB-HC4A to SSRN PhysicsRN. Preprint already on Zenodo.
- [ ] [P2] `AIW-04` **Bochum conference registration**: Register by May 30 at RUB external registration site. Poster abstract already submitted. ATTEND IN PERSON — Melloni, Chalmers, Seth will be there.
- [ ] [P2] `AIW-05` **Researcher outreach — Wave 2** (not yet contacted): Priority targets from `tmp/outreach-master-list-2026.md` — Megan Peters (UC Irvine), Michael Pitts (Reed), Georg Northoff (Ottawa), Olaf Blanke (EPFL), Pedro Mediano (Imperial), Andrea Luppi (Oxford/Cambridge), Robin Carhart-Harris, Viola Priesemann.
- [ ] [P2] `AIW-06` **Conference submissions still open**: 6ICPH Porto (rolling, 250-word abstract, hybrid), SAGE Adaptive Behavior neurophenomenology (May 1, 2026), Models of Consciousness 7 Shanghai (TBA, monitor amcs-community.org), TSC 2026 Tucson (Apr 6-11), AAAI Spring Symposium on Machine Consciousness Burlingame (Apr 7-9).
- [ ] [P3] `AIW-07` **Full FMT paper to journal** (AFTER NoC decision): Top target: *Physics of Life Reviews* (IF ~11-13). Backup: *Consciousness & Cognition*, *JCS*. Do NOT submit while NoC review is active. File: `paper/full/four-model-theory-full.md` (16,744 words).
- [ ] [P4] `AIW-08` **arXiv preprint — UNLIKELY** (AFTER NoC decision): Needs endorsement (q-bio.NC) which is hard to get without institutional affiliation. Endorsement link: https://arxiv.org/auth/endorse?x=E9JU9T. Deprioritized — endorsement may come via outreach contacts. Keep link alive.
- [ ] [P3] `AIW-09` **Online presence / discoverability**: ResearchGate profile, Google Scholar profile (auto after arXiv/journal), ORCID link publications (0009-0005-9697-1665), LinkedIn post (`pop-sci/linkedin-post.md`, post after arXiv/journal).
- [ ] [P3] `AIW-10` **Formalization papers** (3 roadmaps complete): FMT (`paper/fmt_formal/`), RIM (`paper/rim_formal/`), SB-HC4A (`paper/cosmology_formal/`). Need collaborators (computational neuroscientists) — potential outcome of outreach.
- [ ] [P3] `AIW-11a` **Pop-sci book — English review pass**: `pop-sci/book-manuscript.md` (~31,000 words, needs flow/consistency review). KDP setup complete (ISBNs assigned, covers built).
- [x] [P3] ~~`AIW-15` **Redesign "simple" diagrams in all AC design PDFs**~~: DONE Session 129 — all 16 simple diagrams redesigned to TD (top-down) flow with subgraph grouping for implicit/explicit layers, shortened labels, visible self-ref loops. Render height increased to 900px. All PNGs and PDFs regenerated.
- [ ] [P4] `AIW-12` **AC architecture design — MIGRATED**: Implementation split into `~/mirror-box/` (Design 16, public) and `~/crucible/` (Design 15, private). `~/aIware.implementation/` archived. Phase 1 complete. See `docs/engineering/` for all designs.
- [ ] [P4] `AIW-13` **Respond to peer review**: Prepare for likely objections: epiphenomenalism, lack of formalization, independent researcher status. ConCrit (Algom & Shriki) convergence is strongest defense.
- [ ] [P5] `AIW-14` **COGITATE commentary — PARKED**: Draft at `tmp/cogitate-commentary-draft.md` (1,587 words, limit 1,500). Target: NoC Spotlight Commentary. **Parked reason (Session 119):** NoC charges €2,144 APC (Oxford University Press open access). No waiver path for independent researchers. Not paying to fix their experimental design. Revisit only if fee structure changes or institutional affiliation acquired.

## Done

### 2026-02-28
- [x] Compiled 16 AC design PDFs + landscape overview (17 PDFs in `docs/engineering/designs/pdf/`). Build scripts: `tmp/build_design_overview.py`, `tmp/build_individual_pdfs.py`.

*(Older items archived to `docs/backlog-archive.md`)*
