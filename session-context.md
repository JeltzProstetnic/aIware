# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-13 (Session 22)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: NoC submission checklist — ALL ITEMS RESOLVED

## Current State
- **All paper versions compile**: trimmed (41pp) + full (47pp)
- **NoC submission**: SUBMITTED 2026-02-13 via ScholarOne (https://mc.manuscriptcentral.com/ncon)
- **Both PDFs copied to Windows**: `C:\Users\Matthias\Documents\`

## PDF Files on Windows (`C:\Users\Matthias\Documents\`)
| File | Style | Version | Status |
|---|---|---|---|
| `four-model-theory-trimmed-modern.pdf` | Modern (LaTeX) | Trimmed, 41pp | CURRENT |
| `four-model-theory-full-modern.pdf` | Modern (LaTeX) | Full, 47pp | CURRENT |

## Session 22 Changes
1. Ran full NoC submission checklist audit (5 parallel verification agents)
2. Cover letter convergence claim softened to match manuscript ("independently of, though not prior to")
3. Data Availability Statement added to both trimmed and full paper.tex
4. Funding Declaration added to both trimmed and full paper.tex
5. Aaronson2014 .bib entry fixed (@article → @misc) in both versions
6. Figure alt text prepared for ScholarOne: `paper/trimmed/noc/figure-alt-text.md`
7. Submission checklist updated with all Session 22 changes
8. Both PDFs recompiled and copied to Windows

## Emails Status
- **Wave 1 SENT**: Shriki + Hengen (arXiv endorsement) — NO RESPONSES YET
- **Wave 2 PENDING**: Metzinger, Carhart-Harris, Priesemann

## Next Steps
- **Submit to NoC**: Paper is ready. Go to https://academic.oup.com/nc → Submit
- **arXiv**: Still blocked on endorsement (Wave 1 emails sent, no response)
- **Wave 2 outreach**: Metzinger, Carhart-Harris, Priesemann — drafts ready in correspondence/

## Key File Locations
- NoC markdown: `paper/trimmed/noc/four-model-theory-noc.md`
- Trimmed LaTeX: `paper/trimmed/arxiv/paper.tex`
- Full LaTeX: `paper/full/arxiv/paper.tex`
- Cover letter: `correspondence/cover-letter-noc.md`
- Submission checklist: `paper/trimmed/noc/SUBMISSION-CHECKLIST.md`
- Figure alt text: `paper/trimmed/noc/figure-alt-text.md`
- Outreach emails: `correspondence/`

## Compile Commands
- **LaTeX trimmed**: `cd paper/trimmed/arxiv && pdflatex -interaction=nonstopmode paper.tex`
- **LaTeX full**: `cd paper/full/arxiv && pdflatex -interaction=nonstopmode paper.tex`

## Recovery Instructions
1. Read THIS FILE first
2. Paper is READY for NoC submission — all checklist items green
3. ALWAYS push to BOTH remotes: `git push origin main && git push private main`
