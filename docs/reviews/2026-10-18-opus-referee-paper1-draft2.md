# Referee report: "Limits Without an Outside" (draft 2, 2026-10-18)

Reviewer: Opus subagent, acting as independent referee (philosophy of logic / epistemology venue, e.g. *Erkenntnis*). Manuscript: `drafts/papers-book/paper1-draft.md` (8,988 words total, 7,949 before the reference list, measured with `wc -w`). Context: first report `2026-10-18-fable-referee-paper1-draft1.md`, changelog `2026-10-18-paper1-draft2-changelog.md`. No files modified.

I treated these author rulings as binding and did not reopen them: the outside view is not a perspective; there are exactly two unconditional limits; capacity, irreducibility and incompleteness are conditional; the slogan "the generator can appear in what it generates, but not completely" stays; the falsity gradient is out; at most five self-citations; no dependence on the Four-Model Theory (FMT). Where a finding below touches a ruling, the fix works inside it.

## 1. Recommendation

**Major revision (second round).** The revision is real. Most of the 30 first-round findings are properly resolved, not just reworded, and the paper is much better for it. One problem remains at the centre. The new L1 is valid only on a reading that makes it near-definitional, and the paper does not yet say which reading it means. Three things follow from that ambiguity. §6 needs L1 to rest on positional input, but on that reading it rests on a stipulated theory of content. §4 says L1 instantiates "not completely", but under the Kleene concession it only does so in a temporal sense. And §7 still gives L1 work (Nagel, von Foerster, the Popper–Breuer lineage) that the concession has taken away. Two more problems came in with the revision: a contradiction inside §5 about whether positive verdicts are as checkable as negative ones, and a gap in L2 where the definition of certification either lets the rule-plus-condition case through or blocks everything. Each is fixable in a paragraph or two. None of the fixes needs a new idea.

## 2. Were the first-round findings resolved?

The following were resolved in substance: F2, F3 (but see N4), F5, F6, F7, F8, F9, F10, F11, F12 (but see N6), F13, F14, F15, F17, F19, F20, F21, F22, F23, F24, F25, F26, F27 and F28.

The following were not fully resolved:

- **F1.** Option (c) was taken correctly as far as it goes. The extra premise P (that a representation of an act is produced by a different act) is now stated and declined, and Kleene is conceded. But the repair moved the problem rather than closing it; see N1–N3.
- **F4.** Horn (b) was rewritten as asked. The rewrite exposes a tension between the §2 definition of certification and §3's use of it; see N5.
- **F16.** The Miller chapter is still not given. This is an open item, not a fault in the argument.
- **F29.** Three items are still outstanding. Gruber (2015) has no publisher or place. Albert (1975) and Mersenne (1644) are still marked [UNVERIFIED], and neither can go out in that state.
- **F18 (changelog only).** The changelog says a Tarski sentence was added to §7. No Tarski appears in §7, where Tarski is mentioned only at lines 19 and 47. The paper is fine; the changelog is inaccurate.

**Mechanical citation check.** I parsed every author–year citation in the body and every entry in the reference list. All 63 entries are cited, and every in-text citation resolves to an entry. Self-citations are 2015, 2026a, 2026b and forthcoming: four entries, within the ruling. All internal "Section N" cross-references point at sections that exist. One pointer is wrong (see N9).

## 3. Findings

### The new L1

**N1. [BLOCKER] The L1 argument has two readings. On one it is invalid, and on the other it is near-definitional. The paper says the second only in part.**
*Location:* §3 L1, paragraphs 1–3; abstract; §8, last objection.
*Problem.* The key premise is "content, in the sense of Section 2, is complete at the time it is held". It is not in §2: §2 defines content only as what the frame produces and distinguishes. So the premise is new, and it is a stipulation. The conclusion can be read two ways.
- **Representation reading:** no content represents D's current generation completely. The premise does not deliver this. A finished item can represent an unfinished process. A program text plus its current state fixes the whole run, including the part still under way. And by §2's own definition of completeness, a description is complete if, "together with the procedures D can run", it fixes every fact it claims to cover. A quine's output, together with an interpreter, therefore fixes the run in progress. On the paper's own definition, L1 under this reading fails for exactly the case §3 concedes. This is draft 1's F1(i) again, now on the time axis.
- **Token reading:** no content item *is* (or contains as a part) the process-token now producing it. This one is valid, but it follows from the product/process type distinction, which §2 already builds into frame and content. That is first-round option (a). The paper half-admits it: "It is also modest ... close to what Section 2 means by a frame." But the abstract, §1 and §9 still present L1 as a limit on description standing level with L2. And the §3 wording slides between the two readings: c "includes a representation of", c "contains, as a finished item, a process", "the model can contain the act producing it".

*Fix.* Commit to the token reading and say so where it matters:
1. Put "content is complete at the time it is held" into §2 as a clause of the content definition, with a sentence of motivation.
2. Replace "contain" and "include" in §3 and §8 with "be or have as a part". State in one sentence that a complete *representation* of the act in progress (rule plus current state) is not excluded.
3. Add to the abstract's parenthesis: "a limit on the act in progress, near-analytic given the frame/content distinction".
4. Keep L1's use as the closure of L2's third route. Under the token reading it does that correctly, because that route needs W itself, the token, beside Δ.

**N2. [MAJOR] §6 needs the negation of L1 to contradict positional input. As written, it contradicts the content premise instead, which a claimant can drop.**
*Location:* §6, paragraph 3 ("inconsistent with its admission that it has a frame (L1)"); §8, objection 1 ("the limits rest on positional input only").
*Problem.* The contradiction comes from "content is complete when held" together with "the holding is under way". Neither is "being embedded" or "having a frame". A process-content theorist (an enactivist, or someone who models content as a dynamical trajectory) can deny that content is a completed item and go on making claims. So the refutation of not-L1 does not have the "cannot drop without ceasing to claim" status §6 and §8 assert. There is a second gap: on the token reading, almost no actual claimant asserts not-L1. The interesting claim, "I hold a complete self-model, including my present processing", is conceded via Kleene. So L1-as-refutation reaches very little.
*Fix.* Pick one of two routes.
- (a) Argue in §2 that the completeness of content is part of what having a frame means: to distinguish an item is to have it as a completed item. Then the premise becomes positional and §6 stands.
- (b) Say in §6 that the L1 refutation runs on positional input plus the definition of content, and that its main role is to close L2. Under (b), §8 obj. 1 must say "rest on positional input and the definitions of Section 2".

**N3. [MAJOR] After the Kleene concession, the slogan and §7 overstate what L1 shows.**
*Location:* §4 "The common form" ("L1: ... the generation does not appear whole"); §7 Nagel ("L1 is the structural reading of why the view from within cannot be absorbed"); §7 von Foerster ("L1 in another vocabulary"); §7 Popper–Breuer paragraph ("the formal history of L1").
*Problem.* §3 now grants that the generator can appear completely as a description. What cannot appear is the act in progress as a part of its own product. So for L1, "not completely" holds only in a temporal sense: every appearance is of a completed state. Nagel's unabsorbable view and von Foerster's blind spot are representational claims, and the concession weakens them. The Popper–MacKay prediction results and Breuer's state-distinguishability result are representational limits with different mechanisms (diagonal and counting). They are not the history of a token-type limit, and §4's own axis 2 already separates them from L1.
*Fix.* In §4, gloss L1's instance of the binding slogan as: "the generation appears, even completely, but only as a finished state; the generating does not appear in its own product". In §7, downgrade "is L1" and "formal history of L1" to "neighbours of L1, which address representation and so reach further than L1 under conditions". In the Nagel paragraph, say that L1 explains only why the detaching act is never among what it detaches.

### L2

**N4. [MAJOR] §2 and §6 disagree about whether the inconsistency is pragmatic or logical.**
*Location:* §2, admitted input ("presupposed ... pragmatically inconsistent"); §6, Mackie paragraph ("logical rather than operational"); §8, objection 2; abstract ("input every claimant admits in the act of claiming").
*Problem.* §2 grounds positional input in presupposition, which is Mackie's operational category. §6 then says the inconsistency is logical, which is what licenses "false" rather than "unassertable". The bridge is that the two senses coincide once the claimant makes its presuppositions explicit. But that only covers claimants who agree to do so. §8 obj. 2 openly concedes that a claimant who denies embeddedness gets only operational self-refutation. So the logical form, and with it "false relative to input", covers only claimants who admit their position. The abstract says the input is one "every claimant admits".
*Fix.* State the two tiers in §6. Against a claimant who admits its position, the negation is logically inconsistent with that admission, and the claim is false relative to input. Against one who refuses the admission, the claim is operationally self-refuting and so unassertable. Change the abstract to "input every claimant presupposes in claiming, and that a claimant who states its presuppositions admits".

**N5. [MAJOR] As defined in §2, certification either admits the rule-plus-condition case or excludes every certification, restricted scope included.**
*Location:* §2, completeness and certification; §3 L2, horn (b); §2's "a description of restricted claimed scope can be certified complete".
*Problem.* §2: D certifies Δ if D establishes completeness "from its admitted input and by procedures it can run". Suppose the input contains "W is generated by R from I and nothing else". Then D derives Δ's completeness from its admitted input, which is a certification as §2 defines it. §3 rejects this because "that claim is admitted, not certified". That adds a requirement the definition lacks: the premises must themselves be certified. Applied generally, that requirement defeats every certification, including the restricted-scope one §2 allows and the positive verdicts of fit §5 relies on. So L2 is either false by definition (definition as written) or not specific to wholes and parts (requirement as used).
*Fix.* Name what is special about the totality premise. Every other admitted item can, in principle, be checked against further input. "Nothing else exists" is the one item whose check needs access to what lies outside all input, which is the remainder that horn (c) and L1 exclude. Write this into §2's definition: "certification may rest on admitted items, except an admitted claim about the complement of the input". The definition then allows restricted-scope certification and excludes the totality case without a regress.

### New inconsistencies introduced by the revision

**N6. [MAJOR] Breuer is classed as unconditional and counting, while §4 makes counting depend on finiteness.**
*Location:* §4 Capacity ("W is finite, so that a proper part has fewer degrees of freedom"); §4 taxonomy ("nothing for L1, L2 and Breuer's non-injectivity result"; "Breuer's result counting and unconditional"); §7 ("unconditional tier by counting").
*Problem.* §2 removed finiteness at F2's request because "an infinite proper part can be equinumerous with the whole". On that same reasoning, a non-injectivity argument by counting needs finiteness, or some extra structural premise about how the observer's states relate to the whole's. As written, §4 contradicts itself: counting is conditional for capacity and unconditional for Breuer.
*Fix.* Check which premise Breuer (1995) actually uses to get non-injectivity for proper subsystems, and state it. If it is finiteness, move Breuer to the conditional tier, next to capacity. If it is a structural premise that also holds for infinite systems, name it and say why capacity cannot use the same premise.

**N7. [MAJOR] §5 contradicts itself on whether positive verdicts are as checkable as negative ones.**
*Location:* §5, "Why truth as match is unavailable" ("'This model fits the input I admit' is checkable, and no harder to check than its negation"), against the formal-systems paragraph ("Consistency, the positive verdict, has no certificate from inside"; inconsistency is only semi-decidable).
*Problem.* "Fits the input" means being consistent with it. For any system that Gödel's second theorem governs, §5 then says that verdict has no certificate from inside, while its negation does. The asymmetry the section exists to establish is denied two paragraphs earlier.
*Fix.* Restrict "fit" to agreement on the consequences actually derived and checked, a finite, local verdict, and say that fit in this sense is weaker than consistency. Then "no harder to check than its negation" holds for the local verdict, and the global asymmetry stays.

**N8. [MINOR] §6's list of refutations covers four of the five limits and does not phrase irreducibility as a contradiction.**
*Location:* §6, paragraph 3.
*Fix.* Add incompleteness: a system of the stated kind that claims to prove its own consistency is inconsistent with being consistent, which is Gödel's second theorem read as a refutation. Recast the irreducibility sentence as "... claims to obtain it ahead of the whole, which together with the condition contradicts its being a proper part with fewer resources".

**N9. [MINOR] A cross-reference points at a footnote, not a section.**
*Location:* §2: "a describer outside such a whole can see about it what its parts cannot (Section 4)". The only support in §4 is the last sentence of note 2.
*Fix.* Change to "(note 2)", or move that sentence into the §4 body.

**N10. [MINOR] The abstract says the limits are "not positive truths about all perspectives", while §6 holds the two-limit thesis as a positive fit.**
*Location:* abstract; §6, last paragraph.
*Fix.* In the abstract: "are not offered as positive truths held from nowhere".

**N11. [MINOR] A self-citation carries a load-bearing premise, and an FMT citation sits inside the core argument.**
*Location:* §5, "Why truth as match is unavailable" (Gruber 2015 is the only support for "every observation is information assigned to ... a model"); §3 L1 (Gruber 2026a, §3.6, the FMT paper).
*Problem.* The §5 premise can be derived from inside the paper, from §2's "anything D uses in a check is admitted input". Relying on an unpublished-imprint German monograph invites a referee's objection that it need not face. The FMT citation is not load-bearing, but it sits in the central unconditional argument, which the no-FMT-dependence ruling makes unwise.
*Fix.* Ground the §5 step in §2 and L2, and keep Gruber 2015 only as the source of the terminology. Move Gruber 2026a to a note or drop it; that also frees a self-citation slot.

**N12. [MINOR] Length.**
The paper is at 8,988 words, 12 words under the 9,000 cap. N1–N7 add roughly 300–450 words. Candidate cuts: the §5 earth paragraph (keep the auxiliaries, cut the geoid history) and the §7 endophysics paragraph.

## 4. What holds up

These parts are sound after revision:
- the L2 core and its Albert framing;
- the two-axis taxonomy, apart from where Breuer is placed;
- the logical-versus-operational distinction in §6;
- the dialetheist scope condition, now fair to Priest;
- the Duhem–Quine concession and the monotonicity statement of inheritance;
- the Moore and Putnam contrasts;
- the self-application paragraph;
- all the formal statements checked in round one (Rosser form, Q, Presburger and Skolem arithmetic, the Kolmogorov fraction bound, the Rule 90 closed form, the Israeli–Goldenfeld restriction, Cole's factors).

Once the abstract and §8 state the token reading of L1 plainly and §6 stops claiming more for it, the paper's central claim, that the limits travel as refutations, stands.
