<!-- session-context.md — updated by Claude, parsed by rotate-session.sh -->

**Last Updated:** 2026-03-28 18:30 CET
**Machine:** WSL
**Working Directory:** /home/jeltz/aIware
**Session Goal:** German book manuscript review & revision (book-manuscript-de.md)

## Completed Items

- [x] German book .docx conversion pipeline (build_book_docx.py)
- [x] Vorwort + Über den Autor complete rewrite — stripped ego, sachlich tone, CV-based, third person
- [x] Chapter 1 edits: heading rename, Chalmers para, IIT/GNW/PP tweaks, COGITATE rewrite
- [x] Chapter 2 edits: figure captions, five-layer stack, EWM/ESM descriptions, digital twin expansion
- [x] Chapter 3 edits: SDXL placeholder cut (EN+DE), "vier aus vier" → "konsistent", dash→parentheses
- [x] Chapter 4 edits: "wie es ist X zu sein" → "sich anfühlt als", Witz→Mehrwert, strikethroughs
- [x] Anglicism fix book-wide: "erfährt/erfahren" → "erlebt/erleben" (7 instances ch3+)
- [x] nSKI → nAGI (3 instances)
- [x] VMT → FMT throughout (consistent English abbreviation for both languages)
- [x] `--` → `–` throughout (54 occurrences)
- [x] Figures switched to German versions (3 SVG→PNG conversions + homunculi.de.png)
- [x] SDXL color figure → backlog AIW-40 (P4, future color edition)
- [x] Word inline editing knowledge → cfg-agent-fleet inbox (fleet knowledge file)
- [x] German book tone memory saved (no ego, no Spock)
- [x] Never-overwrite-user-files memory saved

## Key Decisions

- German book uses FMT (not VMT) as abbreviation — one shortcut across both languages
- SDXL figure placeholder removed from both EN and DE manuscripts (build script already filtered it)
- "Über den Autor" → "Der Autor" — short CV paragraph, third person, no hero's journey
- Green highlight = anglicism pattern to apply book-wide; yellow = rewrite; strikethrough = delete

## Next Session Task
task: true
file: docs/pending-german-book-review.md
backlog: AIW-24
description: Continue German book review at Chapter 5. Chapters 1-4 fully reviewed and corrected. Build fresh .docx for user to continue inline review.
