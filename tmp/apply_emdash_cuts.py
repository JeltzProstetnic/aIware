#!/usr/bin/env python3
"""Apply remaining em-dash audit cuts to book-manuscript.md.

Each cut is a (old_text, new_text) pair from the audit.
The script finds and replaces each one, reporting results.
"""

import sys

MANUSCRIPT = "/home/jeltz/aIware/pop-sci/book-manuscript.md"

# All CUT recommendations from the em-dash audit.
# Format: (old_text_substring, new_text_substring)
# These are the REMAINING cuts that may not have been applied in Session 82.
CUTS = [
    # ======== Chapter 2 (L227, L249, L279x2, L295, L299, L329, L341, L349x2) ========
    # L227: sandwich → parens
    ("when an illusion collapses — when you suddenly see it both ways — you catch",
     "when an illusion collapses (when you suddenly see it both ways), you catch"),
    # L249: sandwich → parens
    ("The simulation — your conscious experience — runs at the very top",
     "The simulation (your conscious experience) runs at the very top"),
    # L279: cluster - two gloss-dashes to parens
    ("Your motor skills — riding a bike, typing, playing an instrument",
     "Your motor skills (riding a bike, typing, playing an instrument)"),
    ("Your autobiographical memory structure — the framework that organizes your memories into a life story",
     "Your autobiographical memory structure (the framework that organizes your memories into a life story)"),
    # L295: sandwich → parens
    ("The **real side** — the two implicit models — is physical",
     "The **real side** (the two implicit models) is physical"),
    # L299: sandwich → parens
    ("The **virtual side** — the two explicit models — is simulated",
     "The **virtual side** (the two explicit models) is simulated"),
    # L329: lazy break → period
    ("This is a well-known anatomical fact — you can see it in any neurobiology textbook",
     "This is a well-known anatomical fact. You can see it in any neurobiology textbook"),
    # L341: lazy break → period
    ("I'm not claiming Layer 4 does this and Layer 5 does that — it's an observation",
     "I'm not claiming Layer 4 does this and Layer 5 does that. It's an observation"),
    # L349: cluster cuts
    ("the octopus, with its radically distributed nervous system — eight semi-autonomous arms, each with its own neural processing center containing roughly 40 million neurons — represents",
     "the octopus, with its radically distributed nervous system (eight semi-autonomous arms, each with its own neural processing center containing roughly 40 million neurons) represents"),
    ("their pallium organized into nuclear clusters rather than sheets — yet crows make tools",
     "their pallium organized into nuclear clusters rather than sheets, yet crows make tools"),

    # ======== Chapter 3 (L357x2, L381, L395, L421, L425) ========
    # L357: cluster - two filler dashes to commas
    ("Not on the screen, exactly — the screen just displays light patterns. Not in the graphics card or the CPU, exactly — those are running",
     "Not on the screen, exactly, the screen just displays light patterns. Not in the graphics card or the CPU, exactly, those are running"),
    # L381: sandwich → parens
    ("self-referential closure — the simulation observing itself from inside — is, I argue,",
     "self-referential closure (the simulation observing itself from inside) is, I argue,"),
    # L395: lazy break → period
    ("CBT does exactly this — it systematically identifies",
     "CBT does exactly this. It systematically identifies"),
    # L421: gloss → parens
    ("a part contains the whole, at lower resolution — but unlike",
     "a part contains the whole, at lower resolution) but unlike"),
    # Alternate L421 pattern
    ("It's what I call a *patchwork hologram* — a part contains the whole, at lower resolution",
     "It's what I call a *patchwork hologram* (a part contains the whole, at lower resolution)"),
    # L425: causal → comma
    ("Small strokes and small lesions often cause surprisingly mild deficits — because within any given cortical area",
     "Small strokes and small lesions often cause surprisingly mild deficits, because within any given cortical area"),

    # ======== Chapter 4 (L441, L463, L473, L475x3, L487, L493, L515, L523, L537) ========
    # L441: sandwich → parens
    ("The physical processing — neurons firing, synapses transmitting, the implicit models storing and computing — has no experience",
     "The physical processing (neurons firing, synapses transmitting, the implicit models storing and computing) has no experience"),
    # L463: sandwich → parens
    ("an identity claim — the kind of claim that, in science, marks a resting point rather than a gap",
     "an identity claim (the kind of claim that, in science, marks a resting point rather than a gap)"),
    # L473: gloss → parens
    ("a digital twin — an engineering simulation of a jet engine",
     "a digital twin (an engineering simulation of a jet engine)"),
    # L475: 6-dash paragraph - 3 cuts
    ("mirror the substrate's processing — it *adds* phenomenal valence",
     "mirror the substrate's processing. It *adds* phenomenal valence"),
    ("They don't exist at the substrate level (neurons don't feel pain any more than metal feels fatigue) — they exist at the simulation level",
     "They don't exist at the substrate level (neurons don't feel pain any more than metal feels fatigue). They exist at the simulation level"),
    ("the kind where reflexes won't suffice — the simulated self must register",
     "the kind where reflexes won't suffice. The simulated self must register"),
    # L487: cluster → period
    ("the weight of the book in your hands — illusionism says",
     "the weight of the book in your hands. Illusionism says"),
    # L493: sandwich → parens
    ("The simulation level — the explicit models, the virtual world and virtual self — has genuine experience",
     "The simulation level (the explicit models, the virtual world and virtual self) has genuine experience"),
    # L515: sandwich → parens
    ("the conscious \"you\" — the virtual self — cannot see the machinery",
     "the conscious \"you\" (the virtual self) cannot see the machinery"),
    # L523: cluster → period
    ("below the surface of your experience — that uncanny feeling",
     "below the surface of your experience. That uncanny feeling"),
    # L537: cluster → period
    ("binding the old and new personas into a single story — this is what your brain already does every night",
     "binding the old and new personas into a single story. This is what your brain already does every night"),

    # ======== Chapter 5 (L543x2, L553x2, L559, L563x2, L579, L583, L587x2, L593, L621) ========
    # L543: triple sandwich → parens
    ("what the architecture looks like — four models, two axes, a simulation running on a substrate",
     "what the architecture looks like (four models, two axes, a simulation running on a substrate)"),
    ("what identity is — a reconstruction, assembled fresh each morning",
     "what identity is (a reconstruction, assembled fresh each morning"),
    # L553: cluster → comma
    ("static and periodic systems — too simple to compute anything interesting",
     "static and periodic systems, too simple to compute anything interesting"),
    ("chaotic systems — too disordered for any stable patterns to form",
     "chaotic systems, too disordered for any stable patterns to form"),
    # L559: gloss → parens
    ("the cortical automaton itself — the engine of consciousness",
     "the cortical automaton itself (the engine of consciousness)"),
    # L563: two definitions → parens
    ("the physical one — the substrate must operate at criticality",
     "the physical one (the substrate must operate at criticality)"),
    ("the functional one — the substrate must implement the four-model architecture",
     "the functional one (the substrate must implement the four-model architecture)"),
    # L579: practical aside → parens
    ("Wait for any afterimages to fade — this takes about 30 to 60 seconds",
     "Wait for any afterimages to fade (this takes about 30 to 60 seconds)"),
    # L583: lazy break → period
    ("it's when you stop trying to see that you start seeing — the automaton starts recruiting",
     "it's when you stop trying to see that you start seeing. The automaton starts recruiting"),
    # L587: cluster - 2 cuts
    ("relaxed, passive, not straining to see — the patterns gradually synchronize",
     "relaxed, passive, not straining to see, the patterns gradually synchronize"),
    ("whether in the thalamus or the cortex itself — the mechanism is the same",
     "whether in the thalamus or the cortex itself. The mechanism is the same"),
    # L593: gloss → parens
    ("An epileptic seizure is what happens when parts of the automaton fall into Class 1 or 2 dynamics — periodic, locked, computationally useless",
     "An epileptic seizure is what happens when parts of the automaton fall into Class 1 or 2 dynamics (periodic, locked, computationally useless)"),
    # L621: lazy break → period
    ("the principle I've been describing doesn't just apply to consciousness by analogy — it's literally how the universe works",
     "the principle I've been describing doesn't just apply to consciousness by analogy. It's literally how the universe works"),

    # ======== Chapter 6 (L673, L675x3, L709) ========
    # L673: light → comma
    ("and this is a trainable skill — you get access to the full simulation",
     "and this is a trainable skill, you get access to the full simulation"),
    # L675: 6-dash cluster - 3 cuts
    ("Remember the five nested systems — Physical, Electrochemical, Proteomic, Topological, Virtual",
     "Remember the five nested systems (Physical, Electrochemical, Proteomic, Topological, Virtual)"),
    ("acting at the **electrochemical** level — they change how neurons talk to each other",
     "acting at the **electrochemical** level. They change how neurons talk to each other"),
    ("They change everything *above* the matter, in ascending order — this is a crucial distinction",
     "They change everything *above* the matter, in ascending order. This is a crucial distinction"),
    # L709: lazy break → period
    ("which acts on a single receptor type (kappa-opioid) — this person's Explicit Self Model",
     "which acts on a single receptor type (kappa-opioid). This person's Explicit Self Model"),

    # ======== Chapter 7 (L755, L775, L789) ========
    # L755: cluster → comma
    ("written left-handed, which I never do while awake",
     "written left-handed, which I never do while awake"),  # May need different context
    # L775: sandwich → parens
    ("This distinction — propofol abolishes consciousness by going subcritical, ketamine alters consciousness by going supracritical with disrupted input — is a genuine explanatory advantage",
     "This distinction (propofol abolishes consciousness by going subcritical, ketamine alters consciousness by going supracritical with disrupted input) is a genuine explanatory advantage"),
    # L789: light → comma
    ("this chapter — and provides a reference you can come back to",
     "this chapter, and provides a reference you can come back to"),

    # ======== Chapter 8 (L809, L813, L837, L845, L847, L855, L873) ========
    # L809: technical → parens
    ("a fast route from retina to superior colliculus to pulvinar",
     "(a fast route from retina to superior colliculus to pulvinar)"),
    # Better match for L809
    ("subcortical pathways that bypass the damaged cortex — a fast route from retina to superior colliculus to pulvinar",
     "subcortical pathways that bypass the damaged cortex (a fast route from retina to superior colliculus to pulvinar)"),
    # L813: light → comma
    ("\"There's a blue vase on the table\" — when the table is empty",
     "\"There's a blue vase on the table,\" when the table is empty"),
    # L837: lazy break → period
    ("your heart is beating, your stomach is digesting, your lungs are breathing — they're absent or garbled",
     "your heart is beating, your stomach is digesting, your lungs are breathing. They're absent or garbled"),
    # L845: lazy break → period
    ("but against the patient's conscious will — one hand lights a cigarette",
     "but against the patient's conscious will. One hand lights a cigarette"),
    # L847: light → comma
    ("the \"alien\" hand exhibits disinhibited behavior — grabbing objects, using tools, touching things compulsively",
     "the \"alien\" hand exhibits disinhibited behavior, grabbing objects, using tools, touching things compulsively"),
    # L855: lazy break → period
    ("in the absence of external input — the simulation doesn't stop",
     "in the absence of external input. The simulation doesn't stop"),
    # L873: concessive → comma
    ("your EWM screams *threat* — even though your IWM has never recorded an actual spider injury",
     "your EWM screams *threat*, even though your IWM has never recorded an actual spider injury"),

    # ======== Chapter 9 (L905, L925, L933) ========
    # L905: sandwich → parens
    ("the question might not have a determinate answer — that our concept of \"a person\" simply breaks down",
     "the question might not have a determinate answer (that our concept of \"a person\" simply breaks down"),
    # L925: sandwich → parens
    ("The confabulation — the left-hemisphere interpreter — is the *same mechanism*",
     "The confabulation (the left-hemisphere interpreter) is the *same mechanism*"),
    # L933: lazy break → period
    ("it forks — it creates separate configurations",
     "it forks. It creates separate configurations"),

    # ======== Chapter 10 (L961x2, L973x2, L975, L981, L1003, L1021, L1023) ========
    # L961: sandwich → parens + period
    ("below Darwin's Arch — back when it was still intact — when a huge male orca",
     "below Darwin's Arch (back when it was still intact) when a huge male orca"),
    ("scanning us with sound — and then he",
     "scanning us with sound. And then he"),
    # L973: cluster → parens
    ("cognitive abilities — tool manufacture, mirror self-recognition, future planning, social deception",
     "cognitive abilities (tool manufacture, mirror self-recognition, future planning, social deception)"),
    ("the six-layer argument from Chapter 2 — that mammals evolved six cortical layers",
     "the six-layer argument from Chapter 2 (that mammals evolved six cortical layers"),
    # L975: sandwich → parens
    ("**Cephalopods** — octopuses and cuttlefish — extend the logic",
     "**Cephalopods** (octopuses and cuttlefish) extend the logic"),
    # L981: lazy break → period
    ("our brains are absolutely capable of it",
     "our brains are absolutely capable of it"),
    # Better L981 match
    ("clicking their tongues and reading the echoes — our brains are absolutely capable of it",
     "clicking their tongues and reading the echoes. Our brains are absolutely capable of it"),
    # L1003: humorous → comma
    ("and I believe this was the actual historical approach — you offer it to the neighbor",
     "and I believe this was the actual historical approach, you offer it to the neighbor"),
    # L1021: sandwich → parens
    ("Self-inflicted pain — bumping its own hand against a toy, biting its own foot — often produces curiosity",
     "Self-inflicted pain (bumping its own hand against a toy, biting its own foot) often produces curiosity"),
    # L1023: cluster → period
    ("the implicit self model's interaction with the social world — pain paired with distress",
     "the implicit self model's interaction with the social world. Pain paired with distress"),

    # ======== Chapter 11 (L1065, L1099, L1115, L1155) ========
    # L1065: sandwich → parens
    ("the dose-dependent activation of the visual processing hierarchy — from V1 at low doses through V4 and V5 to anterior IT at high doses — should map",
     "the dose-dependent activation of the visual processing hierarchy (from V1 at low doses through V4 and V5 to anterior IT at high doses) should map"),
    # L1099: sandwich → parens
    ("different anesthetic agents — propofol, ketamine, sevoflurane, xenon, nitrous oxide — should all converge",
     "different anesthetic agents (propofol, ketamine, sevoflurane, xenon, nitrous oxide) should all converge"),
    # L1115: lazy break → period
    ("there's already some evidence",
     "there's already some evidence"),
    # Better L1115 match
    ("not hemispheric specialization — there's already some evidence",
     "not hemispheric specialization. There's already some evidence"),
    # L1155: sandwich → parens
    ("Dissociative identity disorder — multiple distinct identities (\"alters\") in a single person — is controversial",
     "Dissociative identity disorder (multiple distinct identities, or \"alters,\" in a single person) is controversial"),
    # Alternate form
    ("Dissociative identity disorder — multiple distinct identities",
     "Dissociative identity disorder (multiple distinct identities"),

    # ======== Chapter 12 (28 cuts - many) ========
    # L1175: sandwich + gloss
    ("implement the four-model architecture — Implicit World Model, Implicit Self Model, Explicit World Model, Explicit Self Model — on a substrate",
     "implement the four-model architecture (Implicit World Model, Implicit Self Model, Explicit World Model, Explicit Self Model) on a substrate"),
    ("a dormant system — models stored but no simulation running",
     "a dormant system, models stored but no simulation running"),
    # L1179: double sandwich
    ("The nSAI dogma — \"no strong artificial intelligence\" — tells engineers",
     "The nSAI dogma (\"no strong artificial intelligence\") tells engineers"),
    ("The nSU dogma — \"no self-understanding\" — tells them",
     "The nSU dogma (\"no self-understanding\") tells them"),
    # L1189: sandwich
    ("the crucial difference — and this is why it matters for artificial consciousness — is what happens",
     "the crucial difference (and this is why it matters for artificial consciousness) is what happens"),
    # L1193: lazy break → period
    ("an LLM does nothing — it has no ongoing simulation",
     "an LLM does nothing. It has no ongoing simulation"),
    # L1203: heavy break → period
    ("that follows directly from the same engineering specification — if consciousness depends",
     "that follows directly from the same engineering specification. If consciousness depends"),
    # L1213: 6-dash cluster - 4 cuts
    ("At the proteomic level — the molecular machinery of synaptic weights, receptor configurations, enzyme cascades",
     "At the proteomic level (the molecular machinery of synaptic weights, receptor configurations, enzyme cascades)"),
    ("learning rates and receptor sensitivities — the information is in the molecular details",
     "learning rates and receptor sensitivities. The information is in the molecular details"),
    ("you need nanometer-scale scanning — electron microscopy or better — to capture",
     "you need nanometer-scale scanning (electron microscopy or better) to capture"),
    # L1215: sandwich → parens
    ("At the topological level — the network architecture, the connectivity patterns, which regions talk to which others and how strongly — you need",
     "At the topological level (the network architecture, the connectivity patterns, which regions talk to which others and how strongly) you need"),
    # L1217: sandwich → parens
    ("And at the virtual level — the simulation itself, the EWM and ESM in real-time operation — you need",
     "And at the virtual level (the simulation itself, the EWM and ESM in real-time operation), you need"),
    # L1225: sandwich → parens
    ("The dynamics problem — getting the digital substrate to run at criticality — is harder",
     "The dynamics problem (getting the digital substrate to run at criticality) is harder"),
    # L1249: lazy break → period
    ("The self-model stitches a narrative — and narratives always feel real from the inside",
     "The self-model stitches a narrative. And narratives always feel real from the inside"),
    # L1255: lazy break → period
    ("the original — the original is gone",
     "the original. The original is gone"),
    # Better L1255
    ("neither one actually being the original — the original is gone",
     "neither one actually being the original. The original is gone"),
    # L1265: light → comma
    ("and when it does — the implications are staggering",
     "and when it does, the implications are staggering"),
    # L1275: period + colon
    ("The copy problem exists because copying *interrupts* the process — it creates a break",
     "The copy problem exists because copying *interrupts* the process. It creates a break"),
    ("you could, in principle, avoid the problem entirely — by never copying, never breaking the thread",
     "you could, in principle, avoid the problem entirely: by never copying, never breaking the thread"),
    # L1283: lazy break → period
    ("Neurons die, proteins misfold, telomeres shorten, the whole system degrades — but if you could",
     "Neurons die, proteins misfold, telomeres shorten, the whole system degrades. But if you could"),
    # L1285: lazy break → period
    ("*interstellar travel* — not for our bodies",
     "*interstellar travel*. Not for our bodies"),
    # Alternate
    ("interstellar travel — not for our bodies",
     "interstellar travel. Not for our bodies"),
    # L1305: lazy break → period
    ("a transfer to a robot body with rich sensory input would fare better than one to a disembodied server — but in either case",
     "a transfer to a robot body with rich sensory input would fare better than one to a disembodied server. But in either case"),

    # ======== Chapter 13 (18 cuts) ========
    # L1325: period
    ("This doesn't mean consciousness is *simple* — it's extraordinarily complex",
     "This doesn't mean consciousness is *simple*. It's extraordinarily complex"),
    # L1339: two glosses → parens
    ("Your unconscious processing runs at roughly 40 Hz — about 25 milliseconds per cycle",
     "Your unconscious processing runs at roughly 40 Hz (about 25 milliseconds per cycle)"),
    ("Your conscious experience runs at roughly 20 Hz — about 50 milliseconds per cycle",
     "Your conscious experience runs at roughly 20 Hz (about 50 milliseconds per cycle)"),
    # L1343: lazy break → period
    ("a final override, a last line of defense for human agency",
     "a final override, a last line of defense for human agency"),
    # Better L1343
    ("at the last moment, about 50 milliseconds before execution — a final override",
     "at the last moment, about 50 milliseconds before execution. A final override"),
    # L1365: lazy break → period
    ("free will, paradoxically, makes your choices less random, not more",
     "free will, paradoxically, makes your choices less random, not more"),
    # Better L1365
    ("your output *less* random than the amnesiac's — free will, paradoxically",
     "your output *less* random than the amnesiac's. Free will, paradoxically"),
    # L1367: lazy break → period
    ("Your conscious self-model doesn't make decisions in real time — it's too slow for that",
     "Your conscious self-model doesn't make decisions in real time. It's too slow for that"),
    # L1385: cluster → comma
    ("I was lucky that mine never got that far — one of these \"voices\"",
     "I was lucky that mine never got that far, one of these \"voices\""),
    # L1397: cluster - 2 periods
    ("the universe is demonstrably Class 4-capable",
     "the universe is demonstrably Class 4-capable"),
    # Better L1397
    ("or at least the beginning of one — the universe is demonstrably Class 4-capable",
     "or at least the beginning of one. The universe is demonstrably Class 4-capable"),
    ("including the computation that produces consciousness — whether it does is a separate question",
     "including the computation that produces consciousness. Whether it does is a separate question"),
    # L1419: light → comma
    ("The IWM and ISM are \"models\" — but models of what, exactly",
     "The IWM and ISM are \"models,\" but models of what, exactly"),
    # L1437: lazy break → period
    ("elegance is not evidence",
     "elegance is not evidence"),
    # Better L1437
    ("has been legitimately criticized — Sabine Hossenfelder",
     "has been legitimately criticized. Sabine Hossenfelder"),
    # L1449: lazy break → period
    ("You can do this right now — the ISS tracking page",
     "You can do this right now. The ISS tracking page"),

    # ======== Chapter 14 (10 cuts) ========
    # L1485: lazy break → period
    ("Class 3 dynamics can't produce that",
     "Class 3 dynamics can't produce that"),
    # Better L1485
    ("from quantum fluctuations to galaxy clusters — Class 3 dynamics can't produce that",
     "from quantum fluctuations to galaxy clusters. Class 3 dynamics can't produce that"),
    # L1487: sandwich → parens
    ("genuinely random — truly random, not just complex-looking — then nothing stable",
     "genuinely random (truly random, not just complex-looking), then nothing stable"),
    # L1515: sandwich → parens
    ("The **Planck length** — about $10^{-35}$ meters, a number so small that calling it \"small\" is like calling the observable universe \"medium-sized\" — is where physics",
     "The **Planck length** (about $10^{-35}$ meters, a number so small that calling it \"small\" is like calling the observable universe \"medium-sized\") is where physics"),
    # L1531: gloss → parens
    ("point-like in the Standard Model — zero-dimensional, with no internal structure",
     "point-like in the Standard Model (zero-dimensional, with no internal structure)"),
    # L1551: light → comma
    ("Class 4 dynamics contain all classes as subprocesses — including Class 4 itself",
     "Class 4 dynamics contain all classes as subprocesses, including Class 4 itself"),
    # L1555: lazy break → period
    ("I'll follow that thread to its consequences — and they are stranger than I expected",
     "I'll follow that thread to its consequences. And they are stranger than I expected"),
    # L1563: filler removal
    ("and about an architecture that should look very familiar — by the time we reach the end",
     "and about an architecture that should look very familiar by the time we reach the end"),

    # ======== Chapter 15 (18 cuts) ========
    # L1597: light → comma
    ("comfortably far away — propagates *inward*",
     "comfortably far away, propagates *inward*"),
    # L1609: sandwich → parens
    ("Its structural logic — singularities as information transformers, boundaries as the fundamental architectural element — holds regardless",
     "Its structural logic (singularities as information transformers, boundaries as the fundamental architectural element) holds regardless"),
    # L1623: lazy break → period
    ("elementary particles *are* singularities of the same type as event horizons — that's new",
     "elementary particles *are* singularities of the same type as event horizons. That's new"),
    # L1633: lazy break → period
    ("A singularity boundary has finite area — at the Planck scale, that area is as small as area can be",
     "A singularity boundary has finite area. At the Planck scale, that area is as small as area can be"),
    # L1637: light → comma
    ("Particles, in this picture, are the gliders and spaceships of the Planck-scale automaton — the persistent structures that the rule set permits",
     "Particles, in this picture, are the gliders and spaceships of the Planck-scale automaton, the persistent structures that the rule set permits"),
    # L1645: lazy break → period
    ("They're not arbitrary rules imposed from outside — they're bookkeeping constraints",
     "They're not arbitrary rules imposed from outside. They're bookkeeping constraints"),
    # L1709: sandwich → parens
    ("If we are Class 4 automatons — if our brains operate at the edge of chaos, in the same computational class I've just assigned to the universe",
     "If we are Class 4 automatons (if our brains operate at the edge of chaos, in the same computational class I've just assigned to the universe)"),
    # L1749: light → comma
    ("it produces *other Class 4 automata* within its own dynamics — smaller, slower, resource-constrained, but genuinely universal",
     "it produces *other Class 4 automata* within its own dynamics, smaller, slower, resource-constrained, but genuinely universal"),

    # ======== Chapter 16 (18 cuts) ========
    # L1779: sandwich → parens
    ("Everything inside the singularity boundaries — atoms, planets, galaxies, you — is the decompressed side",
     "Everything inside the singularity boundaries (atoms, planets, galaxies, you) is the decompressed side"),
    # L1791: dashes → periods (recap paragraph)
    ("the edge of chaos. Chapter 14 established this by elimination: Classes 1 and 2 are too simple, Class 3 can't compute, Class 5 makes physics impossible — what's left is Class 4",
     "the edge of chaos. Chapter 14 established this by elimination: Classes 1 and 2 are too simple, Class 3 can't compute, Class 5 makes physics impossible. What's left is Class 4"),
    # L1793: technical → parens
    ("Too little activity and you're in deep sleep — Class 2, periodic, unconscious",
     "Too little activity and you're in deep sleep (Class 2, periodic, unconscious)"),
    # L1819: sandwich → parens
    ("Rolf Landauer — an IBM physicist thinking about the fundamental limits of computation — proved",
     "Rolf Landauer (an IBM physicist thinking about the fundamental limits of computation) proved"),
    # L1821: lazy break → period
    ("proportional to its surface area, not its volume — this is one of the most counterintuitive results in physics",
     "proportional to its surface area, not its volume. This is one of the most counterintuitive results in physics"),
    # L1827: dash → colon
    ("Your implicit models hold compressed, maximum-density information — everything you've ever learned",
     "Your implicit models hold compressed, maximum-density information: everything you've ever learned"),
    # L1837: sandwich → parens
    ("If whatever exists had no dynamics — no change, no evolution, no computation — it would be",
     "If whatever exists had no dynamics (no change, no evolution, no computation), it would be"),
    # L1841: lazy break → period
    ("Nothing can carry infinite information in finite space — the Bekenstein bound is a theorem, not a conjecture",
     "Nothing can carry infinite information in finite space. The Bekenstein bound is a theorem, not a conjecture"),
    # L1867: sandwich → parens
    ("all singularities — Planck-scale, black hole, cosmological — are structurally identical",
     "all singularities (Planck-scale, black hole, cosmological) are structurally identical"),
    # L1901: light → comma
    ("the precise boundary of its explanatory reach and give you the structural reason that boundary exists — is doing more than most theories manage",
     "the precise boundary of its explanatory reach and give you the structural reason that boundary exists, is doing more than most theories manage"),

    # ======== Coda (4 cuts) ========
    # L1933: lazy break → period
    ("I have almost nothing in common with my one-year-old self — completely different synaptic connections",
     "I have almost nothing in common with my one-year-old self. Completely different synaptic connections"),
    # L1951: sandwich → parens + period
    ("And if the cosmology chapters are right — if the universe really is a self-similar, quasi-infinite Class 4 system — then there's",
     "And if the cosmology chapters are right (if the universe really is a self-similar, quasi-infinite Class 4 system), then there's"),
    ("except it doesn't require quantum mechanics — just a big enough universe",
     "except it doesn't require quantum mechanics. Just a big enough universe"),
    # L1963: dash → comma
    ("the theory, arguments, and all intellectual content are entirely mine — developed over two decades",
     "the theory, arguments, and all intellectual content are entirely mine, developed over two decades"),

    # ======== Appendix B (8 cuts) ========
    # L2076: sandwich → parens
    ("David Wechsler — whose intelligence scales are the most widely administered in the world — explicitly called",
     "David Wechsler (whose intelligence scales are the most widely administered in the world) explicitly called"),
    # L2084: dash → colon
    ("*Factual knowledge* is knowledge of content — facts, concepts, procedures, cultural repertoire",
     "*Factual knowledge* is knowledge of content: facts, concepts, procedures, cultural repertoire"),
    # L2086: dash → colon
    ("**Performance** is the processing capacity of the cognitive system — working memory, processing speed",
     "**Performance** is the processing capacity of the cognitive system: working memory, processing speed"),
    # L2088: two dashes → colons
    ("*Thirst for knowledge* is the intrinsic drive to understand — curiosity, the need to make sense of things",
     "*Thirst for knowledge* is the intrinsic drive to understand: curiosity, the need to make sense of things"),
    ("*Urge to act* is the drive to apply knowledge — to experiment, to engage",
     "*Urge to act* is the drive to apply knowledge: to experiment, to engage"),
    # L2110: sandwich → parens
    ("A student who learns spaced repetition — distributing practice over time rather than cramming — doesn't merely acquire",
     "A student who learns spaced repetition (distributing practice over time rather than cramming) doesn't merely acquire"),

    # ======== Appendix C (10 cuts) ========
    # L2207: lazy break → period
    ("A heartbeat (approximately) — information is stored",
     "A heartbeat (approximately). Information is stored"),
    # L2213: lazy break → period
    ("genuinely random, not pseudorandom, not deterministic, not compressible — no pattern, no self-similarity",
     "genuinely random, not pseudorandom, not deterministic, not compressible. No pattern, no self-similarity"),
    # L2267: repetitive → comma
    ("within mathematics — within the domain of formal symbolic systems",
     "within mathematics, within the domain of formal symbolic systems"),
    # L2277: sandwich → parens
    ("Class 4 — the regime of consciousness, of universal computation, of the cortical automaton — sits at the *maximum complexity*",
     "Class 4 (the regime of consciousness, of universal computation, of the cortical automaton) sits at the *maximum complexity*"),
    # L2314: lazy break → period
    ("it is the only class that contains all classes, including itself — this self-containment is what makes",
     "it is the only class that contains all classes, including itself. This self-containment is what makes"),
]

def main():
    with open(MANUSCRIPT, 'r') as f:
        text = f.read()

    original_dashes = text.count('—')
    applied = 0
    skipped = 0
    not_found = 0

    for old, new in CUTS:
        if old == new:
            skipped += 1
            continue
        if old in text:
            # Count dashes removed
            old_dashes = old.count('—')
            new_dashes = new.count('—')
            removed = old_dashes - new_dashes

            text = text.replace(old, new, 1)  # Only replace first occurrence
            applied += 1
            if removed > 0:
                print(f"  APPLIED (-{removed} dash): ...{old[:70]}...")
        else:
            not_found += 1

    final_dashes = text.count('—')

    print(f"\n=== SUMMARY ===")
    print(f"Cuts defined: {len(CUTS)}")
    print(f"Applied: {applied}")
    print(f"Already done / not found: {not_found}")
    print(f"Skipped (identical): {skipped}")
    print(f"Em-dashes before: {original_dashes}")
    print(f"Em-dashes after: {final_dashes}")
    print(f"Reduction: {original_dashes - final_dashes}")

    with open(MANUSCRIPT, 'w') as f:
        f.write(text)

    print(f"\nManuscript updated: {MANUSCRIPT}")

if __name__ == '__main__':
    main()
