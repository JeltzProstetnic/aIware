# AIW-109 — PRINT re-upload manifest (S264, 2026-07-15)

What changed this session and must be re-uploaded to KDP (**manual, MG**). All files live in
`pop-sci/`. **EN is unchanged — do NOT re-upload EN.** EU/IngramSpark editions stay PARKED.

## Why these changed (all build-template fixes, text was already final)
- **All 7 translation interiors**: TOC heading localized (was English "Contents" → Índice / Table
  des matières / Indice / Sumário / 目次 / 目录) + figure caption label localized (Figura / Abbildung /
  図 / 图; FR keeps "Figure"). ES/FR/IT/PT also lost a duplicated dedication page. DE lost the phantom
  subtitle page. → interior page counts moved for DE/ES/FR/IT/PT (see table), so their **covers** were
  rebuilt too (spine width). JA/ZH page counts unchanged → JA/ZH **covers unchanged, do not re-upload**.

## Print interiors — re-upload 14 files (paperback + hardcover)

| Book | pages (was) | Paperback interior | Hardcover interior | Cover re-upload? |
|------|-------------|--------------------|--------------------|------------------|
| DE | 297 (299) | `book-manuscript-de.pdf` | `book-manuscript-de-hc.pdf` | YES (both) |
| ES | 288 (290) | `book-manuscript-es.pdf` | `book-manuscript-es-hc.pdf` | YES (both) |
| FR | 297 (299) | `book-manuscript-fr.pdf` | `book-manuscript-fr-hc.pdf` | YES (both) |
| IT | 286 (288) | `book-manuscript-it.pdf` | `book-manuscript-it-hc.pdf` | YES (both) |
| PT | 286 (288) | `book-manuscript-pt.pdf` | `book-manuscript-pt-hc.pdf` | YES (both) |
| JA | 282 (282) | `book-manuscript-ja.pdf` | `book-manuscript-ja-hc.pdf` | NO (spine same) |
| ZH | 218 (218) | `book-manuscript-zh.pdf` | `book-manuscript-zh-hc.pdf` | NO (spine same) |
| EN | 271 (271) | — unchanged, skip — | — unchanged, skip — | NO |

## Covers — re-upload 10 files (only DE/ES/FR/IT/PT, spine width changed)

| Book | Paperback cover | Hardcover cover |
|------|-----------------|-----------------|
| DE | `cover-wrap-de.pdf` | `cover-wrap-hc-de.pdf` |
| ES | `cover-wrap-es.pdf` | `cover-wrap-es-hc.pdf` |
| FR | `cover-wrap-fr.pdf` | `cover-wrap-fr-hc.pdf` |
| IT | `cover-wrap-it.pdf` | `cover-wrap-it-hc.pdf` |
| PT | `cover-wrap-pt.pdf` | `cover-wrap-pt-hc.pdf` |

All 5 rebuilt covers PASSED the AIW-60 visual QA gate (no subtitle/artwork overlap, spine text fits,
back blurb readable). DE cover carries its own barcode (ISBN 9798257520600 PB / 9798257524424 HC);
translation covers keep the white KDP-free-ISBN barcode placeholder.

## eBooks
- **DE.epub only** was rebuilt (subtitle corrected to "Die Architektur von Bewusstsein, Berechnung und
  Kosmos"; the old "Bewusstsein und Kosmos – Eine unerwartete Verwandtschaft" heading is gone). Refreshed
  in `drafts/aiw109-ed2-reupload-2026-07-14/DE.epub`.
- EN/ES/FR/IT/PT/JA eBooks are **unaffected** by the print fixes (the Contents/dedication/figure-label
  issues were LaTeX-print-only; eBooks use pandoc nav + label-free captions — verified clean). Re-upload
  them only if you want uniform re-review; not required.
- ZH eBook (PublishDrive kit `drafts/publishdrive-zh-2026-07-13/`) unchanged — subtitle was already canonical.

## Still open (MG-owned, NOT done by this session)
- Human-native reviewer gate per language — the Fable review is the automated backstop, not a substitute.
