# AIW-108 — DE edition ("Die Simulation namens Ich"): final QA pass (S255, 2026-07-11)

**Purpose (MG, S255):** LAST-LINE hidden-defect sweep of the PUBLISHED ed.2 German manuscript — NOT a theory revision. 5× `claude-fable-5` over disjoint ranges (all self-ID confirmed, gate open), each given (a) the QA hunt, (b) a German-native-quality axis (Anglizismen/Kalke — the port's known risk), (c) the matching EN findings as a cross-check. FLAG-ONLY. **Nothing falsified → "keine ist widerlegt worden" stands.** No reviewer failed; no split needed.

Line numbers are DE-manuscript-absolute.

---

## HIGH — fix before any reprint

| Location | Issue | Fix |
|---|---|---|
| Kap.13 L1225 "Libet bewies das **1979**" **+ reference list L1891** ("Libet (1979, 1985)", omits 1983) | Wrong date — the readiness-potential study is **Libet, Gleason, Wright & Pearl 1983** (*Brain*). Worse than EN: the DE reference list also lacks 1983. | Body → **1983**; add 1983 to the Kap.13 references. |
| Kap.13 L1231 "einen Computer mit **zwei Mäusen** … Die Maus des Probanden war verborgen" | Garbled **and self-contradicting**: the DE appendix (L1891) correctly names it "das **‚I Spy'-Maus-Experiment**" (Wegner & Wheatley 1999) = one shared planchette-mouse + auditory priming. Body and appendix describe two different experiments. | Rewrite L1231–1233 to the single shared-mouse + auditory-priming "I Spy" paradigm. |
| Kap.6 L635 "die stärkste psychedelische Substanz **auf der Erde**" | Missing the load-bearing qualifier ("soweit bekannt" doesn't repair it). Salvinorin A = most potent *naturally occurring* hallucinogen; LSD stronger by mass. | → "die stärkste **natürlich vorkommende** psychedelische Substanz". |
| Anhang B L2062 "Meine eigene Kindheitserfahrung — … — **Alle drei Komponenten funktionieren einwandfrei.**" | **Ungrammatical subjectless sentence** (editing artifact): subject has no predicate; a fresh capitalized clause starts after the dash. Also a tense break (past anecdote → present). | Rejoin into one sentence, e.g. "In meiner … Kindheitserfahrung — … — funktionierten alle drei Komponenten einwandfrei; der Kreislauf stagnierte trotzdem…". |
| Anhang F L2296 "…und **Unitarität eine Konsequenz der Bekenstein-Grenze**." | Non-standard/reversed physics stated flatly as fact, in an appendix that explicitly hedges its *other* speculative step (L2300 "Was jetzt kommt, ist spekulativ… Einen Beweis habe ich nicht"). | Hedge to match: "…was in diesem Modell als Konsequenz der Bekenstein-Grenze gedeutet wird". |
| Kap.4 L269 `<!-- FUTURE: Color edition figure … SDXL prompt preserved in git history -->` | Leftover editorial HTML comment ported into the shipped German file (same defect as EN). | Delete. |
| Typography (whole book) | German opening „ (63×) paired with **ASCII straight " closings** in ~60+ places (only ONE correct closing " in R1's range, hand-set) + parenthetical **em-dashes (63×, English convention) mixed with en-dashes (96×)**. Systematic English-port artifact; fragile through the LaTeX build. | Normalize all closings to " and all parenthetical dashes to spaced en-dash (Duden Halbgeviertstrich) — or verify the build already fixes it. |

## MED — verify / fix

| Location | Issue |
|---|---|
| Kap.9 L830 "trennten **sie** chirurgisch das Corpus callosum" | Attributes the callosotomy *surgery* to Sperry/Gazzaniga (they studied the patients; neurosurgeons operated). Recast so surgeons cut, S&G studied. *(Likely also in EN.)* |
| Kap.5 L519 vs 479/509 | Internal contradiction on seizure direction vs criticality: L519 places seizures purely *above* criticality; L479 says the criticality measure *crashes* (down); L509 says either. Harmonize. *(Likely also in EN.)* |
| Kap.5 L521 vs 513 | "Zwei Jahrzehnte auseinander im Ursprung" — the two research paths originate ~2003/2005 (≈2 yrs apart); two decades is origin→2025 convergence, not the gap between origins. *(Likely also in EN.)* |
| Kap.5 L611 "Kokain, Methamphetamin und Alkohol zerstören Neuronen physisch" | Overstated for cocaine (harm chiefly ischemic/vascular). Split cocaine out. |
| Kap.12 L1105 "**partielle** Konnektome der Fruchtfliege" | Dated — complete adult *Drosophila* connectome (FlyWire ~140k) published 2024; correcting *strengthens* the passage. |
| Kap.13 L1223 "etwa **20 Hz**" vs L1253 "höchstens etwa **5 Hz**" | Two unreconciled conscious-rate figures (appendix canonizes only 40/20 Hz → the 5 Hz floats free). Distinguish refresh vs decision cadence. |
| Kap.10 L996 "**Basales Bewusstsein**" vs L917 "**einfaches Bewusstsein**" | The four-level ladder's bottom rung is relabeled between the ladder and the developmental bullets; also full-EWM (L917) vs rudimentary-EWM (L996). Use one name. |
| Anhang C L2096 vs 2147/2151 | Rule 30 called "rechnerisch irreduzibel" (2096) but the final taxonomy table places it as a compressible Class-3 fractal ("Reduzierbar: Ja"). Unsignaled → reads as contradiction. *(Check EN Appendix C too.)* |
| Anmerkungen Kap.7 L1879 "**Schartner et al. (2015)** zur Ketamin-Entropie" | Likely wrong year — the increased-entropy/signal-diversity finding is Schartner et al. **2017** (*Sci Rep*); 2015 (*PLoS ONE*) is *decreased* complexity under anaesthesia. Verify vs references.md. *(Check EN too.)* |
| Anhang B L1990 "über ein **Lebensalter** hinweg" | Lexical error — "Lebensalter" = a person's age, not a lifespan. Calque of "over a lifetime". → "Lebensspanne". |
| Kap.9 L886 "steht im **Anhang**" | Vague vs the book's precise "Anhang H" (L1041) elsewhere → name it. |
| Kap.13 L1215 (Leibniz' Gesetz) + L1287 (clock/Chalmers) | Zombie argument made twice in Kap.13 with no link (contrast: Leibniz *is* back-referenced at L1764). Add a back-ref at L1287. |
| Kap.16/17 L1788 (#4) + L1792 (#5) | Both "worst" objections reduce to "Gödel-from-within"; #5 framed as categorically separate. Differentiate or acknowledge. |
| Kap.15 L1423 bold "selbstorganisierte Kritikalität" + full Per-Bak-1987 sandpile | Re-taught as if new though SOC named in Kap.5 (L513) and sandpile used there (L463/471). Add "wie in Kapitel 5 … bereits angeklungen". (Per Bak 1987 date correct.) |
| Kap.16 L1471… "informationsundurch**lässig**" vs L1656… "informationsundurch**sichtig**" | Boundary-term drift (impermeable vs opaque — different senses) for the same element; master list says *undurchlässig*, recaps say *undurchsichtig*. Standardize. |
| Kap.14 L1372 "**komputationale** Universalität" | One-off Latinism/Anglizismus — the ONLY occurrence book-wide (elsewhere "rechnerisch"/"universelle Berechnung"). → "rechnerische Universalität". |
| Anhang B L2030/2056/2058 "**du**/**dein**" | Register break — the book uses impersonal "man"; these passages switch to informal "du". Convert for consistency. |
| Anmerkungen L1891→1893 | Notes jump **Kap.13 → Kap.15**; no Kapitel-14 note (every other chapter has one). Confirm Kap.14 needs none, else add it. |

## MED — age (MG directive)
- **Coda L1822 "Nur — ich bin fünfzig."** MG: any hard age is correct for <1 year → self-dates the book; also factually off (born 1978 → 47/48 in 2026). Reword age-robust ("fast ein halbes Jahrhundert" / drop the number).

## LOW — German-native quality (Anglizismen / Kalke / translationese)
Speicherdump→Speicherabzug (L1277); Lock-in→Einrasten (L1317); Roh-Feed→Rohsignal (L1237); Pipeline→Verarbeitungsweg (L1235); Konstruktor→Konstrukteur (Coda L1820/1822); dimmen→drosseln (L2058); "gibt den Punkt zu"→"räumt … ein" (L2018); Forschungswissenschaftler→Wissenschaftler (L2006); "schließt sich der Kreis **zurück**" redundant (L2022); "der gruselige Teil"→"das Beängstigende" (L1826); Drittperson-Perspektive→"dritte Person" (L2024); "Frames"→Einzelbilder (L491); Grafik-Engine (L501); "adversarialer"→adversariell (L121); "Neuverkabeln/verkabeln"→umverdrahten (L285/287); "aus Fenstern gelaufen" (L635); "befriedigenden Zustand" (L489); "Border-Ownership" ungloss'd (L576); "Vor-Stall-Rand" clunky (L475); "Darwin's Arch" English genitive → "Darwins" (L893); English gerund headers Forking/Cloning/… (L279–285). **Citation diacritics:** L1891 "Kuhn"→**Kühn** (Simone — confusion risk with Thomas Kuhn!); L1897 "Berut"→**Bérut**. *(Diacritics likely also in EN references.)*

## LOW — other factual / coherence
- Malformed URL L1865 "github.com/JeltzProstetnic/aIware/references.md" → 404s (needs `/blob/main/` or repo root). *(Check EN.)*
- L1867 "IIT als Pseudowissenschaft … in **Nature Neuroscience (2025)**" — the pseudoscience letter circulated 2023; verify venue/year. (COGITATE "Nature 2025" in the same note is correct.) *(Check EN.)*
- Anhang A L1935/1943: hierarchy called "ventraler Strom" but table includes **V5/MT** (dorsal/motion). Note as dorsal or call it a general hierarchy.
- Kap.1 L115 "Bankomatkartenchip … gewisses Bewusstsein" — passive smartcard ≈ Φ0; softens the IIT→panpsychism point.
- Kap.2 L238 "drei oder vier" vs L240 "drei" cortical layers — harmonize (reptilian dorsal cortex = three-layered).
- Kap.5 L501 "das **Permeabilitätsleck**" (Kap.5) precedes the Kap.6 "Permeabilitätsgradient" intro — forward-dependency + term drift (Leck/Gradient/Barriere/Grenze). *(Same as EN.)*
- Kap.2 L145 "ein altes Prinzip … wenn wir zu den Tieren kommen" — the "animals" principle is never explicitly named where animals are reached; verify payoff.
- Kap.9 L927 "aus Kapitel 1 schuldig geblieben" — confirm Kap.1 actually plants the Copernican-principle debt.
- Kap.10 L933 Kanzi anecdotes (sister's ice; requested private dance performance) presented as fact — verify or soften to reported speech.

## Structural — ed.3 (already logged; confirmed)
- **Coda L1824–1828:** avalanche / knockout / 4-D-fractal near-death episodes re-narrated **at full length** (only the avalanche cites its source chapter) → compress to callbacks.
- **Kap.15 L1423:** SOC + Per Bak sandpile re-taught in full → trim to a callback.
- **2015-book self-ref (Kap.17 L1802/1816):** DE reads coherently (the 2015 book was itself German) — **no fix needed**; only the minor age/date wobble (age 25 ≈ 2003 vs "um 2005") noted.

## Prose tics (thin for ed.3)
- Reveal-hook "…was einem den Schlaf rauben sollte / einen quälen sollte / zu denken geben sollte" ~6× across Kap.9–12 → thin to 2–3.
- First-person extreme-sports "I" (orca freedive, Sidemount, paragliding, martial-arts KO, ice-hang) saturates Kap.9–12 → keep the strongest (orca, KO), trim the rest.
- "…ist keine Theorie — es ist eine **Religion**" aphorism 2× in-range (L1349, L1645) + template siblings ("…sondern eine Geschichte" L1039/2330) → vary one.
- Kap.5 L451/453/489 Game-of-Life "286er/als Kind/drei Regeln" told 3× → condense to one telling.
- Kap.5 L537≈539 duplicated math-beauty→reality hedge → state once.
- Kap.4 L368 digital-twin re-glossed as new (defined Kap.2 L182) → callback.

## Print / artifacts
- L269 leftover HTML comment (see HIGH).
- Kap.16 L1445 raw `$10^{-35}$` inline LaTeX vs glyph-avoidance elsewhere ("Phi" spelled out L1605/1607) → typeset superscript or spell out; **dollar-signs will show literally in a non-math pipeline.** *(Same as EN L1476.)*
- L176 empty figure alt text (`homunculi.de.png`) — add German alt.

---

## ⚠ Cross-edition — DE reviewers surfaced these, and they almost certainly exist in EN too (feed into AIW-109 ed.3 fixes for BOTH sources):
1. **Callosotomy surgery** misattributed to Sperry/Gazzaniga.
2. **Seizure-vs-criticality direction** contradiction (above vs below).
3. **"Two decades apart in origin"** timeline slip (paths originate ~2 yrs apart).
4. **Rule 30** "irreducible" vs Appendix-C taxonomy "compressible Class-3 fractal".
5. **Schartner (2015 → likely 2017)** ketamine-entropy citation.
6. **IIT-pseudoscience venue/year** ("Nature Neuroscience 2025" vs 2023 letter).
7. **Citation diacritics** (Kühn, Bérut) — check EN reference list.
8. **Malformed references.md GitHub URL.**

**Bottom line:** No BLOCKER for the existing ed.2 run. Reprint must-fixes: the **Libet 1983 date** (body + refs) and the **Wegner "I Spy" setup** (both also contradict/omit in the DE apparatus), the **subjectless Anhang-B sentence**, the **unhedged Bekenstein→unitarity claim**, the **"strongest psychedelic" qualifier**, the **leftover HTML comment**, and the **quote/dash typography** (a native German edition should not ship English straight-quotes + em-dashes). The German prose itself is idiomatic and strong — the residue is copy/coherence, a manageable calque list, and the shared-source factual items above.
