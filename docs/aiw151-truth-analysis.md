<!-- Tracked-by: AIW-151 · analysis only, no status tracking here; the decision is recorded in backlog.md -->
# AIW-151 — Should the 2015 truth definition enter English FMT?

**Question (MG, verbatim):** the 2015 FMT truth definition is "base philosophy, might be important to include so no misinterpretation of fmt occurs?"

**Verdict in one sentence:** the 2015 truth definition is a corroboration measure wearing an alethic name; every current FMT claim stands on the knowledge definition beneath it and on nothing above it, so publish the knowledge–truth decoupling in one clause where knowledge is already defined, and keep the formula, the word *relative* and the *Konvention* out of every English venue.

**Scope guard.** MG ruled S288 (2026-08-06) that the monograph-correction analysis (p.24 vs p.32 contradiction, *Wahrheitsgehalt* rename as an erratum) is deferred, probably wrong, and not to be re-raised. This document does not reopen it. It describes what the German text says, page-cited, and asks only what the *English* FMT corpus should state. Where the text admits two readings, both are reported as readings a reviewer will see, and the S288 ruling (keep "no absolute truth", keep absolute falsity, drop the *Konvention* clause) is treated as FMT's canonical position.

Sources read: *Die Emergenz des Bewusstseins* §3.1.3–3.2 (pp. 15–35, German original); `.claude/knowledge/fmt-2015-definitions.md`; `backlog.md` AIW-151/153/122; `docs/decisions.md` 2026-08-06 truth entry; `paper/full/four-model-theory-full.md` (every hit for truth/true/false/knowledge/belief/reference system/reality/veridical); `docs/smoc-middle-layer-draft.md` §3.1; `wiki/reference/glossary.md`; `paper/fmt_formal/fmt-formalization.md`; `~/simbook/pop-sci/book-manuscript.md` (truth hits).

---

## 1. What the 2015 text says, and what it does not say

### 1.1 The chapter, page by page

| Page | Claim (German authoritative) | Type |
|---|---|---|
| 15–16 | Knowledge must be defined without "Wahrheit" or "Meinung". *"Wahrheit ist ein platonisches Konzept, das nur in unserer Vorstellungswelt existiert."* What we call truths are *"allgemein anerkannte Meinungen"*; proofs cannot be finally distinguished from very convincing arguments. | Rhetorical thesis |
| 16–20 | Eight candidate truths dismantled: semantic truths are conventions relative to language use; episodic truth depends on memory; empirical truths face induction; causality is open in physics; the dream argument (*"kann übrigens alle 'Wahrheiten' demontieren"*); negative existentials shift the burden of proof. **Explicit disclaimer:** *"Ich will damit nicht sagen, dass diese Sätze unwahr sind"* — the argument targets certainty, not truth-values. | Fallibilist argument |
| 20–21 | Conclusion drawn: *"Wahrheit [ist] eine relative Vereinbarungssache zwischen den Menschen (und in manchen Fällen sogar eine rein subjektive Sache). Nur wenn, und solange wie die meisten Menschen zustimmen, wird eine Wahrheit als solche **akzeptiert**."* Therefore knowledge is defined *"unter völligem Verzicht auf den Begriff der 'Wahrheit'"*. | Relativist wording; the verb is *akzeptiert* (acceptance), i.e. epistemic |
| 21 | *"Wissen ist Information, die einem Bezugssystem zugeordnet ist."* Bezugssystem = Modell; a virtual system counts because *"auch ein solches lässt sich letzten Endes wieder auf ein physikalisches Bezugssystem zurückführen."* The Bezugssystem need not be conscious. | Definition; physicalist grounding |
| 24 | Because truth-content is removed from the definition, *"es gibt wahres und falsches Wissen."* Pre-Copernican flat-earth knowledge *"war damals genauso falsch wie es heute ist."* | Non-factive knowledge; consensus-independent falsity |
| 25–26 | Gettier ignored via false knowledge; *latente Information* (unassignable information is not knowledge for that system); Goldman's tourist: *"das Wissen des Touristen ist echt in seinem Bezugssystem, unabhängig davon ob es wahr ist oder nicht."* Either drop the knowledge–truth link or admit *"dass es absolutes Wissen in Wirklichkeit genauso wenig gibt wie absolute Wahrheit."* | Framework-internal knowledge; a truth fact the frame does not settle |
| 27 | First attempt at truth-content: *the probability that a knowledge content agrees with reality* — rejected because *"wie die Realität in Wahrheit aussieht, wissen wir ja vielleicht gar nicht."* Replacement target: true knowledge is *"solches Wissen, welches einer bestimmten Art von Überprüfung standhält, möglichst weitgehend unabhängig davon, wer es überprüft."* | Correspondence rejected for lack of access, not for lack of a world; tester-invariance as the goal |
| 28 | *Bedeutung* = relation to a chosen Bezugssystem (position on chosen axes). *Eindeutigkeit* = degree of agreement of the chosen reference systems; *"mehrere Personen oder Maschinen"* are implied. | Inter-system agreement, level 1 (which frame) |
| 29 | *Wahrheitsgehalt* = mapping of the degree of agreement of the meanings assigned, in agreeing reference systems. Operational form W = Σwᵢ/i, wᵢ ∈ {0,1}. Three error sources: assign the information / understand the question / relate the two. | Inter-system agreement, level 2 (which position in the frame); a measurement construct |
| 31 | The concrete formula is weaker than the abstract definition; *"man sollte eine Definition nicht mit einer Rechenanweisung verwechseln"*; W ⇒ f(w). True knowledge = *"von der Mehrheit … auf dieselbe Art interpretiert"*. | The author's own warning against reading the ratio as the definition |
| 32 | *"Auf das Konzept einer absoluten Wahrheit verzichten wir, zugunsten einer Konvention von Wahrheit."* Flat earth *"galt … als wahres Wissen"*; today *"andere Menschen [sind] 'dafür zuständig'"*. The Austrian-liar sentence scores ≈ 50 %; a random Rorschach blot scores false for every concrete proposal. | Consensus wording; *galt als* = "was regarded as" (epistemic) |
| 33–35 | *Glaube* = knowledge a person claims has maximal truth-content. Reliability Z = Σsᵢ/i over sources' certainty (0..1). *Subjektives Wissen* is built firmly into the world-model; *objektives Wissen* carries admitted residual uncertainty and is not. | Aggregate credence; belief taxonomy |

### 1.2 Two strands, one word

The chapter carries two things under one name.

1. **A measurement strand.** *Wahrheitsgehalt* is the proportion of independent reference systems (people or machines) that place a content at the same position in an agreeing frame. Its stated target is invariance across testers (p.27), its grounding is physical (p.21), and the text itself insists it is a definition, not a computing rule (p.31). This is an operationalisation of intersubjective corroboration. It presupposes a world: the flat earth is false "then and now" (p.24), the tourist's knowledge may be false in fact (p.26), the correspondence formulation is rejected only because reality is not directly readable (p.27).

2. **A constitutive strand.** Three passages say truth *is* agreement: p.16 ("allgemein anerkannte Meinungen"), p.20–21 ("Vereinbarungssache … rein subjektive Sache"), p.32 ("Konvention von Wahrheit", truth-value changing with the deciding population). These are the sentences that read as global relativism.

The arguments (pp.16–20) support only the first strand: every case shows we cannot be *certain*, and the author says so. The conclusion is worded in the second. That slide — fallibilism stated, relativism concluded — is the standard error a philosopher will mark, and it is why AIW-151 flagged the definition as a liability. MG's S288 ruling already selects strand 1 (keep "no absolute truth" as anti-God's-eye fallibilism, keep absolute falsity, drop the *Konvention* clause). So the question "is it really global relativism?" has a precise answer: **the machinery is a model-relative, epistemic corroboration measure compatible with realism about the world; the wording of three passages is relativist; FMT's canonical position is the machinery without the wording.**

### 1.3 Mapping onto existing positions

| Position | Overlap with 2015 | Difference | Cite |
|---|---|---|---|
| Fallibilism (Peirce; Popper) | The eight-case argument is pure fallibilism; "false knowledge exists" matches Popper's objective knowledge, which includes conjectures later refuted | Popper keeps truth absolute (Tarskian correspondence) as a regulative idea and denies only a *criterion*; 2015 renounces the concept | Popper 1963 ch.10; Popper 1972 ch.3 |
| Framework-relativity of knowledge (Carnap internal/external questions; Putnam's internal realism; Hawking–Mlodinow model-dependent realism; Goodman) | "Wissen ist echt in seinem Bezugssystem" is an internal question; Bezugssystem = Modell is model-dependent realism avant la lettre | These are all realist about a world and none is a consensus theory of truth; Putnam later abandoned even internal realism as too epistemic | Carnap 1950; Putnam 1981; Hawking & Mlodinow 2010; Goodman 1978 |
| Peirce's end-of-inquiry consensus; Habermas's consensus theory | p.27's "survives testing independent of who tests" is Peircean | Peirce's consensus is the *ideal limit*, which is what protects him from current-majority relativism; 2015's operational form uses the current majority. Habermas built a consensus theory (1973) and gave it up (1999) — a documented warning | Peirce 1878; Habermas 1973, 1999 |
| Deflationism (Ramsey, Quine, Horwich) | "Truth is a Platonic concept existing only in our imagination" resembles the denial that truth is a substantive property | Deflationists keep the predicate and give it no theory; 2015 gives it a substantive (statistical) definition, so it is inflationary, not deflationary | Horwich 1990 |
| Coherence theory | Knowledge as fit into a model is coherentist in flavour | 2015's truth-content is *cross*-system agreement, not intra-system coherence; the S288 falsity mechanism (within-system inconsistency with admitted input) is the coherentist element, and it is negative-only | Rescher 1973 |
| Bayesian / aggregated credence | Z = Σsᵢ/i is a linear opinion pool; W = Σwᵢ/i is a proportion of agreement | Both are estimators; neither literature treats them as *definitions* of truth. Condorcet's jury theorem shows a majority verdict tracks truth only when competence > ½ and votes are independent, which presupposes a truth the verdict does not constitute | Genest & Zidek 1986; Cohen 1960; Condorcet 1785 |
| Objectivity as invariance across frames | The word *Bezugssystem* is borrowed from physics, where objectivity is frame-invariance; p.27's target is exactly that | Nobody calls frame-invariance relativism; this is the cleanest English framing for strand 1 | Nozick 2001 |
| Tarski's semantic conception | Truth defined relative to a language | Language-relativity of the *definition* is not relativism about *what is true*; useful analogy for "model-relative knowledge ≠ relative truth" | Tarski 1944 |
| Formal treatments of the liar | The ≈ 50 % agreement value | Kripke assigns the liar no classical value (ungrounded); many-valued and fuzzy logics assign it ½ — the outcome is occupied, the mechanism (agreement across raters) is not | Kripke 1975; fuzzy ½ (verify) |
| Non-factive "knows" | "false knowledge" | Hazlett argues ordinary "knows" is not factive — the one epistemology paper that supports 2015's usage directly | Hazlett 2010 (verify) |

**Where 2015 is novel.** (i) One physical primitive carries the whole ladder: knowledge, meaning, unambiguity and truth-content are all *operations on models*, and knowledge is made machine-applicable by removing truth from it. (ii) Unambiguity and truth-content are the same relation (inter-system agreement) at two levels — which frame, and which position in it. (iii) The three-error-source decomposition of a verdict (assign / understand the question / relate). (iv) The S288 extension, which is 2026 and MG's own: falsity as a within-system-against-input relation that any successor system inherits, truth as requiring a standpoint outside every system, hence *absolute falsehood without absolute truth*, with the cost-of-conversion prediction. That is Popperian in shape and derived from the model primitive rather than from the logic of universal statements; it is the publishable part and is already routed (AIW-122 blog, v-next §3.6 candidate).

**Where it is occupied.** Everything in the table's first column. A reviewer will see Protagoras, Peirce, Carnap, Habermas and model-dependent realism before seeing anything new, and the only new part is the S288 asymmetry, which does not need the 2015 formula to be stated.

### 1.4 Likely misreadings of the 2015 text itself

1. *"Wahrheit ist relativ"* read as semantic relativism (truth varies by community) — invited by pp.16, 20–21, 32.
2. The ratio W = Σwᵢ/i read as the *definition* rather than an *estimator* — invited by the label, despite p.31's own warning.
3. "Truth is a Platonic concept existing only in our imagination" read as anti-realism about the world — the sentence is about the concept, and p.21 grounds every reference system physically.
4. "False knowledge" read as a contradiction in terms — the factivity objection ("that is belief, not knowledge").
5. Self-application: most people hold truth to be absolute, so "truth is relative" scores low by its own measure — Plato's *peritrope* against Protagoras (Theaetetus 170–171).
6. *Gelten* / *galt als* translated alethically ("was true") instead of epistemically ("was regarded as true") — the standing lesson in `fmt-2015-definitions.md`; in English translation the ambiguity disappears and the relativist reading is forced.

---

## 2. What current FMT actually commits to

Line numbers refer to `paper/full/four-model-theory-full.md` (1,766 lines).

| Commitment | Where | Status |
|---|---|---|
| Model = "a non-trivial reference system with write access, read access, boundary recognition (Gruber, 2015)" | l.162, Table 1 | The Bezugssystem primitive is already public |
| Knowledge = "information assigned to a reference system … The regress is consciousness-free throughout: a system possessing a reference system has knowledge whether or not it is conscious" | l.402, §3.6 regress argument | The 2015 knowledge definition is already public, **non-factive and truth-free** |
| Truth: no theory anywhere. Ordinary uses only: "false dichotomy" (l.231), "true randomness" (l.528), "false-positive" (l.476), Gödel "true statements it cannot prove" (l.1070) | — | No dependence on the 2015 truth definition |
| World-relative accuracy presupposed: "delusions (false world-model updates …)" (l.1037); "veridical agency" (l.574); "reality-contact", "servos the … simulation against reality" (l.598); "not a direct window onto reality" (l.406); "confabulations" (l.150); "model accuracy" (l.310); Anton's syndrome "sees a world that is not there" (l.808); anosognosia "the ISM contains the information (e.g., that a limb is paralyzed)" (l.411); Mary "knows every physical fact" (l.612) | throughout | Every one of these needs a notion of *false/inaccurate relative to the world or to the system's input*, none is consensus-relative. Consistent with p.24 and the S288 principle; inconsistent with the p.32 consensus definition |
| Self-instrumentalism: "Every model has modeling error … it claims to be a useful one" | l.1078, §10.3 | Standard (Box 1976); needs no truth theory |
| Formalization: knowledge only as partitions of W (IWM/ISM) and a self-prediction measure R | `fmt-formalization.md` l.254–255, 461–465 | No truth predicate; nothing to add |
| Wiki: glossary "Knowledge (Wissen)" is the **RIM** sense (accumulated content of learning); the FMT §3.6 sense (information assigned to a reference system) and "reference system" have **no entry**; `real-virtual-split.md` states "This division is not a metaphor"; no truth entry anywhere | `wiki/reference/glossary.md` l.97–98 | Gap: two senses of "knowledge" in the corpus, one undefined in the public glossary |
| Book (`~/simbook`): "truth" appears only incidentally (blind spot, Gödel line 1867) | — | Carries no truth position; needs none |
| SMoC draft §3.1 table: cell "Unambiguity / truth-content — degree of agreement between reference systems — FMT-only" | `docs/smoc-middle-layer-draft.md` l.544 | Internal. The S288 rename (*Konsensgrad / degree of corroboration*) has **not** been applied to this cell; it must be before any public SMoC draft, and the knowledge cell carries no truth condition (verified, l.542) |

**Does any current claim silently depend on the 2015 truth definition?** No. Several claims silently depend on its *negation in the p.32 reading*: delusion, anosognosia, veridicality and reality-coupling all require falsity to be a fact about model-versus-world (or model-versus-input), not about what the majority decides. Importing the p.32 definition would create an inconsistency the master does not now have. Importing the S288 principle would not.

**Two precision findings in passing.**
- l.402 reads *"as information is data assigned an interpretation (Gruber, 2015)"*. In 2015, information is data to which a *coding* can be assigned (p.13) and *interpretation* is the assignment to a reference system that yields knowledge (p.21). The master uses "interpretation" for the information step and then relies on the knowledge step being the interpretive one, so the recursion is stated with the same word at two rungs. Suggested wording: *"as information is data to which a coding can be assigned (Gruber, 2015)"*. MG's call; p.23 does say the two are hard to separate in humans, but the master cites the definitions.
- The "Gruber, 2015" citations at l.162 and l.402 already send any German-reading reviewer to a chapter whose p.16 opens with *"Wahrheit ist ein platonisches Konzept"*. That exposure exists today, independent of any decision here. A one-clause statement of the ruled position in the paper is the cheapest way to fix which reading the paper takes.

---

## 3. Misinterpretations that can arise WITHOUT a stated truth position

| Misreading | Where it starts | Current guard in the master | Would stating the 2015 truth definition prevent it? | What would |
|---|---|---|---|---|
| "The world is a simulation, so nothing is real / FMT is anti-realist or idealist" | l.150 "confabulations", l.406 "not a direct window onto reality" | l.229 *"simulated not in the sense of being unreal"*; l.239 "physically real"; l.598 reality-coupling | **No — it worsens it.** A consensus definition of truth is what an anti-realist reading expects | One clause of world-coupling realism: contents are checked against input; falsity is decidable against it |
| "FMT = Hoffman's interface theory: perception hides reality and does not track truth" | the constructed EWM | prediction error, reality monitoring (§6.0), reality-contact | **No** | Same clause; explicit contrast with Hoffman et al. 2015 if a reviewer raises it |
| "The self is a model, therefore the self is not real" (Metzinger's no-self read onto FMT) | §3.3, §4.2 | l.56 distinction from transparency thesis; §3.4.5 computational-level realism; "real patterns" logic | **No** — truth is irrelevant to this; level-realism handles it | Nothing new |
| "Knowledge without a truth condition is not knowledge; FMT endorses that flat-earth belief is knowledge" | l.402 | none — the stipulation is bare | **Partly.** The 2015 decoupling (false knowledge exists; truth is a separate relation) answers it; the *formula* does not | A one-clause scoping of "knowledge" as non-factive, with falsity located outside the definition |
| "Explicit-model contents are only 'useful', so FMT is instrumentalist about everything including itself" | l.1078 | predictions, falsification criteria (Table 1b) | **No** — the ratio makes the theory look constructivist | Already handled by the falsification apparatus |
| "Machines have knowledge, so LLMs know things" | l.402 | l.402 "learned weights are precisely such a base layer" (intended) | n/a | Intended reading; keep |

**Net:** the only misreading a truth statement of the *right kind* prevents is the factivity objection at l.402, and it is prevented by stating the knowledge–truth decoupling, not the truth-content formula. Every other misreading is already guarded by level-realism and reality-coupling language, and a consensus-flavoured statement would undercut those guards.

---

## 4. What goes wrong WITH it

1. **Relativism charge, and it is decisive.** W = Σwᵢ/i is a consensus theory in form. Reviewers will cite Protagoras and the *peritrope*, Boghossian's *Fear of Knowledge*, and the science-wars framing. A theory that also claims physicalism and falsifiable neural predictions cannot afford to be filed as social constructivism about truth, and filing happens on the abstract of the section, not on the argument.
2. **Internal inconsistency created where none exists.** The master's uses of "false world-model updates", "veridical", "reality-contact" (§2) would have to be reconciled with a consensus definition. Under the S288 principle they need no reconciliation.
3. **Reviewer redirection.** Every reviewer has a view on truth. An epistemology section draws philosophers of language into a consciousness paper and gives them a target unrelated to any prediction. It also makes the self-published German monograph the cited foundation of a strong philosophical claim.
4. **Scope creep.** The definition cannot be stated alone. It sits on Daten → Information → Wissen → Bedeutung → Eindeutigkeit → Wahrheitsgehalt, and stating the top rung invites the whole ladder — which collides head-on with Floridi's veridicality thesis (false semantic information is not information; 2015 holds false knowledge is knowledge). That is a paper of its own, and it is the SMoC middle layer's paper, not the FMT master's.
5. **Routing conflict.** MG's S288 constraint for the truth blog is: publish the principle, never *Wahrheitsgehalt*, the monograph, p.24 or p.32. Putting the formula in the paper reverses that decision by the back door.
6. **Translation hazard.** *Gelten* and *Vereinbarung* lose their epistemic shading in English; a faithful rendering of p.20–21 or p.32 reads more relativist in English than in German.

---

## 5. Recommendation

**Do not include the 2015 truth definition** (the *Wahrheitsgehalt* formula, the consensus wording, the word *relative*) in the FMT master, the formalization, the wiki or the book. **Do include the knowledge–truth decoupling**, because the knowledge definition is already public at l.402 and is the one place the factivity objection lands. The falsity-asymmetry *principle* (S288) is a separate, already-tracked decision (AIW-122 blog first; v-next §3.6 candidate) and is not "base philosophy" to be inserted for safety — it is a contribution that earns its own place or not.

Options, recommended first:

- **(A) Minimal clause at l.402 [recommended].** After *"Take knowledge to be information assigned to a reference system"*, add *"— stored, interpreted content, accurate or not; whether it holds is a separate relation between the model and its input —"* and correct the parenthetical to *"as information is data to which a coding can be assigned"*. Cost: one line. Effect: blocks the factivity objection, states realism about the world by implication, adds no target.
- **(B) Three-sentence footnote at l.402** (draft below). Use if MG wants the position stated rather than implied. Adds one footnote-sized target; still no formula.
- **(C) Public glossary entries** *Reference system (Bezugssystem)* and *Knowledge (FMT sense)*, each two lines from the draft, distinguishing the FMT sense from the existing RIM "Knowledge (Wissen)" entry. Do this in any case; it closes the two-senses gap independently of A/B.
- **(D) SMoC §3.1 cell rename** "truth-content" → "degree of corroboration" per the S288 ruling, before any public draft. Independent of A/B; a standing knock-on that has not been executed.
- **(E) Nothing.** Defensible, since no current claim depends on truth; leaves the l.402 factivity exposure and the "Gruber, 2015" pointer to p.16 unaddressed.

Formalization: nothing (no truth predicate exists there and none is needed). Book: nothing (the blog carries the principle).

### Draft — FMT's position, three sentences, current register

> Knowledge here is information assigned to a reference system, and a reference system is a model, so knowledge is model-relative and can be false. Truth is no part of that definition: a content is shown false wherever a model contradicts its own admitted input, and there is no standpoint outside every model from which a content could be certified true. Agreement between independent models measures how far a content has survived such checking; it records corroboration and does not make the content true.

Fidelity check against 2015: sentence 1 = p.21 (definition, Bezugssystem = Modell) + p.24 (false knowledge exists). Sentence 2 = p.20–21 (knowledge defined without truth) + p.32 first clause and p.26 (no absolute truth, no view from outside all reference systems) + p.24 and the S288 mechanism (falsity decidable against input, consensus-independent). Sentence 3 = pp.27–29 (agreement across independent reference systems as the measure, tester-invariance as its target) with the S288 rename applied (*records corroboration*) and the p.32 constitutive clause dropped, as ruled. Register: no throat-clearing, no self-narration, no history; the one contrast in sentence 3 (records vs makes) is the distinction the position turns on, and the sentence does not say the same thing without it.

---

## 6. Citations used above — confidence

| Cite | Confidence |
|---|---|
| Popper 1963 *Conjectures and Refutations* ch.10; Popper 1972 *Objective Knowledge* ch.3 | high |
| Carnap 1950 "Empiricism, Semantics, and Ontology", *Revue Internationale de Philosophie* 4 | high |
| Putnam 1981 *Reason, Truth and History*; later retreat in the 1994 Dewey Lectures (*J. Phil.* 91) | high / medium (retreat: verify page) |
| Hawking & Mlodinow 2010 *The Grand Design* (model-dependent realism) | high |
| Goodman 1978 *Ways of Worldmaking* | high |
| Peirce 1878 "How to Make Our Ideas Clear", *Popular Science Monthly* 12 | high |
| Habermas 1973 "Wahrheitstheorien"; Habermas 1999 *Wahrheit und Rechtfertigung* (abandons the consensus theory) | high that both exist; medium on characterising 1999 — verify before quoting |
| Horwich 1990 *Truth* | high |
| Rescher 1973 *The Coherence Theory of Truth* | high |
| Genest & Zidek 1986, *Statistical Science* 1(1) (opinion pools) | high |
| Cohen 1960, *Educ. Psychol. Meas.* 20(1) (kappa) | high |
| Condorcet 1785 *Essai …* (jury theorem) | high |
| Nozick 2001 *Invariances* (objectivity as invariance) | high |
| Tarski 1944, *PPR* 4 | high |
| Kripke 1975 "Outline of a Theory of Truth", *J. Phil.* 72 | high; the fuzzy-logic ½ for the liar is commonly stated but **not verified here** |
| Hazlett 2010 "The Myth of Factive Verbs", *PPR* 80(3) | medium — **verify** before citing |
| Gettier 1963 *Analysis* 23; Goldman 1976 *J. Phil.* 73 (fake barns, credited to Ginet) | high |
| Hoffman, Singh & Prakash 2015 "The Interface Theory of Perception", *Psychon. Bull. Rev.* 22 | high |
| Boghossian 2006 *Fear of Knowledge* | high |
| Floridi 2011 *The Philosophy of Information* (veridicality thesis) | high |
| Box 1976 "Science and Statistics", *JASA* 71 | high |
| Plato, *Theaetetus* 170–171 (peritrope) | high |
| Dennett 1991 "Real Patterns", *J. Phil.* 88 | high |

Every citation must pass the project's verification step (title, authors, venue, DOI) before it enters any draft; this table records confidence, not verification.
