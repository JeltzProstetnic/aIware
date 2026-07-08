# Culture & Tone Guide — French (standard/international) · AIW-108-FR

**Every translation agent receives this verbatim, alongside the glossary.**

## Variant (LOCKED)
- **Standard international French** (France-centric orthography, readable across France, Belgium, Suisse, Québec,
  Afrique francophone). No regionalisms, no Québec-specific or Belgian-specific lexicon.
- **Reader-address: "vous" (vouvoiement).** French serious/popular-science nonfiction addresses the unknown reader
  with "vous" — it reads as respectful and natural, NOT distant. Do NOT use "tu" for the reader (too casual for this
  register). Example: "Imaginez que vous jouez à un jeu vidéo." Keep "vous" consistent throughout.

## Register & voice
- **Educated general reader.** Warm, vivid, confident — narrative popular science, not a textbook, not a hype pitch.
- **Grandeur calibration = the WARM MIDDLE.** The EN voice runs high/grand; the DE voice was dialed DOWN for DACH
  reserve. FR sits **between**: French nonfiction accepts intellectual elegance and narrative sweep, but recoils
  from US-style self-promotion. If a sentence sounds like marketing in French, soften toward the DE register. When
  unsure whether a grand claim survives, **keep the meaning, flag the tone** (§D) — do not silently flatten OR inflate.
- **Sentence rhythm:** French tolerates elegant subordination but not German-length chains. Keep the author's punch;
  short declaratives land in French too. Avoid the flat calqued word order of English.

## Sources — how to combine EN + DE (per chunk you get both)
- **Translate the EN** (fuller "grandeur" voice = primary source).
- **Consult the DE** to: (a) disambiguate meaning (DE = source of truth for meaning), (b) inherit native-idiom
  solutions the German pass already found, (c) calibrate grandeur toward the warm middle.
- Where EN and DE differ in *content*, **DE wins on meaning**. If they genuinely conflict, translate the EN but note
  it (do not guess silently).

## Typography (French rules — IMPORTANT)
- **Guillemets « » as PRIMARY**, with the conventional inner spacing (« mot »). Nested quotes = "guillemets anglais".
  In prose you write the characters « … » (spacing/glyphs handled at build).
- **Space before double punctuation:** French puts a (non-breaking) space before ; : ! ? and inside « ». Follow this.
- **Em-dash / tiret:** use — for parenthetical asides as in EN.
- **Numbers:** keep numbers as the EN has them — do NOT reformat digits. Spell small numbers in prose as EN does.
- **Capitalization:** French titles capitalize only the first word + proper nouns ("Chapitre 2 : Les quatre modèles",
  with a space before the colon — NOT "Les Quatre Modèles"), EXCEPT the fixed term "Théorie des Quatre Modèles" and
  the model names, which stay capitalized as in the glossary.

## Do-not-localize list
- The author's personal anecdotes, biography, and place references (keep his life as lived).
- Proper names, citations, DOIs, reference entries (glossary §4).
- Culturally-specific examples STAY; if an idiom won't land, translate the *meaning* naturally (that is the culture
  pass's job in Phase 4 — in Phase 1 prefer a faithful natural rendering and flag doubtful ones).

## Output contract (STRICT)
- Return **only the French translation of the EN span you were given** — same paragraph/heading structure, same
  Markdown (##, **bold**, *italic*, lists, blockquotes) in the same places.
- Do **NOT** add, drop, merge, or reorder paragraphs. No translator notes in the prose. One EN paragraph → one FR paragraph.
- Preserve Markdown headings exactly (translate the heading TEXT, keep the `##` level).
- If a span is a reference list or pure citations, return it **verbatim** (do not translate bibliographic entries).
