<!-- Action: reference -->
<!-- S288 2026-08-06: §4's handover decision IS TAKEN — MG chose the work order (audit → web via
     infrastructure; poster LAST as a sink for crucible results; Bildstein unpinned) and settled all eight
     §4 open decisions. All eight proposed priorities in §5 are CONFIRMED. Do NOT re-present §4 or §5.
     Retained as reference only for the §2 routing table, whose web/blog/JAIC lanes are still live.
     Continuation: docs/pending-s288-audit-continuation.md -->
<!-- Tracked-by: AIW-146, AIW-150, AIW-151, AIW-152, AIW-153, AIW-27, AIW-100, AIW-137 -->
# S285 — content routing + handover

**MG's closing instruction (2026-08-05):** *"make sure everything is documented where it belongs, and inform
cru and books accordingly, consider what goes in which paper, book or new paper or book, what goes into a blog
maybe and so on. when all is filed and tracked, handover, next session must decide what to do next for moc7.
cru is still experimenting and i want to give it a few more days so we have really interesting computational
paper for moc7, so aiware must work on something else for moc7 in the meantime. books and flyer are ready,
standard model will go to web primarily and then maybe paper, maybe standard model proposal whatever."**

---

## 1. Where the session's output already lives

| Artifact | Home | State |
|---|---|---|
| The chart (SMoC draft) | `docs/smoc-middle-layer-draft.md` | ~700 lines, committed |
| The method | `docs/smoc-method.md` | committed |
| Chart figure | `figures/smoc-marks.svg` + `scripts/build_smoc_marks.py` | drawn, visually verified |
| Argument-space map | `figures/smoc-philosophy-map.svg` + `scripts/build_philosophy_map.py` | drawn, visually verified |
| 2015 definitions | `.claude/knowledge/fmt-2015-definitions.md` | ~35 verbatim + rulings + contradiction flags; in the CLAUDE.md triggered table |
| MG's thinking tools | `docs/mg-thinking-tools.md` | Tool 1 captured; standing capture protocol |
| MoC7 questions | `docs/moc7-questions.md` | 5 Class-A + 6 Class-B + 2 Class-C |
| Decisions + rationale | `docs/decisions.md` S285d / S285d.1 / S285e / S285f | committed |
| Review kit (readable) | `tmp/smoc-review/` and `C:\Users\Matthias\Downloads\smoc-review\` | 2 PNGs + 3 PDFs + 2 SVGs |

---

## 2. Routing — what goes where, and why

**MG's standing decision: the standard model goes to the WEB first**, then maybe a paper or a "standard model
proposal". That decision also happens to resolve the `AIW-149` sequencing problem at no cost — web publication
of *new* material carries no prior-publication exposure for the NoC/JAIC slices, because the chart is not the
FMT paper and is not either slice.

| Output | Route | Why this route and not another |
|---|---|---|
| **The chart + the method** | **WEB FIRST** — `fmt.matthiasgruber.com` wiki restructure (`AIW-27`), then optionally a standalone *SMoC proposal* | MG-decided. Web is unbounded in length, revisable (the D6 revisability licence *needs* a revisable medium), needs no affiliation, and is what a MoC7 QR code can point at. A journal cannot host a coordinate system that is meant to be edited. |
| **Bezugssystem regress argument** (implicit models are *logically* required) | **FMT MAIN PAPER**, §3.6 implicit–explicit boundary; and the NoC slice if it fits | The strongest new *argument* of the session and it runs on definitions alone, so it survives readers who reject the neurobiology — exactly what a hostile reviewer cannot dismiss. Wasted on a blog. |
| **Arbeitsmodell = Bottleneck occupancy + the four derivations** | **FMT MAIN PAPER** (§3.6/§5) **and the JAIC slice's detector**; plus a **blog** for the 7±2 result | Paper-grade: it converts a stipulation (working-memory capacity) into a derivation (rank *k*), predicts anaesthesia rather than merely accommodating it, and gives the best available line on GNWT — *right structure, misassigned role*. The 7±2 half is also the single most blog-able thing produced today. |
| **Third dial — Bottleneck rank** | **FMT paper §3.7 / AIW-92 two-dials work**, and **crucible** as a design axis | It amends an existing published framing (two dials), so it must go where the two dials live. Crucible needs it because it is a manipulable axis and blank **B5** is theirs. |
| **Meaning as coordinate transform + the teaching corollary** | **BLOG** (primary), then the RIM/intelligence lane | Accessible, vivid, self-contained, and it lands the *expert-can't-teach* result that general readers immediately recognise. Too small for a paper on its own; excellent as an essay. |
| **MG's Tool 1** (two sides → dimensions) | **BLOG / essay**, and a chapter candidate if `AIW-148` picks the intelligence book | It is a thinking method, not a finding. Its natural form is a first-person essay; forcing it into a paper would strip the voice that makes it work. |
| **The Presence Term + exclusion ledger** | **WEB** (with the chart) + a **BLOG** on the dark-matter parallel | The dark-matter analogy is the most press-friendly asset of the session and it is *disarming* rather than combative — the right first public note. |
| **The 2015 definitions catalogue** | **WIKI glossary** + the FMT paper's terminology section; German original stays authoritative | Reference material. The wiki is where a reader looks up a term; a paper cannot carry 35 definitions. |
| **Truth-chapter contradiction (p.24 vs p.32)** | **INTERNAL ONLY** → a German-book **2nd-edition errata** item (`AIW-153`) | **Do NOT publish this analysis.** It is a self-criticism of MG's own monograph and has no upside in any venue. Its only action is: fix in a future edition, and keep the *Wahrheitsgehalt* framing out of English submissions. |
| **Qualia ruling** (definitionally downstream of consciousness) + the *epiphenomenon* hazard | **WRITING DISCIPLINE** → already in the KB; enforce in every draft | A rule, not a publication. The hazard (philosophers read *epiphenomenalism* = no causal power) would cost a reviewer's goodwill for nothing. |
| **The LLM breadth claim** (a closed LLM would be richer in breadth) | **JAIC slice** §detector discussion, carefully scoped; **not** a blog yet | Publishable in the machine-consciousness venue where the scoping caveats will be read. On a blog it becomes "AI would be more conscious than you", which is the headline nobody wants and which the caveats cannot outrun. |

**What explicitly does NOT get a new artifact.** No new book. `AIW-148` (second-book angle) and `AIW-149` (the
monograph) both stay as they are — today's material strengthens option (c) of AIW-148 (the middle-layer book)
but the trigger for that decision has not fired, and the monograph is still sequenced behind the journal
slices and the Kleiner question.

---

## 3. Cross-project notifications — filed

- **crucible** (inbox): the third dial (rank as a manipulable axis, feeding their blank B5), the
  Arbeitsmodell=occupancy identification and its four derivations, the workspace reframe (GNWT = right
  structure, misassigned role), and the closed-LLM breadth prediction with its lock-in corollary. Plus: the
  chart now carries their S3/S4/S5 selection rules as generalisable results, credited.
- **simbook** (inbox, filed earlier this session): the second-book angle including the middle-layer option, and
  the KDP sales-trend monitoring gap that makes the `AIW-148` trigger undetectable.
- **social** (inbox): three blog candidates ranked, with the one to hold back and why.
- **life** (inbox, filed earlier): cross-reference the thinking-tools registry from `psych-profile.md`.

---

## 3b. STATUS AS OF S287 (2026-08-06)

**The paper lane of §2 is EXECUTED and FMT v14 IS PUBLISHED** — version DOI `10.5281/zenodo.21822872`, concept
`10.5281/zenodo.18669891` now resolves to v14, 130 pp. All three paper-bound results from §2 are in it (the
Bezugssystem regress argument in §3.6; the *Arbeitsmodell*=channel-occupancy identification as new §3.6.1; the
third dial in §3.7), plus the §7.2 GNW reframe. **So the deadline finding in §4 is closed: the MoC7 poster QR
resolves to the concept DOI and therefore now serves a paper that agrees with the poster.**

**What is NOT done from this file:** the WEB lane (`AIW-27` wiki restructure — the chart, the method, the
Presence Term, the 2015 glossary), the BLOG lane, the JAIC-slice items, and `AIW-153` (German-monograph errata).
**The §4 decision below was never taken** — MG redirected S287 to v14 work instead — so it stands as written,
minus candidate B's dependency on a paper that has now shipped.

---

## 4. Handover — what the next session must decide

**MG's framing: crucible needs a few more days so the computational companion is genuinely interesting for
MoC7. So aIware works on something else for MoC7 in the meantime, and next session decides what.**

Books and the flyer are **done** — do not reopen them.

### The candidates, with my read

| # | Candidate | Case for | Case against / blocker |
|---|---|---|---|
| **A** | **The citation audit** of the chart's agreement marks | **Prerequisite to everything public.** Every *agreed* and *converging* mark, plus every argument-space placement, is currently my judgement. Several placements are of theories whose authors will be in the room. | Unglamorous; produces no new artifact. But nothing public can ship before it. |
| **B** | **Web deployment of the chart** (`AIW-27` restructure) | MG-decided route, and the thing a MoC7 QR code should point at. No journal exposure. | Gated on **A** for the marks; the wiki also has a Part-2 refresh already pending (`docs/pending-wiki-refresh.md`). |
| **C** | **The A0 poster** (`AIW-137`) | Hard-dated (Oct 12). The chart is now the obvious spine, and the figure exists. | Organisers still have not answered the four logistics questions; A0 portrait remains the working assumption. |
| **D** | **The ~Sept 12 discussion question** (`AIW-150`) | **One-shot gate**, and the highest-value MoC7 asset is the collective paper it feeds. | Needs MG to pick between "value if it runs" (A1) and "probability it wins" (A2). Not this week, but not much later. |
| **E** | **The SMoC charter** (`AIW-100`) | Gates the dated Bildstein session; smallest artifact that makes the chart real. | Bildstein is post-Greece, mid-late September — slightly behind MoC7 in urgency. |

**My recommendation, for the next session to accept or reject: A then B, with C in parallel.** The audit
unblocks both the web deployment and the poster, and MG has already named the web as the primary route. D needs
an MG decision rather than work, so surface it early rather than doing it. E follows once the chart is public,
because a charter pointing at a live chart is a much easier thing to send than one pointing at a draft.

### Open decisions MG has not yet ruled on

1. **Register naming** — Wired/Running on the chart's face? **New input:** the 2015 book supplies
   **Bewusstsein (capacity) vs Bewusstheit (ongoing interaction)**, MG's own distinction, mapping onto exactly
   this axis. Consider before settling.
2. **Adopt the agreement marks** (§0.2) as the chart's marking system.
3. **Keep 2015's *Interpretation* / *Bedeutung* split**, or let the coordinate-transform language carry both?
4. **Is R4 the sentience floor or the consciousness floor?** Every translation depends on it.
5. **Chart scope** — consciousness only, or with RIM?
6. **Residue name** — the Presence Term?
7. **The *erweitert* ladder is finer-grained than R4–R6** (three 2015 rungs plus identification). Is the chart
   under-resolved there, or do the 2015 rungs collapse?
8. **Truth** — accept the p.24-over-p.32 resolution, rename *Wahrheitsgehalt* to a consensus/corroboration
   term, drop the "Konvention von Wahrheit" sentence?

### Standing item, every exchange until MG confirms

**MoC7 travel — flight and hotel for Oct 11–16 are NOT booked.** Registration, dinner and payment are done.

---

## 5. Backlog priorities awaiting MG's confirmation

Per the fleet rule that new backlog entries need user priority review — **all eight of this session's items
were added at a PROPOSED priority and none has been confirmed.** Surface this early next session; it is a
two-minute pass.

| ID | Proposed | What it is |
|---|---|---|
| `AIW-146` | **P1** | The SMoC chart + method (the session's main deliverable) |
| `AIW-147` | **P3** | MG's thinking-tools registry — standing capture protocol |
| `AIW-148` | **P3** + trigger | Second-book angle decision; **the trigger is currently undetectable** (nobody monitors KDP sales trends — filed to simbook) |
| `AIW-149` | **P2** | The FMT monograph; sequenced behind the journal slices, gated on the Kleiner question (B1) |
| `AIW-150` | **P1** | MoC7 question collection; **P1 because ~Sept 12 is a one-shot gate** |
| `AIW-151` | **P1** | The 2015 definitions + the outstanding rulings; **P1 because a live draft depended on a definition the book contradicts** (now fixed) |
| `AIW-152` | **P1** | Routing today's results into paper / web / blog lanes |
| `AIW-153` | **P2** | German-monograph 2nd-edition errata, opening with the truth-chapter contradiction |

*Note on the rotation warning about five same-day pending files:* four were merely touched rather than created
(`pending-moc7-copenhagen.md` gained a cross-reference, `pending-sjalv-print-order.md` a status update). Only
this file is new. They cover genuinely separate concerns and should **not** be consolidated.
