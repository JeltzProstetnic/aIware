# AIW-92 — Platzierungsvorschlag: didaktische Muster im DEUTSCHEN Buch
**Ziel:** „Die Simulation namens Ich" (`pop-sci/book-manuscript-de.md`)
**Quelle:** `docs/aiw92-criticality-dials-conversation-verbatim.md` (9 Muster)
**Stand:** S232, 2026-06-19 — unabhängig vom EN-Agenten, kapitel-parallel gehalten.

> **Lesart:** Zeilenanker beziehen sich auf den Stand des kanonischen `.md` zum Zeitpunkt dieser
> Analyse. Alle Einfüge-Anweisungen nennen zusätzlich den *Satz davor* wörtlich, damit sie auch
> bei Drift treffen. Der Hauptbeitrag dieses Threads ist nicht neuer Stoff, sondern die
> **Verknüpfung** des Vorhandenen unter EINEM Mechanismus (zwei Regler) — deshalb sind die meisten
> Entscheidungen „ERWEITERN" statt „NEU".

---

## Gesamt-Strategie (eine Minute)

Das Buch hat die Bauteile schon: Kortikaler Automat (Kap 5), Wolfram-Klassen (Kap 5), Anfall (Kap 5),
Salvia-Zeitdehnung (Kap 6), Nahtod-Lebensfilm (Kap 13), die Jetzt-Konstruktion (Kap 13), Libet (Kap 13).
Was fehlt, ist die **Geometrie**, die sie zusammenhält: zwei orthogonale Regler an EINEM Rand des Chaos,
und die obere rechte Ecke (beide maximal), in der Nahtod und Salvia derselbe Ort sind. Die zwei Regler
sind die zentrale neue Klammer; sie gehören nach Kap 5 (Heimat der Kritikalität). Von dort wird in Kap 6
(Salvia) und Kap 13 (Nahtod) jeweils mit einem Satz auf die Ecke zurückverwiesen, statt den Mechanismus
neu zu erklären. Muster 8 (zwei kausale Rollen) ist die einzige große NEU-Passage und gehört zwingend
in Kap 13 NACH Libet/Jetzt-Fenster.

---

## Muster 1 — Der netzförmige Ozean (CA-auf-Hirn)

**ENTSCHEIDUNG:** ÜBERSPRINGEN (bereits abgedeckt) — eine kleine Bild-Verstärkung optional in Muster 2.

**WO:** Kapitel 5, Abschnitt „Der kortikale Automat" (497–503).

**WARUM:** Das Buch realisiert die CA-auf-Hirn-Identität bereits buchstäblich (Z. 499: „Jedes Neuron ist
eine Zelle in einem Zellulären Automaten – nicht metaphorisch, sondern buchstäblich") und liefert mit dem
Oktopus-mit-grenzenlosen-Armen (Z. 503) sogar schon ein bildhaftes Anker-Objekt. MGs Ozean-Bild ist hier
*Vehikel* für Muster 2, kein eigenständiger neuer Inhalt — es einzeln einzuschieben hieße Doppelung. Das
Ozean-Bild wird stattdessen in Muster 2 eingeführt, wo es seine didaktische Arbeit leistet (die zwei Regler
brauchen eine Oberfläche, auf der man drehen kann).

**ENTWURF:** (kein eigener Block — Ozean-Bild wird in Muster 2 eingeführt)

---

## Muster 2 — Die zwei Regler der Kritikalität

**ENTSCHEIDUNG:** NEU (die zentrale Klammer des ganzen Threads).

**WO:** Kapitel 5, eigener neuer Unterabschnitt **direkt nach** dem Abschnitt „Der kortikale Automat",
also **eingefügt vor** der Überschrift „### Die Konvergenz" (Z. 525). Konkret: einfügen **nach** dem
Absatz, der mit „… Deshalb erholen wir uns von diesen Störungen so erstaunlich gut." endet (Z. 523),
**vor** „### Die Konvergenz".

**WARUM:** Hier ist der kortikale Automat gerade greifbar gemacht worden, die Wolfram-Klassen liegen frisch
auf dem Tisch (Z. 481–489) — der ideale Moment, um zu zeigen, dass „Kritikalität" zwei verschiedene Dinge
meint. Parallel zum EN-Buch (Ch 5 „At the Edge of Chaos"). Dieser Abschnitt trägt zugleich Muster 1 (Ozean)
und Muster 3 (Stall) und stellt die Ecke auf, auf die Kap 6/13 zurückverweisen.

**ENTWURF:**

```markdown
### Zwei Regler, eine Kante

Wenn ich über das Gehirn nachdenke, sehe ich keine Formeln. Ich sehe einen Ozean – einen netzförmigen
Ozean, wo das Wasser nicht überall hin kann, sondern nur dorthin, wo Verbindungen liegen. Die Neuronen
sind die Wasserflächen, die Synapsengewichte sind die Kanäle dazwischen, und die Feuermuster sind die
Wellen, die darüberlaufen. Werfe ich einen Stein hinein, breitet sich etwas aus. Und genau hier lohnt es
sich, langsam zu machen, denn an diesem Ozean gibt es nicht *einen* Regler, sondern *zwei* – und beide
nennen die Leute „Kritikalität", was für mehr Verwirrung gesorgt hat, als nötig wäre.

**Regler eins fragt: Wie weit wandert eine Welle?** Drehe ich ihn ganz herunter, ist der Ozean ein
gefrorener Spiegel. Der Stein fällt, macht *plopp*, und nichts geschieht – ein Kräuseln, das sofort stirbt
(Wolframs Klasse 1). Drehe ich ihn ganz auf, peitscht ein einziger Kiesel den ganzen Ozean zum Sturm; alles
schäumt, jede Welle löscht jede andere aus (Klasse 3, kochendes Chaos). Dazwischen liegt der süße Punkt: Die
Welle wandert, zeugt im Schnitt eine neue, stirbt nicht und explodiert nicht. Genau dort breiten sich
Störungen jeder Größe aus – wie bei einem Sandhaufen, der exakt im Schüttwinkel liegt, oder bei Wasser
genau am Gefrierpunkt. Regler eins entscheidet, *wie viel* vom Ozean an einem Geschehen teilnimmt.

**Regler zwei fragt: Was für Formen leben auf dem Ozean?** Das ist der Game-of-Life-Regler – der, auf dem
die ganze Theorie reitet. Beim gefrorenen Spiegel: keine Formen. Bei sanfter Dünung: dieselbe Welle, immer
und immer wieder, eine dumme Schaukel, die nichts rechnet (Klasse 2, Oszillatoren). Beim kochenden Chaos:
jeder Punkt flackert zufällig, auch das rechnet nichts. Aber an der Kante entstehen Gleiter – stehende
Muster, die wandern, zusammenstoßen, überdauern, *etwas tun*. Das ist Klasse 4, Conways Game of Life. Hier,
und nur hier, kann eine Berechnung als stabiles Muster auf dem Ozean leben. Und ein Selbstmodell ist nichts
anderes als ein solches Muster.

Die beiden Regler fallen in den Lehrbüchern meist zusammen – man dreht an einem und meint, der andere geht
mit. Im echten neuronalen Ozean tun sie das nicht. Man kann Regler eins hochdrehen und den Ozean bloß
*lauter* machen, ohne dass die Gleiter besser werden. Es sind zwei verschiedene Fragen: *wie viel* Ozean
mitmacht, und *wie reich* die Formen darauf sind. Behalte beide im Kopf – am Ende dieses Buches werden sie
erklären, warum manche Menschen in einer halben Sekunde ein ganzes Leben durchleben.
```

> **Anmerkung (Stall = Muster 3) ist im obigen Block bewusst NICHT enthalten** — siehe Muster 3 für die
> separate Mini-Einfügung, damit der Stall dort sitzt, wo er didaktisch am stärksten ist (die Kante als
> „kurz vor dem Abriss").

---

## Muster 3 — Der aerodynamische Stall = die Kante

**ENTSCHEIDUNG:** NEU (kurze Einfügung), als bildhafter Anker für „die Kante".

**WO:** Kapitel 5. **Einfügen am Ende** des neuen Muster-2-Blocks, als letzter Absatz **vor** „### Die
Konvergenz". (Sitzt direkt nach „… ein ganzes Leben durchleben.")

**WARUM:** MG kennt den Stall aus der Fliegerei; das Bild „maximaler Auftrieb genau im Moment vor dem
Abriss" ist der präziseste intuitive Anker für „warum am Rand und nicht darüber". Es schließt die Lücke
zwischen „Kante ist gut" und „über die Kante = Absturz" — und bereitet die Anfall-Passage vor.

**ENTWURF:**

```markdown
Aus der Fliegerei kenne ich dafür ein besseres Bild als jede Gleichung: den Strömungsabriss, den Stall. Ein
Flügel gibt den meisten Auftrieb nicht weit weg von der Grenze, sondern *genau* an ihr – im letzten Moment,
bevor die Luftströmung abreißt und in Turbulenz kippt. Stellt man den Flügel ein Grad zu steil, reißt die
Strömung ab, der Auftrieb bricht weg, und das Flugzeug fällt. Das Gehirn fliegt am Vor-Stall-Rand. Genau
dort, kurz vor dem Abriss, ist die Berechnung am reichsten. Einen Schritt weiter – über die Kante – und die
Gleiter lösen sich in Chaos auf, der Auftrieb des Bewusstseins bricht zusammen. Deshalb balanciert ein
waches Gehirn ständig an einer Kante, die es nie ganz überschreiten darf.
```

---

## Muster 4 — Der Anfall als Negativkontrolle

**ENTSCHEIDUNG:** ÜBERSPRINGEN als eigenständige Passage — aber **PRÄZISE KORREKTUR** der bestehenden
Stelle nötig (siehe „Konflikte & Autor-Entscheidungen"). Es wird NICHTS Neues eingefügt; eine vorhandene
Stelle wird umformuliert.

**WO:** Kapitel 5, Z. 523 (die Anfall/Schlaganfall/Ohnmacht-Aufzählung im Abschnitt „Der kortikale Automat").
Zusätzlich harmonieren mit Z. 487 („in chaotische Dynamik geschleudert").

**WARUM:** Das Buch rahmt den generalisierten Anfall derzeit als „über Klasse 4 hinaus in Klasse-5-Chaos"
(Z. 523) und als „in chaotische Dynamik geschleudert" (Z. 487). Muster 4 rahmt ihn als das Gegenteil:
*hypersynchron* (Klasse 2/3), zu geordnet, Regler 1 (Klasse-4-Ausdehnung) niedrig → bewusstlos. Klinisch
ist der generalisierte tonisch-klonische Anfall tatsächlich hypersynchron — Muster 4 ist also die korrektere
Version. Das ist ein echter Widerspruch im Buch und darf nicht stillschweigend stehenbleiben. Da hier kein
neuer Absatz entsteht, sondern eine Korrektur an kanonischem Text, schlage ich den Wortlaut nur vor — die
eigentliche Edit-Entscheidung trifft der Autor (siehe unten).

**ENTWURF (Vorschlag für die korrigierte Stelle, Z. 523 — NICHT von mir eingefügt):**

```markdown
Auch Fehlfunktionen des Automaten lassen sich beobachten. Ein epileptischer Anfall führt nicht etwa zu
*mehr* Bewusstsein, obwohl dabei riesige Teile des Gehirns gleichzeitig feuern – und genau das ist der
aufschlussreiche Punkt. Bei einem generalisierten Anfall feuern die Neuronen *im Gleichschritt*,
hypersynchron: derselbe Takt, überall, gleichzeitig. Das ist Klasse-2/3-Dynamik – maximale Mit-Aktivierung,
aber keine Gleiter, keine reichen Muster, kein Klasse-4-Regime. Mit anderen Worten: Regler eins (wie viel
Ozean schwingt mit) steht hoch, aber Regler zwei (welche Formen leben darauf) steht am Boden. Viel Gehirn
ist *aktiv*, aber fast kein Gehirn ist *bewusst* – und der Mensch verliert das Bewusstsein. Der Anfall ist
die saubere Gegenprobe zu dem, was Bewusstsein *nicht* ist: nicht bloß viele feuernde Neuronen, sondern
Neuronen, die am Rand des Chaos reiche, verschiedene Muster tragen. Ein Schlaganfall ist, was passiert, wenn
Teile des Kortex komplett ausfallen. Eine Ohnmacht ist, was passiert, wenn die Mindestfrequenz für Wachheit
nicht mehr erreicht wird. Der Automat ist fragil. Aber die Struktur, die ihn erzeugt – der Neokortex mit
seinen gelernten Gewichten und seiner evolvierten Architektur – ist robust. Deshalb erholen wir uns von
diesen Störungen so erstaunlich gut.
```

> Reihenfolge-Hinweis: Diese Korrektur sollte **nach** dem Muster-2-Block stehen, damit „Regler eins/zwei"
> bereits eingeführt sind. Da die Anfall-Stelle (Z. 523) im `.md` aber *vor* der Einfügeposition von
> Muster 2 (Z. 525) liegt, gibt es zwei saubere Optionen — siehe „Konflikte".

---

## Muster 5 — Beide Regler maximal → Zeitdehnung

**ENTSCHEIDUNG:** ÜBERSPRINGEN als neue Passage in Kap 5; **ERWEITERN-BESTEHENDES** mit je einem
Rück­verweis-Satz in Kap 6 (Salvia) und Kap 13 (Nahtod). Der neue Beitrag ist die **Vereinigung** beider
unter EINEM Mechanismus + die falsifizierbare Vorhersage.

**WO:**
- (a) **Kap 6, Z. 631** (Salvia-Zeitdehnung): erweitern, **nach** dem Satz, der mit „… dort biologisch
  statt pharmakologisch ausgelöst." endet.
- (b) **Kap 13, Z. 1332** (Nahtod-Speicherdump): erweitern, **nach** dem Satz, der mit „… hier biologisch
  verursacht." endet.

**WARUM:** Beide Stellen erklären die Zeitdehnung schon einzeln und verweisen schon aufeinander („den
Mechanismus behandelt Kapitel 13" / „Dieselbe Zeitdehnung … unter Salvia … Kapitel 6"). Was fehlt, ist der
gemeinsame Nenner: *beide* Regler stehen hier oben (viel Ozean + reiche Muster), und subjektive Dauer =
Verarbeitungsvolumen / Uhrzeit. Diesen einen Gedanken liefere ich an beiden Stellen — kurz, ohne den
Mechanismus zweimal voll auszubuchstabieren, mit Verweis auf die zwei Regler aus Kap 5.

**ENTWURF (a) — Kap 6, nach Z. 631:**

```markdown
Worauf das hinausläuft, lässt sich mit den zwei Reglern aus Kapitel 5 sagen. Normalerweise kann man nicht
beide gleichzeitig ganz aufdrehen: Reißt man das ganze Gehirn in ein einziges Geschehen (Regler eins hoch),
synchronisiert es sich und wird dumm; will man reiche, verschiedene Muster (Regler zwei hoch), braucht es
lokale Unterschiede, die das eine große Geschehen zersplittern. Das Alltagsbewusstsein lebt auf einem
Kompromiss zwischen beiden. Salvia tritt beide Regler zugleich durch – viel Ozean *und* reiche Muster –, und
die subjektive Dauer eines Erlebnisses hängt nicht an der Uhr, sondern am Verarbeitungsvolumen: wie viel die
Simulation in einer Sekunde durchschleust. Pumpt man ein Lebenswerk an Verarbeitung in fünfundvierzig
Sekunden, *durchlebt* man Jahre, statt sie zu erinnern. Dasselbe passiert beim Nahtoderlebnis (Kapitel 13) –
weshalb beide, der dokumentierte Salvia-Trip und der Lebensfilm im Angesicht des Todes, dieselbe seltene
obere rechte Ecke besetzen: hohe Ausdehnung *und* hohe Komplexität auf einmal. Das ist eine prüfbare
Vorhersage: Zustände mit extremer Zeitdehnung sollten gleichzeitig hohe Integration (viel Gehirn beteiligt)
*und* hohe Musterkomplexität zeigen – dort, wo gewöhnliche Zustände das eine gegen das andere eintauschen.
```

**ENTWURF (b) — Kap 13, nach Z. 1332:**

```markdown
In den zwei Reglern aus Kapitel 5 gesprochen, ist das die seltene obere rechte Ecke: Beide stehen ganz oben.
Viel Gehirn ist in einem einzigen Klasse-4-Geschehen versammelt (Regler eins), und dieses Geschehen trägt
zugleich außergewöhnlich reiche Muster (Regler zwei). Weil subjektive Zeit aus Verarbeitungsvolumen gebaut
wird, nicht von einer Uhr abgelesen, dehnt sich ein paar Sekunden auf das Maß eines Lebens. Genau diese Ecke
besucht auch der Salvia-Trip (Kapitel 6). Zwei Wege – einmal die sterbende, durchdrehende Biologie, einmal
die Chemie –, dieselbe Ecke. Die Theorie sagt voraus, dass beide Zustände dieselbe Doppel-Signatur tragen:
hohe Integration und hohe Komplexität gleichzeitig, dort, wo das wache Alltagsgehirn stets nur das eine auf
Kosten des anderen haben kann.
```

---

## Muster 6 — Die zwei Begrenzer der Ecke (Energiebudget + Lock-in)

**ENTSCHEIDUNG:** NEU (Lock-in ist im aktuellen DE-Buch *nicht* vorhanden; die alte Monografie-Stelle
p.281 zur inneren Dimensionalität wurde in diese Ausgabe nicht übernommen). Energiebudget ist ebenfalls neu
als expliziter Governor.

**WO:** Kapitel 13, **direkt nach** dem Muster-5(b)-Block (also nach dem Nahtod-Speicherdump, Z. 1332 +
Muster-5-Erweiterung). Das hält die ganze „obere rechte Ecke"-Argumentation an einem Ort beisammen und sitzt
im EN-Buch an der parallelen Stelle.

**WARUM:** Erklärt, *warum* die Ecke selten ist (zwei Governoren) und – entscheidend – warum sie zugleich
*Spitzenbewusstsein und minimaler Realitätskontakt* ist. Das verbindet sauber mit dem schon vorhandenen
luziden Traum (Z. 601: „Kein sensorischer Input, keine äußere Realität, die das Modell korrigiert") und mit
dem K-Hole (Z. 708–710). Der dissoziative Charakter der Both-maxed-Zustände wird so vorhersagbar statt
mysteriös.

**ENTWURF:**

```markdown
Wenn diese Ecke so spektakulär ist – ein ganzes Leben in Sekunden –, warum lebt dann niemand dort? Weil zwei
Wächter davorstehen.

Der erste ist das **Energiebudget**. Das ganze Gehirn in ein einziges Geschehen zu reißen *und* darauf
maximal reiche Muster rechnen zu lassen, kostet mehr, als der Stoffwechsel dauerhaft liefern kann. Man kann
sich die Ecke schlicht nicht leisten. Deshalb braucht es Ausnahmezustände, um hineinzukommen: das sterbende
Gehirn, dem im Sauerstoffmangel die metabolischen Bremsen versagen, oder eine Substanz wie Salvia, die die
Regulierung sabotiert. Beide schalten kurz den Wächter aus – für ein paar Sekunden Uhrzeit.

Der zweite Wächter ist subtiler, und er ist der eigentliche Grund, warum diese Zustände sich *abgehoben von
der Welt* anfühlen. Das Innere des Gehirns hat ungleich mehr Dimensionen als seine Ein- und Ausgänge. Durch
die Augen, Ohren und die Haut kommt nur ein dünnes Rinnsal Information herein – verglichen mit dem, was im
Inneren gleichzeitig läuft, ist das ein Gartenschlauch neben einem Ozean. Normalerweise reicht dieses dünne
Rinnsal gerade aus, um die riesige innere Simulation fortlaufend an der Realität zu justieren: Die
Sinnesdaten korrigieren das Modell, Bild für Bild, und halten es ehrlich. Dreht man nun beide Regler hoch,
schwillt das innere Geschehen so an, dass der dünne Sinneskanal es nicht mehr nachregeln kann. Die
Simulation läuft der Welt davon, rastet in ihrem eigenen Strudel ein und – verliert die Realität aus dem
Blick. Genau das sieht man im luziden Traum (Kapitel 6/7), wo überhaupt keine Sinnesdaten korrigieren, und
im K-Hole unter Ketamin (Kapitel 7).

Das Tückische daran: Es ist *derselbe* Regler eins, der beides tut. Viel Gehirn in ein Geschehen zu reißen
ist genau das, was den dünnen Draht zur Welt überschwemmt. Wer in die Ecke drückt, kappt damit die Leine, die
ihn am Boden halten würde. Die Ecke begrenzt sich von innen selbst. Und daraus folgt die vielleicht
verblüffendste Umkehrung des ganzen Kapitels: Die obere rechte Ecke ist **Spitzenbewusstsein und minimaler
Realitätskontakt zugleich** – maximale Verarbeitung, abgekoppelt von der Welt. Deshalb sind die Both-maxed-
Zustände – Lebensfilm, hochdosiertes Salvia, tiefe Psychedelika, lebhafte Träume – ausnahmslos
realitätsentkoppelt. Das Energiebudget regelt den *Eintritt* in die Ecke; das Realitäts-Leck ist die *Folge*
des Eintritts. Zusammen machen sie die Ecke selten *und* abgehoben – und die Theorie sagt voraus: Beides ist
derselbe Ort.
```

---

## Muster 7 — Der Dimmer auf der Realitätskopplung

**ENTSCHEIDUNG:** NEU, aber **kurz** — als Brücke, die Muster 6 (unwillkürliches Lock-in) mit Muster 8
(willkürlicher Rückzug) verbindet. Es ist die Erkenntnis „Lock-in und Vorstellung sind EINE Achse".

**WO:** Kapitel 13, **direkt nach** dem Muster-6-Block, **vor** dem Muster-8-Block. Diese Reihenfolge ist
wichtig: Erst die Achse (Muster 7), dann die zwei Enden als kausale Rollen (Muster 8). Beide stehen NACH
Libet (1278–1294) und nach dem Jetzt-Fenster (1296–1306) — siehe Placement-Constraint.

**WARUM:** Liefert das vereinheitlichende Bild — der Dimmer-Schalter —, das den Übergang vom „es passiert dir"
(Nahtod/Salvia) zum „du machst es selbst" (Tagträumen) leistet. Ohne diesen Satz wirkt Muster 8 wie ein
Themenwechsel; mit ihm ist es die natürliche Fortsetzung.

**ENTWURF:**

```markdown
Und jetzt der Dreh, der das Ganze persönlich macht. Dieses Maß an Realitätskopplung – wie fest die Simulation
an die Außenwelt gekettet ist – ist kein Schicksal. Es ist ein Dimmer. An dem einen Ende, unwillkürlich und
extrem, sitzen Nahtod und Salvia: Da wird einem die Leine zur Welt überschwemmt, ohne dass man etwas dazu
tut. Am anderen Ende, willkürlich und sanft geregelt, sitzt etwas, das jeder kennt: das Tagträumen, die
Vorstellung, das Abdriften in eine selbstgemachte Szene. Lock-in und Phantasie sind nicht zwei verschiedene
Dinge – sie sind dieselbe Achse, einmal von außen aufgezwungen, einmal von dir selbst gedreht. Und das führt
zu der vielleicht meistübersehenen Tatsache über den eigenen Willen.
```

---

## Muster 8 — Die zwei kausalen Rollen (KRITISCH)

**ENTSCHEIDUNG:** NEU (die einzige große neue Passage). Reframt Epiphänomenalismus.

**WO:** Kapitel 13, **nach** dem Muster-7-Block. Das setzt es zwingend **NACH** dem Libet-Material
(1278–1294) und **nach** der Jetzt-Fenster-Stelle (1296–1306, endet mit „… und selbst dieses Fenster
erreicht dich mit Verzögerung."). Damit ist die harte Placement-Vorgabe erfüllt: Der „du kannst den Raum in
dieser Sekunde nicht ändern"-Satz landet erst, wenn der Leser frisch weiß, dass er zu 99 % ein verzögerter
Beobachter ist. Im EN-Buch sitzt die Passage an der parallelen Stelle (nach Libet, im „what it means"-Kapitel).

**WARUM:** MGs Kernbeitrag: Bewusstsein hat zwei kausale Griffe, nicht einen. Der nach außen (langsam,
indirekt, über Monate/Jahre — die Rolle, die der Epiphänomenalismus für nichtig erklärt) und der nach innen
(unmittelbar, total — der willentliche Rückzug in selbstgemachte Welten). Die kausale Macht ist am
unsichtbarsten, wo man sie sucht (einen Arm bewegen), und am sichtbarsten, wo man sie übersieht (das eigene
Erleben jetzt ändern). Das frischt die Libet-Pointe auf und dreht sie um.

**ENTWURF:**

```markdown
### Zwei Griffe, nicht einer

Halte einen Moment fest, was die letzten Seiten ergeben haben: Du sitzt eine halbe Sekunde hinter der
Wirklichkeit, in einem Fenster, das deine Schleife dir baut und „Jetzt" nennt. Der Schlag, die Entscheidung,
das Wort – alles ist gefallen, ehe du es erlebst. Das ist der Befund, der so viele zu dem Schluss treibt,
Bewusstsein sei ein Beifahrer ohne Lenkrad, ein Epiphänomen, das mitfährt und nichts bewegt. Ich halte das
für die falsche Pointe – und der Grund liegt darin, dass Bewusstsein zwei kausale Griffe hat, nicht einen,
und wir den falschen anstarren.

Der erste Griff geht **nach außen**: das virtuelle Selbst formt das Substrat, das Substrat formt das
Verhalten, das Verhalten formt die Welt. Aber er ist langsam und indirekt. Man bewegt nicht in dieser Sekunde
einen Arm durch reinen Willen – das hat das Substrat längst entschieden, bevor man davon weiß. Was man
bewirkt, bewirkt man über Monate und Jahre: durch Reflexion, durch Bewertung, durch das langsame Einlagern
bewusster Erfahrung in implizite Struktur, die dann *künftige* Entscheidungen anders ausfallen lässt. Hier ist
die kausale Macht real, aber so verzögert und verteilt, dass man sie kaum bei der Tat ertappt. Genau deshalb
sieht sie wie nichts aus.

Der zweite Griff geht **nach innen**, und er ist das genaue Gegenteil: unmittelbar, total, in dieser Sekunde
verfügbar. Das virtuelle Selbst kann sein eigenes Substrat *übersättigen* und sich in selbstgemachte Welten
zurückziehen – die Aufmerksamkeit umlenken, sich etwas vorstellen, phantasieren, abdriften, und zwar *jetzt*.
Das ist derselbe Dimmer wie eben, nur diesmal von dir gedreht. Du kannst den Raum, in dem du sitzt, in dieser
Sekunde nicht ändern. Aber du kannst ändern, *was du in dieser Sekunde erlebst*. Das ist die unmittelbarste
kausale Macht, die ein bewusstes System überhaupt besitzt – und fast niemand zählt sie als Macht, weil sie
sich nicht in der Außenwelt zeigt.

Damit kippt die ganze Epiphänomenalismus-Anklage. Sie sucht die kausale Wirkung dort, wo Bewusstsein am
schwächsten ist – im Hebel auf die äußere Welt in Echtzeit –, und übersieht sie dort, wo Bewusstsein am
stärksten ist: in der willentlichen Kontrolle über den eigenen Zustand, über die eigene Realitätskopplung.
Die kausale Macht ist am unsichtbarsten, wo wir sie suchen, und am sichtbarsten, wo wir sie übergehen. Ein
bewusstes Wesen kann die Welt reiten – oder seine eigene Simulation. Diese Wahl, Sekunde für Sekunde, ist
kein Beifahrer. Sie ist das Lenkrad, das wir die ganze Zeit übersehen haben.
```

---

## Muster 9 — Präsenz vs. Zugriff

**ENTSCHEIDUNG:** ÜBERSPRINGEN als große neue Passage; **ERWEITERN-BESTEHENDES** mit einem kurzen
Zwischensatz auf der „erweitert"-Leiter in Kapitel 2.

**WO:** Kapitel 2, Abschnitt zur Bewusstseins-Leiter (242–248). Einfügen **nach** dem Absatz „einfaches
Bewusstsein" (endet mit „… aber fast kein ‚für wen es ist wie'.", Z. 242), **vor** „Eine Stufe höher:
**einfach erweitertes Bewusstsein**" (Z. 244).

**WARUM:** Die Präsenz-vs-Zugriff-Unterscheidung ist im Kern eine Verfeinerung der Leiter, die schon da ist:
Auf der untersten Stufe ist der Selbst-Inhalt *präsent* (das System trägt das selbstverursachte Stück Welt
in sich), aber nicht *zugänglich* (es kann ihn nicht greifen und damit spielen). Zugriff entsteht erst, wenn
die expliziten Modelle reich genug für Selbst-Interaktion sind – das ist exakt die Rekursionstiefe, die die
höheren Leiterstufen definiert. Eine eigene Passage wäre Doppelung; ein Zwischensatz, der die Leiter mit
„Präsenz/Zugriff" beschriftet, ist der ganze Beitrag. (Anbindung an Muster 8: Der innere Griff – willentliche
Phantasie – ist genau das, was mit dem Zugriff anspringt, also keine Fähigkeit des Minimal-Selbst.)

**ENTWURF (Zwischenabsatz, nach Z. 242):**

```markdown
Es lohnt sich, hier eine feine Unterscheidung einzuziehen, die später wichtig wird. Auf der untersten Stufe
ist der Selbst-Inhalt durchaus schon *da* – das System trägt das Stück Welt, das es selbst verursacht, in
seiner Repräsentation mit. Aber es kann ihn nicht *greifen*. Der Inhalt ist **präsent**, doch nicht
**zugänglich**: Niemand zu Hause kann ihn herausziehen, betrachten, mit ihm spielen. Genau das ändert sich,
je weiter man die Leiter hinaufsteigt. Höhere Stufen heißen nicht „mehr Inhalt", sondern „Zugriff auf den
Inhalt" – und Zugriff entsteht, wenn die expliziten Modelle reich genug werden, um *mit sich selbst zu
wechselwirken*: Das Selbstmodell handelt am Selbstmodell, das Metamodell bildet das Selbstmodell ab. Diese
Selbst-Interaktion ist der Mechanismus, der aus bloßer Anwesenheit Zugriff macht. Jede weitere Stufe ist eine
weitere Windung dieser Schleife.
```

---

## Konflikte & Autor-Entscheidungen

### K1 — Anfall: Klasse-5-Chaos (Buch) vs. hypersynchron Klasse-2/3 (Muster 4)
Das Buch sagt an **zwei** Stellen, der generalisierte Anfall kippe ins Chaos:
- Z. 487: „… im generalisierten Anfall wird in chaotische Dynamik geschleudert: die Simulation kann nicht
  zusammenhalten."
- Z. 523: „… oder über Klasse 4 hinaus in Klasse-5-Chaos geraten."

Muster 4 (und die klinische Realität) sagt das Gegenteil: Der generalisierte tonisch-klonische Anfall ist
**hypersynchron** – zu *geordnet*, Klasse 2/3, nicht Chaos. **Das ist ein echter Widerspruch und muss
aufgelöst werden, nicht stillschweigend verdoppelt.** Mein Vorschlag (siehe Muster 4) korrigiert Z. 523 auf
die hypersynchrone Lesart und macht den Anfall zur sauberen Negativkontrolle für Regler eins. Wenn Z. 523 so
geändert wird, **muss Z. 487 mitgezogen werden** (sonst widersprechen sich zwei Stellen im selben Kapitel):
- Vorschlag Z. 487: statt „in chaotische Dynamik geschleudert" → „… im generalisierten Anfall in
  hypersynchrone Dynamik gerissen: alle Neuronen feuern im Gleichschritt, zu starr, als dass die Simulation
  zusammenhalten könnte."

**AUTOR-ENTSCHEIDUNG nötig:** (a) Korrektur übernehmen (klinisch korrekt, dient Muster 4 als Negativkontrolle —
empfohlen), ODER (b) die Chaos-Rahmung bewusst behalten (didaktisch einfacher: „zu wenig/zu viel" als
symmetrisches Bild) und Muster 4 dann ganz weglassen, weil es sonst dem Buch widerspricht. Ich kann nicht
beides haben. **Empfehlung: (a).** Klinisch sind generalisierte Anfälle hypersynchron; die Negativkontrolle
ist außerdem das didaktisch stärkere Argument („viel Gehirn aktiv ≠ viel Gehirn bewusst").
Hinweis: Auch die Bewusstseins-Karte in Kap 7 (Z. 720–728) listet den Anfall nicht — dort ist also kein
Folge-Edit nötig.

### K2 — Lock-in / innere Dimensionalität: alte Monografie vs. aktuelles Buch
Das Verbatim zitiert Buch-Monografie p.281 („die innere Dimensionalität des Gehirns ist um ein vielfaches
höher als die Dimensionalität seiner Eingänge"). **Diese Stelle existiert im aktuellen DE-Manuskript NICHT** —
sie wurde in diese Pop-Sci-Ausgabe nicht übernommen. Muster 6 führt das Konzept also erstmals ein (ich habe
es in MGs Bildsprache neu formuliert: „Gartenschlauch neben einem Ozean"). **AUTOR-PRÜFUNG:** sicherstellen,
dass das mit den holographischen Kompressions-Kapiteln 14/15 (Z. 1775: „persönliche Singularität",
implizit=komprimiert / explizit=dekomprimiert) nicht kollidiert. Sie kollidieren nicht — sie verstärken
einander (dünner I/O-Kanal = niedrige Bandbreite der dekomprimierten Projektion). Optionaler Vorverweis in
Muster 6 auf Kap 14/15 möglich, aber nicht nötig.

### K3 — Reihenfolge Anfall (Z. 523) vs. Zwei-Regler-Block (Z. 525)
Die Anfall-Korrektur benutzt „Regler eins/zwei", die erst im Muster-2-Block (eingefügt bei Z. 525) erklärt
werden — aber Z. 523 steht *davor*. Zwei saubere Optionen:
- **Option A (empfohlen):** Den Zwei-Regler-Block (Muster 2 + 3) **vor** die Anfall-Stelle ziehen, d. h. den
  Abschnitt „### Zwei Regler, eine Kante" nicht ans Ende von „Der kortikale Automat", sondern **unmittelbar
  nach** der Wolfram-Klassen-Einführung (nach Z. 489, vor „### Der kortikale Automat" bei Z. 495) setzen.
  Dann sind die Regler eingeführt, bevor Automat *und* Anfall kommen. Sauberste Lesereihenfolge.
- **Option B:** Block bleibt bei Z. 525; in der Anfall-Korrektur „Regler eins/zwei" durch beschreibende
  Wendungen ersetzen („wie viel Gehirn mitschwingt / welche Muster es trägt") und den Begriff erst später
  einführen. Funktioniert, ist aber didaktisch schwächer.

**AUTOR-ENTSCHEIDUNG:** A oder B. Ich empfehle **A** (Regler zuerst, dann alle Anwendungen).

---

## Reihenfolge / Querverweise (Einbau-Plan)

**Kapitel 2** (Leiter): Muster 9 als Zwischenabsatz nach Z. 242.

**Kapitel 5** (Kritikalitäts-Heimat), empfohlene Reihenfolge (Option A aus K3):
1. Wolfram-Klassen (vorhanden, Z. 481–489)
2. → **NEU: „Zwei Regler, eine Kante"** (Muster 2) + Stall-Absatz (Muster 3)
3. „Der kortikale Automat" (vorhanden, Z. 495 ff.)
4. Anfall-Stelle **korrigiert** (Muster 4 / K1, Z. 523) — nutzt jetzt die Regler
5. „Die Konvergenz" (vorhanden)

**Kapitel 6** (Salvia): Muster-5(a)-Erweiterung nach Z. 631 (verweist zurück auf Kap 5, vorwärts auf Kap 13).

**Kapitel 13** (Bedeutung), strikte Reihenfolge wegen Libet-Constraint:
1. Libet (vorhanden, 1278–1294)
2. Jetzt-Fenster / verschmiertes Fenster (vorhanden, 1296–1306)
3. Kampfkünstler (vorhanden, 1308) — bleibt, wo es ist
4. Nahtod-Speicherdump (vorhanden, 1332) + **Muster-5(b)-Erweiterung** (obere rechte Ecke)
5. → **NEU: Muster 6** (zwei Begrenzer der Ecke)
6. → **NEU: Muster 7** (Dimmer — kurze Brücke)
7. → **NEU: Muster 8 „Zwei Griffe, nicht einer"** (zwei kausale Rollen — MUSS nach Libet/Jetzt-Fenster)

> Hinweis zur Platzierung von 5–7 in Kap 13: Der Nahtod-Speicherdump (1332) steckt mitten im freien-Willen-
> /Stimmen-Dissoziations-Block (1326–1336). Sauberer wäre, die Ecke-Argumentation (Muster 5b/6/7/8) als
> eigenen Unterabschnitt **nach** Z. 1336 zu setzen (nach „… wird sichtbar.") und an Z. 1332 nur einen
> Vorverweis-Halbsatz zu lassen („— mehr zu dieser ‚oberen rechten Ecke' gleich"). Das hält den NDE-Absatz
> intakt und gibt der neuen Klammer Raum. **AUTOR-ENTSCHEIDUNG:** Muster-5b direkt an 1332 anhängen ODER als
> eigenen Block nach 1336 bündeln (Letzteres empfohlen, da Muster 6/7/8 ohnehin einen eigenen Block bilden).

**Parallelität EN↔DE:** Alle Einfügepunkte liegen an den kapitel-parallelen Stellen (Kap 2 Leiter, Kap 5
Edge-of-Chaos, Kap 6 Salvia, Kap 13 „what it means" nach Libet). EN- und DE-Buch bleiben ausgerichtet, sofern
der EN-Agent dieselbe Kapitel-Reihenfolge wählt.

**„Vier Modell-Arten", nicht „vier Module":** In allen Entwürfen eingehalten — kein Entwurf spricht von
„Modulen"; wo nötig wird auf „Selbstmodell als Muster auf dem Ozean" verwiesen, nicht auf diskrete Kästchen.
