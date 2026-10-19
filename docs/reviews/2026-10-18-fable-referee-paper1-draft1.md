# Referee report — "Limits Without an Outside: Why the Limits of Embedded Description Travel as Refutations" (draft 1, 2026-10-18)

Reviewer: Fable 5.1 subagent, acting as referee for an Erkenntnis / Philosophy of Science–level venue. Manuscript read: `drafts/papers-book/paper1-draft.md` (body 7,580 words + references 680 = 8,370, measured with `wc`). Context read: `docs/papers-book/paper1-brief.md` (MG rulings treated as binding), `docs/papers-book/prior-art-paper1.md`. No files modified.

Binding rulings respected and not re-opened: the outside-the-universe view is not a perspective; exactly two unconditional limits L1/L2; capacity, irreducibility and incompleteness world-conditional; the falsity gradient excluded.

---

## 1. Recommendation

**Major revision.** Not acceptable as it stands; a revised version could be publishable, and the venue is right for it.

The paper poses a genuine problem (limitative theses appear to be asserted from the standpoint they deny), knows the literature well, and proposes a position that is worth having in print: the limits are held as refutations whose negations are inconsistent with what any claimant is committed to in claiming, and refutations, being relations between a system and its own admitted input, pass between perspectives without a shared ontology. The two-tier taxonomy and the refutation reading are defensible contributions; the §5 account of falsity is competent critical rationalism with a clear statement of what it does and does not claim. The manuscript fails in its present form at its load-bearing point. The regress argument for L1, the first of the two unconditional limits, is invalid as written: its second horn asserts a "further act" that nothing in the argument forces, and a regress that does not terminate is not a proof that no fixed point exists (Kleene's recursion theorem supplies exactly such fixed points for self-description). The natural repairs either make L1 a near-definitional type distinction or turn it into Breuer's counting argument or a Lawvere-form argument, each contradicting something the paper says about L1. Around this sit several substantive but fixable problems: "unconditional" is overclaimed (W is assumed finite and the assumption is used); horn (b) of L2 rests on a false sentence; §6 misapplies Mackie's operational self-refutation, and operational self-refutation would not yield falsity anyway; the Duhem–Quine "reply" concedes the objection's content; the dialetheist exemption is stated in a form unfair to Priest; Moore is engaged on the wrong thesis; and the taxonomy uses two incompatible criteria in §4 and §7. The mathematics is largely correct, with a handful of local errors noted below. I would want to see the revised paper.

---

## 2. Findings

Tags: **[BLOCKER]** argument wrong or self-refuting as it stands; **[MAJOR]** argument or positioning fails as written; **[MINOR]** local fix.

### Validity of L1

**F1. [BLOCKER] The L1 regress is invalid as written; the obvious repairs each contradict a claim the paper makes about L1.**
*Location:* §3 L1 paras 1 and 3; abstract "(a regress, not a diagonal argument)"; §8 last objection.
*Problem.* The second horn reads: if c includes its own being held, "that representation is itself content, produced and held by a further act of G_t". Nothing forces "further". If the act A holds all of c, then the part r of c that represents A is held by A, not by another act; the regress starts only under an unstated premise P: *a representation of an act is produced by an act distinct from the one represented.* P is Ryle's premise and is contested (any self-referential sentence is a prima facie counterexample). Worse, even granting P, the regress shows only that the naive construction (append a representation of the latest act) does not close. Non-termination of an iteration is not non-existence of a fixed point. Kleene's second recursion theorem gives, for any computable transformation, a program whose output is a complete description of itself including the instruction that produces that output; quines are the concrete case. So complete self-description that includes its own production is possible, and ruling out a fixed point needs a fixed-point-free operation, which is Lawvere form, which the paper says L1 does not have. Three internal confirmations: (i) §3 L2 grants that in a rule-plus-initial-condition world D holds a complete description of W, and §4 says that in Rule 90 any cell at any time is given by a closed form; by §2's definition of "fixes" (together with procedures D can run), such a D fixes every fact about its own current generation at t. L1 read as a representational limit is therefore false in the paper's own example world. (ii) §3 says L1 holds "with a frame that is simple"; a one-bit frame is described by one bit. The only thing c cannot *be* is the act, which is the type distinction "a product is not its process". (iii) §8 ("the time index is a convenience") gives away the one reading immune to the quine, namely concurrency: the act in progress is not yet a completed object and so cannot be the object of a completed description. With the time index dropped, the quine applies in full.
*Fix.* Choose one, say which, and rewrite the abstract's parenthesis accordingly:
(a) Keep L1 as a lemma about the frame/content relation, derived from §2's relational definition (within one perspective at one time, the frame is what distinguishes and the content what is distinguished): "the distinguishing is not among the distinguished at the time of distinguishing." State that this is near-analytic, use it only to close horn (c) of L2, and stop calling it a limit with independent epistemic content.
(b) Ground L1 in Breuer's non-injectivity: for finite W = D × E with |E| > 1, the restriction map from W-states to D-states is not injective, and D's content, a proper part of D, cannot distinguish all states of D's generation. This is not Lawvere form (no negation is used), is unconditional given finiteness, and is anticipated (Breuer 1995), so §1 and §7 must then say L1 is Breuer's result restated and the novelty lies in the taxonomy and §§5–6.
(c) Keep the regress, state P explicitly, defend it against the recursion-theorem counterexample by making "current" load-bearing (the act is concurrent and incomplete at t), and withdraw the §8 concession. Under (c) "not a diagonal argument" is true and the result is correspondingly modest; say so.

**F2. [MAJOR] "Unconditional" is overclaimed: W is assumed finite and the assumption is used.**
*Location:* §2 "Let W be a whole, taken finite"; §2 positional input (ii); §3 last para "they depend on nothing about the world"; §9 "without any assumption about the world".
*Problem.* Positional input (ii), fewer degrees of freedom, follows from proper-parthood only for finite W; an infinite proper part can be equinumerous with the whole. Finiteness of the universe is a substantive and open assumption about the world. L1 and L2 as argued do not use (ii); only capacity does (§6 para 3).
*Fix.* Delete (ii) from positional input and move it to §4 Capacity as that limit's premise. Replace "depend on nothing about the world" with "depend on nothing about W beyond D's being a proper part of it with a frame: not on its compressibility, its computation or its arithmetic strength." If F1 option (b) is taken, finiteness becomes a standing assumption of L1 and must be listed as such.

### Positional input

**F3. [MAJOR] "Positional input" conflates explicit admission with pragmatic commitment, and item (iii) is near-analytic.**
*Location:* §2 Admitted input; §6 paras 3 and 5; §8 obj 1.
*Problem.* §2 defines admitted input as items D "accepts as premises ... and uses in drawing" claims. Positional input is not accepted as a premise by every claimant (a dualist describing the physical world does not admit being part of it); it is *presupposed by the act of claiming*. That is a different notion (Apel's retorsion; Mackie's operational category), and §5's refutations are about the first notion. Item (iii), having a frame, is analytic given §2's definition of frame as whatever does the distinguishing, so the §6 "contradiction between the claim and the frame" is never immediate: it runs only through the §3 lemmas, and is exactly as strong as they are (see F1). Item (i) requires W to be maximal (see F19).
*Fix.* In §2: "Positional input is admitted in a second sense: not accepted as a premise, but presupposed by any claim about W, so that denying it while claiming is pragmatically inconsistent. The refutations of §6 run on this sense; §5 runs on the first. The two coincide once the claimant is asked to make its presuppositions explicit, which is what §6 does." Then in §6 replace "contradicts its own frame" with "together with the lemma of §3, is inconsistent with the admission that it has a frame".

### L2

**F4. [MAJOR] Horn (b) of L2 rests on a false sentence; repaired, L2 is Albert's trilemma and inherits its contested status.**
*Location:* §3 L2 para 1 ("the admitted set contains nothing about its own complement"); §3 L2 para 2; §2 Completeness.
*Problem.* The admitted set can contain a totality claim. §2 lists axioms among admitted input, and the paper's own example two sentences earlier, "a part can hold the rule and the condition", is an admitted input of the form "W is generated by R from I and nothing else", which is a claim about the complement. What is true is weaker: a totality claim in the admitted set is admitted, not certified, and certifying it is the original task again. That is Albert's third horn (dogmatic stop), which the next paragraph already names. Two consequences the paper does not draw: (i) the trilemma is contested (foundationalists deny that every stop is dogmatic; infinitists accept the regress, Klein 1999; coherentists deny the circle is vicious). L2 blocks the foundationalist only because §2 *defines* certification as establishing "from its admitted input and by procedures it can run", so that a stop is by definition not a certification; the paper should say that L2 is partly definitional at this point. (ii) §2 defines completeness relative to what Δ "claims to cover", so a Δ with a restricted claimed scope can be certified complete from inside; L2 must be restricted to Δ whose claimed scope is all of W. This restriction is also what supports §5's claim that positive verdicts of fit are available. (iii) "D has access to W only through what it holds" is representationalism unless made analytic.
*Fix.* Rewrite horn (b): "A check against the admitted input shows at most that Δ fixes everything the input reports. The input may itself contain the claim that it reports everything there is; but that claim is admitted, not certified, and certifying it is the original task over again. The second route therefore either begs the question or hands it on." Add after the Albert paragraph: "The trilemma's third horn is disputed; here it is closed by the definition of certification in §2, which does not count a stop as a certification. L2 is to that extent a consequence of what 'certify' means for a part." In §2 add: "Anything D uses in a check is thereby admitted input." And: "L2 concerns descriptions whose claimed scope is W entire; a description of restricted claimed scope can be certified complete, which is one of the positive verdicts §5 leaves available."

**F5. [MINOR] "L2 takes the form of Gödel's second theorem" is an analogy, not an instance.**
*Location:* §3 L2 para 2.
*Problem.* Gödel II concerns consistency, not completeness. A sound system fails to prove its own completeness trivially, because by Gödel I it is incomplete; no second theorem is needed.
*Fix.* "The nearest formal analogue is the second theorem: the system cannot certify from inside a global property of itself on which the standing of all its claims depends."

### Section 6 and self-application

**F6. [MAJOR] §6 misapplies Mackie's operational self-refutation, and operational self-refutation would not deliver falsity.**
*Location:* §6 para 5 ("the completeness claim is operationally self-refuting"); §8 obj 2; abstract.
*Problem.* Mackie's operationally self-refuting proposition may be true; it merely cannot be asserted in that way ("I am asleep"). Two errors follow. (i) The completeness claim does not *deny* being a proper part with a frame; it is inconsistent with that admission only via the L2 argument. That is ordinary inconsistency with an auxiliary premise plus a lemma, not operational self-refutation. (ii) If the paper did rely on operational self-refutation it would be entitled to "cannot be asserted from inside", not to "false relative to input", and "cannot be said from inside" is Moore's "shown, not said" (F11). The paper's entitlement to "false relative to input" is exactly the logical validity of the §3 arguments, which F1 puts in question.
*Fix.* Replace the paragraph: "The negation of each limit, together with the positional input of whoever asserts it, is inconsistent by the arguments of §3. The inconsistency is logical, not merely operational in Mackie's (1964) sense: it is not that the act of asserting presupposes what the content denies, but that the content and the admitted position together entail a contradiction. That is what entitles the account to 'false relative to input' rather than 'unassertable from here'." Keep Mackie for the taxonomy; drop him as the mechanism.

**F7. [MAJOR] The paper applies its own split to one thesis ("there is no outside") and not to its own assertions or to its meta-thesis.**
*Location:* §6 last para; abstract and §3 headers ("hold unconditionally"); §6 para 2 ("the negation fails from inside every perspective"); §9.
*Problem.* By §5, "two limits hold for every embedded describer" and "refutations travel where positive claims do not" are positive universals, held from inside, fitting the author's input. The paper asserts them flatly. A referee will say the account exempts itself, which is the relocation the paper exists to avoid. The honest position is available and is Bartley's: the universals are held as fits; what is offered to every other perspective is the schema each can run on itself. Also "reaches every perspective" means "every perspective that admits the inference steps", as for any argument whatever; the paper should not imply more.
*Fix.* Add to §6 or §9: "The same split applies to this paper. That two limits hold for every embedded describer is, as a positive thesis, held from inside and fits the input the author admits; what is offered to any other perspective is the schema of §§3 and 6, which it can run on itself with its own positional input. That refutations travel is likewise a thesis held here as a fit; what travels is each particular refutation." In §8 obj 1 change "reach every claimant" to "reach every claimant who admits the steps of §3".

### Falsity, Duhem–Quine, scope

**F8. [MAJOR] "Falsity" is inconsistency, and "truth as match is unavailable" is epistemic, not semantic; the Putnam contrast is misdrawn.**
*Location:* §5 title and first two subsections; §7 Putnam; title option B in the brief.
*Problem.* What an exhibited contradiction establishes is inconsistency of a set, a logical relation; "false" follows only on the condition that the input is true, which the paper rightly declines to certify. So "falsity" means "false if the input is true" throughout; fine, but it must be said once, or the title reads as renaming. "Truth as match is unavailable" is a claim about certification (nobody can certify a match), not about truth; Putnam's was semantic (metaphysical realism's truth is incoherent). A deflationist will say truth is cheap and certification dear, and the paper agrees without saying so.
*Fix.* Open §5 with: "'Falsity' below means inconsistency between a system's claims and the input it admits; it is falsity of the claims on the condition that the input is true, and nothing more. 'Truth as match' means a verdict of correspondence certified from a position outside all models; its unavailability is epistemic. A deflationist will say truth is cheap and certification dear; the account concerns certification." In §7 Putnam: "Putnam denies the coherence of the standpoint; the present account denies access to it and leaves its coherence open."

**F9. [MAJOR] The Duhem–Quine reply concedes the objection; inheritance is monotonicity; Lakatos is the prior theory of visible patching; the flat-earth example is a Duhem–Quine case against itself.**
*Location:* §5 Duhem–Quine and Inheritance; §1 third contribution ("meets the Duhem–Quine objection"); §8 obj 5 ("met instead of conceded").
*Problem.* (i) The reply grants what Quine grants, that a recalcitrant experience shows *something* in the set must go, and claims only that. That is accepting holism about localization, not meeting it. (ii) "Inherited by every successor that keeps the input" is monotonicity of classical consequence: supersets of an inconsistent set are inconsistent. Every consistent successor drops a member, so the thesis has no actual successor in its extension unless "the input" means the observations and the dropped member is the hypothesis, which is modus tollens. (iii) The "visible cost" of patching is the subject of Lakatos's (1970) ad hoc₁–₃ distinctions and progressive/degenerating problem-shifts, a developed theory of exactly that; the paper cites Lakatos only as objector. (iv) In the flat-earth example the inferences use auxiliaries, rectilinear propagation of light and the identification of the shadow as the earth's, not named as kept input; a flat-earther who drops rectilinear light keeps every observation listed.
*Fix.* §1 and §8: replace "meets ... instead of conceded" with "accepts holism about which member is false and shows what holism leaves standing: the inconsistency of the kept set, which is monotone under addition, and the visibility of any drop". State inheritance as monotonicity in one sentence. Add: "Which drops are acceptable is Lakatos's question; the present account says only that every drop is visible to those who keep the member." In the example, list the auxiliaries as kept input.

**F10. [MAJOR] The dialetheist exemption is stated in a form that is false and unfair to Priest.**
*Location:* §5 scope condition; §8 obj 3 ("they stand outside the reach of every refutation, not of these alone"); §7 Priest.
*Problem.* Priest's dialetheism is targeted: true contradictions at the limits of thought (inclosure) and in the semantic paradoxes. He accepts classical recapture in consistent domains (*In Contradiction*, 2nd ed. 2006, ch. 8; *Doubt Truth to Be a Liar*, 2006) and would accept Cole's refutation of Mersenne without hesitation. A dialetheist is exempt only from refutations whose contradiction she accepts as true, and for Priest those are precisely the inclosure contradictions, which are precisely this paper's limit claims. So the exemption bites exactly on the paper's thesis and nowhere else; §8's generalization is wrong and §7's "the disagreement is about logic" is correct but understated.
*Fix.* §8: "A dialetheist who accepts the exhibited contradiction as true is not refuted by it. Nothing follows for refutations whose contradictions she does not accept, and for Priest those are almost all of them. The exemption falls where the inclosure contradictions fall, on the limit claims themselves, which is where this account and dialetheism part, and the present account has no argument against him there." Support "most paraconsistent logics treat contradictions as defects" with Priest, Tanaka and Weber (SEP, "Paraconsistent Logic") or Carnielli and Coniglio (2016).

### Fairness and positioning

**F11. [MAJOR] Moore is engaged on the wrong thesis.**
*Location:* §1; §2 "A supposed view from outside everything"; §5 "Why truth as match is unavailable"; §7 Nagel/Putnam/Moore/Grim.
*Problem.* Moore's absolute representation (after Williams's absolute conception) is a representation not perspectival in *content*, made from within; it is not a view from outside everything with no frame, which is what §2 dismisses. And the paper grants Moore's possibility claim: §3 says Δ may be complete. The paper denies only certification. So Moore is not "the direct opponent" on absoluteness; he is the opponent only on whether the limits are known ineffably or said. Given F6, if the paper's refutations were operational, its position would be close to Moore's "shown, not said".
*Fix.* §7: "Moore holds that absolute representations are possible; the present account does not deny it, since Δ may be complete. It denies that a part can certify one as such. The disagreement is over the limits: Moore holds they are known and not sayable; here they are said, as refutations, with a logical rather than performative inconsistency behind them (§6)." This requires F6's repair to be honest.

**F12. [MAJOR] The taxonomy uses two incompatible criteria; Breuer and Wolpert are misplaced by one of them.**
*Location:* §4 (conditions on W or the system); §7 Lawvere para ("the diagonal results carry a condition, an operation without a fixed point ... while the regress and the certification limit carry none"); §7 Popper–MacKay–Breuer–Wolpert para.
*Problem.* §4 classifies by whether a fact about W or the system must be assumed. §7 says conditional = diagonal. Capacity is conditional but is counting, not diagonal. Breuer is counting (non-injectivity) and placed unconditional, while capacity-counting is conditional. Wolpert's main theorem is diagonal (the device is asked about a function that negates its own output) and is placed "kin to the unconditional tier".
*Fix.* Two axes, stated in §4 and used in §7. Axis 1, conditionality: what must be assumed about W or the system beyond proper part with frame: nothing (L1, L2, Breuer), compressibility (capacity), irreducible work (irreducibility), arithmetic strength (Gödel), capacity to negate own output (Popper–MacKay, Wolpert). Axis 2, mechanism: regress or definition (L1, L2), counting (Breuer, capacity), diagonal (Gödel, Turing, Popper–MacKay, Wolpert). Then rewrite the §7 Lawvere sentence as: "the diagonal results need an operation without a fixed point, which the system or describer must supply; L1 and L2 use none, and Breuer's counting uses none either."

**F13. [MAJOR] The Letztbegründung debate is the paper's home and is absent.**
*Location:* §3 (Albert used for L2); §7 Bartley/Apel.
*Problem.* Albert's trilemma and Apel's retorsion are the two poles of the German Letztbegründung debate. Apel (1976) is, if the referee's memory of the subtitle is right ("Versuch einer Metakritik des 'kritischen Rationalismus'", to be verified), explicitly a critique of Albert, Popper and Bartley; Albert replied in *Transzendentale Träumereien* (1975); Kuhlmann's *Reflexive Letztbegründung* (1985) is the systematic defence. The paper's thesis that retorsion yields only negative results is Albert's position in that debate, stated without the debate. A referee in epistemology will see this at once, and the paper currently cites both poles without noticing they are poles.
*Fix.* One paragraph in §7: the account accepts Apel's mechanism and Albert's verdict on its yield, and adds the account of why the negative result travels (§5). Cite Albert 1975, Kuhlmann 1985. Verify Apel 1976 before submission (currently [UNVERIFIED] in the reference list; a referee will not accept that).

**F14. [MINOR] The reading limit is not an instance of L2.**
*Location:* §3 last para.
*Problem.* The reading limit concerns interpretation (which structure is representational), not completeness; none of L2's three horns applies to it as stated.
*Fix.* Present it as "a second application of the absence of an outside, not of L2 itself", or show the mapping: the system cannot certify that its sorting of world structure from surplus structure is complete over the whole, which is L2 relative to that distinction.

**F15. [MINOR] Popper did extend the asymmetry beyond scientific theories.**
*Location:* §8 obj 5.
*Problem.* "What Popper did not do is ... extend the asymmetry to reference systems that are not scientific theories" is false: *Objective Knowledge* (1972), the evolutionary epistemology ("from the amoeba to Einstein"), *All Life Is Problem Solving* (1994).
*Fix.* Delete the clause or replace with: "Popper extended the asymmetry to organisms' expectations (1972) within the setting of trial and error-elimination; what is added is the reference-system formulation and inheritance."

**F16. [MINOR] Miller's position is glossed too strongly.**
*Location:* §5 Popper para.
*Problem.* Miller (1994) rejects justification for all claims, falsity verdicts included; his line is that criticism needs no justification, not that falsity is known securely. The paper's "security that accumulates" is foreign to him.
*Fix.* "Miller (1994) takes the strongest line: nothing is justified, falsity verdicts included, and criticism proceeds without justification. The present account agrees that the verdict needs nothing beyond the derivation, and treats security against withdrawal of input as a separate matter that Miller would not call justification either." Give the chapter.

**F17. [MINOR] Transfer "needs no agreement about what the symbols refer to" is too strong.**
*Location:* §5 "Why falsity needs no outside".
*Problem.* Checking a derivation needs agreement on the logical constants and on which strings are the system's claims and its input. For non-formal perspectives that is interpretation, and Davidson's (1973) principle of charity has the interpreter minimize attributed contradictions, which is the standing objection to "contradictions travel".
*Fix.* "needs no agreement about what the non-logical symbols refer to, given agreement on the logical vocabulary and on which claims are the system's own".

**F18. [MINOR] Missing neighbours in the distinction tradition.**
*Location:* §2 "Anything that distinguishes ... does so by a frame"; §7.
*Problem.* That sentence is Spencer-Brown's (1969) opening injunction; "the observer is the blind spot of its own observation" (von Foerster 1981; Luhmann) is L1 in second-order cybernetics. Tarski's undefinability is the Lawvere-form relative of L1. One sentence forestalls a referee from that tradition and supports the paper's own positioning that the limits are established.
*Fix.* Add one sentence to §7 Endophysics or a new short paragraph.

**F19. [MINOR] W is not defined as maximal, so "denying embeddedness claims the outside view" does not follow.**
*Location:* §2; §6 "Who is reached"; §8 obj 2.
*Problem.* A describer of a toy cellular automaton is not a proper part of it and claims no view from outside everything. The limits apply to descriptions of a whole that contains the describer. The S336 ruling (the view from outside everything is not a perspective) is respected here; it needs a definiendum.
*Fix.* §2: "W is the maximal whole D describes, everything D admits as existing. For descriptions of lesser wholes the limits do not apply, and a describer outside such a whole can see about it what its parts cannot (§4, last paragraph)."

### Factual and mathematical

**F20. [MINOR] "For finite or decidable systems the search terminates either way."**
*Location:* §5 formal para.
*Problem.* If "finite" means finitely axiomatized, false: Robinson's Q is finitely axiomatized and undecidable.
*Fix.* "For propositional systems, or any system with a decidable consequence relation, the search terminates either way."

**F21. [MINOR] Presburger and the Gödel conditions.**
*Location:* §4 Incompleteness.
*Problem.* (i) "the theorem needs the multiplication": multiplication alone (Skolem arithmetic) is also decidable (Skolem 1930; Mostowski 1952); the theorem needs both together. (ii) The first theorem from consistency alone is Rosser's (1936) form; Gödel needed ω-consistency. (iii) "enough expressive power for addition and multiplication" should be "enough to represent the recursive functions; Robinson's Q suffices".
*Fix.* "Arithmetic with addition alone (Presburger 1929) and with multiplication alone (Skolem 1930) are each complete and decidable; the theorem needs both together. If such a system is consistent, then (in Rosser's 1936 form) there is a sentence ..." Add Presburger and Rosser to the references.

**F22. [MINOR] Kolmogorov counting: "most strings have no description shorter than themselves."**
*Location:* §4 Capacity.
*Problem.* The counting gives fewer than 2^(n−c) strings of length n with K(x) < n − c; for c = 0 it yields only that at least one string is incompressible. The fraction bound 2^−c is correct for the convention K(x) < n − c; say which convention.
*Fix.* "most strings cannot be compressed by more than a few bits: fewer than a fraction 2^−c of them by c or more bits, in the sense K(x) < n − c". Solomonoff (1964) is the third name usually given; optional.

**F23. [MINOR] Irreducibility: "closed form" is undefined for finite systems, and the notion is contested.**
*Location:* §4 Irreducibility.
*Problem.* Every finite deterministic system is eventually periodic and has a trivial lookup "closed form"; irreducibility as used is resource-bounded, not Turing-type, and should be said to be. Israeli and Goldenfeld (PRL 92, 074105, 2004; Phys. Rev. E 73, 026203, 2006) show coarse-grained predictability of CAs including Rule 110; irreducibility concerns exact microstate prediction only. Rule 30 as a pseudorandom generator should cite Wolfram (1986, Adv. Appl. Math. 7, 123–169). Culik and Yu formalized Wolfram's classes before proving undecidability; say "a formalization of".
*Fix.* One sentence defining "closed form" as a shortcut whose cost grows slower than simulation; one clause restricting the claim to exact prediction with the Israeli–Goldenfeld citation; the two citations.

**F24. [MINOR] "Every set theory built since ... restricts the principle" is false and the counterexample is the paper's own point.**
*Location:* §5 Inheritance.
*Problem.* Paraconsistent set theories (Brady 2006; Weber 2010, *Review of Symbolic Logic*) keep naive comprehension and drop classical logic instead. That is the "drop a different member" move of the Duhem–Quine subsection and should be used as such.
*Fix.* "Every classical set theory built since restricts the principle; the paraconsistent set theories keep it and drop the logic instead, which is the other way of dropping a member of the inconsistent set."

**F25. [MINOR] Mersenne, Lucas, Cole: facts correct, references missing, one wording too strong.**
*Location:* §5 Arithmetic para; §9; reference list.
*Problem.* Mersenne 1644 (*Cogitata Physico-Mathematica*), Lucas 1876, Cole 1903 with factors 193,707,721 × 761,838,257,287: correct. No reference entries for any of the three. "every perspective that can do so receives the same verdict" needs the shared input named: the rules of multiplication.
*Fix.* Add Cole, F. N. (1903), "On the factoring of large numbers", *Bull. Amer. Math. Soc.* 10(3), 134–137; a Lucas reference (verify which publication records M67 composite; the 1878 *Amer. J. Math.* paper is the usual citation for the test). Change to "every perspective that admits the rules of multiplication receives the same verdict".

**F26. [MINOR] Attribution of Turing to Lawvere.**
*Location:* §1.
*Problem.* "Lawvere (1969) and Yanofsky (2003) showed that Cantor, Russell, Gödel, Tarski and Turing are one fixed-point argument" is fine as a joint attribution, but Lawvere 1969 does not treat Turing; the halting problem, Rice and the recursion theorem are Yanofsky's additions. §3 attributes correctly.
*Fix.* Leave joint, or "Lawvere (1969) for Cantor, Russell, Gödel and Tarski, Yanofsky (2003) adding Turing".

**F27. [MINOR] Lucas–Penrose paragraph has no references and the brief says footnote.**
*Location:* §4 last para.
*Fix.* Cite Lucas (1961, *Philosophy* 36) and Penrose (1989; 1994); reduce to a footnote to recover the words F1–F13 will cost.

### Abstract and wording

**F28. [MINOR] Abstract wording.**
*Location:* abstract.
*Problem.* (i) "They are impossibility claims whose negations contradict ...": every limit is an impossibility claim; the point is how they are held. (ii) "permanent once exhibited" conflicts with §5's "verdicts of falsity are revisable" until the verdict/security distinction arrives three pages later. (iii) "(a regress, not a diagonal argument)" depends on F1.
*Fix.* (i) "They are held as refutations: impossibility claims supported by the inconsistency of their negations with ..." (ii) "permanent, as a fact about the set, once exhibited". (iii) Per F1.

**F29. [MINOR] References.**
*Location:* reference list.
*Problem.* Gruber (2015) lacks publisher and place. Apel (1976) is [UNVERIFIED] and must not go out so. Wittgenstein edition unverified. Missing: Presburger 1929, Rosser 1936, Cole 1903, Lucas, Israeli and Goldenfeld 2004/2006, Wolfram 1986, Albert 1975, Kuhlmann 1985, Lakatos 1970 original, Popper 1972, Davidson 1973, Spencer-Brown 1969, Lucas 1961, Penrose 1989, Priest 2006 (*In Contradiction* 2nd ed.). Priest (1991, *Mind*) is the first statement of inclosure and is cheaper than the book for the structural point.

**F30. [MINOR] Length.**
*Location:* whole.
*Problem.* Body 7,580 + references 680 = 8,370 words (measured). The fixes above add an estimated 600–900 words.
*Fix.* Footnote the Lucas–Penrose paragraph (F27), compress §7 Endophysics and §8 obj 4 (finite describers), which repeats §4.

---

## 3. What the referee did not find

The paper does not misstate Lawvere's theorem, Gödel's mechanism, the Culik–Yu result, Albert's trilemma, Breuer's result, Nagel's position, or the critical-rationalist literature it cites. The semi-decidability correction and the dialetheist/paraconsistent distinction flagged in the prior-art report have been carried, apart from the generalization in §8 (F10) and the word "finite" (F20). The Kolmogorov fraction bound, the Rule 90 closed form, the Cole factorization and the Gödel conditions are correct as stated, subject to the local precisions above. The five self-citations are within the ruling and are used only where the framing comes from them.
