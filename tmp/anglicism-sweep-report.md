# German Anglicism Sweep Report — 2026-04-14

Scope: `pop-sci/book-manuscript-de.md`, lines 67-974 (Kapitel 1 through Kapitel 10).
Excluded from review (intentional): Forking, Cloning, Crashing, Patchwork, Split-Brain, K-Hole, Phosphene, K.o., fMRI/MEG/EEG, V1/V2/V3, FMT introduction in Kap. 1, figure alt-text.

## HIGH CONFIDENCE (clearly broken German or direct English calques)

- Line 595: `elektrochemischen Level`, `proteomischen Level`, `topologische Level`, `virtuelle Level`, `einzige Level`, `elektrochemische Level`, `weitere Level`, and the compound `Fünf-Level-Hierarchie` | Problem: Kapitel 2 (lines 178-200) introduces this hierarchy with the German term **"Ebene"** ("Physikalisch / Elektrochemisch / Proteomisch / Topologisch / Virtuell" plus "Fünf-Ebenen-Hierarchie"). Line 595 then switches to the English loan "Level" eight times in one paragraph, breaking terminology consistency inside the same manuscript. This is exactly the kind of anglicism the sweep targets. | Suggestion: Replace every "Level" with "Ebene" and "Fünf-Level-Hierarchie" with "Fünf-Ebenen-Hierarchie".

- Line 386: `Erfahrung ist das, was Vier-Modell-Selbstsimulation bei Kritikalität (Criticality) *ist*` | Problem: Parenthetical English gloss "(Criticality)" after an already-established German term. "Kritikalität" has been used since Kapitel 5 without a gloss; reintroducing the English here is pure calque. | Suggestion: Delete "(Criticality)" — "bei Kritikalität" is sufficient.

- Line 897: `Das ist das Explizite Selbstmodell (Explicit Self Model, ESM), das aus der Dritte-Person-Perspektive arbeitet` | Problem: ESM was introduced in Kapitel 2 as "Explizites Selbstmodell (ESM)". Re-glossing with the English name "(Explicit Self Model, ESM)" in Kapitel 10 is redundant and inserts English where not needed. | Suggestion: `Das ist das Explizite Selbstmodell (ESM), das …`

- Line 909: `Das Explizite Weltmodell (Explicit World Model, EWM) der Fledermaus` | Problem: Same pattern as line 897 — EWM was introduced in Kapitel 2; the English gloss is unwarranted. | Suggestion: `Das Explizite Weltmodell (EWM) der Fledermaus …`

- Lines 469, 471, 473, 475, 477, 479, 481, 483, 485, 491, 495, 497, 499, 503, 505, 507, 509, 511, 515, 519, 521, 523, 525, 535, 539, 541, 543, 545, 551, 553, 555, 559, 567, 569, 571, 575, 577, 589, 591, 593 (and many more in Kap. 5-6) | Problem: Systematic typography bug — en-dash used as parenthetical dash with a leading space but **no trailing space** (e.g., `Substrat –das physikalische System`, `Paradebeispiel –derselbe Zelluläre Automat`, `Wer weiter zuschaut –nicht konzentriert`, `Zellulären Automaten –nicht metaphorisch`). Not strictly an anglicism, but it is a punctuation import / copy-paste artifact that will render as broken dashes in the final PDF and is concentrated in Kap. 5-6. | Suggestion: Global fix — every ` –` followed by a non-space character should become ` – ` (space before **and** after). Forty-plus occurrences; safest to run a regex pass: `s/ –([A-Za-zÄÖÜäöü])/ – \1/g`.

- Line 402: `Phänomenalität ist kein Zusatzfeature von Bewusstsein.` | Problem: "Zusatzfeature" — English "feature" glued onto German "Zusatz". Pure anglicism where natural German exists. | Suggestion: "kein Zusatzmerkmal", "keine optionale Eigenschaft", or "kein nachträglich angesetztes Extra".

## MEDIUM CONFIDENCE (awkward, may be intentional)

- Line 481: `periodische Oszillationen für Timing und Taktung (Alpha-, Theta-, Gammarhythmen)` | Problem: "Timing und Taktung" is redundant — "Taktung" already means timing/clocking in German. "Timing" here is a bare English loan stacked next to its German translation. | Suggestion: Drop "Timing und" → `periodische Oszillationen für Taktung und Rhythmik (…)`. Intentional only if the author wanted the doublet for emphasis — unlikely in a pop-sci book where the rest of the paragraph is clean German.

- Line 204: `Das Layout der eigenen Wohnung` | Problem: "Layout" is a bare anglicism. Natural German: "Grundriss" (for a floor plan) or "die Anordnung der eigenen Wohnung". | Suggestion: `Der Grundriss der eigenen Wohnung (im Dunkeln lässt sich darin navigieren)`. Could be argued as a colloquialism now naturalized in German; flagging as medium.

- Lines 281, 283, 289, 291 (Kapitel 3 opening): Sustained video-game analogy uses `Open-World-Spiel`, `Hardware`, `CPU`, `GPU`, `Transistor`, `Taktzyklen`, `Rendering-Prozess`. | Problem: Dense anglicism cluster. However, this is the explicit "video game on silicon" analogy that runs through the whole chapter, and the technical terms are the point. | Suggestion: Keep. Listed here only so the author can confirm the analogy is intentional and not a translation oversight.

- Line 787: `Top-Down-Vorhersagen` (Charles-Bonnet-Syndrom section) | Problem: "Top-down" is borderline jargon. Standard neuroscience German does use "Top-down" in technical writing, but in a pop-sci context the established German "absteigende Vorhersagen" or "rückläufige Vorhersagen" would read more fluently. | Suggestion: Leave if targeted at neuroscience readers; replace for general audience.

- Line 440: `die **Grafik-Engine** bleibt fast immer unsichtbar. Der **Quellcode** zeigt sich fast nie. Der **Rendering-Prozess** …` | Problem: Same video-game analogy cluster as Kap. 3. "Grafik-Engine" and "Rendering-Prozess" are directly borrowed English. | Suggestion: Keep — the analogy depends on these technical terms. Flagged for author awareness only.

- Line 719: Table cell `Kritisch/überkritisch` in the Bewusstseins-Karte row for Psychedelika | Problem: Not an anglicism, but a parallel to the original "Bei kritisch" bug from Session 183 — inconsistent adjective vs. noun forms across table rows. Row 1 uses "Kritisch" (adjective), row 5 "Über kritisch", row 6 "Kritisch/überkritisch", row 7 "Nahe-kritisch, Schwelle überschritten". | Suggestion: Consider normalizing the column to all-nominal ("Kritikalität", "Nahe Kritikalität", "Subkritisch", "Superkritisch", …) or all-adjectival for internal consistency. Not a high-confidence bug but would improve the table.

## LOW CONFIDENCE / STYLE CHOICE (flag, do not fix)

- Lines 73, 75, 77, 85, 87 … throughout Kap. 1-10: German quotation style uses `„` (U+201E, low-opening) but closes with ASCII `"` (U+0022) instead of `"` (U+201C, high-closing). | Problem: Not strictly wrong — many German books and the pandoc default use `„…"` — but strict German typography wants `„…"` with curly closing. | Suggestion: Either accept the pandoc-friendly mix or run a pass converting `"` after `„` to `"`. Purely cosmetic; the issue does not affect readability and is consistent throughout the entire 2310-line manuscript, so fixing only Kap. 1-10 would create inconsistency with Kap. 11+.

- Lines 315, 563, 567, 601, 603, 617, 627, 666, 674, 702, 715, 718, 747, 787, 950, 952, 972: the word `Input` used throughout. | Problem: Bare English "Input" where German has "Eingang", "Eingabe", "Eingangsdaten", "Reiz(strom)". This is used consistently as a term of art for sensory/signal input, paralleling "Output" on line 589. The book treats the brain as a computing system, so the English loan is arguably in register. | Suggestion: Style decision only. If the author wants fully German prose, a replace-all `Input → Eingang / Eingangssignal / Reizstrom` would work. Flagging as low-confidence because switching now risks creating inconsistencies with parts of the book (incl. Kap. 11+ and appendices) that also use "Input".

- Line 589: `erlebt man nur den fertigen Output` | Problem: Same as above — "Output" anglicism; German alternatives are "Ergebnis", "Ausgabe". | Suggestion: Group with the "Input" style decision above. Treat consistently or not at all.

- Lines 673-674: wiederkehrender Traum section, `nicht als Erinnerung an ein Gefühl, sondern als das Gefühl selbst` and `die implizite Kodierung`. | Problem: No anglicism; author's lyrical passage reads naturally. Flagging only to confirm nothing was missed. No action.

- Line 830: `Nur die Qualität des Inputs.` | Problem: Genitive of the English "Input". See Input style note above. | Suggestion: Group with general Input decision.

- Line 281: `Open-World-Spiel` | Style choice — this is how German game press uses the term. No action recommended.

## Summary

- Total flagged: 13 distinct findings (plus one systematic ~40-occurrence typography bug counted as a single item).
- High: 6 findings (Level/Ebene inconsistency, three stray English glosses, one en-dash pass, one "Zusatzfeature").
- Medium: 5 findings.
- Low / style: ~6 findings (quotation marks, Input/Output consistency, video-game analogy cluster).

### Recommended fix priority

1. **High-1 (Level → Ebene on line 595)** — this is the Session 183-equivalent miss: terminology drift inside the same manuscript that any German reader will catch immediately. One paragraph, ~8 substitutions.
2. **High-2 (en-dash spacing, Kap. 5-6)** — single global regex pass; ~40 occurrences; purely mechanical.
3. **High-3 (three English glosses on lines 386, 897, 909)** — three deletions, under one minute.
4. **High-4 (Zusatzfeature on line 402)** — one word.
5. **Medium items** — defer to author; would improve prose but none are wrong per se.
6. **Low / style items** — do not touch unless the author wants a consistency pass across the entire manuscript.

### Notes on what was *not* found

- No "Bei kritisch"-style literal preposition transfers in Kap. 1-10 (the Session 183 bug was isolated to the Bewusstseins-Karte; see Medium item above for a related cosmetic concern).
- No "in der Simulation running"-style broken German / verb hanging.
- No semicolon-as-comma misuse — all semicolons scanned (lines 95, 125, 162, 164, 210, 244, 276, 309, 396, 477, 497, 505, 559, 595, 623, 658, 704, plus a few more) correctly separate independent clauses.
- No weil-V2 or dangling-participle constructions detected.
- No article/case errors detected in the chapters scanned.
- No untranslated "state of the art", "random seed", "runtime" in prose.
