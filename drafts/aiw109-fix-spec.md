# AIW-109 — Canonical fix spec for the 6 translation editions

**For:** per-language fix agents (ES/FR/PT/IT/JA/ZH). EN + DE are already done (source editions).
**Method (HARD):** For every change, use the **Edit** tool only — never sed/awk/Bash writes. Each find→replace must match **exactly once** (`count==1`) in the file; if it matches 0 or >1, grep to find the right unique context and narrow the string. Locate every item by grepping for the concept (line numbers below are from the shipped editions and may have drifted). Do NOT commit/push. When done, report the list of find→replace pairs you applied + a grep verification (defect-gone / fix-present counts).

**Translate the CHANGE, not the English.** Below each careful rewrite is the EN BEFORE and EN AFTER. Find the equivalent passage in your language and rewrite it so it says what the EN AFTER says, **matching the existing translation's voice and register** (this is a published literary book — no translationese, no AI-slop). Keep the surrounding sentences intact.

---

## HARD CONSTRAINTS (do NOT violate)
- **Kanzi anecdotes (Ch.10, ice-cream/sister + dance): KEEP AS-IS. Do not touch.** (Author confirmed.)
- **Joscha Bach quote (Ch.4): KEEP AS-IS. Do not touch.** (Verbatim confirmed.)
- **Bruno J. Gruber is ALIVE** — the acknowledgment must be present-tense/active, never death-implying. Never add death dates.
- **Do NOT change the COGITATE "Nature (2025)" citation** — that one is correct. Only the *IIT-pseudoscience* citation is wrong.
- **"Thomas Kuhn" (the philosopher of science, "pre-paradigm") stays UNaccented.** Only "Kühn & Brass" (Simone Kühn, the free-will veto researcher) gets the umlaut.
- Do not invent content. If a passage doesn't exist in your edition, skip it and note "not present".

---

## SOURCE-SHARED CAREFUL REWRITES (translate the change)

### 1. Wegner "I Spy" (Ch.13) — the current text wrongly describes "two mice / one hidden / confederate secretly controls cursor / subject imagines moving". The REAL experiment (Wegner & Wheatley 1999, "I Spy") is:
- EN AFTER: "Daniel Wegner and Thalia Wheatley drove this home with an experiment that is, frankly, devastating — the "I Spy" study. A participant and a confederate posing as a second subject rested their hands together on a small board mounted over a single computer mouse, like two people on a Ouija board's planchette, and together slid a cursor around a screen crowded with little objects. Every so often a musical cue told them to stop, and the participant rated how much they felt they had *intended* to stop where they did. Both wore headphones: the participant heard music with the occasional spoken word dropped in, while the confederate heard the real instructions about when and where to force a stop."
- Then: "on the rigged trials the confederate alone steered the cursor onto a particular object and forced the stop — and, a second or so beforehand, the participant heard that object's name over the headphones. The participant had chosen nothing; the movement was entirely the confederate's. Yet when the word they had just heard matched the object sitting under the cursor, participants reported that they had meant to stop there. They genuinely believed they had done it."
- And the follow-up sentence "It's sufficient to imagine performing an action…" becomes: "It's enough for a thought about an outcome to arrive just before that outcome for the mind to claim it as its own doing — provided nothing visibly contradicts the assumption."
- NOTE: your edition's Notes/appendix already refers to the "I Spy" experiment — so the body currently contradicts its own notes. This fixes that.

### 2. Callosotomy attribution (Ch.9) — surgery misattributed to Sperry & Gazzaniga.
- EN BEFORE: "In the 1960s, Roger Sperry and Michael Gazzaniga performed one of the most dramatic experiments… they surgically severed the corpus callosum…"
- EN AFTER: "In the 1960s, one of the most dramatic experiments in the history of neuroscience took shape. To treat severe epilepsy, the surgeons Philip Vogel and Joseph Bogen severed the corpus callosum — … — and Roger Sperry and Michael Gazzaniga then studied the patients who resulted." (Surgeons Vogel & Bogen cut; Sperry & Gazzaniga studied.)

### 3. Anton's syndrome model label (Ch.6) — mis-assigned to the Self model.
- The parenthetical "Anton's syndrome (the ESM generating vision from memory when the eyes aren't working)" → change **ESM → EWM** (Explicit World Model). Anton's = false *vision* = a WORLD-model failure, not a self-model failure. Leave Cotard's and conversion disorder as ESM.

### 4. Hawking/Bekenstein "didn't read each other's papers" (Ch.17) — FALSE (their black-hole entropy work was intertwined; Hawking radiation confirmed Bekenstein) and self-contradicts the joint Bekenstein-Hawking credit elsewhere.
- EN BEFORE: "These three results were developed independently. Landauer… Bekenstein… Hawking… They were not collaborating. They were not reading each other's papers. And yet all three results converge…"
- EN AFTER: "These results came from very different starting points. Landauer was thinking about computers; Bekenstein and Hawking about the thermodynamics of black holes. Landauer's work belonged to a different field entirely, worked out decades earlier and for unrelated reasons. And yet all of it converges on the same hypothesis…" (Remove the false "not reading each other's papers" claim.)

### 5. Seizure = off-criticality in EITHER direction (Ch.5, the ConCrit paragraph's last sentence). Currently says consciousness goes incoherent when "pushed PAST criticality (by seizure)" — but seizure can be lock-step hypersynchrony (below) OR runaway chaos (above); the same chapter already says both directions elsewhere.
- EN BEFORE: "When it's pushed past criticality (by seizure, possibly by some drug states), consciousness becomes incoherent."
- EN AFTER: "When it's driven off the critical point in the other direction — collapsing into lock-step hypersynchrony or exploding into runaway chaos, as in a seizure and possibly some drug states — consciousness becomes incoherent."

### 6. Cocaine harm is mostly vascular (Ch.6) — currently lumps cocaine with meth/alcohol as directly destroying neurons.
- EN BEFORE: "Cocaine, methamphetamine, and alcohol physically destroy neurons."
- EN AFTER: "Methamphetamine and alcohol physically destroy neurons; cocaine does its damage more indirectly, chiefly by constricting blood vessels and starving neural tissue of oxygen."

---

## SOURCE-SHARED MECHANICAL FIXES (find the equivalent, apply the change)

1. **Libet date** (Ch.13 body): "1979" → **"1983"** (the readiness-potential free-will study is Libet, Gleason, Wright & Pearl **1983**). In the Notes/refs, the "Libet (1979, 1985)" list → **"Libet (1979, 1983, 1985)"** (add 1983).
2. **Salvia** (Ch.6): "the strongest psychedelic substance on Earth" → add "**naturally occurring**" ("the strongest naturally occurring psychedelic…"). LSD is stronger by mass but synthetic.
3. **Fruit-fly connectome** (Ch.12): "fruit fly partial connectomes are now available" → "**the first complete connectome of an adult fruit-fly brain — roughly 140,000 neurons — was published in 2024**".
4. **Wolfram class count** (Notes, Ch.15): the Notes attribute a "five-class hierarchy" to Wolfram → Wolfram had **four** classes; the fifth is the author's own extension. Reword to "Wolfram's four classes, which this book extends to five" (or your language's equivalent). (The main-text Ch.5 passage that says "Wolfram classified… into four… I think it needs a fifth" is CORRECT — leave it.)
5. **Schartner year** (Notes, Ch.7): "Schartner et al. (2015)" → **"(2017)"** (2015 = the propofol paper; ketamine entropy = 2017).
6. **IIT-pseudoscience citation** (Notes, Ch.1): "…documented in Nature Neuroscience (2025)" → "**…in an open letter posted to PsyArXiv (September 2023)**". (124 signatories, 15 Sept 2023.) Leave the COGITATE "Nature (2025)" citation untouched.
7. **Reptile cortical layers** (Ch.2): "three or four cortical layers" → "**three**" (the 3→6 doubling narrative needs three).
8. **Bekenstein/unitarity** (Appendix F): the flat claim "unitarity is a consequence of the Bekenstein bound" → hedge (e.g. "unitarity may itself be underwritten by the Bekenstein bound").
9. **Rule 30 "compressible"** (Appendix C): where Rule 30's structure is called "deterministic and compressible", clarify that "compressible" means **low Kolmogorov complexity (a short rule generates it)**, NOT that the step-by-step computation can be shortcut (it stays computationally **irreducible**). Add a short clarifying clause.
10. **Diacritics**: "Kühn & Brass" / "Kühn and Brass" (with umlaut, = Simone Kühn) in both body (Ch.13) and Notes — NOT Thomas Kuhn. "Bérut et al. (2012)" (with acute, = Antoine Bérut) in Notes Ch.17.
11. **HTML comment** (~Ch.3): delete the leftover line `<!-- FUTURE: Color edition figure — ego perspective dissolving into neural substrate. SDXL prompt preserved in git history. -->` (identical English in every edition). **When deleting, keep exactly ONE blank line between the two surrounding paragraphs — do not merge them.**
12. **GitHub URL** (Notes header): "github.com/JeltzProstetnic/aIware/references.md" → "github.com/JeltzProstetnic/aIware/**blob/main/**references.md".
13. **Bruno acknowledgment** (Acknowledgments): if it reads as a completed-life summary ("whose life in physics showed me…"), make it present-tense/active ("whose work in physics shows me… looks like"). HE IS ALIVE.
14. **Author age** (Coda): "I'm fifty" (or your edition's number) → drop the number, age-robust (e.g. "I'm decades older now"). Author b.1978.
15. **Leaked build markers**: grep for any `<!-- chunk … -->` or stray HTML/markdown build artifacts and delete them.
16. **Aphorism** ("a theory that claims/hides X isn't a theory — it's a religion / a sales pitch"): if it appears 3× (typically Ch.14 open-questions, Ch.16 weaknesses, Ch.17/appendix weak-points), **KEEP the first (Ch.14) and remove the aphorism from the other two** (reword so the sentence still flows without the "it's a religion/sales pitch" punchline).

---

## PER-EDITION items are supplied separately in each agent's brief (§2 of the QA doc): typography, calques, term-consistency, TOC↔heading title mismatches, and BLOCKERs (FR raw-English editor note / garbled sentences / unclosed italic; PT corrupted paragraph / English-labelled figures / meaning-inversion).
