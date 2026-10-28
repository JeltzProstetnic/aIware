# AIW-95 — gap, symmetry and hygiene analysis of the FMT didactic-pattern registry

Run 2026-08-24 against `.claude/knowledge/didactic-patterns.md` (832 lines, 38 patterns),
`~/crucible/docs/didactic-patterns.md` (908 lines, 122-pattern index),
`paper/full/four-model-theory-full.md` (v15 master, 1100 lines), `project-reference.md`,
`fmt-2015-definitions.md`, the MoC7 poster source and the SJÄLV handover.

Nothing was edited. All line numbers are as-read today.

---

## The three things that matter most

### 1. The registry does not contain FMT's own published teaching devices — only the ones invented since June 2026

The registry's oldest entry is the S231 criticality batch. Everything the *paper* uses to teach —
and the paper is dense with teaching devices — is absent:

| device | where it lives in the paper | in the registry? |
|---|---|---|
| the spreadsheet / "cell A1 contains the sum of column B" | §3.4.1 line 280, reused §3.4.2 line 296, §3.4.6 line 376, §4.2.1 line 556 | **0 occurrences of "spreadsheet"** |
| the three-stage weather ladder (simulation → monitored → closed) | §3.4.3 lines 306–316 | only as #36, and for a *different* job |
| the musical score vs the symphony | §3.4.3 line 326, §3.4.5 line 368 | absent |
| "reading a menu does not feed anyone" | §4.2.5 line 606 | absent |
| the self-reading thermostat's display | §4.2.1 line 552 | absent |
| the information singularity / event-horizon structure | §3.4.4 line 356 | named only inside #37's commentary (line 692) |
| the decompiler that returns code, not an experience | §3.4.5 line 368 | absent (crucible has the correction, its #50) |
| qualia as implicit-model echoes (why vision ≠ hearing) | §3.4.4 line 354 | absent |
| the poisonous mushroom / learning from an observed death | §4.2.4 line 594 | absent |
| Anton's syndrome vs blindsight as a double dissociation | §6.5 lines 788–790 | **0 occurrences of "Anton"** |
| propofol vs ketamine (same label, opposite phenomenology) | §5.3 lines 686–688 | absent |
| the dolphin signature whistle as "that could be me" | §3.4.3 line 340 | absent |
| olfaction bypassing the thalamus | §4.4 line 636 | absent |

**Why this is the most consequential finding.** The header calls this file "the durable catalog of
the didactic patterns FMT uses". It is not that. It is a log of session output. The practical
consequence is that a gap analysis run *from the pattern list* — which is what anyone would do —
concludes that P3 and the level distinction are under-taught, when they are the best-taught things
in the corpus and merely unregistered. It also means the registry cannot do the job it exists for:
you cannot check a new pattern for collision against devices the file does not know about. #36 is
the proof — see §3 below, it collides with a paper device that is not in the file.

**The fix is one sweep, not a policy change:** ingest the paper's devices as a numbered batch,
marked `in-paper, published`, so the file distinguishes *invented* from *deployed*.

### 2. The implicit side of the theory has no teaching device at all — and crucible holds the missing ones behind a stale sync clause

Word-boundary counts across the whole registry:

```
ESM  11    EWM  6    ISM  1    IWM  1
```

Both the ISM and IWM occurrences are on the **same line** (150) and are a *quotation of the paper*
inside #32's commentary. **Not one of the 38 patterns takes an implicit model as its subject.**
Half the 2×2 — the half that carries every dissociation the theory leans on (H.M., the Katlowitz
propofol result, anosognosia, blindsight, split-brain) — is didactically silent.

Meanwhile the missing devices exist, in crucible, and are tagged `authoring`:

- **crucible #107** (lines 729–774) *"the implicit model is what you could read from a dead brain;
  the explicit is what it does while alive"* — MG's own, with his precision *"freshly dead though,
  not rotting"*. This is the clearest statement of the implicit/explicit axis anywhere in the record.
- **crucible #108** (lines 776–803) the implicit model as an *actively maintained* molecular state,
  not a wiring diagram — falsifiable against connectomics.
- **crucible #102 / the 500 grandmothers** (lines 571–591, 661–681) — one stored subnet, 500
  instantiations on Mars in clown costumes. MG's, and his own extension makes it the mechanism for
  self-model redeployment "on a lower level or smaller scale".

**The sync clause is stale and it is actively misleading.** Registry line 816 reads: *"Crucible's
measurement-discipline patterns (its #14–26) are deliberately NOT synced here."* That sentence was
written when crucible's list ended near 26. Crucible now runs to 122, and by its own index
(crucible lines 33–154) roughly twenty entries are tagged `authoring` or `both lists`. Unsynced
authoring patterns: **27, 29, 31, 32, 33, 41, 50, 80, 84, 85, 90, 92, 101, 102, 105, 107, 108,
111**. Verified by grep — "span law" 0/2, "500 grandmothers" 0/3, "dead brain" 0/2, "fly at the
window" 0/2, "bottleneck" **0**/12, "bank robber" 0/1, "assembly manual" 0/1.

A reader of the registry reasonably infers that everything outside crucible 14–26 *is* here. It
is not, and the exclusion sentence is what produces that inference.

Two of the unsynced ones are load-bearing for material the paper already carries:
**crucible #29 (closure ⊂ bottleneck)** and **#41 (the span law)** are the only teaching devices
that exist for §3.6.1 — the channel, its rank, and the *Arbeitsmodell* — which is one of the
paper's strongest recent additions (it *derives* the working-memory span, collapses arousal /
attention / working memory into one component, and predicts the anaesthetic dissociation rather
than accommodating it; paper lines 419–431). The registry has **zero** patterns for it.

### 3. The table lies about at least four patterns, because every correction lives in prose below it

The file is read table-first. Four status rows now contradict their own commentary:

- **#5** (line 27) — status *"book prose + paper (gated as Prediction 5)"*. In the current master,
  **Prediction 5 is "Qualia Structure Is Shareable but Absolute Encoding Is Not"** (paper line 945),
  and `"time dilation"` appears **0 times in the paper**. The cross-reference is dead; whether the
  time-dilation claim has any paper home is undecided and nobody has noticed.
- **#34** (line 189) — status *"paper (v15) + book + outreach — MG-directed"*, followed 52 lines
  later (line 241) by *"the claim is UNDOCUMENTED, not confirmed. Write the hedged form only"*, and
  at line 297 by *"'Modality attribution does not fail at all' is FALSE as written"* (23% of dream
  characters carry no modality at all; 44% identified by "just knowing"). The row still reads as an
  unqualified paper commitment.
- **#4** (line 26) — status *"book + paper"*; the cautions at line 827 forbid both wordings the
  pattern has previously been written with (*"ordered/synchronous Class-2"* **and** *"dominant route
  supercritical"*), and flag a circulating unverified claim (Hobbs 2010 σ > 1). Nothing in the row
  signals the mechanism is unsettled.
- **#13** (line 54) — status *"book + paper"*, written before MG's S299 ruling (line 642) that joins
  the dashboard to #35 and draws the line *"causal power begins only where the readout triggers
  associated simulation"*. The file itself says *"the paper does not currently draw it anywhere"*.
  The row was never re-ruled.

Same shape, one level down: **#20**'s depth-vs-richness inversion is recorded in a *batch header*
(lines 75–76), not in #20's row; **#37**'s row still carries the spoken *"feels uncaused"*
formulation that line 702 supersedes for paper use.

**Structural cause, not carelessness:** the file has one status field and an unbounded prose tail.
Withdrawals land in the tail. A `⚠ see body` marker in the status column, or a `status-as-of` date,
would close the whole class.

---

## 1. Coverage — worked from the theory, not from the pattern list

### P1 — open-ended computation allows free modelling

Best-covered principle: **#1** (network-shaped ocean), **#2** (two dials), **#3** (stall),
**#4** (seizure), **#6** (two governors), and **#25** (complexity is a floor).

Uncovered inside P1:

- **The three-part trichotomy — capability / free instantiation / evolutionary forcing** (paper
  lines 514–518). This is what answers *"why isn't a laptop conscious?"* — the single most common
  question a lay reader and a hostile reviewer both ask. **`"laptop"` appears 0 times in the
  registry.** #23 (ant colony) answers a different question (efficiency), and answering the laptop
  question with an efficiency device is a category error a reviewer will name.
- **Creativity without true randomness** (paper line 522) — deterministic-chaotic variability
  harnessed by an edge-of-chaos system, with the songbird LMAN lesion as the empirical anchor. Vivid,
  self-contained, keeps FMT clear of quantum-consciousness accounts. No device.
- **The two thresholds** (paper §3.7.3) — criticality necessary-not-sufficient, architecture
  necessary-not-sufficient, together sufficient. #18 teaches *"not necessity"* on the closure axis
  only. The two-threshold structure itself has no device, and it is where the laptop lives.

### P2 — recurrent dynamics host a second computational level

Covered by **#36** (weather simulation) and, obliquely, **#32** (compute-on-compute above a
complexity threshold). Everything else that teaches P2 is in the paper and unregistered (finding 1).

Uncovered:

- **The real/virtual split as such.** The project's most-used single image — `figure2-real-virtual-
  split-simple.svg`, "the bubble diagram", canonical enough to have its own entry in
  `project-reference.md` — **is not a numbered pattern**. The registry's most successful teaching
  device is not in the registry.
- **The software-like properties** (paper lines 265–268): forked / cloned / redirected /
  reconfigured. Four operations, each anchored to a clinical case, presented as a set. #33 absorbs
  the forking half into the fish; clone, redirect and reconfigure have nothing.
- **The five-system hierarchy** (paper §3.7.1) — Level 5 is where the whole two-level ontology is
  cashed out, and the project already owns a rendered figure for it
  (`figure-five-layer-stack-bw.svg`, in seven languages). No pattern.

### P3 — phenomenology arises exactly where the modelling closes on itself

**This is the theory's single bridging commitment, and in the registry it has no paper-usable
device.** The two that exist are both explicitly barred:

- **#10** (line 46) — *"book candidate ONLY — MG S243: flowery… Do NOT put in the paper."*
- **#15** (line 56) — *"book candidate; keep OFF the paper's asserted-not-derived side of §3.4.3."*

The paper's own P3 devices — the three-stage weather ladder, the score/symphony, the menu/meal, the
decompiler — are unregistered. So the file's picture of P3 is exactly inverted: it reads as the
worst-taught principle and is in fact the best-taught, with none of the evidence in the file.

Also uncovered, and load-bearing:

- **The temporal echo mechanism** (paper §3.4.4) — the constructed "now", temporal smearing, the
  variable clock. This is the paper's answer to *why the inside perspective feels lived rather than
  merely recursive*, i.e. the residual after closure. No device. Crucible **#111** (olive/theta,
  lines 805–829) names a candidate clock and is unsynced.
- **The Meta-Problem** (paper §3.8) — why we think there is a hard problem. #37 already contains the
  mechanism (the model's blind spot) applied to volition; generalising it to the meta-problem is
  nearly free and nobody has drawn the arrow.

### The four model kinds

| kind | patterns whose subject it is | verdict |
|---|---|---|
| **ESM** | #20 #21 #22 #27 #33 #37 #38 (+ #9, #35) | saturated |
| **EWM** | #13 (partly), #36 (as contrast) | thin |
| **ISM** | — | **empty** |
| **IWM** | — | **empty** |

The EWM specifically — the conscious *world*, scene construction, the thing the reader is looking
at right now — is taught by no pattern of its own. Anton's syndrome (a simulation running with no
input) is the ready-made device and is absent from the file.

### Consequences (the demoted set)

The settled scope statement demotes four things to consequences. Their didactic coverage is wildly
uneven:

- **Redeployment onto the non-self** — five patterns (#20 #26 #27 #28 #38). Over-served.
- **Simulation forking** — one, and only as a sub-clause of #33.
- **Variable permeability** — **none.** This is the largest single gap in the file. Permeability
  carries §6.1 (psychedelics), §6.2 (anosognosia), the psychedelic visual progression, and
  **Predictions 1 and 2** — two of the theory's five. `"permeab*"` appears twice in 832 lines, both
  times in a list of consequences, never as the subject of a pattern.
- **The four model kinds themselves** — the 2×2 has a figure but no *device*; the paper's own
  "four is the floor, not the ceiling" and the elimination argument ("why four, not three?") are
  arguments, not teaching devices, and the registry has neither.

### Other load-bearing material with no device

- **Binding** (Requirement §2.5, mechanism §5.1). `"binding"` occurs 5 times: once in #15
  ("self-referential binding"), four times in #34 quoting Revonsuo. **The binding problem has no
  pattern.** And §5.1 carries a sharp, teachable, rival-discriminating claim — *criticality binds
  into one field and is indifferent to whether the contents cohere, which is why dreams are
  expected rather than anomalous* — that is begging for a device.
- **Personal identity by confabulation** (paper line 570) — you are regenerated every morning from
  the ISM and never see the seam. `"confabulat*"` = 0 in the registry. Extremely teachable.
- **Substrate independence** (paper §4.4) — `"corvid"` 0, `"octopus"` 0. Crucible **#80** holds the
  multiple-realizability material and is unsynced.
- **The graduated ladder** (§3.5) — **#9** is the only device and its status is *"paper only (too
  jargon-heavy for lay book)"*. So the ladder has a paper device and **no book device**, which is
  backwards: rungs of self-observation are one of the easiest things in the theory to draw.
- **Cognitive vs reinforcement learning** (§4.2.4) — the poisonous mushroom is the paper's own
  vehicle and is unregistered.

---

## 2. Symmetry — where one side of a pair is vivid and the other is dark

| pair | lit side | dark side | cost to fill |
|---|---|---|---|
| implicit / explicit | explicit, 11:1 by ESM/ISM count | **implicit: nothing** | low — crucible #107/#108/#102 already written |
| world / self | self, 7 patterns | **world: #13 only** | low — Anton's syndrome is ready |
| global / local permeability | **neither** | both | medium — but see below |
| present / accessed | #9 (paper) | **no book device** | low |
| storage / process | #32 gestures at it | crucible #107 owns it, unsynced | zero — copy it |
| cost / capability | saturated (#18 #23 #25 #26 + two scope cautions) | — | — |
| first-person / third-person | #21 #22 | both `paper-assertability undecided` | a ruling, not a device |
| inside / outside | #37, on volition only | the general constitutive asymmetry | medium |
| voluntary / involuntary decoupling | #6 lock-in, #7→#8 | balanced | — |
| necessity / sufficiency | #18 covers "not necessity" | the two-threshold structure | medium |
| extent / complexity | #2 #4 | balanced | — |

**The cleanest asymmetry in the whole file, and the easiest win: global vs local permeability.**
The paper (line 743) states it as an explicit inverse pair — *"psychedelics globally increase
permeability… anosognosia locally decreases permeability"* — and generates **Prediction 1**
(psychedelics should alleviate anosognosia) directly from the symmetry. It is a two-panel picture
waiting to be drawn, it is the theory unifying two phenomena nobody else connects, and **neither
side has a teaching device.** One pattern with two panels covers a named consequence, two clinical
literatures and one prediction.

Second-cleanest: **the implicit/explicit pair.** The registry is 11:1 on the explicit side and the
fix is already written in the sibling project. This is a copy operation, not authoring.

---

## 3. Collisions and undeclared redundancy

**Declared and fine:** #7→#8; #1/#3 as vehicles for #2; #23 as the vehicle for #18; #16 as the
vehicle for #14/#15; #27 as the vehicle for #26; #38 explicitly distinguished from #28
(defensive vs forward move) at line 721.

**Undeclared, and they are real:**

1. **#11 ≡ #18.** #11 (line 52): *"outside a narrow fit window closure is dead weight."*
   #18 (line 80): *"an efficiency MAXIMUM in a fit window, never 'closure is required for X'."*
   Same claim, same window, arrived from crucible one day apart (07-31, 08-01), both `book + paper`,
   never reconciled. In one chapter these read as the author making the same point twice. #11's
   distinct content is the *energy* framing (a double system pays twice); #18's is the NFL proof.
   Merge, or make #11 explicitly the cost half of #18.

2. **#14 ≡ the paper's "maturing".** #14 (line 55): closure's main function is *"transferring
   EXPLICIT learning back into the IMPLICIT substrate"*. Paper §4.2.3 (line 580) names exactly this
   the **maturing** route, *"usage-driven structural change"*, with the rope-over-the-plank image.
   One mechanism, two names, in two files, neither pointing at the other. Anyone writing the book
   chapter will introduce the reader to it twice.

3. **#36 collides with the paper's existing use of the same vehicle.** The weather simulation is
   already Stage 1 of the closure argument in §3.4.3 (paper lines 306–308), where its moral is
   *"level-specific properties are not enough"*. #36 sends the same vehicle to §7 with a different
   moral — *"a prediction run through a world-model is a weather simulation"*. Both morals are
   right; a reader meeting the same simulation twice, forty pages apart, with two conclusions,
   will read it as a slip. Nobody flagged this because the §3.4.3 use is not in the registry —
   which is finding 1 producing a concrete cost.

4. **#10 ≈ #15.** Both are identities rather than derivations, both book-candidate-only, both
   explicitly barred from §3.4.3's asserted side, both answer *"why is it felt?"*. #15's own status
   line says *"like Pattern 10"* — that is a half-declaration. They are one pattern with two images
   (dual resistance; the side effect of closing the loop). Decide which image ships.

5. **#20 ≈ #38 more closely than #28 ≈ #38.** #38's own "related" line (line 755) lists #20, #26,
   #27, #28 flatly. But #38 (*a listener is an instance*) and #20 (*one model, K deployments*) are
   the same mechanism aimed at two audiences; #28 (parsimony) is a genuinely different move. The
   collision risk is with #20, and the file points at #28.

6. **A dispersed citation-discipline cluster.** #17(a) (don't over-read single-cell correlation),
   #30 (don't borrow contested support), #31's three caveats, and the "convergence honesty" caution
   (line 829) are one rule family scattered across four batches. They should be one block, because
   the failure they prevent is one failure (see §5b below).

7. **A cross-file wording collision.** #12 (line 53) sells the language singularity as
   *"Turing-complete language"*. The SJÄLV claim-discipline list (`docs/pending-sjalv-manual.md`,
   review point 6) rules *"the word 'Turing' appears nowhere"* for that deliverable. Two files,
   opposite instructions, neither aware of the other.

---

## 4. Status hygiene — the decision queue that does not currently exist anywhere

Every open ruling in the file, in one place. This is the list to put in front of MG.

### A. Paper-assertability formally undecided (the file says so in these words)

| # | pattern | what is undecided |
|---|---|---|
| 21 | person-format triad | *"book strong; paper-assertability undecided"* — rides §3.4.3's asserted-not-derived cut (line 83) |
| 22 | 1p-only gets a 3p handle | *"same cut as #21"* (line 84) — one ruling settles both |

### B. Effectively undecided, though not labelled as such

| # | pattern | the problem |
|---|---|---|
| 34 | the dream separates the two tags | row says `paper (v15)`; body says the claim is undocumented and only the hedged sentence at line 322–330 is publishable. **Is the hedged sentence in v15 or not?** |
| 5 | both dials maxed → time dilation | row cites `Prediction 5`, which is now a different prediction. Does time dilation have a paper home at all? |
| 13 | dashboard of the digital twin | MG joined it to #35 at S299; row unchanged; file says the paper draws the line nowhere |
| 31 | the smart brain rewires less | *"paper-assertable only with the caveats below"* — a condition, never converted to yes/no. Does it go in v16 with the caveats, or stay out? |
| 32 | compute-on-compute is the discriminator | *"book (Ed 3 candidate) + paper-safe"*. **`paper-safe` ≠ `in the paper`.** Undecided by construction |
| 35 | the rollercoaster | the S300 verification killed the proposed differentiator and recommends the reordering / priority-inversion signature instead; explicitly *"verification input to `AIW-202`, not a positioning ruling — MG's call stands"* (line 633) |
| 36 | the weather simulation | commentary says *"what it settles, and where it must go"*, but no ruling on whether it **replaces** §7's scope-limitation reply or supplements it |
| 8 | two causal roles | the `ESM-on-EWM control` sub-item is marked **(open, S232)** and has been open since June (line 40) |
| 17 | the Bible Code | `book (Ed 3) + blog` — Ed 3 does not exist; effectively parked with no owner |
| 12 | constant problem-size | carries an unverified quantitative claim (*"<1M lines of C#"*) and an unverified singularity claim, with no verification note anywhere in the file, in a pattern cleared for outreach |
| 7 | dimmer switch | *"folds into #8"* — withdrawn, or retained as a sub-device inside #8? Not stated |

### C. Withdrawn or narrowed *inside* commentary, invisible from the table

Anyone reading table-first will re-introduce these:

- the *"empty coding slot"* argument — **retracted**, primary text kills it (line 247)
- the three-level tag ordering — **superseded**, two-level only (line 196)
- drug-induced synaesthesia as the middle rung — **withdrawn** (line 203); and line 400 gives the
  *better* reason it was dropped, which supersedes the first reason recorded above it
- *"modality attribution does not fail at all"* — **FALSE as written** (line 297)
- the *ansisit* ethnographic hint — **over-weighted, near-worthless** (lines 383–393)
- Domhoff & Fox as continuum support — **withdrawn against the primary** (line 682)
- *"Model-based RL is agnostic there; FMT is not"* — **FALSE, must not be written** (line 632)
- the opioid mechanism in #35 — **softened** to relative pain down-weighting (line 614)
- *"the cats acted out their dreams"* — **interpretation, not observation** (line 682)
- *"advantage scales with recursion depth"* — **axis inverted**, corrected (line 76)
- *"closure enables learnability"* — **withdrawn** (line 762)
- *"feels uncaused"* as a paper formulation — **superseded** (line 702)
- Pattern 4's seizure route — **both** previous wordings forbidden (line 827)

### D. Navigational defects

- **#33, #34, #35 reference `R5` / `R6`** as if they were paper objects. The paper has no R-numbering
  (`grep -cE '\bR[0-9]\b'` = 0); they live in `docs/crucible-evidence-ledger-digest.md`, which the
  registry never names. A reader following the reference finds nothing.
- **Three literature items are marked "do not cite without checking" and have sat unchecked**
  (line 338): Snyder 1970, Schredl & Wittmann 2005, the Hall & Van de Castle category list — the
  last confirmed only from Domhoff's coding site, which is precisely the secondary-source failure
  mode the same session documented twice (see §5a).
- **Three gaps blocking any published gap-claim** are named at line 590 (Winget & Kramer 1979;
  Hunt et al. 1982; the Khallieva 2022 full text — *"Order it."*) with no owner and no backlog ID.

---

## 5. The risk register — recurring failure modes, each named from ≥2 instances

These are stated as checks to run against the *next* pattern before it is added.

**(a) A claim confirmed only from a secondary source fails against the primary.**
Instances: the Revonsuo "empty coding slot" (line 247 — the file's own note says *"the second time
in this session"*); Domhoff & Fox's "continuum", which does not appear in the primary at all
(line 682); Meisel 2012 over-read into "supercritical"/"hypersynchrony" (line 827); the Hall & Van
de Castle list taken from a coding website (line 341); Hobbs 2010's σ > 1, *"unverified and
circulating"* (line 827). **Rule:** a citation may not enter a pattern's *claim* until the primary
has been read; a secondary-confirmed citation is tagged as such and cannot be paper-bound.

**(b) Support borrowed from a result that points the right way but cannot discriminate.**
Instances: mirror neurons, dropped (#30); Schultz & Cole / Thiele, kept only with three caveats
because generic neural efficiency predicts the same sign (#31, lines 118–130); the *ansisit*
vernacular terms (line 383); drug-induced synaesthesia, where the only placebo-controlled test says
it probably is not synaesthesia (line 208). **Rule:** every empirical anchor must name, in the
pattern, the rival account that predicts the same sign. If no rival is named, the support has not
been assessed — it has been enjoyed.

**(c) The signal put on the confound — an axis stated backwards.**
Instances: #20/#26, advantage scaled on depth instead of richness, *"axis-corrected same day"*
(lines 75–76); #4's seizure route, flipped between Class-2 and supercritical, *"both overstate"*
(line 827); the patchwork hologram sitting on both sides of the real/virtual split in the book for a
year (#32, lines 142–148); #35's named trap that *"path length runs opposite to timescale"*
(line 682). **Rule:** for any pattern containing "scales with X" or "belongs to side Y", write the
inverted version out explicitly and state what observation separates them. If nothing separates
them, the axis is not yet a claim.

**(d) Capability language where only price is licensed.**
Instances: the S288 over-application of No-Free-Lunch (lines 765–794); the S299 second axis, with
the violation *"found live in the FMT master twice on 2026-08-10"* (line 812); *"closure enables
learnability"*, withdrawn (line 762); §4.2.3's necessity claim, narrowed to constitutive-not-
competitive (paper line 584). **Rule:** three axes, and barrier language is licensed on none of
them — (A) implicit/explicit, (B) self/world, (C) closure/feedforward, where only (C) licenses
*budget-relative* capability. The licensed form is always **price**.

**(e) An absence written as a finding, in both directions.**
Instances: #34's core sentence, which needed the whole hedged apparatus at lines 322–330; the
missing middle rung, where *"that absence is the point"* (line 215); the full-text corpus that does
not index *Dreaming*, making the zero-hit result *"a weak negative"* (line 332). And the mirror
failure: the *"free modelling is free"* account, which can redescribe every apparent cross-modal
case and therefore needed a stated falsifier written down before use (lines 510–516). **Rule:**
every absence claim carries (i) what was searched and what was not, and (ii) a named observation
that would falsify it. An account that cannot fail is not a finding — crucible's #39.

**(f) A mechanism that an existing literature already owns, discovered late.**
Instances: #35 vs model-based/model-free RL, where the proposed differentiator did not survive
contact (line 632) and *three* steps of the mechanism turned out already occupied; #36, which
exists only because §7's PP reply was defensive rather than discriminating (line 666); #34, where
*"two literatures pass within inches and never touch"* (line 563); #31 vs classical neural
efficiency; #38 vs Bennett's Theorem 2, conceded (line 748). **Rule:** before a pattern is marked
paper-bound, name the literature that already owns its mechanism and state what FMT adds that it
does not. Five instances say this is the most expensive failure mode in the file.

**(g) A first-person or n=1 report drifting toward evidential use.**
Instances: MG's salvia flight case, contained by an explicit *"VEHICLE, never evidence"* (line 537);
Day (2013), the only clear positive on synaesthetic dreaming and n=1 first-person (line 583); the
rollercoaster itself, a worked case that reads as data if the frame is dropped. **Rule:** make
`vehicle | evidence` a field on every pattern rather than a footnote in three of them.

**(h) Status drift — the row outliving its own body.** Instances: #34, #5, #13, #4, #37 (see §3
above). **Rule:** a `status-as-of` date, or a `⚠` in the status column whenever the body contains a
withdrawal.

---

## 6. Poster and book yield — the five to draw

Baseline, so the ranking is honest. The **MoC7 poster** (`scripts/assets/moc7-poster/poster.html`)
currently has eight sections — *Two axes, four kinds · Three principles · What the architecture
accounts for · The criterion · What would falsify it · The ledger · In progress* — and **two
figures, both architecture diagrams** (the 2×2 and the bubble). **The poster carries zero teaching
devices.** The **SJÄLV** handout has ten drawn panels, of which one ("07-leaks") is permeability —
so permeability has an illustration and no pattern, the exact inverse of everywhere else.

⚠ Worth recording separately: the SJÄLV brief defined the **"could not draw" list** as *"the most
scientifically useful part of the return… each entry is a place the theory is still prose"*
(`docs/pending-sjalv-manual.md`, review point 7). MG waived the review on 2026-08-05 and **that list
was never produced.** It would have been AIW-95's gap analysis, done independently, by an
illustrator. It is still obtainable and it is cheap.

Ranked by (a) vivid × (b) self-contained × (c) unused:

**1. #4 — the seizure negative control.** *Two cortical sheets side by side: left, a generalized
tonic-clonic seizure — near-total co-activation drawn as one flat uniform colour, captioned
"co-activation ≈ max, Class-4 involvement ≈ 0, unconscious"; right, waking — patchy, differentiated,
multi-coloured, captioned "co-activation lower, Class-4 involvement high, conscious".*
The only pattern in the set that *discriminates* rather than illustrates. It is already paper-bound,
needs no new claim, and it kills "more activity = more consciousness" in one look — which is the
misreading a room of neuroscientists arrives with. A poster audience respects a negative control
more than an analogy. ⚠ Caption must say only *"exit from Class-4"* — the route is unsettled
(line 827).

**2. #34 — the four-case dissociation table.** *A 4 × 3 grid: rows lilliputian hallucination,
Charles Bonnet, synaesthesia, dreaming; columns content generated / modality tag / reality tag.
Eleven cells green, one red — dreaming's reality tag — with a small brain inset beside that row
showing dorsolateral PFC greyed out.*
This is the strongest empirical-looking object the theory owns that is not a prediction, and the
grid delivers the conclusion visually before anyone reads it: *the reality tag is a property of the
reader, not of the signal.* It is already drawn as a table at line 408. ⚠ The modality column must
be labelled *"intact / often unassigned"*, not *"never fails"* (line 297).

**3. #2 + #3 — the two dials against the stall curve.** *A lift-vs-angle-of-attack curve with the
brain's operating point marked just before flow separation; two independent dials beside it, EXTENT
and COMPLEXITY, with the rare jointly-maximised corner shaded and labelled "dissociative".*
The poster currently states the three principles in words with no picture of the regime. This is
also the one place where FMT's contribution over C_N is *visible* — two axes on different
mathematical objects, not one optimised scalar — which is precisely the priority-claim the
convergence-honesty caution (line 829) requires us to make carefully. Drawing it makes the careful
version the easy version.

**4. #27 — the cat learns to hunt by imitation.** *Mama cat's causal chain across the top as four
small panels (forage → catch → neck-bite → eat); below, the kitten watching, with its own
body-outline ghosted onto mama's — one model, re-pointed, marked "level-1".*
The best drawing in the whole set for a lay audience, and the cleanest statement of redeployment.
It is also the pre-loaded answer to the question a poster actually gets asked — *"isn't this just
recursion?"* — with the answer visible in the picture: the ghost outline, not a stack of loops.
Book value is equally high.

**5. #37 — the one thing missing from your world.** *A first-person scene containing everything the
simulation models — the room, the body, other people, the self — and one object-shaped absence where
the apparatus would be, rendered the way a visual blind spot renders: not a hole, but nothing at
all.*
The project already owns `figures/blind-spot-test.png`, so half the visual grammar exists and the
figure can literally demonstrate itself on the reader before the argument is made. ⚠ Must carry the
S300 refinement (line 702): the caption is *"the choice presents as originating in the self, with
nothing behind the self"* — **not** *"feels uncaused"*, which the Fable red-team retired because an
uncaused event presents as arbitrary rather than free.

**Runners-up and why they lost.** #23 (ant colony) is vivid but teaches a negative, and a poster
panel whose moral is "this is inefficient" reads as a concession. #33 (the fish) is excellent book
material but the terminology trap — *sentience*, never *awareness* (line 154) — is hard to enforce
in a caption. #16 (tears at the musical phrase) is the best pure-book image in the file and is
nearly undrawable. #17 (Bible Code) risks reading as anti-neuroscience on a wall in front of
neuroscientists. #35 (the rollercoaster) is the most quotable prose in the file — *"will do so one
of these days just to prove free will (and never does it)"* — but its positioning against
model-based RL is unsettled (line 633), so it should not go on a poster before MG rules.

---

## 7. What I would do first, in order

1. **Ingest the paper's own devices** as a numbered batch marked `in-paper`. Until that exists the
   registry cannot detect collisions, and #36 already collided undetected.
2. **Copy crucible's authoring patterns** (27, 29, 31, 32, 33, 41, 50, 80, 84, 85, 90, 92, 101, 102,
   105, 107, 108, 111) and **rewrite the exclusion clause at line 816** to name what is excluded by
   *tag* rather than by a number range that stopped being true 96 patterns ago.
3. **Put §4's decision queue in front of MG.** Twelve rulings; #21/#22 and #34 are the two that
   block paper work.
4. **Write one pattern for permeability with two panels** (global up / local down). It is the
   largest gap, it is a documented inverse pair, and it carries two of five predictions.
5. **Add a `status-as-of` field and a `vehicle | evidence` field** to every row. Those two fields
   close failure modes (g) and (h) mechanically.
6. **Ask for the SJÄLV "could not draw" list.** It is an independent gap analysis that was
   commissioned, paid for in brief-writing, and never collected.
