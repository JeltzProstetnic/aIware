# MoC7 freeze plan (S321, 2026-09-23)

Provenance: S321 plan drafted from the poster, gemstones, figure and robot audits, then revised against a read-only red-team review (dispositions in §8); no project file was edited to produce it.

## 1. Verdict

v15 contradicts several of the poster's claims, and each one is fixed by swapping text. The robot box does not fit in the free space unless the caption is cut to about four lines and paid for with a deletion. Freeze content on Fri Oct 2 and order the print by Mon Oct 5. A fabric print would need the Sep 30 freeze.

## 2. Must-fix defects before print

Each fix goes into three files in the same pass: `scripts/assets/moc7-poster/poster.html` (the build source), `drafts/moc7-poster-content.md` and `drafts/moc7-handout-a4.md`. Paths are relative to `/home/jeltz/aIware`.

**MF1. "Fails by construction" contradicts v15 lines 867–869 and the companion paper.**
- Where: `poster.html:228-232`, `content.md:124-127`, `handout:66-68`.
- Replace with: "The criterion is intrinsic and substrate-neutral: invariant under structure-preserving relabelling. An unfolded feed-forward chain matches the closed system's behaviour only with unbounded resources; under a resource bound the two come apart, and that efficiency gap is the empirical handle." ("Efficiency" is fine: the ban covers figure captions only.)

**MF2. The first corroborated row misstates its sources.**
- Where: `poster.html:258-265, 270`, `content.md:135-139`, `handout:74-79`.
- Header: "Corroborated — derived from the architecture in 2015; independent work consistent with it". Also tag Meisel 2013 in row 2 "(predates)".
- Row 1 sources: "Maschke 2024 (ketamine); Toker 2026; Algom & Shriki 2026; PCI, consistent, predates: Casali 2013, Casarotto 2016". These are the direct-arm sources v15 line 909 cites.
- Hengen & Shew 2025 (~140 datasets) moves to the honest box as the setpoint premise.

**MF3. "No competing theory generates it" is false by v15 §8.2.**
- Where: `poster.html:291`, `content.md:149`, `handout:88`.
- Replace with: "untested; coarse form also follows from REBUS — FMT adds sub-ego-dose dependence, lesion-side complexity, disconnection vs destruction"

**MF4. The Kawakita result is overstated.** Tsuchiya's group ran that study and will be at this conference.
- Where: `poster.html:307`, `content.md:153`, `handout:92`.
- Replace with: "group-level structural alignment shown (Kawakita 2025); individual-level arm and the paired decoding failure untested"

**MF5. The detector sentence implies results that do not exist.** crucible has no detector run, and the companion paper has 0 hits for "detector".
- Where: `poster.html:330-333`, `content.md:227-229`, `handout:130-132`.
- Replace with: "The criterion is being written up as a three-check detector (paper in preparation): self-attractor present; closure enters the world-model update; open-ended computation actually deployed. Toy-scale closure mechanism results: doi.org/10.5281/zenodo.21610993."
- This removes the only instance of "gates" on the poster (banned wording, MG 2026-08-21).
- The Q&A line at `content.md:243` changes to: "Offer to send the detector paper when it is out."
- **It frees no space**: the old text is 261 characters and the replacement is 258.

**MF6. The figures (SVG files only).**
- **2×2 (`fig-2x2-poster.svg:57-122`), must-fix under either D2 ruling:** the ESM self-ring never touches EWM, under a caption saying it enters the EWM's update rule. Draw ESM→EWM (one-way) or ESM↔EWM (mutual).
- **Bubble (`fig-bubble-poster.svg:111-121`): change only if D2 = mutual.** It already draws v15's one-way statement (lines 138, 272).
- Draw arrowheads as explicit polygons; cairosvg renders arc markers reversed.
- Raise all labels to at least 18 pt at print size (some are 10.6–15 pt now) and move the bubble's "sensory input" label off its path, which currently makes it read "sensbry".

**MF9. The ledger note calls criticality a "requirement".**
- Where: `poster.html:313`, `content.md:155`, `handout:94`.
- Replace with: "It concerns criticality — the neural signature of Principle 1 — which FMT holds in common with ConCrit, REBUS and the entropic-brain program."
- In the next sentence, "the requirement was motivated…" becomes "Principle 1 was motivated…".

**MF10. v15 says "Near-criticality".** `poster.html:171`, `content.md:168`, `handout:21`: "Criticality is what this looks like" → "Near-criticality is what this looks like".

**MF11. Formula line breaks.** Make "do(σ := c)" non-breaking (`&nbsp;`). The κ expression currently wraps over three lines in the proof; put it in its own `.eq` div and make it non-breaking too.

**MF12. The lede promises a measurement nobody has made.** v15 line 184 says closure has no established measurement protocol, and line 197 calls it the least accessible core claim.
- Change "a relation that can be clamped, swept and measured" → "a relation stated as an intervention, so it can be clamped and swept in any system one can intervene on".

**MF13. The "Open" header contradicts row 5 once MF4 is applied.** "Open — novel, untested" → "Open — novel; four untested, one partly tested" (v15 §8 intro).

**Should-fix (polish, cut if time runs short):**
- **MF7, split-brain.** Ledger `poster.html:283`, `content.md:143`, `handout:82`: "Pinto 2017 — FMT's reading of their data; observable not unique to FMT". Table `poster.html:191`, `content.md:199`, `handout:107`: "each hemisphere keeps a degraded but complete copy — halved in resolution, not in content".
- **MF8, "depth of closure" is not a v15 term.** Dreams row (`poster.html:190`, `content.md:198`, `handout:106`): "permeability; lucid onset = basic → simply extended consciousness" (the §3.5 terms). Animal row (`poster.html:193`, `content.md:201`, `handout:109`): "graded depth of recursive self-modelling".

**Needs a theory ruling from MG (§7):**
- **M2, κ notation (D2).** At minimum, add ", ω" to both Δ terms and use the same formula on the poster and the handout.
- **M4, P3 caveat (D3).** At `poster.html:177-178`, append: "— the theory's one bridging commitment, argued for rather than derived."
- **M6, subtitle (D1).** "with empirical confirmation" → "with converging empirical support".
- **M10, spoken answer** (`content.md:249`): "…but that construction needs unbounded activation precision — the same infinity, through a different door."
- **Formal-box provenance (D15).** v15 has 0 hits for "do(", "κ", "off-line" or relabelling invariance, so the QR code leads to a paper that contains none of Block 3.

**Check after the pass:** grep all three files for "gate", "gating" and "sampl".

**Housekeeping after the freeze:** clear the stale L6 records, especially `.claude/knowledge/prediction-framing.md` item 1, which caused the MF3 error. Also: `content.md:2` Tracked-by `AIW-136` → `AIW-137`; `content.md:8` A0-portrait question (answered, e4e0e0d8); `docs/pending-moc7-copenhagen.md` §7 "blocked".

## 3. What to do with the free space

**Budget (measured):** 56, 51 and 52 mm free per column (limit 1,163 mm). MF2, MF3, MF4, MF7, MF12 and M4 each add about a line; MF5 frees nothing; the old 68-word robot caption needed 110–140 mm. Every addition must be paid for with a deletion.

**Ranking:**

1. **Robot box.** Defensive: visitors will ask whether it is conscious. Short caption only (§5, about 4 lines), funded by deleting the honest box's last two sentences (161 characters, about 36 mm), which repeat the criticality falsifier bullet. Placement (D7): column 2 under the off-line sub-clause (on-topic; only MF1 adds a line there), or column 3 below the formalization paragraph.
2. **A#9, one line: self-inclusion falls out of wiring.** This is v15 §8.9's "Eighth result", so it contradicts nothing the QR code leads to. It ran on numpy, so do not call it "spiking". "Cost" is allowed, since the ban covers captions only. Optional, and only if the build has room.
3. **CRU-108, wired bottleneck: do not print (D5 = omit).** v15 §8.9, which the QR code resolves to, says no relayed implementation has run on the spiking substrate. 39.5× is a ceiling; the honest range is about 4–40×. Keep it as a spoken answer.
4. **AIW-230 closure figure: laptop, not print (D8).** It needs 130–160 mm, its CE/ISM labels are not FMT's model kinds, it shows an edge cut rather than the clamp, and it carries no result.

CRU-153 K3 and CRU-64 are for spoken answers only.

**Recommended change set:**
- MF1–MF6 and MF9–MF13.
- MF7 and MF8 if time allows.
- The short robot box, funded by the honest-box deletion.
- Optionally, one A#9 line.
- **If the build overflows:** trim A#9 first, then the robot caption. Leave the "ask" paragraph and the formalization paragraph alone; the formalization paragraph is the visible hook for the P1 work.

## 4. The handout

- Apply the same swaps (MF1–MF13 as adopted) at the handout lines cited above, with the same κ formula (D2) and the same subtitle (D1).
- Delete `handout:72` ("kept apart on purpose") and `handout:111` ("visibly doing the explanatory work"). Both break the prose-register rules, and neither is on the poster.
- Fix the page break (L4). "What the architecture accounts for" sits at 262 mm on page 2, and its table starts on page 3.
- If the robot box is printed, use the identical caption, or leave the robot out of the handout. Do not paraphrase it.
- Delete the stale `content.md:252` ("bring handouts of the abstract").
- The 2×2 figure on the handout is optional, and only after MF6.

## 5. The robot

**Poster caption (exact string, pending MG, D7):**
> By this poster's own criterion, the robot beside it is not conscious: hand-set rules on its own battery and motion sensors, no world-model for a self-model to enter — the baseline a closure architecture must beat.

The label words come from `robot_affect.py:38` `MOODS`, which includes "hungry", "scared", "nervous" and "crying". Before printing any mood words, check them against what the live cockpit shows most often. The caption above deliberately names none.

**Spoken line:**
> "It's a thermostat with good PR: it reads its own battery and balance, but there's no self-model in there — and that's why it's here. It's what my criterion says isn't enough."

Say "it", not "he".

**What visitors see:** a robot standing still, with no LEDs, screen or buzzer when untethered. The live content is the cockpit, behind a double login (so no QR code), shown on MG's laptop or phone with the sensed-values panel open (D13). "Pain" and "crying" invite a welfare question.

**Logistics owners:**

| Item | Owner | By |
|---|---|---|
| Full-day battery runtime (home WiFi); Wh from cell label (2S, likely ~20–26 Wh) | crucible | Sep 28 |
| Venue WiFi reply (mailed Sep 23); socket request + charger (D12) | MG | Sep 30 |
| Hotspot credentials on the Pi; `crucible-robot` fallback (`.local` unverified) | MG supplies, crucible installs | Oct 2 |
| Camera-relay keepalive (CRU-169); hotspot data ~0.6–0.8 GB/day | crucible, MG checks plan | Oct 2 |
| Vendor Flask on `0.0.0.0:5000`, no auth: bind localhost or firewall | crucible | Oct 2 |
| Cockpit regression run + real-row deploy probe | crucible | Oct 2 |
| Untethered hotspot dress rehearsal | MG + crucible | Oct 3–4 |
| Boredom drive | — | after Copenhagen |

## 6. Schedule, working back from travel on Sun Oct 11

MG also owes one Emergency Review (`AIW-262`) and the FMT P0 work this week, so D10 and D12–D14 are pre-decided (§7).

| Date | Step |
|---|---|
| Wed Sep 23 – Fri Sep 25 | MG rules on the open decisions (D1, D2, D3, D5, D7, D8, D9, D11, D15). If D11 = fabric, the Sep 30 freeze applies and everything below moves two days earlier. |
| by Mon Sep 28 | crucible: battery runtime and Wh (§5). |
| Tue Sep 29 – Thu Oct 1 | Joint trim pass with MG: text swaps in all three files, MF6 SVG work, robot box. Build: one A0 page, overflow gate clean; render and check from 5 m; handout PDF; MG read-through. |
| **Fri Oct 2** | **Content freeze.** |
| Sat–Sun Oct 3–4 | Robot hotspot dress rehearsal. |
| Mon Oct 5 | Order the print from a local Vorarlberg shop. Copenhagen on-site is fallback only; pick a shop anyway. |
| Thu Oct 8 | Pick up; test-scan the QR code on the print; tube with ≥90 cm inside length. |
| Fri Oct 9 | Pack. **The FMT deposit is mandatory if D5 = range/wait or D15 = fold**; otherwise optional (the concept DOI picks it up). |
| Sun Oct 11 | Travel, tube as carry-on (check the airline). |

## 7. Decisions for MG

- **D1:** Subtitle "confirmation" → "converging empirical support"? (yes/no)
- **D2:** Closure direction, which settles κ and the figures. **One-way:** soften the symmetric clause, κ with only the ω fix, ESM→EWM arrow in the 2×2, bubble untouched. **Mutual:** keep the clause, κ = min(κ_W, κ_S), two-headed arcs in both, mutual statement added to master §3.4 in the FMT P0 pass. (one-way/mutual)
- **D3:** Add the P3 bridging-commitment caveat? (yes/no)
- **D4:** Folded into D2. The figure arrows follow the closure-direction ruling; the 2×2 self-ring fix and the label sizes in MF6 go ahead either way.
- **D5:** CRU-108 on the poster? (omit/range/wait) I recommend omit. Range or wait makes the Oct 9 deposit mandatory.
- **D6:** One A#9 line in column 3? (yes/no)
- **D7:** Robot box with the short §5 caption, funded by deleting the honest box's last two sentences. Where does it go? (column 2/column 3/no)
- **D8:** AIW-230 figure in print, or on the laptop? (print/laptop) I recommend laptop.
- **D9:** Keep "The closure criterion needs someone to break it"? (keep/cut)
- **D10:** Cite the formalization roadmap DOI 10.5281/zenodo.21843693 in Block 6 and fix the dead AIW-261 OSF DOI in the same pass? Pre-decided: yes, unless MG objects.
- **D11:** Print type and location? (local paper/fabric/onsite) Fabric folds into hand luggage but needs the Sep 30 freeze.
- **D12:** Ask the organisers for a socket and bring the charger? Pre-decided: yes.
- **D13:** Default cockpit screen at the booth? Pre-decided: sensed values.
- **D14:** Spelling on the poster? Pre-decided: keep "modelling".
- **D15:** Formal-box provenance. **Tag:** add "formal statement: paper in preparation" under the box. **Fold:** put the intervention paragraph into master §3.4 during the FMT P0 pass, which makes the Oct 9 deposit mandatory. (tag/fold)

## 8. Red-team dispositions

Accepted as written: A1 (caption cut, funded deletion, D7), A2, A3 (verified `robot_affect.py:38`; the caption now names no moods), A4, A5, A6, A7, B1 (D2 and D4 merged), B2 (MF8 demoted with MF7), B3, C1 (MF12), C2 (D15), C3, C4 (MF13), C5, C6, red-team D2 to D5.

**Partly accepted: red-team D1 (schedule).** The Oct 2 freeze, Oct 5 order and the pre-decided items are adopted. One claim is rejected: the Sep 24 and Sep 29 dates are not MG's own reviewing load. Per `AIW-262`, he volunteered for one Emergency Review, not a reviewer and meta-reviewer share.

## 9. MG rulings — S321, 2026-09-23

MG, verbatim: *"your recs except D2: explain better"* and *"poster print i wil do locally in wolfurt, a few days before flight is enough buffer"*.

| # | Ruling | Why this was the recommendation |
|---|---|---|
| D1 | **Yes** — subtitle "…with converging empirical support" | "Confirmation" is the word v15's own §8.1 caveat makes hardest to defend. |
| D2 | **MUTUAL — and it was never a real question.** MG: *"where are the self models and the world models in a real brain? how would they be able to be one way? seriously?"* | ESM and EWM are activity patterns in one recurrent, reciprocally wired substrate; a one-way arrangement is not physically available. Poster: keep the symmetric clause, κ = min(κ_W, κ_S), ESM↔EWM arcs in both figures. |
| D3 | **Yes** — append "the theory's one bridging commitment, argued for rather than derived" | It is v15's own wording (line 138), so the poster matches the paper. |
| D4 | Follows D2 | — |
| D5 | **Omit** CRU-108 | v15 §8.9 says no relayed implementation has run on the spiking substrate; spoken answer only. |
| D6 | **Yes if it fits** — one A#9 line; first thing trimmed on overflow | It is in v15 §8.9 already. |
| D7 | **Placeholder in column 2**, funded by the honest-box deletion; caption waits on crucible's demo decision | MG: the demo is crucible's call. |
| D8 | **Laptop**, not print | Figure labels are not FMT's model kinds and it carries no result. |
| D9 | **Cut** "The closure criterion needs someone to break it" | Advertises good practice to scientists — the meta-science register MG banned in S282. Keep "please come and argue with me". |
| D10 | **Yes** — cite the formalization roadmap DOI; fix the dead OSF DOI in the same pass | Pre-decided. |
| D11 | **Local paper print in Wolfurt, a few days before the flight** | MG's call. Freeze stays Fri Oct 2; the print date is MG's. |
| D12–D14 | As pre-decided (socket + charger; sensed-values screen; "modelling") | — |
| D15 | **Tag** — "formal statement: in preparation" under the box | Folding it into the master forces an unreviewed formal addition plus a deposit under time pressure; the formalization roadmap does not contain it either (0 hits for `do(`). |

## 10. S327 (2026-09-30) — D7 resolved: robot tent card, off the poster

crucible ruled the MoC7 demo brain on 2026-09-30 (the Q-table brain: LIF pool, vision nucleus, learned value readout
over seven moves, probe reflex, ground memory, reverse fear, back bias), which made the §5 caption ("hand-set rules on
its own battery and motion sensors") inaccurate. MG chose a new caption, then the box was measured at 89.5 mm against
~36 mm of spare poster space (column 2: 0 mm, column 3: ~36 mm after the honest-box deletion). MG chose an A5 tent card
beside the robot over trimming the poster. The poster and the honest box are unchanged. Source
`scripts/assets/moc7-poster/robot-card.html`, built and gated by `scripts/build-moc7-poster.sh`, proof
`drafts/moc7-robot-card.pdf`. ⚠ If crucible changes the demo brain, the caption changes with it.
