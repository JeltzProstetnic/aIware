# Prior art and citation check: Paper 1 ("No Outside", limits of embedded description)

Compiled 2026-10-18 (aIware, WSL). Metadata was checked against Crossref (`api.crossref.org/works`),
OpenAlex and the arXiv API. "Verified" means the title, authors, year, venue and DOI came back from
a registry record. For books with no DOI, the existence of the edition is confirmed through reviews
that are themselves registered (cited below). Page numbers are given only where a registry returned
them. I have **not** supplied pinpoint page numbers for any quotation; each one has to be taken from
the source itself.

Summaries of what each work argues come from abstracts in the registries (marked [abstract]) or from
standard knowledge of well-known texts (marked [content from standard knowledge, check against the text]).
Treat the second kind as hypotheses to confirm in the text before relying on them.

---

## A. Candidate neighbours

### A1. Graham Priest: inclosure schema and dialetheism

- **Priest, G. (1995). *Beyond the Limits of Thought*. Cambridge: Cambridge University Press.** First
  edition confirmed through reviews: Dale, *Philosophy* 71(276), 308–310 (1996), doi:10.1017/s0031819100041528,
  and Thomas, *Bull. Hegel Soc. GB* 17(2), 80–82 (1996), doi:10.1017/s0263523200005887.
  2nd expanded ed.: Oxford: Clarendon Press, 2002, doi:10.1093/acprof:oso/9780199254057.001.0001. **Verified.**
- **Priest, G. (1991). "The Limits of Thought — and Beyond." *Mind* 100(399), 361–370.** doi:10.1093/mind/c.399.361. **Verified.**
- **Priest, G. (1994). "The Structure of the Paradoxes of Self-Reference." *Mind* 103(409), 25–34.** doi:10.1093/mind/103.409.25. **Verified.**
- Optional: Priest, G. (2010). "Inclosures, Vagueness, and Self-Reference." *Notre Dame J. Formal Logic* 51(1), 69–84, doi:10.1215/00294527-2010-005. **Verified.**

What it argues [standard knowledge]: the limits of expression, iteration, cognition and conception all
have the "Inclosure Schema" form. A totality Ω, together with a diagonaliser δ that takes any subset
of Ω to an element of Ω outside that subset, produces a contradiction at the limit: δ(Ω) is both inside
and outside Ω. Priest reads this as **transcendence** together with **closure**. He concludes,
dialetheically, that these limit contradictions are *true*. The thinker does get outside, and does so
inconsistently. The 2002 edition extends this to Kant, Hegel, Wittgenstein, Heidegger and Nāgārjuna.

Bearing:
- **(1)–(2): strong structural anticipation.** "A totality whose generator, applied to the totality,
  yields something it cannot contain" is the inclosure schema. "The generator never appears
  completely in what it generates" is close to Priest's closure/transcendence pair. The paper must
  either show that its two unconditional limits (a) and (b) are instances of inclosure or say exactly
  how they differ. One candidate difference: (a) is a regress of holders rather than a diagonal
  contradiction.
- **(4): direct conflict, which is also the paper's best foil.** Priest takes the same limit structure
  and accepts the contradiction. The paper treats contradiction as the mark of failure, so a
  completeness claim is *refuted*. The paper's stated condition, that its refutations reach only
  perspectives that treat contradiction as failure, is essentially a concession to Priest. It should
  be stated as such, with Priest named, and not attributed to "paraconsistent perspectives" in general.
  Note that Priest is a dialetheist. Many paraconsistent logicians are not, and do treat
  contradictions as failures that are merely non-explosive. The paper's "paraconsistent ones are
  outside every refutation" therefore needs tightening: the exemption applies to dialetheists, and
  paraconsistency alone does not confer it.

### A2. Lawvere 1969; Yanofsky 2003

- **Lawvere, F. W. (1969). "Diagonal arguments and cartesian closed categories." In *Category Theory,
  Homology Theory and their Applications II*, Lecture Notes in Mathematics 92, pp. 134–145. Springer.**
  doi:10.1007/bfb0080769. **Verified** (pages and DOI from Crossref; the LNM volume number 92 comes from
  standard knowledge and Crossref did not return it, so check it).
- **Yanofsky, N. S. (2003). "A Universal Approach to Self-Referential Paradoxes, Incompleteness and
  Fixed Points." *Bulletin of Symbolic Logic* 9(3), 362–386.** doi:10.2178/bsl/1058448677. **Verified.**

What they argue [abstract, Yanofsky]: Cantor, Russell, the liar, Gödel, Tarski, Turing and the
recursion theorem all follow from one fixed-point scheme. If an object A can *point-surjectively*
represent all maps A → Y, then every endomap of Y has a fixed point. Contrapositively, if Y has a
fixed-point-free endomap (such as negation), no object can fully represent its own family of
predicates.

Bearing:
- **(2): this is the formal version of the unifying principle.** "It can appear in part (Gödel
  numbering), but complete appearance costs consistency" is very nearly the contrapositive of
  Lawvere's theorem: partial representation is fine, while point-surjective (complete)
  self-representation together with a fixed-point-free negation is impossible. The paper should not
  present (2) as a new unification of Gödel, Turing and the paradoxes. That unification is Lawvere's.
  What may be new is applying it to *embedded describers of a physical whole* and adding the
  regress-based limit (1a), which is not obviously a diagonal argument. This should be checked
  carefully: can (1a) be rendered in Lawvere's form?
- (1b) the inside-completeness check resembles the halting- and Gödel-type corollaries.

### A3. Wolpert 2008 (and 2001)

- **Wolpert, D. H. (2008). "Physical limits of inference." *Physica D* 237(9), 1257–1281.**
  doi:10.1016/j.physd.2008.03.040; arXiv:0708.1362. **Verified.**
- Precursor: **Wolpert, D. H. (2001). "Computational capabilities of physical systems." *Physical Review E*
  65(1), 016128.** doi:10.1103/physreve.65.016128. **Verified.**

What it argues [abstract]: devices that observe, predict or recollect share one mathematical structure,
which Wolpert calls an "inference device". There are impossibility results that hold *independently of
the physical laws*. Laplace's demon is impossible even in a classical, non-chaotic universe. The results
parallel the halting theorem. "No universe can contain more than one strong inference device", and
inference complexity is defined by analogy with Kolmogorov complexity.

Bearing: **the closest formal anticipation of (1) in physics.** It is law-independent (matching
"unconditional"), it applies to devices inside the universe they infer about, and it connects the
result to Turing and Kolmogorov. The paper must engage Wolpert directly and say what its limits add.
Plausible additions: the regress about holding one's *own current generation* as content, and the
certification-of-completeness limit framed epistemically. Wolpert's results concern predicting
arbitrary questions, so (1a) is not literally his theorem, but a referee will see the family
resemblance.

### A4. Breuer 1995 (and 1996)

- **Breuer, T. (1995). "The Impossibility of Accurate State Self-Measurements." *Philosophy of Science*
  62(2), 197–214.** doi:10.1086/289852. **Verified.**
- **Breuer, T. (1996). "Subjective decoherence in quantum measurements." *Synthese* 107(1), 1–17.**
  doi:10.1007/bf00413900. **Verified.**

What it argues [abstract]: an observer cannot distinguish all present states of a system that contains
it. This holds classically and quantum-mechanically, for deterministic and stochastic dynamics alike.
A corollary is that an observer cannot measure the EPR correlations between itself and an outside
system. The paper draws consequences for how universally valid theories must be understood.

Bearing: **direct anticipation of (1a) in measurement form.** "No perspective holds its own current
generation, as a whole, as content" is close to "no observer can distinguish all states of a system
containing it." Breuer's argument is a counting/injectivity argument (the observer's states are a
proper part), so it also touches the *capacity* limit. The paper's claim that (1a) is unconditional and
regress-based has to be set against this. Breuer's result is likewise independent of the dynamics.

### A5. Popper 1950 on self-prediction

- **Popper, K. R. (1950). "Indeterminism in Quantum Physics and in Classical Physics. Part I."
  *BJPS* 1(2), 117–133**, doi:10.1093/bjps/i.2.117; **Part II, *BJPS* 1(3), 173–195**,
  doi:10.1093/bjps/i.3.173. **Verified.**

What it argues [standard knowledge]: a "predictor" that is part of the world it predicts cannot fully
predict its own future states, or the results of its own predictions, from within. This yields
indeterminism even in classical physics, through self-reference and Gödel/Tarski-style considerations.

Bearing: **historical anticipation of (1a)/(1b).** Popper is the earliest philosophical statement of
the "describer inside the described" limit. It is related to MacKay's argument (A11). Cite it as the
origin of the line that Breuer and Wolpert formalise.

### A6. Nagel 1986

- **Nagel, T. (1986). *The View from Nowhere*. New York: Oxford University Press.** No DOI for the
  monograph. Existence confirmed through the review by Lauder, *The Thomist* (1987),
  doi:10.1353/tho.1987.0056, and Avramides (2006), "Thomas Nagel: *The View From Nowhere*," in
  *Central Works of Philosophy*, doi:10.1017/upo9781844653621.013. **Verified (edition); no page numbers supplied.**

What it argues [standard knowledge]: objectivity is a matter of degree, reached by stepping back from
a perspective and including it in a more detached conception. The process cannot be completed: the
fully objective view leaves out the subjective standpoint, and no view is *from nowhere*. Nagel stays a
realist, holding that there is more to the world than any view can capture.

Bearing: shares the *conclusion* "no outside view" with (1) and (5). Nagel offers no proof of a limit,
however. His incompleteness is phenomenological and metaphysical. The paper's distinction between
description and instance (5) is a reframing of Nagel's subjective/objective tension: one structure is a
description for a reader and the frame for the one who lives in it. Cite Nagel as the canonical
statement of the problem and position (5) as a structural reading of his "the view from within cannot
be absorbed".

### A7. A. W. Moore 1997

- **Moore, A. W. (1997). *Points of View*. Oxford: Clarendon Press** (xiii + 313 pp.). Existence
  confirmed through Bunnin's review, *Philosophy* (1999), doi:10.1017/s0031819199230306. OUP online
  doi:10.1093/0198250622.001.0001 (Crossref dates the online version 2000). **Verified.**
- Do not confuse it with Moore's earlier article "Points of View," *Philosophical Quarterly* (1987),
  doi:10.2307/2220058.

What it argues [standard knowledge]: Moore *defends* the possibility of **absolute representations**,
representations from no point of view, against Nagel-style and Wittgensteinian doubts. He argues that
we have **ineffable** knowledge (in a qualified, "shown not said" sense) of the limits that perspectival
representation cannot state.

Bearing: **direct conflict with (1)/(4), and the most important philosophical opponent.** Moore holds
that absolute representation is possible. The paper denies that anyone holds positive truth from
nowhere. Moore's appeal to ineffable knowledge is also an alternative answer to the self-application
problem that (4) addresses. Where the paper says "the limits travel as refutations, not as positive
truths", Moore says "the limits are known ineffably". Engaging Moore here gives (4) a sharp contrast.

### A8. Self-refutation literature (Burnyeat, Passmore, Mackie, Castagnoli)

- **Burnyeat, M. F. (1976). "Protagoras and Self-Refutation in Plato's Theaetetus." *Philosophical
  Review* 85(2), 172–195.** doi:10.2307/2183729. **Verified** (Crossref returns start page 172. The end
  page 195 is from standard knowledge, so check it).
- **Passmore, J. (1961). *Philosophical Reasoning*. London: Duckworth** (ch. 4 on self-refutation).
  Existence confirmed through reviews (Gettier, *Phil. Review* 74(2), 1965, doi:10.2307/2183277).
  **Verified edition; the chapter number is from standard knowledge, so check it.**
- **Mackie, J. L. (1964). "Self-Refutation — A Formal Analysis." *Philosophical Quarterly* 14(56), 193–203.**
  doi:10.2307/2955461. **Verified** (start page 193 from Crossref; the end page is not verified).
- **Castagnoli, L. (2010). *Ancient Self-Refutation*. Cambridge: CUP.** Confirmed through Barnes's
  review, *Mind* 121(482), 478–485 (2012), doi:10.1093/mind/fzs051. Book DOI **UNVERIFIED**.

What it argues: Burnyeat reconstructs the *peritrope* (turning-around). Protagorean relativism refutes
itself once "true for x" is cashed out properly. Mackie distinguishes absolute, pragmatic and
operational self-refutation.

Bearing on (4): the paper's move is a **reverse peritrope**. Instead of showing that a rival's claim
undermines itself, it argues that its *own* limitative claims survive self-application, because they
are held as refutations. Mackie's taxonomy is the right tool. The completeness claim the paper rejects
is "operationally self-refuting": the act of asserting it from inside presupposes the condition it
denies. The paper's limits are not asserted as positive truths and so escape the turnaround. Burnyeat
also shows that the turnaround needs a stable notion of truth, which bears on (3): falsity without
absolute truth must still license the turnaround.

### A9. Svozil; Rössler; endophysics

- **Svozil, K. (1993). *Randomness and Undecidability in Physics*. Singapore: World Scientific.** doi:10.1142/1524. **Verified.**
- **Svozil, K. (1994). "Extrinsic-Intrinsic Concept and Complementarity." In Atmanspacher & Dalenoort (eds.),
  *Inside Versus Outside*, Springer Series in Synergetics 63, pp. 273–288.** doi:10.1007/978-3-642-48647-0_15.
  **Verified** (the series volume number 63 is from standard knowledge; Crossref did not return it).
- **Svozil, K. (2018). *Physical (A)Causality*. Fundamental Theories of Physics 192, Springer.** doi:10.1007/978-3-319-70815-7;
  ch. 1 "Intrinsic and Extrinsic Observation Mode," pp. 3–13. **Verified** (the series number 192 is not verified).
- **Atmanspacher, H. & Dalenoort, G. J. (eds.) (1994). *Inside Versus Outside: Endo- and Exo-Concepts of
  Observation and Knowledge in Physics, Philosophy and Cognitive Science*. Springer.** doi:10.1007/978-3-642-48647-0. **Verified.**
- **Rössler, O. E. (1994). "Endophysics — Descartes Taken Seriously." In *Inside Versus Outside*, pp. 153–161.**
  doi:10.1007/978-3-642-48647-0_9. **Verified.**
- **Rössler, O. E. (1998). *Endophysics: The World as an Interface*. Singapore: World Scientific.** doi:10.1142/3183. **Verified.**
- Background: **Toffoli, T. (1978). "The Role of the Observer in Uniform Systems." In *Applied General Systems
  Research*, pp. 395–400. Springer.** doi:10.1007/978-1-4757-0555-3_29. **Verified.**

What they argue [standard knowledge]: endophysics distinguishes *intrinsic* (endo) descriptions, made by
an observer embedded in a system and using only its resources, from *extrinsic* (exo) ones. Svozil
models this with automaton universes and Moore-type computational complementarity, then derives
undecidability and complementarity-like limits for intrinsic observers. Rössler argues that the world
is given to us only as an *interface* and is observer-relative.

Bearing: **(1) and (5) are squarely inside this programme**, whose name for "No Outside" is "endo
perspective". (5), on description versus instance, is close to the endo/exo distinction, though the
paper's version (the same structure being content for one and frame for another) is somewhat more
specific. The paper must cite the 1994 volume as a whole. Its contribution over endophysics is its
claim of *unconditional* limits (endophysics results are usually model-specific) and the epistemic
treatment of falsity and self-application in (3)–(4), which endophysics does not offer.

### A10. Putnam 1981

- **Putnam, H. (1981). *Reason, Truth and History*. Cambridge: CUP.** doi:10.1017/cbo9780511625398. **Verified.**

What it argues [standard knowledge]: there is no "God's Eye point of view" from which the world's
fixed totality of mind-independent objects could be described. Putnam supports this with model-theoretic
and brains-in-a-vat arguments and proposes internal realism, on which truth is idealised rational
acceptability.

Bearing: shares the "no outside standpoint" premise of (3). It **conflicts** with (3)'s asymmetry
claim, though. Putnam does not conclude that positive truth is unavailable while falsity remains
absolute. He redefines truth epistemically. The paper's position, that falsity relative to admitted
input is absolute and positive match-to-world is unattainable, is a different and more asymmetric
answer to Putnam's starting point. Cite him to make that contrast.

### A11. Further close neighbours found

**For (1)/(2): observer self-reference formalised**
- **Szangolies, J. (2018). "Epistemic Horizons and the Foundations of Quantum Mechanics." *Foundations of
  Physics* 48(12), 1669–1697.** doi:10.1007/s10701-018-0221-9; arXiv:1805.10668. **Verified.** [abstract]
  Szangolies uses *Lawvere's* fixed-point theorem to derive in-principle "epistemic horizons" on what an
  observer can know about a system, and proposes them as the origin of quantum information limits.
  **Very close to (1) together with (2): Lawvere applied to embedded observers.** It must be cited.
- **Dalla Chiara, M. L. (1977). "Logical self reference, set theoretical paradoxes and the measurement problem
  in quantum mechanics." *J. Philosophical Logic* 6(1), 331–347.** doi:10.1007/bf00262066. **Verified.**
  An early link between Gödel/Tarski self-reference and the observer's inability to describe itself.
- **Frauchiger, D. & Renner, R. (2018). "Quantum theory cannot consistently describe the use of itself."
  *Nature Communications* 9, 3711.** doi:10.1038/s41467-018-05739-8. **Verified** (DOI; the article
  number 3711 is from standard knowledge). Optional. It is a physics instance of "complete self-application
  costs consistency".
- **MacKay, D. M. (1960). "On the Logical Indeterminacy of a Free Choice." *Mind* 69(273), 31–40.**
  doi:10.1093/mind/lxix.273.31. **Verified.** An agent cannot be bound to accept a complete prediction of
  its own choice, because that prediction changes the state it describes. This is a cousin of (1a).
- **Grim, P. (1991). *The Incomplete Universe: Totality, Knowledge, and Truth*. Cambridge, MA: MIT Press.**
  Confirmed through reviews (Mendelson, *Phil. Quarterly* 44(176), 1994, doi:10.2307/2219630;
  Yaqub, *Phil. Review* 104(2), 1995, doi:10.2307/2186007). **Verified edition.** [standard knowledge]
  Cantorian arguments show there is no set of all truths and no omniscient knower. This anticipates (1b)
  at the level of totality, and it is the standard reference for "no complete description from anywhere".
- **Rescher, N. (2009). *Unknowability: An Inquiry into the Limits of Knowledge*. Lanham: Lexington (Rowman & Littlefield).**
  doi:10.5040/9781978740181. **Verified.** A survey of unknowable facts; useful framing and optional.
- **Fitch, F. B. (1963). "A Logical Analysis of Some Value Concepts." *J. Symbolic Logic* 28(2), 135–142.**
  doi:10.2307/2271594. **Verified.** The knowability paradox: not every truth can be known. Optional.
- **Ryle, G. (1949). *The Concept of Mind*. London: Hutchinson**, ch. VI, "the systematic elusiveness of
  the 'I'". The Routledge reissue is doi:10.4324/9780203875858. **Verified edition; the chapter is from standard knowledge.**
  The pre-formal ancestor of (1a): a higher-order commentary on one's current act can never include that
  commentary itself. **This is (1a)'s regress almost exactly, and should be cited.**
- Wittgenstein, *Tractatus* 5.63–5.641 (the eye that does not see itself in its visual field). Cite the
  section numbers, which are stable across editions. No DOI is needed.

**For (1b): no inside certification of completeness**
- **Albert, H. (1968). *Traktat über kritische Vernunft*. Tübingen: Mohr (Siebeck).** Confirmed through a
  review in *Schmollers Jahrbuch* 90(1), 67–74 (1970), doi:10.3790/schm.90.1.67. **Verified edition.**
  The Münchhausen trilemma: any final justification ends in regress, circularity or dogmatic stopping.
  (1b)'s dilemma ("hold the remainder, or prove from admitted input") is a specialised form of it.

**For (4): limits held as refutations rather than positive truths**
- **Bartley, W. W. III (1962). *The Retreat to Commitment*. New York: Knopf** (London: Chatto & Windus 1964).
  Confirmed through reviews (Holmer, *J. Religion* 44(2), 1964, doi:10.1086/485659; Jones, *BJPS* 17(2), 1966,
  doi:10.1093/bjps/17.2.153). **Verified edition.** Pancritical rationalism holds every position,
  including rationalism itself, open to criticism instead of justified. Bartley shows the position
  survives self-application *because it claims no positive justification*. **This is the closest
  precedent for (4)'s self-application move.** The paper should say how "limits travel as refutations"
  differs from Bartley's "positions held as criticisable". One candidate difference: the paper's
  refutations are *forced* by input that cannot be dropped, whereas Bartley's are merely available.
- **Transcendental pragmatics and performative contradiction (Apel; Habermas).** Apel, K.-O. (1976), "Das
  Problem der philosophischen Letztbegründung im Lichte einer transzendentalen Sprachpragmatik," in
  B. Kanitschneider (ed.), *Sprache und Erkenntnis*, Innsbruck. **UNVERIFIED** (no registry record found;
  check the bibliographic details in a library catalogue). Apel uses strict reflection: any denial of
  certain presuppositions of argument commits a performative self-contradiction. **This is
  structurally the same move as (4)** ("any perspective claiming completeness contradicts input it cannot
  drop"), but Apel uses it to secure *positive* ultimate foundations, the opposite of what the paper
  concludes. The paper needs a sentence on why retorsion yields only negative results in its setting.
- Kant's antinomies (*KrV* A405ff/B432ff) are the classical "reason that claims the unconditioned whole
  falls into contradiction". Cite them by A/B numbers if they are used.

**For (3): the asymmetry of falsity and truth beyond Popper 1959**
- **Popper, K. R. (1959). *The Logic of Scientific Discovery*. London: Hutchinson** (orig. *Logik der Forschung*, 1935 [1934]).
  The Routledge reissue is doi:10.4324/9780203994627. **Verified edition.**
- **Lakatos, I. (1970). "Falsification and the Methodology of Scientific Research Programmes." In Lakatos &
  Musgrave (eds.), *Criticism and the Growth of Knowledge*, pp. 91–196. CUP.** Reprinted in *The Methodology
  of Scientific Research Programmes* (1978), pp. 8–101, doi:10.1017/cbo9780511621123.003. **The 1978 reprint
  is verified. The 1970 page range is from standard knowledge and is UNVERIFIED.** **Conflict with (3):**
  Lakatos argues that falsification is not conclusive (Duhem–Quine). A refuted system can always protect
  itself by adjusting auxiliaries, and historically refutations are often reversed.
- **Quine, W. V. O. (1951). "Two Dogmas of Empiricism." *Philosophical Review* 60(1), 20–43.** doi:10.2307/2181906.
  **Verified** (start page 20; the end page is from standard knowledge). The holism behind the
  objection. **(3) has to meet this head-on.** The paper's careful wording ("inconsistency between a
  reference system and its own admitted input", "inherited by every successor that *keeps the input*")
  seems built to survive Duhem–Quine: the *inconsistency of the set* is absolute, while *which member is
  false* is not settled. The paper should say this explicitly. The novelty lies in that wording, and
  without it the claim reads as naive falsificationism.
- **Miller, D. (1974). "Popper's Qualitative Theory of Verisimilitude." *BJPS* 25(2), 166–177.** doi:10.1093/bjps/25.2.166. **Verified.**
- **Tichý, P. (1974). "On Popper's Definitions of Verisimilitude." *BJPS* 25(2), 155–160.** doi:10.1093/bjps/25.2.155. **Verified.**
  These two papers show that Popper's attempt to measure progress toward truth by truth and falsity
  content fails. They bear on (3): a theory of falsity that does not need truth must avoid smuggling
  verisimilitude back in.
- **Miller, D. (1994). *Critical Rationalism: A Restatement and Defence*. Chicago: Open Court.** Confirmed
  through Watkins's review, *BJPS* 46(4), 610–616 (1995), doi:10.1093/bjps/46.4.610. **Verified edition.**
  Miller's 2006 *Out of Error* (Routledge, Crossref dates the reissue 2017, doi:10.4324/9781315247465) is
  optional. Miller takes the strongest line that one can have knowledge of falsity without justified
  truth. **The nearest anticipation of (3)'s "falsity without truth".**
- **Musgrave, A. (1999). *Essays on Realism and Rationalism*. Amsterdam: Rodopi (now Brill).** doi:10.1163/9789004665774;
  "Critical Rationalism," pp. 314–350. **Verified.** Optional.
- **Laudan, L. (1981). "A Confutation of Convergent Realism." *Philosophy of Science* 48(1), 19–49.** doi:10.1086/288975.
  **Verified.** The pessimistic meta-induction says positive theoretical claims have a poor track record.
  This is empirical support for the *gradient* half of (3): positive claims reverse more often than
  rejections.
- Negative knowledge (empirical and sociological): **Knorr Cetina, K. (1999). *Epistemic Cultures*.
  Cambridge, MA: Harvard UP.** doi:10.4159/9780674039681 (**verified**), which covers "negative knowledge"
  in high-energy physics. **Gartmeier, M., Bauer, J., Gruber, H., & Heid, H. (2008). "Negative Knowledge:
  Understanding Professional Learning and Expertise." *Vocations and Learning* 1(2), 87–103.**
  doi:10.1007/s12186-008-9006-1 (**verified**; the fourth author, Heid, is from standard knowledge).
  These are peripheral and give only vocabulary.
- Case studies for the gradient prediction: **Oreskes, N. (1999). *The Rejection of Continental Drift*. New York:
  OUP.** doi:10.1093/oso/9780195117325.001.0001 (**verified**). **Thagard, P. (1998). "Ulcers and bacteria I:
  discovery and acceptance." *Stud. Hist. Phil. Biol. & Biomed. Sci.* 29(1), 107–136.**
  doi:10.1016/s1369-8486(98)00006-5 (**verified**). Note that both cases concern *rejections of positive
  claims* that were reversed. That supports the prediction that cheap rejections reverse. It also shows
  that falsity rulings *do* get reversed, which sits uneasily with "absolute falsehood". The paper has to
  separate (i) a logical inconsistency ruling, which is absolute relative to kept input, from (ii) a
  community's *judgement* that a theory was refuted, which is what continental drift and H. pylori
  actually exhibit. The gradient prediction is about (ii), and the absolute claim is about (i). The
  paper must not slide between them.

**Conditional limits (cite the originals)**
- Gödel, K. (1931). "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I."
  *Monatshefte für Mathematik und Physik* 38(1), 173–198. doi:10.1007/bf01700692. **Verified.**
- Turing, A. M. (1937 [read 1936]). "On Computable Numbers, with an Application to the Entscheidungsproblem."
  *Proc. London Math. Soc.* s2-42(1), 230–265. doi:10.1112/plms/s2-42.1.230. **Verified** (Crossref
  dates the volume 1937, and it is commonly cited as 1936).
- Kolmogorov, A. N. (1968). "Three approaches to the quantitative definition of information." *Int. J. Computer
  Mathematics* 2(1–4), 157–168. doi:10.1080/00207166808803030. **Verified** (English translation of the 1965 *Problemy
  Peredachi Informatsii* original; the original's details are UNVERIFIED).
- Chaitin, G. J. (1974). "Information-Theoretic Limitations of Formal Systems." *J. ACM* 21(3), 403–424.
  doi:10.1145/321832.321839. **Verified.**
- Wolfram, S. (2002). *A New Kind of Science*. Champaign, IL: Wolfram Media. No registry DOI was found
  for the book. **Edition from standard knowledge**. Computational irreducibility is in ch. 12.

---

## B. Conclusions

### (i) Novelty and positioning

| Claim | Status | Anticipated by |
|---|---|---|
| (1a) No perspective holds its own current generation as content (regress) | **Anticipated.** The informal regress is Ryle's "systematic elusiveness". The formal measurement version is Breuer 1995, with Popper 1950 and MacKay 1960 on self-prediction. | Ryle 1949; Popper 1950; MacKay 1960; Breuer 1995; Wolpert 2008 |
| (1b) No part certifies its own description of the whole complete | **Largely anticipated** across several literatures, though not in this exact epistemic dilemma form. | Albert 1968 (trilemma); Grim 1991; Wolpert 2008; Gödel's second theorem as the formal analogue |
| (1) The unconditional vs conditional split (capacity, irreducibility, incompleteness as world-dependent) | **Plausibly new as an organising taxonomy.** I found no source that separates exactly these two tiers. This is the most defensible structural contribution. | Partial: Svozil 1993 and Wolpert 2008 both list several of the limits together |
| (2) "The generator never appears completely in what it generates" | **Anticipated formally** by Lawvere 1969 and Yanofsky 2003, and philosophically by Priest's inclosure schema. Applied to embedded observers by Szangolies 2018. | Lawvere; Yanofsky; Priest 1995; Szangolies 2018 |
| (3) Falsity without truth (locally decidable inconsistency, inherited by successors that keep the input) | **The core is anticipated** by critical rationalism (Popper 1959; Miller 1994). The specific "reference system plus admitted input, inherited by successors" formulation, as a *response to Duhem–Quine*, may be new. | Popper; Miller; challenged by Quine 1951 and Lakatos 1970 |
| (3) Gradient prediction (resistance to reversal scales with conversion cost) | **Appears new as a testable prediction.** It is related to Laudan's meta-induction and to Kuhn and Lakatos on entrenchment, but I found no statement of a cost-scaling law. | Laudan 1981 (asymmetry in track record) |
| (4) Limits held as refutations, so the account survives self-application | **The most original-looking move, with two close precedents:** Bartley's pancritical rationalism (survives self-application by claiming no positive justification) and Apel's retorsion (the same performative-contradiction mechanism, used for the opposite purpose). Moore 1997's "ineffable knowledge" is the rival answer and Priest the rival logic. | Bartley 1962; Apel 1976; Mackie 1964; contrast Moore 1997, Priest 1995 |
| (5) Description vs instance is perspectival | **Close to the endo/exo distinction** (Svozil, Rössler, the *Inside Versus Outside* 1994 volume) and to Nagel's subjective/objective tension. The "same structure, content for one and frame for another" framing is a modest refinement. | Svozil 1994; Rössler 1998; Nagel 1986 |

**Recommended positioning.** The article should not claim to discover the limits in (1) or the
unification in (2). Reviewers in logic will know Lawvere/Yanofsky and Priest, and reviewers in
philosophy of physics will know Breuer and Wolpert. Its honest contributions are:

1. **A two-tier taxonomy** that separates unconditional limits (regress, certification) from
   world-conditional ones (Kolmogorov/Chaitin, Wolfram/Turing, Gödel), with the claim that the former
   need no assumption about the world.
2. **A self-application argument (4)** showing that the limitative thesis is not self-refuting.
   This is positioned between Bartley (whose refutations are available) and Apel (whose retorsion is used
   for positive foundations), and against Moore's ineffability and Priest's dialetheism.
3. **A Duhem–Quine-proof formulation of falsity without truth (3)** plus a falsifiable *gradient*
   prediction. The logical inconsistency of a kept input set must be kept distinct from community
   refutation verdicts.

Frame the paper as "what the embedded-observer limits *license epistemically*". The existence of the
limits is the established part. The novelty claims come afterwards.

**Technical flags to fix before submission**
- *Locally decidable* inconsistency: for first-order theories, inconsistency is only semi-decidable
  (by Church/Turing). Either restrict to finite or decidable reference systems, or say "detectable once
  found, and then permanent" instead of "decidable".
- *Paraconsistent exemption*: the exemption is properly for **dialetheists** (Priest). Most
  paraconsistent logics still treat contradictions as defects.
- Check whether (1a) can be cast in Lawvere form. If it can, (1a) and (1b) unify under (2), which is
  elegant but makes the anticipation by Lawvere stronger. If it cannot, say why: a regress is not a
  diagonal.
- Continental drift and H. pylori are reversals of *rejections of positive hypotheses*. Make sure they
  illustrate the gradient and do not count against "absolute falsehood".

### (ii) Minimal reference set (18 items)

1. Priest, G. (1995/2002). *Beyond the Limits of Thought*. CUP / OUP.
2. Priest, G. (1994). "The Structure of the Paradoxes of Self-Reference." *Mind* 103, 25–34.
3. Lawvere, F. W. (1969). "Diagonal arguments and cartesian closed categories." LNM, 134–145.
4. Yanofsky, N. S. (2003). *Bull. Symbolic Logic* 9(3), 362–386.
5. Szangolies, J. (2018). *Found. Phys.* 48, 1669–1697.
6. Popper, K. R. (1950). "Indeterminism in Quantum Physics and in Classical Physics," I–II. *BJPS* 1.
7. Breuer, T. (1995). *Philosophy of Science* 62(2), 197–214.
8. Wolpert, D. H. (2008). *Physica D* 237, 1257–1281.
9. Svozil, K. (1993). *Randomness and Undecidability in Physics*; plus Atmanspacher & Dalenoort (eds.) (1994), *Inside Versus Outside*.
10. Ryle, G. (1949). *The Concept of Mind*, ch. VI.
11. Nagel, T. (1986). *The View from Nowhere*.
12. Moore, A. W. (1997). *Points of View*.
13. Putnam, H. (1981). *Reason, Truth and History*.
14. Grim, P. (1991). *The Incomplete Universe*.
15. Mackie, J. L. (1964). "Self-Refutation — A Formal Analysis." *Phil. Quarterly* 14, 193ff.; and/or Burnyeat (1976).
16. Bartley, W. W. (1962). *The Retreat to Commitment*.
17. Popper (1959) *LSD* and Miller (1994) *Critical Rationalism*.
18. Quine (1951) "Two Dogmas" and Lakatos (1970/1978) "Falsification and the MSRP".

Plus the four technical originals, cited briefly: Gödel 1931, Turing 1936/37, Chaitin 1974 (with
Kolmogorov 1965/68) and Wolfram 2002. Optional additions: Albert 1968, Laudan 1981, Apel (once its
details are verified), MacKay 1960, Rössler 1998 and Frauchiger & Renner 2018.

### UNVERIFIED items (do not cite until checked)
- Apel 1976 (bibliographic details).
- Castagnoli 2010 book DOI (the book exists, confirmed through Barnes's review).
- Lakatos 1970 original page range 91–196.
- Kolmogorov 1965 Russian original details.
- Series volume numbers: LNM 92 (Lawvere), Springer Synergetics 63, FTP 192.
- End pages for Burnyeat (195), Mackie (203) and Quine (43); the start pages are verified.
- Wolfram 2002 (no registry DOI; the edition details are from standard knowledge).
- Every content summary marked [standard knowledge] has to be confirmed against the text, especially
  Moore's absolute representations and ineffability, Popper 1950's self-prediction argument, and
  Bartley's self-application argument.
