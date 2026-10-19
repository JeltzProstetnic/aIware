# Culture & Tone Guide — Greek · AIW-108-EL

**Every translation agent receives this verbatim, alongside the glossary.**

## Variant & register (LOCKED)
- **Standard Modern Greek (νεοελληνική δημοτική), MONOTONIC (μονοτονικό) — LOCKED.** One tonos only; no polytonic
  accents, no dialect (no Cypriot, no καθαρεύουσα archaisms). This is the register of published Greek popular-science
  and consciousness-science nonfiction (the Greek Metzinger, Dennett, Damasio, Sacks translations run here): educated,
  assertive, warm, readable. Confident theoretical claims stated plainly.
  - Avoid καθαρεύουσα fossils where a living δημοτική word exists — but keep the learned register of scientific prose
    (established Greek scientific compounds like αυτοαναφορικός, κρισιμότητα are correct, not "archaic").
- **Reader-address — replaces the IT "tu" rule. LOCK second-person SINGULAR familiar (ενικός/οικείος).** The book
  takes the reader intimately by the hand ("close your left eye", "hold the book at arm's length"); this matches the
  German **du** exactly. **Never the formal plural εσείς/πληθυντικός ευγενείας** — it would distance the reader and
  read like a manual or a lecture.
  - **Default: DROP the pronoun.** Greek is pro-drop; person is carried by the verb ending. "you close your eye" →
    «κλείνεις το μάτι σου», not «εσύ κλείνεις…». A text peppered with εσύ reads heavy and unnatural.
  - **Imperatives for the do-this-now passages** (the blind-spot demo): singular imperative — «Κράτησε το βιβλίο…»,
    «Κλείσε το αριστερό σου μάτι», «Κοίτα το Χ». This is how Greek science writing directs the reader.
  - **Conjectural engagement:** «ίσως σκεφτείς…», «μπορεί να νιώθεις…», «θα αναρωτηθείς ίσως» for the EN rhetorical
    "you might think…".
  - **εσύ explicit ONLY where the second person itself carries the argument's weight** — e.g. the turn where the book
    points at the reader ("the character the brain creates is *you*" → «ο χαρακτήρας που δημιουργεί ο εγκέφαλος — αυτός
    είσαι εσύ»). There, εσύ is the payload; keep it. Budget: if εσύ appears more than a couple of times per page, you
    are over-using it.
  - Consistency: keep number/gender of address singular throughout. Do NOT switch to εμείς ("we") except where the EN
    genuinely says "we" (the shared-human-condition passages: «ζούμε μέσα σε μια προσομοίωση»).

## Register & voice
- **Educated general reader.** Warm, vivid, confident — narrative popular science, not a textbook, not hype.
- **Grandeur calibration = RESERVED, at or below the German dial.** Project policy: the farther from US promotional
  culture, the more reserved. EN runs high/grand; DE was dialed down for DACH reserve; **Greek sits at or below the
  German level** — Greek nonfiction persuades through precision, clarity, and understatement, not through superlatives
  or TED-talk applause lines. Concretely: keep the WONDER (the ocean, the edge of chaos, the simulation turn), strip
  the SALESMANSHIP. If a sentence sounds like ad copy, soften toward sober statement — keep the full meaning, and
  **flag the tone call in your output rather than silently flattening OR inflating**. Understatement is the default
  resolution; deletion is never.
- **Sentence rhythm:** Break English periodic sentences into natural Greek flow — Greek tolerates longer periods than
  German, but do not calque English word order or stack participles. Keep the author's punch: where the EN lands a
  short, hard sentence, land a short, hard Greek one.

## Sources — how to combine EN + DE (per chunk you get both)
- **Translate the EN** (fuller "grandeur" voice = primary source).
- **Consult the DE** for meaning (DE = source of truth for meaning), for reserved-register calibration, and to
  disambiguate whatever the EN leaves loose. Do NOT inherit German idiom or sentence architecture — neither transfers
  to Greek.
- Where EN and DE differ in *content*, DE wins on meaning; if they genuinely conflict, translate the EN but note it.

## Typography (Greek)
- **Quotation marks: «εισαγωγικά» (guillemets) PRIMARY; “διπλά ανωφερή” for (a) quotes nested inside «…» and (b) titles
  of works within prose.** NO „low-high“ German quotes, NO Western "straight" quotes, NO Japanese 「」 brackets anywhere
  in Greek prose. (Latin-script spans left verbatim — citations, DOIs — keep whatever punctuation they came with.)
- **Greek question mark = «;» (Greek erotimatiko — looks like a semicolon).** LOCKED. Never a Latin "?" in Greek prose.
- **Greek "semicolon" = «·» (άνω τελεία, the raised dot).** Use it where the EN uses a semicolon for a mid-sentence
  break; the low Latin ";" is the QUESTION mark in Greek and must never be used as a semicolon.
- **Em-dash / aside: «—» (em-dash, U+2014).** Use it for parenthetical asides and dramatic pivots where the EN uses
  "—". Ellipsis = «…» (U+2026, single glyph).
- **Numbers: keep Arabic numerals as the EN has them.** Do NOT convert to Greek numerals (Αʹ, Βʹ). Do NOT reformat
  digit grouping or force a decimal comma. Number-words spelled out in EN prose may become natural Greek number-words
  (δεκαπέντε εκατοστά).
- **Emphasis/italics:** Preserve the Markdown markers (**…**, *…*) exactly in place per the output contract —
  downstream typesetting converts them. Do not substitute quotation marks for emphasis on your own. Keep *qualia* and
  other Latin technical loans in italics.
- **No ¿ ¡ (Spanish only), no ALL-CAPS shouting** — render EN caps-for-emphasis by «…» or wording, keep the Markdown.
- **Final -ν rules & elision:** apply standard δημοτική orthography (τον/την, elision σ' / ν' where natural). Do not
  hypercorrect.

## Do-not-localize list
- The author's personal anecdotes, biography, and place references (keep his life as lived — an Austrian author's
  world: the bridge in Innsbruck stays Ίνσμπρουκ, not transposed to Athens).
- Proper names, citations, DOIs, reference entries (glossary §4).
- Culturally-specific examples STAY; if an idiom won't land, translate the *meaning* naturally (the culture pass in
  Phase 4 refines — in Phase 1 prefer a faithful natural rendering and flag doubtful ones).

## Output contract (STRICT)
- Return **only the Greek translation of the EN span** — same paragraph/heading structure, same Markdown
  (##, **bold**, *italic*, lists, blockquotes) in the same places.
- Do NOT add, drop, merge, or reorder paragraphs. No translator notes in the body (flags go in the designated flag
  channel, not inline). **One EN paragraph → one Greek paragraph.**
- Preserve Markdown headings exactly (translate heading TEXT, keep the `##` level).
- If a span is a reference list or pure citations, return it **verbatim**.
- Keep IWM/EWM/ISM/ESM/FMT and all Latin technical acronyms verbatim; keep *qualia* as the Latin term.
