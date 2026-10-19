<!-- Action: reference — judgment round DONE + all MG decisions applied (S262); kept as the per-language edit record for the human-native reviewer gate. Tracked-by: AIW-109. -->
<!-- Tracked-by: AIW-109. -->
# AIW-109 — Judgment review round results (S262, 2026-07-14, WSL)

The "another review round on the corrected manuscripts" MG asked for (S260/S261). Six Fable
native-editor agents, one per manuscript (no file collision), re-verified the deferred
lexical/name/grammar items against the CURRENT corrected text and applied only what was still open.
**All 6 manuscripts remain exactly 2475 lines — alignment invariant intact.** Model: Fable (cost-cleared by MG this session).

Uncommitted at time of this write → committed same session for crash safety.

## Per-language applied edits

- **FR (6):** Parfit tense-clash (passé simple→composé, L870); number-drift "seventy years" was rendered «trois quarts de siècle» (=75) → «soixante-dix ans» (=70) to match EN (L1606) [flagged — factual figure]; Cotard «syndrome»→«délire» ×2 (L670, L1850); «fabule/fabulation»→«confabule/confabulation» ×2 (L864, L890).
- **JA (3):** コスモロジー→宇宙論 ×3 (L1836/1846/1870) — the only open item; masked earlier by a head-truncated grep.
- **ES (9):** «de tus ojos»→«de tu cara» (L58); "one restart" negation fix «no produce un solo reinicio» (L1560); restored dropped "on this picture" hedge «—en esta imagen—» (L2333); «córtex»→«corteza» ×6 incl. glossary head-word (kept «neocórtex» compound).
- **IT (1):** «pre-morte»→«premorte» NDE-term harmonization (L1298). Everything else already correct.
- **PT (5 + CRITICAL):** **CRITICAL — the S260 High+Med pass (commit 52db8226) grip-standardization (`preensão→garra`) was a blind substring replace that corrupted «compreensão»→«comgarra»/«autocomgarra» at 8 sites** (L94/124/126/952/956/1076/2005/2015) — a real shipped non-word error, now restored to «compreensão»/«autocompreensão». Plus síndrome mid-sentence lowercase ×3 (L300/830/1304).
- **ZH (9):** de-stacked 你的…大脑的 heading (L162); 副框架→套框架 measure word (L188); bold-colon spacing ×4 (L946/1016/1018/1020); book/paper titles italic→《》 ×3 (L1212 Bobiverse, L1890 Die Emergenz, L2323 Gruber 2026 paper).

## needs_MG_decision (BUILD-BLOCKING review items — MG to rule before rebuild)

1. **FR "seventy years" (L1606):** applied faithful «soixante-dix ans» (=70, matches EN). If MG intended ≈75 (Feynman diagrams ~1948), revert AND fix the EN master to keep the line-aligned pair consistent.
2. **JA 仮想の自己/仮想自己 & 仮想の世界/仮想世界:** book-wide split (4:3 and 6:11); both valid; two parallel qualia definitions differ only by this. MG pick one register if desired. Also: 固有感覚 (body) vs 固有受容感覚 (glossary head-word) — unify glossary or keep as precise headword. Also kanji 我々 ×~8 in narrative/appendix vs 私たち elsewhere (exclude book title 『われらはレギオン』).
3. **ES capitalization «Capítulo N» vs «capítulo N»:** systemic split (uppercase dominant in body/TOC, lowercase in appendix + ~20 body sites). One-way global decision — recommend uppercase. Also dialect: manuscript is LatAm-neutral; «camarero» is pan-Hispanic (recommend keep). «introspeccionar» calque left (transparent, consistent).
4. **IT:** «accuditrice» (caregiver, warm) vs suggested «custode» (keeper, cold) — kept accuditrice; «cluster nucleari» kept (faithful to EN "nuclear clusters"). Confirm.
5. **PT grip metaphor «garra»:** the preensão↔garra split is resolved (all «garra», internally consistent) but «garra» = claw/grit, not grip/purchase-on-the-world. A more idiomatic word (alavanca/controle/domínio) needs a deliberate 6-site pass — not imposed. Also «indiscutivelmente» for "arguably" asserts where EN hedges — confirm or soften to «possivelmente».
6. **ZH:** 演化 ×14 vs 进化 ×8 — recommend unify to 演化 (neutral, non-teleological); the 8 进化 lines listed. Kolmogorov now uniformly Latin (matches recommendation — confirm). Kühn/Brass/Wegner/Wheatley/Per Bak left raw Latin (book has an established in-body Latin author-year citation style) — transliterate for parity only if MG wants (note 库恩 already = Thomas Kuhn, so Kühn needs a distinct form). pangu 年-spacing split (35 glued vs 16 spaced) — recommend glued as its own typography sweep.

## Decisions RESOLVED + applied (MG, S262 2026-07-14)
All build-blocking judgment items ruled by MG ("a and go with your recs") and applied via 4 Fable agents (own file each, substring-swap guard enforced). All 6 manuscripts remain 2475 lines.
- **FR:** option (a) — keep «soixante-dix ans» (70, faithful to EN). Already applied; no change.
- **ES:** uppercase «Capítulo N» standardized (30 refs across 26 lines; plurals «capítulos» + generic uses correctly skipped). «camarero» + «introspeccionar» kept.
- **ZH:** 进化 → 演化 unified (13 occurrences, 0 remaining; 进化论证→演化论证 handled as 进化+论证). Kolmogorov kept Latin; Western author names kept Latin (book's citation style).
- **JA:** glossary head-word 固有受容感覚 → 固有感覚（Proprioception）; parallel qualia definition (L396) aligned to の-form; narrative/appendix 我々 → 私たち (12 occ across 8 lines); book title 『われらはレギオン』 preserved.
- **IT:** keep «accuditrice» + «cluster nucleari» (no change — faithful to EN).
- **PT:** «indiscutivelmente» → «possivelmente» (restores the "arguably" hedge, L1166); «garra» → «domínio» ×6 (EN image = causal purchase/leverage, not claw/grit; «controle» avoided to preserve EN's control/grip distinction).

**Manuscripts are now text-FINAL for ed.2.** Next = build-level typography pass, then build & ship.

## Remaining path (unchanged from handoff, after MG rules on the above)
1. Build-level typography pass (pipeline): FR EPUB narrow-NBSP U+202F + curly apostrophe ’; CJK italics→bold emphasis (JA+ZH); PT quotes auto-curl (confirmed OK — pandoc smart).
2. Flip edition marker First→Second (PRINT copyright page only; eBooks keep © 2026).
3. Rebuild 8 print interiors + 7 eBooks; ZH via PublishDrive kit.
4. Re-upload (MG-manual). Human-native reviewer gate per language before "final".

## Agent handles (SendMessage to continue with full context)
FR a18fa49f1134033ea · JA a9fccfc575227b659 · ES a249f4fad9d9178c1 · IT af57d1e5b99ca0aa9 · PT a9b8d2844f08e2616 · ZH a8b58d6ceb9fae410
