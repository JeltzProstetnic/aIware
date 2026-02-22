## Anhang C: Fünf Klassen der Berechnung

*Dieser Anhang vertieft das in Kapitel 5 angerissene Berechnungs-Framework — die fünf Klassen dynamischen Verhaltens, die darüber entscheiden, ob ein physisches System Bewusstsein tragen kann. Wer mit der intuitiven Version aus Kapitel 5 zufrieden ist, kann diesen Anhang bedenkenlos überspringen; für das Hauptargument wird hier nichts Neues gebraucht. Wer aber das vollständige Bild will: Hier trifft Mathematik auf Physik.*

### Wolframs vier Klassen

2002 veröffentlichte Stephen Wolfram *A New Kind of Science* — das Ergebnis jahrzehntelanger Forschung an der Frage, was passiert, wenn man absurd einfache Regeln auf absurd einfache Systeme loslässt. Sein zentrales Werkzeug war der zelluläre Automat: eine Reihe (oder ein Gitter) von Zellen, jede entweder an oder aus, die synchron nach einer festen Regel aktualisiert werden — einer Regel, die nur die unmittelbaren Nachbarn jeder Zelle berücksichtigt.

Die Überraschung: Aus diesen trivial einfachen Regeln entstand eine enorme Vielfalt an Verhalten. Wolfram ordnete es in vier Klassen:

| Wolfram-Klasse | Verhalten | Beispiel | Was man sieht |
|:---:|---|---|---|
| 1 | Uniform | Regel 0 | Alles wird leer. Jede Zelle stirbt. |
| 2 | Periodisch | Regel 4 | Stabile, sich wiederholende Muster. Blinker. Uhren. |
| 3 | Zufällig/chaotisch | Regel 30 | Scheinbare Zufälligkeit. Keine erkennbare Wiederholungsstruktur. |
| 4 | Komplex | Regel 110 | Lokalisierte Strukturen, die sich bewegen, wechselwirken und überdauern. |

Diese Klassifikation war tatsächlich nützlich. Sie erfasste etwas Reales über das Verhalten dynamischer Systeme und galt weit über zelluläre Automaten hinaus — für Strömungsdynamik, biologische Systeme, ökonomische Modelle, neuronale Netze. Die vier Klassen waren nicht bloß Schubladen, sondern Attraktoren. Systeme aus völlig unterschiedlichen Domänen fielen immer wieder in dieselben vier Verhaltensregime.

Aber es gab ein Problem.

### Das Fraktal-Problem

Wolframs Klasse 3 war ein Sammeltopf. Sie enthielt zwei grundlegend verschiedene Systemtypen, die auf den ersten Blick *ähnlich aussahen*:

**Fraktale Systeme** wie Regel 90, die ein perfektes Sierpinski-Dreieck erzeugt — ein unendlich selbstähnliches, rekursiv strukturiertes Muster. Mathematisch elegant, vollständig deterministisch und rechnerisch langweilig: Den Zustand jeder Zelle zu jedem Zeitschritt kann man berechnen, ohne die gesamte Simulation durchlaufen zu müssen. In der Fachsprache: *rechnerisch reduzibel*.

**Pseudochaotische Systeme** wie Regel 30, deren Ausgabespalte Wolfram selbst als Pseudozufallsgenerator in *Mathematica* verwendete. Sie produzieren Output, der *zufällig aussieht*, aber vollständig deterministisch ist — gleicher Input, gleicher Output, jedes Mal. Hier lässt sich die Berechnung nicht abkürzen; jeder Schritt muss tatsächlich durchlaufen werden. Fachbegriff: *rechnerisch irreduzibel*.

Wolfram packte beide in Klasse 3. Seine Definition betonte das *Erscheinungsbild* von Zufälligkeit („erscheint in vielerlei Hinsicht zufällig"), während er bemerkte, dass „Dreiecke und andere kleinskalige Strukturen im Wesentlichen immer auf irgendeiner Ebene zu sehen" seien. Er räumte ein, dass die Klassifikation Schwächen hatte: „Bei praktisch jedem allgemeinen Klassifikationsschema gibt es unvermeidlich Fälle, die je nach Definition der einen oder der anderen Klasse zugeordnet werden."

Eric Rowland argumentierte auf der NKS-Konferenz 2006 unabhängig davon, dass verschachtelte (fraktale) Muster eine eigene Klassifikation verdienen.

Das Problem geht aber tiefer als Klassifikationsästhetik. Fraktale und chaotische Systeme unterscheiden sich strukturell — und zwar auf eine Weise, die für das Kernargument dieses Buches entscheidend ist: Welche Systeme können Bewusstsein tragen?

### Das Fünf-Klassen-Schema

Das Fünf-Klassen-Schema ordnet die Verhaltenstypen als sauberen monotonen Gradienten vom geordnetsten zum ungeordnetsten:

**Klasse 1 — Statisch.** Systeme, die in einen Fixpunkt konvergieren und dort verharren. Ein Pendel, das einmal schwingt und zur Ruhe kommt. Tot. Es wird nichts berechnet. Periode: 1.

**Klasse 2 — Periodisch.** Systeme, die sich in wiederkehrende Schleifen einpendeln. Eine Uhr. Ein Herzschlag (näherungsweise). Information wird im Muster gespeichert, aber nie transformiert. Periode: endlich.

**Klasse 3 — Fraktal.** Systeme, die selbstähnliche Struktur auf jeder Skala erzeugen. Ein Sierpinski-Dreieck. Ein Farn. Die Mandelbrot-Menge. Mathematisch reichhaltig, ästhetisch atemberaubend — und *rechnerisch reduzibel*: Man kann vorausspringen, ohne jeden Schritt durchrechnen zu müssen. Struktur ohne Rechenaufwand. Periode: quasi-unendlich, mit exakter oder statistischer Selbstähnlichkeit auf jeder Skala.

**Klasse 4 — Komplex (Rand des Chaos).** Systeme, die persistente lokalisierte Strukturen erzeugen, die sich bewegen, wechselwirken und beliebige Berechnungen kodieren können. Conways Spiel des Lebens. Der kortikale Automat. Rechnerisch *irreduzibel* — keine Abkürzungen möglich. Diese Systeme sind zur universellen Berechnung fähig: Bei geeigneten Anfangsbedingungen können sie jeden Algorithmus simulieren, einschließlich Simulationen ihrer selbst. Periode: quasi-unendlich, mit Selbstähnlichkeit *plus* persistenten wechselwirkenden Strukturen. Hier lebt Bewusstsein.

**Klasse 5 — Zufällig.** Systeme, deren Output tatsächlich zufällig ist — nicht pseudozufällig, nicht deterministisch, nicht komprimierbar. Kein Muster, keine Selbstähnlichkeit, keine Periode, die sich irgendwann wiederholt. Tatsächlich unendlicher Informationsgehalt. Struktur: *unbekannt* (siehe unten).

Die Abbildung auf Wolframs Schema:

| Fünf-Klassen | Wolfram | Was sich änderte |
|:---:|:---:|---|
| 1 | Klasse 1 | Gleich |
| 2 | Klasse 2 | Gleich |
| 3 | Klasse 3 (Teil) | Abgespalten aus Wolframs Klasse 3 |
| 4 | Klasse 4 | Gleich |
| 5 | Klasse 3 (Teil) | Abgespalten aus Wolframs Klasse 3 |

Wolframs Anordnung auf dem Unordnungsspektrum lief: 1 → 2 → 4 → 3. Unhandlich. Das Fünf-Klassen-Schema ergibt einen sauberen monotonen Gradienten: 1 → 2 → 3 → 4 → 5, geordnet nach zunehmender Unordnung und zunehmender rechnerischer Irreduzibilität.

### Warum deterministische Automaten keine Zufälligkeit produzieren können
