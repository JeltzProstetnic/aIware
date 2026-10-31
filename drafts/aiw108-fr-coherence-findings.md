# AIW-108 — FR whole-book COHERENCE pass (temporal fluency & consistency)

Session 252, 2026-07-08. Method: ONE Opus agent read `pop-sci/book-manuscript-fr.md` start-to-finish in order —
the class of issue the parallel per-segment Kalk scan cannot see (each segment edited blind; book was restructured).
**14 issues** — by type: term-re-explanation, result-before-question, dangling-reference, temporal-discontinuity,
consistency-drift. **scope=structural** means the issue was likely inherited from the EN/DE ed.2 restructure and so
probably affects ALL editions (EN/DE/ES/FR/PT) — worth checking upstream, not just in FR.

## 1. [consistency-drift] · severity=medium · scope=fr-only
- **Where:** Table des matières (l. 19) vs Chapitre 3 titre (l. 250)
- **Anchor:** « Chapitre 3 : Le versant virtuel »
- **Issue:** La table des matières annonce « Chapitre 3 : Le versant virtuel », mais le titre réel du chapitre est « Chapitre 3 : Le côté virtuel ». Un lecteur linéaire qui revient à la table des matières ne retrouve pas le titre. C'est le symptôme visible d'une hésitation lexicale plus large entre « versant » et « côté » pour désigner les deux faces réel/virtuel.
- **Suggestion:** Uniformiser le titre du chapitre et l'entrée de la table des matières (choisir « versant » OU « côté », de préférence « versant » puisque c'est le terme dominant dans le corps du chapitre 3 lui-même — l. 306).

## 2. [consistency-drift] · severity=medium · scope=fr-only
- **Where:** Chapitre 2 (l. 198, 206-216) et Chapitre 3 (l. 250, 280, 328-338)
- **Anchor:** « ### Le côté réel et le côté virtuel »
- **Issue:** Les deux faces de l'architecture sont nommées de deux façons interchangeables sans règle apparente : « versant réel/virtuel » (l. 206-216, la majorité) et « côté réel/virtuel » (titre de section l. 198, titre du ch. 3 l. 250, l. 336-338, récap. l. 1824). Le chapitre 2 introduit d'abord la paire sous le titre « le côté réel et le côté virtuel » (l. 198) puis bascule immédiatement sur « versant » dans le corps (l. 206). Pour un terme aussi central, répété des dizaines de fois, cette oscillation use le lecteur et brouille l'impression qu'il s'agit d'un concept technique fixe.
- **Suggestion:** Choisir un seul terme (« versant » est le plus fréquent et le plus imagé) et l'imposer partout : titres de section, titre du ch. 3, corps de texte, légendes de figures et récapitulatif du ch. 17. Réserver « côté » aux emplois non techniques.

## 3. [consistency-drift] · severity=medium · scope=structural
- **Where:** Coda (l. 1850-1856) vs Chapitre 13 (l. 1290-1296) et Chapitre 12 (l. 1150)
- **Anchor:** « J'ai frôlé la mort. Dans une avalanche »
- **Issue:** La Coda re-raconte in extenso trois anecdotes autobiographiques déjà pleinement narrées plus tôt : l'avalanche avec revue de vie (ch. 13, l. 1290-1294 — « décision imprudente d'un officier », « quatorze d'entre nous ») et le knock-out avec amnésie/redémarrage de l'ESM (ch. 12, l. 1150). Dans un livre lu linéairement d'un bout à l'autre, ces re-narrations arrivent très près de leur première occurrence (l'avalanche est même racontée deux fois au ch. 13, l. 1290 puis 1294) et donnent une impression de radotage plutôt que de rappel maîtrisé.
- **Suggestion:** Dans la Coda, compresser ces rappels en une phrase allusive qui s'appuie sur ce que le lecteur a déjà lu (« l'avalanche du chapitre 13, le knock-out du chapitre 12 ») au lieu de re-planter le décor complet. Garder seulement l'angle neuf de la Coda (l'ESM comme constructeur qui donne priorité au substrat).

## 4. [consistency-drift] · severity=medium · scope=fr-only
- **Where:** Chapitre 10 (l. 908-946) — genre grammatical d'« orque »
- **Anchor:** « un orque mâle, énorme, a surgi »
- **Issue:** Le mot « orque » oscille en genre dans le même passage : masculin à l'ouverture (« un orque mâle », l. 908 ; « il — je ne trouve pas d'autre mot — a parlé », l. 908) puis féminin ensuite (« Si cette orque était quelqu'un », l. 912 ; « L'orque qui a ouvert ce chapitre », l. 946 — ici masculin « l'orque... était l'un de ces esprits »). En français « orque » est usuellement féminin ; le récit vise un mâle, d'où le flottement. Le lecteur linéaire bute sur le changement de genre à quelques lignes d'intervalle.
- **Suggestion:** Fixer le genre : soit garder « une orque » (féminin standard) tout du long en précisant « une orque mâle », soit assumer le masculin « un orque » partout. Ne pas alterner « un orque » (l. 908) et « cette orque » (l. 912) dans le même récit.

## 5. [dangling-reference] · severity=medium · scope=structural
- **Where:** Chapitre 5 (l. 554)
- **Anchor:** « J'y reviendrai au chapitre 14, où j'expliquerai pourquoi je pense que la Relation 3 »
- **Issue:** Le chapitre 5 promet que la Relation 3 (automate à structure de règles holographique) sera reprise « au chapitre 14 ». Le développement réel de cette conjecture se fait effectivement au chapitre 14 (section « La conjecture automate-hologramme », l. 1374-1396), donc le renvoi tient — MAIS le chapitre 4 (l. 554 est dans le ch.5) et le passage du ch.5 l.554 renvoient au « chapitre 14 » pour la question, puis « chapitres 15 à 17 » pour la réponse ; or au chapitre 14 (l. 1416) l'auteur re-décrit « trois relations possibles » comme s'il les posait à neuf (« J'ai décrit trois relations possibles... et j'ai posé la question la plus difficile »), reprenant quasi mot pour mot le ch. 5. Le lecteur linéaire relit une exposition qu'il connaît déjà.
- **Suggestion:** Au chapitre 14, transformer la ré-exposition des trois relations en rappel condensé (« les trois relations du chapitre 5 — substrat holographique, sortie holographique, règles holographiques ») au lieu de les re-déployer, puisque le renvoi du ch. 5 avait déjà promis ce retour.

## 6. [dangling-reference] · severity=medium · scope=structural
- **Where:** Chapitre 4 (l. 418) — « branches plus anciennes de cette tradition »
- **Anchor:** « Nous avons déjà rencontré dans ce livre les branches plus anciennes de cette tradition — l'auto-modèle de Metzinger, le soi narratif de Dennett »
- **Issue:** Le chapitre 4 (l. 418) affirme « Nous avons déjà rencontré dans ce livre... l'auto-modèle de Metzinger, le soi narratif de Dennett ». Or dans le corps du texte lu jusque-là (ch. 1-4), ni Metzinger ni Dennett ne sont nommés : Metzinger n'apparaît nommément qu'à la ligne 414 (même chapitre, quelques lignes plus haut, via « transparence phénoménale ») et Dennett qu'au ch. 4 sur l'illusionnisme (l. 392). Ils ne sont pas « déjà rencontrés » dans un chapitre antérieur — ils viennent d'être introduits dans le même chapitre. Le « déjà rencontré dans ce livre » surestime ce que le lecteur linéaire a vu.
- **Suggestion:** Remplacer « Nous avons déjà rencontré dans ce livre » par « comme je viens de l'évoquer » ou « ces branches plus anciennes de la tradition — l'auto-modèle de Metzinger, le soi narratif de Dennett », sans prétendre à une rencontre antérieure qui n'a pas eu lieu.

## 7. [temporal-discontinuity] · severity=medium · scope=structural
- **Where:** Chapitre 6 (l. 600) vs Chapitre 5 (l. 508-518)
- **Anchor:** « La voie de la méditation, que j'ai décrite au chapitre précédent »
- **Issue:** Au chapitre 6 (l. 600) l'auteur renvoie à « la voie de la méditation, que j'ai décrite au chapitre précédent (une pièce sombre, une attention détendue, de la patience) ». Or au chapitre 5 (l. 508-520) l'exercice de la pièce sombre n'est jamais présenté comme de la « méditation » — il est décrit comme une observation directe de l'automate cortical (« observer l'automate cortical directement »). Le lecteur linéaire ne reconnaît pas immédiatement la technique sous l'étiquette « méditation », car le mot n'a pas été employé au ch. 5.
- **Suggestion:** Soit introduire le mot « méditation » au chapitre 5 lors de la description de l'exercice en pièce sombre, soit, au chapitre 6, reformuler le renvoi (« l'exercice de la pièce sombre du chapitre précédent ») pour que le lecteur retrouve exactement ce qui a été décrit.

## 8. [consistency-drift] · severity=low · scope=structural
- **Where:** Chapitre 11 (l. 1054-1056) — statut de la commentaire BBS / prédictions déjà croisées
- **Anchor:** « Vous avez déjà croisé la plupart des autres, même si je ne me suis pas toujours arrêté pour les montrer du doigt »
- **Issue:** Le chapitre 11 (l. 1054-1056) affirme que le lecteur a « déjà croisé la plupart des autres [prédictions] » et cite « les prédictions sur l'anesthésie et le sommeil » (ch. 7), « le cerveau divisé et l'identité dissociative » (ch. 9). C'est cohérent. Mais la Prédiction 4 (anosognosie + psychédéliques, annexe H l. 2387) et la prédiction sur l'anosognosie n'ont PAS été posées comme « prédiction » dans le corps — au ch. 6 (l. 686-688) le lien psychédéliques/anosognosie est présenté comme « une prédiction transversale... Personne ne l'a jamais testé ». Donc elle a été croisée, mais l'affirmation globale « chacune posée là où elle a sa place, à côté du phénomène » est légèrement optimiste pour les prédictions 1 et 7 (signatures neuronales des 4 modèles ; construire la machine) qui ne sont pas clairement étiquetées « prédiction » avant l'annexe H.
- **Suggestion:** Nuancer l. 1056 : distinguer les prédictions effectivement mises en scène dans les chapitres (sommeil, anesthésie, split-brain, TDI, dissolution de l'ego) de celles qui n'apparaissent formellement qu'à l'annexe H (signatures des 4 modèles, machine consciente), pour ne pas promettre au lecteur qu'il les a toutes déjà vues.

## 9. [dangling-reference] · severity=low · scope=fr-only
- **Where:** Chapitre 12 (l. 1108)
- **Anchor:** « je vais parcourir la hiérarchie à cinq niveaux du chapitre 6 »
- **Issue:** Le corps du chapitre 12 attribue la hiérarchie à cinq niveaux au « chapitre 6 » (l. 1108 et l. 1158/1172 renvoient à « les cinq niveaux de la hiérarchie »), ce qui est exact (elle est bien exposée au ch. 6, l. 604-624). Mais la note de fin du chapitre 12 (l. 1916) dit que cette même hiérarchie « découle de l'architecture des quatre modèles du chapitre 2 ». Le lecteur attentif qui suit les renvois reçoit deux localisations différentes (ch. 6 dans le texte, ch. 2 dans les notes) pour le même objet.
- **Suggestion:** Harmoniser : dans la note (l. 1916), préciser « la hiérarchie à cinq niveaux (introduite au chapitre 6, dérivée de l'architecture des quatre modèles du chapitre 2) » pour que texte et notes pointent au même endroit.

## 10. [result-before-question] · severity=low · scope=structural
- **Where:** Chapitre 1 (l. 136) vs Chapitre 2 (l. 146-182)
- **Anchor:** « C'est le point de départ de la Théorie des Quatre Modèles »
- **Issue:** Le chapitre 1 (l. 136) affirme déjà la conclusion — « ce simple fait, suivi jusqu'au bout, dissout le Problème Difficile » — et nomme « la Théorie des Quatre Modèles » avant que les quatre modèles ne soient définis (ce qui n'arrive qu'au ch. 2). Le nom du dispositif et sa promesse de résolution précèdent son exposé. Ce n'est pas fatal (c'est une annonce), mais combiné au fait que le ch. 4 re-annonce encore la dissolution du Problème Difficile, le lecteur reçoit le résultat trois fois (ch. 1, ch. 4, ch. 13) avant/autour de sa démonstration.
- **Suggestion:** Au chapitre 1, retarder ou atténuer la nomination « Théorie des Quatre Modèles » (parler de « la théorie que je vais exposer ») pour que le nom et sa promesse tombent au chapitre 2 quand les quatre modèles apparaissent réellement, réduisant l'effet résultat-avant-question.

## 11. [term-re-explanation] · severity=low · scope=structural
- **Where:** Chapitre 5 (l. 480-482) — vs Chapitre 3 (l. 254-256)
- **Anchor:** « La façon dont je me représente vraiment le cortex, c'est un océan »
- **Issue:** La métaphore centrale « l'océan en forme de réseau / les planeurs » est introduite au chapitre 5 (l. 480) comme si le mot « planeur » était neuf (« Ces formes sont les planeurs »), alors que le Jeu de la Vie et ses planeurs ont déjà été présentés quelques lignes plus haut dans le même chapitre (l. 466). Ce n'est pas un doublon franc, mais la formule « Ces formes sont les planeurs. » se lit comme une première définition alors que le terme vient d'être posé — le lecteur linéaire ressent une redéfinition rapprochée.
- **Suggestion:** Alléger la seconde occurrence : au lieu de « Ces formes sont les planeurs. » (posé comme une découverte), écrire « Ce sont les mêmes planeurs que ceux du Jeu de la Vie » pour signaler explicitement le rappel plutôt qu'une nouvelle définition.

## 12. [term-re-explanation] · severity=low · scope=structural
- **Where:** Chapitre 8 (l. 674-688) vs Chapitre 6 (l. 674 est ch.6) — anosognosie
- **Anchor:** « l'ESM travaillant sur des signaux intéroceptifs absents »
- **Issue:** L'anosognosie est traitée à fond au chapitre 6 (section « Anosognosie : l'inverse », l. 674-688, avec le mécanisme prédictif-rétroactif et l'exemple des applaudissements). Le chapitre 8 la réintroduit dans le couple blindsight/Anton et via Cotard (l. 672, 814) sans toujours signaler qu'elle a déjà été disséquée. Au ch. 8 le lecteur retrouve « anosognosie de la cécité corticale » (l. 788) comme si le concept d'anosognosie était neuf, alors que le mécanisme complet a été donné deux chapitres plus tôt. La Prédiction 4 (annexe H, l. 2387-2393) le ré-explique une troisième fois de zéro.
- **Suggestion:** Au chapitre 8, ajouter un rappel explicite (« l'anosognosie, dont nous avons vu le mécanisme au chapitre 6 ») pour marquer que c'est un retour et non une première introduction, et éviter de re-dérouler le blocage de perméabilité comme si le lecteur le découvrait.

## 13. [term-re-explanation] · severity=low · scope=structural
- **Where:** Chapitre 3 (l. 306-324) vs Chapitre 9 (l. 880-886)
- **Anchor:** « C'est l'hologramme en patchwork du chapitre 3, à présent coupé en son milieu »
- **Issue:** La propriété holographique / « hologramme en patchwork » est établie en détail au chapitre 3 (Lashley, rats, l. 306-324). Le chapitre 9 (l. 880-886) la re-présente sous un titre de section « La propriété holographique » et re-explique le principe de fond (« Dans les réseaux neuronaux, l'information est distribuée... vous obtenez deux copies dégradées mais complètes ») presque comme une première exposition, avant de citer le rappel « C'est l'hologramme en patchwork du chapitre 3 ». L'ordre interne fait que la ré-explication complète précède la mention du rappel — le lecteur relit la démonstration avant qu'on lui dise que c'est un rappel.
- **Suggestion:** Au chapitre 9, inverser : ouvrir par « C'est l'hologramme en patchwork du chapitre 3 » puis n'en donner que l'application nouvelle (le cerveau coupé en deux), sans re-dérouler la démonstration holographique de base.

## 14. [term-re-explanation] · severity=low · scope=structural
- **Where:** Annexe C (l. 2097-2245) vs Chapitre 5 (l. 464-478)
- **Anchor:** « Cette annexe développe le cadre computationnel brièvement évoqué au chapitre 5 »
- **Issue:** L'annexe C se présente honnêtement comme un développement du ch. 5 et invite à la sauter (l. 2099). Mais plusieurs blocs y sont re-narrés à l'identique du corps du livre plutôt que renvoyés : le Jeu de la Vie / automate cortical (déjà ch. 5), l'usage des quatre classes par le cerveau (l. 2234-2245, quasi-doublon du ch. 5 l. 474), et l'auto-inclusion de Classe 4 (l. 2245, doublon du ch. 17 l. 1762). Pour le lecteur qui lit tout linéairement (annexes comprises), c'est une troisième exposition du même matériel.
- **Suggestion:** Dans l'annexe C, remplacer les passages qui répètent le corps (usage des classes par le cerveau, auto-inclusion Classe 4) par des renvois courts au ch. 5 et au ch. 17, et ne garder en propre que ce qui est réellement nouveau (la 5e classe, l'argument de Kolmogorov, la frontière d'exprimabilité).

---
**10 of 14 are `structural`** → candidates to fix in the EN/DE source + re-propagate, not FR-only.