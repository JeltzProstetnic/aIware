<!-- STATUS (Session 224, 2026-06-12): REFRAMED for the standard-method correction.
     Created as a STANDALONE Gmail draft via MCP (no threading params). DO NOT SEND until either
     Lehmann replies to the design question OR the ~2026-06-16 timeout (governing decision, decisions.md).
     Before sending: attach the FINAL corrected PDF `drafts/aiw47-eneuro/aiw47-eneuro-opinion-DRAFT.pdf`.
     Send from the matthias@matthiasgruber.com alias. Recipients know German; formal Sie. MG reviews/edits/sends. -->
# AIW-47 outreach email — transparent co-author opener, standard-method correction (Opus writer, Session 224)

**To:** mirko_lehmann@uni-bonn.de, ulrich.ettinger@uni-bonn.de, wittmann@xi.psychologie.uni-mannheim.de
**From:** matthias@matthiasgruber.com
**Subject:** Manuskript-Entwurf zu Ihrer Ketamin-Studie — mit einer methodischen Korrektur meiner Reanalyse

Lieber Herr Lehmann, lieber Herr Ettinger, lieber Herr Wittmann,

eine kurze Ergänzung zu meiner letzten Nachricht, bewusst noch vor Ihrer Antwort: Der angehängte Entwurf nimmt Gestalt an — eine anonymisierte, doppelblinde Fassung, ausdrücklich ein Arbeitsstand und eine Diskussionsgrundlage, kein fertiges Stück. Ich schicke ihn jetzt, damit Sie sehen können, woran Ihre Rückmeldung eigentlich ansetzt.

Zunächst aber eine Korrektur, die ich Ihnen schuldig bin. In meiner letzten Nachricht hatte ich die meta-d′-Reduktion als statistisch signifikant berichtet (p≈0,018). Bei der Vorbereitung des Manuskripts bin ich auf das feldübliche, response-konditionale Verfahren umgestiegen — also Maniscalco–Lau / Fleming HMeta-d, exakt Ihre Methode — und habe dabei festgestellt, dass mein früherer Wert aus einer nicht-standardmäßigen, gemeinsamen Typ-2-Likelihood stammte, die meta-d′ überschätzt hat. Korrekt nachgerechnet bleibt zwischen den Gruppen ein richtungskonsistenter, aber nicht signifikanter Trend: meta-d′ Ketamin 0,42 vs. Placebo 0,70 (Hedges g ≈ −0,55; Welch p ≈ 0,085, n.s.). Eine unabhängige hierarchisch-bayesianische HMeta-d-Schätzung (PyMC) bestätigt das Bild — Gruppen-M-Ratio Ketamin ≈ 0,47 vs. Placebo ≈ 0,66 —, doch das 95%-Kredibilitätsintervall der Differenz schließt die Null ein.

Ich möchte das nicht beschönigen, aber auch nicht überdramatisieren: Ihr publiziertes Ergebnis steht, und es ist das besser abgesicherte. Dass meine Reanalyse nur einen Trend erreicht, ist methodisch begründet und kein Mangel auf Ihrer Seite — ich habe einen anderen (Maximum-Likelihood-)Schätzer verwendet und hatte vor allem Ihre subjektweise Staircase-Variabilität nicht als Kovariate (die ANCOVA-Adjustierung Ihrer Analyse). Auf der Effizienz-Ebene (M-Ratio) stimmt mein Befund mit Ihrem sogar überein — beide „marginal / Intervall schließt Null ein". Dass ich diesen Fehler vor jeder Einreichung selbst bemerkt und behoben habe, liegt gerade daran, dass ich meine Reanalyse an Ihrem Standard gemessen habe; Ihre kovariaten-adjustierte hierarchische Analyse ist der rigorose, gut abgesicherte Bezugspunkt.

Damit kein Missverständnis entsteht, was der Entwurf nun beansprucht: Meine unabhängige Reanalyse (zwei Schätzer) reproduziert die Richtung Ihres Effekts, ist zwischen den Gruppen aber zu schwach besetzt, um Signifikanz zu erreichen — also „vorläufige, richtungskonsistente" Evidenz, ausdrücklich keine Reproduktion Ihrer Signifikanz. Die eigentliche architektonische Vorhersage der Theorie — dass Weltmodell-Treue (≈ d′) und Selbstmodell-Treue (≈ meta-d′) orthogonal dissoziierbar sind — ist damit noch gar nicht geprüft: Die Staircase Ihres Designs klammert d′, sodass dieser Datensatz die beiden Achsen nicht trennen kann. Der entscheidende Test bräuchte ein Within-Subject-Design mit freiem d′.

Was ich von Ihnen erbitte, ist genau Ihr seniores, kritisches Urteil — auch und gerade in der harten Form: Wie weit tragen die Daten, wo überdehnt der Entwurf? Ihr Separabilitätsbefund steht dabei unabhängig von jeder darüberliegenden Deutung; eine Beteiligung in welcher Form auch immer — eine kritische Lektüre, ein Rat, bis hin zur Mitautorschaft am empirischen Teil — setzt keinerlei Zustimmung zur theoretischen Rahmung voraus. Die theoretische Einbettung (knapp: zwei Arten von Modellen entlang Welt/Selbst × implizit/explizit) ist absichtlich leicht gehalten, und es steht Ihnen frei, sie vollständig zu verwerfen. Als naheliegender gemeinsamer nächster Schritt böte sich ohnehin die im Entwurf benannte entscheidende Studie an — ein Within-Subject-Design mit freiem d′, das Ihr Paradigma, meine validierte Pipeline und die theoriegeleitete Hypothese zusammenführt; ganz ohne Druck, nur als das, was sich empirisch eigentlich aufdrängt.

Zur Transparenz, weil es die Einordnung erleichtert: Ich bin unabhängiger Forscher, ohne institutionelle Anbindung und akademisch junior. Die fehlende Affiliation hat mir wiederholt Desk-Rejections eingetragen; das Doppelblind-Format ist auch ein Weg, das zu umgehen. Ich suche entsprechend keinen Segen, sondern Ihre fachliche Prüfung des tragenden Teils. Eine letzte Klärung zum Design: Ich habe aus Ihren OSF-Materialien (gucm2) entnommen, dass es sich um ein Between-Subjects-Design mit Parallelgruppen handelt, es also keinen Paarungsschlüssel gibt — korrigieren Sie mich bitte, falls ich das falsch gelesen habe.

Mit besten Grüßen
Matthias Gruber
ORCID 0009-0005-9697-1665
