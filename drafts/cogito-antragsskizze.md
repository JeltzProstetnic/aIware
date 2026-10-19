# Antragsskizze: Sekundäranalyse COGITO-Daten

**Projekttitel**: Asymmetrische Varianzsignaturen kognitiver Tagesleistungen als Identifikationsmerkmal rekursiver Regulationsschleifen — eine Sekundäranalyse der COGITO-Daten

**Antragsteller**: Matthias Gruber, M.Sc. (unabhängiger Forscher; Affiliation in Verhandlung)
**Korrespondenz**: matthias@matthiasgruber.com
**Vermittler**: Prof. em. Werner W. Wittmann (Universität Mannheim)
**Vorgeschlagene Ko-Autoren** (vorbehaltlich deren Zustimmung): Prof. Dr. Florian Schmiedek (DIPF Frankfurt), Prof. Dr. Manuel Völkle (Universität Freiburg)

---

## 1. Hintergrund und theoretischer Rahmen

Das **Recursive Intelligence Model (RIM)** (Gruber, 2026, Zenodo DOI 10.5281/zenodo.20125096) ist abgeleitet aus der **Four-Model-Theory of consciousness (FMT)** (Gruber, 2015/2026, Zenodo DOI 10.5281/zenodo.20415804). Es beschreibt Intelligenz als rekursive Interaktion zwischen einem impliziten Weltmodell (IWM), einem expliziten Weltmodell (EWM) und einem expliziten Selbstmodell (ESM), wobei eine *Evaluationsfunktion* im ESM die Verteilung kognitiver Ressourcen reguliert.

Aus dieser Architektur folgt eine spezifische Vorhersage zur Dynamik kognitiver Variabilität, die mit den vorhandenen mittelwertbezogenen Kopplungsmodellen (Brose, Schmiedek, Lövdén, & Lindenberger, 2012; Brose, Lövdén, & Schmiedek, 2014) nicht generiert werden kann:

> **Eine Zunahme intraindividueller Varianz** in kognitiver Tagesleistung kann sowohl durch Intelligenz- als auch durch Motivationsdynamik getragen sein (neuartige Strategie-Exploration, Nutzung neuer Lerngelegenheiten).
> **Eine Abnahme intraindividueller Varianz** ist nach RIM überwiegend motivationsdominiert (stabile Evaluationsfunktion, konsistente Ressourcenallokation).

Die Richtung der Varianzänderung ist somit ein Identifikationssignal für die jeweils aktive Regulationsschleife. Diese Asymmetrie-als-Identifikator-Aussage stellt den eigentlichen empirischen Beitrag dar.

## 2. Stand der Literatur und Forschungslücke

Eine systematische Sichtung des COGITO-Korpus (≥ 70 Publikationen seit 2010) sowie der adjazenten Literatur zur intraindividuellen Variabilität ergibt folgendes Bild:

- **Schmiedek, Lövdén, & Lindenberger (2013, *Psych. Science*)** zeigten, dass ältere Erwachsene auf trainierten Aufgaben *niedrigere* Tag-zu-Tag-Variabilität aufweisen als jüngere — eine Niveau-Vergleichsaussage, keine richtungsbezogene Aussage zur Varianzänderung im individuellen Trajektorienverlauf.
- **Brose et al. (2012, 2014, *Emotion*)** koppelten tägliche Affekt- und Motivationsbewertungen an Mittelwerte der Arbeitsgedächtnisleistung. Eine Modellierung der *Varianzdirektion* als Funktion von Motivation findet sich nicht.
- **Hamaker et al. (2018, *MBR*)** dokumentierten via DSEM, dass negative Tagesereignisse die Residualvarianz negativer Affekte *erhöhen* — eine richtungsbezogene Varianzaussage, aber bezogen auf Affekt, nicht auf Kognition, und als Perturbations-Reaktion, nicht als Regulator-Identifikation.
- **von Oertzen, Schmiedek, & Voelkle (2020, *J. Intelligence*)** entwickelten die Ergodic Subspace Analysis (ESA), die Varianz in geteilte (ergodische) und regimespezifische Anteile zerlegt — eine symmetrische Zerlegung.
- **Schmiedek et al. (2020, *PeerJ*)** zeigten, dass innerpersonale Faktorstrukturen sich von zwischenpersonalen unterscheiden — eine statische Strukturaussage.
- **Driver, Oud, & Voelkle (2017)** publizierten das ctsem-R-Paket; **Driver & Voelkle (2018, *Psych. Methods*)** dessen hierarchisch-bayesianische Variante. Eine erstautorenschaftliche ctsem-Anwendung auf COGITO-Daten durch Voelkle oder Driver ist nicht publiziert.

**Lücke**: Keine bisherige Analyse innerhalb des COGITO-Korpus testet Varianzzunahme vs. Varianzabnahme über das 100-Tage-Fenster als Träger *unterschiedlicher* psychologischer Signale. Die methodischen Werkzeuge (DSEM, ctsem, ESA, regCtsem) sind etabliert; die spezifische Asymmetrie-als-Identifikator-Hypothese ist nicht operationalisiert.

## 3. Forschungsfrage und Hypothesen

**Hauptfrage**: Trägt die Richtung intraindividueller Varianzänderung kognitiver Tagesleistung über das 100-Tage-Messfenster ein dissoziierbares Identifikationssignal für die zugrundeliegende Regulationsschleife (Intelligenz × Motivation vs. Motivation allein)?

**H1 (Expansion)**: In Phasen wachsender Varianz (Expansion) ist die tägliche Leistung gemeinsam moduliert durch Intelligenzindikatoren *und* Motivationsindikatoren; die Interaktion ist signifikant ungleich Null.

**H2 (Kompression)**: In Phasen schrumpfender Varianz (Kompression) dominieren Motivationsindikatoren; die Modulation durch Intelligenzindikatoren ist statistisch flach.

**H3 (Asymmetrie als Identifikator)**: Die Interaktion *Varianzrichtung × (Intelligenz, Motivation)* auf die Tagesleistung ist signifikant ungleich Null; das Modell mit asymmetrischer Spezifikation passt besser als das symmetrische Vergleichsmodell.

## 4. Geplante Daten aus COGITO

| Variable | Skala | Begründung |
|---|---|---|
| Daily working memory composite | Spatial n-back, numerical n-back, memory updating | Schmiedek 2013 etablierte Kern |
| Daily perceptual speed composite | Number comparison, choice RT | Sensitivität für Motivationsfluktuation (Brose 2012) |
| Daily episodic memory composite | Word pair, location memory, object-location | Konsistenz mit Schmiedek 2010 |
| Daily affect / negative affect | PANAS-X kurz | Brose 2012 Standard |
| Daily motivation / attention rating | Selbstauskunft | Brose 2012 Standard |
| Pre/post g-factor proxy | Reasoning + Knowledge | Brunswik-symmetrische Niveaubestimmung |

Falls verfügbar zusätzlich Schlaf, Stresseinschätzung, Tagesereignisse — als Kontrollvariablen.

## 5. Methodisches Vorgehen

**Schritt 1**: Schätzung individueller Varianztrajektorien über das 100-Tage-Fenster mittels gleitender Fensteranalyse oder Multilevel-VAR mit zeitvariablen Residualvarianzen (Hamaker et al., 2018; Schmiedek 2009). Identifikation von Expansions- und Kompressionsperioden.

**Schritt 2**: Spezifikation eines hierarchisch-bayesianischen continuous-time SEM (ctsem; Driver & Voelkle 2018) mit zwei latenten Konstrukten (Kognition, Motivation) und richtungsabhängiger Drift-Spezifikation. Vergleich der Drift-Matrix zwischen Expansions- und Kompressionsphasen pro Person.

**Schritt 3**: Test der Interaktion *Varianzrichtung × (Intelligenz-Proxy, Motivations-Proxy)* mittels mehrebenenanalytischer Moderation, vergleichbar mit Adolf, Voelkle, Brose, & Schmiedek (2017).

**Schritt 4**: Sensitivitätsanalysen — alternative Operationalisierung der Varianzrichtung, Vergleich mit symmetrischen Modellen, Test der Robustheit gegen Altersgruppe (jung vs. alt — Schmiedek 2013 als Plausibilitätscheck).

**Software-Stack**: R (lavaan, OpenMx, ctsem, regCtsem, dynr) — die etablierte Pipeline der Berliner Methodik-Tradition. Eine prototypische Python-Implementierung der Datenboxzerlegung existiert (vgl. Korrespondenz Wittmann–Gruber, Mai 2026), dient aber ausschließlich als private Plausibilitätsprüfung. Die Hauptpipeline läuft in R, ko-entwickelbar mit Schmiedek (R-Konversion der SAS-Programme bereits abgeschlossen, Mai 2026) und Völkle (ctsem-Autor).

## 6. Erwarteter wissenschaftlicher Beitrag

1. **Empirischer Test einer aus der FMT-Architektur abgeleiteten Vorhersage** zur Asymmetrie kognitiver Varianzdynamik — eine Vorhersage, die etablierte Mittelwertkopplungsmodelle (Brose 2012) nicht generieren.
2. **Methodische Erweiterung** der ctsem-Anwendung auf COGITO-skalierte Daten durch richtungsabhängige Drift-Spezifikation.
3. **Brücke zwischen FMT/RIM und der Berliner Methodik-Tradition** (Wittmann → Schmiedek/Völkle → Lindenberger-Gruppe).
4. **Replizierbare Analyse-Pipeline** in R, archiviert als OSF-Projekt mit Code und (im Rahmen der Nutzungsbedingungen) Outputs.

## 7. Geplante Publikation

Primäres Ziel: *Psychology and Aging* (APA), als substantive Erweiterung der Brose 2012 / Schmiedek 2013 Linie. Alternative Ziele: *Multivariate Behavioral Research* (falls der Asymmetrie-Schätzer selbst als methodische Pointe gerahmt wird) oder *Intelligence* (falls die Brunswik-symmetrische Intelligenz-Motivations-Rahmung dominiert).

## 8. Anforderungen an den Datentransfer

Daten der jüngeren (N=101, 20-31) und älteren (N=103, 65-80) COGITO-Kohorte, beschränkt auf die unter (4) aufgeführten Variablen, in deidentifizierter Form gemäß COGITO-Datentransferprotokoll. Anwendungszeitraum: 18 Monate ab Datenfreigabe. Veröffentlichungen mit COGITO als Datenquelle gemäß COGITO-Publikationsrichtlinien; geplante Ko-Autorenschaft Schmiedek und Völkle.

## 9. Zeitplan

| Phase | Dauer | Output |
|-------|-------|--------|
| Datenfreigabe + Setup | M1–M2 | R-Pipeline auf simulierten COGITO-Daten validiert |
| Hauptanalyse | M3–M9 | Drift-Schätzungen, Asymmetrie-Tests |
| Robustheit + Sensitivität | M10–M12 | Alternative Operationalisierungen |
| Manuskript + Submission | M13–M15 | Einreichung *Psychology and Aging* |

## 10. Referenzen

Brose, A., Lövdén, M., & Schmiedek, F. (2014). *Emotion*, 14(1), 1–6.
Brose, A., Schmiedek, F., Lövdén, M., & Lindenberger, U. (2012). *Emotion*, 12(3), 605–617.
Driver, C. C., & Voelkle, M. C. (2018). *Psychological Methods*, 23(4), 774–799.
Driver, C. C., Oud, J. H. L., & Voelkle, M. C. (2017). *Journal of Statistical Software*, 77(5).
Gruber, M. (2026). *Recursive Intelligence Model* (v2 preprint, Zenodo). https://doi.org/10.5281/zenodo.20125096
Gruber, M. (2026). *The Four-Model Theory of Consciousness*. Zenodo, DOI: 10.5281/zenodo.20415804.
Hamaker, E. L., Asparouhov, T., Brose, A., Schmiedek, F., & Muthén, B. (2018). *Multivariate Behavioral Research*, 53(6), 820–841.
Lövdén, M., Bäckman, L., Lindenberger, U., Schaefer, S., & Schmiedek, F. (2010). *Psychological Bulletin*, 136(4), 659–676.
Schmiedek, F., Lövdén, M., & Lindenberger, U. (2010). *Frontiers in Aging Neuroscience*, 2:27.
Schmiedek, F., Lövdén, M., & Lindenberger, U. (2013). *Psychological Science*, 24(9), 1747–1754.
Schmiedek, F., Lövdén, M., von Oertzen, T., & Lindenberger, U. (2020). *PeerJ*, 8, e9290.
von Oertzen, T., Schmiedek, F., & Voelkle, M. C. (2020). *Journal of Intelligence*, 8(1), 3.
Wittmann, W. W. (2002). Brunswik-Symmetrie und die fünf Datenboxen.

---

**Status**: Antragsskizze v1, 2026-06-04. Zur Weiterleitung an Florian Schmiedek und Manuel Völkle über Werner W. Wittmann; bei deren Zustimmung Formalisierung und Einreichung beim COGITO Steering Committee (Maike Kleemeyer, MPIB).
