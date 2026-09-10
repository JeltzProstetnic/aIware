<!-- Action: reference -->
<!-- Tracked-by: AIW-93 -->
# AIW-93 — DE manuscript tell-inventory (Phase 1, read-only)

Session 238 (2026-07-04). 12 parallel Opus native-ear reviewers over `pop-sci/book-manuscript-de.md`.
This is the diagnostic that drives Phase 2 (Opus rewrite). **~386 tells total.** Confirms MG's "AI slop" flag.

## Totals by chunk
| Chunk | Range | Issues | Escalate |
|-------|-------|--------|----------|
| Vorwort/Autor/Kap1 | 44–139 | 15 | 1 |
| Kap2 | 140–278 | 22 | 1 |
| Kap3+4 | 279–470 | 36 | 1 |
| Kap5 (AIW-92) | 471–572 | 30 | 0 |
| Kap6 (AIW-92) | 573–683 | 33 | 2 |
| Kap7+8 | 684–845 | 38 | 0 |
| Kap9+10 | 846–1008 | 34 | 1 |
| Kap11 | 1009–1129 | 34 | 1 |
| Kap12/Pattern8 (AIW-92) | 1130–1285 | 33 | 1 |
| Kap13 (AIW-92) | 1286–1459 | **52** | 0 |
| Kap14+15 | 1460–1768 | 30 | 2 |
| Kap16+Coda | 1769–1964 | 29 | 3 |
| **TOTAL** | | **~386** | **~13** |

Appendices (A–E) NOT yet inventoried — deferred to Wave 2 if MG wants them.

## Cross-cutting recurring patterns (fix in bulk)
- **Anglizismus-Kalk:** „goes nowhere"→„kommt nirgendwohin"; „the part that…"→„der Teil, der…" (MG-flagged; recurs ~10×); „best guess"→„beste Vermutung"; „lights go out" (plural); „over time"→„über die Zeit"; „a matter of X"; „no way to"→„keinen Weg"; „does its job / does the pushing" do-support.
- **False friends (MEANING errors, priority):** `demütigend` (humbling→humiliating) L1292/L1708 → „ernüchternd/demütig"; `Ignoranz` (ignorance→wilful disregard) L1907 → „Unwissenheit"; `basisch` (basic→alkaline!) L992 → „basal"; `Instanz` (instance→authority) L1670/L1760 → „Fall"; `Dekade` L1424 → „Jahrzehnt"; `Bequemlichkeit` (convenience→laziness) L1618; `teilweise`→`zeitweise` L1354; `massiv` (massive→big) L848/925/976; `komputational` (non-word) L1376/1447; `neural`→`neuronal` (throughout Kap11).
- **AI symmetry:** „not-X-it's-Y" via em-dash (should be „…, sondern…"); negation-tricolons „Nicht A. Nicht B. C."; over-tidy „X hat A. Y hat B." metronome; „Dieselbe… Dieselbe…" anaphora.
- **Address-form drift:** stray `du`-imperatives („Nenn ihn", „Behalte", „Berühre") where the book uses `man`; `Sie`/`ihr` whiplash at the close.
- **Typography:** English em-dash `—` (no spaces) vs German ` – `; ALL-CAPS emphasis (German uses italics); Oxford comma before „und".
- **Untranslated artifact:** „Both-Regler" L659 (English „Both" welded into a German compound).

## AUTHOR-DECISION items (do NOT auto-fix — MG arbitrates)
1. **FACTUAL CONTRADICTION (content, not voice):** L1150 „verliert täglich eine Million Neuronen" vs L1242 „Etwa 85.000 Neuronen pro Tag". Same book, incompatible. 85k/day (~1/sec) is the correct/common figure. → unify.
2. **Uncle Bruno tense:** L64 „…war eine große Inspiration" — Bruno J. Gruber is ALIVE (fleet rule: never past-tense implying death). → „ist". (Treat as rule-fix, not open question.)
3. **Coda emotional register** (L1931 vindication arc „nobody read it → science caught up → proved me right"; L1939 NDE life-review testimony; L1961 „Seid nett zueinander" sign-off): how much to mute vs keep as dry personality.
4. **Closing address form** (Kap13 peroration L1378–1451 + Kap16 close shift to `du`/`ihr`): deliberate earned direct-address, or force `man`? (Accidental `du`-drift in mechanism passages e.g. L1324–1326 gets fixed to `man` regardless.)
5. **DID „Alters"** (English plural, L1113+): germanize („Alter-Persönlichkeiten") or keep clinical English term?
6. **Boundary term unify:** `informationsundurchsichtig` (L1735/1743) vs `informationsundurchlässig` (Kap14). Recommend „undurchlässig".

## DO NOT CHANGE (guard against overcorrection)
- **„vier Modelle" / „Vier-Modelle-…" is the book's INTENTIONAL lay shorthand** (Kap2 title „Die vier Modelle"; Anhang E „Warum vier Modelle"). Only „Module" would be wrong. A Kap14/15 agent proposed „Vier-Modellarten-Architektur" — REJECT that change.
- **Locked verbatim (never touch):** „…wer weiß, ob du zurückkommst, und wie viele" (Kap12); „Gedankenpaläste" (Kap12).
- Personal anecdotes that are dry personality (childhood dream, K.o., café) — keep; strip only ego/grandeur, not personality.

---

# RAW FINDINGS BY CHUNK

## Vorwort / Der Autor / Kapitel 1 (L44–139) — 15 issues, 1 escalate
L46 „Keine einzelne Disziplin besitzt die Frage." — calque („owns the question") → „…ist für sie zuständig."
L52 „was, wenn man darüber nachdenkt, genau das ist, was…" — LLM filler („when you think about it") → drop.
L54 „sind zwei Dinge wahr. Erstens … Zweitens" — calque („two things are true") → „gilt zweierlei."
L56 „wird sich … der langen Liste … anschließen" — calque → „reiht sich … in die lange Reihe … ein."
L60–62 „Der Autor": clean (3rd person, CV-factual — target voice).
L64 „Bruno J. Gruber … war eine große Inspiration" — ESCALATE (tense; Bruno ALIVE → „ist").
L73 „die halten die meisten Menschen nachts nicht wach" — idiom calque → „verliert kaum jemand nachts den Schlaf."
L73 „Physiker haben… Biologen haben… Chemiker haben…" — rigid tricolon → vary framing.
L75 „Das Ergebnis? … Tausende… Dutzende… Hunderte…" — English beat + quantity-tricolon → „Das Ergebnis:" + dissolve.
L87 „es ist die Art von schwierig, mit der…" — calque + missing article → „eine Schwierigkeit, mit der die Neurowissenschaft…"
L93 „wie einem Bankomatkartenchip" — Kasus → „wie ein Bankomatkartenchip" (keep Austrianism „Bankomatkarte").
L107 „was wird… Was aus… Was aus…" — translated anaphora-tricolon → fold to one.
L125 „Newton brauchte… Darwin brauchte… Einstein brauchte…" — over-tidy tricolon → vary verbs.
L129 „so selten, dass es nur einmal passieren konnte" — English word order → „kein so seltenes … Phänomen, dass…"
L131 „Menschen sind nicht magisch." — calque („aren't magic") → „Am Menschen ist nichts Übernatürliches."
L137 „durch Jahrhunderte … hindurchschneiden … tatsächlich funktioniert" — calque + „actually" → rework.
Note: ego well-controlled here; „Der Autor" stays CV-dry, no hero framing.

## Kapitel 2 (L140–278) — 22 issues, 1 escalate
L142 „auf einen Apfel schauen" — calque + wir/man wobble → „betrachten".
L144 „Scheint unkompliziert – man sieht einen Apfel." — verbless English-telegraph → add verb.
L146 „um Größenordnungen komplizierter" — calque („orders of magnitude") → „ungleich komplizierter".
L148 „feuert die neuronale Aktivität, die „Apfel" entspricht" — only neurons fire + dative → „feuern die Neuronen, die dem „Apfel" entsprechen".
L150 „Man spürt nicht Photonen, … nicht Signale, … nicht Merkmalsdetektoren" — „not X, not Y" + wrong negation → „keine Photonen … keine Signale…"
L152 „unkontroverse Neurowissenschaft / stimmt zu, dass / beste Vermutung" — 3 calques.
L162 „Es baut nicht ein Modell; es baut viele" — doesn't-X-it-Y → „nicht ein Modell, sondern viele."
L164 „auf Splitter zusammengestaucht" — calque („to slivers") → „auf ein Minimum".
L172 „Jetzt die Schlüsseleinsicht." — verbless throat-clearing → „Nun zur Schlüsseleinsicht."
L210 „die Crew hinter der Bühne" — Anglizismus „Crew" → „Bühnenmannschaft".
L214 „Man IST die Figur…" — US ALL-CAPS + verbatim repeat → italic „ist".
L224 „Die reale Seite ist Licht aus." / L228 „…ist Licht an." — ungrammatical predicate → „ist das Licht aus/brennt das Licht."
L224 „nicht mehr „erlebt" als Wasser…" — „no more X than" calque → „so wenig … wie".
L226 „Das ist es wert, betont zu werden / schaut er auf / die Hälfte des Bildes" — 3 calques.
L238 „Bewusstsein kommt in Graden." — calque → „gibt es in Abstufungen."
L242 „ein „wie es ist wie" … „für wen es ist wie"" — ESCALATE (Nagel term — confirm German rendering).
L250 „bei jeder Dinnerparty" — US calque → „auf jeder Party / bei jedem Abendessen".
L258 „drei Schichten decken es ab" — calque → „genügen dafür".
L270 „Nun schaue man auf andere Tiere." — recurring „auf…schauen" → „betrachte man".
Note: no ego; first-person moments (L154, L232) modest — leave.

## Kapitel 3+4 (L279–470) — 36 issues, 1 escalate
L283 doubled „…, genau genommen —" parallel → rework.
L285 „Das Spiel hat… Die CPU hat… Das Spiel hat… Die GPU hat…" — metronome antithesis → fold.
L299 „real für die Figur" + tricolon → „Für die Figur sind…real".
L305 „kein Ding – es ist ein Prozess" — not-X-but-Y via dash → „…, sondern ein Prozess."
L309 „Und das tun sie." — bare calque → „Und genau das tun sie."
L321 „wirft eine … Frage auf zu Therapien" — split verb + „raises a question about" → reorder; „jemanden zu finden, der eine hat" → „Therapeutenwechsel".
L323 „reihen sich … über … hinweg auf" — „line up across" → „häufen sich … quer durch".
L327 „in derselben Geschwindigkeit" → „mit derselben Geschwindigkeit / im selben Tempo".
L329 „Diese Hand ist meine." — calque → „Das ist meine Hand."
L337 „Entfernte er ein wenig… Entfernte er viel…" — metronome → „Je mehr … desto…"; „berühmterweise" → „vielzitiert".
L343 „substanziell schlechter … bei allem" — Anglizismus + word order.
L345 „und hier wird es interessant" — LLM throat-clearing → „Doch damit ist es nicht getan".
L351 „…, oder den Kindheitshund, oder den Geschmack" — repeated „oder" → one „oder".
L366/L414 „die Art und Weise des virtuellen Selbst, … zu registrieren" — genitive-agent calque → relativize.
L370/L386 „Ähnlich:" sentence-opener — calque of „Similarly:" → „Genauso…/Ebenso".
L372 „bringt keine Erfahrung hervor – sie bringt eine Simulation hervor" — not-X-but-Y + repeat → „…, sondern eine Simulation."
L378 „ein „Außen" zur Wettersimulation" — „outside to" → „der Wettersimulation".
L382 „in verschiedenen Vokabularen" — mass-noun plural → „in unterschiedlichen Begriffen".
L394 „treibt … keine Vermeidung an" — collocation → „löst … kein Vermeidungsverhalten aus".
L396 „Das Triebwerk hat… der Zwilling hat…" — metronome → fold into flowing example.
L398 „nur mehr" — AT-German „no longer" — MISLEADING → „nur in größerem Maßstab".
L400 „Der Unterschied ist nicht der Grad. Es ist die Architektur." — two-beat → „Nicht der Grad…, sondern die Architektur."
L414/448/452/456 „Von innerhalb" — „from within" → „von innen"; „X lebt hier/dort" abstract → „sitzen".
L418 „die einzige Art real, die zählt" — broken calque → „die einzige Realität, die zählt."
L420 „Rahmenwerk" — framework-calque → „Ansatz".
L424 „Dennett mit Extraschritten" — meme calque → „Dennett auf Umwegen" (or flag deliberate).
L438 „Bach sagt dir… Ich sage dir…" — du-address → „uns"; „Dasselbe Ziel, aber ich habe die Baupläne mitgebracht" — ESCALATE (swagger vs personality).
L446 „Hier ist der seltsame Teil:" — the flagged „der Teil" family → „Und jetzt wird es seltsam:".
L452 triple „oder…" + triple „Das ist…" anaphora → collapse.
L456 „offener Faden" → „loses Ende"; English word order rework.
L460 „Hier ist ein Gedankenexperiment…" — „Here's a…" → „Das folgende Gedankenexperiment…".
L462 „jeden einzelnen Tag" → „Tag für Tag".
L468 „über die Zeit" + „Das ist, was … tut" → „im Lauf der Zeit" / „Genau das tut…".

## Kapitel 5 — AIW-92 priority (L471–572) — 30 issues, 0 escalate
L473 „vier Modelle, zwei Achsen, eine Simulation … Darum,… Und darum,…" — countdown-tricolon + anaphora → rework.
L475 four stacked rhetorical questions → cut to two.
L477 „das, das mich … überzeugt hat" — „das, das" clumsy → „genau dieses".
L479 „in dem arbeiten, was … nennen" — calque → „in jenem Bereich…, den … nennen".
L485 not-X-but-Y semicolon → „—…sondern…".
L487 „kommt nirgendwohin" / „davonlaufendes Chaos" — calques → „dreht sich im Kreis" / „entfesseltes Chaos".
L489/L495/L507 Oxford comma before „und" → drop.
L491 „der Teil der gesamten Theorie, bei dem…" — flagged „der Teil" + „es fühlte sich an wie" → rework.
L493 mirrored chiasmus → loosen one half.
L495 mapping-tricolon „X sind die Y" + „saubere Kreise" (clean) → „gleichmäßige Kreise".
L501/L503 „Regler … fragt" personification; „der süße Punkt" (sweet spot!) → „optimaler Bereich"; „stirbt"→„verebbt"; **„Nenn ihn"** du-imperative → „Nennen wir ihn".
L503 „auf dem die Theorie reitet" — „rides on" → „von dem … abhängt".
L505 „das sauberste Bild" (cleanest) → „das klarste Bild"; „gibt den meisten Auftrieb" → „erzeugt"; „brechen" 4× → vary.
L507 „Ein-Knopf-Geschichte" (metaphor mix) + „am Boden" (dialed to the floor) → „Ein-Regler-Erklärung" / „ganz heruntergedreht".
L509 „festnagelte" (nail down) + „nach roher Zahl" + „wie viel Gehirn" + **„Behalte"** du-imperative → rework to „man".
L539 „Ein … Anfall ist, was passiert, wenn… Ein Schlaganfall ist, was passiert…" ×3 → vary.
L551 „auseinander im Ursprung, konvergierend auf" → rework.
L553 „die … ernst nehmen lässt" — missing subject → „bei der man … ernst nimmt".
L563 „Das ist vermutlich, was das Gehirn tut." → „So arbeitet vermutlich das Gehirn."
L567 „bis ganz nach unten" — „all the way down" → „bis auf die unterste Ebene".
L569 „Nicht ein System" → „Kein System".
NOTE (agent): L495–509 densest concentration — clearly never voice-passed, as flagged.

## Kapitel 6 — AIW-92 priority (L573–683) — 33 issues, 2 escalate
L575 „macht sie nicht sicher" → „macht sie kein bisschen ungefährlicher".
L577 escalating comparative-tricolon → drop the middle limb.
L579 „wenn man weiß, worauf man achten muss" — stock calque → „dem geschulten Blick jedenfalls".
L595 three „-areale" parallel → subsume.
L599 „einfach zu komplex, V1 zu höheren Arealen" — „von"-drop → „von … zu …".
L615 „Ja, das klingt faszinierend." — chatbot cadence → delete.
L615 „Nicht so schnell, … Aber genauso…" — antithetical seesaw → rework.
L617 „augenöffnend" — calque → „erhellend"; „--" dashes → „–".
L619 „Wenn man … nur eines mitnimmt:" + climbing parallel + „ikonisch" → rework.
L627 fronted participle „Beraubt seines … Inputs" → „Ohne seinen … Input".
L639 „Wer fernsieht, wird… Wer … liegt, wird… Wer … anschaut, wird…" — tricolon → collapse to two.
L641 „kontrolliert man … kontrollieren" — false friend + repeat → „steuert".
L643 „auf der Erde" (on Earth) → „die man kennt"; „Freitagabend-Kuriosität" calque → rework.
**Two-governors (L653–659):**
L653 „viel Gehirn … gerissen und … maximal reich" — awkward → rework.
L655 „schlichte Ökonomie" → „schlicht Energiehaushalt"; door/brakes mixed metaphor → unify on one image.
L657 „gegen eine innere Simulation" (versus) + „atemberaubend" flourish → rework.
L657 „Die Simulation läuft ihrer … Realitätsprüfung davon, rastet … ein und treibt … ab" — ESCALATE (metaphor salad; author picks governing image).
L657 „mehr Gehirn nach innen zu reißen … überschwemmt … kappt … die Linie … am Boden gehalten" — ESCALATE (leash/flood/line mix; unify at author level).
L659 „die ich noch immer verblüffend finde" — ego intrusion → „die verblüfft:".
L659 **„die Both-Regler-Zustände"** — English „Both" artifact → „Zustände mit beiden Reglern oben".
L659 „Sie sind nicht trotz … Sie sind abgehoben, weil…" — signature not-despite-but-because chiasmus → plain causal.
L663 „das beste Selbst, das es kann" → „so gut es kann"; „Es … Es … Es …" triple → fold.
L665 „Die Inverse" — math calque → „die Umkehrung".
L667 „eine schöne Symmetrie" / „ist, was passiert, wenn" — aesthetic editorializing + calque → rework.
L673 „auf eine … elegante Weise" — editorializing → rework.
L675 „Er hörte es. Er fühlte es. Er erlebte es." — dramatic triple → „Er hat es gehört, gefühlt, erlebt."
L679 „erhöht Durchlässigkeit global" — dropped article → „erhöht die Durchlässigkeit".

## Kapitel 7+8 (L684–845) — 38 issues, 0 escalate
L700 „gibt ihr Bestes mit dem, was sie hat" → „macht das Beste aus dem, was ihr bleibt."
L704 „wiederkehrenden Traum – … der … immer wiederkam" — tautology → trim.
L708 „Was tat der Traum? In den Begriffen der Theorie:" — do-support + „in terms of" → rework.
L710 „Vielleicht sollte ich es." — elliptical calque → add verb.
L714 „der Teil, in dem der Gang zum Schreibtisch stattfand" — flagged „the part where" → „die Phase, in der er … ging".
L716/L791 „niemand ist zu Hause" — idiom calque (keep motif, de-anglicize) → „da ist niemand".
L722 „Im Wachleben tut es das immer." + „Zeit auf … verschwenden" → rework.
L724 „sich bewusst, dass… ×3" + „Einen Moment… Im nächsten…" → rework.
L726 „Luzidität-Einsetzen" — pressed compound → „der Moment, in dem die Luzidität einsetzt".
L730 „unter demselben Etikett laufen" + „produzieren" (experiences) → „denselben Namen tragen" / „hervorrufen".
L734 „Das Ergebnis? Das „K-Hole" –" — throat-clearing → „Das Ergebnis ist das „K-Hole":".
L738 „macht die Unterscheidung ganz natürlich" — calque → „trifft die Unterscheidung mühelos".
L740 „Einen Moment … Im nächsten…" (repeat) → rework.
L742 „stoppt einfach" — Anglizismus → „hört einfach auf".
L756 „Nachschlage-Referenz … keine separaten Mysterien" — redundant + „mysteries" → „zum Nachschlagen … keine getrennten Rätsel".
L763 „Herumwedeln" (hand-waving) + du-imperatives + „an ihren Platz fallen" → rework to „man".
L767 „nur eine Sache … behält" + US-grandeur (every other theory fails) → tone down, keep fact.
L769 „Und er meint es." + „soweit seine … Erfahrung reicht" → rework.
L773 subjectless staccato + „der gesamten Neurowissenschaft" hyperbole + „einen Geist gesehen" → „Gespenst".
L777 „absolut, unerschütterlich überzeugt" — stacked intensifiers → trim.
L779 „erfahrungsgemäß" — wrong word → „im Erleben".
L781/L821 „beste Vermutung … darüber, wie" — recurring calque.
L783 mirrored fragments + „Beide…Beide" + „Paar von Testfällen" grandeur → rework.
L787 „das Denken über … veränderte" → „das Verständnis … veränderte".
L795 „Und das tut er." + „Implikationen" → „Und genau das tut er." / „Folgen".
L799/L807/L843 „Und dann gibt es…" recurring transition → vary.
L803 „Inzwischen dürfte … vertraut klingen." — throat-clearing → trim.
L805 „tut immer seine Arbeit … das es kann" → rework.
L811 „Hat er nicht." — elliptical do-support → „Hat er aber nicht."
L813 „Die Hand tut Dinge…" + „Dieselbe X, unterschiedliche Y." AI-aphorism → „macht Dinge" + don't overuse pattern.
L815 „Die zentrale Erkenntnis … ist:" — throat-clearing → „Diese Syndrome zeigen vor allem eines:".
L819 „Volle Szenen" — „full scenes" → „Ganze Szenen".
L825 „Glitch" — Anglizismus → „Aussetzer".
L827 „mit fast keinem Detail … nahtlose Erfahrung" — calques → rework.
L837/L839 „buchstäblich" (literally) + „Jedes Mal, wenn … Jedes Mal, wenn" → trim.
L841 „Schlag gegen die Macht" — calque → „keine Absage an".
L843 „gelingt, wenn es gelingt" + „soweit … betrifft" → rework.

## Kapitel 9+10 (L846–1008) — 34 issues, 1 escalate
L846/L854 „Zwei Bewusstsein" (unmarked plural, inconsistent w/ L888 „Bewusstseine") → „Bewusstseine".
L848/925/976 „massiv" (massive→big) → „dick/gewaltig/enorm".
L852 „keine Metaphern … Es sind buchstäbliche … Kämpfe" — not-X-but-Y + „literally" → rework.
L852 „Partytricks" — Anglizismus → „Kuriositäten".
L856/L860 „Der Linke-Hemisphären-Interpret" — bound English compound → „Der Interpret der linken Hemisphäre".
L858 „nicht die Teilung – es ist, was passiert, wenn" — calque → „sondern das, was geschieht, wenn".
L862 „Der Patient zögert nicht. Sagt nicht… Schaut nicht…" — fragment triad → one sentence.
L862 „Das ist kein Lügen." — gerund calque → „keine Lüge".
L864 „Und jetzt der Teil, der einem den Schlaf rauben sollte:" — flagged „der Teil" → „Und jetzt kommt, was…".
L864 „Nur die Qualität des Inputs." + „Input" → rework.
L880 „der gleich kommt" — signposting → „der gleich folgt".
L886/L888 „Man bekommt nicht… Man bekommt…" + repeat → „Man erhält nicht … sondern…".
L898 „ist keine Pathologie – es ist die Notfallreaktion" — wrong „es" (→„sie") + not-X-but-Y.
L902 „Performance" (was „Schauspiel") — inconsistent Anglizismus → „Schauspiel".
L902 „Das ist, was man … erwartet." — calque → „Genau das erwartet man…".
L904 „akkommodiert" — Latinism/Anglizismus → „erklärt".
L913+ (Kap10) „—" no-space em-dashes → „ – ".
L925 „Es gab nicht den geringsten Zweifel, dass das Sprache war" — ESCALATE (grandeur/absolute claim; soften to perception).
L929 „Evidenz von … eine Linie ziehen … verheerend für jeden, der" — triple calque → rework.
L931 „Das sind keine Reflexe. Keine … Reaktionen. Das sind…" — negation-triad → „…, sondern ein Geist…".
L933 „Anwesenheit von Empathie" — calque → „Empathie vortäuschen".
L947 „aus der besten Vermutung … konstruiert, was … bedeutet" — word order → rework.
L949 „Warum die Mühe, bei Bewusstsein zu sein?" — „Why bother" → „Wozu der ganze Aufwand…".
L955 „Berühre… spür… Finde…" du-imperatives → „man".
L957 „Buchstäblich fatal." + L958 „Lernen beendet." — „literally" + fragment → rework.
L968 „gletscherhaft langsamen Prozess" — „glacially slow" → „quälend langsam".
L968/L957 „buchstäblich" filler → drop.
L986 „kalibriert … gegen sozialen Input" — „against" + „Input" → „eicht … an der sozialen Rückmeldung".
L992 „Basisches Bewusstsein" — FALSE FRIEND (basic→alkaline!) → „Basales Bewusstsein".
L1004 „(CBT)" — English abbr → „(KVT)".

## Kapitel 11 (L1009–1129) — 34 issues, 1 escalate
L1011 „ist keine Theorie — sie ist eine Geschichte" — dash not-X-it's-Y → „…, sondern eine Geschichte."
L1011 „Hier sind sie." — list throat-clearing → drop.
L1013+ „neurale" (Anglizismus) → „neuronale" (L1013/1019/1113/1117/1123).
L1015 „je eine pro Modell" — Kasus → „je einen".
L1017 „das Gehirn weiß es einfach" — „just knows" → „erkennt es ohne Zutun".
L1019 staccato fragment-triad + „2x2" → „2×2"; rework.
L1021 templated per-prediction closer (recurs L1043/1053/1063/1087/1111/1123) — „nicht nur X — es ist Y" scaffolding → vary; let some end dry.
L1027 „komplett mit Bedeutung und Handlung" — „complete with" → „samt".
L1029 „Verdrahtungsdiagramm" — „wiring diagram" → „Schaltplan"; „Die Vorhersage:" scaffolding (L1041/1061) → vary.
L1035 „und eine, die keine andere … macht" — „and one that" → rework.
L1037 „gradlinig" (typo+semicalque) → „einfach".
L1043 postposed adverbial (English word order) → embed.
L1047 „die seltsamsten Dinge, die das Gehirn tut" — calque → „zum Seltsamsten, wozu … fähig".
L1051 „Jetzt der überraschende Teil." — „der Teil" family → „Jetzt kommt das Überraschende."; „Genau das tun sie." tag (echo L1127).
L1057 „machen ihr eigenes Ding" (do their own thing) + „verschiedene… verschiedene… verschiedene…" triad → rework.
L1059 „gehen die Lichter aus" (plural) → „geht das Licht aus"; standalone „Weil…" fragment → „Denn…".
L1059 dense italics-as-emphasis → reduce.
L1065/1075/1083/1093/1111 „doesn't-X-it-Y" via em-dash (even in headings) → „…, sondern…"/commas.
L1071 „erlebnismäßiger" — ugly -mäßig → „erlebnishafter/phänomenaler".
L1075 „Warum? Weil…" — „Why? Because…" → „Der Grund:".
L1077 „eine 2017-Studie … fand, dass" — adjective-date + „found that" → „eine Studie … aus dem Jahr 2017 zeigte, dass".
L1085 „Es hätte… Es hätte… Es würde…" anaphora + „durch die Zeit läuft" + „jemand zu Hause ist" → rework.
L1091 „auf eine Weise, wie es … die Leber nicht tut" — calque → rework.
L1093 „Neuronen rauschen. … driftet." — staccato quadruple → semicolon-join.
L1093/1103 „dimmen/Dimmen" — Anglizismus → „schwächer werden/Verlöschen".
L1095 „Das ist REM-Schlaf. Das ist Träumen." — twin calque → „Das ist der REM-Schlaf — das Träumen."
L1113/1117/1119 „Alters" — ESCALATE (English plural of DID term; germanize or keep).
L1119 „Zwischen-Alter- / Innerhalb-Alter-Variabilität" — calqued hyphen-compounds → rework.
L1123/1127 „Genau das macht sie brauchbar." — tag calque → „Deshalb taugt sie etwas."

## Kapitel 12 / Pattern 8 — AIW-92 priority (L1130–1285) — 33 issues, 1 escalate
L1140 „ein schneller Test" — quick→schnell false → „ein kurzer Test".
L1142 „bis die Hölle zufriert" — English idiom calque → „bis ans Ende aller Tage".
L1148 „unterscheidet vom … Er unterscheidet nicht vom" — doesn't-X-it-Y + missing object → „grenzt … ab".
L1150 „verliert täglich eine Million Neuronen" — ESCALATE (contradicts L1242 „85.000/Tag").
L1154 „kann kein Negativ beweisen" — „prove a negative" → „eine Abwesenheit nicht beweisen".
L1156 „Es hätte … — nicht … sondern … Es hätte … — nicht … sondern" — doubled anaphoric antithesis → break.
L1156 „dass da jemand zu Hause ist" — „somebody's home" → „dass da wirklich jemand ist".
L1160 „das Bedürfnis, ob man … versteht" — missing verb → „das Bedürfnis zu wissen, ob…".
L1162 „Da skalierst du dich nicht hin. Da baust du…" — du-address → „man"; „Kreislauf und alles" (loop and all) → „mitsamt Kreislauf".
L1172 „ein guter genug Scanner" — „good enough" ungrammatical → „ein hinreichend guter Scanner"; „die Herausforderung nur eine der Auflösung" → „ginge es nur um die Auflösung".
L1182 „Das ist der Teil, der einen um den Schlaf bringt" — flagged „der Teil" (recurs L1146/1158/1192/1230×2/1254) → vary; „es selbstorganisiert zur Kritikalität" → „organisiert sich selbst".
L1200 „jeden Grund zu glauben" — „every reason" → „allen Grund".
L1204 „In jedem sinnvollen Sinne" — calque + echo → „In jeder sinnvollen Hinsicht".
L1208 „Fall erledigt." — „case closed" → „Damit erledigt."
L1210 „jede einzelne Nacht" — „every single" → „Nacht für Nacht".
L1218 „durch eine Lebenszeit des Lernens" (recurs L1280) — „a lifetime of" → „ein Leben voller Lernen"; „ist verstört, dass" — missing prep → „darüber, dass".
L1224 „was, wenn" — „what if" → „was wäre, wenn".
L1246 „Handgewedel" — „hand-waving" → „Spinnerei".
L1250 „Information reist" — „travels" → „breitet sich aus".
L1252 „wirft eigene Albträume auf" — mixed idiom → „bringt eigene Albträume mit sich"; „der Punkt steht" → „es bleibt dabei".
L1254 „Jetzt der Teil, den ich nirgends ehrlich diskutiert gesehen habe" — „der Teil" + participle-stack + „ehrlich/offen" overuse (L1156/1232/1266/1278) → rework.
L1268 „transitiert" — Anglizismus verb → „geht … über".
L1272 „Aufzuwachen und gesagt zu bekommen, dass…" — verbless fragment → add main clause.
L1274 „fühlen … anfühlt" — echo → „nachempfinden".
L1276 „Das ist keine Science-Fiction — es ist eine unvermeidliche Folge" (recurring antithesis; densest here) → rebuild ≥half.
L1278 „Ich will etwas offen sagen." + „Sorge über/genau über" + „Vertrauen, dass" → rework (note: this is the closest passage to the „Grenze ziehen" caveat; harden here).
L1282 „Was heißt:" — „which means" opener → „Das heißt:".
NOTE (agent): the „Und hier muss ich ehrlich eine Grenze ziehen…" paragraph no longer exists in this range; nearest self-justifying passage is L1278. Locked strings not present in this range.

## Kapitel 13 — AIW-92 priority (L1286–1459) — 52 issues, 0 escalate
L1288 „folgen mehrere Dinge" → „ergeben sich mehrere Konsequenzen".
L1290 „das Ausführen eines Videospiels" (execute) → „ein laufendes Videospiel"; „Die Simulation tut es." do-support → „Die Simulation schon."
L1292 „demütigend" — FALSE FRIEND (humbling→humiliating) → „ernüchternd".
L1296 „es zu entwickeln sollte nicht warten" — infinitive-subject → rework; „Rahmenwerk" (L1366) → „Rahmen"; „sich wundern und fürchten" (wonder) → „staunen".
L1298 „bestimmen die Rate" (clock) → „bestimmen den Gang"; „ist das, was … macht" cleft → „Erst … macht"; „erledigt das Schieben" gerund → „besorgt das Substrat"; „keinen Weg, … keinen Weg, … keinen Weg" → „keine Möglichkeit…".
L1300 „rahmt … neu" (reframe) → „stellt … neu".
L1304 „Die halbe Sekunde Lücke" — noun-stack → „Die Halbsekundenlücke".
L1316 „nimmt … die Lorbeeren" → „erntet die Lorbeeren".
L1318 „hier ist, was … übersehen:" — cleft → „fast alle übersehen bei Libet einen Punkt:".
L1322 compressed word order → rework.
L1324–1326 du-drift in mechanism passage → „man" (distinct from deliberate close at L1378).
L1326/L1390 „Und hier kommt eine Überraschung/das Gegengewicht" — announce throat-clearing → cut.
L1328 „blutet in den nächsten hinein" (bleeds into) → „geht … über"; „glatt" (smooth) → „nahtlos". (Blitz/Donner image itself: keep.)
L1336 „Cafe" → „Café" (typo).
L1340 „verfehlt den Punkt … spektakulär" → „geht … am Kern vorbei".
L1342 „tiefste Evidenz" → „stärkster Beleg".
L1344 mid-sentence apposition commas → embed.
L1346 „Wo lässt das … den freien Willen?" — „where does that leave" → „Wo bleibt…".
L1348 „über die Zeit" → „mit der Zeit".
L1350 „Gegenverkehr" (oncoming/collision) → „Verkehr in beide Richtungen".
L1354 „teilweise" (partially→at times) → „zeitweise"; „Präsenzen" → „nichts von außen".
L1358/1360 „Lebenswerk" (magnum opus ≠ „a life's worth") → „ein ganzes Leben".
L1360 „sich austauschen" (dials converse) → „gegeneinander spielen"; „erinnert sein Leben" transitive anglicism → „ruft … in Erinnerung"; tripled doesn't-X-it-Y → break; „seltene Ecke" + telegraphic ellipsis → rework.
L1364 „psychotische Brüche" → „Schübe".
L1372 „fällt … aus der Uhr-Analogie" → „ergibt sich aus"; „auf … Maschinerie reitet" → „aufsitzt".
L1376/1447 „komputational" — non-word → „berechenbar/rechnerisch"; „Sache von Glück" → „Frage des Glücks".
L1378 „bist nicht du es, der entscheidet" — garbled inversion → „bist du es nicht, der…"; „ganz zu dir zurückholen" (bring back to you) → „auf dich beziehen".
L1380 „so viel ist real / Es tut das" do-support → rework.
L1382 „aus eigener Herstellung" (of your own making) → „aus eigenem Stoff".
L1386 „kommt … nirgendwohin" → „nicht vom Fleck"; infinitive-of-purpose „zum Zurückziehen/Bewohnen" → relativize.
L1388/1390 „Supermacht" — FALSE FRIEND (superpower ability→superstate) → „Superkraft"; „keinen Zoll weiter" → „keinen Deut weiter".
L1390 „eingebildet" (imagined/conceited ambiguous) → „vorgestellt". („Gedankenpaläste" LOCKED.)
L1392 „geteilt" (divided vs shared) → „gemeinsam"; „nicht länger" → „nicht mehr". (Danger line LOCKED.)
L1424 „ist keine Theorie — es ist eine Religion" — „es"→„sie"; „Dekade" → „Jahrzehnt".
L1429 „die anderen zwei" → „die anderen beiden".
L1431 „außergewöhnlicher als die letzte" → „…als die andere".
L1435 „projiziert hinunter" → „hinabprojiziert"; L1437 Input/Ausgabe register mix → „Eingabe/Ausgabe".
L1443 „gebe ich frei zu" (freely admit) → „offen zu".
L1451 „rufen Sie mich an" — „Sie" breaks the du-peroration → decide (business-card joke?).
L1453 „empirische Unterstützung" → „empirische Belege"; „festnageln" → „dingfest machen".
L1455 „bevor die Lichter angehen" (plural) → „bevor das Licht angeht".

## Kapitel 14+15 (L1460–1768) — 30 issues, 2 escalate
L1462 „kein künstliches Licht kilometerweit" — word order → „kilometerweit kein Licht"; „Schleier, den man zusammenkneifen musste" — wrong object → „mit zusammengekniffenen Augen".
L1468 „anfing zu ziehen" — thread idiom, no object → „am Faden zu ziehen".
L1498 „stärkste verfügbare Behauptung" — „available" → „die sich vertreten lässt".
L1514 „wie jede Wand es sein könnte" — calque → „wie jede Wand".
L1516 „was gewusst werden kann" — clumsy passive → „was sich … wissen lässt".
L1520/L1644 „Das ist der Punkt / Aber der Punkt ist:" — calque → „Genau darum geht es / Entscheidend ist".
L1526 „ändert … das Denken über alles" → „verändert, wie man … denkt".
L1528/L1550 „Ich denke" (I think) → „Ich glaube"; „Das Inventar." one-word opener → rework.
L1550 „einige Merkmale teilen" → „gemeinsam haben".
L1564 „Konsequenzen — über Zeit, über Materie…" — „about" → „für".
L1580 „kein „Davor" zum Zugreifen" → „auf das man zugreifen könnte".
L1586+ „Rahmenwerk" (~10×: 1586/1592/1594/1598/1600/1602/1610/1616/1620) → vary: „Rahmen/Modell/Ansatz".
L1590 „es zykliert" — non-word → „läuft in Zyklen".
L1598 „bequem … am Horizont sitzt" — „conveniently" → „normalerweise weit draußen".
L1616 „verdient, ausgesprochen zu werden … die Art von Sache, die" — double calque → rework.
L1618 „mathematische Bequemlichkeit" — false friend → „Vereinfachung".
L1632 „Menü" (particle list) → „Auswahl".
L1654 „Volle Offenlegung:" — „Full disclosure" → „Ganz offen gesagt:".
L1662 „nicht über Materie" — „not about" → „handelt nicht von Materie".
L1668 „Fäden zusammenzuziehen" → „zusammenzuführen".
L1670/L1760 „Instanz" — false friend (instance→authority) → „Fall".
L1708 „demütigend" — false friend → „stimmt mich demütig".
L1714 „ehrlich hält" — „keeps me honest" → „zur Ehrlichkeit zwingt".
L1716 „nicht ein Merkmal" → „kein Merkmal".
L1718 „konstitutionell unfähig" — false friend → „gar nicht anders können".
L1730/L1762 „hier ist das, was mich … hinzusetzen" — awe-gesture calque → rework.
L1756 „instanziiert" — heavy Anglizismus → „verwirklicht".
L1735/1743 „informationsundurchsichtig" vs Kap14 „…undurchlässig" — ESCALATE (unify?).
L1740 „Vier-Modelle-Architektur" — ESCALATE flagged BUT: „vier Modelle" is intentional book term → REJECT the „Modellarten" change; only reconfirm.

## Kapitel 16 + Coda (L1769–1964) — 29 issues, 3 escalate
L1771 „Hier kommt es — … lässt es sich nicht mehr übersehen" — opener + „can't be unseen" + dash-drama → rework.
L1773 „Nicht ähnlich. Nicht metaphorisch verwandt. Strukturell identisch." — negation-tricolon (recurs L1811) → fold.
L1781/1795/1801/1807 „Dieselbe … Dieselbe …" anaphora → vary every second.
L1785 „der Teil, der berechnet, … der Teil, wo etwas passiert" — „der Teil" calque → rework.
L1799 „Der Sweet Spot, der Ort, wo Bewusstsein lebt" — Anglizismus + „where … lives" → „Der schmale Grat…".
L1811 „hier bitte ich um kurzes Innehalten" — throat-clearing → drop; „Dinnerpartys" + dinner-party trope → „Abendessengespräch".
L1815 „nicht weil … und nicht weil … Weil …" + „Das ist es, was … tun" → rework.
L1869 „Die Poesie würde überleben. Die Physik vielleicht nicht." — AI button (optional).
L1875/L1905 „Nicht weil … Nicht weil … Weil …" + „hart genug versucht" — repeated triad + calque → vary both.
L1877 „Ehrlich?" — „Honestly?" tic → „Um ehrlich zu sein:".
L1881 „Killer-Einwand … über den ich nachts wach liege … Der, den" — Anglizismus + confessional calque → rework.
L1889 „Symmetrie zu finden das ist, was wir tun" — cleft → „…nun einmal darauf aus ist…".
L1907 „Die Lücke ist keine Ignoranz." — FALSE FRIEND → „keine Unwissenheit".
L1909/1811/1815/1787 ALL-CAPS emphasis → italics.
L1911 „Voller Kreis" (heading) — calque → „Der Kreis schließt sich."
L1913 „Bringen wir das nach Hause." — „bring this home" → „Fassen wir zusammen."
L1917 „sich selbst berechnen, … modellieren, … erleben" — closing tricolon swell → tighten.
L1931 „Niemand las sie … Forschung [hat] aufgeholt … bewiesen werden konnten" — ESCALATE (hero's-journey vindication arc; „bewiesen" also a strength claim).
L1935 „Das ist, was es tut. Das ist alles, was es tut." — double calque → „Mehr tut es nicht. Nichts sonst."
L1937 „anderes alles" → „alles anders"; „Hatte nie jemand." inverted echo → rework.
L1939 „Ich war sicher, dass ich sterben würde. Ich sah mein ganzes Leben…" — ESCALATE (NDE testimony; dry deflation mostly rescues it — trim setup?).
L1941 „der gruselige Teil" — „der Teil" → „das Unheimliche daran"; „als Nachgedanke" → „fast nebenbei".
L1943 „Und dann gab es den … Traum" — „And then there was" → „Dazu kam…".
L1949 „der ultimative Trip" — Anglizismus (keep joke) → „der letzte große Trip".
L1955 „ein großes genug Universum … generischer genug Prozess" — ungrammatical „genug" → „hinreichend groß … hinreichend generisch".
L1961 „Seid nett zueinander…" — ESCALATE (ihr-address + „be kind" US sign-off; keep as earned final beat or impersonalize?).
