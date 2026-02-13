# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-13 (Session 14, in progress)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Networking plan, arXiv submission preparation, LaTeX conversion

## Current State
- **Active Task**: LaTeX conversion complete, ready for Overleaf upload
- **Progress**:
  - Networking plan saved to `networking-plan.md`
  - Full LaTeX conversion: `arxiv/paper.tex` (739 lines) + `arxiv/references.bib` (99 entries, 978 lines)
  - Three PNG figures copied to `arxiv/`
  - README hero image changed: Figure 2 (real/virtual split) now at top
- **Next**: User creates arXiv + Overleaf accounts, uploads arxiv/ to Overleaf, seeks endorsement

## What Changed This Session

### Networking Plan (NEW)
- Created `networking-plan.md` with tiered contact strategy
- Tier 1: ConCrit authors (Algom/Shriki), Hengen/Shew, Metzinger, Graziano
- Tier 2: Carhart-Harris, Melloni (COGITATE), Priesemann, Massimini
- Tier 3: AI consciousness (Butlin, Schneider, Birch, Anthropic)
- Tier 4: Philosophers (Frankish, Goff, Schwitzgebel)
- Conference targets: ASSC 29 (Santiago, Jun 30-Jul 3), satellite workshop (deadline Feb 28!)

### LaTeX Conversion (NEW)
- `arxiv/paper.tex`: Complete conversion from paper.md
  - All Markdown → LaTeX (sections, emphasis, citations, lists, tables)
  - 4 tables converted to proper LaTeX tabular environments
  - 3 figures placed with captions and labels
  - natbib citations (plainnat style) throughout
  - All cross-references use `\ref{}` and `Section~N` format
- `arxiv/references.bib`: 99 BibTeX entries covering all paper references
  - All citation keys match between .tex and .bib
  - Proper diacritics (Llinás, Klüver, Güntürkün, etc.)
  - Acronyms protected with braces in titles
- `arxiv/*.png`: Three figure PNGs (1720px retina)

### README Update
- Hero image changed from Figure 1 to Figure 2 (real/virtual split) per user preference

## Files Modified/Created
| File | Change |
|------|--------|
| `networking-plan.md` | NEW — Full networking strategy with tiers, conferences, channels |
| `arxiv/paper.tex` | NEW — Complete LaTeX conversion of paper.md |
| `arxiv/references.bib` | NEW — 99 BibTeX entries |
| `arxiv/*.png` | Copies of figure PNGs for arXiv bundle |
| `README.md` | Hero image swapped to Figure 2 |

## Remote Config
- `origin` → `JeltzProstetnic/aIware` (public) — ONLY push target
- Changes NOT yet committed/pushed

## Open TODOs

### Immediate (This Session)
- [ ] User: Create arXiv account (arxiv.org, "Independent" affiliation)
- [ ] User: Create Overleaf account (overleaf.com)
- [ ] Upload `arxiv/` directory to Overleaf, verify compilation
- [ ] Commit and push networking-plan.md, arxiv/, README change

### arXiv-Specific
- [ ] Get endorsement for q-bio.NC (best candidates: Shriki, Hengen, Priesemann)
- [ ] Submit to arXiv once endorsed
- [ ] Cross-list to cs.AI

### Near-term
- [ ] ASSC 29 abstract submission (deadline TBD, submissions open now)
- [ ] ASSC satellite workshop submission (deadline Feb 28)
- [ ] Email ConCrit authors (Shriki/Algom)
- [ ] Email Hengen/Shew
- [ ] Email Metzinger (German)
- [ ] LinkedIn posting with Figure 1 PNG (after arXiv goes live)

### Ongoing
- [ ] Sync private repo
- [ ] Frontiers submission
- [ ] Magazine submissions
- [ ] Book manuscript review

## Recovery Instructions
1. Read THIS FILE first
2. `arxiv/` directory contains complete LaTeX package ready for Overleaf
3. `networking-plan.md` has the full contact strategy
4. Paper has 9 predictions with P1=fMRI signatures
5. README now leads with Figure 2 (real/virtual split)
6. Nothing committed yet this session — all changes are local
