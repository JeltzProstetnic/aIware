# Theory-map paper v3 cut: change report

Source: `theory-map-paper.md` (v2, 11,324 words by `wc -w`). Output: `theory-map-paper-v3-cut.md`.

**Final `wc -w` on the whole output file: 9,762** (limit 9,800). The abstract is 250 words (it was 299).

About 520 of those words are table pipe characters (`|`) that `wc -w` counts as words. The rendered word count, which is what the journal counts, is therefore lower, roughly 9,250.

## Per-section word counts (`wc -w`, headings included)

| Section | Before | After |
|---|---|---|
| Title block | 35 | 35 |
| Abstract + keywords | 315 | 266 |
| 1. Introduction | 279 | 253 |
| 2. Method (heading) | 3 | 3 |
| 2.1 Atomic claims | 103 | 76 |
| 2.2 Placement | 61 | 61 |
| 2.3 Verdicts | 168 | 140 |
| 2.4 Contradiction records | 111 | 116 |
| 2.5 Encoding | 286 | 135 |
| 2.6 Frame failure | 117 | 102 |
| 3. The Reference Frame | 779 | 760 |
| 4. The Map (incl. Table 1) | 1,676 | 1,625 |
| 4.1 The pattern | 268 | 232 |
| 5. intro | 59 | 44 |
| C1 IIT | 445 | 369 |
| C2 GNW/CTM | 495 | 416 |
| C3 HOT | 388 | 325 |
| C4 PRM | 221 | 195 |
| C5 RPT | 335 | 281 |
| PP/FEP/REBUS | 256 | 234 |
| C6 AST/illusionism | 261 | 238 |
| C7 SMT | 250 | 227 |
| C8 IWMT | 181 | 171 |
| C9 ICT | 150 | 135 |
| C10 Biological naturalism | 258 | 223 |
| C11 Enactivism | 200 | 196 |
| 6. Figures (heading) | 3 | 3 |
| 6.1 Figure 1 | 74 | 74 |
| 6.2 Figure 2 | 322 | 104 |
| 6.3 Claim graph (incl. Table 2) | 828 | 558 |
| 7. Scope and Limits (incl. Table 3) | 785 | 646 |
| 8. Conclusion | 112 | 68 |
| Supplementary material | 33 | 33 |
| Declaration of AI use | 62 | 62 |
| Competing interests | 4 | 4 |
| References | 1,401 | 1,352 |
| **Total** | **11,324** | **9,762** |

## What was kept

- All table rows are kept (96 table lines before and after).
- All verdicts, all contradiction records C1–C11 with their Point, Evidence, Decider and Decides lines, and all rival claim IDs are kept.
- Nothing was added: no new claims, citations or facts.
- The title block, Supplementary material, Declaration of AI use and Competing interests are unchanged. The only exception is the version line, which now reads "Preprint, version 3".

## Cuts that removed more than one sentence (or a structural block)

- **§2.5: the claims-file-to-prediction-map correspondence list was removed.** It began "Where the two files encode the same claim, the correspondence is: F-P1, F-FM1, F-FM2 → A1; …" and ended "Claims without an entry appear in one file only." This was about 125 words of pure data. The claim IDs F-BIND1, F-EFF1, F-LLM1, F-P1, F-SRC2 and F-THR appeared only in this list, so they no longer appear in the paper. This list is not in either JSON file (checked). See "Unsure" below.
- **§6.2: the Figure 2 cell-data list was removed.** It began "Cell data (theory: row = verdict; unlisted cells empty; R0 formal model, …" and had 21 bullets. It was replaced by one sentence naming the three hatched FMT levels (substrate/cellular, closure, formal model), which keeps the Gruber (2026b) citation. Every rival verdict in that list is also in Table 1.
- **§6.3: the Table 2 identifier glossary was removed.** It began "Identifiers: IIT-1 (identity with intrinsic cause-effect structure), IIT-2 (Φ > 0 suffices), …" and ran about 260 words. Every identifier is defined in Table 1, and the text now says the nodes use "the identifiers given there". Also removed: "Every X in Table 1 has a contradiction row; the record column gives its entry in Section 5." and "Each contradiction edge carries a link to its record in Section 5." Both repeat the Table 2 caption.
- **§5, all records: the *Status.* lines were removed.** Each one duplicated the Status column of Table 3. §2.4 now says the status "is given in Table 3". C1's "Linked: F-UNF1 …, node F10 …" is kept, as a *Linked.* line. Status detail that existed only in the records and is now gone:
  - C1: "in animal models" (the C1 Decides line still says "in the animal")
  - C4: "the conflict is narrow"
  - C5: "islands of awareness are inaccessible to report, and disconnected tissue may hold its own closed loop"
  - C7: "If verified MPE episodes show no self-modelling signature, Principle 3 is false." (this is also stated in the C7 Point and in §7)
  - C8: "no measure of experience"
- **§7 ledger: the numbered list "(1) IIT-1, (2) IIT-2, … (21) ENA-2. Twenty-one claims in eleven records." was removed.** It is replaced by "The ledger of contradicted claims holds twenty-one claims in eleven records (Table 3)." The sentences that follow still name all 21 claims by category.
- **§7, opening: removed "The verdicts are a single coder's, the author's, …"**, the sentence beginning "'Absorbed' means that FMT contains a claim …", and "GNW proponents, for example, would not accept …". Also removed: "A different reference frame would produce a different table; running the method with two frames …" and "The frame-failure checks of §2.6 have not been run." All of these repeat §2.3 and §2.6.
- **§8: removed "The agreements locate each theory on …"** and the count sentence beginning "Twenty-one contradicted claims are recorded in eleven records; …". The counts are kept in the abstract and §7.
- **§4.1:** removed "The verdicts fall into three groups." The seven one-sentence mechanism absorptions were merged into one list sentence. The five sufficiency sentences were merged into two, with the same content.
- **§5 intro:** "One constraint applies to every record that proposes removing closure. In a recurrent system, cutting a loop …" (three sentences) was shortened to one sentence that refers back to Section 3.
- **C1:** removed "silencing units that are already silent changes nothing on either theory", "and none where it does not" and "The second test bears on FMT's reply to the unfolding argument and does not measure experience." The sufficient-conjunction parenthetical, which repeats §3, was also dropped.
- **C2:** removed "and its proponents now present it as a multilevel model of conscious processing" (the citation was merged into the preceding one). Also removed: 'The two "converge on the structure and diverge on its role"', "That conflict needs an artificial implementation to decide; the CTM's AI blueprint (Yu et al., 2026) is discussed there" and "No-report paradigms separate the correlates of experience from those of report (Tsuchiya et al., 2015)."
- **C3:** removed "The higher-order representation is usually itself unconscious, so HOT does not require …; introspection is the case in which …" (Table 1 keeps "usually itself unconscious"). Also removed: "because transfer to long-term memory can fail as well" and "which have no higher-order representation" (the Point already says this).
- **C4:** removed "without which recall would be hallucination" and "which on PRM need not coincide with it".
- **C5:** removed "Recurrent non-linear dynamics host the second level (Principle 2), and", "On Principle 3, phenomenality is the modelling closed on itself", "which it allows for islands of awareness" and "On the question of local sufficiency the two theories conflict."
- **PP/FEP/REBUS:** removed "Markov blankets can be drawn around systems no theory counts as conscious (Bruineberg et al., 2022)". The N verdict for FEP is kept, but its stated rationale is gone.
- **C6:** removed "Tests of AST's attention-control predictions (Wilterson et al., 2020) test the mechanism FMT absorbs and leave the ontology untouched."
- **C9:** removed "so the test separates the architectures and leaves the phenomenal question open" (the Decides line says "architecture only").
- **C10:** removed "the conflict with FMT is over computation, not over biology as such" (Table 1 keeps "Searle allows non-biological systems with equivalent causal powers"). Also removed: "and that artificial consciousness is unlikely on current trajectories" and the sufficient-conjunction parenthetical.
- **§2.1:** removed "Two theories can share a mechanism and disagree on whether it is constitutive of experience; separating claims by type keeps …"
- **§2.3:** removed "A theory usually receives several verdicts, one per claim." and "The verdicts in this paper are a single coder's, the author's; no second coder has yet coded Table 1." The single-coder caveat is still in §2.6, the Figure 1 caption and §7.
- **§1:** removed "Every atomic claim of every other theory is placed on the component it is about and compared with …"
- **Table 1 caption:** removed "each A names the FMT claim (supplementary file) that contains it" (§2.3 says this) and "The fifth column records what the rival theory supplies that FMT lacks at the same component." (the column header says this).

## Reference entries removed as uncited

- Bruineberg, J., Dolega, K., Dewhurst, J., & Baltieri, M. (2022). The Emperor's new Markov blankets.
- Yu, H., Zhao, Y., Blum, L., Blum, M., & Liang, P.P. (2026). CTM-AI: A blueprint for general AI …

I checked every other entry by script, and each is still cited. The remaining entries are byte-identical to v2 (checked with diff).

## Small wording changes in kept sentences

- §3, third feature: "what closure buys a system" became "what closure gives a system", because "buys" is on the banned list.
- Some pairs of sentences were joined with a semicolon or relative clause, with no change of content:
  - Principle 1, on near-criticality
  - "not filled by a copy of stored content"
  - "The architecture, like free modelling, is necessary and not sufficient."
  - C6: "a 'small' illusionism in Graziano's (2024) term"
  - C7 (a)
  - C10, Searle
  - C2: "The conscious Turing machine … It also defines …"
- Table 1, Beautiful Loop cell: "Laukkonen et al. (2025) state the loop … so whether it meets that condition is not fixed by the source" became "the source states the loop … and does not fix whether it meets that condition". The verdict and meaning are unchanged.
- Component table, SI row: the parenthetical listing the conjunction was dropped, because it is spelled out in the paragraph above the table.
- §2.4 was rephrased to send status to Table 3. This section grew by 5 words.

## Unsure

1. **The correspondence list (§2.5).** It is data that exists nowhere else, because neither JSON file carries the cross-file mapping. I recommend adding it to `fmt-prediction-map.json` (or a small supplementary table) before submission. Putting it back in the paper costs about 125 words, which would take the total to about 9,890.
2. **Dropping the *Status.* lines.** This changes the record format from §2.4. Status now lives only in Table 3. If you want them back, they cost about 60 words. The cheapest offset would be the Gurnee et al. evidence sentence plus its reference, which together save about 80 words.
3. **Figure 2 cell data.** This assumes the figure image is the deliverable. If the list is needed as alt text or for regenerating the figure, v2 still has it.
4. **The FEP N rationale (Bruineberg) and the CTM blueprint pointer (Yu et al.)** are gone. Both are pointers rather than arguments, but reviewers sometimes look for them.
