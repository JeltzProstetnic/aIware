# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-16 (Session 53, in progress)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Analyze Perplexity review thread → book additions + paper change tracking system

## What Was Done (Session 53)

### Perplexity Thread Analysis
Analyzed a detailed Perplexity Deep Research thread covering reviewer vulnerabilities:
1. Self-referential closure → experience (is the defense defensible?)
2. "Virtual qualia are real" — the genuine/functional dichotomy
3. Lack of mathematical formalization
4. Social component of experience (babies, learned qualia)
5. "Simulation must feel" functional necessity argument

### Book Additions (4 new sections in `pop-sci/book-manuscript.md`)

1. **Identity claim + H₂O analogy** — New paragraph in Ch.4 after the self-referential closure argument. Makes the identity claim explicit: experience IS four-model self-simulation at criticality, like water IS H₂O. Falsifiable but not further explainable.

2. **"But Couldn't the Simulation Run 'In the Dark'?"** — New subsection in Ch.4. Focused argument that phenomenality is functionally necessary: the simulation serves as evaluation mechanism; evaluation requires valence; valence IS phenomenality. Addresses RL objection (scalar in Class 1/2 vs ESM registration at Class 4). Brings together scattered pieces from Ch.10 and Ch.14 into one focused argument.

3. **"Real Within the Simulation — What Does That Actually Mean?"** — New subsection in Ch.4 after the illusionism section. Dissolves the false dichotomy: "genuinely phenomenal" vs "merely functional" presupposes a god's-eye view that self-referential closure eliminates. Links to Metzinger's phenomenal transparency.

4. **"How Experience Develops: The Social Construction of the Self-Model"** — New section in Ch.10 after Baldwin Effect. Covers: infant qualia are learned not innate; social feedback trains ISM; developmental trajectory maps to graduated consciousness levels (newborn → mirror test → theory of mind → metacognition); feral child prediction; CBT as adult developmental recalibration. ~1,200 words.

### Paper Change Tracking System
- Created `paper/full/four-model-theory-full-tracked.md` — working copy of the full paper with tracked proposed changes
- Convention: HTML comment markers with source attribution for insertions/deletions
- Change log table at the top
- Three proposed additions from this session:
  1. New Section 6.7: Developmental Psychology Bridge
  2. Section 4.2: "Simulation must feel" argument strengthening
  3. Section 3.4: Identity claim framing

## Canonical File Paths
- **Full paper Markdown**: `paper/full/four-model-theory-full.md` (RECONCILED — ~16,744 body words)
- **Full paper TRACKED**: `paper/full/four-model-theory-full-tracked.md` (NEW — working copy with proposed changes)
- **Full paper LaTeX**: `paper/full/biorxiv/paper.tex` (STALE — needs regeneration from .md)
- **Full paper PDF**: `paper/full/biorxiv/paper.pdf` (bioRxiv version)
- **Trimmed paper (NoC)**: `paper/trimmed/noc/` (FROZEN — submitted 2026-02-13)
- **Intelligence paper**: `paper/intelligence/paper.md` (canonical, ~8,757 words)
- **Book manuscript**: `pop-sci/book-manuscript.md` (~30,500+ words after additions, 14 chapters + 3 appendices)
- **Book .tex**: `pop-sci/book-manuscript.tex` (STALE after book additions — needs rebuild)
- **Book PDF**: `pop-sci/book-manuscript.pdf` (STALE after book additions — needs rebuild)
- **Build script**: `tmp/build_book_pdf.py`

## User TODOs (Carried Forward + New)
1. **Two figure placeholders remain** in book-manuscript.md: five-layer stack SVG + VR illustration
2. **Book .tex regeneration**: Stale after Session 53 additions
3. **Book review pass** for flow/consistency — later
4. **Full paper .tex regeneration**: Still stale from Session 51
5. **BBS journal decision**: After NoC decision (~late March)
6. **Intelligence paper → NIP submission**
7. **Review tracked paper changes** in `four-model-theory-full-tracked.md` for journal submission

## Recovery Instructions
1. Read this file
2. Session 53 work: 4 book additions + tracked paper version
3. Book additions are in `pop-sci/book-manuscript.md` — search for "H₂O", "Run Dark", "What Does That Actually Mean", "Social Construction"
4. Tracked paper at `paper/full/four-model-theory-full-tracked.md`
5. Book .tex is STALE — needs rebuild via `tmp/build_book_pdf.py`
