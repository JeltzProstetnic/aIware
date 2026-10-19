# Portuguese interior — Fable native-editor review (S259, 2026-07-13)

Full pt manuscript reviewed by 9 Fable agents vs the aligned EN source. High=fix before publish, Med=should fix, Low=polish. Fixes not yet applied.

---

# PT interior review — pt-01 (teaser + About the Author + Capítulos 1–2, lines 48–249)

| line | severity | issue | suggested fix |
|------|----------|-------|---------------|
| all (48–249) | Med | Typography: PT section uses only straight ASCII double quotes (`"`, 34 pairs, 0 curly) — identical to EN source. Sibling editions localized their quotes (DE `„…"`, ES/FR `«…»`), so the build pipeline does NOT auto-curl; PT will ship with straight quotes, contrary to this edition's curly `"…"` (U+201C/U+201D) convention. Systematic, not per-line. | Convert all straight `"…"` to curly `"…"` (U+201C/U+201D) throughout the PT manuscript, matching the edition's typographic convention. |
| 180 | Med | Register inconsistency: "Se isso **te** incomoda, por favor **leia**…" mixes the *tu* clitic ("te") with the *você* imperative ("leia") in one sentence. The rest of the book addresses the reader with *você* + *lhe/o* (e.g. line 50 "lhe contar", 64 "lhe entrega"). Lone *te* stands out. | "Se isso **o** incomoda, por favor leia…" (or "Se isso lhe causa incômodo, por favor leia…") to keep the *você/lhe/o* register. |
| 114 | Low | "cada uma delas uma **percepção** genuína envolvendo o mesmo centro ausente" — EN "each a real **insight** wrapped around the same missing center." "percepção" for *insight* collides with the book's central technical sense of *percepção* (perception); momentarily ambiguous in a book about perception. | "cada uma delas uma **intuição** genuína (ou: um insight genuíno) em torno do mesmo centro ausente." |
| 222 | Low | "sendo o modelo explícito do eu **quem** carrega o peso maior" — relative "quem" personifies a model (properly for persons); slight anthropomorphic slip. | "sendo o modelo explícito do eu **o que** carrega o peso maior" (or "…aquele que carrega…"). |

---

# PT interior review — pt-02 (Chapters 3–4, lines 250–451)

Reviewer: Fable native-Portuguese editor (neutral / Brazilian-leaning)
Scope: `pop-sci/book-manuscript-pt.md` L250–451 vs EN `pop-sci/book-manuscript.md` same range.

Overall: high-quality translation. Register, flow, and philosophical phrasing ("what it is like" → "como ser", "unaskable" → "não há como formulá-la") are handled idiomatically. FMT terminology is consistent: *Teoria dos Quatro Modelos*, *Modelo Explícito do Mundo/Eu* (EWM/ESM kept as canonical acronyms), *automodelo*, *Problema Difícil* (consistent capitalization), *beira do caos*, *criticalidade* (used consistently — not mixed with "criticidade"). Typography clean: curly quotes throughout, em dashes (—), correct accents, H₂O subscript preserved, Brazilian spellings (gêmeo, videogame, cetamina, assomatognosia). Numbers correct (3.000 with PT thousands separator; 10% / 50%). Only genuine issues below.

| # | Sev | Line(s) | EN | PT | Issue |
|---|-----|---------|----|----|-------|
| 1 | Med | 378 | "Recall the digital twin from Chapter 2." | "Pense num gêmeo digital (uma simulação de engenharia de um motor a jato)." | Cross-reference to Chapter 2 dropped and replaced with a parenthetical re-definition. Inconsistent with the rest of the section, which preserves every other chapter callback (L280/282 "Capítulo 9", L284/430 "Capítulo 6"). A PT reader loses the "same example you already met" signal. Suggest restoring: "Lembre-se do gêmeo digital do Capítulo 2 (a simulação…)." |
| 2 | Low | 380 | "Your brain does the same thing, but more so." | "Seu cérebro faz a mesma coisa, só que em escala maior." | Semantic shift: "but more so" = greater degree/intensity, not scale. "em escala maior" reads as size. Closer: "só que muito mais" / "só que de forma ainda mais acentuada". |
| 3 | Low | 416 | "…were uploaded into a monkey…" | "…fosse carregado em um macaco…" | "carregado" is a valid rendering of "upload" (fazer upload = carregar), but here it is ambiguous with "carregar" = to carry, so it can misread as "carried in a monkey" in a mind-upload context. Clearer: "transferido para um macaco" or "baixado num macaco". |

---

# PT interior review — pt-03 (Chapters 5–6, lines 452–691)

Reviewer: Fable native-Portuguese editor (neutral / Brazilian-leaning)
Scope: `pop-sci/book-manuscript-pt.md` lines 452–691 vs EN `pop-sci/book-manuscript.md` same range.

## Omission check (vs EN)
- Ch5 (Edge of Chaos): all paragraphs present — intro, two thresholds, ocean image, Two Dials, wing, seizure, Cortical Automaton, dark-room/synesthesia observation, Convergence (Beggs/Plenz, Carhart-Harris, Tagliazucchi, Hengen/Shew, Algom/Shriki), Three Ways a Hologram Meets an Automaton (all 3 relationships, 't Hooft). No drops.
- Ch6 (Psychedelics): permeability gradient, V1→higher table (7 rows, all intact), meditation/lucid-dreaming routes, Five Nested Systems (all 5 levels), Redirectable Self (salvia, 5 quotes, time dilation, Addy et al. 2015, thought experiment), Anosognosia. No drops.
- **Anosognosia opening symmetry paragraph (line 674) IS PRESENT** — the too-permeable/too-impermeable paragraph that FR dropped is intact in PT. No omission.

## Issues

| # | Sev | Line | EN | PT | Problem / Fix |
|---|-----|------|----|----|---------------|
| 1 | Med | 492 | "…or thrown into runaway chaos" | "…ou **lançado** num caos desenfreado" | Gender-agreement error. Subject is "a folha inteira" (fem.); "varrida" agrees but "lançado" does not. Fix → **lançada**. |
| 2 | Low | 474 | "empirical neuroscience was independently heading toward the same conclusion" | "a neurociência empírica caminhava**,** para a mesma conclusão de forma independente" | Stray comma splits verb from complement. Remove it: "caminhava para a mesma conclusão, de forma independente" (or drop entirely). |
| 3 | Low | 498 | "at 10 to 40 Hz" | "a 10 **ou** 40 Hz" | Range rendered as two discrete values. "ou" = "or"; should be a range → "de 10 a 40 Hz". |
| 4 | Low | 589 (table, V2) | "border ownership" | "propriedade de bordas" | Vision-science term "border ownership" rendered ambiguously ("propriedade" reads as property/ownership but is unclear here). Consider "pertencimento de bordas" or keep the English term. Minor. |

## Notes (not flagged — acceptable)
- Straight quotes used throughout ("ruído retiniano", "em criticalidade", etc.) — but the EN source uses straight quotes identically and consistently; curly conversion happens at build. No divergence from source.
- Em dashes (—) and accents correct throughout.
- FMT terminology consistent and correct: quatro modelos, modelo do eu/mundo (via EWM/ESM/IWM/ISM), beira do caos, problema difícil (n/a in this range), criticalidade / criticalidade auto-organizada, Teoria dos Quatro Modelos (FMT).
- Register/flow is fluent, natural, Brazilian-leaning idiom used well ("no mesmo balaio", "chuvisco de uma TV mal sintonizada", "dobrado feito um acordeão", "sem graça"). No calques/anglicisms of note.
- Numbers/facts verified: 2002 Wolfram, 286, 140 datasets/Neuron 2025, ConCrit 2026, 't Hooft (Nobel), 1998/1999, "oito anos completos", "quarenta e cinco segundos", Addy et al. 2015, décimo andar, serotonina 2A — all match EN.
- "EXTENSÃO"/"COMPLEXIDADE" caps in the Two-Dials section: stylistic emphasis (bold in EN), consistent internally — not an error.

---

# PT interior review — pt-04 (Capítulos 7–9)

Reviewer: Fable, native-Portuguese editor (neutral / Brazilian-leaning).
Scope: `pop-sci/book-manuscript-pt.md` lines 692–909 vs EN `pop-sci/book-manuscript.md` same range.
Verdict: no High-severity errors — no mistranslation, omission, or factual/number error. Names (Massimini, Vogel, Bogen, Sperry, Gazzaniga, Owen, Nagel, Parfit, Pinto, Reinders, Kubrick), dates (1960s, 2006, 1971, 2017, 2003), "Previsão 9", and all case-study content match EN faithfully. Findings below are terminological consistency and register nits.

| # | Line(s) | Severity | Type | Issue | Suggested fix |
|---|---------|----------|------|-------|---------------|
| 1 | 757, 760, 792, 814 (×2), 816 (×2) vs 708, 786, 840, 864, 898 | Med | Consistency / anglicism | Core FMT concept "input" is rendered two ways: **"input"** (kept in English — table rows, Cotard "o input interoceptivo", Anton "nenhum input visual", "quando o input está certo/errado") and **"entrada"** (elsewhere: "entrada sensorial/externa/visual", "qualidade da entrada"). A translated book should fix one term for this load-bearing concept. | Standardize on **"entrada"** throughout (or keep "input" everywhere) — recommend "entrada" for a book register; update the table cells to "entrada interna / entrada errada". |
| 2 | 700 vs 806 | Med | Cross-chapter term inconsistency | PCI's full name differs between the two chapters in scope: Ch7 keeps English **"O Perturbational Complexity Index (PCI)"**; Ch8 translates it to **"O Índice de Complexidade Perturbacional"**. Same measure, two names — a careful reader may not link them (only the acronym "PCI" ties them). | Pick one form and use it in both places (e.g. translate in both: "Índice de Complexidade Perturbacional (PCI)" at first mention in Ch7, then "PCI"). |
| 3 | 834 | Med | Term choice / FMT collision | Section heading **"Déjà-vu: o modelo que combina bem demais"** renders EN "template" as **"modelo"**, but the section body consistently uses **"molde"** / "memórias-molde". Beyond the head/body mismatch, "modelo" collides with the book's core FMT vocabulary ("os quatro modelos"), inviting confusion. | Change heading to **"o molde que combina bem demais"** to match the body and avoid the FMT-term clash. |
| 4 | 816 | Med | Flow / ambiguity | "…você se sente uma cadeira, **ou bem, quando você está paralisado**, ou morto quando está vivo." The comma-bracketed "ou bem," parses on first read as a discourse marker ("or rather / or well") instead of "or [feel] *fine* when paralyzed" (EN: "or fine when you're paralyzed"). | Rephrase, e.g. "…você se sente uma cadeira, ou **se sente bem** quando está paralisado, ou morto quando está vivo." |
| 5 | 694, 700, 706, 742, 806, 884 (passim) | Low | Glossary reconciliation | Manuscript uses **"criticalidade"** consistently; the review glossary lists the FMT term as **"criticidade"**. Note for the parent: "criticalidade" is the *standard* Portuguese physics term (cf. "criticalidade auto-organizada"), so the manuscript is likely correct and "criticidade" (severity sense) would be worse — flagging only so the project glossary is reconciled to the manuscript, not the reverse. | Keep "criticalidade"; align the glossary. |
| 6 | 748, 816 | Low | Missing accent / orthography | **"salvia"** (the plant/drug) is written without accent; the Portuguese common noun is **"sálvia"**. Acceptable only if deliberately treated as a drug-slang loanword — otherwise it is a missing accent inconsistent with PT orthography. | Decide: italicize as loanword *salvia*, or accent to **"sálvia"**; apply consistently in both occurrences. |
| 7 | 784 | Low | Term drift | Same paragraph uses **"pista de obstáculos"** and then **"percurso de obstáculos"** for EN "obstacle course". | Pick one ("percurso de obstáculos" reads best) and use it for both. |
| 8 | 818, 824 (lowercase) vs 826 | Low | Capitalization drift | "síndrome da mão alienígena" is lowercase in the heading/body but appears capitalized as **"Síndrome da Mão Alienígena"** at line 826. PT convention favors lowercase for syndrome names. | Lowercase at 826 for consistency: "pacientes com síndrome da mão alienígena". |
| 9 | 896, 898 vs 902 | Low | Term mixing | DID terminology alternates between **"alter" / "os alters"** (896, 898) and **"personalidade alternante"** (902) for EN "alter". Both are standard in PT DID literature, but mixing within one chapter reads inconsistently. | Choose one (recommend "alter", already glossed) and use it throughout Ch9. |
| 10 | 878 | Low | Nuance / hedge dropped | EN hedges: "the answer **leans toward** two." PT flattens to a firmer claim: **"A meu ver, a resposta é: duas."** Slightly stronger epistemic stance than the source. | Soften, e.g. "A meu ver, a resposta **pende para** duas." |
| 11 | 900 | Low | Prescriptive grammar | **"É preciso circunstâncias extraordinárias…"** — with a plural noun, strict grammar prefers **"São precisas circunstâncias extraordinárias…"** or **"É preciso haver circunstâncias…"**. The invariable "é preciso + plural noun" is informal. | "São precisas circunstâncias extraordinárias para bifurcar…" (or "É preciso haver…"). |

Notes (not defects):
- Quote typography: both PT and EN sources use straight `"` (0 curly), so curly-quote rendering is handled uniformly at build time — no PT-specific defect. Em dashes (—) present throughout, matching EN.
- Register: BR-style tratamento mixing (e.g. line 748 "te dá" alongside "você") is natural for the neutral/BR-leaning target and is not flagged.
- FMT model names ("Modelo Explícito/Implícito do Mundo/do Eu", "Teoria dos Quatro Modelos", acronyms EWM/ESM/IWM/ISM), "beira do caos"-family terms, "corpo caloso", "cérebro dividido", and Class-2/3/4 dynamics are all rendered consistently and correctly.

---

# PT interior review — pt-05 (Capítulos 10–12)

Reviewer: Fable native-PT editor pass (neutral / Brazilian-leaning).
Scope: `pop-sci/book-manuscript-pt.md` lines 910–1223 vs EN ref `pop-sci/book-manuscript.md` same range.
Verdict: **0 High, 4 Med, 4 Low.** Translation is accurate and fluent; all numbers/facts correct; no omissions. Issues are consistency/idiom, not meaning.

Typography note (no defect): the PT source uses straight ASCII quotes `"..."` throughout, exactly matching the EN source (0 curly in both files). This is the manuscript convention — curly conversion happens at build/LaTeX time — so it is NOT a PT-only typography error. Em dashes (—) and accents are correct.

FMT terms verified consistent except where noted below: *quatro modelos* ✓, *modelo do eu / automodelo* ✓, *modelo do mundo* ✓, *beira do caos* ✓, *criticalidade* ✓ (*problema difícil* not in range).

| Line(s) | Sev | Category | EN | PT | Issue / suggestion |
|---|---|---|---|---|---|
| 998 | Med | Coherence / humor | "hair loss" … "hairless" … "fur-covered" … "less hair" … "hairy" (EN uses one undifferentiated word) | "queda de cabelo" (head baldness) … "sem pelos" / "peludos" / "menos pelos" (body fur) | PT splits English "hair" into *cabelo* (head) vs *pelo* (body/fur). The setup is head-baldness (*queda de cabelo*) but the cold-by-the-fire logic and the amplified trait are body-fur (*sem pelos / menos pelos*). Referent mismatch weakens the joke's internal logic. Use *pelos* throughout (e.g. "sofria de perda de pelos" / "rarefação de pelos") for coherence. |
| 1020 | Med | FMT term consistency | "Simply extended consciousness comes online." | "A consciência **estendida simples** entra em cena." | The level term is rendered "simplesmente estendida/estendido" at 938 and 944 (canonical). Here word order flips and the adverb becomes an adjective → "estendida simples". Normalize to **"consciência simplesmente estendida"**. |
| 1060 | Med | Term consistency (glossary) | "The split-brain and dissociative-identity predictions" | "As previsões sobre **split-brain** e identidade dissociativa" | Lone untranslated "split-brain" — the book uses **"cérebro dividido"** in all 22 other occurrences (incl. line 1144 in this very chapter set). Change to "cérebro dividido". |
| 1106 | Med | Anglicism / verb semantics | "one that science fiction has been obsessing over for decades" | "um que a ficção científica **vem obcecando** há décadas" | *obcecar* is transitive = "to obsess/haunt someone"; here sci-fi is the subject and the relative *que* the object, so it reads "a side that sci-fi makes obsessed" — inverted from the intended "a side sci-fi is obsessed with". Fix: "com o qual a ficção científica vem se obcecando há décadas" or "que obceca a ficção científica há décadas" or "que fascina a ficção científica há décadas". |
| 942 | Low | Internal consistency | "a hall of mirrors, and it is, but it's a hall of mirrors you need…" | "um **labirinto de espelhos**, e de fato é, mas é um **salão de espelhos** de que você precisa…" | The repeated EN phrase "hall of mirrors" is rendered two different ways within a single sentence. Pick one (recommend "salão de espelhos" both, or "labirinto de espelhos" both). |
| 1018 / 1022 | Low | Typography (dash) | "6-12 months" / "3-4 years" (both hyphens) | "**6–12 meses**" (en dash) / "**3-4 anos**" (hyphen) | Numeric-range dashes inconsistent within the same list — 6–12 uses en dash, 3-4 uses hyphen. Make uniform (en dash for both, per PT range convention). |
| 1108 vs 1124/1210 · 1108 vs 1218 | Low | Phrasing consistency | "Mind uploading" / "Whole brain emulation" | "upload **de** mente" (1108) vs "upload **da** mente" (1124, 1210, 1216…); "emulação **do cérebro inteiro**" (1108) vs "emulação **total do cérebro**" (1218) | Two harmless but visible variants of the key phrases. Standardize (recommend "upload da mente" and "emulação total do cérebro"). |
| 958 | Low | Localization (informational) | "they'll find it on the 36th of August." | "eles vão encontrá-la **no dia de São Nunca**." | Idiomatic and correct (PT "never" idiom), but replaces the specific fake-date joke rather than translating it (e.g. "no dia 36 de agosto"). Acceptable editorial choice — flagged only so the author can confirm the localization is intended. |

---

# PT Interior Review — pt-06 (Capítulos 13–15, lines 1224–1519)

Reviewer: native-Portuguese editor pass (neutral/Brazilian-leaning), EN reference `pop-sci/book-manuscript.md` same range.
Overall: strong, idiomatic translation. All numbers, dates, and FMT core terms verified correct (Libet 550/200/350 ms, 40/20/10/5 Hz, Bak 1987, Nobel 1998, 93 bi anos-luz, 60 ordens, $10^{-35}$). Curly quotes and em dashes consistent. No High-severity issues.

| # | Sev | Line | Issue | Current PT | Suggestion |
|---|-----|------|-------|------------|------------|
| 1 | Med | 1280 | Ungrammatical stray comma splitting subject from verb | "…o seu próprio café — o que, passa longe do ponto de forma espetacular." | Delete the comma: "— o que passa espetacularmente longe do ponto." |
| 2 | Med | 1300 | Calque of EN "feel the same from the inside" — reflexive "se sentem iguais" reads as the states having feelings/being emotionally equal | "esses dois estados … se sentem iguais por dentro" | "por que esses dois estados … parecem o mesmo por dentro" / "produzem a mesma sensação por dentro" |
| 3 | Med | 1316 | Anglicism: "discutivelmente" for EN "arguably" — rare, stilted, and ambiguous (can read as "questionably") | "já que o 'nada' é discutivelmente uma abstração platônica" | "já que se pode argumentar que o 'nada' é uma abstração platônica" |
| 4 | Med | 1338 | English acronym "NDE" kept; PT standard is EQM (experiência de quase-morte); Ch13 (1298) already used "quase-morte" in Portuguese, so the acronym appears unglossed and inconsistent | "a mesma disparada que a NDE e a salvia em dose alta impõem" | "que a EQM (experiência de quase-morte) e a salvia em dose alta impõem" — or "que a experiência de quase-morte e …" |
| 5 | Med | 1320–1328 vs 1336/1364 | EN motif "grip" split across two renderings: "preensão" (Ch13 — clinical/anatomical register, odd as metaphor) vs "garra" (Ch14 — natural). The deliberate EN echo ("slow outward grip" ↔ "fast grip") is severed across the chapter boundary | "preensão causal", "a segunda preensão", "A preensão rápida" (Ch13); "a lenta garra voltada para fora", "a garra voltada para dentro" (Ch14) | Unify on "garra" (or another single term) in all six occurrences |
| 6 | Low | 1318 | Register: "deixe eu" mixes formal imperative with unassimilated pronoun — nonstandard in edited prose | "Então deixe eu conectar tudo isso à sua vida" | "Então deixe-me trazer tudo isso de volta para você" (also restores EN "bring this all the way back down to you") |
| 7 | Low | 1328 | "deflation" → "desilusão" shifts nuance (disappointment vs. deflating of a pretension) | "tome a desilusão por exatamente o que ela é" | "tome esse rebaixamento por exatamente o que ele é" |
| 8 | Low | 1338 / 1456 | EN "dial" rendered three ways: "mostradores" (two-dials motif, 1300), "válvula" (1338), "mostrador" (1456, where EN dial = control knob; "mão no mostrador" is a hand on a display, which adjusts nothing) | "a válvula que deixa você entrar pode travar aberta"; "sem a mão de ninguém no mostrador" | 1338: acceptable as is or "o botão que deixa você entrar pode travar aberto"; 1456: "sem a mão de ninguém no botão de ajuste" |
| 9 | Low | 1396 | EN "profound … deep" flattened to "profundo … profundo" in one sentence | "um resultado profundo, porque nos diria algo profundo" | "um resultado profundo, porque nos diria algo fundamental" |
| 10 | Low | 1408 | Missing article: "à distância segura" is off; idiomatic is "a uma distância segura" (or "de uma distância segura" with "fazer a pergunta") | "parei de fazê-la à distância segura" | "parei de fazê-la de uma distância segura" |
| 11 | Low | 1466 | Word order: "A grande galáxia mais próxima" reads as epithet ("the great galaxy"); EN means nearest *large* galaxy | "A grande galáxia mais próxima está a dois milhões e meio de anos-luz." | "A galáxia grande mais próxima…" |
| 12 | Low | 1328 vs 1404 | Term wobble: "modelo de mundo" (1328) vs "modelo do mundo" (1404 and dominant elsewhere) | "quanta preensão o automodelo tem sobre o *modelo de mundo*" | "sobre o *modelo do mundo*" |

Notes (no action needed): translator glosses "(EWM)" at 1310 and "(o ESM)" at 1340 are additions vs EN but helpful and consistent with book practice. "criticalidade", "beira do caos", "Problema Difícil", "Teoria dos Quatro Modelos", "Modelo Explícito do Mundo/do Eu", "automodelo" all used consistently. "os defensores do livre-arbítrio" for EN "the libertarians" (1360) is a good disambiguation, not an error.

---

# PT Interior Review — pt-07 (Capítulos 16–17, lines 1520–1843)

Reviewer: native-Portuguese editor pass (neutral/BR). EN reference: book-manuscript.md same range.

**Title self-citation check (Ch17):** VERIFIED CORRECT — line 1832 cites *A simulação que você chama de "eu"* and line 1830 uses the same wording; both match the real PT title exactly. No FR/JA-style title error here.

**Typography note (not an issue):** section uses straight quotes `"` throughout — identical to the EN source and the entire PT file (642 straight, 0 curly). Source-level convention, presumably smartened at build. Em dashes correct. `'t Hooft` apostrophes match EN (3×).

**Term consistency (clean):** "quatro modelos", "modelo do eu / Modelo Explícito do Eu", "modelo do mundo", "beira do caos" (38× book-wide, no "borda do caos"), "Problema Difícil", "criticalidade" (72× book-wide, fully consistent — book uses "criticalidade", never "criticidade").

| # | Sev | Line(s) | Issue | EN reference | Suggestion |
|---|-----|---------|-------|--------------|------------|
| 1 | High | 1550 | Truncated sentence / omission: "…é isso que singularidades conservadoras de informação *fazem*: convertem entre." — "convertem entre" dangles with no complement; EN complement dropped entirely. Ungrammatical as printed. | "that's what information-conserving singularities *do*: they transform between compressed boundary states and decompressed interior states." | "…*fazem*: convertem entre estados de fronteira comprimidos e estados interiores descomprimidos." |
| 2 | Med | 1548 | (a) Wrong regency: "E com o que se assemelha um estado…?" — "assemelhar-se" governs **a**, not "com" ("A que se assemelha…" or "Com o que se parece…"). (b) Omission: "Parece com as condições iniciais." drops "for a new expansion". | "And what does a maximally compressed state at Bekenstein saturation look like? It looks like the initial conditions for a new expansion." | "E com o que se parece um estado maximamente comprimido em saturação de Bekenstein? Parece as condições iniciais de uma nova expansão." |
| 3 | Med | 1670, 1818, 1834 | Mixed Popperian terminology within the two chapters: "infalseabilidade" (1670) vs "infalsificável" (1818) vs "Falseável" (1834); rest of book also has "falsificável" (368, 1054, 1058). Pick one family (falseável/falseabilidade OR falsificável/falsificabilidade) and normalize book-wide. | unfalsifiability / unfalsifiable / falsifiable | Normalize, e.g. "infalseabilidade / infalseável / falseável" everywhere. |
| 4 | Low | 1560 vs 1782 | Gender inconsistency for same predicate: "as singularidades são transformadoras de informação" (1560, fem) vs "as singularidades se tornam transformadores de informação" (1782, masc). | "singularities are/become information transformers" | Use "transformadoras" in 1782. |
| 5 | Low | 1706 | "é, em si, uma predição do modelo" — only occurrence of "predição"; everywhere else the book uses "previsão/previsões" (1576, 1610, 1828). | "is itself a prediction of the model" | "é, em si, uma previsão do modelo". |
| 6 | Low | 1724 | "limitado por singularidades" — established rendering elsewhere is "delimitado por singularidades" (1626 SB-HC4A expansion, 1700). | "bounded by singularities" | "delimitado por singularidades". |
| 7 | Low | 1680 vs 1712 | Broken echo: EN pairs "made me sit down" (1680) with "make you want to sit down" (1712). PT renders 1680 as "me deixou perplexo" but keeps "sentar" at 1712, so the deliberate callback is lost. | "the thing that made me sit down when I first saw it" | 1680: "…o que me fez sentar quando vi isso pela primeira vez." (or drop "sentar" in both). |
| 8 | Low | 1596 | Anglicized fronted whether-clause as subject: "Se alguém já mapeou sistematicamente essa hierarquia de fragilidade continua sendo… uma questão em aberto" — grammatical but reads as calque; hard to parse. | "Whether anyone has systematically mapped this fragility hierarchy remains… an open question" | "Até onde sei, continua em aberto a questão de saber se alguém já mapeou sistematicamente essa hierarquia de fragilidade…" |
| 9 | Low | 1818 | "Classe 4.5" — decimal point; PT convention is comma ("Classe 4,5"). Book uses PT comma elsewhere ("13,8 bilhões", "0,37"). | "some Class 4.5" | "alguma Classe 4,5". |
| 10 | Low | 1774 | "Elas negociam entre si." for "They trade." — "negociar" reads as bargaining/negotiation; EN means interconversion/exchange. | "They are not separate substances. They trade." | "Elas se convertem uma na outra." / "Elas se intercambiam." |
| 11 | Low | 1822 | "Achar isso profundo ou revoltante" — "revoltante" (outrageous/repugnant) shades away from "infuriating". | "Whether you find that profound or infuriating" | "profundo ou exasperante" / "enfurecedor". |

---

# PT Interior Review — pt-08: Coda + Backmatter (Notas/Referências, Apêndice A, Apêndice B)

Reviewer: Fable native-Portuguese editor (neutral / Brazilian-leaning)
Scope: PT lines 1844–2102 vs EN reference (Coda, Acknowledgments, Notes and References, Appendix A neurology glossary, Appendix B intelligence model)
Sections covered: Coda, Agradecimentos, Notas e Referências, Apêndice A, Apêndice B (through line 2099; Apêndice C begins at 2103)

## Summary

This span is in excellent shape. Coda register is natural and moving in idiomatic PT-BR; the Notes preserve every citation, author name, year, DOI, and page number faithfully (spot-checked against EN: PsyArXiv Sep 2023, Bach @Plinz 12 Jun 2026, 140-dataset meta-analysis, *Research in Human Development* 7(1), 61–78, *PeerJ* 8:e9290, 204 people / 100 daily sessions, twenty-four years, trillions of tokens / billions of parameters — all intact). Apêndice A technical terms are correct (potencial de ação, corpo caloso, colículo superior, receptores kappa-opioides, giro fusiforme/FFA, receptive fields ~1°/~8-16°, 0,5 mm). Apêndice B keeps the FMT/intelligence vocabulary consistent (conhecimento × desempenho × motivação; Modelo Explícito do Mundo/Eu; aprendizado cognitivo vs. por reforço). FMT terms consistent throughout: **quatro modelos**, **automodelo / modelo do eu / modelo do mundo**, **Problema Difícil**, **criticalidade** (+ "criticalidade auto-organizada"), **Teoria dos Quatro Modelos**.

Typography: em dashes (—) used correctly throughout; accents complete; no missing diacritics. Straight double quotes ("...") appear in PT, but the EN source uses straight quotes in the identical passages — this is the manuscript's shared markdown convention, NOT a PT-specific defect, so it is not flagged. Localization touches are good: "Dr. Fantástico" for *Dr. Strangelove* (correct BR title), "efeito Mateus" (Matthew effect), German "mein Beileid" preserved in italics.

## Issues

| # | Sev | PT line | EN ref | PT text | Issue | Suggested fix |
|---|-----|---------|--------|---------|-------|---------------|
| 1 | Low | 1882 | 1882: "an AI writing tool, editor, and **cross-checker**" | "...ferramenta de escrita com IA, editor e **revisor**." | Borderline. "revisor" reads as proofreader/reviewer and slightly softens the fact-verification sense of "cross-checker." Acceptable single-word choice; note only. | Optional: "editor e verificador de fatos" (or leave "revisor" — natural and defensible). |

No High or Medium issues found. Citations, numbers, and technical terms are untouched and faithful; no omissions, calques, or anglicisms of consequence detected.

---

# PT interior review — pt-09 (Apêndices C–H)

**Scope:** `pop-sci/book-manuscript-pt.md` lines 2103–2475 (Apêndice C: cinco classes de computação; D: sonhos lúcidos; E: por que "quatro" modelos; F: Modelo Padrão como contabilidade de fronteiras; G: quatro pontos fracos cosmológicos; H: as nove previsões) vs EN `pop-sci/book-manuscript.md` same range.
**Reviewer:** Fable, native-Portuguese editor pass (neutral / Brazilian-leaning).

**Overall:** Strong, faithful, idiomatic translation. No mistranslations, no omissions, no number/name errors. All five class definitions, the Wolfram/five-class mapping tables, the three-generations bookkeeping (múon, tau, charm, top), the four cosmological weak points, and all nine predictions match EN exactly and in order. Idioms land well ("saco de gatos", "livro-razão", "me dá um nó no estômago", "alguém em casa", "trazer à tona"). Technical terms correct (casa dos pombos, teorema de Bell, complexidade de Kolmogorov, TEPT, cetamina, corpo caloso, PCI/LZ). Typography clean (see note below). Only two terminology-consistency issues and minor nuance items.

| # | Sev | Line(s) PT | EN ref | Issue | Suggested fix |
|---|-----|-----------|--------|-------|---------------|
| M1 | Med | 2297, 2313 | 2297 ("neither pure world-model nor pure self-model"), 2313 ("No self model") | **Term inconsistency for "self model".** Generic self-model is rendered **"automodelo"** (2297 "nem puro automodelo"; 2313 "Sem automodelo"), but the named canonical models everywhere else use **"Modelo (…) do Eu"** (e.g. 2391, 2397, 2431). Result: two different PT terms for the same concept, and an asymmetric pair with "modelo do mundo" (EN keeps a symmetric "world-model / self-model"). The FMT term sheet specifies "modelo do eu". | Use "modelo do eu" for the generic self-model too (2297: "nem puro modelo do eu"; 2313: "Sem modelo do eu"), so it mirrors "modelo do mundo" and the named models. If "automodelo" is deliberately used book-wide as the generic term, keep it — but then reconcile against chapters; do not mix within one book. |
| M2 | Med | 2475 vs 2367 | 2367 ("full falsification battery… none has been falsified"), 2475 ("Each of these predictions is falsifiable") | **Popperian key term flips within one appendix.** Intro uses the *falsific-* root ("bateria completa de falsificação… nenhuma foi **falsificada**", 2367); conclusion uses the *false-* root ("Cada uma dessas previsões é **falseável**", 2475). Both are valid PT, but a science book should pick one. "falsificável / falsificada / falsificação" is the more standard Popper vocabulary in BR-PT philosophy of science. | Standardize on the *falsific-* family: 2475 → "Cada uma dessas previsões é **falsificável**." |
| L1 | Low | 2295 | 2295 ("spiking neurons **atop** proteomic networks") | Slight nuance shift: EN "atop proteomic networks" (neurons built *on top of* proteomic networks) → PT "neurônios que disparam **através de** redes proteômicas" (firing *through*). Changes the layering image. | "neurônios que disparam **sobre** redes proteômicas" (or "assentados sobre / apoiados em"). |
| L2 | Low | 2453 vs 2457 | 2453 ("step-like transition"), 2457 ("step-like discontinuity in EEG complexity") | "step-like" rendered inconsistently: sub-prediction 2 → "transição **em degrau**" (2453), but sub-prediction 4 → "descontinuidade **abrupta**" (2457). The second loses the "step / digital" image that ties to the "colapso digital do autômato" motif. | 2457 → "uma **descontinuidade em degrau** na complexidade do EEG" for consistency. |
| L3 | Low | 2257, 2403, 2407, 2409, 2431, 2443 (passim) | — | **Term-sheet reconciliation, not an error.** The manuscript uses **"criticalidade"** consistently, whereas the review brief's term list glossed "criticidade". "Criticalidade" is the standard BR-PT physics calque (cf. "criticalidade auto-organizada") and is used consistently and correctly here — flagging only so the term sheet and manuscript are known to diverge, and to confirm no mixed usage exists. | No change needed; keep "criticalidade" (recommend updating the term sheet to match). |

## Typography note (clean — no issue)
The PT source uses straight ASCII double quotes (`"`, 68 occurrences) with zero literal curly quotes, **identical to the EN source (68 / 0)** and to the ES/FR/IT sources. All Latin-script manuscripts rely on the build pipeline's smart-quote conversion; only the DE manuscript pre-curls. Em dashes are literal U+2014 throughout (96), accents are correct (autossimilar, número, é, óbvio, etc.), and a proper en dash is used for the "V2–V4" range (2246). No PT-specific typography defect.

