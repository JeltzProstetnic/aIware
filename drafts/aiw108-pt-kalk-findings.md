# AIW-108 — PT-BR Kalk-scan findings (native-Portuguese calque/naturalness sweep)

Session 252, 2026-07-08. Method: 36 parallel **Opus 4.8** native-Brazilian-Portuguese editors (Fable on token-conserve
per MG S252) over the whole `pop-sci/book-manuscript-pt.md` (36 segments), surgical A/B/C/D findings only, scanning
calques of BOTH sources (EN **and** DE — one Spanish-calque leak «superviene» was also caught), false friends,
collocations, BR orthography, glossary/typography/reader-address violations, awkwardness.
**127 findings: A=83, B=39, C=5, D=0.**

## A. APPLIED — 83 objective fixes (of 83)
Applied via verified match-once script (`tmp/kalk_apply.py`). Meaning-preserving. Full list `tmp/pt-kalk/a_all.json`;
git diff. By type: anglicism×29, fluency×19, collocation×15, false-friend×8, reader-address×5, glossary×4, orthography×2, calque×1.
(all A-items applied)

## B. HELD for MG — voice/style/meaning judgment calls (39)
- **[seg 02 · anglicism]** "O estado atual do jogo"
  → proposta: "A situação atual do debate"
  — Calque of EN 'state of play' as heading; deliberate sports metaphor follows, so hold.
- **[seg 03 · register]** "Se isso o incomoda, por favor leia"
  → proposta: "Se isso te incomoda, por favor leia"
  — "o" clitic is correct but formal; "te" fits the warm "você" register better. HOLD.
- **[seg 04 · glossary]** "o personagem que o cérebro escreve dentro da própria simulação"
  → proposta: "o personagem que o cérebro cria dentro da própria simulação"
  — Glossary fixes 'o personagem que o cérebro cria'; 'escreve' drifts, but 'writes into' may be intentional.
- **[seg 04 · fluency]** "e de outro para assistir ao processamento acontecer"
  → proposta: "e de outro para ver o processamento acontecer"
  — 'assistir a X acontecer' leans anglicism; 'ver' is more natural for watching a process unfold.
- **[seg 06 · anglicism]** "arrancar o display do painel de um cockpit"
  → proposta: "arrancar o display do painel de uma cabine"
  — English "cockpit" plus "display"; consider "cabine". Held — aviation register may want it.
- **[seg 08 · fluency]** "Guarde esses dois mostradores em mente"
  → proposta: "Tenha esses dois mostradores em mente"
  — 'guardar em mente' echoes EN 'keep in mind'; 'ter em mente' is more idiomatic BR
- **[seg 09 · fluency]** "Eu era jovem, e tolo, e tive sorte."
  → proposta: "Eu era jovem, tolo, e tive sorte."
  — comma-before-"e" chain mirrors English "young, and foolish, and" rhythm.
- **[seg 09 · anglicism]** "os blocos de construção que ele normalmente usa"
  → proposta: "os tijolos com que ele normalmente constrói"
  — "blocos de construção" calques "building blocks"; "tijolos" more idiomatic.
- **[seg 09 · anglicism]** "Os psicodélicos atuam no meio da pilha"
  → proposta: "Os psicodélicos atuam no meio dos níveis empilhados"
  — "pilha" for "the stack" reads as computing calque here.
- **[seg 10 · collocation]** "Fazer as duas coisas ao mesmo tempo é metabolicamente ruinoso"
  → proposta: "Fazer as duas coisas ao mesmo tempo é metabolicamente proibitivo"
  — "ruinoso" = causing ruin; calques EN "ruinous" for costly; "proibitivo" fits cost sense.
- **[seg 11 · anglicism]** "a consciência rodando com input *errado*"
  → proposta: "a consciência rodando com uma entrada *errada*"
  — "input" anglicism recurs; consistency choice held for author (keep vs Portuguese).
- **[seg 11 · collocation]** "Os modelos implícitos comandam o espetáculo"
  → proposta: "Os modelos implícitos estão no comando"
  — Calque of "run the show"; "comandam o espetáculo" reads slightly literal.
- **[seg 12 · fluency]** "se lê como um filme de terror"
  → proposta: "que parece um filme de terror"
  — "se lê como" lightly calques "reads like"; softer BR = parece/lembra. Voice call.
- **[seg 14 · collocation]** "soa como um salão de espelhos"
  → proposta: "soa como uma casa de espelhos"
  — BR funhouse idiom is 'casa de espelhos'; 'salão de espelhos' is a mild calque.
- **[seg 15 · anglicism]** "davam suporte a uma autossimulação mais rica"
  → proposta: "sustentavam uma autossimulação mais rica"
  — 'dar suporte a' = mild calque of 'support'; 'sustentavam' cleaner. Voice call.
- **[seg 15 · glossary]** "é o blindsight do Capítulo 8"
  → proposta: "é a visão cega do Capítulo 8"
  — 'blindsight' kept in EN; standard PT term is 'visão cega'. Author decides.
- **[seg 17 · false-friend]** "é, sem dúvida, o problema não resolvido mais profundo"
  → proposta: "é, indiscutivelmente, o problema não resolvido mais profundo"
  — If EN was 'arguably', 'sem dúvida' inverts the hedge; clashes with hedged register.
- **[seg 17 · register]** "E eis o que me impactou quando voltei por completo"
  → proposta: "E eis o que me marcou quando voltei por completo"
  — 'me impactou' reads as anglicism; 'me marcou' is stronger literary BR register.
- **[seg 18 · collocation]** "seu traje de carne"
  → proposta: "seu invólucro de carne"
  — 'traje de carne' calques EN 'flesh suit'; authorial image, held for MG.
- **[seg 19 · fluency]** "A resposta cai direto da analogia do relógio"
  → proposta: "A resposta decorre diretamente da analogia do relógio"
  — Calque of 'falls right out of'; segment elsewhere uses 'decorre'.
- **[seg 19 · collocation]** "o comportamento molda o mundo — e essa alça gira devagar"
  → proposta: "o comportamento molda o mundo — e esse laço gira devagar"
  — 'alça' breaks the loop term; 'laço' used for every other loop here.
- **[seg 21 · fluency]** "não pode espontaneamente começar a pensar"
  → proposta: "não pode começar a pensar espontaneamente"
  — Adverb wedged between modal and verb — English/German word order; end-position is more natural BR.
- **[seg 21 · collocation]** "onde ele cai no espectro das cinco classes"
  → proposta: "onde ele se situa no espectro das cinco classes"
  — "cair no espectro" mildly calques "fall on the spectrum"; "se situa/se encaixa" reads more native.
- **[seg 22 · fluency]** "o chão me carregando através do escuro"
  → proposta: "o chão me carregando pela escuridão"
  — "através do" reads as calque of "through the dark"; "o escuro" recurs as motif so noun kept
- **[seg 22 · collocation]** "superfícies de fronteira operando em capacidade máxima"
  → proposta: "superfícies de fronteira operando com capacidade máxima"
  — "em capacidade máxima" mildly anglicized; BR prefers "com capacidade máxima"
- **[seg 23 · anglicism]** "os blocos de construção da matéria"
  → proposta: "os elementos fundamentais da matéria"
  — Mild calque of "building blocks" (recurs 3x); understood but EN-ish — voice call, held.
- **[seg 24 · anglicism]** "um dos insights mais profundos da física teórica"
  → proposta: "uma das ideias mais profundas da física teórica"
  — 'insights' anglicism; naturalized in BR pop-sci but 'ideias/percepções' more idiomatic.
- **[seg 24 · collocation]** "os rostos de predadores e presas"
  → proposta: "as faces de predadores e presas"
  — 'rosto' is human-specific in careful PT; animals take 'face/focinho'.
- **[seg 25 · calque]** "E se isso não faz você querer se sentar"
  → proposta: "E se isso não te faz sentar por um instante"
  — 'makes you want to sit down' is an English idiom that lands weakly in BR PT; voice call.
- **[seg 26 · register]** "quase absurdamente simples"
  → proposta: "quase absurdamente simples"
  — Faithful to EN "almost absurdly simple"; grandeur call held for author, no change needed.
- **[seg 27 · collocation]** "e o construtor nunca piscou"
  → proposta: "e o construtor nem pestanejou"
  — "nunca piscou" is a literal calque of "never blinked"; BR idiom is "nem pestanejou".
- **[seg 27 · collocation]** "editor e revisor cruzado ao longo de todo"
  → proposta: "editor e revisor ao longo de todo"
  — "revisor cruzado" calques "cross-reviewer"; plain "revisor" is idiomatic.
- **[seg 29 · collocation]** "Eu tinha batido numa parede que não tinha nada a ver com capacidade"
  → proposta: "Eu tinha esbarrado num muro que não tinha nada a ver com capacidade"
  — "batido numa parede" reads as EN "hit a wall" idiom calque; verify voice.
- **[seg 29 · fluency]** "Aqui vou expô-lo como se deve"
  → proposta: "Aqui vou apresentá-lo como merece"
  — "expô-lo como se deve" is slightly stiff; author voice call.
- **[seg 31 · collocation]** "produz um gradiente monotônico limpo: 1"
  → proposta: "produz um gradiente monotônico nítido: 1"
  — 'limpo' for EN 'clean gradient' reads as anglicism; 'nítido/claro' more natural.
- **[seg 33 · collocation]** "como seus dedos devem se moldar para a pegada"
  → proposta: "como seus dedos devem se moldar para agarrá-la"
  — 'pegada' (grip/footprint) is awkward for grasping a cup.
- **[seg 33 · anglicism]** "quanto o layout do ambiente"
  → proposta: "quanto a disposição do ambiente"
  — 'layout' is an English borrowing; 'disposição/traçado' reads more literary.
- **[seg 33 · collocation]** "neurônios que disparam sobre redes proteômicas"
  → proposta: "neurônios que disparam através de redes proteômicas"
  — 'disparar sobre' reads as 'fire upon/at'; ambiguous for firing across a substrate.
- **[seg 34 · fluency]** "E então há o mistério das três gerações"
  → proposta: "E há também o mistério das três gerações"
  — "E então há" mirrors EN "And then there's"; sequencing+existential reads translated.

## C. KEPT as-is — deliberate recurring motifs (5)
- **[seg 02 · motif]** "por que ler é algo que se sente"
  — Core 'feels like something' motif; rendered with variation across segment — keep, do not normalize.
- **[seg 07 · motif]** "O meio segundo de ninguém em casa não foi uma pane"
  — Callback to the established 'gap/absence-of-self' image; reads idiomatically in BR — protect, do not 'correct'.
- **[seg 12 · motif]** "recebe input visual por vias subcorticais"
  — "input" is the segment's consistent technical loan (7x) — protect, do not nativize to "entrada".
- **[seg 15 · motif]** "Eles não desligam o renderizador"
  — 'renderizador/renderiza' = deliberate rendering/simulation motif; do NOT correct.
- **[seg 20 · motif]** "quem sabe se você volta, e quantos de você"
  — Locked verbatim ch.14 danger-line motif (glossary §3) — flag so it is NOT altered.

## Phase-4 mechanical consistency — PASS (+1 consistency item for the human pass)
- Reader-address: "você" ×352. The 4 remaining "o leitor / leitores" hits are legitimate "for readers who want the
  detail" appendix pointers (subset reference, matches the EN), NOT third-person distancing. The one genuine
  distancing case ("a maioria dos leitores faz") was fixed (category A).
- Typography: 0 «guillemets» — correct; BR primary is "aspas duplas".
- Model abbreviations IWM/EWM/ISM/ESM + FMT intact; "Teoria dos Quatro Modelos" ×47. 0 Spanish-calque leaks remain.
- **CONSISTENCY ITEM for the human native pass:** the loanword "input" occurs ~16× (input visual/auditivo/retiniano/
  externo/interno, o input, seu input). BR academic Portuguese tolerates "input", but the scan preferred "entrada"
  throughout. NOT auto-swept because "entrada" is FEMININE (o input → a entrada; input auditivo → entrada auditiva)
  and a blind replace would break gender agreement. Recommend the human reviewer normalize input→entrada with correct
  agreement if desired — it is a preference, not an error.

**Status:** PT-BR = **publish-candidate**. Gate: human native Brazilian-Portuguese review before any KDP upload.


## Extra pass (S252) — checklist-primed 2nd scan (Opus, 54 finer segments)
MG-directed because Opus under-found vs Fable on the shared source-calque clusters. Primed each agent with
`tmp/shared-calque-checklist.txt` (recurring EN/DE source calques extracted from the ES/Fable findings). Result:
**+144 A-findings** (vs 83 in the 1st pass) → **135 applied** after a malformed-fix quarantine
(5 quarantined for MG: agents wrote "orig → proposed" into the fix field). New held: **128 B, 0 D, 16 C**.
All extra held items are in the inline-review file `drafts/aiw108-review-pt.txt`.
