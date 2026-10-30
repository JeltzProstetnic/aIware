# aIware Project Memory

> **Scope (set 2026-06-10, Session 215):** durable, slow-changing facts and lessons only.
> **Live status does NOT live here** — it goes stale and resurrects dead tasks (a "BBS commentary
> deadline Jun 12" survived here for weeks after the commentary was rejected May 29). Removed the
> status-mirror sections (Active TODOs, Waiting, Journal Targets, "translation in progress",
> per-paper status tables) this session. Canonical sources, always:
> - tasks / status / journal targets → `backlog.md`
> - session state & history → `session-context.md` + `docs/conversation-log.md`
> - rules → `CLAUDE.md`  ·  reference list → `references.md`  ·  git/push → `CLAUDE.md` (Git & Push)
> Do not mirror any of those here. Backup of the pre-cleanup file: `tmp/MEMORY.md.bak-2026-06-10`.
>
> **This file is a convenience mirror — every fact below has an official KB home (keep them in sync):**
> comms rule → `.claude/knowledge/neuroscience-communication.md` · build/PDF/review lessons → `.claude/knowledge/publication-build.md` · prose register / AI-tells → `.claude/knowledge/prose-register.md` ·
> KDP specs → `.claude/knowledge/kdp-specs.md` · theory/bubble/author/paths → `.claude/knowledge/project-reference.md` ·
> ORCID → `career.md` · photo → `user-profile.md` · math-style → `psych-profile.md` · Uncle Bruno → `family.md`.

## Neuroscience Communication Rule — MANDATORY
When writing to neuroscientists (emails, papers, any outreach):
- **NEVER enumerate fixed model counts** as if they are discrete brain modules. Saying "the brain runs four models" triggers immediate rejection — it sounds like naive modularism. Instead say "two kinds of models" or "model kinds/classes".
- **Frame FMT as a computational/systems-theoretic taxonomy**, not a circuit diagram. Neuroscientists know the brain doesn't have clean boxes.
- **Use "implicit/explicit" and "world/self" as dimensions**, not as four separate things. The "four" in FMT is a 2×2 matrix of *kinds*, not four discrete modules.
- **Show familiarity with their empirical methods** (fMRI, MEG, ECoG, etc.) — demonstrate we understand what brain data looks like.
- **Never sound like we're proposing architecture without grounding in neurobiology.** Always connect computational claims to known neural phenomena.
- Learned from Biyu He email (Session 100): "four models in parallel" → "two kinds of models in parallel"; "four distinct models" → "four distinct model kinds".

## Durable Lessons
- **Paper review copies:** compile submission-quality `.tex` PDFs — never weasyprint/pandoc renders when a `.tex` build exists. Highlight changed passages in yellow (`<mark>` tags in a `tmp/` copy of the `.md`, compiled separately).
- **Canonical PDF protection:** never recompile `paper/*/paper.pdf` or `paper/cosmology/sb-hc4a.pdf` for comparison/testing — compile into `tmp/` with clear names. They are multi-pass bibtex builds; recompiling without bibtex turns every citation into `???` in both "before" and "after" simultaneously (Session 106 disaster). Restore: `git checkout HEAD -- <path>`.
- **Paper build pipelines:** Full FMT — `paper/full/latex/paper.tex` (hand-maintained), copy `latex/` → `tmp/build-full/`, `pdflatex ×3` + `bibtex` (sandbox=true for bibtex; `.bbl` exists, bibtex only if refs change). When revising, update `.md` AND `.tex` (md = source of truth, tex = build source).
- **Parallel text-revision agents:** MAX 50–65 lines per agent (200–300 overflows context — Session 97 lost 6/7 agents); always Opus for German revision (weaker models → translationese).
- **Console output:** never paste >10 words for copy-paste (2-space indent corrupts it) — write to a `tmp/` file and open in an editor.
- **Feedback files (durable corrections, recalled on demand):** `memory/feedback_german_book_tone.md` (no ego, no Spock) · `memory/feedback_book_cover_qa.md` (subtitle/artwork overlap shipped twice — visual check mandatory before any cover is "done") · `memory/feedback_never_overwrite_user_files.md` · `memory/feedback_numbered_action_items.md` (number closing action/choice items so MG can cite them by number) · `memory/feedback_response_length.md` (**"the text wall has lost me"** — answer in the first sentence; long arguments go to a `drafts/` file, not the terminal).
- **Prose register (AI-tells) moved OUT of memory S291** → `.claude/knowledge/prose-register.md`, with a trigger row in CLAUDE.md. It failed three times (S270, S276, S291) as a memory file because memory is *recalled*, not *loaded*: nothing fired it while prose was being written. Do not re-create it here.

## Author / Project Facts (durable)
- **Project:** consciousness theory (FMT) → publications → artificial-consciousness implementation. 2015 German monograph; 2026 English pop-sci "The Simulation You Call 'I'" + German "Die Simulation namens Ich" (KDP).
- **ORCID:** 0009-0005-9697-1665. Author photo: `/mnt/c/Users/Matthias/Pictures/1749406479497.jpg` — all author-facing contexts.
- **Math style:** self-described "pure intuitionist" — architectural intuition, not formal notation; actively resists becoming a calculator; needs intuition→formalism translation without losing meaning.
- **Uncle Bruno J. Gruber:** theoretical physicist (QM, symmetries), **ALIVE** — never write death dates. Inspiration for the symmetry approach; acknowledged in cosmology paper + book.
- **German book source PDF (external):** `/mnt/c/Dropbox/DMS-Sync/Academic/book-consciousness-fmt/Die Emergenz des Bewusstseins 6x9 lit.pdf` (299pp; read via PyMuPDF/fitz — poppler not installed). [Path corrected S230 2026-06-18 — old `/mnt/c/Users/Matthias/Documents/_Eigene/…` is DEAD; mirror also at `/mnt/c/Dropbox/DMS-Sync/Academic/Die-Emergenz-des-Bewusstseins-6x9-lit.pdf`.] FMT-origin pages (2016-PDF numbering; CITE Lulu = +1, i.e. pp.60/62/261/264/282 — AIW-325): p.59 (Metamodell⊇Selbstmodell), p.61 ("Ich-Modell eingebettet" in Weltmodell = O_ESM⊆S_EWM, 2015), p.260 (self/world boundary via direct-vs-indirect feedback, glass example — NO efference/reafference vocab in this edition), p.263 (qualia/virtuelles Ich), p.281 (internal closure). **Canonical citing source + concept DOI: `.claude/knowledge/project-reference.md`.**
- **KDP specs:** US paperback ISBN 9798249169121, US hardcover 9798249172268; trim 6×9; spine = pages×0.002252"; paperback margins inner 0.875" / outer-top-bottom 0.75"; KDP minimums 300 DPI, 0.75pt lines. Build scripts live in **`~/simbook`** (extracted 2026-07-31, AIW-125) — the old `tmp/build_book_*.py` paths are dead. In aIware, durable build scripts are in tracked `scripts/`, never `tmp/` (AIW-145, MG-signed-off 2026-08-06).

## Gmail (durable gotcha)
Account `jeltz.prostetnic@gmail.com` only — there is **no Google login** for `matthias@matthiasgruber.com` (it's a send-as alias). Gmail-exclusive rule is in CLAUDE.md.

## Theory (ultra-brief orientation)
- **Consciousness** = ability to create a self-model, relate to it, interact with it.
- **Four model *kinds* (2×2):** Implicit/Explicit × World/Self — IWM→EWM, ISM→ESM. (Say "kinds," never "four modules" — see comms rule above.)
- **Qualia** = virtual "6th sense" of the simulation; exist only in the simulation, not the substrate → transforms the hard problem (PHENOMENAL-7, S342: never "dissolves"). Explicit content is phenomenal only in the closed self-model loop (S341); criticality is a signature, free modelling the requirement (S329).
- **Lineage:** MDM (Dennett) + SMT (Metzinger) + six-layer neural nets. **C4CA** = Class-4 cellular automaton shorthand for edge-of-chaos dynamics.
- German originals renamed to English in Session 10 (conversation log preserves originals).

## "The Bubble Diagram"
= `figures/figure2-real-virtual-split-simple.{svg,png}` (color, no "Key Insight" box). SVG 780×560 viewBox; PNG 2340×1680 (300 DPI). Not the BW version, not the architecture figure.

## AC Implementation
Migrated out of `~/aIware.implementation` (archived) → `~/mirror-box/` (Design 16, public) + `~/crucible/` (Design 15, private). Still research/publication phase; code is post-step-6. Designs: `docs/engineering/`.
