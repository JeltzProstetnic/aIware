---
name: Book cover QA — visually verify subtitle vs artwork before declaring done
description: Before any book cover build is declared complete, visually verify subtitle text does not overlap the cover artwork. This defect has shipped twice (English + German editions) — real money wasted on author copies.
type: feedback
originSessionId: 8678362e-8dc4-4028-8126-f13713b2191c
---
Before declaring any book cover build complete — **open the final wrap PDF visually** and confirm the subtitle text does not overlap the cover artwork. Adequate margin between subtitle bounding box and any image element is mandatory.

**Why:** The subtitle/image overlap bug shipped on BOTH the English and the German editions of "The Simulation You Call 'I'" / "Die Simulation namens Ich". Same defect, twice, published live on KDP. The German author copy was ordered, paid for, shipped, and arrived defective — real money, real time, real frustration. The current build pipeline (`tmp/build_book_cover.py`, `tmp/build_book_cover_de.py`) declares success on PDF build completion alone, with no geometric or visual verification of text-vs-artwork composition.

**How to apply:**
- Every book cover build (English, German, future translations, future titles) must include a visual check of the rendered wrap at print size **before** committing, uploading, or declaring done.
- Never trust "build succeeded" as evidence that the cover is print-ready.
- If user says "the cover is done" — still verify, because the pipeline's history of this exact bug is worse than their trust signal.
- Fix the root cause in the build scripts (bounding-box check + mandatory visual step) — see AIW-60. Do not just flag and move on.
- Publishing a defective cover has a measurable cost (author-copy shipping + print fees + user time); treat cover QA as a gate, not a nicety.
