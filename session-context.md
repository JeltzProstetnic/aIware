# Session Context — aIware

## Session Info
- **Last Updated**: 2026-02-23T16:00Z (Session 105)
- **Working Directory**: /home/jeltz/aIware
- **Session Goal**: Fix citation linking, heading corruption, and table duplication in build scripts

## What Was Done This Session

### Citation Linking Fixes (both build scripts)
1. **Pipeline reorder**: `convert_citations()` now runs BEFORE `convert_body()`/`_convert_inline()` — prevents `&` from being escaped to `\&` before citation matching
2. **Unicode author names**: Regex character class expanded from `[a-zé\-]` to `[a-zà-öø-ÿ]` (covers ü, å, ö, ø, etc.)
3. **Lowercase particles**: Changed from matching ANY lowercase word (which falsely matched "see") to explicit particle list: `von|van|de|di|le|la|du|el|al`
4. **Hyphenated surnames**: `Melby-Lervåg` → `[A-Z][a-z]{2,}(?:-[A-Z][a-z]{2,})*`
5. **Surname minimum length**: Changed from `[A-Z][a-z]+` (matches `Mc` as complete surname) to `[A-Z][a-z]{2,}` — prevents McClelland/McDonald from being split at the Mc boundary
6. **Free-text citation prefixes**: `(for exceptions, see Author...)` — regex now uses `re.search` instead of `re.match`, finding author-year anywhere in the semicolon-split part
7. **Missing citation keys**: Added Dignath, Jaeggi, Chase, Bloom, Flavell to intel key dictionary
8. **pdflatex Unicode output**: Added `errors='replace'` to all `subprocess.run` calls

### Cross-Line Matching Bug (CRITICAL FIX)
- All `\s` in citation regex patterns replaced with `[^\S\n]` (`_S` variable) — prevents regexes from matching across line boundaries
- Without this: `Author's` on heading line + `(Year)` on next paragraph → entire paragraph swallowed into `\subsection{}`
- Affected headings 2.2, 2.3, 2.5 in intelligence paper and 2.1, 2.2, 2.8 in FMT paper

### Table Duplication Fix (FMT paper)
- Markdown pipe tables (`| header | header |`) now stripped from body (since LaTeX tables are injected as floats)
- Bold table captions (`**Table N. Title**`) also stripped

### Overfull Hbox Fix (intelligence paper)
- Added `\usepackage{microtype}` and `\emergencystretch=1em` to preamble

### Outstanding Issues — NEXT SESSION
1. **FMT bibtex sandbox issue**: bibtex can't write `.blg` due to `openout_any = p` restriction → all citations show as `??` in PDF. Need to either: (a) run bibtex outside sandbox, (b) pre-generate `.bbl`, or (c) switch to `\begin{thebibliography}` inline like the intel paper
2. **`(Hinton, McClelland, & Rumelhart, 1986)` splitting**: The minimum-3-char surname fix should help, but the FMT key dict may need `("Hinton", "1986"): "Hinton1986"` and similar entries verified
3. **`(see; \citealp{...})` formatting**: The "see" prefix in mixed parentheticals still appears as `(see;` — the non-citation prefix text handling could be cleaner
4. **FMT scoring matrix table**: User reports it seems missing — check if `FLOAT_TABLE_COMPARISON` injection is working correctly
5. **Overfull hbox in FMT paper**: FMT preamble may also need `microtype` + `emergencystretch`
6. **Test coverage**: Need tests for cross-line boundary prevention, McClelland-type names, and all specific FMT citation patterns

## Files Modified
- `tmp/build_intelligence_pdf.py` — citation regex overhaul, pipeline reorder, microtype
- `tmp/build_fmt_full_pdf.py` — same citation regex overhaul, pipeline reorder, table stripping
- `tmp/test_build_scripts.py` — 9 new tests (TestIntelCitationPatterns class)

## Recovery Instructions
1. Read this file
2. Tests: `python3 -m pytest tmp/test_build_scripts.py -v -m "not slow"` → 52/52 pass
3. Rebuild: `python3 tmp/build_intelligence_pdf.py` / `python3 tmp/build_fmt_full_pdf.py`
4. **FMT PDF will show `??` for all citations** — bibtex sandbox issue, needs resolution
5. Intel PDF should be correct now — verify citation links and headings
6. Comparison files in `tmp/{fmt,intel}-{ORIGINAL,GENERATED}.{tex,pdf}`
