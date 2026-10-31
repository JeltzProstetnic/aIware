# AIW-109 — Combined Cross-Language Interior Findings (S259)

**Work-order for the fix session.** Synthesis of 54 Fable native-editor reviews
(6 languages × 9 sections) of the translated interiors of *The Simulation You Call "I"*.
Manuscripts are line-aligned with the EN source (±2 lines), so findings at the same
line in multiple languages are treated as one underlying issue.

- **Source reviews:** `tmp/interior-review/{fr,ja,es,it,pt,zh}-{01..09}.md`
- **Manuscripts:** `pop-sci/book-manuscript-{fr,ja,es,it,pt,zh}.md`; EN source `pop-sci/book-manuscript.md`
- **Do NOT** blind-apply "criticality" or "self-model" changes — those are documented **glossary-vs-manuscript reconciliation decisions** (see §5). Read each row's "root cause" before editing.

---

## 1. Summary

### Severity counts by language

| Lang | High | Med | Low | Section notes |
|------|------|-----|-----|---------------|
| FR | **3** | ~20 | ~28 | High: anosognosia ¶ omission (674), Ch17 title self-citation (1830) — plus a Class-4 bullet omission (2245, logged Med) |
| JA | **2** | ~18 | ~30 | High: Ch17 title self-citation (1832), weak-point-4 authorial line omission (2357) |
| ES | **2** | ~19 | ~30 | High: meaning-inversion "decided **for** you" → "by you" (1324); EWM/ESM edition mismatch (678, logged Med) |
| IT | **1** | ~16 | ~35 | High: broken impersonal-*si* grammar in the chapter thesis question (330–340) |
| PT | **1** | ~16 | ~26 | High: truncated/omitted sentence "convertem entre …" (1550) |
| ZH | **2** | ~13 | ~30 | High: permeability/transparency term collision (1298), Chalmers name split (1308) — plus meaning-inversion "pushed past → pushed into" Class 4 (1750, logged High below) |

(Med/Low counts are approximate — several "Med" rows are the *same* systematic criticality/self-model/typography item counted once per section. The High list in §2 is exhaustive and exact.)

**Totals: 11 High findings** across the six languages (12 if the ZH 1750 meaning-inversion is counted as High — it is listed in §2). Plus 2 High-adjacent omissions logged at Med (FR 2245, JA is High). See §2 for the authoritative table.

### Cross-language vs per-language

- **~12 issue-clusters are cross-language (≥2 languages).** The dominant ones:
  - **Ch2 digital-twin callback dropped (line 378)** — FR, JA, ES, IT, PT, ZH — **all 6 languages** (root cause: shared restructure; the EN callback survives, translators independently glossed it away).
  - **"criticality" → criticalité/criticalidad/criticalità/criticalidade** — FR, ES, IT (partial), PT (all use the "-al-" calque; glossary says the shorter form). Systematic per-language; a **reconcile-glossary** decision, not a bulk edit.
  - **"self-model" generic term drift** (auto-modèle / automodelo / automodello vs modèle du soi / modelo del yo / modello del sé / modelo do eu) — FR, ES, IT, PT (and one JA の-insertion analogue). Systematic; glossary decision.
  - **Ch17 title self-citation** — FR + JA have the **wrong** title; ES, IT, PT, ZH **verified correct**. (§3, §2.)
  - **Ch5 cross-reference dropped at line 1452** ("which we first met in Chapter 5") — FR, JA, ZH (root cause: shared EN passage; PT/ES/IT retained it — check).
  - **"sit down" callback lost** (~1678/1712) — FR, JA, IT, PT (systematic translation choice; EN repeats the phrase).
  - **REM/non-REM orthography split** (roman vs kana) — JA only, but appears in two sections (04, 09) → treat as one JA-internal cluster.
  - **French typography (NBSP + curly apostrophe) absent** — FR, all 9 sections (build-dependent; see §5).
  - **Quote typography** — PT ships straight quotes where the edition convention is curly (PT-01 flags this as a real defect; ES/IT/FR use guillemets; ZH already curly). See §5.
  - **"mind uploading" rendered 3–4 ways** — ES, IT, PT (per-language internal inconsistency).
  - **"input" kept in English vs translated** — ES, IT, PT (per-language).
  - **Ch17 "weaknesses belong in the account" paraphrase / doubled aphorism** — IT, ZH, ES (EN 1674/1726 diverged from current translations).

- **The rest are per-language** (§4): grammar/agreement fixes, name transliterations, orthography, and lexical polish specific to one manuscript.

---

## 2. HIGH-severity must-fix (all)

Every High finding, plus the two authorial-omission items that reviewers flagged as borderline-High. **Meaning-inversions and omissions are called out in the "type" column.**

| lang(s) | line | type | issue | fix |
|---------|------|------|-------|-----|
| **ES** | 1324 | **MEANING INVERSION** | EN "the inner retreat … was decided **for** you" rendered «decidido **por** ti» = "decided **by** you" — the exact opposite of the chapter's determinism thesis, at the argument's climax. | «...lo decidieron por ti, como todo lo demás.» or «...fue decidido en tu lugar, como todo lo demás.» |
| **ZH** | 1750 | **MEANING INVERSION** | EN "pushed **past** Class 4, the simulation shatters" rendered 「被推入第四类」= "pushed **into** Class 4" — inverts the mechanism (consciousness already *is* Class 4; a seizure is pushed *out/past* it). | 「被推出第四类之外」or「越过第四类」 |
| **ZH** | 1298 | **TERM COLLISION** (High) | *permeability* rendered 透明性 (transparency) — but 透明性 is the book's reserved term for Metzinger's *transparency* (现象透明性, line 412), a near-opposite concept. The book renders *permeability* as 通透性 everywhere else (564–596, 678, 2385–2399). Distorts the mechanism. | 那道**通透性**边界被彻底冲开。 |
| **FR** | 1830 | **WRONG TITLE (self-citation)** | Text cites *La Simulation que vous appelez « moi »* — but the real title (line 1) is *La simulation que vous appelez « Je »* (capital Je). This is the passage where the title is explained. See §3. | Replace with the exact title *La simulation que vous appelez « Je »* (case + pronoun identical to the title page). Also fix line 1828 echo («je» → «Je»). |
| **JA** | 1832 | **WRONG TITLE (self-citation)** | Text says 本書の題名は『あなたが「私」と呼ぶシミュレーション』 — but the real title (line 1) is 『「私」という名のシミュレーション』. See §3. | 本書の題名は『「私」という名のシミュレーション』である。(Also align the 1830 echo to the title wording.) |
| **ZH** | 1308 | **NAME INCONSISTENCY** (High) | Same philosopher under two Chinese names: 大卫·查尔默斯（David Chalmers）here vs the book-established 戴维·查默斯 (Ch1, 102/110). | 戴维·查默斯（David Chalmers） |
| **IT** | 330, 332, 338, 340 | **BROKEN GRAMMAR** (thesis question) | «perché l'elaborazione fisica **ci si sente come qualcosa**?» — impersonal-*si* cannot take an explicit subject; this is the **bolded thesis question** of Ch4 and the core "what-it-is-like" phrase. Recurs at 338, 340. Calque. | Use the Italian idiom: «perché si prova qualcosa nel corso dell'elaborazione fisica?»; 338 «la commutazione dei transistor non si prova come niente»; 340 «l'attività di scarica dei neuroni non si prova come vedere il rosso». (Then standardize the "what it is like" idiom section-wide — see §4-IT.) |
| **PT** | 1550 | **OMISSION / truncation** | «…é isso que singularidades conservadoras de informação *fazem*: convertem entre.» — "convertem entre" dangles; the EN complement is dropped, ungrammatical as printed. | «…*fazem*: convertem entre estados de fronteira comprimidos e estados interiores descomprimidos.» |
| **FR** | 674 | **OMISSION** (opening ¶) | Entire opening paragraph of "Anosognosie : l'inverse" missing — the too-permeable / too-impermeable symmetry that motivates the section title. **ES/IT/PT/ZH all verified this paragraph PRESENT — FR is the only drop.** | Add: «Il y a ici une belle symétrie. Si les psychédéliques sont ce qui se produit quand la frontière implicite-explicite devient *trop* perméable, l'anosognosie est ce qui se produit quand elle devient *trop* imperméable — du moins localement.» (Verify against latest EN.) |
| **JA** | 2357 | **OMISSION** (authorial voice) | EN opens weak-point Four with "This is the one that ties my stomach in knots." — dropped entirely; jumps straight to the Gödelian consequence. Pairs rhetorically with 2349. | Restore, e.g. 「これは、考えるたびに胃が締めつけられる一点だ。」after the heading. |
| **FR** | 2245 | **OMISSION** (logged Med, treat as must-fix) | Class-4 bullet drops EN's closing sentence "The engine of the simulation." | Add «Le moteur de la simulation.» to close the bullet. |

**Also verify (edition-level, flagged in ES-03 and IT-03 as Med — a real EN/translation disagreement on a load-bearing FMT term):**

| lang(s) | line | type | issue | fix |
|---------|------|------|-------|-----|
| ES + IT | 678 | **EDITION MISMATCH** | EN says "so the **Explicit World Model** never includes the deficit"; ES and IT both silently corrected to **Explicit Self Model (ESM)** (a paralyzed arm is a body/self deficit; surrounding sentences are all about the self). The two ES/IT translators independently "fixed" what looks like an EN author slip. **The editions now disagree with EN.** | Decide at EN source: if the intended term is ESM, **fix EN → "Explicit Self Model (ESM)"** and re-propagate so all editions match; if EWM is deliberate, revert ES/IT to the World model. Do not leave EN and two translations disagreeing. |

---

## 3. Cross-language issues (≥2 languages)

Root cause coded **(a)** shared EN source / restructure artifact → **fix EN + re-propagate**, or **(b)** systematic per-language translation choice → **fix each translation**.

| ~line | languages | issue | fix approach | root cause |
|-------|-----------|-------|--------------|------------|
| **378** | **FR, JA, ES, IT, PT, ZH (all 6)** | EN "Recall the digital twin **from Chapter 2**." Every language dropped the Ch2 callback and substituted an inline gloss "(engineering simulation of a jet engine)". The "you've seen this before" signal is lost in all editions. | **(a/b hybrid).** The EN callback is intact, so this is a **repeated independent translation choice** — but because it hit all 6, verify the EN phrasing isn't ambiguous, then **restore the "Chapter 2" back-reference in each translation** (keep or drop the added gloss per house style). FR: «Rappelez-vous le jumeau numérique du chapitre 2.» · ES: «Recuerda el gemelo digital del capítulo 2…» · IT: «Ricorda il gemello digitale del Capitolo 2.» · PT: «Lembre-se do gêmeo digital do Capítulo 2…» · JA: 「第2章で見たデジタルツイン…を思い出してほしい。」 · ZH: 「还记得第2章讲过的数字孪生吗——…」 | (b) per-language |
| **1830 / 1832** | **FR, JA** have the bug; **ES, IT, PT, ZH verified correct** | **Ch17 title self-citation.** FR cites *…« moi »* (should be *« Je »*); JA cites 『あなたが「私」と呼ぶ…』 (should be 『「私」という名の…』). ES/IT/PT/ZH each explicitly PASS-checked at line 1832 and match their real titles. **The task's "found in FR/JA/PT/ZH" premise is only half right — PT and ZH are clean.** | **(b).** Fix FR (1830 + 1828 echo) and JA (1832 + 1830 echo) only. Each edition must cite its own real front-cover title verbatim (exact case + pronoun). | (b) per-language |
| **1452** | **FR, JA, ZH** (check ES/IT/PT) | EN "self-organized criticality — **which we first met in Chapter 5**." The Ch5 back-reference dropped in FR, JA, ZH. | **(b).** Restore the Ch5 cross-reference in FR/JA/ZH. FR: «…, que nous avons rencontrée pour la première fois au chapitre 5,…» · JA: 「——第5章で最初に出会ったあの仕組み——」 · ZH: 「——我们在第5章初次见过它。」 Confirm ES/IT/PT retained it. | (b) per-language |
| **~1678 / 1712** | **FR, JA, IT, PT** | EN deliberately repeats "sit down" (opening "made me sit down" ↔ closing "make you want to sit down") as a bracketing callback. Each language rendered the two with *different* images, breaking the echo. | **(b).** Use one repeated image per language at both points. FR «m'a coupé le souffle»/«ne vous coupe pas le souffle»; JA 座り込みたく… at both; IT «senza fiato» twice; PT «me fez sentar» / «fazer você querer sentar». | (b) per-language |
| **~1674 / 1726** | **IT, ZH, ES** (EN drift) | Ch17 lines: EN "the weaknesses belong in the account as much as the strengths do" (1674) and "the fault lines deserve as much attention as the structure" (1726). IT and ZH both paraphrase 1674 into a *different* aphorism ("a theory claiming no weakness deserves no trust") and near-duplicate it at 1726, creating a repetition **absent in EN**. ES echoes 1674/1726 into near-identical wording too. | **(a).** These translations track an *older* EN. **Re-propagate the current EN 1674/1726 wording** and retranslate faithfully so the two sentences stay distinct: IT «La includo comunque, perché i punti deboli appartengono al resoconto quanto i punti di forza.» / «perché le linee di faglia meritano la stessa attenzione della struttura.» ZH literal versions given in zh-07. ES: vary 1726. | (a) EN re-propagate + (b) retranslate |
| **"mind uploading"** ~1108–1220 | **ES, IT, PT** | Central Ch12 term rendered 3–4 ways per language. ES: "transferencia de la mente" / "transferencia mental" / **"carga mental"** (false friend = *cognitive load*, 1144) / English «mind uploading». IT: "trasferimento della mente" (also used for *mind transfer*) vs "caricamento della mente". PT: "upload de/da mente" + "emulação do cérebro inteiro" vs "emulação total do cérebro". | **(b).** Standardize each language on ONE term for *uploading* and reserve a distinct term for *mind transfer*. ES: "transferencia de la mente" (fix "carga mental" → this at 1144). IT: "caricamento della mente" for uploading; "trasferimento" only for transfer. PT: "upload da mente" + "emulação total do cérebro". | (b) per-language |
| **"input"** (prose vs table) | **ES, IT, PT** | Same FMT concept kept in English "input" in some places, translated ("entrada") in others incl. the consciousness-map table. | **(b).** Standardize each to the translated form ("entrada") throughout incl. table cells (or keep English everywhere — reviewers recommend "entrada"). | (b) per-language |
| **"criticality"** (systematic) | **FR, ES, IT (partial), PT** | All four use the "-al-" calque (criticalité / criticalidad / criticalità / criticalidade) 70–107× each, **0×** the glossary's shorter form. Reviewers unanimously note the calque is the **domain-standard** term for "self-organized criticality" and recommend **updating the glossary**, not the manuscripts. IT is mostly on the short form «criticità» but has the "autoorganizzata" hyphenation issue (§5). | **(b) → glossary reconcile.** DECISION REQUIRED (see §5). Recommended: keep the manuscript calque, update the term sheet. Do **not** do a blind 100+-instance replace. | glossary decision |
| **"self-model"** generic drift | **FR, ES, IT, PT** (+ JA の-analogue) | Generic *self-model* alternates with the auto- form (auto-modèle / automodelo / automodello / modelo do eu vs modèle du soi …). The *named* capitalized models (ESM/ISM) stay consistent. | **(b).** Pick one generic term per language and align (glossary says the "modèle du soi / modelo del yo / modello del sé / modelo do eu" family). Internal consistency matters more than which. See §5. | glossary decision |
| **Popperian root** (falsifiable) | **PT, IT** | Term family flips within one appendix/chapter: PT "falsificável" vs "falseável" (1670/1818/1834/2367/2475); IT less affected. | **(b).** PT: standardize on *falsific-* family (BR-PT philosophy-of-science standard): 2475 → "falsificável"; 1818/1834 → "infalsificável/falsificável". | (b) per-language |
| **"Neural Signature" vs "Neural Fingerprint"** (Pred 1 vs Pred 9 titles) | **ES, IT, PT, JA (preserved), ZH** | EN varies Pred-1 "Signature" vs Pred-9 "Fingerprint"; ES/IT/PT collapse both to one word ("firma"/"impronta"→"firma"). JA preserves the distinction (神経的シグネチャ vs 神経的指紋). ZH renders both consistently. | **(b), optional.** Low priority — Pred-9's EN *body* also says "signature", so collapsing is defensible. If preserving the contrast: ES "huella neuronal", IT "impronta neurale", PT "impronta"→keep. | (b) per-language, optional |
| **Class "4.5" decimal point** | **FR (1816), IT (1818), PT (1818)** | English decimal point "4.5" where the locale uses a comma (and the same texts write 0,37 / 13,8). | **(b).** FR «Classe 4,5»; IT «Classe 4,5»; PT «Classe 4,5». (Also FR annexe G line 2351.) | (b) per-language typography |
| **French NBSP + curly apostrophe** absent | **FR, all 9 sections** | 0× U+00A0 / U+202F and 0× typographic ’ in the entire FR manuscript. | **(a/build).** babel-french auto-inserts thin spaces in the **print PDF**; pandoc does **not** for EPUB. **Verify the FR EPUB path**; if it passes source through, run an NBSP + ’ post-process. See §5. | build/pipeline |
| **Quote typography** (straight vs edition convention) | **PT** (flagged as defect); ES/FR/IT use «»; ZH already curly | PT-01 flags that PT ships straight ASCII `"` and the pipeline does **not** auto-curl (DE pre-curls, ES/FR use guillemets), so PT would print straight quotes against the edition's curly `""` convention. PT-02..09 reviewers note the EN source is *also* straight and assume build-time smart-quote conversion. **Conflict between reviewers — resolve.** | **(a/build).** Confirm whether the PT build applies smart quotes. If not, convert PT `"…"` → `""` (U+201C/U+201D) or the pipeline's target. | build/pipeline |

---

## 4. Per-language issues (remaining Med/Low not covered above)

### FR — French

| line | sev | issue | fix |
|------|-----|-------|-----|
| 298/300 vs 336/348/352/444 | Med | "self-model" = "modèle du soi" (298/300) vs "auto-modèle" (336…). | Standardize generic term (see §5). |
| 620 | Med | "supervenes on" → "émerge de" (emergence ≠ supervenience); caption 606 correctly uses "survient sur". | «Chaque niveau survient sur celui qui est en dessous…» |
| 506, 624 | Med | "fMRI" left English; book uses "IRMf" (4×). | Use «IRMf». |
| 814, 872 | Med | «se sentir + [nom]» non-idiomatic ("vous vous sentez une chaise"). | «vous vous sentez **être** une chaise» / «avez l'impression d'être». |
| 878, 868 | Med | Tense clash (passé composé + passé simple in one sentence / adjacent philosophers). | Harmonize to one tense. |
| 892–902, 904 | Med | "fork/forking" split scinder/scission vs embranchement — Ch3 callback weakened. | Unify DID splitting verb to the Ch3 term (bifurquer/embrancher). |
| 900 | Med | Scare-quoted «qu'» abuts «une» — reads broken. | «n'est qu'une « simple » performance». |
| 910/912 | Med | Orca gender flips elle→il within the anecdote. | Hold one gender. |
| 1058 | Med | "fire" callback broken («au pied du mur» then «le feu» dangles). | Use a fire idiom: «passer les théories par le feu … Cette annexe est ce feu». |
| 1292 | Med | Agreement: «facettes … intégrés» → «intégrées». | Fix. |
| 1826 (×2) | Med | «vivant … du versant» (wrong prep) + agreement «dissous» after «propriétés» f.pl. | «sur le versant virtuel»; restructure the qualia/mystère sentence. |
| 1606 | Med | «vues prises» — mixed-gender antecedents → masc. pl. | «vus pris». |
| 1858, 1910, 1918, 2065 | Med | «assommement» (non-standard); «conscience couverte» (false friend for *covert*); «interoception» missing accent (book uses intéroception); "in either English or German" → «ni en français ni en anglais» (German dropped — author's native lang, load-bearing). | «l'ESM assommé»; «conscience cachée/non manifeste»; «intéroception/intéroceptive»; confirm/restore German. |
| 1074, 1450 | Low/Med | Dropped cross-refs ("du chapitre 1"; Ch5 back-ref — 1450 also in §3). | Restore. |
| 78, 124, 154, 50, 58, 512, 488, 550/552, 1604, 1608/1704/1764, 1760, 1706, 1800, 1280, 1294, 650/670, 836/862, 840, 720, 834, 902 | Low | Localization/lexical polish, "seventy years"→"trois quarts de siècle" silent number drift (1604), auto-similaire/autosimilaire spelling, Cotard délire vs syndrome, confabulation vs fabuler. | Apply per-row fixes in fr-0X. |
| 114/116 | Med | IIT/GNW acronyms appear before being tied to their French names. | Introduce acronym at first mention. |

### JA — Japanese

| line | sev | issue | fix |
|------|-----|-------|-----|
| 62 | Med | Near-verbatim repetition 「目がまっすぐそこに向いている」×2. | Restore first half to a position clause. |
| 166/190/206 | Med | "synaptic weights" シナプス荷重 vs シナプスの重み. | Unify (recommend シナプスの重み). |
| 226/236 | Med | 序数 kanji vs Arabic (第一層 vs 第4層). | Unify to kanji. |
| 470 | Med | Doubled adjective 「ゆるやかなゆるやかな」. | Delete one. |
| 670, 960, 2355 | Med | Half-width `)` closing a full-width `（` clause (parenthesis width). | Use full-width ）. |
| 802 | Med | "subcritical" 臨界未満（サブクリティカル）vs established 亜臨界. | Use 亜臨界. |
| 704 | Med | Heading 省エネモード ("energy-saving") for "Degraded Mode" — opposite spin; body uses 劣化. Borderline High (heading visibility). | 劣化モード. |
| 1250, 1252 | Med | Name errors: 「クーン」(Kühn) collides with Thomas Kuhn → キューン; 「サリア・ウェットリー」→ タリア・ウィートリー (Thalia Wheatley). | Fix both. |
| 1336 | Med | 「切り離れ」non-standard verb form. | 「切り離され」. |
| 1438–1466 | Med | われわれ vs 私たち within one chapter (book favors 私たち 65:19). | Unify to 私たち. |
| 1580+ (1532/1538/1540 vs 1580…) | Med | 事象の地平線 vs 事象の地平面 (9:8 book-wide); 宇宙論的地平線 vs 地平面/地平. | Unify to 地平線. |
| 1630/1736–1746/1782–1808 | Med | "decompress" rendered 展開/解凍/伸張/伸長 — 4 ways; the 伸張→伸長 flip is inside the load-bearing compressed/decompressed argument. | Pick one (圧縮／伸張); keep 展開 only as Ch16 narrative verb. |
| 1620/1748/1796 | Med | "subprocess" 部分プロセス/下位プロセス/部分過程 (3 ways). | Unify to 部分プロセス. |
| 1116/1118/1138/1176 | Med | Five-level hierarchy names inconsistent; 「プロテオミクスの」names the discipline, not the level. | Unify to プロテオーム的レベル / トポロジー的レベル. |
| 1930, 2077/2083 | Med | "performance" 遂行 vs body's 性能 (same formula, two middle terms); "operational knowledge" 運用的知識 vs 操作的知識. | 性能; 操作的知識. |
| REM/non-REM (757/758, 2445–2457 vs 2257/2281) | Med | Roman REM睡眠 vs katakana レム睡眠 across App D/H and body. | Standardize book-wide. |
| 238, 206, 272 (・), 336/396, 628/632, 906, 1846, 1858, 1610, 1774, 2421, 2447 | Low | 現象学 vs 現象面; 固い vs 硬い; ハード・プロブレム nakaguro; 仮想の自己 vs 仮想自己; 転向 register; hive→群れ; コスモロジー vs 宇宙論; 固有感覚 vs 固有受容感覚; Arabic 17 amid kanji; ランダウア missing 長音; 繊維→線維; リズム repetition. | Apply per-row ja-0X fixes. |
| 944/1008/2265… | Low | Half-width `?` vs full-width `？`. | Standardize to full-width. |
| 912 vs 1198, 922–928 | Low | 三十メートル vs 200メートル number orthography; "Commitment" → 前提 (premise). | Align; consider 基本前提/コミットメント. |

### ES — Spanish

| line | sev | issue | fix |
|------|-----|-------|-----|
| 648 | Med | "walked out of tenth-floor windows" → «se han lanzado» (implies deliberate jumping; EN = oblivious). | «han salido por ventanas de un décimo piso». |
| 1144 | Med | "mind uploading" → «carga mental» (false friend = cognitive load). Also in §3 cluster. | «transferencia de la mente». |
| 1290, 1328, 1238/1308 | Med | «Modelas el sistema» (collides with modelo/modelar; use «Moldeas»); "to author" → «autorizarla» (loses authorship motif → «no la escribes tú»); clock "display" «indicación» vs «esfera». | Apply es-06 fixes; unify on «esfera». |
| 1610 | Med | "subprocess" → «subproducto» (byproduct) — changes the claim; book uses «subproceso» elsewhere. | «subproceso». |
| 1936–1963 | Med | Apéndice A claims «ordenadas alfabéticamente» but glossary keeps English sort order — false for Spanish. | Re-sort by Spanish head-word, or soften the claim. |
| 1991–2039 vs 2055–2099 | Med | "recursive loop" «bucle recursivo» → «ciclo recursivo» mid-appendix. | Standardize on «bucle recursivo». |
| 1108–1210 (uploading), input, 1088/1126 (thousands sep), 1036/1180 (spaced em dash) | Med/Low | See §3 for uploading/input; number separator 85.000 vs 140 000; English-style spaced em dashes → colon/hugging raya. | Standardize. |
| 58, 114 (×2), 428, 712, 1144 cap, 1330, 1342, 1492, 1560, 1674/1726, 2333, 2463, cross-ref caps | Low | «tus ojos»→«tu cara»; «admisión»/«red»→«reconocen»/«matriz»; «introspeccionar» calque; «infinitamente extensa»; «del capítulo 9» cap; «Lo que deja»→«Lo cual»; «cerodimensionales»→«de dimensión cero»; "one restart" negation risk (1560); "on this picture" hedge dropped (2333); Signature/Fingerprint (§3). | Apply es-0X rows. |
| 84/110/188/214, 784/896, «camarero» | Low | Dialect mix (LatAm vs peninsular) — pick one house register book-wide. | Decide register; align. |
| 484/486 | Low | Dial names ALL-CAPS «EXTENSIÓN/COMPLEJIDAD» vs EN bold-lowercase. | Bold lowercase unless small-caps convention established. |
| 466/472/502 vs 510… | Low | «córtex» vs «corteza». | Prefer «corteza». |

### IT — Italian

| line | sev | issue | fix |
|------|-----|-------|-----|
| 334, 340 (×2) | Med | «assomigli a» distorts "nothing it is like to be" (334); «lo scarico neuronale» wrong lexeme — firing = «la scarica» (feminine); «lo scarico» = drainage (340). | «Non c'è nulla che si provi a essere…»; «la scarica neuronale». |
| 378, 398 | Med | Ch2 callback dropped (§3); «È luci accese.» ungrammatical (parallel with «Le luci sono spente»). | Restore callback; «Le luci sono accese.» |
| 712/714/716 | Med | "disembodiment" disincarnazione (712/714) → scorporazione (716), breaks callback. | Use disincarnazione at 716. |
| 894/904/906 | Med | fork/forking sdoppi / «forking» / biforcata+sdoppiata — tangled; sdoppiare used for both *fork* and *doubled*. | Pick one IT rendering, gloss «forking» once, tie the verb to it. |
| 1108–1220 | Med | "mind uploading" trasferimento vs caricamento (§3). | Standardize (caricamento for uploading). |
| 1326 | Med | «contribuire» used transitively (anglicism). | «apporta … Apporta necessità». |
| 1300 (cf 1338) | Med | "two dials" → «quadranti» (= gauge face, collides with clock-face «quadrante»); Ch14 correctly uses «regolatore». | Unify to «regolatori»/«manopole» across chapters. |
| 1566, 1674, 1684/1692, 1782, 1810/1820, se/sé, 1832 «pattern» | Med | «possibilmente» (false friend for "possibly")→«forse/magari»; 1674 paraphrase (§3); «all'/sull'orlo del caos» mirrored-list mismatch; «trasformatori»→«trasformatrici» (agreement); «il SB-HC4A»→«l'SB-HC4A»; se stesso/sé stesso convention (also 2148 etc.); bare «pattern»→«schema». | Apply it-07 fixes. |
| 1936/2045 | Med | Apéndice A alphabetical claim false (as ES); "Knowledge" component «Sapere» vs body «Conoscenza». | Re-sort/soften; «alta Conoscenza». |
| 222, 180, 236, 62, 358, 386, 348 (knockout), 748, 816, 958, 968, 952, 1008, 1046, 1194, 1274, 1290, 1298/1338, 1328, 1466, 1608, 1726, 1744, 1814, 1922, 2317, 2339, 2369/2463 | Low | Lexical/register polish, sé/se accent consistency (274 vs 342…), «cluster nucleari»→«nuclei», «accuditrice»→«custode», auto-organizzata hyphenation, pre-morte vs NDE, en dash+comma stacking (2339), floor/ceiling base vs pavimento. | Apply per-row it-0X fixes. |

### PT — Portuguese

| line | sev | issue | fix |
|------|-----|-------|-----|
| 180 | Med | Register mix: *tu* clitic «te» + *você* imperative «leia». | «Se isso o incomoda, por favor leia…». |
| 378 | Med | Ch2 callback dropped (§3). | Restore. |
| 492 | Med | Agreement: subject «a folha inteira» (fem) → «lançado» should be «lançada». | «lançada». |
| 700 vs 806 | Med | PCI full name English in Ch7, translated in Ch8. | Pick one; gloss once. |
| 834 | Med | Heading «modelo que combina bem demais» (EN "template") collides with FMT «modelo»; body uses «molde». | «o molde que combina bem demais». |
| 816 | Med | «ou bem, quando você está paralisado» parses as discourse marker, not "or fine when paralyzed". | «ou se sente bem quando está paralisado». |
| 998 | Med | "hair" split cabelo (head) vs pelo (body) breaks the fire/fur joke logic. | Use «pelos» throughout. |
| 1020, 1060, 1106 | Med | «estendida simples» word-order (→ «simplesmente estendida»); lone «split-brain» (book uses «cérebro dividido» 22×); «vem obcecando» inverts subject/object. | Fixes per pt-05. |
| 1280, 1300, 1316, 1338, 1320–1364 | Med | Stray comma (1280); «se sentem iguais» calque (1300); «discutivelmente» for "arguably" (1316); «NDE» unglossed → EQM (1338); "grip" preensão vs garra split (§4). | Apply pt-06 fixes. |
| 1548, 1550, 1670/1818/1834 | Med/High | 1550 truncation (§2 High); 1548 wrong regency «assemelhar-se com» + dropped "for a new expansion"; Popperian root flip (§3). | Fix regency + omission; standardize falsific- family. |
| 380, 416, 474, 498, 589, 748/816 (salvia), 784, 818/824/826, 878, 896/900/902, 942, 1018/1022, 1108, 1328, 1396, 1408, 1466, 1560/1782, 1706, 1724, 1774, 1822, 1596, 1818, 1882, 2295, 2453/2457 | Low | "but more so"→"em escala maior"; upload/carregado ambiguity; stray comma; "10 ou 40 Hz" range; border ownership; sálvia accent; obstacle-course wobble; síndrome capitalization; "leans toward" hardened; alter vs personalidade alternante; hall-of-mirrors two renderings; range-dash consistency; NDE; grip echo; "revoltante"; whether-clause calque; cross-checker→revisor; atop→através; step-like→abrupta. | Apply per-row pt-0X fixes. |

### ZH — Simplified Chinese

| line | sev | issue | fix |
|------|-----|-------|-----|
| 1396 | Med | Garbled apposition/stutter «一个候选，一个候选——…». | «拥有了一个候选——一个迄今为止对物理实在所提出的最根本描述的候选。» |
| 1452 | Med | Ch5 cross-ref dropped (§3). | Restore. |
| 1246/1258 vs 1324/1328 | Med | Libet Latin vs 利贝特 within one chapter; broader name-policy mix (Kühn/Brass/Wegner/Wheatley/Per Bak/'t Hooft/Susskind left Latin). | Unify: transliteration + Latin-in-parens on first mention. |
| 1524, 1800, 1558, 1808 | Med/Low | «————» quad em-dash typo → single «——»; 't Hooft/Susskind three renderings (§ name policy); 贝肯斯坦界限 vs book-dominant 贝肯斯坦上限; stacked-modifier translationese (1808). | Apply zh-07 fixes. |
| 378, 272… | Med | Ch2 callback (§3); Hard Problem 难问题 vs glossary 难题 (book uses 难问题 consistently — glossary decision, §5). | Restore callback; reconcile glossary. |
| 1000 | Med | «长出……皮层发展» redundant/ungrammatical. | Drop 发展. |
| 798/822 vs 902 | Med | Adrian Owen / Stanley Kubrick left raw Latin while other names transliterated. | Transliterate for parity. |
| 2174–2206 | Med | "Kolmogorov complexity" Latin ×4 vs 柯尔莫哥洛夫 ×1 (2181). | Standardize (recommend Latin form). |
| 970, 1016/1022, 1212, 1898 (added 124 signers + exact date not in EN), 1856 (顿号 misuse), 654, 672–678 (病感失认 drops 症), 508/532, 2226, 2323, spacing | Low | Hyperbole scaled down; bold-colon spacing; English titles italics vs 《》; **additive citation detail** (query — mandate says numbers stay untouched); 顿号 vs 逗号; anosognosia term; pangu spacing; Wolfram outlier transliteration; paper-title 《》. | Apply per-row zh-0X fixes. Note 1898 additive detail should be reconciled with EN. |
| 196, 162, 188, 86/240 | Low | Emphasis on 你 flattened; 的…的 stacking; 副框架 measure word; 演化 vs 进化. | Apply zh-01 fixes. |

---

## 5. Terminology & typography watch-list (enforce globally in the fix session)

### FMT term reconciliation decisions (DECIDE ONCE, APPLY BOOK-WIDE)

1. **"criticality"** — Romance manuscripts use the "-al-" calque (FR *criticalité*, ES *criticalidad*, PT *criticalidade*; IT is mostly on *criticità*). Every reviewer notes the calque is the **domain-standard rendering of *self-organized criticality*** and recommends **updating the glossary/term-sheet to the calque**, NOT a 70–107×/language find-replace. **Recommended: keep manuscripts, fix the term sheet.** Whatever is decided, it must be **book-wide per language** — no coexisting spellings. (ZH 临界性/自组织临界性 and JA 臨界性 are already clean.)

2. **"self-model" (generic)** — align each language's generic term with its named models and glossary:
   - FR: *modèle du soi* (not *auto-modèle*) — book mixes ~42× auto- vs 15× soi.
   - ES: glossary *modelo del yo*; manuscript uses *automodelo* consistently — reviewers call *automodelo* a defensible Metzinger rendering. Decide; apply once.
   - IT: *modello del sé* (reserve *automodello* for the *process* / to avoid «il modello del sé modella se stesso»).
   - PT: term sheet *modelo do eu*; manuscript uses *automodelo*. Decide; apply once.
   - Keep the **capitalized named models** (Modelo Explícito del Yo / ESM etc.) as-is — they are consistent everywhere.

3. **"Hard Problem"** — ZH: book uses 难问题 consistently (set Ch1 line 102); glossary says 难题. Reviewer recommends keeping 难问题 or aligning glossary. JA: ハード・プロブレム (nakaguro) vs ハードプロブレム/難問 — pick one form book-wide (ja-02/07/08). Romance: *Problème/Problema Difficile/Difícil* consistent — no action.

4. **EN/translation edition mismatch at line 678** (Explicit **World** vs **Self** Model) — see §2. **Resolve at the EN source of truth** and re-propagate; do not let EN + ES + IT disagree.

5. **"self-organized criticality"** hyphenation — IT «autoorganizzata» → «auto-organizzata» (1120/1316/1452 etc.); FR/PT/ES «auto-organisée/autoorganizada/autoorganizada» — apply each language's standard hyphenation.

6. **"neural signature" vs "neural fingerprint"** (Pred 1 vs Pred 9) — optional; JA preserves the contrast, Romance collapses it. Low priority.

7. **Popperian family** — PT: standardize on *falsific-* (falsificável/falsificação); IT/FR: check for the same flip.

### Name-rendering policy (enforce per language)

- **ZH:** one policy — transliteration + Latin in parens on **first** mention, then Chinese. Fix: **Chalmers** 戴维·查默斯 (not 大卫·查尔默斯, §2 High), **'t Hooft** 特·胡夫特 (not 特霍夫特/裸 't Hooft), **Susskind** 萨斯坎德, **Libet** 利贝特 consistently, **Owen/Kubrick** transliterate (阿德里安·欧文 / 斯坦利·库布里克).
- **JA:** fix **Kühn** キューン (not クーン — collides with Thomas Kuhn), **Thalia Wheatley** タリア・ウィートリー (not サリア・ウェットリー), **Landauer** ランダウアー (long vowel).
- **Chalmers** — verify the spelling is stable within each edition (ZH is the offender).

### Typography rules per language (enforce in the typesetting pass)

| lang | rules to enforce |
|------|------------------|
| **FR** | Guillemets « » with **narrow NBSP** (U+202F) inside and **NBSP** (U+00A0) before `: ; ! ?`; typographic apostrophe **’** (not `'`). babel-french does this for **print**; **verify the EPUB path** — pandoc does NOT. Decimal comma (4,5 not 4.5). |
| **ES** | «» guillemets; ¿ ¡; decimal comma; thousands = non-breaking thin space (not period): unify 85.000 vs 140 000. Replace English-style **spaced em dashes** with colon or hugging raya. Dial names bold-lowercase (not ALL-CAPS) unless small-caps convention. |
| **IT** | «» guillemets; decimal comma (Classe 4,5); em dash — spaced; **sé/se** accent convention picked once (Crusca favors accented *sé stesso*); no em-dash+comma stacking; auto-organizzata hyphen. |
| **PT** | **Curly "" (U+201C/U+201D)** per edition convention — PT-01 warns the pipeline does NOT auto-curl (DE pre-curls); **confirm the build applies smart quotes, else convert manuscript**. Decimal comma (4,5); en dash for numeric ranges (6–12); em dash —. |
| **ZH** | Full-width 。，、：？（） ; curly “”‘’ for quotes; **《》** for book/chapter titles (wrap the Gruber 2026 paper title and confirm foreign-title policy); —— single em-dash (no quad ————); Chinese numeral 30万 not Western 300,000; **one** Latin↔CJK spacing rule (pangu single space recommended) applied to all Latin tokens; 、 for lists only, 逗号 for clauses. |
| **JA** | Full-width （）「」 ; **full-width ？** not half-width; no half-width `)` closing a full-width `（` clause; katakana vs roman consistency (REM睡眠 vs レム睡眠 — pick one); ハード・プロブレム nakaguro decision; kanji vs Arabic numeral policy. |

### Build/pipeline verification checklist (do BEFORE per-line typography edits)

- [ ] **FR EPUB**: confirm NBSP + curly apostrophe are inserted at build. If not, add a `fr_nbsp` + `'→’` post-process. (Print PDF via babel-french is safe.)
- [ ] **PT quotes**: confirm smart-quote conversion runs. If not, convert `"…"` → `""` in the PT manuscript.
- [ ] **CJK emphasis**: EN uses italics for stress; slanted italics on Hanzi/Kana are typographically wrong. Decide once at pipeline level (bold or 着重号 for ZH; bold for JA).
- [ ] Confirm all six manuscripts render their **own** front-cover title at the Ch17 self-citation (only FR + JA are currently wrong).

---

*End of work-order. Priority order for the fix session: §2 (High, all) → §5 build-checklist → §3 cross-language clusters → §4 per-language.*
