<!-- session-context.md — updated by Claude, parsed by rotate-session.sh -->

**Last Updated:** 2026-04-14 15:10 CET
**Machine:** WSL
**Working Directory:** /home/jeltz/aIware
**Session Goal:** German book review complete + full KDP publication asset build (ebook, paperback, hardcover)

## Completed Items

- [x] Startup checklist (run late after user correction — lrn audit filed)
- [x] German book review Kap 11–16 + Anhang B/E: ~30 user-flagged issues fixed (sentence fragments, calques, word order, reflexive verbs, meta-commentary removal, Bernhard reference dropped, Real/Virtual→Virtuell)
- [x] Sub-agent anglicism sweep Kap 1–10 applied: 82 en-dash spacing fixes, Level→Ebene drift, re-glossed technical terms removed, Zusatzfeature→Zusatzfunktion
- [x] v10 docx built, scanned for inline marks (none — user flagged issues in chat instead)
- [x] Book interior rebuilt: `book-manuscript-de.pdf` (269 pages, 6×9 paperback)
- [x] Hardcover interior built: `book-manuscript-de-hc.pdf`
- [x] German-specific cover build script written: `tmp/build_book_cover_de.py` (derived from English, German title/subtitle/blurb/Kindle alt-text)
- [x] German EPUB build script written: `tmp/build_book_epub_de.py` (German metadata, de language, German figure map, YAML metadata block parsing disabled to avoid mid-doc `---` collision)
- [x] Paperback wrap built: `cover-wrap-de.pdf` (spine 0.606")
- [x] Hardcover wrap built: `cover-wrap-hc-de.pdf` (case laminate 14.370×10.417)
- [x] Paperback front built: `cover-front-de.pdf`
- [x] Kindle front cover built: `cover-kindle-de.jpg` (1600×2560, EXIF alt text)
- [x] Kindle EPUB built: `book-manuscript-de.epub` (3.0 MB, 4 German figures embedded)
- [x] aIware CLAUDE.md fixed: `scripts/push.sh` reference → `~/cfg-agent-fleet/setup/scripts/filtered-push.sh` (retired script was still documented)
- [x] lrn findings filed to cfg-agent-fleet inbox (4 items): PreToolUse startup gate hook, rule against unilateral tracking-file reconciliation, SessionStart hook conversation-log session-gap warning, infrastructure-retirement doc-coherence check
- [x] Backlog entry AIW-50 added for tomorrow's KDP upload

## Key Decisions

- **German book ready for publication.** All three editions (ebook, paperback, hardcover) have build artifacts committed. Upload scheduled tomorrow pending German ISBN decision.
- **German ISBN decision PENDING** — wraps built with `[TBD-DE-PB]`/`[TBD-DE-HC]` placeholders, no barcode. User needs to decide KDP-free vs bought ISBNs before upload. Build scripts ready to regenerate with real values.
- **Back cover blurb approved:** "Das Ich ist eine Simulation…" (in `tmp/build_book_cover_de.py` BACK_COVER_BLURB, also Kindle EXIF alt text and metadata description).
- **Figure 3 (phenomenological content) is NOT in German EPUB** — only SVG exists for German, no rendered PNG. Either render before KDP upload or accept the gap (one figure of four).
- **Data integrity cascade lesson:** Session 183 wrote three contradictory review-position self-reports (commit msg / pending file / session-context). Session 185 initially trusted the wrong line and corrupted the pending file further. Fixed after user correction. Filing: global rule proposed against unilateral tracking-file reconciliation (cfg inbox).
- **Push script discovery lesson:** aIware CLAUDE.md pointed to retired `scripts/push.sh`. Fixed locally + filed process-rule proposal to cfg inbox (infrastructure retirements should scan all project CLAUDE.md files for stale references in the same commit).

## Carry-Over Items

- `docs/pending-german-kdp-publication.md` (present) — **active task for next session**
- `docs/pending-mcfarnell-reply.md` (present) — Gmail draft exists, not touched this session
- `docs/pending-jcs-submission-prep.md` (triage) — AIW-46, fire-and-forget
- `docs/pending-word-editing-protocol.md` (reference) — no action

## Next Session Task

task: true
file: docs/pending-german-kdp-publication.md
backlog: AIW-50
description: German KDP publication. All assets built in Session 185 (ebook/paperback/hardcover). BEFORE upload: decide German ISBNs (KDP-free vs bought), update `tmp/build_book_cover_de.py` EDITIONS dict, rerun `python3 tmp/build_book_cover_de.py --edition all --wrap` to regenerate wraps with barcodes. Optionally render `figures/figure3-phenomenological-content-bw-de.svg` → PNG and rebuild EPUB. Upload order: Kindle first, then paperback, then hardcover. Metadata and back cover blurb are in the build script. Full checklist in `docs/pending-german-kdp-publication.md`.
