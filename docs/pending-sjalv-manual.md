<!-- Action: reference -->
<!-- Tracked-by: AIW-139 -->
# SJÄLV manual — handover

## S285 (2026-08-04) — the drawings arrived; artwork approach settled

**The external take is in**, as 10 pages at `C:\Users\Matthias\Pictures\SJÄLV\` (`01-title.png` …
`10-troubleshooting.png`; `09.png` is a clean uncompressed export of page 09; `old/` holds earlier
generations). **MG's verdict on the content: he likes the order, content, jokes, symbolism and
style.** The only complaint is raster quality.

**Settled, do not relitigate:**

1. **Do NOT redraw the pages from scratch.** A full hand-authored SVG rebuild of page 09 was
   attempted this session and MG rated it **"unusable"** — it does not reach the reference's
   quality, and redrawing discards the artwork that is already working. The prototype was deleted;
   rationale in `docs/decisions.md` (S285).
2. **The route is a standard vectorizer, or resize-and-sharpen.** MG owns this. Note there is no
   `potrace` / `inkscape` / `autotrace` / ImageMagick on WSL — only `cairosvg` and PIL.
3. **Page 07 (`07-leaks.png`) is the exception and still needs rework.** Its problem is
   compositional, not compression: the three panels are copy-pasted at three different scales,
   labels are duplicated ("waking" and "dreams / psycedelics" each appear twice, the second
   misspelled). No vectorizer fixes that.

**PRINT RESOLUTION — CLOSED by MG 2026-08-04.** The 1664×928 sources give ~222 DPI at 190 mm wide. MG ruled that sufficient: *"222dpi will be more than enough, it is a conference fun handout to be printed on the cheapest paper i can find."* **Do not re-raise this.** Print sourcing is now `AIW-144` (P1).

**Two content questions raised and not answered:**

- The brief's genre contract §2.1 specifies a **wordless** manual — "the hardest and best
  constraint". Every drafted page is heavily worded. MG has implicitly accepted this by liking the
  drafts, but it has not been called explicitly.
- Page 09's footer reads *"If your SJÄLV's eye glows, requests management access."* — grammar slip,
  or deliberate broken-manual English?

**CLOSED 2026-08-05 — MG declared SJÄLV final for print and waived the review.**
Recorded plainly for whoever reads this later: the 7-point review below was **not run**. It was
not run and found clean; it was set aside by the owner, who had looked at the artwork himself and
was satisfied. So red line #1 (does the parts page read as four snap-together modules?) and every
drawn number against Part 3 are **unverified, not verified**. The two numbers on the cover, 45 and
22000, do trace to Part 3. Nothing else was checked. The four gating questions below likewise stay
unanswered — the artwork settled them implicitly by existing. **Do not reopen this as a defect;
it was a decision.** If a number turns out wrong after the run, this file is where the exposure
was recorded before the money was spent.

Left in place for MG to delete when done with it: `C:\Users\Matthias\Pictures\SJÄLV\vector-test\`
(~1.4 MB, the rejected page-09 rebuild plus its comparison renders).

---

**State at end of S283 (2026-08-03).** The content brief is written and complete. MG sent it to
**Perplexity (Opus 5 via Perplexity Computer)** for a first take on the drawings. **That take has
now arrived — see the S285 section above.**

- **The brief:** `drafts/sjalv-manual-brief-for-perplexity.md` — self-contained, no drawings.
- **Backlog:** `AIW-139` (P1). MoC7 is the deadline: Oct 12–16, 2026.
- **Source spec:** crucible `docs/design/cru61-semi-emergent-connectome-program.md` §5b.
- **Verified numbers:** crucible `packages/crucible/src/crucible/spiking/closure_brain.py`.

---

## When Perplexity's take arrives — review it against these, in order

1. **Red line #1 first, before anything else.** Do the four model kinds read as four separable
   snap-together modules? A parts list structurally invites exactly the misread FMT has spent years
   correcting. Required: one continuous substrate sheet with graded, overlapping regions — not four
   separately bagged plastic parts. **If this fails, nothing else about the draft matters yet.**
2. **Every drawn number against Part 3 of the brief.** crucible verifies these. An invented
   specification is the one thing that makes the artifact worthless in the room it is carried into.
3. **The finished-product panel.** No glow, no spark, no eyes opening, no face. If it awakens, it is
   wrong.
4. **The call-for-help panel.** Assembly complete, every part fitted, figure still on the floor with
   the phone. That is P3 asserted-not-derived, drawn accurately.
5. **The demonstrator panel.** Neutral second figure. No parent-and-child scene until the
   developmental claim is sourced (AIW-138 open question).
6. **Claim discipline.** No panel may imply closure enables what feed-forward cannot; advantage
   scales with redeployed-model richness, not recursion depth; the word "Turing" appears nowhere.
7. **The flagged "could not draw" list.** This is the most scientifically useful part of the return.
   Each entry is a place the theory is still prose. Read it as a finding, not a defect report.

## Blocking on MG — these gate the drawing

1. **Parts-list identity.** FMT's four *kinds* (IWM/EWM/ISM/ESM) or the implementation's four
   *circuits* (CE/EWM/ISM/ESM)? *Recommendation on file: the kinds, with the criticality engine drawn
   as the power supply rather than a component — faithful to AIW-138's demotion of criticality from
   principle to signature.*
2. **Demonstrator panel** — neutral now, or source the developmental claim first?
3. **Permeability in an AC** — anything to draw, or does it stay in the sealed bag?
4. **Print scope** — folded booklet or single folded A3? Sets the panel budget.

## Then

- crucible verification pass on the technical claims and the parts numbers (CRU-62).
- Print decision and lead time, coordinated with the poster print (AIW-136/137).
- social gets the written long-form version once the panels settle.
