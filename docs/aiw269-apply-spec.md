<!-- AIW-269 S324 — the ruled edit list for FMT v16 + formalization v4. Rulings: docs/decisions.md (2026-09-28 S324). Verified references: docs/aiw269-refs-verified.md. -->
# AIW-269 apply spec: every ruled edit, with its final text source

Line numbers are v15-era approximations. **Locate every edit by its quoted text, never by line number.**
Every edit to the master goes into BOTH `paper/full/four-model-theory-full.md` and the hand-maintained
`paper/full/latex/paper.tex`. References go into the md reference list AND `paper/full/latex/references.bib`,
copied from `docs/aiw269-refs-verified.md` exactly as given there.

## Master (FMT v16)

| ID | Where | Final text source / instruction |
|---|---|---|
| A1+A4 | §6.3 hot-zone paragraph ("Siclari et al. (2017) identified…"); §8.1 | `drafts/aiw269-must-answer-drafts.md` A1+A4, verbatim (both parts). |
| A3 | Table 1 closure row, cell "No-report paradigms (Tsuchiya et al., 2015) + targeted TMS during metacognition." | drafts A3, verbatim. |
| A5 | §8.7 "**Unique?**" line | drafts A5, plus one clause naming CTM-AI and ReCoN-Ipsundrum as further implementation blueprints (refs file). |
| A6 | Footnote at first "self-referential closure" in §3.4.3 | drafts A6, verbatim. |
| A2 | §7.2 after the unfolding-argument paragraphs; §4.4 pointer sentence | drafts A2, verbatim (hedged form; Basri PDF not read). Add Chalmers 1996b; **relabel the existing Chalmers 1996 (*The Conscious Mind*) citations to 1996a** (4 in-text sites, per refs file). |
| A7 | §3.7 | `drafts/aiw269-a7-g1-review.md` A7: paragraph after "Concrete neural signatures" paragraph + the four accompanying edits. |
| G1 (a) | §7.2 GNW entry, replaces its last sentence | review file G1(a), **but replace its final falsifier sentence** with: "The first claim predicts a gradient in what such training can recover: a comparable model trained only on the output of sub-Class-4 processes should develop no comparable workspace, one trained only on mathematical or physical equations at most a far more abstract one, and text written by model-running systems yields the workspace observed." |
| G1 (b) | Block paragraph, "The operationalizations in Table 1 … are therefore tracking the right target…" | review file G1(b), with "ignition-like broadcast" (already so worded). |
| G1 (c) | §4.4 LLM paragraph | review file G1(c), both insertions. |
| A8 | Table 4 propofol cell; the "Propofol produces absence…" sentence | Cell: `Absent` → `Absent at surgical depth`. Sentence → "At surgical depth propofol produces absence of reportable experience (Alkire, Hudetz, & Tononi, 2008; Boly et al., 2012). Dream reports after propofol anaesthesia are nonetheless common, and whether the dreams occur during maintenance or at emergence is unresolved (Sikka, Hu, & Heifets, 2026). Awakened repeatedly from deep propofol sedation, participants gave experience reports on 24 of 52 attempts, and perturbational and Lempel-Ziv complexity did not differ between awakenings with and without reported experience (Bajwa et al., 2025)." **No prediction sentence (MG ruled it dropped).** |
| A9 | §7.2 PP entry, after the Hohwy & Seth quote; §1 COGITATE sentence | PP entry: "Its proponents have since entered active inference as a contender, alongside IIT and neurorepresentationalism, in an adversarial collaborative review (Corcoran et al., 2026), and the comparison below treats it on those terms." §1, after the COGITATE sentence: "A second adversarial review has since compared IIT, neurorepresentationalism and active inference (Corcoran et al., 2026), and a reanalysis of the COGITATE data found prefrontal ignition at stimulus offset as well as onset (Bandara, Rowe, & Garrido, 2026)." |
| AIW-243(1) | three one-clause hedges | Locations and text: `backlog.md` AIW-243 item (1) and `docs/reviews/2026-08-26-fmt-v15-fable-review-3.md`; re-locate (old line refs :233/:326/:417 are stale). |
| AIW-243(2) | §7.2 GNW entry; §6.0 PRM sentence (cites only Dijkstra) | Citations only: Mashour et al. 2020 beside the GNW citations; Lau 2022 beside the Dijkstra PRM line. No under-sell pass. |
| AIW-266 | near the Class 4 requirement (§3.7) | One sentence: membership in Class 4 is formally undecidable (Culik & Yu, 1988), which is why the theory commits to the regime's measurable signatures rather than to a decision procedure. |
| AIW-219 | seventh banked result (search "bottleneck"/"span", ≈ l.1003) | One clause crediting Friedlander et al. 2015 with the bow-tie ⇔ rank-deficient-goal result. |
| AIW-251 | §3.7 extent dimension ("σ and the DFA exponent be estimated regionally") | One methods sentence: regional criticality estimates need a surrogate that preserves each region's temporal structure (window-jitter), because shuffling columns manufactures spurious local criticality. |
| Must-cites | per refs file master table | Every VERIFIED / CORRECTED row not already present, at its stated location, as a minimal citation of an existing claim. Rows whose note says the draft's gloss is unsupported (Bates, Dijkstra-Fleming-Shea) are cited only for what their abstract says. **Skip Tiehen & Tubert** (a must-answer MG has not ruled) and list it. |
| AIW-240 | md reference list | Alphabetical sort after all insertions (35 out-of-order entries). |

**Held (do NOT apply):** AIW-243(3) style pass, AIW-201, AIW-265, AIW-75, AIW-77.

## Formalization roadmap (v4) — `paper/fmt_formal/fmt-formalization.md`

| ID | Where | Instruction |
|---|---|---|
| F1 | Lemma L2 item (v), after the Zenil sentence | drafts F1 text, corrected: the necessary-and-sufficient theorem is Sugiura et al.'s (continuous time; **verify those papers**); Roig, Muñoz & Morales (2026) extend it to driven discrete-time reservoirs and find it peaks at marginal driven stability. Add Du & Wang (arXiv:2607.17909) as the counterweight (forecasting optimum off the Lyapunov edge). |
| AIW-251 | §4, E-dial over locally-critical regions (≈ :335–369) | 3–4 sentences, stated as a methods point with a standard jitter-surrogate reference (verify it), not as an unreplicated crucible result. |
| Must-cites | refs file roadmap table | Every VERIFIED / CORRECTED row not already present, at its stated location. |
