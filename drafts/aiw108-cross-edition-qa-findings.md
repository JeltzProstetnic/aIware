# AIW-108/109 — Cross-edition final QA findings (ALL 8 editions)

**Session S255, 2026-07-11.** Final "last-line" hidden-defect QA sweep of every published ed.2 manuscript. **41 Fable reviewers** (`claude-fable-5`, self-ID confirmed, no content-gate refusals), 5 per edition over disjoint ranges (EN also had a Ch.11+App-H probe). Purpose = catch defects that hid well; **NOT a theory revision** (nothing is falsified; crucible results are preliminary + positive). FLAG-ONLY — nothing was rewritten.

Per-edition detail files: `drafts/aiw108-en-fable-final-review.md`, `drafts/aiw108-de-fable-final-review.md`. This file is the **consolidated cross-edition work-list** for the fix session (AIW-109).

Editions & file: `pop-sci/book-manuscript{,-de,-es,-fr,-pt,-it,-ja,-zh}.md`. Line maps: EN/ES/PT/IT/JA = 2477 ln (parallel); ZH = 2479; DE = 2369; **FR = 2475 (−2 from Ch.7 on)**. Verify each line number in-file before editing (Kalk `count==1` discipline).

---

## ⚠ 0. VERIFY FIRST — before any fixing

1. **Suspect citations (Ch.5, ~L534 EN/ES/FR/PT/IT, DE L519, ZH L536, JA L534):** `Keith Hengen & Woodrow Shew, "140-dataset meta-analysis", Neuron (2025)` and `Inbal Algom & Oren Shriki, "ConCrit" framework, Neuroscience & Biobehavioral Reviews (2026)`. **Every reviewer flagged "Inbal Algom" + "ConCrit" as unverifiable / possibly non-existent** (Shriki, Hengen, Shew are real criticality researchers). A fabricated citation in a published book is serious. **WebSearch-verify all four (authors/journal/year/DOI); if unconfirmable → escalate to MG (remove or replace), do not silently "fix".**
2. **Kanzi anecdotes (Ch.10, ~L954):** sister's ice-cream + "requested a private dance performance", framed "well documented". Verify vs Savage-Rumbaugh corpus or hedge/cut.
3. **IIT-pseudoscience venue/year:** reviewers say the 124-signatory "IIT as pseudoscience" letter was **PsyArXiv, Sept 2023**, not "Nature Neuroscience (2025)". Confirm before rewriting (COGITATE "Nature 2025" in the same note IS correct — different item).
4. **Bach direct quotes (Ch.4, ~L418):** verify verbatim + that Bach *wrote* (vs said) them.

---

## 1. SOURCE-SHARED DEFECTS — fix in ALL editions

Line numbers per edition (✓ = confirmed present; "?" = not explicitly flagged in that edition's pass → CHECK). "NP" = reviewer confirmed not-present/already-clean.

### FACTUAL / CITATION (highest priority)

| # | Defect → fix | EN | DE | ES | FR | PT | IT | JA | ZH |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Libet "1979" → 1983** (Ch13 readiness-potential study = Libet, Gleason, Wright & Pearl 1983). DE **also** add 1983 to refs (list has "1979,1985"). | 1248 | 1225 +refs1891 | 1248 | 1246 | 1248 | 1248 | 1248 | 1250 |
| 2 | **Wegner "two mice" → "I Spy" (Wegner & Wheatley 1999): single shared mouse/planchette + auditory priming.** Full rewrite. DE body contradicts its own appendix ("I Spy" at 1891). | 1254 | 1231 | 1254 | 1252 | 1254 | 1254 | 1254 | 1256 |
| 3 | **Salvia "strongest psychedelic on Earth" → add "naturally occurring"** (Ch6; LSD stronger by mass). | 650 | 635 | 650 | 650 | 650 | 650 | 650 | 652 |
| 4 | **Fruit-fly "partial connectome" → complete adult FlyWire (~140k neurons, 2024)** (Ch12). | 1128 | 1105 | 1128 | 1126 | 1128 | 1128 | 1128 | 1130 |
| 5 | **Callosotomy: surgery misattributed to Sperry & Gazzaniga → surgeons (Vogel & Bogen) cut, S&G studied** (Ch9). | ? | 830 | 850 | 848 | 850 | 850 | 850 | 852 |
| 6 | **Wolfram "five classes" → four; 5th is the author's own extension** (Notes Ch15). Contradicts Appendix C. | ? | ? | 1926 | 1924 | 1926 | 1926 | 1926 | ? |
| 7 | **Schartner "(2015)" → 2017** ketamine entropy (Notes Ch7; 2015 = propofol paper). | ? | 1879 | 1912 | 1910 | 1912 | 1912 | 1912 | 1914 |
| 8 | **IIT-pseudoscience "Nature Neuroscience (2025)" → 2023 PsyArXiv letter** (Notes Ch1). IT: internal contradiction (body 2023 vs note 2025). | ? | ? | 1900 | 1898 | 1900 | 1900 vs body114 | 1900 | 1902 |
| 9 | **Anton's syndrome mis-assigned to ESM (self) → EWM/IWM (world)** (Ch6, contradicts Ch8). IT **also** ISM→EWM swap at L680. | ? | ? | ? | 672 | 672 | 672 +680 | ? | ? |
| 10 | **Hawking/Bekenstein "didn't read each other's papers" — FALSE + self-contradicts joint-credit** (Ch16/17). | ? | ? | ? | ? | 1782 | 1780/1782 | ? | ? |
| 11 | **Seizure above-vs-below criticality contradiction** (Ch5): "pushed beyond criticality" vs Class1/2 hypersynchrony. Reconcile to "either direction". JA = NP (clean). | ? | 519 | 524/534 | 534 | 534 | 534 | NP | 496/536 |
| 12 | **"Two decades apart in origin" → paths originate ~2 yr apart** (Ch5). | ? | 521 | 536 | 536 | 536 | 536 | 536 | 538 |
| 13 | **Bekenstein→unitarity claim stated flat → hedge** (Appendix F). | ~2335 | 2296 | 2335 | 2333 | 2335 | 2335 | 2335 | 2337 |
| 14 | **Rule 30 "irreducible" vs Class-3 "compressible" unsignaled contradiction** (Appendix C). | ? | ? | 2132/2183 | 2130/2181 | 2132/2183 | 2132/2183 | 2132/2183 | 2134/2185 |
| 15 | **Cocaine "physically destroys neurons" overstated** (Ch5; cocaine harm mainly vascular). | ✓ | ? | 626 | 626 | 626 | 626 | 626 | 628 |
| 16 | **Reptile cortical layers "three or four" vs "three"** (Ch2; breaks the 3→6 doubling). | ✓ | 238 | 238 | 238 | 238 | 238 | 238 | 238 |
| 17 | **Kühn (not Kuhn, = Simone Kühn) + Bérut (not Berut) diacritics** (Ch13 body + Notes). NB Thomas Kuhn stays unaccented. | ? | ? | 1252 | 1250 | 1252/1924/1930 | 1252/1924/1930 | ? | ? |

### CROSS-REF / COHERENCE / PROSE (mostly ed.3, but cheap)

| # | Defect → fix | Notes |
|---|---|---|
| 18 | **"20 Hz" vs "5 Hz" conscious-rate unreconciled** (Ch13). Add a clause (refresh vs decision rate). | all editions (~L1246 vs 1276) |
| 19 | **"Three relationships" attributed to Ch5 vs "last chapter"=Ch14** (Ch14/15). Harmonize. | EN/ES/FR/PT/IT/JA (~1380 vs 1422); DE=NP; ZH ✓ |
| 20 | **Per Bak 1987 sandpile re-taught in Ch15 → callback to Ch5** (ed.3). | all (~L1454) |
| 21 | **Zombie argument twice in Ch13 (Leibniz + clock) no back-ref.** | all (~L1238 & 1310) |
| 22 | **Weak points #4 & #5 both reduce to "Gödel-from-within"** (Ch16/17). Differentiate. | all (~L1820/1822) |
| 23 | **Raw LaTeX `$10^{-35}$` vs glyph-avoidance** (Ch15/16). EPUB-visible → typeset "10⁻³⁵" or spell out. | all (~L1476; DE 1445; PT in Ch15) |
| 24 | **Boundary-term drift: impermeable vs opaque** (Ch15-17). Standardize. | all |
| 25 | **"permeability leak" used definite before "permeability gradient" introduced** (Ch5→6). | all (~L516→566) |
| 26 | **Duplicated beauty→reality hedge, adjacent paragraphs** (Ch5). Cut one. | all (~L552/554) |
| 27 | **Game of Life "three rules" (canonically 3–4)** (Ch5). | all (~L466/468/504) |
| 28 | **Vague cross-refs "clinical chapter"/"the appendix" → name Ch8 / App H** (Ch9). | all (~L892/906) |
| 29 | **Hive/collective foreshadow ("into the hive") no Ch10 payoff** (Ch9). Add beat or drop. | all (~L908) |
| 30 | **Extreme-sports anecdote density across Ch9-12** (ed.3, thin). | all |
| 31 | **salvia "proprioceptive input overwhelms" dubious mechanism** (Ch3). Hedge. | all (~L286) |
| 32 | **"that never happens" absolute (daily neuron loss)** (Ch3). Soften. | all (~L322) |
| 33 | **"one principle for animals" foreshadow payoff unclear** (Ch2→Ch10). Verify/name. | all (~L140) |
| 34 | **Missing Chapter 14 note (Notes jump 13→15)** (Notes). | all (~L1924/1926) |
| 35 | **Coda re-narrates avalanche/knockout/4-D-fractal at FULL length → callbacks** (ed.3). | all (~L1854-1862) |
| 36 | **"the German book's analysis" self-ref** (Ch8, ~L828) — MG: keep or make edition-neutral. | EN/ES/FR/PT/IT ✓; DE reads OK; JA「ドイツ語版」opaque |

### ARTIFACTS (delete / repair)

| # | Defect | Where |
|---|---|---|
| 37 | **Leftover HTML comment `<!-- FUTURE: Color edition figure … SDXL prompt… -->`** → delete. | EN 272, DE 269, ES 272, FR 272, PT 272, IT 272, JA 272, ZH 272 |
| 38 | **Leaked build chunk-marker `<!-- chunk … | EN lines … -->`** → delete. | ZH L384 (only edition; others confirmed clean — re-grep all) |
| 39 | **Un-localized figures** (`homunculi.en.png`, `figure1/figure2-…-bw` with English labels; German `-de` variants exist, no other language). Needs localized figure assets per language (or confirm label-neutral). | ES (homunculi+fig1+fig2), FR (homunculi), PT (**all 3 = BLOCKER**), IT (homunculi+fig1+fig2). Check JA/ZH. |
| 40 | **GitHub references.md URL malformed** (missing `/blob/main/`) (Notes header). | ES 1898, FR 1896, PT 1898, IT 1898, JA 1898; check EN/DE/ZH |
| 41 | **Bruno J. Gruber acknowledgment "the life he spent in physics" → present/active phrasing (HE IS ALIVE)** (Ringraziamenti). HARD constraint. | ES 1886, FR 1884, PT 1886, IT 1886, JA 1886, ZH 1886; check EN/DE |
| 42 | **Author age "I'm fifty" → reword age-robust (drop the number)** (Coda). MG directive; also factually off (b.1978→~48). | EN 1854, DE 1822, ES 1854, FR 1852, PT 1854, IT 1854, JA 1854, ZH 1856 |
| 43 | **TOC/Indice-vs-heading TITLE mismatches** (word-level, not separators). | IT (6: Sull'autore, Cap6, Cap7, AppA, AppF, AppH), PT (4: Cap4, Cap9, Cap12, AppF), JA (many: AppA/B/D/E/F/G + Ch6/Ch14 + 付録G broken xref「あらゆるものの建築」); check EN/DE/ES/FR/ZH |

---

## 2. EDITION-SPECIFIC DEFECTS (highlights; see per-edition detail)

**EN** (source; cleanest): aphorism "isn't a theory — it's a religion/sales pitch" ×3 (L1374/1676/1728, keep one); "automatons"→"automata" (L1668); ketamine-vs-criticality robustness (App H); "not X—it's Y" cadence density; anti-metaphor hammer ×5-6. **CHECK in EN the "?" rows above (5,6,7,8,9,10,11,12,14,17,40,41,43).**

**DE** — 🔴 **typography**: German „ openings paired with **ASCII straight " closings** (~60×) + em-dash(63)/en-dash(96) mix → normalize. Subjectless sentence Anhang B L2062 (editing artifact). Calques: Speicherdump(1277), Lock-in(1317), Konstruktor→Konstrukteur(1820), dimmen(2058), "Lebensalter"→Lebensspanne(1990), "komputationale Universalität"(1372), du/man register break Anhang B(2030+). "einfaches"/"Basales Bewusstsein" naming (996 vs 917).

**ZH** — 🔴 **预测/预言 split** (TOC L44 预测 vs 付録H heading L2369 预言 + 预言 in Ch11 L1148; unify → 预测). **模拟/仿真** core-term split (Ch2 vs rest → 模拟). **表现/效能/性能** performance-term (formulas literally disagree L1934 vs 2095 → unify 表现). Salvia mistranslations: 丹参属→鼠尾草属(L638), 丹酚素A→correct salvinorin(672), 萨尔维亚草(820). Name romanization inconsistency. Garbled duplicated sentence L206. 通透性/可透过性/通透度 split. Bruno 度过的一生(1886).

**ES** — **TID→DID→TID** acronym flip (896/898/900). **"el 36 de agosto"** German calque for "never"(960) → "el 30 de febrero"/Spanish idiom. **Comma-thousands** "85,000" reads as 85.0 in neutral ES (L1182) + "300,000"(1468). "Lo que deja"→"Lo cual deja"(668). operacional/operativo(2007 vs 2041). NDE→ECM(1340). Spaced em-dash isolated to Cap4.

**JA** — **Heading-separator inconsistency** (：/full-width　/**half-width ASCII space** at Ch2 L146 & Ch17 L1722 = errors). Substrate **基盤/基体/基質** split. サイケデリック/**サイケデリックス** seam (病態失認 section). PCI 指標/指数. Doubled particles: 「まではは」L1406, 「結局のところ結局は」L1772 (typos). Bekenstein katakana ベッケンシュタイン/ベケンシュタイン. 付録G broken xref「あらゆるものの建築」→「万物のアーキテクチャ」. 形状定数→形態定数(2385). Half-width parens App H (2393/2397/2399/2411). 「ドイツ語版」self-ref.

**FR** — 🔴 **L1088 raw English editor note left in text** (`vary one instance, e.g...` placeholder — BLOCKER). 🔴 **L636 garbled merged sentence** ("C'est Le plus spectaculaire est la salvia" — BLOCKER). 🔴 **L554 unbalanced markdown italic** (unclosed `*` → PDF corruption). L114 "que qu'une". L236 broken correlative. L1622 broken sentence ("principe holographique, née… et est devenu"). L966 garbled fragment. **"le 36 août"**(958)→"à la Saint-Glinglin". orque gender switch(912 vs 916). Blindsight/vision aveugle. PCI EN/FR. Feynman "70 years"→~77(1606). All-caps emphasis→italics(1762/1766).

**PT** — 🔴 **L518 corrupted paragraph** (orphaned ellipsis fragments, partly unreadable — BLOCKER). 🔴 **All figures English-labelled** (fig1/fig2/homunculi — BLOCKER, no -pt). **L1326 meaning-inversion** ("decidido por você" = opposite of the free-will thesis — HIGH). L2027 garbled compound-interest sentence. "auto**o**rganizada"→"auto-organizada" (6+ hits). "que que"(820). "E igual a I" garden-path(1782). "no dia 36 de agosto"(960)→PT idiom. sálvia accent drift.

**IT** — **Anton ISM→EWM** double swap (672 + **680** ISM→ESM-not-EWM). **Hawking/Bekenstein** "non leggevano gli articoli"(1780/1782). **IIT year** body2023 vs note2025 contradiction. **sapere/conoscenza** knowledge-term split (formula L2093 ≠ definition L2007). **previsione/predizione** split (Ch11 vs App H). L1518 dangling "E sono più strane". "monotòno"→monotono accent(2164). ASCII quotes in App E→«». "sperimentare una mela" calque(156). "in piedi" vs lying-down(356). hard disk/disco rigido(176). insect-consciousness contradiction(966 vs 976). IT localized "never"(30 febbraio) + no free-will inversion = clean there.

---

## 3. ed.3 STYLE REFINEMENTS (NOT errors — MG decides, don't auto-apply)
Coda compression (#35), Per Bak callback (#20), aphorism-thinning, anti-metaphor density, extreme-sports density (#30), "German book" self-ref (#36), "not X—it's Y" cadence, em-dash density. These are polish; separate from the factual/artifact must-fixes.

---

## 4. Method for the fix session (AIW-109)
1. Do §0 verifications first (WebSearch citations; escalate fabrications to MG).
2. Source-shared factual/artifact fixes (§1 #1–17, #37–43): fix in **all 8** editions. Many are mechanical (dates, diacritics, comment deletion, URL). Wegner (#2), callosotomy (#5), Anton (#9), Hawking/Bekenstein (#10) need careful accurate rewrites — do EN first, then translate the fix per language.
3. Per-edition artifacts/BLOCKERs (§2): FR L1088/L636/L554, PT L518/figures — priority.
4. Localized figure assets (#39) — generate `-es/-fr/-pt/-it/(ja/zh)` variants or confirm label-neutral.
5. Use verified find→replace pairs, `count==1` per file, never parallel-write the same file (S254/decisions.md method). Update EN/DE `.md` first for source-level items, then re-propagate.
6. After fixes: rebuild interiors/eBooks → KDP re-upload (AIW-109). Translations still need per-language human-native gate before KDP-publish (AIW-108).
