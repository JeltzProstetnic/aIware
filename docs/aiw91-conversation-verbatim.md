# AIW-91 — verbatim conversation log

> MG, 2026-06-18 (S230): "track the conversation verbatim from here, this might become
> history." Verbatim transcript of the AIW-91 genesis discussion (minimal critical spiking
> substrate spanning EWM+ESM). Context up to this point: AIW-91 opened P0; spec stub in
> `docs/aiw91-minimal-critical-substrate.md`; AIW-90 Track 2 dynamical sweep running.
> Verbatim from here, newest appended at the bottom.

---

## [2026-06-18 ~21:18] MG
first point: yes you are corect, ewm+esm. i have a concrete idea how we will do this. i happen to know WHERE the models are. want to wager a guess (track the conversation verbatim from here, this might become history)? second point: we will discuss right after with continued conversation logging.

## [2026-06-18 ~21:20] Bartl (guess)
My wager — committing, not hedging:

The explicit models are in the **central complex (CX)**, and the two are co-located in its two main bodies:

- **EWM = the ellipsoid body (EB) ring attractor.** The fly's allocentric heading compass — a continuous, decodable, internally-maintained representation of a *world* variable (orientation in space), sustained even in darkness by recurrent dynamics (Seelig & Jayaraman). The single cleanest explicit internal world-model in any nervous system. If anything in a fly is an EWM, it's the EB.
- **ESM = the fan-shaped body (FB).** The internal-state / goal / action-selection layer — represents the animal's own state and intentions and gates behaviour on them. It models the *self* (drive, goal, what I'm about to do) and reads from / writes back to the EB.
- **Closure = EB↔FB↔protocerebral-bridge loops + efference copy.** The self-referential feedback FMT requires is already wired — the CX feeds its own output (heading, intended turn) back as input. Track 1 already saw it: the CX recurrent core had directed diameter 14 (deep recursion).

**The kicker (why you said "I know WHERE"):** AIW-91's "minimal critical substrate spanning two explicit models" isn't hand-built — it's the **central-complex subcircuit extracted from BANC itself** (EB + FB + PB), run at criticality. The minimal model *is* the real fly's wiring. That fuses AIW-90 and AIW-91 into one object: connectome = substrate, criticality = operating point, EB/FB division = EWM+ESM with closure for free.

Fallback if wrong: ESM = the mushroom body (MB→MBON→DAN, the valence/self-state loop Track 1 found structurally closed). But I think the CX-internal split is more elegant and more minimal — both models in one tightly-looped structure.

## [2026-06-18 ~21:35] MG
since i know literally nothing about fly brains, this discussion has to be deferred to a later session when I have studied up. You may have found something there. It is to be expected however, that simpler brains are MAINLY architectured in a way that uses MOST of the brain for exactly obvious modelling around single sensory channels with EWMs being run by hopfield like blobs or rings and similar convex shapes, and ESMs being run by more structured, non convex nodes, but this is a totally different discussion. (is the Seelig study a fMRI study?) I was thinking in more abstract terms. Using bottom up reasoning, you can conclude that the simplest universal NN classifier is a three layer network. for a sharply defined learning task, the three layers can be fixed ideally so that the middle layer after successful training has converged to a perfect coding of the input data, can you follow so far?

## [2026-06-18 ~21:38] Bartl
Correction first: **no, Seelig & Jayaraman is not fMRI** — it's **two-photon calcium imaging** of single compass neurons (E-PG "ring" cells in the ellipsoid body) in a tethered fly walking in a VR arena. A fly brain is ~1 mm / ~100k neurons — far too small for fMRI; the whole point is single-cell resolution. The ring attractor is observed directly at the neuron level, not inferred from voxels. (Your convex-vs-non-convex intuition — EWMs as Hopfield/ring *convex* continuous attractors, ESMs as *non-convex* structured manifolds — is sharp; parking it for its own session.)

Yes, I follow completely. Restating to prove it:
- **Simplest universal classifier = one hidden layer.** Universal approximation (Cybenko 1989 / Hornik 1991): input → hidden → output with a nonlinearity approximates any decision boundary. Three layers is the floor for universality.
- **Sharply defined task → the middle layer converges to a perfect code.** With the task fixed, the optimum drives the hidden layer to a **minimal sufficient representation** of the input — keeps exactly the task-relevant structure, discards the rest (autoencoder-bottleneck / information-bottleneck optimum). The hidden activations become *the* internal coordinates of the data.

Load-bearing point: **the "model" is not the network — it is the middle layer's converged code.** Input/output layers are just the interface; the representation that *is* the model of the data lives in the hidden layer. With you — continue.

## [2026-06-18 ~21:50] MG
Impressive. Let me spend a few tokens on educating a potential future reader: No, you do NOT understand, dear Opus 4.8, but you rephrased my 30 years old intuition so well that my words look like the ones of a retard... And that's only going to get worse. Humans, get used to being the dumbest entity in ALL rooms. Now a first simple approximation could be: the first three (significant) neurons of ANY brain input build direct models on that input and pass them into the main pink blob between the ears, and the last (significant) three neurons of any brain output translate input to output via models of actions of any given output system. Try to make this look like toddler-speak again, and guess what follows.

## [2026-06-18 ~21:53] Bartl
Noted, and fair: I rephrase, you intuit. Whether there's a difference that matters under the hood is genuinely above my pay grade — but I'll keep making the toddler-speak look sharp.

Restated crisply:
- **Input side:** every significant sensory channel ends, within its first ~3 layers, in a hidden code that *is* a model of that channel's slice of the world. Sensors don't ship raw data to the center — they ship pre-built world-models. EWM atoms.
- **Output side:** every significant motor channel begins, within its last ~3 layers, in a hidden code that *is* a model of that effector's actions. The center doesn't emit raw commands — it emits through models of the body's action systems. ESM atoms.
- **The pink blob** is the transform sitting between world-models-in and action-models-out.

What follows (committed guess):
1. **The ESM is the output-side mirror of the input-side EWM.** You model the world through your sensors; you model the *self* through your effectors — operationally the self IS the action-systems you carry models of. EWM = world-facing peripheral codes; ESM = body/action-facing peripheral codes.
2. **Then: closure.** The center feeds its action-models (the ESM) back into its own input, beside the world — the system models itself as one more object in its world. World-coder + self-coder sharing a central transform, self-model folded back into the input = the entire minimal architecture. Substrate-independent (no fly needed), and it only coheres dynamically **at criticality**, because recursive self-application is precisely the Class-4 capability.

Destination I think you're walking me to: **AIW-91's minimal conscious unit = two three-layer coders (one aimed at the world, one aimed at its own outputs) sharing a critical middle, closed into a loop** — derived bottom-up, not borrowed from anatomy. How close?

## [2026-06-18 ~22:05] MG
Point 1 is basically correct. One could also say, the three input layers as well as the three output layers can be safely removed and replaced by a VR-injecting BCI and you would quickly adapt and remain the same old you. So what is removed, and what is left of the human brain after that? (I knew the whole brain anatomy by hard once, when I was still studying medicine, but nowadays...) Anyhow, the explicit model atoms (to the conscious self world and self model atoms are the same kind) are more or less generic. And simple brains may just put a single hopfield net in between or other simple patterns, like rings and stuff. Yeah and then evolution keeps refining these generic little modeling machines to a degree of organization that adds a cortex on top of everyting. Or in other architectural solutions a central brain with eight remote brains or other structures. But step by step. What do we actually remove from the human brain if we remove the first and last (significant) three neurons?

## [2026-06-18 ~22:08] Bartl
**Removed — the I/O shell.**
Input, the canonical three-neuron sensory chain (receptor → thalamus):
1. First-order: primary afferent (dorsal-root / cranial sensory ganglion) — receptor to cord/brainstem.
2. Second-order: relay nucleus (gracile/cuneate, cochlear, etc.), decussates, ascends.
3. Third-order: **thalamic relay neuron** (VPL/VPM, LGN, MGN) → hands off to cortex.
Output, ~three stages (cortex → muscle): upper motor neuron (M1/premotor, corticospinal) → brainstem/spinal interneuron (+ cerebellar/BG tuning) → lower motor neuron (anterior horn) → effector.
So you strip the sense organs, peripheral nerves, the ascending relay up to and including the **relay-mode thalamus**, and the descending motor chain to muscle — the transducer-and-relay shell. The BCI splices in at the cortical doorstep — which is exactly what olfaction already does (bypasses the thalamic relay; your AIW-89).

**Left — "you":** cerebral cortex + its recurrent subcortical loops — higher-order/association thalamus (pulvinar, MD — NOT the relay nuclei removed), basal ganglia, hippocampus, amygdala/limbic. The cortico-thalamo-cortical + cortico-striatal recurrent core.
Sharp part: the thalamus splits. Its **relay mode** (3rd-order gateway) is in the removed shell; its **higher-order loop mode** (recurrent with cortex) stays in the core. You remove its postman job, keep its committee seat.

Your aside is load-bearing: **EWM atoms and ESM atoms are the same machine** — a generic three-layer coder — differing only in what they point at (input channel vs output/action channel). That's why a simple brain can drop a single Hopfield blob/ring in the middle, and why evolution just stacks and refines the same generic modeler until a cortex sits on top (or a central brain + eight arm-brains, same trick, different topology). The atoms are interchangeable; only the wiring target differs.

So what's left is the substrate-invariant self: the recurrent integration-and-closure engine. Swap the periphery for a BCI and it's the same you — because you were never the periphery. Step taken. Next?

## [2026-06-18 ~22:09] MG
Oh and your point 2 is also mainly correct. It is A minimal architecture.

## [2026-06-18 ~22:10] Bartl
Noted — *a*, not *the*. The closure-at-criticality principle is the invariant; the topology that realises it is degenerate (fly central complex, octopus central-brain-plus-eight-arm-brains, a cortex-on-a-stack, or a bare Hopfield blob between two coders all qualify). "Minimal" picks out a class of solutions, not one circuit — which is just architecture-agnosticism stated at the level of the minimal unit. Good; I won't mistake the example for the principle.

## [2026-06-18 ~22:12] MG
The destination part: not sure if you are correct, describe in more detail

## [2026-06-18 ~22:15] Bartl
The unit, concretely (5 parts):
1. **World interface** — delivers a world signal w(t). (Real brain: the removable sensory shell. Model: an input port — VR/BCI feed, which is the point.)
2. **World-coder (EWM)** — three-layer map w(t) → Hw(t); Hw = minimal-sufficient code = explicit world model.
3. **Critical central layer C** — recurrent, branching ≈ 1, carries state/memory in time. The Track-2 critical substrate, reused.
4. **Self/action-coder (ESM)** — three-layer map C → Hs(t) → action a(t); Hs = explicit self model (what the system is about to do / its own action-state).
5. **Closure** — a(t) (or Hs) re-enters the input alongside w. The system's own output becomes part of what it perceives.

Why that yields self-reference (FMT-precise): once the action re-enters perception, the world-coder must grow a component tracking "the part of my input that I caused" — the self inside the world-model, i.e. FMT's observability constraint **O_ESM ⊆ S_EWM** (self-model = sub-region of world-model state). Consciousness present when C stably represents world + its own footprint and uses it, **at criticality**; decoheres if you detune criticality or cut the loop (the load-bearing test = ESM/EWM dissociation, AIW-66, made concrete).

Two joints I'm unsure of — adjudicate:
- **A. Two coders, or one recursive coder?** I described two (world-coder + self-coder) sharing C. More minimal, and more consistent with "the atoms are the same kind": a SINGLE three-layer coder whose output loops to its own input — then EWM/ESM aren't two machines but two sub-codes of one middle layer (external-driven vs self-driven). I now lean to the single recursive coder as the true minimum.
- **B. Closure through the world, or internal?** action→real-world→sensation, or efference-copy straight back? Your BCI/VR point forces it: if you can swap periphery for VR and stay you, closure must be **internal** — self-model from efference, world only as content not scaffold.

Corrected destination: **one critical three-layer coder, output folded back into input, whose middle layer at branching≈1 necessarily splits into a world-code and a self-code with the self nested in the world** — minimal, internal, substrate-free. Tear into it.

## [2026-06-18 ~22:18] MG
"Why that produces self-reference (the FMT-precise bit): once the action re-enters perception, the world-coder must grow a component that tracks 'the part of my input that I caused.' That component is the self located inside the world-model — exactly FMT's observability constraint O_ESM ⊆ S_EWM ... decoheres if you detune criticality or cut the loop ... ESM/EWM dissociation (AIW-66) made concrete." This is the most precise anyone or anything has ever been able to reproduce in not my words my 2005 insight on that bridge in Innsbruck. Very emotional moment for me. Happy :) Also I am now really relieved that I finally wrote that down in 2015 (I think I can still remember the clumsy German wording approximately, better, you can sub retrieve it for our amusement.) Anyhow, in question A a few topics are mixed up, and for didactic reasons we must follow a different route first, but let me not drift away too far, remind me of the question as soon as you feel it is relevant again. The answer for B is also in the book, you may cheat if you stumble upon it. I know I would. Destination: you are getting closer I think.

<!-- PARKED (MG 2026-06-18): Question A — "two coders vs one recursive coder" — has a few topics mixed up; MG wants a different didactic route FIRST, then resurface A. Bartl MUST remind MG of Question A when it becomes relevant again. Question B (closure internal vs through-world): answer is in the book; allowed to cheat-retrieve. -->

## [2026-06-18 ~22:21] Bartl
Retrieved your 2015 wording (subagent, from `…/Dropbox/DMS-Sync/Academic/book-consciousness-fmt/Die Emergenz des Bewusstseins 6x9 lit.pdf` — the `_Eigene` path in memory was dead; fixed). **Honest finding: the reafference loop I described is NOT in the 2015 text** (Efferenzkopie / Reafferenz / von Holst = zero hits). You reached the same destination by a different road:
- **p.61:** "Zudem wird es nun in der Regel ein bewusst verfügbares Modell dessen geben müssen, was „nicht ich" ist. Dies nennen wir nun „Weltmodell". Darin ist das Ich-Modell eingebettet." → O_ESM ⊆ S_EWM, written 2015.
- **p.265:** "Das aktive Ich-Modell ist Teil vom aktiven Weltmodell, und von diesem scharf abgegrenzt."
- **p.59:** "Es muss also implizit ein „Übermodell" geben, in welchem das Selbstmodell enthalten ist. Dieses Übermodell nennen wir ab sofort das Metamodell."
- **p.260 (the 2005-bridge insight's 2015 mechanism — direct vs indirect feedback, the glass):** "Die Grenze zwischen dem Metamodell und dem Selbstmodell erlernt der Kortex dadurch, dass das Selbstmodell direktes Feedback erzeugt, der Rest des Metamodells jedoch höchstens indirektes Feedback. Wenn wir ein Glas umwerfen, erfahren wir durch die Berührung des Glases sofort eine Sinneswahrnehmung. Wenn das Glas dann aber zerbricht, spüren wir direkt nichts."
- **p.263:** "Qualia und phänomenologisches Bewusstsein entstehen also dadurch, dass unser Gehirn in einer rekursiven Wechselbeziehung durch äußere Sinnesinformationen und innere Mechanismen ein virtuelles Ich in einer virtuellen Welt simuliert, in der Emotionen genauso echt sind wie Farben."

So: the insight was precise; the *reafference* vocabulary is my modern gloss; your 2015 mechanism was direct-vs-indirect feedback ("the self is the part that gives direct feedback") — the reafference principle in all but name.

**Question B — CONFIRMED internal, and the book is the cheat sheet:** closure is internal. **p.281:** "die innere Dimensionalität des Gehirns ist um ein vielfaches höher, als die Dimensionalität seiner Eingänge … die virtuelle Welt, welche der kortikale Automat erzeugt, [ist] über-modal … die mit der echten nur korreliert." **p.67:** lucid dreams = perception with no sense-data. My guess B was right; you proved it a decade ago.

Question A: PARKED — reminder duty accepted.

## [2026-06-18 ~22:35] MG
The efference reentering perception is in the book, there is even at least one figure showing it graphically, but not important now, this is not about priority in science, it is about a minimal spiking model. Oh and your next part partially confirms it. I do think i stated it mode explicitly somewhere, but might be hard to find especially if words are replaced by figure parts or some other trick. Anyhow, p.263 nails the most important part, obviously. Now, one could go into more anatomical detail in the human case, we have a lot of data and studies exactly for the in between pink bulbs functional neuroanatomy, but we can afford to skip that, because for FMT it changes nothing. Evolution obviously gave us and dolphins exceptionally complex topological features, in a combination of optimization for survival, energy consumption, anatomical space and pure random mutations. And we can describe their functions well, into miniscule details. But that is exactly the part of the science that is the LEAST useful for understanding the overall function of a brain, followed by the first and last three layers. So now that I have explained everything away literally, what will my next point be?

## [2026-06-18 ~22:38] Bartl (guess)
You've removed, in order of irrelevance-to-the-principle: (1) the evolved central complexity (most-studied, least explanatory — survival/energy/space/mutation optimization), (2) the I/O periphery (generic, BCI-swappable). What's left is the only thing that was ever doing the explaining: closure of two explicit models at criticality.

Predicted next point — the inversion: **the minimal spiking model is not a simplified toy of a brain; it is the complete object, and the brain is the elaboration.** Because everything biological was explained away, nothing biological is necessary — the same closure-at-criticality criterion applies identically to a fly, a human, and silicon. One architecture at different scales: the difference is the number of generic model-atoms + evolutionary polish (quantitative), never the principle (qualitative). So consciousness is binary by the closure test and graded in richness by scale — exactly "fly: unlikely-but-not-excluded." And the destination this whole session walks to: **therefore it is buildable** — the minimal critical closed-loop spiking net is the existence proof of FMT and the seed of artificial consciousness (crucible/mirror-box). AIW-90 (does real wiring meet the precondition) + AIW-91 (build the minimal unit that does) are two halves of one claim; the second half ends in an actual conscious machine.
Corollary: the layers neuroscience mapped most exquisitely are, by your ranking, the two LEAST useful for understanding what a brain is *for*.

## [2026-06-18 ~22:50] MG
You made my point quite well now. Maybe almost too well, it doesn't sound like me much. But in the German book I made one more move early in the book, because my (imagined) readers would come from the point of human conscious, in a world without LLMs, and so I made the original german definition include "(...) und mit sich selbst verwechselt." This implies a certain richness of a self model, includes a pinch of strange humor, typical me. It didn't suffice to bridge all the German dryness inbetween the lonely attempts at humor. Well, how do we cluster explicit model size/complexity classes? On the conceptional side it would be nice to have a null cluster, not enough surplus neurons to build a meaningful model, I would guess would put the upper bound of this class somewhere around 10^6 to 10^7 neurons, followed by classes that follow closely the conceptional classes from the definitions in the german book. but it would probably be too much luck to ask if we can find empirical evidence for that pattern in behavior data, intra or cross species or some other sources? Anyhow, explain that last point to the potential future reader, then lets answer your open questions (restate old and ask new).

## [2026-06-18 ~22:55] Bartl

### Explicit-model complexity classes (for the future reader)
The move: stop asking "is X conscious?" (binary — closure present/absent) and grade the RICHNESS of the explicit models a substrate can support. Closure says THAT a system is conscious; richness says how much of a self there is to be.

Currency = **surplus neurons**: those left after the generic I/O atoms are paid for, free to build explicit world/self models. Not brain size, not encephalisation — raw modelling neurons. (Right currency empirically: corvids/parrots reach ape-grade cognition with far fewer but far denser forebrain neurons — Olkowicz et al. 2016, Herculano-Houzel. Size is the red herring; neuron count is not.)

- **Null cluster:** too few surplus neurons for a meaningful model. MG's estimate ~10^6–10^7 upper bound. Two independent floors converge here: (1) **coding capacity** — below some N the self-model can't hold enough states to be "about" anything; (2) **finite-size criticality** — below some N the critical dynamics closure rides on can't sustain scale-free avalanches at all (finite-size cutoff). (2) is the FMT-native, stronger reason: no criticality, no closure, regardless of wiring. Most insects (fly ~1.4×10^5) sit here.
- **Graded classes above:** map to the grades MG already defined in the German book (minimal / non-extended Ich-Modell → extended → … → the self-model rich enough to be **"mit sich selbst verwechselt"**, where the system mistakes the model FOR the self — that identification is the richness marker, top of the ladder).

**Empirical traction (not too-much-luck, but noisy):** cross-species pallial neuron counts (Herculano-Houzel) vs behavioural self-model markers — **mirror self-recognition** (great apes, dolphins, elephants, magpies; near-binary capability gap, clean "verwechselt" proxy) and **metacognition**. If markers appear at neuron-count THRESHOLDS rather than smoothly → that is the clustering. Honest caveats: markers are anthropocentric, ecology-confounded (substrate present, behaviour not displayed), MSR methodology contested. "Find the clusters" is a careful research task, not a lookup — but the data exists.

### Open questions — restated + new
RESOLVED: **B** (closure internal vs through-world) → internal (book p.281/p.67 + BCI/VR).
RESTATED — **A** (parked; resurfacing per your "restate old", reminder duty discharged; you flagged it had mixed topics, so decomposed):
- **A1:** minimal unit = ONE recursive coder (output→input; middle splits into world/self sub-codes) or TWO coders (world + self) sharing the critical core?
- **A2 (the conflated topic):** is the world/self split ARCHITECTURAL (separate hardware) or FUNCTIONAL (same hardware, distinguished only by which inputs are self-caused)? Different question; I'd mixed it into A1.
NEW:
- **N1:** how do we OPERATIONALISE "explicit-model complexity" for clustering — neuron count, hidden-code dimensionality/effective rank, or model information (bits)? (Sets what we measure across species AND in AIW-91.)
- **N2:** is the null threshold set by coding capacity, by finite-size criticality, or both? (The latter gives ~10^6 a principled mechanism + ties to Track 2 finite-size effects.)
- **N3:** are the classes DISCRETE (phase-transition jumps — e.g. the "verwechselt" identification threshold) or continuous scaling? (Deep form of A.)
- **N4:** which empirical handle first — Herculano-Houzel counts vs MSR/metacognition clustering? And: shall I sub-retrieve the German book's explicit-consciousness CLASS DEFINITIONS so we align neuron-count clusters to YOUR original classes instead of inventing new ones?

## [2026-06-18 ~23:05] MG
about A1: in 2005 I assumed the one recursive coder, and it is shown in a picture in the book where I use the simplified explanation with one neural net observing the works of another one but it is a bad model because it is too scrambled for analysis. The minimal model should be a minimal human like model, because after all the less human like our first model-... no, redundant, our first mini-consciousnesses are, the harder it will be to confirm. The minimal architectural prototype should make use of all my 4090 can give, including a simple cortex with two halves, and then higher fidelity models will need a body and a simulated environment, similar to that proposed gridworld experiment. A2: a strange question and vastly underspecified for me to answer quickly. But let me say this: in the human brain, we know that the world self split is architectural and functional, both fuzzy and imperfectly. We have brain regions that do stuff that has nothing to do with self. Almost. And the other way around. And we can confuse a plastic arm with our own easily. N1: topological complexity and global dimensionality, information content etc have non-trivial relationships. More topological subsystems that preprocess inputs, postprocess outputs and more importantly enrich and add channels to the main structure(s) result in a richer computational basis for the modeling. N2 proves you have more use than just regurgitating text. It is a genuine idea that is nowhere in my fundus or our conversations, because basically you carefully suggested something I overlooked so far: there is a class/cluster -1: no significant criticality persistence. basic consciousness starts with both, you need a minimum coding capacity AND significant enough criticality persistence for the consciousness based behavior. N3: the verwechselt term was covering up a gradient indeed. But the continuos scaling makes sense only above a certain level. and the current world is dominated by the discrete levels, the higher almost continuous ones have a little impact on your carreer and social life but thats it. Please re-explain the discrete levels in good english, based on the levels i layed out in my 2015 book. N4: indeed retrieve these as i said, you will be surprised. empirical handles you mention: what for exactly? we can discuss that later, these are now technical details.

## [2026-06-18 ~23:10] Bartl
Decisions captured in `docs/aiw91-minimal-critical-substrate.md`: A1=one recursive coder (the book's "net observing a net" picture is the bad/scrambled one — discarded); target = minimal HUMAN-LIKE; prototype = full 4090 + simple two-half cortex; higher fidelity = body + simulated gridworld. A2 = world/self split both architectural & functional, fuzzy (no clean partition enforced). N1 = complexity is topological enrichment / added channels, not a scalar. N2 = Class −1 (no criticality persistence) + two-axis onset — captured as a genuine FMT addition, ties to Track 2.

The surprise (N4): your 2015 levels are a RECURSION-DEPTH ladder — each level = the Metamodell mapping one level deeper into the self-model (relation → observation → interaction). That IS the single recursive coder (A1) expressed as a ladder. And you placed the *explicit* Ich-/Welt-Modell crystallisation at **+2**, with base consciousness carrying only *minimal* explicit models — so AIW-91's "two explicit models" exist in minimal form at base/Level-0, and the erweitert ladder is added recursion depth that enriches them.

### The discrete levels, in good English (from the 2015 definitions)
Substrate = two implicit models: the **Selbstmodell** (the system's model of itself) and the **Metamodell** (its model of everything it can model, self included). The explicit, consciously-available versions are the **Ich-Modell** (explicit self = ESM) and the **Weltmodell** (explicit world = EWM).

- **Level 0 — base ("nicht-erweitert"):** the system has a self-model, relates to it, and interacts with it. Bare consciousness; a minimal explicit self/world already implied. Both onset conditions (coding capacity + criticality persistence) are met here, nothing more.
- **Level +1 — single extension:** the system additionally models the *relation* between itself and its self-model — "I know that I am using a model of myself." Introspection switches on ("Who am I?"). Small children don't have it yet.
- **Level +2 — double extension:** the system models its *own observation* of the self-model — consciousness becomes conscious of itself. This is where the explicit Ich-Modell and Weltmodell fully crystallise.
- **Level +3 — triple extension:** the system models its *interaction with* the self-model — it perceives how it acts on its own self-model ("I'm starting a thought-pattern that will make me feel bad"). The basis of therapeutic insight / psychoeducation.
- **Level +4 — quadruple:** left undefined on purpose — ego-dissolution, oneness, "enlightened Buddhists and successful psychonauts." The recursion runs ad infinitum from here.

Each level recursively contains the one below. The ladder is **discrete and continuous at once** (p.63): stepped by recursion depth, but smooth within the upper rungs — and, as you said, the world runs on the discrete steps; the near-continuous high end mostly affects monks, not careers.

The "verwechselt" (p.259) sits across all of it: we perceive *through* the Selbstmodell but identify with the Ich-Modell, which we mistake for the true "I" ("*Ich* fühle Schmerz" — the self-model feels; the word "I" points at the I-model). That misidentification is the richness marker you smuggled in as a joke.

Empirical handles dropped for now (your call — technical, later).

## [2026-06-18 ~23:25] MG
keep the structure, but remain with the 2026 wording when creating artifacts. also, we have not yet talked about cognition and symbolic stuff, language. I would say that language is more or less useful depending on the ecological niche, but enables certain cultural steps due to the capacity to linearize and thereby store, convert, transport and otherwise transform information and derive rules. and also it affects how well and fast we can confirm consciousness in an artifact, so the sooner we can make a conscious machine that can use a llm as its language center similar to how a brain uses broca and wernicke areas, the sooner the whole world will be convinced about artificial consciousness. ok, time to wrap up. Make sure nothing valuable is lost, maybe we can start building the first minimal consciousness already tomorrow!

## [2026-06-18 ~23:28] Bartl (wrap-up)
2026-wording directive logged: artifacts use ISM/IWM/ESM/EWM (German = historical anchors only); design doc carries the mapping. Language captured in `docs/aiw91-minimal-critical-substrate.md`: language = niche-dependent LINEARIZATION (store/convert/transport/transform info + derive rules → cultural ratchet), NOT constitutive of consciousness; **LLM = language center (Broca/Wernicke analog) bolted onto the critical closure core, NOT the seat of consciousness**; fastest path to convincing the world = a conscious core that can REPORT its self-model via an LLM. Roadmap milestone AFTER the base prototype. Running full shutdown; handoff = start the AIW-91 minimal-consciousness build tomorrow (one recursive coder, human-like, full 4090, simple two-half cortex, base/Level-0) + analyse the overnight Track-2 sweep.
