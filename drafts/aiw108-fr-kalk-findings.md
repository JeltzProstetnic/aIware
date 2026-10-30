# AIW-108 — FR Kalk-scan findings (native-French calque/naturalness sweep)

Session 252, 2026-07-08. Method: 36 parallel **Opus 4.8** native-French editors (Fable on token-conserve per MG S252)
over the whole `pop-sci/book-manuscript-fr.md` (36 segments), surgical A/B/C/D findings only, scanning calques of BOTH
sources (EN **and** DE), false friends, collocations, glossary/typography/reader-address violations, awkwardness.
**114 findings: A=84, B=23, C=4, D=3.**

## A. APPLIED — 82 objective fixes (of 84)
Applied via verified match-once script (`tmp/kalk_apply.py`). Meaning-preserving. Full list `tmp/fr-kalk/a_all.json`;
visible in git diff. By type: fluency×30, anglicism×21, collocation×17, false-friend×11, germanism×2, glossary×2, typography×1.

### A-items NOT auto-applied (2) — for the human native reviewer
- **[seg 15 · fluency]** « un EWM rudimentaire avec un ESM minimal »
  → proposition : « un EWM rudimentaire avec un ESM minimal »
  — "un" before vowel-acronym is fine here; no change needed — flag withdrawn.
- **[seg 15 · false-friend]** « des choses qui ne sont pas actuellement visibles »
  → proposition : « des choses qui ne sont pas visibles à cet instant »
  — "actuellement" = currently, but reads as false-friend echo of "currently"; ambiguous — clarify.

## B. HELD for MG — voice/style/meaning judgment calls (23)
- **[seg 02 · germanism]** « livre un plan de construction concret pour une machine authentiquement consciente »
  → proposition : « livre un schéma concret pour construire une machine authentiquement consciente »
  — "plan de construction" echoes German Bauplan; "schéma pour construire" reads more natively. Held for author.
- **[seg 04 · fluency]** « un grand reconnaisseur de motifs »
  → proposition : « un grand détecteur de motifs »
  — 'reconnaisseur' is an awkward neologism for 'pattern recognizer'.
- **[seg 04 · anglicism]** « un modèle de ce qui est là-dehors »
  → proposition : « un modèle de ce qui existe au-dehors »
  — 'là-dehors' = colloquial calque of 'out there'; borderline register.
- **[seg 05 · anglicism]** « dispose de la base de preuves la plus solide »
  → proposition : « dispose des données probantes les plus solides »
  — 'base de preuves' calques 'evidence base'; FR prefers 'données probantes'.
- **[seg 05 · anglicism]** « **Le forking.** »
  → proposition : « **La bifurcation (le « forking »).** »
  — English gerund as heading; consider glossing the FR term. Judgment call vs CS-motif.
- **[seg 06 · anglicism]** « c'est du Dennett avec des étapes supplémentaires »
  → proposition : « c'est du Dennett en plus alambiqué »
  — "avec des étapes supplémentaires" is a literal calque of the English idiom "with extra steps"; voice call, hold for author.
- **[seg 07 · collocation]** « l'érudit polymathe Stephen Wolfram »
  → proposition : « le polymathe Stephen Wolfram »
  — Redundant: a polymath is by definition erudite; "érudit polymathe" doubles up.
- **[seg 07 · anglicism]** « les états de flow l'amincissent »
  → proposition : « les états de flux l'amincissent »
  — "flow" is an English loan; widely used but author may prefer "flux".
- **[seg 07 · fluency]** « La demi-seconde de « personne à la maison » »
  → proposition : « La demi-seconde de « vide », de personne aux commandes »
  — "personne à la maison" calques EN "nobody home"; idiom doesn't carry in FR.
- **[seg 08 · fluency]** « C'est la fuite de perméabilité à l'œuvre »
  → proposition : « C'est la fuite due à la perméabilité, à l'œuvre »
  — "fuite de perméabilité" reads as opaque calque; may be a recurring motif — hold.
- **[seg 10 · fluency]** « C'est la salvia divinorum qui le démontre de la manière la plus spectaculaire, un psychédélique dissociatif qui »
  → proposition : « La salvia divinorum le démontre de la manière la plus spectaculaire. C'est un psychédélique dissociatif qui »
  — English-style dangling apposition far from its noun; split reads more naturally in FR.
- **[seg 10 · fluency]** « est cette affection où les patients ne perçoivent »
  → proposition : « est une affection où les patients ne perçoivent »
  — Demonstrative 'cette' implies a known referent; 'une' fits a first definition.
- **[seg 16 · fluency]** « peut y accéder et le réadresser »
  → proposition : « peut y accéder et le réorienter »
  — 'réadresser' (=forward a letter) is odd for redirecting the self; unclear.
- **[seg 17 · anglicism]** « Juste : ici, puis là. »
  → proposition : « Simplement : ici, puis là. »
  — 'Juste :' as sentence-opener echoes English 'Just:'; 'Simplement' matches earlier usage
- **[seg 18 · collocation]** « C'est la recette d'une souffrance à une échelle »
  → proposition : « C'est le terreau d'une souffrance à une échelle »
  — 'recette de' echoes EN 'recipe for'; vivid, held for author
- **[seg 19 · register]** « capable de computation universelle »
  → proposition : « capable de calcul universel »
  — "computation" as a FR noun is anglicizing; standard term is "calcul" (adjective "computationnel" stays).
- **[seg 20 · collocation]** « il faudra que quelqu'un cloue la chose au sol »
  → proposition : « il faudra que quelqu'un élucide définitivement la question »
  — 'clouer au sol' calques 'nail it down'; odd for pinning a mechanism.
- **[seg 21 · anglicism]** « La réponse, je vais le soutenir, se détermine par élimination »
  → proposition : « La réponse, comme je vais le montrer, se détermine par élimination »
  — 'je vais le soutenir' calques 'I will argue'; incise reads awkward.
- **[seg 25 · fluency]** « si cela ne vous donne pas envie de vous asseoir »
  → proposition : « si cela ne vous coupe pas le souffle »
  — Calque of EN "want to sit down" idiom; doesn't carry in FR. Author's striking image — HOLD.
- **[seg 28 · anglicism]** « Le TDI comme forking de modèle virtuel »
  → proposition : « Le TDI comme bifurcation de modèle virtuel »
  — Bare English gerund 'forking' unassimilated in FR prose; recurs — francize or keep? Author call.
- **[seg 28 · anglicism]** « la fenêtre développementale du forking est originale »
  → proposition : « la fenêtre développementale de la bifurcation est originale »
  — Same English 'forking'; must match the choice made above for consistency.
- **[seg 32 · anglicism]** « pour peupler les modèles »
  → proposition : « pour alimenter les modèles »
  — 'peupler'=calque of 'populate'; 'alimenter/remplir' reads more natural computationally.
- **[seg 34 · collocation]** « ce serait un indice puissant en faveur de l'ensemble du cadre »
  → proposition : « ce serait un indice fort en faveur de l'ensemble du cadre »
  — 'indice puissant' mildly calques EN 'powerful hint'; FR prefers 'indice fort'.

## D. CULTURAL-GRANDEUR flags — MG's call (3)
- **[seg 02 · grandeur]** « formule des prédictions qu'aucune théorie concurrente ne peut égaler »
  → proposition : « formule des prédictions que les théories concurrentes ne parviennent pas à formuler »
  — Full EN self-promotion register; FR should sit at warm middle. Hold for author.
- **[seg 08 · grandeur]** « ce serait le plus beau fait jamais découvert »
  → proposition : « ce serait l'une des plus belles découvertes jamais faites »
  — Superlative hype ("most beautiful fact ever") — flag tone for author.
- **[seg 08 · grandeur]** « la plus importante question non résolue des mathématiques »
  → proposition : « l'une des plus importantes questions non résolues des mathématiques »
  — Grand absolute claim; consider softening toward warm middle — hold.

## C. KEPT as-is — deliberate recurring motifs (4)
- **[seg 01 · motif]** « pourquoi quoi que ce soit fait l'effet de quelque chose »
  — 'fait l'effet de' = recurring 'feels like something' motif (cf. Ch.4 title); keep.
- **[seg 02 · motif]** « la raison pour laquelle lire fait l'effet de quelque chose »
  — "fait l'effet de quelque chose" = the recurring "what it's like" motif; deliberate, do not normalize.
- **[seg 16 · motif]** « à côté du phénomène sur lequel elle joue sa vie »
  — Deliberate 'theory stakes its life' motif (falsifiability = agreeing to die).
- **[seg 20 · motif]** « qui sait si vous reviendrez, et combien de vous »
  — Locked ch.14 danger-line motif (glossary §3); keep, do not correct.

## Phase-4 mechanical consistency — PASS
- Reader-address: vouvoiement (« vous ») consistent. The single « tu » hit is Uncle Bruno's reported dialogue (correct).
- Typography: « guillemets » primary present throughout.
- Model abbreviations IWM/EWM/ISM/ESM + FMT intact; « Théorie des Quatre Modèles » ×47.

**Status:** FR = **publish-candidate**. Gate: human native French review before any KDP upload.


## Extra pass (S252) — checklist-primed 2nd scan (Opus, 54 finer segments)
MG-directed because Opus under-found vs Fable on the shared source-calque clusters. Primed each agent with
`tmp/shared-calque-checklist.txt` (recurring EN/DE source calques extracted from the ES/Fable findings). Result:
**+141 A-findings** (vs 82 in the 1st pass) → **133 applied** after a malformed-fix quarantine
(4 quarantined for MG: agents wrote "orig → proposed" into the fix field). New held: **143 B, 1 D, 22 C**.
All extra held items are in the inline-review file `drafts/aiw108-review-fr.txt`.
