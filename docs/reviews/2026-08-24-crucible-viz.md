<!-- Action: present -->
# Crucible visualization survey → what could feed the MoC7 poster and the FMT figure set

**Surveyed 2026-08-24, read-only against `~/crucible`. Nothing was written, run, rebuilt or committed
in crucible. No figure was regenerated.** Poster sources read at
`~/aIware/scripts/assets/moc7-poster/`; proofs at `~/aIware/tmp/moc7-poster/` and
`tmp/build-moc7-poster/` inspected but **not rebuilt**.

---

## 0. The verdict in one sentence

**Crucible's visualization track produced exactly two things in the last six weeks, both in a
36-hour burst on 18–19 August, and the strongest poster candidate is the cheap one, not the
beautiful one: the closure ON/OFF connectome pair, where the manipulation the poster describes in
algebra (`do(σ := c)`) appears as a white rectangle you can read from five metres.**

---

## 1. Inventory — all visualization work in crucible, last six weeks

The track is two backlog items, `CRU-112` (matrix views) and `CRU-115` (3-D anatomy). Both are
**PAUSED by MG**. There is nothing newer: the most recent visual artefact anywhere in the tree is
dated 2026-08-19, and every commit since (2026-08-21, 08-23) belongs to `CRU-113`, the
discrimination task. The working tree has no uncommitted viz changes.

| # | artefact | what it shows | question it was built to answer | path | format |
|---|---|---|---|---|---|
| V1 | `cru112-brain-closure-{on,off}.png` | the four-circuit substrate, 1,100 cells, as a target×source weight matrix; ON = 38,305 synapses, OFF = 32,846 | "can a human read this network at all?" — MG's request for renderings that show connectivity, direction, sign and region simultaneously | `~/crucible/docs/results/figures/` | matplotlib PNG, 1170×1105 @ dpi 130, script tracked |
| V2 | `cru112-motor-routes-{on,off}.png` | the motor population and its two capacity-matched routes; 160 cells, 3,264 synapses, one pixel per synapse | shows the `CRU-113` structural claim: both relay banks reach motor, only the loop bank has a column back into content | same | same |
| V3 | `cru115-anatomy-{wiring-only,region-overlay}.png` | a 3-D force embedding of the same 1,100-cell substrate, grown from the wiring with the region labels withheld | "do FMT's four circuits fall out of connectivity, or are they painted on?" | same | **screenshot of a WebGL viewer**, 1400×900, UI chrome included |
| V4 | `cru115-glass-brain.png` · `cru115-brain-container.png` | the same cloud inside a translucent brain-shaped shell | MG: *"i want the brain displayed filling real brain volumes… a mostly transparent surface with some glare"* | same | screenshot, 2545×1281 and 1650×594, UI chrome included |
| V5 | `cru115-substrate-viewer.html` | the live interactive viewer — somas flash on spike, pulses travel the wire, orbit/zoom/scrub to 0.01×, two conditions (loop connected / loop cut) in one file | the intuition instrument MG asked for after rejecting the matrix view | same, 2.1 MB | **self-contained WebGL HTML**, opens directly in a browser |
| V6 | `crucible/viz/` package | `model` · `adapters` · `reduce` · `caption` · `matrix` · `layout3d` · `viewer3d` · `brainmesh` · `affinity` · `dichromacy` | the reusable toolset behind V1–V5 | `~/crucible/packages/crucible/src/crucible/viz/` | Python, ~90 tests green |

**Generating scripts, all tracked, all CPU:** `repro/cru112_first_renderings.py` (seconds),
`repro/cru115_3d_viewer.py` (layout ~27 s CPU; the *activity recording* wants the card for ~1 s),
`repro/cru115_blob_check.py`, `repro/cru115_functional_vs_anatomical.py`,
`repro/cru115_shell_preview.py`.

**Not visualization but adjacent:** `docs/model-explainer/` (`topology.png`, `training.png`,
`crucible-model-explainer.pdf`) is from 2026-07-08 and outside the window; it describes a
superseded substrate and should not be mined.

---

## 2. Judgement per artefact — what it would teach, and which pattern

Mapped against `~/aIware/.claude/knowledge/didactic-patterns.md` (aIware numbering, 1–38) and
`~/crucible/docs/didactic-patterns.md` (crucible numbering, cited as C-n).

### V1 — closure ON/OFF connectome pair · **STRONG**
Teaches **aIware #24, "Same-N = the matched pair biology never provides"** — better than anything in
the current figure set, because it *is* the matched pair, drawn. Two connectomes, same 1,100 cells,
same four circuits, differing only in whether the self circuit's efferents exist. In the OFF figure
the ESM **source column** goes white for its top three blocks while the ESM→ESM diagonal survives —
so **"closure OFF leaves two closed systems, {CE,EWM,ISM} and {ESM}, not zero"** is not a sentence
you have to be told, it is a shape. Secondary: **C-31, "closure OFF is a stroke, not an ablation"**,
and **C-29, "closure ⊂ bottleneck"**.
It also does something the poster badly needs: it makes `do(σ := c)` a *thing* rather than a
formalism.

### V2 — motor routes ON/OFF · **MODERATE, and premature**
Teaches the capacity-matched-bypass method (#24 again, methods flavour) and reads better at distance
than V1 because 160 cells means each synapse is a large crisp square rather than speckle. **But
`CRU-113` has banked no result yet** — B3's leak screen passed on 08-24, and everything downstream
is blocked on an MG ruling about B4 ordering. A poster figure showing a manipulation with no result
behind it reads as a promise, not a finding.

### V3/V4 — the wiring-grown 3-D anatomy · **HIGHEST IMPACT, HIGHEST COST, AND GATED**
Teaches the single most useful thing crucible has for FMT's central rhetorical problem: **the four
model kinds are not painted on.** The layout function takes a cell count and three edge arrays and
has nowhere in its signature to put a label; a cell's ten nearest neighbours nonetheless share its
circuit **88.0 %** of the time against a **27.3 %** chance level. That is the visual form of
**C-41, the span law** — self-inclusion derived with no self-label anywhere in the derivation — and
it directly answers the objection the poster's own Column 1 pre-empts in prose ("not four modules,
four boxes in a wiring diagram, or four anatomical regions"). Right now that paragraph asserts;
this figure would demonstrate.
It also serves **aIware #32** (the explicit models are not patchwork-modular) by showing four
*interpenetrating* clouds rather than four islands.

### V5 — the live viewer · **NOT A POSTER FIGURE, BUT POSSIBLY THE BEST BOOTH ASSET**
Self-contained HTML, opens offline, scrubs to 0.01×, morphs between arrangements. On a laptop at the
poster board this is a conversation magnet in a way no printed panel is. Zero build cost — the file
exists and works. Worth naming as an option even though it is out of scope for the print.

### V6 — the toolset · **INFRASTRUCTURE, NOT A CANDIDATE**
Relevant only because it means V1/V2 regenerate at arbitrary resolution from a tracked, tested,
CPU-only path.

---

## 3. Gap analysis — the most valuable part

### What the poster currently shows

One figure (`fig-2x2-poster.svg`, the 2×2 taxonomy; the bubble variant swaps in
`fig-bubble-poster.svg`), then **prose and tables the whole way down**: three principles, an
accounts-for table, the closure criterion with its `do(σ:=c)` box and κ, a falsification list, the
corroborated/open ledger, an honesty box, and a short "In progress" section.

### The hole

**Column 3's "In progress" section says the closure criterion "runs as a three-check detector on
synthetic systems" and points at a DOI — and shows nothing.** The poster's own lede promises *"a
relation that can be clamped, swept and measured"*, and then never exhibits the thing that was
clamped. An A0 poster with one diagram and 2,000 words of body copy is a paper pinned to a wall;
the reader who stops has nothing to look at while you talk.

### The single best candidate, and why

**V1, the closure ON/OFF pair.**

1. **It closes exactly the gap.** It is a picture of the artificial brain the criterion was run on,
   with the manipulation visible as an absence. The poster's most abstract claim becomes its most
   concrete panel.
2. **It survives every tripwire** (§4). It is structural — no dynamics, no energy, no capability
   claim — which is precisely the class of crucible result that is still standing after August's
   withdrawals.
3. **It is nearly free.** CPU, seconds, tracked script, deterministic seed. No card, no data on
   disk, no re-run of any experiment.
4. **It reads at distance.** The signal is block-level: four denser diagonal blocks, and one column
   band that vanishes. Individual synapses being speckle does not matter.
5. **Its number is on aIware's own safe-to-quote list** — "closure OFF … leaving 2 and 3 closed
   systems" is a structural graph claim, listed in `docs/crucible-status-2026-08-23.md` §4.

The runner-up, V3/V4, is the better *image* and the worse *bet* — see §4 and §5.

### A second gap, named because nobody has noticed it

**Crucible's own self-described "strongest didactic asset the project has produced" — the span law
(C-41) — has no visualization at all.** `docs/span-rule-draft.md` states three *numbers*
(195 → 2159 → 6048) and no figures; `grep` for any figure reference across all four span-rule
documents returns nothing. This is the result crucible has formally handed to aIware for standalone
publication (`docs/design/span-rule-standalone-publication.md`, MG: *"hand this over to aIware"*).
It is aIware's to draw, it is the one whose derivation contains no self-label, and it is currently
prose-only in both projects. **Not a poster item for 3 September** — it needs design work from
scratch — but it is the highest-value figure gap in the joint corpus and belongs in the backlog.

---

## 4. ⚠ HAZARD CHECK — every candidate against the three known tripwires

### (a) "Bottleneck arm" was a dense materialised matrix, off by 2,569× — dynamics/energy suspect, storage fine

| candidate | verdict |
|---|---|
| **V1** (brain closure ON/OFF) | ✅ **UNTOUCHED.** Built from `ClosureBrain`, renders the connectome as a structure. No arm, no dynamics, no energy. |
| **V2** (motor routes) | ✅ **UNTOUCHED, and doubly so.** It renders `wire_motor_routes` from `spiking/bypass.py` — the **wired** object built 2026-08-15 *after* the correction. Its module docstring explicitly separates itself from `experiments/instantiated_bottleneck.two_hop_extra`, which is the materialised one. And it is structural regardless. |
| **V3/V4/V5** | ✅ **UNTOUCHED** for structure. ⚠ V5 *plays back activity* — but the recorded activity is free-running background drive with no task and no arm comparison, so it makes no dynamical claim. It must never be captioned as showing a bottleneck's behaviour. |

### (b) The energy negative is WITHDRAWN in both directions

✅ **Nothing in the inventory visualises energy, cost or metabolism.** No candidate is exposed.
⛔ **Caption discipline:** no caption on any of these figures may say *cheaper*, *costs*, *efficient*
or *metabolic*. The one surviving clean energy number (the return costs ×1.03 at rest, ×1.01 under
load) is **not visualised anywhere**, and importing it as a caption on a structural figure would
attach a dynamical claim to a structural picture.

### (c) The renamed-region control was withdrawn — both arms built an identical connectome

**This is the one that needs care, because V3/V4 contain a check with the same shape.**

CRU-115 ships a test that *permutes every region label and asserts the positions come out
byte-identical*. Structurally that is the withdrawn control's error — a check that cannot fail.

**But the result does not rest on it.** The permutation test is a **construction check on the layout
function** (it proves label-blindness), not evidence. The *evidence* is the 88.0 % neighbour
agreement, and it has a control that **can** fail and **did move**: a degree- and weight-preserving
scramble, run through the identical embedder, falls to **0.277 against a 0.273 chance level**, with
modularity Q dropping 0.196 → 0.003.

⇒ **V3/V4 survive tripwire (c) — but only if the caption cites the scramble control.** Citing the
label-permutation test as though it were evidence would reproduce the withdrawn control's exact
error on an A0 poster. Write *"a degree-preserving scramble of the same wiring falls to chance"*,
never *"the labels were permuted and nothing changed."*

### ⚠ Two further hazards specific to V3/V4, and they are the reason it is ranked second

**(d) aIware's own status document files CRU-115 under "do not resurrect."**
`~/aIware/docs/crucible-status-2026-08-23.md` §5 — the section headed *"Withdrawn or corrected since
2026-08-12 — do not resurrect"* — carries: *"CRU-115 visualization [BANKED but PAUSED by MG] …
**Do not build on it.**"*
Crucible's own backlog says something compatible but differently weighted: the **result** is banked,
the **track** is paused (MG: *"this is really good now … now lets pause this visualization track"*),
and *"he has unstated feature wishes — wait for him to state them rather than guessing."*
**These are not in flat contradiction, but a standing "do not build on it" sitting in a withdrawn
section is not something a subagent should reinterpret.** Flagged for MG in §7; **no work on V3/V4
should start until he rules.**

**(e) The picture flatters the substrate, and crucible says so itself.**
Q = 0.196, where networks normally called modular sit at 0.3–0.7; within-circuit density is only
2–3× between-circuit density; *every* circuit pair is wired. Crucible's own words: *"a spring
embedder amplifies weak modularity into visually crisp territories; Q = 0.196 does not warrant
reading the four regions as strongly separated systems."*
⇒ On a poster, where the image is read at five metres and the caption at one, a crisp four-territory
picture **over-claims by default**. The caveat cannot be carried by 20 pt caption text alone.

**(f) One more, found in this survey and not previously recorded — a number that must not travel.**
The V1 pair's own synapse counts are **38,305 ON vs 32,846 OFF = 14.25 %**. The figure **14.03 %**
that aIware quotes belongs to a *different instance* — the 22,000-neuron / 15.4 M-synapse connectome.
⛔ **Do not print 14.03 % under a figure captioned 38,305 → 32,846.** Either quote 14.25 % as the
figure's own number, or quote neither and say *"about a seventh of the synapses."*

---

## 5. What each candidate would actually need

### V1 — closure ON/OFF pair
- **Data on disk?** Not needed. Regenerates deterministically from `ClosureBrain(sizes={CE:400,
  EWM:300, ISM:200, ESM:200}, seed=0)`.
- **Script tracked?** Yes — `repro/cru112_first_renderings.py`, plus the `viz` package, 41 tests green.
- **GPU?** **No.** Pure CPU, seconds.
- **Print spec, concretely** (read out of `viz/matrix.py`):
  - figure is `figsize=(9.0, 8.5)` inches, saved at `dpi=130` → 1170 px. At an A0 column width
    (~240 mm ≈ 9.4 in) that prints at **~124 DPI. Below the 300 DPI floor.**
  - **Fix: raise `savefig(dpi=…)` to ≥ 320, not the reduction target.** `downsample_sign_safe`
    *never enlarges* (1,100 cells → 900 px is the data ceiling), but `imshow` uses
    `interpolation="nearest"`, so a higher save-DPI draws each data cell as a larger crisp square —
    honest upsampling, because the source pixels *are* cells. `dpi=320` on a 9 in figure gives
    2,880 px ≈ 300 DPI at 240 mm.
  - **Line widths pass, barely.** Block boundaries are `linewidth=0.8` — above the 0.75 pt floor at
    1:1 placement, and scaling up only helps. No change needed, but do not scale the figure *down*.
  - **The caption block fails and must be re-set.** `fig.text(..., fontsize=7)` — 7 pt against a
    poster whose smallest existing type is 19–20 pt. **Move the caption out of the figure into the
    poster's `<figcaption>`,** or the honesty text (direction convention, counts, clipping) is
    invisible, which defeats its purpose.
  - Colour: red/blue diverging on near-white. Compatible with the poster's light palette.
- **⚠ Cross-project mechanics.** The repro script writes into `crucible/docs/results/figures/`.
  aIware must not write there. **Route: run the render with an aIware-side output path** (import
  crucible's `viz` read-only, write into `aIware/tmp/`), then commit the resulting asset into
  `scripts/assets/moc7-poster/` — or file an inbox item asking crucible to export a print-spec
  variant. Do not run the tracked script as-is.
- **Estimated effort: under an hour**, most of it poster layout rather than rendering.

### V2 — motor routes pair
Identical mechanics to V1, and cheaper still (160 cells = 160×160 data pixels, so it reads
beautifully at any size). **Blocked on content, not on tooling:** no banked `CRU-113` result yet.

### V3/V4 — the 3-D anatomy
- **Data on disk?** The layout regenerates on CPU in ~27 s, deterministic at seed 0. The *activity*
  recording wants the 4090 for ~1 s — **not needed for a still**.
- **Script tracked?** Yes — `repro/cru115_3d_viewer.py`, `viz/layout3d.py`, `viz/viewer3d.py`,
  `viz/brainmesh.py`, `viz/affinity.py`, all tested.
- **Format cost: this is the expensive one.**
  - The committed stills are **screenshots of the interactive page, with the control panel and the
    legend panel in frame.** Unusable as-is.
  - Largest is 2,545×1,281 → **215 mm at 300 DPI.** A third of an A0 column. Not a hero image.
  - A print version needs a **clean off-screen WebGL render at a large framebuffer with the panels
    hidden** — which means driving a browser. Crucible dropped its browser-automation scratch from
    the tree on 2026-08-19 (`c342090`), so that path is not sitting ready.
  - **There is no vector path.** Every wire is a screen-space ribbon; wire width is a slider in
    pixels (`1.3px`), so the **0.75 pt minimum line width is not controllable by any exposed
    parameter** and would have to be reasoned about per output size.
  - **Design collision:** the render is dark-on-black; the poster is `#16181d` ink on white with a
    `#2f6ba8` accent. A black panel on an A0 white poster is a deliberate design decision, not a
    drop-in.
- **Estimated effort: a day, plus an MG ruling first.**

### V5 — the live viewer as a booth asset
- **Needed: nothing.** The file exists, is self-contained, and opens offline in a browser.
- Worth a line on the poster (*"live viewer at the board"*) and a laptop.

---

## 6. ⇒ RANKED SHORTLIST

**1 — The closure ON/OFF connectome pair (V1). Do this one.**
It fills the poster's actual hole: the in-silico work is currently one paragraph and a DOI with no
picture. It converts `do(σ := c)` from algebra into a visible white rectangle. It is structural, so
it clears all three tripwires with room to spare. It regenerates on CPU in seconds from a tracked,
tested script — the only real work is raising save-DPI to ≥ 320, lifting the 7 pt caption out into
the poster's own caption slot, and routing the output to an aIware path. Under an hour.
*Caption it as the matched pair (#24) and the two-closed-systems result. Use 14.25 %, never 14.03 %.*

**2 — The wiring-grown 3-D anatomy (V3/V4). Ask MG first; do not start on your own judgement.**
Strongest image the project has, and the only visual answer to "aren't your four kinds just boxes
you drew?" — 88.0 % neighbour agreement from a layout that never saw a label, with a scramble
control at chance. But it is gated three ways: aIware's own status doc says *"do not build on it"*,
MG paused the track with unstated feature wishes, and the picture demonstrably flatters a substrate
whose modularity is Q = 0.196. Add a day of off-screen-render work and a light/dark design decision.
**High reward, but the gate is a person, not a task.**

**3 — The motor-routes pair (V2), only if the poster gains a methods panel.**
Cheapest of the three and the most legible at distance. It shows the capacity-matched bypass — both
banks reach motor, only the loop bank returns — which is a clean methods illustration. Hold it until
`CRU-113` banks something, or it advertises a manipulation with no finding attached.

**Not ranked but free: bring the live viewer (V5) on a laptop.** No build cost, and it does at the
board what no printed panel can.

---

## 7. Two things for MG, and neither is mine to settle

1. **The CRU-115 status conflict.** `~/aIware/docs/crucible-status-2026-08-23.md` §5 files the
   3-D anatomy under *"Withdrawn or corrected — do not resurrect"* with **"Do not build on it"**;
   `~/crucible/backlog.md` records the same work as **banked result, paused track**, with MG's own
   *"this is really good now"*. Reported, not reconciled. **Recommendation #2 above is blocked on
   this ruling.**
2. **The span law has no picture.** Crucible calls C-41 *"the strongest didactic asset the project
   has produced"*, it is the result MG handed to aIware for standalone publication, and there is no
   figure of it in either repository. Too big for 3 September; belongs in the backlog.
