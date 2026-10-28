<!-- Action: reference -->
<!-- Tracked-by: AIW-137 -->
# MoC7 poster — print + delivery (S327, 2026-09-30)

Poster FROZEN by MG 2026-09-30 ("poster is perfect now"). Bubble variant only. MG's order: printed in top quality,
one copy delivered to the MoC7 venue, one to his home in Bildstein. Nothing has been ordered or paid; MG places both.

## Files (kit: `tmp/moc7-print/`, rebuild from `drafts/moc7-poster-A0-proof-bubble.pdf`)
- `FMT-poster-A0-2mm-bleed-RGB.pdf` — 845 × 1193 mm (A0 + 2 mm white bleed each side). **Upload this one.**
- `FMT-poster-A0-2mm-bleed-CMYK.pdf` — same, converted with Ghostscript (DeviceCMYK, no FOGRA profile). Only if a
  printer insists on CMYK; rendered and checked, no visible shift.
- `FMT-poster-A0-RGB.pdf` — exact A0, no bleed.
- Checked: 1 page, fonts embedded (DejaVu subsets), figure 394 dpi and QR 534 dpi at print size. The poster has a white
  30 mm margin, so bleed carries nothing and trimming cannot cut content.

## Plan (two vendors; no cheap printer ships one order to both DK and AT)
1. **Venue copy → Jensen Print, Copenhagen** (https://www.jensenprint.dk/produkter/conference-poster-print-in-copenhagen/).
   180 g matte (no glare under corridor lights), 450 DKK ≈ €60 incl. VAT, delivery "+200 DKK" in Copenhagen (probably
   ex VAT). 24 h service; delivers to hotels and conference centres; tube included. **Gmail draft ready** (from
   matthias@, to info@jensenprint.dk, PDF attached, draft `r7104028067011972684`): asks delivery to HCØ on **Tue 13 Oct**
   with MG as recipient on site (+43 699 11358065), hotel Charlottehaven as fallback, total price, private invoice OK,
   order/pay deadline. Poster needed **Thu 15 Oct, board P56** (renumbered 2026-10-02). Weekend/Friday delivery to the university is risky
   (closed, needs a signature), which is why the draft asks for a weekday with MG present.
2. **Home copy → SAXOPRINT.at** (https://www.saxoprint.at/shop/poster?c=1-00N00f01E01m01w04403J0E3).
   230 g Fotodruckpapier glänzend (sharpest, keepsake) €29.02 Standard incl. shipping, or 200 g Bilderdruck matt to match
   the venue copy. Delivery address Bereuter 183, 6858 Bildstein. No deadline pressure: MG is home until Oct 11.
   ⚠ Unverified: whether SAXOPRINT ships A0 rolled; the colour setting reads "Euroskala" (CMYK), so upload the CMYK file
   if the upload check complains.

Estimated total ≈ €125.

## Fallbacks (researched S327, prices read from live configurators 2026-09-30)
- **flyeralarm** two orders (.dk + .at, 190 g matt photo): ≈ €51 + €41 standard if ordered by Thu 1 Oct 12:00; express
  ≈ €110 + €54. Needs bleed; converts RGB itself. Rolled shipping unverified.
- **Onlineprinters.dk**: 190 g photo, rolled delivery confirmed, but standard arrives 9–13 Oct; fastest ≈ €104. Wants
  CMYK FOGRA51, 2 mm bleed.
- **XEST Nimmerrichter** (Vienna): 180 g tearproof polypropylene, €84 ex VAT + UPS by quote — single vendor for both.
- Carry-on fallback: print the Bildstein copy early and fly it (tube ≥ 90 cm inside length).
- KU's own print shops (campusprint.ku.dk, named by the organisers) appear to serve KU units only — unverified.

## Status S327 (2026-09-30, MG: "order both, bildstein glossy, go")
- **Jensen Print: ORDER SENT** 16:3x from matthias@ (Gmail msg `1a0f2bab07734108`, PDF attached): 180 g matte, delivery
  **Mon 12 Oct to hotel Charlottehaven** (MG's choice), venue HCØ as fallback, private invoice to Bildstein. Old draft
  deleted. Waiting for their invoice + payment link → MG pays.
- **SAXOPRINT.at: NOT yet ordered.** Configured (230 g Fotodruckpapier glanz, Standard, €29.02) and file check passed in
  the agent's browser, but checkout needs an account and MG wants accounts created in his own Chrome with Google Password
  Manager. Cart does not transfer between browsers, so MG re-does it in his Chrome: `tmp/moc7-print/SAXOPRINT-STEPS.txt`.
  Expected check warnings: Farbraum (RGB→CMYK by them) and Randanschnitt (white edge; harmless, 30 mm white margin).
- cfg todo filed: agent-created accounts with generated, vault-stored passwords.
- **Jensen invoice received** 2026-09-30 16:35 (no. 14962, Gmail `1a0f2befa3231111`): **650 DKK incl. 25 % VAT** (520 net),
  A0 84×119 cm, 180 g matte, tube included, delivery address Charlottehaven (guest from Sun 11 Oct). Payable upfront by
  card via the onpay.io link in the mail; **not printed until paid**. SAXOPRINT: no order mail yet as of 16:4x.
- **Jensen invoice 14962 PAID by MG 2026-09-30** (650 DKK, card via OnPay). Delivery Mon 12 Oct to Charlottehaven.
  Legitimacy checked before payment: DKIM/SPF/DMARC pass for e-conomic.com (Danish invoicing SaaS), reply-to
  info@jensenprint.dk, CVR 55861455 = Jensen Print (Lars Henning Jensen), address/phone match their site, and their order
  page announces the card-payment link. Remaining: SAXOPRINT home copy (MG's Chrome); collect the tube at the hotel Mon 12.
- **SAXOPRINT home copy ORDERED + PAID by MG 2026-09-30** in his own Chrome (230 g Fotodruckpapier glanz, Standard, ~€29,
  expected ~7 Oct to Bereuter 183, Bildstein); status "in Bearbeitung". Account login in vault as `saxoprint_at`.
  ⇒ Both copies ordered. Nothing left but delivery: Jensen tube at the hotel Mon 12 Oct (calendar event set).

## S331 2026-10-07 — SECOND Jensen order: corrected poster (MG: "order the corrected poster")
- Sent from matthias@ to info@jensenprint.dk, Gmail `1a116353289b80e2`. File: `tmp/moc7-print/FMT-poster-A0-2mm-bleed-RGB-corrected.pdf` (845 × 1193 mm, from `drafts/moc7-poster-A0-proof-bubble.pdf` after the free-modelling correction).
- Same spec (A0, 180 g matte, tube). Additional to invoice 14962, which still delivers Fri 9 Oct.
- Asked: hotel delivery Mon 12 / Tue 13, latest Wed 14; fallback HCØ by Thu 15 08:00. Expected cost ~650 DKK (first order's price).
- ~~OPEN: Jensen's invoice + payment link~~ → **Invoice 14986** received 2026-10-07 13:03 (Gmail `1a11676b66956bf8`, "order 2"). **PAID by MG**: Jensen confirmed 2026-10-08 08:48 (Gmail `1a11a4698d7a553d`, "Thanks for payment. We deliver the poster"). They did not restate the date; delivery goes to the address and day requested in `1a116353289b80e2` (hotel Mon 12 / Tue 13, latest Wed 14).
- If the corrected print arrives, hang it at P56; the pen corrections on the first print are then only a fallback.

## S333 2026-10-08 — printed criticality line
- MG (via social, 2026-10-07): *"poster will be fixed at moc7"*. The printed line "criticality is necessary, not sufficient" and the criticality falsifier on the first print get corrected by hand on site. This replaces the earlier note that the printed poster "cannot change". If the corrected Jensen print (invoice 14986) arrives, it already carries the ruling and the hand fix is only for the first print.

## S333 2026-10-08 — FMT v18 reading copies (MRS Digitaldruck, Wolfurt)
- Sent 18:58 to t.pawlica@mrs.to (Gmail `1a11c73c67fe91ec`): FMT v18 (Zenodo `…23217056`, md5-identical source) scaled to A4, 161 pp, **3 copies**, b/w duplex, cheapest/fastest binding (spiral). Pickup + cash Friday 9 Oct with the Quartett. File: `tmp/wolfurt-print/FMT-v18-Gruber-A4.pdf`. **OPEN:** MRS price/confirmation.
