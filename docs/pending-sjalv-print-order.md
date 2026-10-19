<!-- Action: reference -->
<!-- Tracked-by: AIW-144 -->
# SJÄLV print order — PLACED 2026-08-05 at WirmachenDRUCK

> **STATUS 2026-08-05 (S285 late): ORDERED, FONT FIX RE-UPLOADED, AWAITING DELIVERY.** MG confirmed the
> corrected print file (`SJALV-12831205-1-print-A5-bleed-FONTS-FIXED.pdf`) was re-uploaded to Auftrag
> 12831205-1 — *"already all done, awaiting delivery in a few days."* The unembedded-font hold is
> cleared and nothing is open but the courier. **Delete this file when the booklets arrive and
> `AIW-144` closes.**
>
> **Earlier status (S286 numbering, superseded): ORDERED.** MG placed the order at WirmachenDRUCK, product 846, a day
> ahead of the intended date. The `ccw` rotation is committed. Everything below is the historical
> decision record — do not re-present it at session start. Delete this file when the booklets arrive
> and `AIW-144` closes.

**Historical — the state as of 2026-08-05 morning.** MG said on 2026-08-05: *"track the print for tomorrow."*
**The artwork is FINAL — MG froze it the same evening. Nothing about the slides is open; only
the order itself is.**
Deadline pressure is real but not acute — MoC7 is Oct 12–16 and online printers run about
5–10 working days, so the true drop-dead is late September. Ordering now is MG being ahead.

## What to send the printer

`ccw-sjalv-printshop-A5-bleed.pdf` — 12 single A5-landscape pages, trim 210×148 mm inside a
216×154 mm media box (3 mm bleed), reading order. Mirrored to
`C:\Users\Matthias\Pictures\SJÄLV\print\` and rebuildable from `drafts/sjalv-print/`.

**Never send the A4 duplex file** — that is the home-printer imposition; the shop does its own.

## The recommendation on the table

**1000 copies, 90 g Offset/Naturpapier weiß (uncoated), WirmachenDRUCK product 846
— €183.10 net**, roughly €220 with 20 % Austrian VAT, plus shipping.

Reasoning, with the live quote table in `backlog.md` under `AIW-144`:

- Uncoated is simultaneously the cheap option and the correct IKEA look — about **2 cents
  a copy** more than the cheapest stock in the shop.
- **Recycled paper is the most expensive of the four**, not the cheapest. Counter-intuitive,
  verified: €209.75 at 500 against €133.97 for the uncoated offset.
- Volume is where the money is: €0.44/unit at 250, €0.27 at 500, **€0.18 at 1000**.
- MoC7 absorbs perhaps 100–140 at 150–200 attendees; MG wants the rest for elsewhere.

## Open before ordering

1. **Second and third quote.** Only WirmachenDRUCK has been priced. `onlineprinters.at` and
   `druckdiscount24` both need full browser interaction (JS configurator, no plain form controls).
   ~~`druckdiscount24` lists a **60 g Naturoffset**~~ — **WRONG, killed 2026-08-05 (S286).** MG
   could not find it; verified against the product's real option list: the uncoated stocks for a
   12-page A5-quer saddle-stitch are **90 / 120 / 150 g/m² Offset/Naturpapier weiß only**. 90 g is
   the floor, i.e. the stock already recommended. The "Naturoffset ab 60 g" line is category-page
   marketing copy spanning the whole brochure range and does not survive into this configuration.
   druckdiscount24 is still worth a quote (independent shop — Häuser Druck GmbH / WKS Druckholding),
   just not for lighter paper.
2. **Shipping to Austria and lead time** — unpriced at every shop.
3. **Cover rotation** — `ccw` is what is built and what MG has been printing. Confirm before
   committing 1000 copies; it is not reversible after the run.
4. ~~7-point red-line review~~ — **WAIVED by MG 2026-08-05, artwork frozen.** Do not reopen it
   as a blocker. The exposure it leaves is recorded in `docs/pending-sjalv-manual.md`.
5. **The QR points at the Zenodo concept DOI**, which always resolves to the newest version —
   v13 today, still five principles. If v14 has not landed by Oct 12, repoint it at the v13
   version DOI before printing (`AIW-138`).

## Build

`~/aIware/.claude/knowledge/sjalv-booklet-build.md` — how to regenerate everything, the
imposition rule, and why a software fold check cannot validate it.
