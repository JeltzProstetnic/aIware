<!-- AIW-269 half (a), produced S323 2026-09-28 by triage subagent; unverified by main loop until MG rulings. -->
# AIW-269 (a): open-todo sweep, FMT v16 + formalization v4

Swept 2026-09-28: all 135 open entries in `backlog.md` (`[ ]`, `[>]`, `[?]`). Only the entries that would change the text of either paper are listed below. Every "landed" claim was checked with grep against `paper/full/four-model-theory-full.md` (MD), `paper/full/latex/paper.tex` (TEX) or `paper/fmt_formal/fmt-formalization.md` (FORMAL).

Left out on purpose: cosmology (AIW-163/165/166/167/168/169/173/174/186/187), RIM (227/249), the companion (182/140/218), NoC/JCS/JAIC/PLR (235/46/62/129/228), the wiki, the book, outreach, and tooling-only items.

**Tracking gap found:** v16 has no epic. The S317 handover says the master queue "rides `AIW-210`'s v16". AIW-210 is `[x]` at backlog:135, so that pointer goes nowhere. This is the same problem AIW-193 recorded for v15.

## FMT master (v16, P0)

| ID | What | Class | Evidence / size / decision |
|---|---|---|---|
| AIW-263 `[?]` | Free-will part (ii) paragraph in §4.2.2 | LANDED in source | 4 refs present (MD `Charpentier` ×2). The entry says it closes when a gated build promotes a PDF that contains it, so it closes at the v16 build, not before. |
| AIW-222 | A#7 "condensation graph" wording, which no code implements | LANDED | Fixed at S316 in `6e38c7f9`. MD:1003 now reads *"an exhaustive minimum-synapse block search over the model connectome"*. `condensation` gives 0 hits in MD and TEX. The drift checker still shows `[pdf-only] the condensation graph of` only because v15 is the canonical PDF. |
| AIW-243 (4) | Four-decimal tie: within-run, with the reproduction floor stated | LANDED | MD:1003 reads *"That tie is a within-run comparison … reproduce across rebuilds only to about 0.00026"*. The TEX carries the same text. |
| AIW-243 (1) | Three optional one-clause hedges (reafference scope, score-analogy qualifier, independent 5-HT2A ceiling criterion) | NEEDS-RULING | MG chose "smallest diff" for v15. Decision: apply them in v16 or drop them for good. The entry's line numbers (`:233/:326/:417`) are stale and have to be re-located. About 3 clauses. |
| AIW-243 (2) | Missing Mashour et al. 2020 (canonical GNW) and Lau's perceptual reality monitoring. Six places where FMT under-sells itself | NEEDS-RULING (recommend yes) | `Mashour` gives 0 hits. Lau's PRM is not cited: §6.0 at MD:718 cites only the Dijkstra PRM line. The citations alone are about 2 sentences plus 2 refs in §7.2/§6.0/OQ7. The six under-sold places are about a paragraph each (source: `docs/reviews/2026-08-26-fmt-v15-fable-review-3.md`). Decision: citations only, or the full under-sell pass. This is also a literature-half (b) item. |
| AIW-243 (3) | Ambient style load (123× "rather than", 861 em-dashes) | NEEDS-RULING | This would be a whole-paper pass. Recommend deferring it: it is the most expensive item and has the lowest value for a preprint. |
| AIW-240 | 35 MD reference-list entries out of alphabetical order | IN-SCOPE v16 | Re-measured today: `check_md_pdf_drift.py --paper full` still reports 35. This is MD only, because bibtex sorts the PDF. It is mechanical, about 35 line moves. The Libet sort-key question has a standard answer: APA puts the single-author entry first, so no ruling is needed. |
| AIW-253 | "More meaning than meaning" plus the Gurnee J-space contrast (forward direction derived, reverse asserted) | IN-SCOPE v16 (placement open) | Content was ruled at S316. The S317 handover lists it as not needing MG. `Gurnee`, `J-space` and `more meaning` all give 0 hits. About 1 paragraph in §7 plus 3 refs: Harris 1954, Firth 1957, Gurnee 2026 arXiv:2607.15495. The refs must be verified first. This is the largest new-content item. Keep it away from Fable (classifier). |
| AIW-201 | Capability-null inversion as a dissociation prediction (null on the self-relational increment, in a named long-horizon/novelty regime) | NEEDS-RULING | `capability-null`, `self-relational` and `spandrel` all give 0 hits. Ruled P1, and the four repairs are specified. Decision: write it into §8 now, as a prediction without data, or hold it until crucible's matched-recurrence design exists. |
| AIW-265 | Boredom | NEEDS-RULING | `boredom` gives 0 hits. The analysis recommends Option D: nothing, or at most one §9 open question. MG's foraging reframe turns it into a citation (Hills, Agrawal 2022, Burghardt). Q-place is unanswered. The analysis also flags a separate Q-will tension: the paper's will (≈MD:564) against the 2015 p.114 definition. |
| AIW-266 (optional master half) | Class 4 membership is formally undecidable (Culik & Yu 1988) | NEEDS-RULING | `Culik` gives 0 hits. About 1 sentence plus 1 ref near the Class 4 requirement. It is a likely reviewer objection. The entry itself calls it optional. |
| AIW-219 | Friedlander et al. 2015 already owns "bow-tie iff rank-deficient goal; waist = rank" | NEEDS-RULING (recommend yes) | `Friedlander` gives 0 hits. The seventh banked result (MD:1003) states bottleneck selection and span without this prior art. About 1 clause plus 1 ref. The entry only ruled the framing for the standalone paper, not for the master. |
| AIW-251 | Local-criticality surrogate caveat (column shuffle manufactures +0.44; use window-jitter) | NEEDS-RULING for master | MD:482 only requires regional estimation and describes no method. At most 1 sentence here. The formalization is the better home (see below). |
| AIW-75 | Deferred polish bucket | Mostly LANDED; one NEEDS-RULING | Landed: Passos-Ferreira at MD:798, TEX:1005, ref MD:1500. The citation-breadth pass was grep-verified at S241. `[^quantum]` was kept on purpose. Open: pruning the self-citations (`Gruber, 2015` ×17 in MD), which was deferred "to next edition". Decision: now or never. |
| AIW-77 | Fold "sentience" as the name for the awareness floor into the terminology section | NEEDS-RULING | The knowledge-base half is done (`.claude/knowledge/awareness-consciousness-terminology.md`). `sentience` gives 0 hits in MD. This is a terminology decision and interacts with AIW-190's two floors. |
| AIW-190 | Two-floors sub-threshold awareness claim | DEFER | Gated on AIW-192's DREAM reanalysis, which has not run. The entry states that the weak form needs no paper change. |
| AIW-142 | Pattee epistemic cut → §3.4.3; Kirkeby-Hinrup & Stoll; Stewart | DEFER | Convergence-note lane (P2) with no master ruling. `Pattee` gives 0 hits. Birch's manifesto is already cited (MD:1172). |
| AIW-252 | ↻ missing from the `figure1-*-bw*.svg` files | DEFER (does not touch the paper) | The paper uses the colour `figure1-four-model-architecture.png` (TEX:311, md5-identical to `figures/`). Its SVG contains no ↻ at all, so the defect is book/bw only. This was not render-checked. |
| AIW-234 | Reference gate silently substitutes when a printed DOI fails | DEFER (tooling) | Changes no text. Any v16 run of `verify_references.py` inherits the blind spot, so hand-check the DOIs of new refs. |
| AIW-95 | Didactic registry gaps | DEFER | Registry only. The §3.4.3/§7 double use of the weather simulation that it flags is now cross-referenced (MD:855 cites Section 3.4.3). |

## Formalization roadmap (v4, P1)

| ID | What | Class | Evidence / size / decision |
|---|---|---|---|
| AIW-266 (formalization half) | Lemma L2 item (v) cites Zenil 2010; caveat on the K dial | LANDED | `40d68e1d`. `Zenil` ×3 in FORMAL. Zenil's second reply ("no proof, only empirical evidence") matches FORMAL:307 as written, so no edit is owed. The entry stays open only for the SB-HC4A Module 2 half, which is parked until after MoC7. |
| AIW-268 (formalization mention) | Principle 3 must state mutual closure | Nothing to change (as far as grep shows) | FORMAL never states Principle 3 or "enters the update rule". Closure appears as ESM self-representation (FORMAL:128, §6.4 Ψ(m\*)=m\*). Optional: one clause in §6.4 saying that ESM and EWM enter each other's dynamics. **Unsure whether MG wants that clause.** |
| AIW-251 | Window-jitter vs column-shuffle surrogate caveat for local criticality | IN-SCOPE v4 (ruled "attach wherever a draft describes measuring local criticality") | FORMAL §4 (≈:335–369) defines the E dial over *locally-critical regions*, which is exactly the method the caveat covers. About 3–4 sentences. State it as a methods point, with a standard jitter-surrogate reference, rather than as an unreplicated crucible result. |
| AIW-10 | Collaborator outreach | DEFER (no text change) | Outreach only. |

No other open entry names `fmt_formal/` or the formalization roadmap. AIW-261 and AIW-208 are already `[x]`.

## Pending files

The reference pending files were checked by their Tracked-by IDs, and `pending-s309`, `-s312` and `-s317` were read for FMT sections. None of them names an unfinished paper edit that is missing from the backlog. The only new finding is the dangling "AIW-210's v16" pointer in `pending-s317-collaborators-and-master.md` (reported above).

## LANDED — close these (or narrow them to their non-paper remainder)

- **AIW-222**: close. Evidence: `6e38c7f9`, MD:1003 "minimum-synapse block search".
- **AIW-202**: close. The §4.2.3 DREAMING/MATURING re-cut (`0b422f17`, MD:586/588) and the PP discriminator (MD:855 "a prediction run through a *world*-model is a weather simulation … through a *self*-model is one that someone undergoes") are both in v15.
- **AIW-193** (v15 epic): close. v15 is published, and the one site left for MG ("or ablation of the explicit self-model") is gone (`ablation` in MD appears only at :674, Lashley).
- **AIW-110**: close. The paper side was done at S267 (§8.9 exists at MD:995). Only blog routing remains, which AIW-122 covers.
- **AIW-53**: close. Barrett/Milinkovic/…/Seth 2026 (MD:1150), Tucker, Toker, Algom & Shriki and Bach & Sorensen are all cited. The rest is outreach or media.
- **backlog:347 / :348** (orphan sub-bullets under the closed AIW-73): close as superseded by AIW-75 (2)/(3).
- **AIW-232**: narrow to the companion. The FMT obligation landed at S309. `falsifier`, `spandrel`, `joule` and `26–79×` all give 0 hits in MD.
- **AIW-151 / AIW-152**: narrow. The regress argument (MD:402) and the v14 paper lane landed. What remains is knowledge-base, wiki and blog work.
- **AIW-243 (4)**: mark done inside the entry (see table).
- **AIW-266** formalization half: mark done. **AIW-263** closes at the v16 gated build.
