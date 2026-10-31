# Spanish interior — Fable native-editor review (S259, 2026-07-13)

Full es manuscript reviewed by 9 Fable agents vs the aligned EN source. High=fix before publish, Med=should fix, Low=polish. Fixes not yet applied.

---

# es-01 — ES review: teaser ("El punto que no está ahí") + "Sobre el autor" + Capítulos 1–2 (lines 48–249)

Overall: very high-quality translation. Fidelity to EN is strong, FMT terminology is consistent (cuatro modelos / modelo del yo / modelo del mundo; IWM/ISM/EWM/ESM acronyms kept as in EN; Problema Difícil consistent), all numbers/facts correct (nueve lunas, kilo y medio, veinticinco, 300 páginas, 120 investigadores, 40 millones, Tbr1/Satb2/Ctip2/Fezf2, seis/tres capas). Typography clean: «» guillemets, rayas —, ¿¡, accents (neocórtex, córvidos, parálogos, Gödel, Φ) all correct. Only minor items below.

| line | severity | issue | suggested fix |
|------|----------|-------|----------------|
| 58 | Low | "a unos treinta centímetros de **tus ojos**" for EN "around a foot from your **face**" — minor fidelity swap and internal inconsistency with L56 "acerca... el libro a **tu cara**" (both are "face" in EN). | "a unos treinta centímetros de **tu cara/rostro**" |
| 114 | Low | "por **admisión** de sus propios arquitectos" (EN "by its own architects' admission") — mild calque; "admisión" in Spanish reads as entry/acceptance, not confessing a fact. | "según **reconocen/admiten** sus propios arquitectos" |
| 114 | Low | "una **red** suficientemente grande de puertas lógicas" for EN "a large enough **grid** of logic gates" — "grid" is a rectangular array, not a network ("red"). | "una **matriz/cuadrícula** suficientemente grande de puertas lógicas" |
| 84 / 110 / 188 / 214 | Low | Mild dialect mix: LatAm lexicon ("maestría" L84, "computadora" L110) alongside peninsular ("montar en bicicleta" L188, "des**c**odificador" L214). Each item is pan-Hispanic-acceptable, but flag for a single house-style choice (neutral vs. peninsular vs. LatAm) across the book. | Pick one target register and align (e.g. neutral: keep "computadora"/"maestría", use "decodificador"). |

---

# ES interior review — es-02 (Capítulos 3–4)

Source: `/home/jeltz/aIware/pop-sci/book-manuscript-es.md` lines 250–451
EN ref: `/home/jeltz/aIware/pop-sci/book-manuscript.md` (Chapters 3–4)
Reviewer: Fable native-Spanish editor pass

| line | severity | issue | suggested fix |
|------|----------|-------|---------------|
| 368, 372, 382, 410, 418 | Med | "criticalidad" used consistently for "criticality". This is a direct anglicism; the FMT glossary term specified for this project is **criticidad** (also the more standard Spanish term in complexity/statistical-physics usage). Deviates from the canonical term throughout the section. | Replace all "criticalidad" → "criticidad" (verify against the rest of the manuscript for global consistency; if the whole book uses "criticalidad", align on the glossary term "criticidad"). |
| 378 | Med | Omission of authorial cross-reference. EN: "**Recall** the digital twin **from Chapter 2**." ES drops the callback and instead *introduces* the concept fresh: "Piensa en un gemelo digital (una simulación de ingeniería de un motor a reacción)." This breaks the Chapter-2 continuity and implies the digital twin is new here. | Restore the callback, e.g.: "Recuerda el gemelo digital del capítulo 2 (la simulación de ingeniería de un motor a reacción)…" |
| 428 | Low | "no puedes **introspeccionar** tus propios pesos sinápticos" — "introspeccionar" is a calque of "to introspect" and is not RAE-sanctioned (transitive use especially). | Prefer standard phrasing: "no puedes examinar por introspección tus propios pesos sinápticos" or "no puedes hacer introspección sobre tus propios pesos sinápticos". |

Notes (not flagged — acceptable/intentional):
- English acronyms (EWM/ESM/ISM) kept alongside Spanish full names; consistent throughout, presumably a deliberate glossary decision.
- "un kilo y medio de células cableadas" (l.448) for "a few pounds" — accurate localization of brain mass, kept.
- Guillemets («»), em dashes (—), ¿¡, and accents are used correctly throughout the section.
- FMT terms otherwise correct: "Teoría de los Cuatro Modelos", "Modelo Explícito del Mundo/Yo", "borde del caos", "Problema Difícil".
- No factual/number errors (names Botvinick/Cohen, Lashley, Brodmann área 17, Dennett/Frankish, Metzinger, Bach, Chalmers all correct; percentages and "3000 metros" correct).

---

# ES interior review — es-03 (Capítulos 5–6, lines 452–691)

Reviewer: Fable 5 (native-Spanish editor pass). Source: `pop-sci/book-manuscript-es.md` vs EN `pop-sci/book-manuscript.md`, same line range.

**Anosognosia check (FR-bug regression):** PASS. The opening symmetry paragraph ("Aquí hay una hermosa simetría. Si los psicodélicos son lo que ocurre cuando la frontera implícito-explícito se vuelve *demasiado* permeable, la anosognosia es lo que ocurre cuando se vuelve *demasiado* impermeable, al menos de forma local.") is present at line 674. No paragraph dropped in Ch6; paragraph count matches EN (674/676/678/680/682/684/686/688). No omissions found anywhere in Ch5–6 — the dense stacked paragraphs (624, 664) and the visual-hierarchy table (586–594) are fully rendered.

**Summary: 0 High, 2 Med, 4 Low.**

| # | Sev | Line(s) | Category | EN | ES | Issue / recommendation |
|---|-----|---------|----------|----|----|------------------------|
| 1 | Med | 678 | Mistranslation / cross-edition term mismatch | "so the **Explicit World Model** never includes the deficit" | "de modo que el **Modelo Explícito del Yo (ESM)** nunca incluye el déficit" | ES says **Self** model, EN says **World** model. Context is a paralyzed arm (body-self), and the surrounding sentences invoke the Implicit *Self* Model, so ESM is almost certainly correct — the ES translator silently fixed what looks like an EN typo. Not a Spanish error, but the two editions now disagree on a load-bearing FMT term. Reconcile: correct EN to "Explicit Self Model (ESM)" so both editions match. |
| 2 | Med | 648 | Nuance mistranslation | "People under salvia's influence have **walked out of** tenth-floor windows." | "se han **lanzado** por ventanas de un décimo piso." | "lanzarse por una ventana" reads as deliberately jumping/throwing oneself. The EN point is oblivious loss of body awareness (they didn't know where their body/the window was), not suicidal intent. Suggest "han salido por ventanas de un décimo piso" or "han acabado saliendo por ventanas de un décimo piso" — keep the obliviousness, drop the volition. |
| 3 | Low | 486, 632, 670 | FMT terminology consistency | "self-model" | alternates "**automodelo**" (486, 670) and "**modelo del yo**" (632) | Both are valid ("automodelo" is the standard Spanish rendering of Metzinger's self-model and is arguably preferable), but the book should pick one for the informal term. Verify which form earlier ES chapters use as canonical and align. (The formal "Modelo Explícito del Yo (ESM)" is used consistently and is fine.) |
| 4 | Low | 466/472/502 vs 510/516/522 | Lexical consistency | "cortex" | mixes "**córtex**" (466, 472, 502) and "**corteza**" (510, 516, 522) | Both correct; "corteza" is more standard in Spanish neuroscience ("corteza visual/auditiva"). Pick one noun for "cortex" throughout (the adjective "cortical" is fine either way). |
| 5 | Low | 484, 486 | Typography / styling | "the **extent** dial" / "the **complexity** dial" (bold, lowercase) | "el dial de **EXTENSIÓN**" / "el dial de **COMPLEJIDAD**" (bold, ALL-CAPS) | All-caps diverges from EN's bold-lowercase and can read as shouting in running prose. Consider bold lowercase ("el dial de **extensión**", "el dial de **complejidad**") unless earlier chapters established the small-caps/all-caps convention for dial names. |
| 6 | Low | 472 | Translationese / word echo | "periodic oscillations for **timing** and gating (alpha, theta, gamma **rhythms**)" | "oscilaciones periódicas para **el ritmo** y el control de paso (**ritmos** alfa, theta, gamma)" | "el ritmo" for "timing" collides with "ritmos" two words later. Use "la temporización" (or "la sincronización") for "timing" to remove the echo. |

## Notes (verified clean)
- FMT terms consistent and correct: **borde del caos**, **criticalidad**, **cómputo universal**, **integración global**, **Teoría de los Cuatro Modelos**, **cuatro modelos**, **modelo del mundo**, acronyms EWM/ESM/IWM/ISM kept in English throughout (616, 618). ("problema difícil" does not occur in this range.)
- Typography: guillemets « » used correctly for quotes (636–640, 620, 622, 654), interrogatives open with ¿ (456, 542, 622), accents correct on spot-check (cómputo, teoría, océano, fenoménica, según).
- Numbers/facts all match EN: 286, 10–40 Hz, 30–60 s, 140 datasets, years 2003/2014/2016/2022/2025/2026/2015, "años veinte" (1920s), 1998 o 1999, ocho años, cuarenta y cinco segundos, medio segundo, quince minutos, décimo piso; researcher names (Wolfram, Beggs, Plenz, Carhart-Harris, Tagliazucchi, Hengen, Shew, Algom, Shriki, 't Hooft, Klüver, Addy et al. 2015); journals (*Neuron* 2025, *Neuroscience & Biobehavioral Reviews* 2026); receptor/pharm details (serotonina 2A, kappa-opioide, Salvinorina A, Amanita muscaria).
- Idioms/register strong and idiomatic: "entrar en pérdida" (correct aviation term for *stall*), "meter en el mismo saco", "me hizo soltar la pluma", "la nieve en un televisor mal sintonizado", "De casi nada, todo.", "cerebro escindido" (split-brain).

---

# ES interior review — es-04 (Capítulos 7–9)

Reviewer: Fable native-Spanish editor pass. Scope: `book-manuscript-es.md` lines 692–909 vs EN `book-manuscript.md` same range (Ch7–9).
Overall: translation is fluent, accurate, and idiomatic; typography (« », rayas —, ¿ ¡, accents) is clean and correct throughout. Issues below are consistency/terminology, not mistranslations or omissions. No content dropped vs EN.

| # | Sev | Loc (ES line) | Category | Issue | Suggested fix |
|---|-----|---------------|----------|-------|---------------|
| 1 | Med | 816, 822 (Ch8) vs 846–888 (Ch9) | Terminology consistency | "split-brain" is rendered two ways: **"cerebro escindido"** in Ch8 (l.816 "la confabulación del cerebro escindido"; l.822 "conflicto del cerebro escindido") but **"cerebro dividido"** throughout Ch9 (title l.846, l.848 "síndrome del cerebro dividido", l.854, l.874, l.888). Both are valid, but the term crosses the chapter boundary as a callback ("En el próximo capítulo... del cerebro escindido") so the mismatch is visible. | Pick one term book-wide. "Cerebro dividido" is used more and matches the Ch9 chapter title/theme — change the two Ch8 instances to "cerebro dividido". |
| 2 | Med | prose l.744, 792 vs table l.757, 760; also l.708 | Terminology consistency / anglicism | Same core concept ("input") is rendered as English **"input"** in prose (l.744 "con input equivocado"; l.792 "ningún input visual actual", "sin input actual") but as **"entrada"** in the consciousness-map table (l.757 "entrada interna", l.760 "entrada errónea") and in prose at l.708 ("La entrada externa habitual queda cortada"). | Standardize. "Entrada" is the cleaner Spanish choice and already used in the table; replace the "input" occurrences with "entrada" (e.g., "con la entrada equivocada", "ninguna entrada visual actual", "sin entrada actual") unless the book glossary deliberately keeps the anglicism. |
| 3 | Med | l.694, 698, 700, 706, 734, 740, 742, 746, 762, 884 (all Ch7–9) | FMT term / glossary | Section consistently uses **"criticalidad"** for the criticality principle. The review brief's canonical FMT term is **"criticidad"**. "Criticalidad" is defensible (matches "criticalidad autoorganizada" in complexity-science Spanish), and it is internally consistent within this section — but if Ch1–6 or the glossary use "criticidad", this is a systematic split. | Verify against the book glossary / earlier chapters. If book standard is "criticidad", replace all "criticalidad"/"crítica-" derivatives here; otherwise no change needed. |
| 4 | Low | l.896, 898 ("alter") vs 902, 904 ("personalidad alternante") | Terminology consistency | DID "alter" rendered as the anglicism **"alter"** (l.896 "Cada *alter*", "Los alter"; l.898) then switched to the clinical **"personalidad alternante"** (l.902 "distintas personalidades alternantes"; l.904 "una personalidad alternante") within the same short passage. | Choose one. "Alter" (italicized) is fine as an in-community term if defined once; if using the clinical term, apply "personalidad alternante" throughout. |
| 5 | Low | l.784 ("video"), 896 ("computadora") | Register / dialect | Latin-American markers: **"video"** (no accent; Peninsular = "vídeo") and **"computadora"** (Peninsular = "ordenador"). Consistent with a neutral/LatAm target, but confirm this matches the dialect chosen for the rest of the book. | No change if book targets neutral/LatAm Spanish; otherwise switch to "vídeo"/"ordenador". Consistency check only. |
| 6 | Low | l.712 | Nuance | EN "an infinitely long fractal structure" → "una estructura fractal infinitamente extensa" ("infinitely extensive"). Minor semantic drift from "long"; the following "valles que se hundían sin fin" already carries the depth image, so "extensa" reads slightly redundant. | Optional: "una estructura fractal infinitamente larga/prolongada" or leave as is (acceptable). |

Counts: 0 High, 3 Med, 3 Low.

---

# ES interior review — es-05 (Capítulos 10–12)

Reviewer: Fable (native-Spanish editor pass). Scope: `book-manuscript-es.md` lines 910–1223 vs EN `book-manuscript.md` same range.
Register note: manuscript is neutral/LatAm Spanish (uses *computadora*, *monitorear*) — consistent, fine. Quotation marks (« »), ¿ ¡ placement, accents, paired *rayas*, and long-scale number conversions (see below) are handled correctly throughout. Only genuine issues listed.

Overall count: **0 High, 2 Med, 6 Low**

| # | Sev | Line(s) | Category | Issue | Recommendation |
|---|-----|---------|----------|-------|----------------|
| 1 | Med | 1144 | Mistranslation / false friend | "Mind uploading is the same phenomenon…" is rendered **"La carga mental es el mismo fenómeno…"**. *Carga mental* is an established Spanish idiom meaning **mental load / cognitive burden** (psychology, the "mental load" discourse) — a different concept. It is also inconsistent with how the chapter renders the term everywhere else. | Use "La transferencia de la mente es el mismo fenómeno…" (matches 1108/1110). |
| 2 | Med | throughout (924, 926, 928, 964, 966, 1062, 1072, 1120, 1122, 1128, 1176…) | FMT term / calque | "criticality" is consistently rendered **"criticalidad"** (incl. "criticalidad autoorganizada", 1120). The standard Spanish physics term is **"criticidad"** ("criticidad autoorganizada"), which is also the glossary term named in the review brief. *Criticalidad* is a recognized English calque. Internally consistent, so likely a house-style choice — but it deviates from the standard term and the brief's glossary. | Verify against the project FMT glossary. If the glossary is not already committed to "criticalidad", switch book-wide to "criticidad". |
| 3 | Low | 1108, 1110, 1144, 1160, 1182, 1204, 1210 | Term consistency | The central Ch12 concept "mind uploading" is rendered four different ways: "Transferencia de la mente" (1108, 1110), "transferencia mental" (1160), "carga mental" (1144, see #1), and English «mind uploading» (1182, 1204, 1210). There is a partial logic (neutral concept vs. pop-hype buzzword) but it reads as inconsistent. | Standardize. Suggest: "transferencia de la mente" for the concept; reserve «mind uploading» only where the pop/hype label is intended. |
| 4 | Low | 1088, 1126, 1180 | Typography (numbers) | Thousands separator is inconsistent: **"85.000"** (period; 1088, 1180) vs **"140 000"** and **"86 000 millones"** (thin space; 1126). | Pick one convention (RAE recommends the non-breaking thin space, no period/comma) and apply uniformly. |
| 5 | Low | 1144 | Typography (capitalization) | **"…del capítulo 9"** is lowercase, while every other cross-reference is capitalized ("Capítulo 1/2/5/6/8", "Apéndice B/H"). | Capitalize to "Capítulo 9" to match house style. |
| 6 | Low | 1036, 1180, 1184, 1190, 1192, 1218 | Anglicism (typography) | Several lone **spaced em dashes** used English-style to introduce/append an appositive, e.g. 1036 "…el contenido equivocado — una conciencia…"; 1180 "…al día — alrededor de una por segundo."; 1218 "…en criticalidad — de abajo arriba…". Spanish prefers a colon or a *raya* hugging the phrase. (Paired enclosing *rayas* elsewhere are correct.) | Replace with a colon or a hugging raya, e.g. "…el contenido equivocado: una conciencia…". |
| 7 | Low | 1008, 1036 (vs 1054, 1140, 1196, 1206, 1208) | Term consistency / anglicism | "input" left in English at 1008 ("un input de alta amplitud") and 1036 ("de input social"), but rendered "entrada" everywhere else (1054, 1140, 1196, 1206, 1208). | Unify to "entrada" (or keep "input" consistently — but "entrada" dominates). |
| 8 | Low | 1070 | Nuance / emphasis | "an engineering specification" → **"una especificación técnica"** softens the "engineering" emphasis the chapter builds toward ("desafíos de ingeniería", 1218; "la ingeniería puede comenzar"). | Consider "una especificación de ingeniería" for consistency and emphasis. |

Verify-only note (not counted): "self-model" is rendered "automodelo" (standalone) while the four named models use "…del Yo" (e.g., "Modelo Explícito del Yo"). This is internally consistent and *automodelo* is standard Spanish philosophy-of-mind usage; only confirm it matches the glossary if the glossary prefers "modelo del yo".

---

# ES Interior Review — es-06 (Capítulos 13–15, ES lines 1224–1519)

Native-Spanish editor pass vs EN reference (`book-manuscript.md`, Chapters 13–15, same line range).
Scope: mistranslation/omission, calques/translationese, register/flow, FMT terminology, Spanish typography, factual/number errors.

Overall: very strong translation — register, flow, and voice are excellent; all numbers, dates, names, and units verified correct (Libet 550/200/350 ms, 40/20/10/5 Hz, 1983/2009/1987/1998, 10^-35 m, 93 mil millones, 60 órdenes, 14 soldados, 40 km). FMT terms consistent («criticalidad» 107/0 vs «criticidad» manuscript-wide; «borde del caos», «Problema Difícil», «Teoría de los Cuatro Modelos», «automodelo»/«Modelo Explícito del Yo» all consistent). Issues below are the only genuine findings.

| # | Sev | Line (ES) | Issue | Current | Suggested |
|---|-----|-----------|-------|---------|-----------|
| 1 | High | 1324 | Mistranslation inverts meaning at the argument's climax: EN "was decided **for** you" rendered as «decidido **por** ti» = "decided **by** you" — the exact opposite of the chapter's thesis. | «El repliegue interior que se sentía como tu acto soberano privado fue decidido por ti, como todo lo demás.» | «...lo decidieron por ti, como todo lo demás.» or «...fue decidido en tu lugar, como todo lo demás.» |
| 2 | Med | 1328 | EN "the opening of the inner act isn't yours to **author**" → «no es tuya para **autorizarla**» (= authorize). Loses the authorship motif that echoes "delayed observer told he is the author" (1318). | «la *apertura* del acto interior no es tuya para autorizarla» | «la *apertura* del acto interior no la escribes tú» / «...no es obra tuya» |
| 3 | Med | 1290 | EN "You **shape** the system that chooses" → «**Modelas** el sistema» — collides with the book's technical modelo/modelar vocabulary; reads as "you model the system." Same paragraph family uses «moldea» for "shape" (1320). | «Modelas el sistema que elige» | «Moldeas el sistema que elige» |
| 4 | Med | 1238 vs 1308 | Load-bearing clock-analogy term rendered inconsistently: "display" = «la indicación» in Ch13 opening («La conciencia es la indicación»), but «esfera» in the zombie passage («todos los engranajes en su sitio pero sin esfera»). «Indicación» is also unnatural Spanish for a clock's display. | «La indicación es lo que hace del mecanismo un *reloj* ... La conciencia es la indicación.» | Unify on «esfera» (or «la esfera y las agujas»): «La esfera es lo que hace del mecanismo un *reloj* ... La conciencia es la esfera.» |
| 5 | Low | 1316 | Typography: closing raya before the sentence-final period wraps the *main clause* as if parenthetical. | «...por qué son conscientes» —esa parte se sigue de la arquitectura—.» | Drop the trailing raya: «— esa parte se sigue de la arquitectura.» |
| 6 | Low | 1322 | EN "unmistakably, instantly *yours*" (two adverbs) → adjective + adverb; slight meaning wobble. | «el único acto que es inconfundible, instantáneamente *tuyo*» | «el único acto que es inconfundiblemente, instantáneamente *tuyo*» |
| 7 | Low | 1330 | Fragment «Lo que deja...» reads oddly as sentence opener (EN "Which leaves..."). | «Lo que deja exactamente una sola cosa por la que vale la pena pasar la página» | «Lo cual deja exactamente una sola cosa...» / «Lo que te deja exactamente una cosa...» |
| 8 | Low | 1342 | Deliberate divergence from EN: "three **discrepancies** you should watch" → «tres **versiones de ti**». The ES arguably fixes EN's own mislabel (the list is of selves, the discrepancies are the gaps) — flagging so EN/ES divergence is a known, intentional choice rather than drift. | «Hay tres versiones de ti que deberías vigilar» | Keep ES; consider fixing EN to "three versions of you" instead. |
| 9 | Low | 1256/1328 vs 1338/1378/1438 | Cross-reference capitalization mixed: «(Capítulo 6)», «(Capítulo 5)» vs «(capítulo 6)», «(capítulo 9)», «el capítulo 5». | mixed | Unify (suggest capitalized «Capítulo N» in parenthetical cross-refs, matching Ch13 usage). |
| 10 | Low | 1492 | «cerodimensionales» is a nonstandard calque coinage for "zero-dimensional". | «(cerodimensionales, sin estructura interna)» | «(de dimensión cero, sin estructura interna)» |

Not flagged: «camarero» (3 uses, whole-book choice, universally understood despite the manuscript's LatAm-leaning baseline of «computadora»/«afuera»); «el clima del próximo mes» for "weather" (consistent with that baseline); spaced English-style em-dashes — systematic book-wide style choice, not a per-section defect.

---

# ES Review 07 — Capítulos 16–17 (lines 1520–1843)

Reviewer: native-Spanish editor pass (Fable). EN ref: book-manuscript.md 1520–1843.
**Title self-citation check (Ch17, line 1832): PASS** — «El título de este libro es *La simulación que llamas «yo»*.» matches the real title exactly. Line 1830 in-text echo also correct.

| # | Sev | Line(s) | Issue | Suggestion |
|---|-----|---------|-------|------------|
| 1 | Med | 1610 | Mistranslation + internal terminology break: «los sistemas de Clase 4 llevan estructura autosimilar como **subproducto**» — EN says "as a **subprocess**". The book itself uses «subproceso» everywhere for this exact concept (lines 716, 1450, 1512, 1620, 2339…). «Subproducto» (byproduct) changes the claim: self-similar structure is a *running sub-computation* of Class 4, not a side effect. | «…llevan estructura autosimilar como subproceso» |
| 2 | Med | 1596, 1620, 1748, 1750, 1752, 1796, 1820 (71× book-wide) | FMT term: manuscript uses «criticalidad (autoorganizada)» throughout; expected glossary term is «criticidad» (standard ES physics term for self-organized criticality: «criticidad autoorganizada»; «criticalidad» is an anglicism, though attested). Usage is 71×/0× — fully consistent book-wide, so this is a **global decision, not a local patch**. If the FMT ES glossary is «criticidad», a whole-book replace is needed; do NOT fix only Ch16–17. | Decide globally: keep «criticalidad» everywhere or replace all 71 with «criticidad» |
| 3 | Low | 1560 | «el Big Rip no produce **un** reinicio. Produce *muchos*.» — EN "doesn't produce **one** restart. It produces *many*." First read in Spanish is "produces no restart" (negation of existence) before the next sentence corrects it. | «no produce un solo reinicio. Produce *muchos*.» |
| 4 | Low | 1632, 1652, 1654, 1656, 1658, 1666, 1672, 1674, 1686, 1710, 1782, 1806 (19 lines in section) | Typography: English-style spaced em dashes («no una representación — la misma cosa», «La Weltformel — la «ecuación del mundo» … — no es») mixed with correct Spanish rayas attached to the inciso («—desde la escala de Planck…—», 1522, 1820). Inconsistent within the section and book-wide (~125 spaced instances). Cosmetic; a print-interior style decision. | Normalize to Spanish raya convention: «palabra —inciso—, sigue» |
| 5 | Low | 1674 + 1726 | Both EN sentences are distinct ("the weaknesses belong in the account as much as the strengths do" / "the fault lines deserve as much attention as the structure") but ES paraphrases both into near-identical wording: «una teoría honesta tiene que exponer sus debilidades, no ocultarlas» (1674) / «toda teoría honesta tiene que señalar sus propios puntos débiles» (1726) — creates an echo across chapters not present in EN. | Vary 1726, e.g.: «porque las líneas de fractura merecen tanta atención como la estructura» |

No other issues: numbers (13 800 millones, 12 fermiones, Bak/Chen/Creutz 1989, Landauer 1961/2012, Gödel 1931/25 años, tres generaciones), names ('t Hooft, Susskind, Maldacena, Lashley, Bekenstein), appendix refs (F, G), chapter cross-refs (2, 3, 4, 5, 13, 15, 16), FMT terms (cuatro modelos, borde del caos, Problema Difícil, Modelo Explícito del Yo, modelos implícitos/explícitos, SB-HC4A), Uncle Bruno in present tense (alive), Spanish ¿¡/«»/accents all correct. Register and flow are strong throughout — no translationese beyond the items above.

---

# ES Interior Review — es-08 (Coda + Agradecimientos + Notas y referencias + Apéndice A + Apéndice B)

Reviewer: Fable 5 (native-Spanish editor pass)
Source: `pop-sci/book-manuscript-es.md` L1844–2102 vs EN `pop-sci/book-manuscript.md` same range.
Verdict: strong translation. FMT terminology, guillemets, rayas, accents, decimal commas (0,5 mm; 8-16°), and — notably — the numeral traps are all handled correctly (EN "trillions of tokens" → "billones", EN "billions of parameters" → "miles de millones"; both correct for Spanish). Citations, author names, years, page ranges (7(1), 61–78; 8:e9290), and DOIs are untouched and faithful. Gender alternation of the "student" examples is preserved. Only two consistency issues found; no mistranslations or number errors.

| # | Sev | Loc (ES line) | Issue | EN ref | Suggested fix |
|---|-----|---------------|-------|--------|---------------|
| 1 | Med | 1936–1963 (Apéndice A intro + glossary) | The intro states «Las entradas están ordenadas alfabéticamente», but the glossary keeps the **English** alphabetical order, so it is not alphabetical in Spanish. Misplaced under the Spanish sort: "Potencial de acción" (P) is listed first; "Áreas de Brodmann" sits after Axón; "Colículo superior" appears at the old "S/Superior" slot; "Receptores kappa-opioides" and "Receptores de serotonina 2A" are scattered mid-list instead of under R. The stated claim is factually false for this edition. | "Entries are organized alphabetically." | Either re-sort the glossary by the Spanish head-word, or soften the claim (e.g. «ordenadas por término»). Re-sorting is cleaner and keeps the promise. |
| 2 | Med | 1991–2039 vs 2055–2099 (Apéndice B) | The central recurring concept "the recursive loop" is rendered **«bucle recursivo»** in the first half (¶ opening story, "El bucle recursivo", 2013/2019/2023/2025/2029/2031/2039) but switches to **«ciclo recursivo»** from "La conexión con la conciencia" onward (2055/2057/2059/2061/2063/2069/2093/2095/2097). EN uses "loop" uniformly throughout. Both Spanish words are correct, but splitting a defined, repeated core term inside one appendix reads as an editorial slip. | "loop" (uniform) | Standardize to one term across the whole appendix — «bucle recursivo» is the better technical match for "loop" (reserve «ciclo» for "cycle"). |
| 3 | Low | 1856 | «casi como una cuestión secundaria» for "almost as an afterthought" captures the "minor" sense but loses the "came-later" nuance. In context the preceding «vino después» already carries the temporal sense, so this is marginal. | "almost as an afterthought" | Optional: «casi de pasada» or «casi como una ocurrencia tardía». |

Notes:
- Coda: no omissions; all 16 paragraphs present and accurate. «inmortalidad cuántica», «Sé amable con todo el mundo. Puede que todos sean tú.» land well. «el viaje definitivo» for "the ultimate trip" preserves the double sense (journey / drug trip).
- Agradecimientos: Norbert "has since passed away" → «Hoy ya no está entre nosotros» (correct); Bruno kept present-tense/alive (consistent with KB). *mein Beileid* retained. No issue.
- Notas y referencias: every chapter note (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, Apéndice B) matches EN; Ch14 intentionally absent in both. Dates ("12 de junio de 2026"), "140 conjuntos de datos", "Nobel 2011", Planck (1899), all citations verbatim. «Problema Difícil», «criticalidad», «cuatro modelos» consistent.
- Apéndice A table: all 7 rows, receptive-field degrees, and psychedelic signatures accurate; FFA/Kanwisher (1997) intact.
- Apéndice B: knowledge × rendimiento × motivación, Cattell-Horn-Carroll, Wechsler (1940), Matthew/«efecto Mateo», Wittmann (Mannheim), Schmiedek/COGITO (204 personas, cien sesiones), Perry Preschool Project — all correct.

---

# ES interior review — es-09 (Apéndices C–H)

**Source:** `/home/jeltz/aIware/pop-sci/book-manuscript-es.md` lines 2103–2475
**EN reference:** `/home/jeltz/aIware/pop-sci/book-manuscript.md` lines 2103–2475 (Appendix C–H)
**Reviewer:** Fable native-Spanish editorial pass
**Scope:** Ap. C (cinco clases de computación), D (sueños lúcidos), E («cuatro» modelos), F (Modelo estándar), G (puntos débiles cosmológicos), H (nueve predicciones)

Overall: the translation is excellent — fluent, idiomatic, register-consistent (tú throughout, matching EN "you"), typography clean (« », rayas —, accents correct). All numbers, dates, names, class tables, prediction titles and the nine predictions match EN exactly (verified: Wolfram tables, mapping table, ordering 1→2→4→3 and 1→2→3→4→5, the 5-class properties table, V1/V2/V3, PCI/Lempel-Ziv, 90-min cycle, 5 sub-predictions of Pred 8, DMN + corteza prefrontal medial, Pinto 2017, Cantor 1870s, Rowland 2006 NKS, LaBerge 1990 / Voss 2009 / Baird 2019, tres generaciones "ni dos, ni cuatro, ni diecisiete", SB-HC4A, E = I). No content/number errors found. Issues below are terminology-consistency and minor nuance only.

| # | Loc (ES line) | Sev | Type | Issue | Suggestion |
|---|---------------|-----|------|-------|------------|
| 1 | 2257, 2403 (title), 2405–2411, 2443–2459 (Pred 5 + Pred 8, ~15 occurrences) | Med | FMT term consistency | Manuscript uses **"criticalidad"** throughout; the canonical FMT term list for this review names **"criticidad"**. Internally consistent within the section, and "criticalidad" is arguably the more standard complexity-science rendering (cf. "criticalidad autoorganizada"). But it deviates from the stated canonical term — a mismatch that must be reconciled against how the rest of the book renders "criticality". | Do NOT change blindly. Verify which term the other chapters/appendices use and unify book-wide. If the book elsewhere uses "criticidad", global-replace here; if "criticalidad", update the canonical term list instead. |
| 2 | 2297 ("un automodelo puro"), 2313 ("Sin automodelo") vs 2312 ("Sin modelo del mundo") | Low | Term consistency | Asymmetry: "world-model" → "modelo del mundo" but "self-model" → **"automodelo"** (not "modelo del yo", the canonical term listed). "automodelo" is a legitimate philosophy-of-mind term (Metzinger's Selbstmodell), so this is defensible, but it breaks parallelism with "modelo del mundo" and with the named "Modelo … del Yo". | Optional: if strict parallelism / canonical "modelo del yo" is desired, use "modelo del yo" in 2297/2313; otherwise leave and note "automodelo" as an accepted equivalent. |
| 3 | 2333 | Low | Nuance/hedge drop | EN "unitarity, **on this picture**, may itself be underwritten by the Bekenstein bound" → ES "la unitariedad, **a su vez**, podría estar sustentada por el propio límite de Bekenstein." "a su vez" (= in turn) fits the causal chain, but drops the framework hedge "on this picture" (en esta imagen / en este marco), which flags the claim as speculative-within-the-model. | Consider "y la unitariedad, en esta imagen, podría a su vez estar sustentada por el propio límite de Bekenstein." |
| 4 | 2463 (Pred 9 title) | Low | Lexical distinction | EN title uses "Neural **Fingerprint**" (Pred 9) vs "Neural **Signature**" (Pred 1); ES renders both as **"firma neuronal"**. The EN body of Pred 9 also says "neural signature", so meaning is preserved and consistency is arguably an improvement — flagged only because the EN title's lexical variation is flattened. | No change needed unless the author wants to preserve the fingerprint/signature contrast (e.g., "huella neuronal" for Pred 9 title). |

Notes (not issues): The 2181 parenthetical about what "compressible" means is condensed rather than translated clause-for-clause ("comprimible en el sentido de Kolmogorov —una regla brevísima la genera por completo—, aunque la computación paso a paso siga siendo irreducible y no admita atajos") — but both facts (compact description exists; step-by-step stays irreducible/no shortcuts) are fully preserved. Idioms handled well: "grab-bag" → "cajón de sastre" (2126), "someone is actually home" → "hay alguien ahí dentro" (2435), "the floor, not the ceiling" → "el suelo, no el techo" (2317), "compass points" → "puntos cardinales" (2308). English technical terms retained appropriately in guillemets/parentheses (MILD, WILD, WBTB, PCI, «alters», «form constants» → «constantes de forma»).

