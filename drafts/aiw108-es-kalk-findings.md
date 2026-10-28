# AIW-108 — ES Kalk-scan findings (native-Spanish calque/naturalness sweep)

Session 252, 2026-07-08. Method: 36 parallel **Fable-5** native-Spanish editors over the whole assembled
`pop-sci/book-manuscript-es.md` (36 segments, ~68 ln each), each returning surgical A/B/C/D findings only (no
wholesale rewriting), scanning for calques of BOTH source languages (EN **and** DE), false friends, wrong
collocations, glossary/typography/reader-address violations, and genuine awkwardness. Mirrors the AIW-107 German
Kalk methodology. **354 findings total: A=245, B=85, C=21, D=3.**

## A. APPLIED — 242 objective fixes (of 245 A-findings)
Applied via verified match-once script (`tmp/kalk_apply.py`, each quote matched exactly once). All meaning-preserving
calque/false-friend/collocation/typography/glossary corrections. Full list: `tmp/es-kalk/a_all.json`; visible in the
manuscript git diff. By type: anglicism×96, fluency×45, false-friend×34, collocation×29, typography×19, glossary×16, germanism×4, register×2.

### A-items NOT auto-applied (3) — for the human native reviewer
- **[seg 10 · anglicism]** «No están en negación en el sentido psicológico»
  → propuesta: «No lo niegan en el sentido psicológico»
  — "en negación" calques English "in denial".
- **[seg 23 · anglicism]** «colapsa de vuelta a un solo punto»
  → propuesta: «colapsa de nuevo en un solo punto»
  — 'collapses back to' calque; 'de vuelta a' unidiomatic with colapsar.
- **[seg 25 · fluency]** «el mundo que ves ahora mismo, el yo que sientes ser»
  → propuesta: «el mundo que ves ahora mismo, el yo que sientes que eres»
  — "sientes ser" calques "feel yourself to be"; natural is "sientes que eres".

## B. HELD for MG — voice/style/meaning judgment calls (85, NOT applied)
- **[seg 01 · fluency]** «a unos treinta centímetros de tu cara»
  → propuesta: «a unos treinta centímetros de tus ojos»
  — "tu cara" repeats from previous sentence's ending; minor echo.
- **[seg 02 · fluency]** «La genera alrededor de un kilo y medio»
  → propuesta: «La genera aproximadamente un kilo y medio»
  — Tras «genera», «alrededor de» se lee espacial — frase jardín; «aproximadamente» desambigua.
- **[seg 02 · anglicism]** «Esa sensación es el tema entero de este libro.»
  → propuesta: «Esa sensación es todo el tema de este libro.»
  — «el tema entero» huele a «the entire subject»; leve, decisión de voz.
- **[seg 02 · anglicism]** «Estás teniendo una experiencia.»
  → propuesta: «Estás viviendo una experiencia.»
  — «estar teniendo» suena calco; pero «tener una experiencia» es término filosófico — juicio.
- **[seg 02 · fluency]** «o bien (lo más honesto) la perspectiva de ser explicado por completo resulta»
  → propuesta: «o bien (lo más honesto) sucede que la perspectiva de ser explicado por completo resulta»
  — Anacoluto: tercer miembro rompe la lista de «se invocan»; quizá retórica deliberada del EN.
- **[seg 03 · register]** «los ingenieros puedan monitorizar el sistema e interactuar»
  → propuesta: «los ingenieros puedan supervisar el sistema e interactuar»
  — 'monitorizar' leans Iberian (LatAm 'monitorear'); 'supervisar' is pan-Hispanic.
- **[seg 04 · anglicism]** «un proceso virtual que corre sobre hardware neuronal»
  → propuesta: «un proceso virtual que se ejecuta sobre hardware neuronal»
  — 'correr' for software is a mild anglicism; glossary itself used 'ejecutándose'. Voice call.
- **[seg 05 · fluency]** «paisajes y personajes y física y luz»
  → propuesta: «paisajes, personajes, física y luz»
  — English polysyndeton (and...and...and) reads as translationese in Spanish.
- **[seg 05 · collocation]** «los trucos de fiesta más reveladores»
  → propuesta: «los trucos de salón más reveladores»
  — 'party trick' calque; 'truco de salón' is the natural Spanish collocation.
- **[seg 05 · fluency]** «no suelen encajar cuatro de cuatro a lo largo de»
  → propuesta: «no suelen encajar las cuatro a lo largo de»
  — 'four for four' sports idiom calque; awkward in Spanish.
- **[seg 05 · fluency]** «un latido, no hay nadie en casa»
  → propuesta: «un latido, no hay nadie al mando»
  — 'nobody home' idiom calque; doesn't carry the no-one-conscious sense naturally in ES.
- **[seg 06 · fluency]** «No puedes preguntar con sentido»
  → propuesta: «No tiene sentido preguntar»
  — «preguntar con sentido» es wittgensteiniano-libresco; alternativa más fluida para pop-sci.
- **[seg 06 · fluency]** «la versión lenta y almacenada de ti mismo que el sueño deja atrás»
  → propuesta: «la versión lenta y almacenada de ti mismo que sobrevive al sueño»
  — «deja atrás» sugiere abandono; el sentido es que persiste al borrado.
- **[seg 06 · germanism]** «que el «tú» sentido es un proceso virtual»
  → propuesta: «que el «tú» que sientes es un proceso virtual»
  — «el tú sentido» (das gefühlte Du) ambiguo: «sentido» se lee como sustantivo.
- **[seg 06 · anglicism]** «Concede que el cerebro ejecuta una autosimulación. Concede la arquitectura de cuatro modelos»
  → propuesta: «Concedamos que el cerebro ejecuta una autosimulación. Concedamos la arquitectura de cuatro modelos»
  — Imperativo «Concede» calca «Grant that»; español filosófico prefiere «concedamos».
- **[seg 06 · anglicism]** «el Problema Difícil sigue viviendo en otra dirección»
  → propuesta: «el Problema Difícil sigue vivo, solo que en otro domicilio»
  — «en otra dirección» se lee primero como rumbo, no domicilio; juego EN ambiguo.
- **[seg 06 · anglicism]** «Aférrate a esa brecha. Es el capítulo entero.»
  → propuesta: «Aférrate a esa brecha. Todo el capítulo está en ella.»
  — «Es el capítulo entero» calca «It's the whole chapter»; lectura literal desconcierta.
- **[seg 06 · anglicism]** «Este es el movimiento más fuerte disponible dentro del fisicalismo de procesos»
  → propuesta: «Esta es la jugada más fuerte disponible dentro del fisicalismo de procesos»
  — «movimiento» calca el «move» argumentativo; «jugada» es lo natural. Tono grande: decide autor.
- **[seg 07 · fluency]** «se topa con una opacidad de principio»
  → propuesta: «se topa con una opacidad de raíz»
  — "de principio" suena a calco de "in-principle"; "en principio" significaría otra cosa.
- **[seg 08 · fluency]** «colapsa fuera del régimen del borde del caos»
  → propuesta: «sale del régimen del borde del caos»
  — 'colapsar fuera de' reads as English 'collapse out of'; slightly unnatural.
- **[seg 10 · glossary]** «el Modelo Explícito del Mundo (EWM) nunca incluye el déficit»
  → propuesta: «el Modelo Explícito del Yo (ESM) nunca incluye el déficit»
  — Bodily paralysis is self-model territory; ISM→ESM pairing expected, EWM likely wrong — verify vs source.
- **[seg 11 · fluency]** «pero no hay nadie en casa»
  → propuesta: «pero dentro no hay nadie»
  — Calque of English idiom 'nobody home'; vivid image — hold for author.
- **[seg 11 · fluency]** «y todo se sentía distinto»
  → propuesta: «y todo resultaba distinto»
  — Mild calque of 'everything felt different'; borderline — hold.
- **[seg 12 · anglicism]** «recibe input visual a través de vías subcorticales»
  → propuesta: «recibe información visual a través de vías subcorticales»
  — unadapted anglicism 'input' recurs; 'entrada/información' more natural — book-wide call.
- **[seg 12 · anglicism]** «No hay nadie en casa, no porque la persona»
  → propuesta: «No hay nadie dentro, no porque la persona»
  — 'nobody home' English idiom; literal calque may not carry in ES.
- **[seg 12 · collocation]** «para crear una experiencia sin costuras»
  → propuesta: «para crear una experiencia sin fisuras»
  — 'sin costuras' calques 'seamless'; 'sin fisuras/continua' more idiomatic.
- **[seg 12 · collocation]** «que su sangre se ha drenado»
  → propuesta: «que su sangre se ha secado»
  — reflexive 'drenarse' for blood is a calque of 'drained'.
- **[seg 13 · anglicism]** «Solo cambia la calidad del input.»
  → propuesta: «Solo cambia la calidad de la información de entrada.»
  — 'input' anglicism; recurs 3x in segment — likely deliberate, held for author.
- **[seg 13 · fluency]** «y apuesta una prueba a ello»
  → propuesta: «y apuesta una predicción comprobable a ello»
  — 'apostar una prueba a ello' is not idiomatic; clunky rendering.
- **[seg 13 · fluency]** «abierta a palanca lo bastante como para poder ver a través de ella»
  → propuesta: «forzada como con una palanca lo justo para poder ver a través de ella»
  — 'abierta a palanca' reads unnatural; imagery-heavy, held for author.
- **[seg 13 · anglicism]** «mi primer pensamiento fue que quería comernos»
  → propuesta: «lo primero que pensé fue que quería comernos»
  — Mild calque of 'my first thought was'; more natural reworded.
- **[seg 15 · fluency]** «la simulación del recién nacido es delgada»
  → propuesta: «la simulación del recién nacido es tenue»
  — "delgada" (physically thin) calques EN "thin"; "tenue" fits an abstract, faint simulation.
- **[seg 15 · anglicism]** «La habitación ha sido preparada antes de que llegues.»
  → propuesta: «Han preparado la habitación antes de que llegues.»
  — Agentless periphrastic passive reads as EN calque; active/impersonal is more natural.
- **[seg 16 · anglicism]** «hasta que el infierno se congele»
  → propuesta: «hasta el fin de los tiempos»
  — Calque of 'until hell freezes over'; propose native idiom, voice call.
- **[seg 16 · anglicism]** «A las teorías hay que acercarles los pies al fuego»
  → propuesta: «A las teorías hay que ponerlas contra las cuerdas»
  — Calque of 'hold their feet to the fire'; but fire image is extended next sentence—hold.
- **[seg 16 · register]** «Piensa en los supervivientes de un ictus»
  → propuesta: «Piensa en los supervivientes de un derrame cerebral»
  — 'ictus' is Spain-favored; 'derrame cerebral' more pan-Hispanic.
- **[seg 16 · fluency]** «La entrada entra, pasa por capas de atención y cómputo, y la salida sale»
  → propuesta: «La entrada llega, pasa por capas de atención y cómputo, y la salida emerge»
  — 'entrada entra'/'salida sale' tautological in Spanish; reads as stutter.
- **[seg 17 · false-friend]** «Si la carga mental llega a funcionar alguna vez»
  → propuesta: «Si la transferencia mental llega a funcionar alguna vez»
  — 'carga mental' reads as cognitive load; also inconsistent with «mind uploading»/«transferencia mental» used later. Term choice for author.
- **[seg 17 · anglicism]** «El sustrato sobre el que corres ahora mismo»
  → propuesta: «El sustrato sobre el que te ejecutas ahora mismo»
  — 'correr' for software running is an anglicism (recurs as the substrate metaphor); global voice call for author.
- **[seg 18 · collocation]** «el confinamiento en solitario quiebra a las personas al privarlas de estímulo sensorial y social»
  → propuesta: «el aislamiento prolongado quiebra a las personas al privarlas de estímulos sensoriales y sociales»
  — «solitary confinement» calcado; «estímulo» singular raro — juicio
- **[seg 18 · anglicism]** «que el «verdadero» tú sigue caminando por ahí»
  → propuesta: «que tu «verdadero» yo sigue caminando por ahí»
  — «the real you» calcado; pero el libro juega con «tú» — juicio
- **[seg 18 · anglicism]** «Esa es una receta para el sufrimiento a una escala»
  → propuesta: «Eso anuncia un sufrimiento a una escala»
  — «recipe for» anglicismo hoy asentado — decisión de voz
- **[seg 18 · fluency]** «pero en el que no hay nadie en casa dentro de nadie»
  → propuesta: «pero en el que, dentro de cada uno, no hay nadie en casa»
  — «nobody home» literal; imagen posiblemente deliberada — juicio
- **[seg 18 · false-friend]** «Una última línea de defensa de la agencia humana.»
  → propuesta: «Una última línea de defensa de la voluntad humana.»
  — «agencia» tecnicismo filosófico, opaco para lector general — juicio
- **[seg 18 · fluency]** «Aquí está el truco: sin que el sujeto lo supiera»
  → propuesta: «Y aquí viene el truco: sin que el sujeto lo supiera»
  — presentativo «here's the trick» calcado — matiz de voz
- **[seg 18 · glossary]** «implementar la arquitectura de los cuatro modelos en la criticalidad»
  → propuesta: «implementar la arquitectura de los cuatro modelos en criticalidad»
  — segmento mezcla «en criticalidad» y «en la criticalidad» — unificar
- **[seg 20 · false-friend]** «La única libertad en oferta»
  → propuesta: «La única libertad disponible»
  — «en oferta» reads as 'on sale/discount'; calque of 'on offer'. Chapter title — author call.
- **[seg 20 · false-friend]** «libertad que alguna vez estuvo en oferta»
  → propuesta: «libertad que alguna vez estuvo disponible»
  — Same 'on offer' calque as title; must move together with it.
- **[seg 20 · fluency]** «Hay tres discrepancias que deberías vigilar como un halcón»
  → propuesta: «Hay tres versiones de ti que deberías vigilar sin quitarles ojo»
  — List items are selves, not discrepancies (incoherent with «brecha entre ellas»); hawk simile is an anglicism.
- **[seg 20 · register]** «resulta que alcanza para construir una vida sobre ella»
  → propuesta: «resulta que basta para construir una vida sobre ella»
  — «alcanza» = 'suffices' is LatAm-leaning; «basta» is pan-Hispanic neutral.
- **[seg 20 · anglicism]** «no por el incienso ni las playlists»
  → propuesta: «no por el incienso ni las listas de reproducción»
  — «playlists» is a raw anglicism; widely used though — author call.
- **[seg 20 · anglicism]** «has rebotado contra ella —cosa común»
  → propuesta: «te has estrellado contra ella —cosa común»
  — 'Bounced off it' calque; in Spain «rebotado» also reads as 'miffed'.
- **[seg 20 · anglicism]** «Honestamente, de los dos, la meditación»
  → propuesta: «Francamente, de los dos, la meditación»
  — Sentence-initial «Honestamente» is an EN discourse-marker calque; «Francamente» is native.
- **[seg 20 · anglicism]** «Es una pregunta fundacional para la que no tengo»
  → propuesta: «Es una pregunta fundamental para la que no tengo»
  — «fundacional» strictly means 'of a founding'; 'foundational' calque — judgment call.
- **[seg 20 · glossary]** «computa en la frontera entre el orden y el caos»
  → propuesta: «computa en el borde entre el orden y el caos»
  — Glossary motif uses «borde» (borde del caos); «frontera» drifts from the fixed image.
- **[seg 21 · anglicism]** «Hay una de ellas que no pude dejar en paz»
  → propuesta: «Hay una de ellas que no me dejaba en paz»
  — Spanish idiom reverses agency: the question haunts you; author call.
- **[seg 21 · fluency]** «Este es ese trabajo.»
  → propuesta: «Aquí empieza ese trabajo.»
  — este/ese clash stumbles; proposed keeps the punch — author call.
- **[seg 21 · false-friend]** «Bien podría no existir.»
  → propuesta: «Para ti, es como si no existiera.»
  — EN 'might as well not exist' ≠ epistemic «bien podría»; meaning call.
- **[seg 22 · false-friend]** «Las fronteras definen la arena. Fuera de la arena, las reglas no se aplican»
  → propuesta: «Las fronteras definen el terreno de juego. Fuera de ese terreno, las reglas no se aplican»
  — "arena" momentarily reads as sand; DRAE-valid but voice call for author.
- **[seg 23 · false-friend]** «una conveniencia matemática más que una afirmación física»
  → propuesta: «una comodidad matemática más que una afirmación física»
  — 'mathematical convenience'; 'comodidad' more native, but 'conveniencia' attested in physics ES.
- **[seg 23 · anglicism]** «Superficies de singularidad hasta el fondo, hasta lo más alto y en cada escala intermedia.»
  → propuesta: «Superficies de singularidad en lo más profundo, en lo más alto y en cada escala intermedia.»
  — 'all the way down/up' calque; may be intentional turtles-echo — author call.
- **[seg 24 · fluency]** «Impermeables a la información, saturadas hasta el límite de Bekenstein y delimitando el dominio computacional.»
  → propuesta: «Impermeables a la información, saturadas hasta el límite de Bekenstein, delimitan el dominio computacional.»
  — Gerund coordinated with adjectives is awkward; fragment vs clause is a style call.
- **[seg 24 · false-friend]** «o bien su reivindicación más profunda»
  → propuesta: «o bien su validación más profunda»
  — EN «vindication»; «reivindicación» leans claim/demand — defensible but held for author.
- **[seg 26 · collocation]** «No son sustancias separadas. Comercian entre sí.»
  → propuesta: «No son sustancias separadas. Se intercambian.»
  — «Comerciar» odd for physical quantities; may continue deliberate economic metaphor («te cobra»).
- **[seg 26 · false-friend]** «entre dos representaciones del mismo material»
  → propuesta: «entre dos representaciones de lo mismo»
  — «material» reads as physical matter; EN «stuff» means the same underlying thing.
- **[seg 26 · anglicism]** «mostrarte por qué el patrón no es opcional»
  → propuesta: «mostrarte por qué el patrón es inevitable»
  — «no es opcional» calques EN «not optional»; meaning is forced/necessary given axioms.
- **[seg 26 · anglicism]** «Aquí están los cinco axiomas.»
  → propuesta: «Estos son los cinco axiomas.»
  — Presentational «Aquí están X» mirrors EN «Here are»; «Estos son» more idiomatic.
- **[seg 26 · anglicism]** «Juntos, lo restringen a exactamente una.»
  → propuesta: «Juntos, lo restringen a una sola.»
  — «a exactamente una» is calqued word order; «a una sola» flows naturally.
- **[seg 26 · anglicism]** «Lo planteé hace un capítulo»
  → propuesta: «Lo planteé en el capítulo anterior»
  — «hace un capítulo» calques «a chapter ago»; possibly deliberate playful voice — author call.
- **[seg 27 · anglicism]** «a partir del input disponible»
  → propuesta: «a partir de la información disponible»
  — «Input» es anglicismo evitable, pero podría ser registro computacional deliberado (cf. hardware).
- **[seg 27 · anglicism]** «editor y verificador cruzado durante todo el proceso»
  → propuesta: «editor y herramienta de verificación cruzada durante todo el proceso»
  — «Verificador cruzado» aplicado a un agente calca «cross-checker».
- **[seg 29 · false-friend]** «la firma psicodélica característica que resulta»
  → propuesta: «la huella psicodélica característica que resulta»
  — 'firma'='signature' calque; recurs as table header — decide book-wide.
- **[seg 29 · anglicism]** «factores motivacionales. El campo lo ignoró»
  → propuesta: «factores motivacionales. La disciplina lo ignoró»
  — 'el campo'='the field' (discipline) is an English calque.
- **[seg 29 · fluency]** «se hace accesible a la conciencia por orden»
  → propuesta: «se hace accesible a la conciencia de forma secuencial»
  — 'por orden' reads as 'by command'; sense is 'in sequence'.
- **[seg 30 · anglicism]** «Esa observación ya concede el punto»
  → propuesta: «Esa observación ya concede lo esencial»
  — 'Concede the point' is debate-English; borderline in Spanish — author call.
- **[seg 30 · fluency]** «Aquí va el segundo, y es más afilado»
  → propuesta: «Aquí va el segundo, y es más incisivo»
  — 'Sharp' link mixes metaphor; 'incisivo' more natural — voice call.
- **[seg 30 · fluency]** «la motivación pertenece al interior de la inteligencia»
  → propuesta: «la motivación está dentro de la inteligencia»
  — 'Belongs inside' calque; stilted but emphasis may be intended.
- **[seg 30 · fluency]** «Quien esté a gusto con la versión intuitiva»
  → propuesta: «Quien se dé por satisfecho con la versión intuitiva»
  — 'Comfortable with the version' calque-tinged; 'a gusto con' borderline — author call.
- **[seg 30 · collocation]** «este patrón: rendimientos que crecen con el tiempo»
  → propuesta: «este patrón: beneficios que crecen con el tiempo»
  — 'rendimientos' (returns) collides with component term 'Rendimiento' (Performance).
- **[seg 31 · false-friend]** «el espectro del desorden era: 1 → 2 → 4 → 3. Incómodo.»
  → propuesta: «el espectro del desorden era: 1 → 2 → 4 → 3. Poco elegante.»
  — «Incómodo» renders EN «awkward» oddly for an ordering; judgment call.
- **[seg 31 · anglicism]** «puedes saltar hacia adelante sin ejecutar cada paso»
  → propuesta: «puedes ir directamente al resultado sin ejecutar cada paso»
  — «saltar hacia adelante» calques EN «jump ahead»; mildly unnatural.
- **[seg 32 · collocation]** «generando lentas ondas delta»
  → propuesta: «generando ondas delta lentas»
  — Preposed adjective; standard neuro collocation is 'ondas delta lentas'.
- **[seg 33 · fluency]** «intenta empujar un dedo a través de la palma de tu otra mano»
  → propuesta: «intenta atravesar con un dedo la palma de tu otra mano»
  — "empujar … a través de" reads as calque of "push through".
- **[seg 34 · anglicism]** «los capítulos que siguen la mostrarán realizando un verdadero trabajo explicativo»
  → propuesta: «los capítulos que siguen mostrarán que realiza un verdadero trabajo explicativo»
  — "show it doing work" gerund calque; grammatical but anglicized — author call.
- **[seg 35 · anglicism]** «de que de verdad hay alguien en casa»
  → propuesta: «de que de verdad hay alguien ahí dentro»
  — 'alguien en casa' calques EN 'somebody home'; image may be intended — hold.

## D. CULTURAL-GRANDEUR flags — MG's call (3, NOT applied)
- **[seg 02 · grandeur]** «hace predicciones que ninguna teoría rival puede igualar»
  → propuesta: «hace predicciones que ninguna teoría rival ha podido igualar»
  — Alarde de superioridad estilo EN; punto medio cálido sugiere formulación empírica, no absoluta.
- **[seg 07 · grandeur]** «Solo que yo traje los planos.»
  — Se posiciona por encima de Bach; posible tono de autopromoción. Decisión del autor.
- **[seg 18 · grandeur]** «Ese es un poder extraordinario, y no tengo ninguna confianza en que la humanidad esté lista para él.»
  → propuesta: «Es un poder enorme, y no confío en que la humanidad esté preparada para él.»
  — autoengrandecimiento estilo EN; calibrar al punto medio cálido

## C. KEPT as-is — deliberate recurring motifs (21)
- **[seg 01 · motif]** «por qué algo se siente como algo»
  — Deliberate recurring motif (echoes ch. 4 title) — do not "correct".
- **[seg 02 · motif]** «por qué leer se siente como algo»
  — «se siente como algo» = motivo nuclear recurrente del libro; no «corregir» nunca.
- **[seg 02 · germanism]** «la piedra más pesada de toda mi vida se me caía de encima»
  — Parece calco de «ein Stein fiel mir vom Herzen», pero es imagen autoral intensificada — conservar.
- **[seg 06 · motif]** «sin costuras, y nunca llegas a ver la juntura»
  — «sin costuras» parece anglicismo (seamless) pero sostiene la imagen costura/juntura; conservar.
- **[seg 06 · motif]** «donde has estado de pie todo este tiempo»
  — Motivo deliberado del «estar de pie» dentro de la simulación (anécdota inicial); no corregir.
- **[seg 06 · motif]** «una simulación que corre sobre un sustrato»
  — «correr» (software) es opción deliberada y consistente del libro, natural en LatAm; conservar.
- **[seg 07 · motif]** «corre sobre hardware biológico»
  — Anglicismo ("run on") pero motivo recurrente: simulación que "corre sobre" un sustrato. No corregir.
- **[seg 15 · motif]** «el «yo» renderizado, eso que está leyendo»
  — "renderizar/renderizador" is a deliberate recurring self-as-rendered-image motif; do not de-anglicize.
- **[seg 18 · motif]** «Un ejército de ti.»
  — eco deliberado del motivo bloqueado «cuántos de ti» (cap. 14) — no corregir
- **[seg 18 · motif]** «Dice que la simulación correrá.»
  — «correr» = run (software), motivo recurrente del libro, natural en LatAm — mantener
- **[seg 20 · motif]** «quién sabe si volverás, y cuántos de ti»
  — Glossary §3 locked ch.14 danger-line motif — HOLD for MG, do not edit.
- **[seg 20 · motif]** «El lento agarre hacia afuera construyó civilizaciones»
  — Recurring outward/inward «agarre» (grip) motif — keep consistent, not a calque.
- **[seg 21 · motif]** «antes de que se enciendan las luces»
  — Deliberate recurring 'lights come on' consciousness image — do not correct.
- **[seg 21 · motif]** «sin la mano de nadie en el dial»
  — Two-dials motif (glossary §3) — deliberate, keep.
- **[seg 23 · motif]** «El acertijo del balón medicinal se disuelve.»
  — Deliberate 'disolver, no resolver' motif (mirrors dissolving the Hard Problem); keep.
- **[seg 24 · motif]** «el cuadro completo, porque no hay afuera»
  — «no hay afuera» echoes the deliberate «afuera» motif — do not correct.
- **[seg 26 · motif]** «Entrada, proceso y salida son la misma cosa.»
  — Deliberate fixed-point motif, echoed later in segment («entrada, proceso y salida…»); keep verbatim.
- **[seg 27 · motif]** «una simulación autorreferencial que corre en el borde del caos»
  — «Correr» (software run) es motivo computacional deliberado del libro — no corregir.
- **[seg 30 · motif]** «Debajo hay un suelo subconsciente»
  — 'Floor' imagery likely deliberate (glossary's 'felt floor' motif) — keep.
- **[seg 30 · motif]** «Encima cabalga la capa conscientemente enmarcada»
  — 'Consciously framed layer' recurs consistently (also line 32) — deliberate term, keep.
- **[seg 34 · motif]** «esto es el libro mayor que hay detrás»
  — "Libro mayor" = ledger, deliberate accounting metaphor (contabilidad de fronteras). Keep.

## Phase-4 mechanical consistency — PASS
- Reader-address: `tú` only; **0** vosotros/vos.
- Glossary terms intact; the 2 `consciencia` hits are `inconsciencia` (correct). `conciencia` used correctly.
- Typography: «guillemets» primary; the ASCII `"` instances are correct RAE nesting + an EN citation title.
- Model abbreviations IWM/EWM/ISM/ESM + FMT present and unaltered; "Teoría de los Cuatro Modelos" ×47.

**Status:** ES = **publish-candidate**. Gate: human native Spanish review (§0.3) before any KDP upload.
