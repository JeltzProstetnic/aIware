# Pending: Dutch / Greek / Korean translations (AIW-123)

Action: reference
Tracked-by: AIW-123

**Provenance:** started in a remote Claude Code *web* session on 2026-07-23 while MG's
local console SSO token was locked out (IT later granted an SSO exception). The
Fable-heavy stages were run here because they had to happen while Fable/this
session was available; the remaining Opus + build + publish stages are handed off
to a normal, fleet-governed local session.

**Branch:** `claude/book-translations-nl-el-ko` (aiware-private) — full history retained there. Artifacts brought onto `main` (on disk) in S266 (2026-07-24) via selective checkout (manuscripts + control docs + interior reviews + pipeline scripts). `session-context.md` from the branch was intentionally NOT taken. Nothing left to merge.

**Book:** *The Simulation You Call "I"* (`pop-sci/book-manuscript.md`, EN base; DE = `-de.md`).

---

## Locked decisions (record in decisions.md)

- **Languages:** Dutch (`nl`), Greek (`el`), Korean (`ko`). Priority order nl → el → ko.
- **Engine:** translation by **Fable** (`claude-fable-5`), per MG. Native-editor interior
  review also Fable. Kalk scan + coherence remain **Opus**.
- **Distribution channel (KDP language limits):** KDP print supports only a short list
  (en, de, fr, it, es, pt, nl, ja, + Catalan/Galician/Basque). So:
  - **Dutch → KDP** (print + Kindle) — KDP-native, no new channel.
  - **Greek + Korean → NOT KDP** (unsupported in either format) → route via **PublishDrive**
    (same as the existing `zh` edition, see `drafts/publishdrive-zh-2026-07-13/`).
- **Fable-failure policy:** do NOT auto-fall-back to Opus; halt and ask MG. (No failures occurred.)

---

## DONE in this session (Fable-heavy core)

- [x] Regenerated shared EN+DE aligned source chunks (45) — `scripts/translation/chunker.py`
      → `tmp/translation-chunks/` (throwaway, regenerate with the script).
- [x] Authored per-language control docs (Fable), modeled on the `ja` templates:
      glossary + culture-guide for nl/el/ko. **Tracked copies:** `drafts/translation-nl-el-ko/control/`.
      (Downstream Kalk expects them at `tmp/<code>-pipeline/`; copy them back there first.)
- [x] Fable translation of all **135 chunks** (45 × 3), zero failures →
      `tmp/<code>-pipeline/fable-out/chunk-NNN.<code>.md` (throwaway; content is in the manuscripts).
- [x] Assembled manuscripts (tracked, the deliverable):
      `pop-sci/book-manuscript-nl.md`, `-el.md`, `-ko.md`.
- [x] 9-agent Fable interior review per language vs EN source →
      `drafts/aiw-{nl,el,ko}-interior-fable-review.md` (High/Med/Low findings, flag-only).

## REMAINING (do in the local session)

Follow the canonical SOP `docs/pending-spanish-translation.md` Phases 3–7, per language:

1. **Restore control docs to pipeline paths:** `cp drafts/translation-nl-el-ko/control/*
   tmp/<code>-pipeline/` for each of nl/el/ko (tmp/ is gitignored / not in this branch).
2. **Kalk scan (Opus, mandatory)** — calque/anglicism/germanism + typography sweep,
   A/B/C/D classified. Adapt `tmp/ja-pipeline/aiw108-kalk-ja.js` per language; **Greek and
   Korean need language-specific handling** beyond the EN/DE source-calque checklist
   (own script, own quote convention «…» for el, own false friends) — see
   `docs/aiw108-fable-opus-kalk-analysis.md`. Apply category-A via `tmp/kalk_apply.py`
   (match-once); hold B/D for MG. Output `drafts/aiw108-<code>-kalk-findings.md`.
3. **Coherence pass (Opus)** — whole-book read; fix `<code>-only` findings, log `structural`
   ones upstream. Adapt `aiw108-coherence-ja.js`.
4. **Reconcile the interior-review findings** in `drafts/aiw-<code>-interior-fable-review.md`
   (High before publish, Med should-fix).
5. **Localize figures** — 3 per language (`figures/*-<code>.{svg,png}`).
6. **Build (AFTER MG sign-off):** `.md → .tex → .toc → .pdf/.epub`. nl uses
   `tmp/build_translation_interior.py nl both` (Latin path) + `build_book_epub_lang.py`;
   el/ko are new script targets (el = Greek/babel or xelatex; ko = xelatex CJK-style font,
   cf. `build_translation_interior_cjk.py`). Covers + blurbs + ISBN per KDP/PublishDrive.
   Gate: `scripts/check_pdf_margins.py`. Never recompile canonical EN/DE PDFs.
7. **Publish:** nl → KDP; el + ko → PublishDrive.

## DO NOT
- Do NOT publish before MG's human native pass.
- Do NOT edit `.tex` directly (regenerate from `.md`).
- Do NOT parallel-write a single manuscript file.
- Do NOT trust `tmp/` across machines — it's gitignored; the keepers are in
  `drafts/translation-nl-el-ko/` and `scripts/translation/`.

## Pipeline reproducibility
- `scripts/translation/chunker.py` — regenerates the 45 EN+DE chunks.
- `scripts/translation/wf-fable.js` — the exact Workflow that produced the translations +
  interior reviews (glossaries → 135-chunk Fable translate → assemble → 9×3 Fable review).
