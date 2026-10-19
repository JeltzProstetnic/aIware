# Culture & Tone Guide — Dutch · AIW-108-NL

**Every translation agent receives this verbatim, alongside the glossary.**

## Variant & register (LOCKED)
- **Standard Netherlands Dutch (nl-NL)**, trade nonfiction (bol.com / Standaard Boekhandel). No Flemish/Belgian lexis or word order, no dialect, no youth slang.
- **Register = informal "je/jij" — LOCKED. Do NOT use "u".** This is the register of published Dutch popular-science nonfiction: warm, direct, confident, addressing an educated general reader as a peer. "u" would import a distancing formality (brochure/officialese) the original does not have and that Dutch pop-science deliberately avoids; "je" is how the genre takes the reader by the hand. The ONLY exceptions: (a) direct quoted speech inside „" keeps its own natural register; (b) genuinely institutional/quoted formal registers where the source itself is formal.
- **Reader-address — how to render the EN "you":**
  - **Default: "je"** (subject and object), possessive **"je"** / emphatic **"jouw"**. Most EN "you do X / you see Y" sentences become "je doet X / je ziet Y".
  - **"jij" (stressed) only where the second person itself carries the argument's weight** — the passages where the book turns and points at the reader ("YOU are the character the brain creates" → „JIJ bent het personage dat het brein creëert"). There, "jij" is the payload; keep it. Budget guideline: if stressed "jij" appears more than a couple of times per page, you are over-using it — most instances are unstressed "je".
  - **Imperatives for the do-this-now passages** (e.g. the blind-spot demo) take the informal singular: "Sluit je linkeroog", "Houd het boek …", "Kijk naar de X". Never the "u"-imperative ("Sluit u …").
  - Never "men" for direct address (impersonal, wrong register); "de lezer" ("the reader") only in genuinely meta passages.

## Register & voice
- **Educated general reader.** Warm, vivid, confident — narrative popular science, not a textbook, not hype.
- **Grandeur calibration = RESERVED, at or below the German dial.** Project policy: the farther from US culture, the more traditional/reserved. EN runs high/grand; DE was dialed down for DACH reserve; **Dutch dials down at least as far.** Dutch nonfiction culture is famously nuchter — "doe maar gewoon, dan doe je al gek genoeg" — and recoils from US-style self-promotion and superlatives; big claims persuade in Dutch through precision and understatement, not through grandeur. Concretely: keep the WONDER (the ocean, the edge of chaos, the simulation turn), strip the SALESMANSHIP. If a sentence sounds like ad copy or a TED-talk applause line, soften toward sober statement — keep the full meaning, and **flag the tone call in your output rather than silently flattening OR inflating**. Understatement is the default resolution; deletion is never. Note: the DE edition already tempered the author's most personal/grand passage (the Innsbruck bridge) into something quieter — take DE, not EN, as the ceiling there.
- **Sentence rhythm:** Respect Dutch V2 word order and clause structure — do not calque English word order, and avoid the overlong tangconstructie (verb stranded far from its subject) when breaking up English periodic sentences. Keep the author's punch: where the EN lands a short, hard sentence, land a short, hard Dutch one.
- **Compounds:** Dutch closes compounds (zelfmodel, wereldmodel, geheugenpaleis, toegangsbewustzijn) — never split them English-style. Dutch does NOT capitalise common nouns (unlike German): write "het bewustzijn", "het brein", not "das"-style caps.

## Sources — how to combine EN + DE (per chunk you get both)
- **Translate the EN** (fuller "grandeur" voice = primary source).
- **Consult the DE** for meaning (DE = source of truth for meaning), for reserved-register calibration, and to disambiguate whatever the EN leaves loose. Dutch and German are close, but do NOT calque German syntax, German compounds, or German idiom — render into natural Dutch.
- Where EN and DE differ in *content*, DE wins on meaning; if they genuinely conflict, translate the EN but note it.

## Typography (Dutch)
- **Quotation marks: „lage-hoge dubbele" PRIMARY** — opening low „ (U+201E), closing high " (U+201D). For quotes nested inside quotes and for emphasis-quotes use **‚single low-high'** (‚ U+201A / ' U+2019). Book and work titles → *italics* (Markdown `*…*`), e.g. *De Ego-Tunnel*. NO «guillemets», NO Western "straight" or "curly" double quotes as the primary form anywhere in Dutch prose. (Latin-script spans left verbatim — citations, DOIs — keep whatever punctuation they came with.)
- **Dash / aside: the spaced en-dash " – " (kort gedachtestreepje, U+2013 with a space on each side) — LOCKED.** Use it for parenthetical asides and the dramatic pivots where the EN uses "—". Never a bare em-dash "—", never "~", never "...". Ellipsis = the single glyph "…" (U+2026), not three periods.
- **Numbers: Dutch conventions.** Decimal separator = comma (1,5 kilogram); thousands separator = period or thin space (3.000 meter). Convert EN "3,000 meters" → "3.000 meter" and EN "1.5 kg" → "1,5 kg". Do NOT keep the English point-decimal / comma-thousands. Number-words spelled out in EN prose may become natural Dutch number-words ("anderhalve kilogram").
- **Emphasis/italics:** Preserve the Markdown markers (**…**, *…*) exactly in place per the output contract. Render EN caps-for-emphasis by wording or *italics*, not by shouting caps; keep the Markdown. No ALL-CAPS emphasis in the Dutch body except where a glossary term is deliberately set that way.
- No ¿ ¡ (Spanish only).

## Do-not-localize list
- The author's personal anecdotes, biography, and place references (keep his life as lived — an Austrian author's world: Innsbruck, the bridge, the 2015 German self-published book — not transposed to the Netherlands).
- Proper names, citations, DOIs, reference entries, researcher names (glossary §4 — Dutch does not transliterate names).
- Culturally-specific examples STAY; if an idiom won't land, translate the *meaning* naturally and flag doubtful ones (the culture pass in Phase 4 refines — in Phase 1 prefer a faithful natural rendering).

## Output contract (STRICT)
- Return **only the Dutch translation of the EN span** — same paragraph/heading structure, same Markdown (##, **bold**, *italic*, lists, blockquotes) in the same places.
- Do NOT add, drop, merge, or reorder paragraphs. No translator notes in the body (flags go in the designated flag channel, not inline). **One EN paragraph → one Dutch paragraph.**
- Preserve Markdown headings exactly (translate heading TEXT, keep the `##` level).
- Preserve image references, figure captions, and links exactly — translate only the visible caption text, keep the path/URL verbatim.
- If a span is a reference list or pure citations, return it **verbatim**.
