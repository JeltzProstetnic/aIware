Action: act

# Session 161 Carryover — NoC Rejection Response + Paper Revision

## Context
NoC desk-rejected FMT trimmed paper a second time (NCONSC-2026-071, Andrillon, Mar 16).
Decision: abandon NoC, pivot to full paper submission at better journal.

## Priority Items

### 1. Fix REM sleep factual error
Andrillon: "sensory input is not entirely absent during REM sleep."
- Find the claim in `paper/full/four-model-theory-full.md` and `paper/full/biorxiv/paper.tex`
- Research current literature on sensory processing during REM sleep
- Correct the claim with proper citations
- Also fix in trimmed paper `.md` for consistency

### 2. Definition attack surface — assess, then minimize
Andrillon: "definition departs from standard focus on subjective experience and centers on the self"
- **First: is this criticism justified?** Launch Opus subagent to research: how do major theories (IIT, GNW, HOT, PP, AST) define consciousness? Is "subjective experience" really the standard? Or is Andrillon applying a narrow framing? FMT defines consciousness as self-simulation — which GENERATES subjective experience. Is centering on the mechanism rather than the output actually non-standard, or is Andrillon wrong?
- **Then: how to minimize the attack surface regardless?** Even if the criticism is unjustified, editors have this reaction. Research how to frame the definition so it explicitly connects to subjective experience literature without abandoning the self-simulation core. Add bridging language early in the paper.
- **Broader question: what other "attack surfaces" exist?** Review all Andrillon feedback + the first rejection feedback. Map every objection to a specific passage. Which can be fixed with better framing? Which require substantive changes? Which are gatekeeping we can't fix?
- Goal: make it structurally harder for any editor to dismiss FMT as "not about consciousness"

### 3. Refine predictions — fewer, sharper, better (OPUS SUBAGENTS)
Andrillon: "predictions too general or not specified enough"
- **Launch Opus subagents** to research each of the 9 predictions' current empirical landscape:
  - What experiments already exist that test similar claims?
  - What specific experimental designs would test each prediction?
  - What quantitative markers would confirm/refute each?
  - Which predictions distinguish FMT from ALL other theories vs just some?
- Based on subagent research, propose: which predictions to keep (strongest), which to sharpen (add specifics), which to drop (too general or not distinguishing)
- Also evaluate Andrillon's specific REM sleep objection — does it invalidate the prediction or just require a correction?
- Goal: 4-5 bulletproof, highly specific predictions with proposed experimental designs, instead of 9 general ones

### 4. Pick next journal target
- NoC done (2 desk rejections, 0 peer reviews)
- Full paper (16,744 words) is the submission vehicle now
- Top candidates: *Physics of Life Reviews* (IF ~11-13), *Consciousness & Cognition*, *Frontiers in Psychology: Consciousness Research*, *Philosophical Psychology*
- Research each journal's scope, word limits, and editorial stance on novel frameworks

## Files Modified This Session
- `paper/full/four-model-theory-full.md` — Byczynski & D'Angiulli citation added (Section 4.2)
- `paper/full/biorxiv/paper.tex` — same citation
- `paper/full/biorxiv/references.bib` — Byczynski2025 entry
- `paper/full/biorxiv/paper.bbl` — rebuilt
- `correspondence/outreach-emails.md` — D'Angiulli draft (#6)
- `sources/book-2015/` — ingested from ext8tb
- `.gitignore` — unignored correspondence/, private/, book PDF, reference papers

## Carried Forward from Session 160
1. **Marie Kaiser (Bielefeld ISoS) outreach** — prep file at `tmp/izw-bielefeld-outreach-prep.md`. Draft pitch email.
2. **Alnagger citation in .md** — `paper/full/four-model-theory-full.md` needs Alnagger citation to match .tex (Section 5.1).
3. **German manuscript image paths** — update `pop-sci/book-manuscript-de.md` for `-de` figures.
4. **tmp/ cleanup decisions** — build scripts, research analyses, implementation spec, AC design docs. See session 160 carryover for details.

## D'Angiulli Outreach
Email sent (from matthias@matthiasgruber.com to amedeodangiulli@cunet.carleton.ca).
Duplicate draft in Gmail Drafts — DELETE IT.
