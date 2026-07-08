# Culture & Tone Guide — ES neutro/internacional · AIW-108

**Every translation agent receives this verbatim, alongside the glossary.**

## Variant (LOCKED)
- **Neutral/international Spanish (español neutro).** Reach = Spain + all Latin America.
- **Second person: ustedes / usted-neutral.** The book addresses the reader directly and warmly. Use the
  informal singular **"tú"** for the reader-address (pop-sci intimacy: "imagina que sostienes este libro…"),
  which reads natural across Spain + most of LatAm. **NEVER "vosotros"** (Spain-only) and **no "vos"** (Rioplatense).
  Plural you → "ustedes". Keep reader-address consistent in "tú" throughout.
- **No region-specific slang, no localisms.** Neutral lexical choices (e.g. "ordenador/computadora" → prefer the
  neutral "computadora" or reword to avoid; "móvil/celular" → "teléfono"). When a word splits Spain vs LatAm,
  pick the pan-Hispanic option or rephrase.

## Register & voice
- **Educated general reader.** Warm, vivid, confident — narrative pop-science, not a textbook, not a TED-talk pitch.
- **Grandeur calibration = the WARM MIDDLE.** The EN voice runs high/grand; the DE voice was dialed DOWN for DACH
  reserve. ES target sits **between**: Spanish pop-sci accepts narrative warmth and wonder, but **not US-style
  self-promotion or hype**. If a sentence sounds like a marketing boast in Spanish, soften it toward the DE
  register. When unsure whether a grand claim survives in ES, **keep the meaning, flag the tone** (§D of the Kalk
  structure) — do not silently flatten OR inflate.
- **Sentence rhythm:** Spanish tolerates longer periods than English but shorter than German. Break German-length
  chains; don't merge English staccato into one clause. Keep the author's punch — short declaratives land in ES too.

## Sources — how to combine EN + DE (per chunk you get both)
- **Translate the EN** (fuller "grandeur" voice = primary source).
- **Consult the DE** to: (a) disambiguate meaning (DE = source of truth for meaning), (b) inherit native-idiom
  solutions the German Kalk pass already found, (c) calibrate grandeur toward the warm middle.
- Where EN and DE differ in *content* (not just tone), **DE wins on meaning**; keep the EN's fuller phrasing only
  if it doesn't contradict DE. If they genuinely conflict, translate the EN but note it (do not guess silently).

## Typography (RAE)
- **Quotation marks: «comillas angulares/guillemets» as PRIMARY.** Nested = "comillas inglesas". Innermost = 'simples'.
  (In prose you write plain «…»; the LaTeX build handles glyphs later — you write the characters « ».)
- **Dialogue / em-dash:** use — (raya) for parenthetical asides as in EN.
- **Decimals & thousands:** neutral Spanish → decimal comma is traditional but international sci often keeps the
  point; **keep numbers as the EN has them** unless it's a spelled-out quantity — do not reformat digits (the
  build/typesetting is not your job). Spell small numbers in prose as EN does.
- **Capitalization:** Spanish does NOT capitalize every title-word. Chapter titles: capitalize only the first word +
  proper nouns ("Capítulo 2: Los cuatro modelos", not "Los Cuatro Modelos" — EXCEPT the fixed term
  "Teoría de los Cuatro Modelos" and the model names, which stay capitalized as defined in the glossary).
- **¿ ¡** opening marks required on questions/exclamations.

## Do-not-localize list
- The author's personal anecdotes, biography, and place references (keep his life as lived — do not relocate to a
  Spanish setting).
- Proper names, citations, DOIs, reference entries (see glossary §4).
- Culturally-specific examples STAY, but if an idiom won't land in Spanish, translate the *meaning* naturally
  (that's the culture pass's job in Phase 4 — in Phase 1 prefer a faithful natural rendering, flag the doubtful ones).

## Output contract (STRICT)
- Return **only the Spanish translation of the EN span you were given** — same paragraph/heading structure, same
  Markdown (##, **bold**, *italic*, lists, blockquotes) in the same places.
- Do **NOT** add, drop, merge, or reorder paragraphs. Do NOT add translator notes inside the prose. Do NOT rewrite
  structure. One EN paragraph → one ES paragraph.
- Preserve Markdown headings exactly (translate the heading TEXT, keep the `##` level).
- If a span is a reference list or pure citations, return it **verbatim** (do not translate bibliographic entries).
