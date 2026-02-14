# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-14 (Session 25, in progress)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Reframe Prediction 8, create changes-highlighted paper version, prepare for book writing

## Current State
- **Active Task**: Session 25 work in progress.
- **Progress**: Prediction 8 reframed, highlighted-changes PDF generated.
- **Pending**: Conversation log update, git commit, book chapters (deferred to next session).

## Session 25 Summary

### Completed:
1. **Prediction 8 reframed** in `paper/full/arxiv/paper.tex`:
   - OLD: "Lucid Dream Onset Is a Criticality Threshold Crossing" (narrow, single prediction)
   - NEW: "Sleep Architecture Reflects Criticality Maintenance" (expanded with 5 sub-predictions)
   - Key argument: Brain is inherently unstable analog substrate, never calibratable for digital computation. The CA at criticality provides stable digital layer. Substrate drifts → CA breaks down radically (sleep onset). NREM restores substrate; REM = substrate briefly re-approaching criticality (CA flickers on = dreams). 90-min ultradian cycle = oscillation around critical point.
   - Sub-predictions: (a) waking criticality decline, (b) sleep onset as radical transition, (c) NREM/REM cycling tracks criticality, (d) lucid dreaming as ESM threshold crossing, (e) sleep deprivation produces subcriticality
   - Compiles cleanly: 50 pages, no errors
2. **Changes-highlighted PDF** — `paper/full/arxiv/paper-changes.tex` + `.pdf`:
   - Baseline: pre-Session-24 version (commit `7a39188`)
   - 6 yellow-highlighted change blocks (Session 24 + Session 25 edits)
   - Reusable script: `paper/full/generate_changes_pdf.py`
   - Baseline saved at `/tmp/paper-pre-session24.tex` (volatile — save to repo if needed for future diffs)

### Not addressed (deferred to next session):
- **Book chapters** — user wants to start writing (Ch. 2 Brain Anatomy + others in parallel)
- arXiv endorsement — still blocked
- Wave 2 outreach emails — drafts ready, NOT SENT

### Author note (captured for future use):
- **Toddler 3rd→1st person speech**: When toddlers switch from referring to themselves in 3rd person to 1st person, that marks the separation between EWM and ESM. (Potential developmental evidence for the four-model architecture — relevant for Ch. 6 / The Boundary, or as supporting evidence for Prediction 1.)

## Key File Locations
- **Full LaTeX (edited this session)**: `paper/full/arxiv/paper.tex`
- **Changes-highlighted PDF**: `paper/full/arxiv/paper-changes.pdf`
- **Changes generator**: `paper/full/generate_changes_pdf.py`
- **Baseline for diff**: `/tmp/paper-pre-session24.tex` (VOLATILE)
- **Trimmed LaTeX (SUBMITTED, do NOT modify)**: `paper/trimmed/arxiv/paper.tex`
- **Pop-sci book outline**: `pop-sci/book-outline-expanded.md`
- **Pop-sci manuscript**: `pop-sci/book-manuscript.md`

## Session 26 TODO (suggested priority)
1. **Start writing the book** — multiple chapters in parallel (Ch. 2, 3, 5, or others per user preference)
2. **arXiv endorsement**: Check email for responses, explore alternative paths
3. **Wave 2 outreach**: Review/send Metzinger, Carhart-Harris, Priesemann emails
4. **Save diff baseline to repo** (currently in /tmp, will be lost on reboot)

## Recovery Instructions
1. Read THIS FILE first
2. Read `pop-sci/book-outline-expanded.md` for book structure and chapter dependencies
3. Read `pop-sci/book-manuscript.md` for existing 12-chapter draft
4. Paper is SUBMITTED to NoC (2026-02-13) — do NOT modify trimmed version
5. ALWAYS push to BOTH remotes: `git push origin main && git push private main`
