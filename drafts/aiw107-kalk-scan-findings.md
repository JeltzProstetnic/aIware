# AIW-107 — Kalk-Scan findings (native-German de-Anglizismus sweep, ed.2 new/ported DE prose)

Session 248, 2026-07-07. Method: 5 parallel **Opus** native-German editors (Fable on cost-hold) over ALL new/ported DE prose — the integrated new prose (`pop-sci/book-manuscript-de.md`, diff `69e5b69b..HEAD`) + the still-banked wave-1 prose (`drafts/book-ed2-de-new-prose.md`). Each returned surgical findings only (no rewriting). Overall verdict from all five: the prose is **already strongly native**; real calques are few and concentrated. The exact tells MG named were confirmed present (the „der Teil, der…"/„hier ist der Teil" family at 3 spots; `Rahmenwerk`=framework flagged twice independently).

## A. APPLIED — 38 objective-correctness fixes (named tells + grammar/collocation errors + false friends + clear Anglizismen)
Applied via verified script (`tmp/aiw107-kalk/apply_kalk.py`, each fix matched exactly once). All meaning-preserving. MG may veto any in the .docx redline.

**Named tells (the „der Teil, der…" family + cadence):**
- „Und jetzt der Teil, der wahnsinnig klingt und … ist:" → „Und jetzt kommt, was wahnsinnig klingt und … ist:"
- „Und hier ist der Teil, den ich damals verschwieg." → „Und jetzt kommt der Teil, den ich damals verschwieg."
- (banked §7) „Das ist das Stück, das das Ganze zum Laufen bringt …" → „Genau das bringt das Ganze zum Laufen …"

**Grammar / collocation calques:**
- „zwischen dem Berichten der Welt …" → „… Wiedergeben der Welt …" (berichten takes no accusative)
- „vorab getroffenen Vermutungen" → „vorgefertigten Vermutungen" (Vermutungen ≠ „treffen")
- „während die Belege still auf seiner Seite eintrafen" → „… ihm still recht gaben" (calque of "came in on its side")
- „Ich bin an keine Universität angebunden." → „Ich gehöre keiner Universität an."
- „und setzt einen Test darauf" → „und knüpft einen Test daran"
- „mit dem dieses Kapitel öffnet" → „… beginnt" (intransitive „öffnen" = "opens")
- „den dominanten Sinnesreiz über die Durchgänge …" → „… von Durchgang zu Durchgang …" ("across the runs")
- „läuft normalerweise auf dem stetigen Zufluss …" → „speist sich normalerweise aus dem stetigen Zufluss …" ("runs on")
- „Und dann war da das eine Mal, als ich" → „… war da noch das eine Mal, als ich"
- „wie mein Körper eine Sache tat, während das Fraktal eine andere tat" → „… das eine tat, … das andere tat"
- „die Füße ans Feuer halten wollen" → „auf den Zahn fühlen wollen" (English idiom has no German equivalent)
- „Testbar mit … plus fMRI." → „Mit … und fMRI testbar." (Anglizismus „plus" + word order)
- „gehen *immer* subkritisch" → „werden *immer* subkritisch" ("go subcritical")
- „Beginn mit etwas, das du …" → „Beginnen wir mit etwas, das du …" (calqued imperative)
- „von innerhalb einer Schleife" → „aus dem Inneren einer Schleife" ("from within")
- „eine nähere Frage" → „eine näherliegende Frage" ("nearer" = more detailed, not more immediate)
- „Womit eine Frage stehen bleibt." → „Womit eine Frage im Raum stehen bleibt."
- „Halte das Buch auf Armlänge von dir weg." → „… mit ausgestrecktem Arm von dir weg." (doubled distance)
- „Er kündigt sich nie an. Hat er nie." → „… Hat er noch nie." (stranded auxiliary echo of "Never has.")

**False friends / Anglizismen:**
- „ein fairer Instinkt" → „ein berechtigter Instinkt" (fair = just/sportsmanlike)
- „treibt progressiv ins Subkritische" → „treibt zunehmend …" (progressiv = political/medical)
- „ein katastrophaler Gedanke" → „ein katastrophisierender Gedanke" (CBT term)
- „multiple virtuelle Konfigurationen" → „mehrere …"
- „dopaminerge Belohnungspfade" → „… Belohnungsbahnen"
- „To-do-Liste" → „Aufgabenliste"
- „Mainstream-Neurowissenschaft" → „gängige Neurowissenschaft"
- „Psychedelische Visuals enthüllen …" → „Psychedelische Seherscheinungen enthüllen …" (heading; body already native)
- „ein Rahmenwerk, das nicht nur erklärte" → „ein Gerüst …"  ·  „Kein anderes Rahmenwerk verbindet" → „Kein anderer Ansatz verbindet" (framework-calque, flagged twice independently)
- „dicht an technischem Apparat" → „dicht gepackt mit technischem Apparat" ("dense with")

**De-scaffolding / clarity (light):**
- „ist hier an der Stelle, an der er das Buch vielleicht weglegt" → „wird hier vielleicht das Buch weglegen"
- „so wie sich vor einer Seite jener Punkt aufgelöst hat" → „… eine Seite zuvor …" (spatial→temporal)
- „Keine andere Bewusstseinstheorie macht diese Vorhersage." → „… trifft diese Vorhersage." (scientific register)
- (en-dash→em-dash consistency) „nicht bloß – sie sagt" → „nicht bloß — sie sagt" (lone stray en-dash among em-dashes; the book-wide —→– sweep is the separate deferred AIW-93 step)

## B. HELD for MG — judgment/voice calls (NOT applied)
These are genuine style/voice/meaning decisions, not corrections. MG decides (in the .docx or here):
1. „die ungeschickt genug ist, **dich zu ertappen**" → proposed „**sich zu verraten**". Logic question: does the blind spot catch *you*, or does *you* catch the *brain* („dein Gehirn auf frischer Tat" two lines on)? May read backwards. **Check against EN source.**
2. „**Denk das zu Ende.**" — optional signpost cut. („zu Ende denken" is native; only objection is the pointer imperative.)
3. „um Mitleid zu **ernten**" → „erregen/heischen" (borderline; „ernten" fits Applaus/Spott).
4. „im Anhang **hinten im Buch**" → „im Anhang" (redundancy trim vs. helpful pointer for a pop-sci reader).
5. „Die **härtere** Frage ist" → „schwierigere" (low-confidence).
6. „Der Placebo-Effekt **sitzt auf** derselben Doppelbewertung" → „beruht auf" (possibly intentional physical metaphor, paralleling „saß an diesem oberen Ende").
7. „**verfolgt** ihn **zurück auf** die Überzeugung" → „führt ihn zurück auf" (active-tracing verb may be intended for the CBT detective-work image).
8. „Ich **baue** das Argument hier nicht **aus**" → „führe … aus" (possible deliberate echo of the „bauen"/AC-building motif two sentences up).
9. „**Was mich störte, war …**" repeated back-to-back (Coda fractal) → restructure second with „Sondern" (optional anti-anaphora).
10. „Was da subtrahiert wird, ist ein **Input**." → „… ein **Eingang**." (through-line with „Simulation mit einem Eingang" 4 sentences on; „Input" is defensible naturalized German).
11. „**Hier steht** die vollständige Falsifikationsbatterie" (Anhang H intro) → „Es folgt …" (low priority).
12. „dass tatsächlich jemand **zu Hause** ist" → „jemand **da** ist" (but „jemand zu Hause" is native idiom for presence/sentience; may deliberately echo the EN recurring image — **keep unless EN dropped it**).
13. (banked §3) „unter einer einzigen sichtbaren **Disziplin** gebaut" → „…Vorgabe" (possible intended pun: Disziplin = field + self-discipline).

## C. REJECTED — deliberate motif, kept as-is
- „**umbringen**" for killing a theory („Eine Theorie, die man umbringen kann, ist überhaupt erst eine." / „das sie umbringen würde") — one scan flagged it as a calque, but it is a **deliberate recurring motif**. Left untouched (2 occurrences intact).

## D. CULTURAL-GRANDEUR FLAGS — MG's call (NOT applied)
DACH readers are allergic to US-style self-celebration (see the old S176 tone note). BUT the ed.2 restructure (MG-approved) deliberately reinstated the first-person bridge cold-open, and **EN ed.2 already shipped with this grandeur**. So the default is "DE mirrors EN." Flagged for MG to decide whether DE should be more reserved for the DACH audience:
1. Bridge epiphany-in-tears: „Tränen liefen mir übers Gesicht, während ich haltlos lachte und mir der schwerste Stein meines Lebens vom Herzen fiel." (conversion-drama register)
2. „meine Aufgabenliste für den Rest meines Lebens erledigt" — life's work finished at 25.
3. Triple superlative in one breath: „löst das vielleicht schwierigste offene Problem der Wissenschaft auf, macht Vorhersagen, mit denen keine konkurrierende Theorie mithalten kann, und liefert einen konkreten Bauplan für eine wirklich bewusste Maschine".
4. „Diese Theorie existiert nur, weil mir nie jemand gesagt hat, welche Disziplinen einander nicht berühren durften." (lone-outsider-genius; low risk — counterweighted by „kein Doktortitel" humility).
5. „Die Theorie erklärt DID nicht bloß — sie sagt genau diese Art von Architektur vorher" ("doesn't merely explain—predicts" boast cadence).
6. „die empirisch am besten abgesicherte Psychotherapie, die es gibt" ("…there is" intensifier).
7. „und er beschert einem zwei von allem" (showy reveal beat).
8. Ch16 confession tricolon: „Ich sah das Bewusstsein, ich sah das Universum, und ich sah, dass es dasselbe Muster war." + „beide Hälften fielen in derselben Sekunde an ihren Platz, dort auf der Brücke in Innsbruck, mit fünfundzwanzig." (genius-origin-myth; partly self-deflated by the „Spinner"-Schublade line that follows).
9. Anhang H uniqueness/superlative cluster: „Keine andere Bewusstseinstheorie trifft diese Vorhersage." + „Kein anderer Ansatz verbindet …" + „ist das die ultimative Bestätigung."
10. (banked §5) „dass ich mein Leben dieser einen Intuition widmen würde" + „war das Wichtigste, was ich bis dahin je gelernt hatte" (devote-my-life + superlative childhood epiphany).
11. (banked §10, Anhang G) „Eine Theorie, die ihre Schwachpunkte verbirgt, ist keine Theorie." (TED-style aphorism; content is humble — low concern).

## Note — data-integrity conflict surfaced
Memory `feedback_german_book_tone.md` (S176, 100d old: third-person author, "no tears on a bridge", "theory over person") is **superseded** by MG's S245 ed.2 restructure directive (first-person bridge cold-open, EN already committed). It reflects 1st-edition front matter. Not silently applied; the section D flags are exactly where the two doctrines collide — MG resolves.

## E. RESERVED-TONE PASS — APPLIED (MG decision: "Trim DE for DACH")
MG chose to dial the section-D grandeur DOWN for the German edition (DE diverges from EN, which keeps its grandeur). An Opus writer recast the flagged passages; **13 recasts applied** (verified script `tmp/aiw107-kalk/apply_reserved.py`, each matched once). Keep/strip line: author self-mythology → stripped; theory substance → kept, de-superlatived. All claims/terms preserved. MG can dial any back up in the .docx redline.
- **D1 bridge-in-tears** → „…mit genau fünfundzwanzig. Ich blieb stehen, weil der Boden für einen Moment nicht mehr dort war, wo er eben noch gewesen war." (melodrama out; keeps bridge/25/felt-click; ties to the „Schwindel" motif)
- **D2 life's-work-at-25** → „Woran ich von da an arbeiten würde, stand damit fest."
- **D3 triple-superlative** → drops „vielleicht schwierigste offene Problem der Wissenschaft" + „keine konkurrierende Theorie mithalten kann"; keeps all three claims + the nachahmt/hat thesis contrast.
- **D5 „nicht bloß — sagt vorher"** → „erklärt DID nicht nur, sie sagt diese Art von Architektur voraus…" (boast cadence flattened)
- **D6 „…, die es gibt"** → dropped.
- **D7 „beschert einem zwei von allem"** → „der aus allem zwei macht" (borderline; original was defensible theory-drama, trimmed per MG's directive).
- **D8 confession „ich sah … ich sah … ich sah"** → „— Bewusstsein und Universum, dasselbe Muster." (veni-vidi-vici origin-myth cut; „Spinner"-Schublade self-deflation kept)
- **D9 uniqueness cluster** (4 spots): „Keine andere…" ×2 + „Kein anderer Ansatz…" + „ultimative Bestätigung" → stated once plainly / superlative dropped.
- **D10 (banked §5)** „das Wichtigste, was ich je gelernt" + „mein Leben … widmen" → understated.
- **KEPT as-is:** D4 (lone-outsider, low risk, counterweighted) · D11 („Theorie, die ihre Schwachpunkte verbirgt…" — humble content).
