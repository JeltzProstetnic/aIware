# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-13 (Session 16)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Overleaf upload, arXiv submission, outreach execution

## Current State
- **Active Task**: Overleaf upload DONE, arXiv submission next
- **Progress**:
  - Uploaded `arxiv/` to Overleaf via zip — compiles successfully
  - Fixed Table 3 overlap: column spec changed to wrapping `p{}` columns + `\arraystretch{1.4}` for row padding
  - PDF downloaded from Overleaf for sharing
  - Local `arxiv/paper.tex` synced with Overleaf version
- **Next**: Start arXiv submission process, get endorsement code, send Shriki/Hengen emails

## What Changed This Session (Session 16)

### Overleaf Setup
- Created zip of `arxiv/` directory, uploaded to Overleaf
- Paper compiles cleanly in Overleaf
- User downloaded PDF for family/friends

### Table 3 Fix (arxiv/paper.tex)
- Column spec: `{lllXl}` → `{>{\raggedright}p{1.9cm} >{\raggedright}p{1.7cm} >{\raggedright}p{3.2cm} X >{\raggedright\arraybackslash}p{2cm}}`
- Added `\renewcommand{\arraystretch}{1.4}` for row padding
- All five columns now support text wrapping; rightmost column no longer overlaps

## Files Modified
| File | Change |
|------|--------|
| `arxiv/paper.tex` | Table 3 column wrapping + row padding fix |

## Untracked Files (not committed)
| File | Status |
|------|--------|
| `The_Four_Model_Theory_of_Consciousness.pdf` | PDF downloaded from Overleaf — do NOT commit (binary) |
| `arxiv-upload.zip` | Temp upload artifact — do NOT commit |

## Previous Sessions Summary
- **Session 15**: 6 author-review revisions to paper.md + arxiv/paper.tex, Treisman1980 BibTeX added
- **Session 14**: Networking plan, LaTeX conversion, outreach emails drafted, arXiv/Overleaf accounts created
- **Session 13**: Prediction reorder (P1=fMRI), figure polish, consolidation audit
- **Session 12**: Paper trimmed to ~12k words, 3 SVG figures, cover letter
- **Session 11**: Full paper written, pop-sci content created

## Remote Config
- `origin` → `JeltzProstetnic/aIware` (public) — ONLY push target

## Open TODOs

### Immediate (This Session)
- [x] Upload `arxiv/` directory to Overleaf, verify compilation
- [x] Fix Table 3 column overlap
- [ ] Start arXiv submission → get endorsement code
- [ ] Update Shriki/Hengen emails with endorsement link, send them
- [ ] Draft ASSC 29 abstract

### arXiv-Specific
- [ ] Get endorsement for q-bio.NC (best candidates: Shriki, Hengen, Priesemann)
- [ ] Submit to arXiv once endorsed
- [ ] Cross-list to cs.AI

### Near-term (Deadlines)
- [ ] ASSC satellite workshop submission (deadline **Feb 28**)
- [ ] ASSC 29 abstract submission (deadline TBD, submissions open now)

### Outreach (after arXiv live)
- [ ] Email Metzinger (German)
- [ ] Email Carhart-Harris (P3 experiment pitch)
- [ ] Email remaining Tier 2-4 contacts
- [ ] LinkedIn posting with Figure 1 PNG

### Ongoing
- [ ] Sync private repo
- [ ] Frontiers submission
- [ ] Magazine submissions
- [ ] Book manuscript review

## Recovery Instructions
1. Read THIS FILE first
2. Paper is on Overleaf (compiles cleanly, Table 3 fixed)
3. `outreach-emails.md` has 5 email drafts — Shriki/Hengen need endorsement link added before sending
4. `networking-plan.md` has the full contact strategy
5. Paper has 9 predictions with P1=fMRI signatures
6. Next: arXiv submission → endorsement code → send emails → ASSC abstract
