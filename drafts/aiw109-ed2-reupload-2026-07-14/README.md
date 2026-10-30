# AIW-109 — Second-edition eBook re-upload kit (2026-07-14, S263)

Corrected **Second edition** eBooks. All manuscripts are text-final (S262 judgment
round + MG decisions); this session added the build-level typography pass and rebuilt
every artifact fresh. **Upload is manual (MG).**

> **S264 UPDATE (2026-07-15):** the last Fable review ran (5 agents, source + print interiors).
> Verdict: text clean in all 8 editions; only build-template defects, all fixed. **`DE.epub` was
> re-exported this session** — its visible subtitle now reads the canonical "Die Architektur von
> Bewusstsein, Berechnung und Kosmos" (the old "Bewusstsein und Kosmos – Eine unerwartete
> Verwandtschaft" heading is gone). The other 6 eBooks here are unchanged (the print-only fixes
> don't touch them — verified). Print interiors + covers changed too: see
> `drafts/aiw109-print-reupload-S264.md`.

⚠ **Human-native reviewer gate still open per language** (see §Caveat) — the Fable review is the
automated backstop, not a substitute.

## KDP eBooks — upload these 7 (this folder)

| File | KDP title | Language |
|------|-----------|----------|
| `EN.epub` | The Simulation You Call "I" | English |
| `DE.epub` | Die Simulation namens Ich | German |
| `ES.epub` | La simulación que llamas «yo» | Spanish |
| `FR.epub` | La simulation que vous appelez « Je » | French |
| `IT.epub` | La simulazione che chiami «Io» | Italian |
| `PT.epub` | A simulação que você chama de "eu" | Portuguese |
| `JA.epub` | 「私」という名のシミュレーション | Japanese |

**Steps (per book, on KDP Bookshelf):**
1. Open the existing Kindle title → **Edit eBook Content**.
2. Upload the matching `*.epub` from this folder (replaces the manuscript).
3. Cover unchanged — do **not** re-upload the cover.
4. Save → Publish. (KDP re-review is usually a few hours.)

> The eBook copyright page keeps just `© 2026` (no edition line) — nothing to change there.
> The canonical files also live in `pop-sci/book-manuscript-<lang>.epub` (same bytes).

## Simplified Chinese — separate route (NOT KDP)

ZH ships via **PublishDrive** (KDP has no Simplified-Chinese store). Refreshed kit:
`drafts/publishdrive-zh-2026-07-13/` (epub + docx now updated to final text). Follow that
folder's own `README.md`.

## What changed vs the first edition

- **Text:** S260 High/Med fixes → S261 low-risk mechanical pass → S262 Fable judgment
  round + MG rulings (ES «Capítulo N», ZH 进化→演化, JA proprioception/qualia/我々→私たち,
  PT hedge + garra→domínio, FR kept 70yr, IT unchanged). comgarra corruption fixed.
- **Build-level typography (this session, S263):**
  - **FR EPUB** — narrow no-break space (U+202F) inside « » and before ; ! ?, full NBSP
    before : (parity with babel-french print). Apostrophes already curled by pandoc `smart`.
  - **JA + ZH** — stress emphasis now renders **bold** (was slanted/lost CJK italic);
    Latin titles (*Nature*, *C. elegans* …) correctly kept italic.
- **Print interiors** — edition marker flipped **First → Second** on the copyright page
  (all 8 languages, all trim variants). eBooks unchanged there.

## Caveat (unchanged from S259)

Translations are AI-produced (Fable/Opus). A **human-native review per language** is still
recommended before treating any translation as final for a paying audience. The pending
Fable review round (source + print-interior sampling) is the automated backstop, not a
substitute for a native human pass.
