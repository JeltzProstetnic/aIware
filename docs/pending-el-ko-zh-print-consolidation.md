<!-- Action: reference -->
<!-- Tracked-by: simbook (routed 2026-08-04) -->
<!-- S284 2026-08-04 — ROUTED OUT OF aIware, NOT aIware work any more. Both build scripts named below
     (build_translation_interior_cjk.py, build_book_epub_lang.py) moved to ~/simbook/tmp/ in the
     2026-07-31 extraction (AIW-125 / CFG-478), a week after this file was written — so this had no
     owner for the intervening period. Filed as a P1 simbook inbox item 2026-08-04 (the ZH glyph
     defect is live on a published product). This copy is kept as the canonical write-up simbook is
     pointed at; aIware is not working it. The MG decisions below (PublishDrive, ISBNs, domestic
     Korea, hardcover) remain MG's and were surfaced to him in S284. -->
<!-- Source: aIware WSL S268 2026-07-24 (background research agent af6c04d2). -->
# el / ko / zh — consolidated print + ebook platform (research + recommendation)

**Question (MG S268):** publish Greek, Korean, Simplified-Chinese in print (POD) **and** ebook on as **few platforms as possible** — "I don't want to operate 5 platforms for 5 languages." (EN/DE/ES/FR/IT/PT/JA already on KDP; these three are not KDP-supported.)

## RECOMMENDATION — PublishDrive as the single platform

**PublishDrive is the only evaluated platform that does non-Latin PRINT (via Ingram) + non-Latin EBOOK + a best-effort mainland-China channel in one account.** Every alternative either bans non-Latin retail print (Lulu retail, D2D Print = Latin-only) or just re-sells the same Ingram POD (BookBaby, IngramSpark) while adding a platform — the opposite of the goal. It also already delivers the ebooks to Apple/Google/Kobo, so no separate direct accounts are needed. This dovetails with the existing `drafts/publishdrive-zh-2026-07-13/` ebook kit — same account, extend to el+ko ebook and all-three print.

### Setup on PublishDrive
- **Ebook** (all three): EPUB; free PublishDrive PUI identifier accepted (no ISBN needed). Delivers to Apple/Google/Kobo + China (Dangdang/JD/CNPeReading).
- **Print (Ingram POD)** (all three): **paperback only (NO hardcover)**; **$10/title/yr**; royalty **45% of list − manufacturing**.
- **China Print** (zh, optional): mainland POD, best-effort, ~6-month state review, royalty 50%.

### HARD build/logistics requirements (gate the print track)
1. **Fonts MUST be fully embedded in the interior PDF** — this is Ingram/Lightning-Source's real acceptance gate for Greek/Hangul/CJK, not the script itself. Our xelatex CJK/Greek builds must embed all fonts (verify with PyMuPDF `get_page_fonts`; poppler `pdffonts` is not installed on WSL). ← build-gate. The existing zh interior IS fully embedded (passes the gate) — but see the font-variant bug below.

### ZH font-variant BUG (S268 diagnosis — fix Wednesday, needs no Fable)
The shipped zh **print interior AND the live zh ebook** render Simplified Chinese in the **Japanese** Noto glyph variant (`NotoSerifCJKjp`), not Simplified (`sc`). Diagnosis:
- **Print** (`build_translation_interior_cjk.py` L59): script correctly asks `\setCJKmainfont{Noto Serif CJK SC}`, but xeCJK loads the **JP default face from the Noto CJK OpenType Collection**. Test-confirmed on WSL: both plain `{Noto Serif CJK SC}` AND `[Language=Chinese Simplified]{Noto Serif CJK SC}` still embed `NotoSerifCJKjp`. fontconfig *does* expose "Noto Serif CJK SC" (fc-match resolves it), so the fix is a fontspec **face-selection** issue — force the SC named-instance (e.g. `\setCJKmainfont[FontIndex=N]{...}` for the SC face in the .ttc, or install/point at a standalone `NotoSerifCJKsc-Regular.otf`). Verify the rebuilt PDF embeds `...CJKsc` via PyMuPDF.
- **Ebook** (`build_book_epub_lang.py` L87): the CJK CSS font stack is `"Hiragino Sans","Yu Gothic","Noto Sans CJK JP","Noto Sans CJK SC"` — **Japanese fonts first**, applied to BOTH ja and zh. Fix: make `css()` language-aware → for zh put **SC** fonts first (`"Noto Sans CJK SC","Source Han Sans SC","PingFang SC","Microsoft YaHei"`), and set `dc:language` to `zh-Hans` (currently `zh`).
- **MG wants the corrected zh EBOOK rebuilt so he can replace the published one** — do this Wednesday together with the zh print rebuild for PublishDrive/Ingram.
2. **Paperback only via Ingram** — the existing zh **hardcover** interior/cover can't ship through PublishDrive; hardcover for these three would need IngramSpark-direct (loses the China channel) or be dropped.
3. **Own ISBN required per PRINT title per language** — PublishDrive assigns NO print ISBN. → **MG action:** source ISBNs (Bowker ~$295/10, or an Austrian ISBN agency) — 3 paperback ISBNs (el/ko/zh) minimum; more if hardcover. Ebook needs none.

## The ONE unavoidable exception — Korean DOMESTIC retail
- Korea's market is ~80%+ **Kyobo / Yes24 / Aladin / Ridibooks**, and **no Western aggregator reaches any of them** (they contract only with Korea-registered entities + local tax ID + domestic distribution).
- Via PublishDrive, Korean readers are reachable only through **Apple Books KR + Google Play KR (ebook)** + **Ingram POD (diaspora/import)**.
- **If domestic Korea matters:** separate deal with a Korea-based distributor/co-publisher — NOT a platform you can add to the stack. If it doesn't, the Apple/Google-KR + Ingram-diaspora coverage is the pragmatic ceiling with zero extra platforms.

## Optional single add-on
- **IngramSpark direct** — only if you want **hardcover** for these three (PublishDrive-via-Ingram is paperback-only). It loses the China channel and otherwise duplicates reach, so add it *only* for hardcover.

## Verification caveats (confirm before committing)
- The "no aggregator reaches Korean domestic stores" is a high-confidence *negative* (absent from every channel list) but not a single explicit vendor statement — confirm with PublishDrive support.
- PublishDrive's full live store list + current ebook subscription tier pricing weren't enumerable externally — verify inside an account (`publishdrive.com/pricing.html`).
- Apple Books mainland-China confirmed dark since 2016; no 2026 reversal found (still treat mainland as diaspora-only + best-effort China channel).

## Sources (load-bearing)
- PublishDrive Ingram POD (languages, own-ISBN, $10/yr, 45%): help.publishdrive.com/distributing-to-ingram-with-publishdrive
- PublishDrive China Print / China special terms (best-effort, censorship, 6mo): help.publishdrive.com/distributing-to-china-print-with-publishdrive · help.publishdrive.com/distribution-in-china-special-terms
- PublishDrive ISBN policy: help.publishdrive.com/print-on-demand-requirements
- D2D Print Latin-only: draft2digital.com/blog/everything-you-need-to-know-about-d2d-print/
- Lulu global distribution Latin-only: help.lulu.com/en/support/solutions/articles/64000267552
- Ingram font-embedding gate: ingramspark.com/hubfs/downloads/file-creation-guide.pdf
- Korean market concentration (Kyobo/Yes24/Aladin/Ridi): publishersweekly.com international book news
