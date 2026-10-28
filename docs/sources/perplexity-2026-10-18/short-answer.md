<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

## Short answer

Some people know this explicitly, most working scientists only half-know it, and your second error type is real and documented. But complex numbers are close to the worst example you could pick for it, and the conclusion that the correct logic is "probably much simpler" doesn't follow.

## Who knows it

- **Philosophers of math and physics** have argued about this for over a century. Formalism (Hilbert), Wittgenstein, instrumentalism vs. realism, Korzybski's "the map is not the territory", and Wigner's "unreasonable effectiveness of mathematics" all circle the question of whether math describes reality or just our way of handling it.
- **Physicists** mostly practice "shut up and calculate." They switch freely between "it's just a model" and "the field is real," depending on mood and funding.
- **Your second error type is a known pattern:**
    - **Epicycles:** the textbook example.
    - **Renormalization:** Dirac hated it, and Feynman called it a "dippy process."
    - **Lakatos's "monster-barring":** patching definitions to save a theorem instead of rethinking it.
    - **Duhem–Quine:** you can always save a theory by adding auxiliary assumptions.
    - **Redhead's "surplus structure":** math in a theory that corresponds to nothing physical, like gauge freedom.

So the idea isn't new. It's just not taught, because it doesn't help anyone pass exams.

## Where your argument breaks

**1. Extensions usually don't poison consistency.** Complex numbers are just pairs of real numbers with a multiplication rule (Hamilton, 1830s). They're consistent if the reals are, and they're a conservative extension: nothing provable about the reals changes. The math stays clean. Where contamination does happen is in the mapping to reality, when people treat mathematical artifacts as physical things. Examples are taking the wavefunction literally, infinities that get subtracted away, and potentials that turn out to be gauge choices.

**2. Complex numbers aren't a patch. They're structure the reals were missing.** They encode rotation and phase, which really exist in oscillations and interference. In quantum mechanics this has been tested: Renou et al. (Nature, 2021), followed by experiments in 2022, showed that real-valued quantum theory (with the standard rules for combining systems) makes different predictions and loses to experiment. So reaching for complex numbers wasn't importing an error. It revealed that the original vocabulary was too poor.

**3. The "simpler correct logic" may not exist in a form your intuition likes.** Human intuition evolved for medium-sized objects. Quantum mechanics has resisted every attempt to make it more intuitive, and Bell's theorem rules out the most natural class of such attempts (local hidden variables). Sometimes the patch is the truth and the intuition is the error. Sometimes it really is an epicycle. The hard part is telling which, and no general method does it.

## Where you're right

- **Math is a language with a built-in proof checker.** You can't say just anything in it, which is its power. But it also shapes what questions you can ask. If your toolkit is differential equations, everything looks like a dynamical system.
- **Formalizing too early locks in bad concepts.** Once something is in equations, the equations get defended instead of the concept getting revisited.
- **Consciousness research is where this bites hardest.** Integrated Information Theory (IIT) is the prime example: elaborate math, Φ, attached to a concept nobody has nailed down conceptually. The critique that it's mathematically rigorous but conceptually arbitrary is essentially your argument. In physics the math is at least checked against experiment, which forces the patches to be honest. In consciousness research that check is mostly missing, so ad hoc constructs survive much more easily.


## The sharper version of your claim

"Math is just a language" undersells it. The defensible version is that every mathematical model includes surplus structure. Some of it corresponds to reality, some is just how the representation works, and the theory itself can't tell you which is which. You only find out from conceptual analysis or experiment.

For your own consciousness work, the practical rule: get the concepts and their logic right first, then formalize. Every new mathematical object you add should either predict something new or be explicitly labeled as bookkeeping. If it does neither, it's an epicycle.

---

# So funny... You know this, and in 2. fall for it yourself, just like the humans on whose output you were trained.

Numbers are supposed to count things linearly. Complex numbers are not numbers and are also not number pairs, they are objects and underlie different rules of computation than numbers. They are mini models. And they mislead physicists into believing rotation and phase are pure mathematics which they are not. Or less so than they think. The fact that we use these mini models instead of numbers just hides the true logic, and it could well be that rotation and phase are not elementary (in fact if the universe is a cellular automaton and the spacetime is a holographic projection of lower dimensional logic or computation, rotation in the strict sense does not exist and phase neither, just oscillators). As far as I understand it has been shown that you can arrive at correct physics without the complex numbers, contrary to what you stated. Or they made a level mistake in both, however saying that real numbered physics "loses" in prediction is an unfair statement, since complex numbered quantum physics is still wrong (as in doesn't predict general relativity and isn't consistent die tominfinities and so on). Also the argument under 3 is wrong because quantum mechanics is not a physical theory and unless we find that we will never know how fundamentally wrong qm actually is and why it matches reality so closely for it's scope - but only for that scope. The fact that maths works so well for physics is STILL just because we are living in a subset of the universe in which simple logic works, or there would be no brains able to survive by predicting likely "futures", while at the same time leaving enough complexity and uncertainty for life and success vs failure to make sense in the first place. Correct me where and if I am wrong.

You're right about the physics I cited, half-right about complex numbers, and wrong in two places. Taking your points in turn:

## Where you're right and I was wrong

**Real-valued quantum mechanics works.** My claim was out of date. The 2021 Renou et al. result assumed that a real-valued theory has to combine systems with the standard tensor product. Since 2025, several groups have dropped that assumption and built real-valued theories that give exactly the same predictions as standard quantum mechanics. Gidney also showed that quantum algorithms can avoid the T gate, the one gate that needs complex numbers. Another paper argues that, with operationally defined source independence, real QM can't be experimentally falsified at all. So I presented a result as settled when it wasn't. That was the error you're pointing at.[^2_1][^2_3][^2_9]

**The interesting twist supports you more than me.** Critics point out that these real formulations are only nominally real. They still carry a complex structure: an operator $J$ with $J^2 = -1$, which they need for energy-conserving time evolution. That's your argument almost exactly. $i$ isn't a number, it's a packaged structure, and you can rename it but not remove it. What survives every reformulation is "something that acts as the generator of a 2D rotation in state space." Whether that is fundamental or emergent from oscillators is exactly the open question.[^2_10]

**Rotation and phase may not be elementary.** In a cellular automaton, continuous rotational symmetry is broken at the lattice scale and only reappears approximately at large scales. That's a legitimate position; 't Hooft has worked on it seriously. A quantum phase is just the state of an oscillator, so your "only oscillators" view and "phase exists" may describe the same thing at different levels.

**Your explanation of why math works is reasonable.** I'd add one thing: math also benefits from survivorship bias. Mathematicians have explored a huge range of consistent structures, and we only remember the ones that turned out to fit physics. Coverage plus selection explains most of Wigner's puzzle.

## Where you're wrong

**1. The line between "numbers" and "objects" doesn't fall where you draw it.** Only the natural numbers count. Negative numbers are already a model (debt, direction), and the reals are much worse: Dedekind cuts, uncountably many, and almost none of them computable. If the universe is a cellular automaton, the real continuum is the big imported fiction, much more than $i$. Complex numbers are literally pairs of reals with a different multiplication, equivalent to 2×2 rotation-scaling matrices. That's the same as your "objects with different rules," so on that point we disagree only about words. Your argument gets stronger if you aim it at the reals instead.

**2. "QM is inconsistent because of infinities" is false.** The infinities live in quantum field theory, the relativistic extension. Non-relativistic QM is mathematically consistent. Not predicting general relativity makes it incomplete, not inconsistent, and GR doesn't predict QM either. Calling QM a framework without a mechanism is fair. Many people agree it's essentially a probability calculus with no ontology (QBism, Hardy's axioms). But that's a different charge.

**3. Bell's theorem doesn't depend on QM being true.** It's a constraint derived from measured correlations, not from the QM formalism. So even if QM turns out to be fundamentally wrong, any underlying theory, your cellular automaton included, has to reproduce those correlations. That leaves three options: nonlocality, superdeterminism, or abandoning something like counterfactual definiteness. 't Hooft's cellular-automaton approach accepts superdeterminism for exactly this reason. That's the actual price of your view, and I'd defend that version of my point 3. The "intuition" phrasing I used was weak.

## Net result

The defensible thesis: physics' complex formalism probably hides an underlying structure. The structure itself, some generator of 2D rotation, is apparently needed, but nothing in the formalism tells you whether it's fundamental or emergent. If you want to build the simpler logic from a cellular automaton, it has three hard constraints:

- **Bell correlations:** you have to choose nonlocality or superdeterminism.
- **Lorentz invariance:** experiments confirm it to extremely high precision, so the automaton must recover it almost perfectly at large scales.
- **The complex structure:** something has to play the role of $J$ for unitary time evolution to work.

Most of the people who want "simpler underlying logic" fail on one of these.

<span style="display:none">[^2_11][^2_12][^2_13][^2_14][^2_15][^2_16][^2_17][^2_18][^2_19][^2_2][^2_20][^2_4][^2_5][^2_6][^2_7][^2_8]</span>

<div align="center">⁂</div>

[^2_1]: http://arxiv.org/abs/2504.02808

[^2_2]: https://www.nature.com/articles/s41586-021-04160-4.pdf

[^2_3]: https://www.quantamagazine.org/physicists-take-the-imaginary-numbers-out-of-quantum-mechanics-20251107/

[^2_4]: https://arxiv.org/pdf/2504.07808.pdf

[^2_5]: https://www.arxiv.org/pdf/2502.20102.pdf

[^2_6]: https://arxiv.org/pdf/2604.19482v1.pdf

[^2_7]: https://arxiv.org/pdf/2610.03644.pdf

[^2_8]: https://inspirehep.net/literature/3178191

[^2_9]: https://arxiv.org/html/2603.19208v1

[^2_10]: https://arxiv.org/html/2609.23041v1

[^2_11]: https://algassert.com/post/2501

[^2_12]: https://ar5iv.labs.arxiv.org/html/2111.15128

[^2_13]: https://physics.aps.org/articles/pdf/10.1103/Physics.15.7

[^2_14]: http://arxiv.org/list/quant-ph/2021-01?skip=350\&show=50

[^2_15]: https://www.arxiv.org/pdf/2504.16838.pdf

[^2_16]: http://arxiv.org/search/quant-ph?searchtype=author\&query=Renou,+M

[^2_17]: https://repositum.tuwien.at/handle/20.500.12708/138464

[^2_18]: https://arxiv.org/pdf/2503.09724v1.pdf

[^2_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8695381/

[^2_20]: https://ar5iv.labs.arxiv.org/html/2506.08091


---

# 1. is my point driven ad extremum and I actually agree. Even worse: some numbers are actually algorithms! Simply multiplying by them does stuff that is way more than multiplication or one could also say algorithms and numbers are exchangeable, meaning we trickmourselves even more. 2. is what I meant to say, I was just a bit clumsy with my words.

Locality is a wild assumption that should be dropped asap. Locality is assuming we are observing ground truth, being a projection from a lower dimension would make locality on our level an absurd assumption.

Non super determinism is also a wild assumption especially for mathematical physicists. They have to assume the possibility of true randomness for qm to work in the first place.

So bells theorem is merely a first strong "Indiz" that these assumptions are not based on good reasons and are probably both wrong, at least one of them though. In any class 4 cellular automaton it should be quite easy to create uncountable many systems that behave on the projected plane exactly the behaviour bells theorem was based on (after all they are turning complete). It just appears wild if you were believing qm to be true physics in the first place.

Cellular automaton physics has come quite far you seem to have overlooked some stuff there.

And what is J and unitary time evolution? Sounds like something we wish for, not something grounded in reality. How many time dimensions are there and how is time even a dimension? All dimensions of spacetime are equal, it's just that we move at the speed of light in the direction of one of these. The whole observable universe does. An asymmetry that should make us reconsider our egocentric view of time in the first place. But I may be missing sth there, analyze, Research and reply.

Your intuitions are mostly ahead of the textbooks, but three of your arguments contain errors that would hurt your case if you built on them. Taking each in turn:

## Numbers as algorithms

Agreed, and this is formally established. Turing's original 1936 paper defined "computable numbers" as exactly that: a number is an algorithm that outputs digits. Multiplying by $e^{i\theta}$ is a rotation operator wearing a number costume.

The punchline helps your cellular-automaton view: almost all real numbers are not computable. No algorithm can produce them. The continuum is mostly made of objects no finite process could ever generate. If the universe is a CA, the real numbers are the deepest fiction in physics, deeper than $i$.

## Locality

You're right at the level of the substrate, but the conclusion needs a precise form.

- Bell's "locality" refers to the spacetime we observe. If emergent spacetime is a projection, CA cells that are neighbors in the substrate don't have to be neighbors in that spacetime. That is simply Bell's nonlocality option. It isn't a loophole, it's the cleanest way out, and mainstream quantum gravity points the same direction. In AdS/CFT, locality in the bulk spacetime is emergent and only approximate.
- One hard constraint remains: no signaling. The nonlocality must never be usable to send messages faster than light at our level. That is measured, not assumed. Any projection has to hide its nonlocality exactly that well, which is a strong, non-trivial restriction on the projection.


## Superdeterminism and randomness

**Correction: quantum mechanics doesn't require true randomness.**

- Bohmian mechanics is fully deterministic and nonlocal.
- Many-worlds is deterministic too.
- Statistical independence is not "true randomness." It only says detector settings aren't correlated with the hidden variables. A deterministic chaotic world gives you that for free.

So the real choice in Bell's theorem is between nonlocality and violating statistical independence. Randomness vs. determinism is a separate axis.

**Where you're right:** dismissing superdeterminism reflexively is poorly justified. Hossenfelder \& Palmer argue the standard objections come from intuitions built on linear, classical systems. Their later "supermeasured" paper argues statistical independence can fail through the geometry of the state space, with no conspiracy between settings and hidden variables. 't Hooft accepts superdeterminism explicitly. Critics like Maudlin argue that his "conservation of ontology" rule is itself nonlocal in Bell's sense.[^3_27][^3_41][^3_45]

**The economy point for your model:** if you already have a nonlocal projection, you don't also need superdeterminism. Dropping one assumption is enough, and you'd be paying twice for the same thing.

## Turing completeness doesn't buy much

- **Countable, not uncountable.** CA rules are finite descriptions, so there are only countably many. That ties back to your own point 1.
- **Existence is trivial; finding the rule isn't.** Any Turing-complete CA can simulate quantum mechanics, so Bell-violating behavior in the projection is guaranteed to exist. But the simulation stores amplitudes globally, which is exactly the nonlocal projection again, and the overhead grows exponentially. The hard problem is a minimal, natural rule from which QM, Lorentz invariance and gravity all emerge without being put in by hand.


## Where CA physics actually stands

You're right that I underplayed this.


| Program | What it achieved | Limitation |
| :-- | :-- | :-- |
| D'Ariano, Perinotti et al. (quantum cellular automata) | Derived the Dirac equation without assuming relativity[^3_1], plus Weyl and Maxwell[^3_3], from unitarity, locality, homogeneity and isotropy. Lorentz symmetry emerges at low energy and is deformed at the Planck scale, which is in principle testable. | The automata are already quantum, so they don't derive QM from classical rules. Free fields only. |
| 't Hooft (cellular automaton interpretation) | Classical ontological states evolving by permutations, with QM as a tool rather than a theory[^3_21], which is very close to your view. | His own conclusion: a convincing model is still lacking[^3_23]. |
| Wolfram model | Quantum gates encoded in multiway rewriting systems[^3_12] (Dec 2025); Gorard's derivations of relativistic properties. | No quantitative predictions yet. |

So free fields from CAs are done. A realistic interacting theory with gravity isn't, in any program.

## What J and unitarity mean

Neither is wishful thinking. Both are the quantum names for things you already believe.

- **Unitary time evolution** means the evolution preserves total probability and is reversible: no information is lost. A reversible CA update is a permutation of states, and a permutation is unitary. 't Hooft's ontological states evolve by exactly such permutations. Unitarity is "reversible deterministic update" written in Hilbert-space language.[^3_22]
- **J** comes from Stone's theorem: any continuous, reversible, probability-preserving evolution has the form $e^{-iHt}$. J is what turns an energy into a rotation in state space. Physically it says every energy eigenstate is an oscillator with frequency $E/\hbar$. 't Hooft's models are literally cogwheels running in periodic orbits.

So your "just oscillators, no fundamental phase" is not an alternative to J. It is the physical content of J. The disagreement is only about whether the continuous version is fundamental or a large-scale approximation of discrete cycles.

## Time

**"All dimensions are equal" is false in relativity.** The spacetime metric has signature $(-,+,+,+)$. That single minus sign is the whole of causality: light cones, the difference between before and after.

**"We all move at c through spacetime"** is a popularization (Brian Greene's). The four-velocity always has magnitude c only because it's defined by differentiating with respect to your own proper time. It's a tautology of the bookkeeping, exactly the kind of mathematical artifact you started this conversation warning about. It also breaks for photons, which have no proper time at all.

**Why one time dimension:** Tegmark showed that with more than one, the equations of physics become ultrahyperbolic and ill-posed. Observers could no longer predict anything. That's your own anthropic argument from last round: brains that predict futures need exactly one time direction.[^3_31]

**Is time a dimension?** Your suspicion is correct, but for the opposite reason. In a CA, time isn't a dimension at all. Space is the lattice and time is the computation, the update step. Treating time as a fourth axis is a representation, and the minus sign in the metric is what's left of the fact that time is fundamentally different from space, not equal to it. The arrow of time then comes from initial conditions or information loss, and 't Hooft derives an arrow from information loss in his models.[^3_29]

## Net result

The defensible version of your view: a reversible, discrete substrate in which time is the update and space is emergent. Observed locality is a property of the projection, not of the substrate. QM, J and unitarity are the continuum bookkeeping for discrete reversible oscillators.

Its open debts:

- **No signaling:** the projection must hide its nonlocality perfectly.
- **Lorentz invariance:** it must emerge almost exactly at large scales.
- **A concrete minimal rule** that reproduces interacting fields and gravity, which nobody has produced yet.

The deformed Lorentz symmetry predicted by the quantum-CA models is the most realistic route to an experimental test.

<span style="display:none">[^3_10][^3_11][^3_13][^3_14][^3_15][^3_16][^3_17][^3_18][^3_19][^3_2][^3_20][^3_24][^3_25][^3_26][^3_28][^3_30][^3_32][^3_33][^3_34][^3_35][^3_36][^3_37][^3_38][^3_39][^3_4][^3_40][^3_42][^3_43][^3_44][^3_46][^3_47][^3_48][^3_49][^3_5][^3_50][^3_51][^3_52][^3_53][^3_54][^3_55][^3_56][^3_57][^3_58][^3_59][^3_6][^3_60][^3_61][^3_62][^3_63][^3_64][^3_65][^3_66][^3_67][^3_68][^3_69][^3_7][^3_70][^3_8][^3_9]</span>

<div align="center">⁂</div>

[^3_1]: https://link.aps.org/doi/10.1103/PhysRevA.90.062106

[^3_2]: https://inspirehep.net/literature/1395004

[^3_3]: http://arxiv.org/abs/1601.04832

[^3_4]: https://arxiv.org/pdf/2011.09881.pdf

[^3_5]: https://link.springer.com/content/pdf/10.1007/s11047-019-09762-6.pdf

[^3_6]: http://arxiv.org/pdf/1212.2839v1.pdf

[^3_7]: https://arxiv.org/pdf/1802.03911.pdf

[^3_8]: https://arxiv.org/pdf/1503.02229.pdf

[^3_9]: https://arxiv.org/search/quant-ph?searchtype=author\&query=Perinotti,+P

[^3_10]: https://quantum-journal.org/papers/q-2025-05-28-1756/

[^3_11]: https://www.wolframphysics.org/archives/index?i=Latest

[^3_12]: https://wolframinstitute.org/research/wolfram-physics-project

[^3_13]: https://www.linkedin.com/posts/stephenwolfram_we-also-just-finished-our-2026-wolfram-summer-activity-7485800436357152768-UNtD

[^3_14]: https://www.wolframscience.com/

[^3_15]: https://www.wolframphysics.org/archives/index?i=2026

[^3_16]: https://www.wolframphysics.org/technical-documents/

[^3_17]: https://wolframphysics.org/

[^3_18]: https://writings.stephenwolfram.com/all-by-date/

[^3_19]: https://blog.wolfram.com/author/wolfram-blog-team/

[^3_20]: https://blog.wolfram.com/category/events/

[^3_21]: https://www.arxiv.org/abs/1405.1548

[^3_22]: https://webspace.science.uu.nl/~hooft101/CAQu_Larsfest.pdf

[^3_23]: http://link.springer.com/10.1007/978-3-319-41285-6_10

[^3_24]: https://en.wikipedia.org/wiki/Digital_physics

[^3_25]: https://indico.cern.ch/event/199008/contributions/1481291/attachments/295151/412495/thooft-tam2013.pdf

[^3_26]: https://arxiv.org/html/1308.1007v1

[^3_27]: https://www.math.columbia.edu/~woit/wordpress/?p=9621

[^3_28]: https://link.springer.com/article/10.1134/S0040577923020101

[^3_29]: https://www.rug.nl/research/vsi/events/groenewold/thooft.pdf

[^3_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7515376/

[^3_31]: https://tegmark.org/dimensions.pdf

[^3_32]: https://academic.oup.com/book/35857/chapter/308271802?searchresult=1

[^3_33]: https://ar5iv.labs.arxiv.org/html/1909.01399

[^3_34]: https://www.physics.smu.edu/scalise/P4321/notes/MaxTegmark.pdf

[^3_35]: https://arxiv.org/pdf/0812.0210.pdf

[^3_36]: https://tegmark.org/dimensions.ps

[^3_37]: https://arxiv.org/pdf/2412.02428.pdf

[^3_38]: http://arxiv.org/pdf/0812.3869.pdf

[^3_39]: https://physics.stackexchange.com/questions/129829/why-doesnt-the-number-of-space-dimensions-equal-the-number-of-time-dimensions

[^3_40]: https://arxiv.org/pdf/2606.12457v2.pdf

[^3_41]: https://arxiv.org/abs/1912.06462

[^3_42]: https://agenda.infn.it/event/22106/contributions/113563/attachments/72525/91523/Hossenfelder.pdf

[^3_43]: https://philpapers.org/archive/BAAWDT.pdf

[^3_44]: https://inspirehep.net/literature/2116898

[^3_45]: https://inspirehep.net/files/4a6ebca10b93ef4b645c99dae7f8584d

[^3_46]: https://inspirehep.net/literature/2066122

[^3_47]: https://research-information.bris.ac.uk/ws/portalfiles/portal/444345375/2108.08144v1.pdf

[^3_48]: https://arxiv.org/pdf/2010.01324.pdf

[^3_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9954994/

[^3_50]: https://royalsocietypublishing.org/doi/pdf/10.1098/rspa.2021.0667

[^3_51]: http://arxiv.org/abs/2504.02808

[^3_52]: https://www.nature.com/articles/s41586-021-04160-4.pdf

[^3_53]: https://www.quantamagazine.org/physicists-take-the-imaginary-numbers-out-of-quantum-mechanics-20251107/

[^3_54]: https://arxiv.org/pdf/2504.07808.pdf

[^3_55]: https://www.arxiv.org/pdf/2502.20102.pdf

[^3_56]: https://arxiv.org/pdf/2604.19482v1.pdf

[^3_57]: https://arxiv.org/pdf/2610.03644.pdf

[^3_58]: https://inspirehep.net/literature/3178191

[^3_59]: https://arxiv.org/html/2603.19208v1

[^3_60]: https://arxiv.org/html/2609.23041v1

[^3_61]: https://algassert.com/post/2501

[^3_62]: https://ar5iv.labs.arxiv.org/html/2111.15128

[^3_63]: https://physics.aps.org/articles/pdf/10.1103/Physics.15.7

[^3_64]: http://arxiv.org/list/quant-ph/2021-01?skip=350\&show=50

[^3_65]: https://www.arxiv.org/pdf/2504.16838.pdf

[^3_66]: http://arxiv.org/search/quant-ph?searchtype=author\&query=Renou,+M

[^3_67]: https://repositum.tuwien.at/handle/20.500.12708/138464

[^3_68]: https://arxiv.org/pdf/2503.09724v1.pdf

[^3_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8695381/

[^3_70]: https://ar5iv.labs.arxiv.org/html/2506.08091


---

# We have no way to know if information Transfer on our level is actually impossible given that we have no real GUT I think. After all we know that GR is also wrong or at least incomplete, and also just describes out level of reality.

In a ca based world statistical independence on our level would be hard to achieve, especially in a local experiment.
If I remember correctly there are good arguments against bohemian mechanics.
Many worlds is ridiculous, requires infinity times infinity, not the tiniest piece of evidence that infinity is sth real in the first place, also unscientific.
A ca consists of rules and cells in our limited worldview, but the combination of a mobius-like-quasi-infinite grid like the human brain and co-evolving rules this turns out to be oversimplified.

Any large enough grid-rule-system will produce our world by mere chance with random initial conditions (but that is oversimplified, there is no reason to assume a beginning or end in Möbius infinity- this is human level oversimplification)

The Langton ant is probably even too much to assume, the simple.logic of prime.numbers shows that very little logic can lead to our universe given the correct implementation.

Conserving total probability and reversibility again based on our level of "reality", the carry a lot of weight here and I would question these. Especially reversibility I find weak.

So it seems to me J = BS, same fallacy as all the ones we were talking about. My "oscillations" are an argument against current physics, not FOR a certain simplified view on CAs.

The signature of the spacetime metric is then an assumption needed to make gr work, not a trace of reality.

Analyze and reply again

Several of your points hold up. But one argument keeps recurring, and it's where your reasoning goes wrong, so I'll name it first and then go point by point.

## The recurring move

You keep arguing: "X only holds at our level, so X is an assumption, so X is BS." That doesn't follow.

A law that holds at our level is compressed data, not an assumption. The fallacy we identified earlier was reification: mistaking that compression for the fundamental thing. Using it is not the fallacy. If you throw out every regularity that only holds at our level, your cellular-automaton (CA) universe has nothing left to reproduce. Then it can't be tested, which is the same charge you level at many-worlds.

So the productive move is: list the regularities we observe, deny that they're fundamental, and find a substrate that reproduces them. With that in mind:

## Signaling: you're right, and it's testable

You can't prove no-signaling. A CA also has something relativity lacks: a preferred frame, the lattice. With a preferred frame, faster-than-light signals cause no paradoxes.

There's a concrete theorem in your favor. Bancal et al. (Nature Physics 2012) showed that any model explaining Bell correlations through hidden influences moving at a finite speed, even far faster than light, predicts correlations that could be used to signal faster than light. So your framework faces a fork:[^4_2]

- **Influences propagate at a finite speed through the lattice.** Then signaling exists in principle, and you can look for it in multi-party experiments.
- **The projection is truly nonlocal.** Nothing propagates, and there's no signaling.

Either way you get a testable prediction. That's the strongest result in this whole thread for your program.

## Statistical independence in a CA

Agreed: in a deterministic local CA, everything with a shared past is correlated. The problem isn't whether correlations exist but what kind. Chaotic mixing generically washes correlations out, which is why randomized trials work.

Superdeterminism needs one specific correlation, the exact quantum statistics, and it has to hold no matter how the settings are chosen: humans, random number generators, or quasar light. The cosmic Bell test chose settings from quasar light emitted at least 7.8 billion years ago. Any local mechanism would have to be at least that old, and that experiment excludes it from 96% of the experiment's past light cone. That's not impossible, but it's not generic CA behavior either. The Hossenfelder/Palmer "supermeasured" idea is the serious attempt to explain how it could happen without fine-tuning.[^4_11][^4_75]

## Bohm and many-worlds

**Bohm:** Yes, there are good objections:

- The nonlocality is explicit, with a hidden preferred frame.
- It has trouble with particle creation in quantum field theory.
- "Empty" pilot waves keep existing after the particle has gone elsewhere.
- The wave acts on particles, but particles never act back on it.

But I only used Bohm as a counterexample to "QM requires true randomness." For that it only has to be consistent, not true.

**Many-worlds:** Your infinity argument fails. Many-worlds is standard QM minus the collapse postulate, so it adds no structure. The number of branches isn't even well defined, and in a finite-dimensional state space it's finite. By your own principle of not bolting on objects to fix the math, collapse is the bolted-on object and many-worlds is the cleanup. Its real weaknesses are the Born rule and the preferred basis problem. "Unscientific" applies equally to 't Hooft's CA interpretation as long as it predicts no deviations from QM.

## Your Möbius grid

**An infinity consistency check.** You reject infinity for many-worlds, then use "Möbius quasi-infinity, no beginning or end" for your own model. You have to choose:

- **Truly infinite:** you're using what you rejected.
- **Finite but unbounded** (like a torus or Möbius strip): this is fine, but it has consequences. In a finite deterministic system, every trajectory eventually ends up in a cycle.

**"Any large enough grid produces our world by chance"** has two problems:

- **Most rules produce nothing.** Most CA rules settle into dead or periodic behavior (Wolfram's classes 1 and 2).
- **The Boltzmann-brain problem.** With random initial conditions, small fluctuations that produce a lone observer are overwhelmingly more likely than a whole low-entropy universe like ours. Our universe is far more ordered than an observer needs, which counts as evidence against pure chance.

**Co-evolving rules:** That's legitimate, and Wolfram's rewriting systems go that way. But rules that evolve need meta-rules for how they evolve, and that regress has to stop at some fixed logic. The brain analogy shows the same thing: synaptic plasticity is itself governed by fixed biochemistry.

## Primes

Better than you might think. The spacing statistics of the Riemann zeta zeros match the eigenvalues of random Hermitian matrices. Those are the same statistics as the energy levels of chaotic quantum systems without time-reversal symmetry. Nobody knows why. So very little logic does produce quantum-like structure.[^4_21]

But primes are static. A universe needs dynamics and observers. And "given the correct implementation" is where all the content of your claim hides. That phrase is the whole problem, not a detail.

## Reversibility

Two corrections.

**First, your own framework produces reversibility.** In a finite deterministic system, even with an irreversible rule, every trajectory ends up in a cycle (an attractor). On the cycle, the update is one-to-one, so it's reversible, and probability measure is conserved. A system with no beginning, as you propose, has been on its attractors forever. So reversibility at our level isn't an assumption you have to swallow. It's what your model predicts even if the substrate rule is irreversible. 't Hooft makes a related argument with information loss: the classical states are irreversible while the quantum description built from them is reversible.[^4_59]

**Second, reversibility is not time-reversal symmetry.** Reversible means the update can be inverted. Time-symmetric means the rule looks the same run backward. The zeta zeros above match statistics for systems that are reversible but not time-symmetric. Doubting time symmetry is defensible. Doubting effective reversibility at our level fights both the data and your own model.

Probability conservation isn't physics, it's bookkeeping. Probabilities summing to 1 just means "something happens." If information leaked from our level into the substrate, we'd see it as extra noise. Collapse-model experiments look for exactly that and keep tightening the limits.

## J isn't BS

J as ontology, meaning "rotation in state space is fundamental," can be BS. J as compression, meaning "interference, phase relations and $E = hf$ are measured," is data.

Your "oscillations argue against current physics" also has a problem: quantum field theory is literally coupled harmonic oscillators, so oscillation is what current physics already says. The real disagreement is a continuous phase vs. discrete cycles. That's an argument against the continuum, which is your point 1 again, not against J.

## The metric signature

This one is historically and logically wrong. The signature predates general relativity: it's already in Maxwell's wave equation ($\partial_t^2 - c^2\nabla^2$) and in Minkowski's 1908 geometry. It is what a measured invariant speed of light looks like geometrically.

Your own framework predicts it. A CA has a maximum propagation speed, one cell per step. That creates light cones, and in the continuum limit light cones mean a minus sign in the metric. The quantum-CA program derived Lorentz symmetry without assuming relativity, exactly that way. So the signature is a trace of a substrate with bounded information speed. It's evidence for your kind of world, not against it.[^4_31]

## Where this leaves you

What survives is strong: a finite-but-unbounded discrete substrate, with reversibility and unitarity emerging on attractors, light cones from bounded update speed, and nonlocality living in the projection. And the Bancal result gives you a real test: finite-speed hidden influences imply detectable signaling.

What doesn't survive: calling every regularity at our level a fallacy. That isn't more rigorous than physics. It removes the only data your theory could ever be checked against.

<span style="display:none">[^4_1][^4_10][^4_100][^4_12][^4_13][^4_14][^4_15][^4_16][^4_17][^4_18][^4_19][^4_20][^4_22][^4_23][^4_24][^4_25][^4_26][^4_27][^4_28][^4_29][^4_3][^4_30][^4_32][^4_33][^4_34][^4_35][^4_36][^4_37][^4_38][^4_39][^4_4][^4_40][^4_41][^4_42][^4_43][^4_44][^4_45][^4_46][^4_47][^4_48][^4_49][^4_5][^4_50][^4_51][^4_52][^4_53][^4_54][^4_55][^4_56][^4_57][^4_58][^4_6][^4_60][^4_61][^4_62][^4_63][^4_64][^4_65][^4_66][^4_67][^4_68][^4_69][^4_7][^4_70][^4_71][^4_72][^4_73][^4_74][^4_76][^4_77][^4_78][^4_79][^4_8][^4_80][^4_81][^4_82][^4_83][^4_84][^4_85][^4_86][^4_87][^4_88][^4_89][^4_9][^4_90][^4_91][^4_92][^4_93][^4_94][^4_95][^4_96][^4_97][^4_98][^4_99]</span>

<div align="center">⁂</div>

[^4_1]: https://www.arxiv.org/abs/1110.3795

[^4_2]: https://www.nature.com/articles/nphys2460

[^4_3]: https://link.springer.com/article/10.1007/s10701-014-9785-1?error=cookies_not_supported\&code=f4b9883c-8e87-4965-b1a2-d4632251c624

[^4_4]: https://indico.cern.ch/event/198153/contributions/1480317/attachments/293112/409600/Presentation_ICNFP13.pdf

[^4_5]: https://inspirehep.net/literature/2152469

[^4_6]: https://academic.oup.com/book/36528/chapter/321333331

[^4_7]: https://inspirehep.net/literature/2794254

[^4_8]: https://inspirehep.net/literature/1319444

[^4_9]: https://inspirehep.net/literature/2022759

[^4_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4980107/

[^4_11]: https://arxiv.org/abs/1808.05966

[^4_12]: https://scispace.com/papers/cosmic-bell-test-using-random-measurement-settings-from-high-1yebafsxjc

[^4_13]: https://arxiv.org/search/quant-ph?searchtype=author\&query=Benn,+C

[^4_14]: https://asfriedman.physics.ucsd.edu/CosmicBell/MIT_MKI_03.18.2019.pdf

[^4_15]: https://asfriedman.physics.ucsd.edu/Press/DerStandard_2018.pdf

[^4_16]: https://www.oeaw.ac.at/detail/news/quantenverschraenkung-erstmals-mit-licht-von-quasaren-bestaetigt

[^4_17]: https://asfriedman.physics.ucsd.edu/CosmicBell/UCSD_CASS.04.10.19_Best.pdf

[^4_18]: https://astronomy.sdsu.edu/dr-andrew-friedman-uc-san-diego/

[^4_19]: https://asfriedman.physics.ucsd.edu/Press/Podbregar_Wissenschaft_2018.pdf

[^4_20]: http://arxiv.org/search/quant-ph?searchtype=author\&query=Rauch,+D

[^4_21]: https://www.ias.edu/ideas/2013/primes-random-matrices

[^4_22]: https://arxiv.org/html/2602.04022v1

[^4_23]: https://arxiv.org/pdf/solv-int/9901003.pdf

[^4_24]: https://arxiv.org/pdf/1102.3764.pdf

[^4_25]: https://arxiv.org/pdf/chao-dyn/9412004.pdf

[^4_26]: https://arxiv.org/html/2406.12852v2

[^4_27]: https://arxiv.org/html/0708.4223v1

[^4_28]: https://cims.nyu.edu/~bourgade/papers/PoincareSeminar.pdf

[^4_29]: https://minerva-access.unimelb.edu.au/server/api/core/bitstreams/80919a97-a851-525c-9294-08e9eeb187d0/content

[^4_30]: https://math.uchicago.edu/~may/REU2021/REUPapers/Prodromidis.pdf

[^4_31]: https://link.aps.org/doi/10.1103/PhysRevA.90.062106

[^4_32]: https://inspirehep.net/literature/1395004

[^4_33]: http://arxiv.org/abs/1601.04832

[^4_34]: https://arxiv.org/pdf/2011.09881.pdf

[^4_35]: https://link.springer.com/content/pdf/10.1007/s11047-019-09762-6.pdf

[^4_36]: http://arxiv.org/pdf/1212.2839v1.pdf

[^4_37]: https://arxiv.org/pdf/1802.03911.pdf

[^4_38]: https://arxiv.org/pdf/1503.02229.pdf

[^4_39]: https://arxiv.org/search/quant-ph?searchtype=author\&query=Perinotti,+P

[^4_40]: https://quantum-journal.org/papers/q-2025-05-28-1756/

[^4_41]: https://www.wolframphysics.org/archives/index?i=Latest

[^4_42]: https://wolframinstitute.org/research/wolfram-physics-project

[^4_43]: https://www.linkedin.com/posts/stephenwolfram_we-also-just-finished-our-2026-wolfram-summer-activity-7485800436357152768-UNtD

[^4_44]: https://www.wolframscience.com/

[^4_45]: https://www.wolframphysics.org/archives/index?i=2026

[^4_46]: https://www.wolframphysics.org/technical-documents/

[^4_47]: https://wolframphysics.org/

[^4_48]: https://writings.stephenwolfram.com/all-by-date/

[^4_49]: https://blog.wolfram.com/author/wolfram-blog-team/

[^4_50]: https://blog.wolfram.com/category/events/

[^4_51]: https://www.arxiv.org/abs/1405.1548

[^4_52]: https://webspace.science.uu.nl/~hooft101/CAQu_Larsfest.pdf

[^4_53]: http://link.springer.com/10.1007/978-3-319-41285-6_10

[^4_54]: https://en.wikipedia.org/wiki/Digital_physics

[^4_55]: https://indico.cern.ch/event/199008/contributions/1481291/attachments/295151/412495/thooft-tam2013.pdf

[^4_56]: https://arxiv.org/html/1308.1007v1

[^4_57]: https://www.math.columbia.edu/~woit/wordpress/?p=9621

[^4_58]: https://link.springer.com/article/10.1134/S0040577923020101

[^4_59]: https://www.rug.nl/research/vsi/events/groenewold/thooft.pdf

[^4_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7515376/

[^4_61]: https://tegmark.org/dimensions.pdf

[^4_62]: https://academic.oup.com/book/35857/chapter/308271802?searchresult=1

[^4_63]: https://ar5iv.labs.arxiv.org/html/1909.01399

[^4_64]: https://www.physics.smu.edu/scalise/P4321/notes/MaxTegmark.pdf

[^4_65]: https://arxiv.org/pdf/0812.0210.pdf

[^4_66]: https://tegmark.org/dimensions.ps

[^4_67]: https://arxiv.org/pdf/2412.02428.pdf

[^4_68]: http://arxiv.org/pdf/0812.3869.pdf

[^4_69]: https://physics.stackexchange.com/questions/129829/why-doesnt-the-number-of-space-dimensions-equal-the-number-of-time-dimensions

[^4_70]: https://arxiv.org/pdf/2606.12457v2.pdf

[^4_71]: https://arxiv.org/abs/1912.06462

[^4_72]: https://agenda.infn.it/event/22106/contributions/113563/attachments/72525/91523/Hossenfelder.pdf

[^4_73]: https://philpapers.org/archive/BAAWDT.pdf

[^4_74]: https://inspirehep.net/literature/2116898

[^4_75]: https://inspirehep.net/files/4a6ebca10b93ef4b645c99dae7f8584d

[^4_76]: https://inspirehep.net/literature/2066122

[^4_77]: https://research-information.bris.ac.uk/ws/portalfiles/portal/444345375/2108.08144v1.pdf

[^4_78]: https://arxiv.org/pdf/2010.01324.pdf

[^4_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9954994/

[^4_80]: https://royalsocietypublishing.org/doi/pdf/10.1098/rspa.2021.0667

[^4_81]: http://arxiv.org/abs/2504.02808

[^4_82]: https://www.nature.com/articles/s41586-021-04160-4.pdf

[^4_83]: https://www.quantamagazine.org/physicists-take-the-imaginary-numbers-out-of-quantum-mechanics-20251107/

[^4_84]: https://arxiv.org/pdf/2504.07808.pdf

[^4_85]: https://www.arxiv.org/pdf/2502.20102.pdf

[^4_86]: https://arxiv.org/pdf/2604.19482v1.pdf

[^4_87]: https://arxiv.org/pdf/2610.03644.pdf

[^4_88]: https://inspirehep.net/literature/3178191

[^4_89]: https://arxiv.org/html/2603.19208v1

[^4_90]: https://arxiv.org/html/2609.23041v1

[^4_91]: https://algassert.com/post/2501

[^4_92]: https://ar5iv.labs.arxiv.org/html/2111.15128

[^4_93]: https://physics.aps.org/articles/pdf/10.1103/Physics.15.7

[^4_94]: http://arxiv.org/list/quant-ph/2021-01?skip=350\&show=50

[^4_95]: https://www.arxiv.org/pdf/2504.16838.pdf

[^4_96]: http://arxiv.org/search/quant-ph?searchtype=author\&query=Renou,+M

[^4_97]: https://repositum.tuwien.at/handle/20.500.12708/138464

[^4_98]: https://arxiv.org/pdf/2503.09724v1.pdf

[^4_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8695381/

[^4_100]: https://ar5iv.labs.arxiv.org/html/2506.08091


---

# But we have no true random to use to randomize experiments probing at randomness dependent theories right? And no way to know how tightly coupled we are with any quasar. If there is only one electron...

The Boltzmann brain is one of the most consistent and logical theory of all physics if you ask me.
We actually have evidence for something like this being possible by our own point of view which allows no proof against solipsism and no outside view of anyone else's qualia. Our own local and temporally finite existence may be just one temporary thought of a larger Boltzmann brain mechanism, instantiated similarly for every conscious observer.
Dynamics are not fundamental, they erge as a point of view after the fact. I could in theory reproduce the whole life of a c. elegans in silico and no matter how often I instantiate it, no matter in which time direction I run it, and even if I just statically lay out each time step on a storage medium, if it has consciousness, interrogating it at any point would result in a spacetime like experience just like mine. I don't think dynamics is fundamental, logic might be all you need. I never questioned apparent, local reversibility on OUR plane.
Read my full most recent FMT preprint on zenodo to update your knowledge about consciousness and put it all together. What remains should go into a brief for Claude code and include also the full thread of this conversation verbatim.

Ran cd fmt; rg -n -o ".{0,350}(in the doing|thermodynamic arrow|Boltzmann|statistically likely|Permutation City|lookup table …

<span style="display:none">[^5_1][^5_10][^5_100][^5_101][^5_102][^5_103][^5_104][^5_105][^5_106][^5_107][^5_108][^5_109][^5_11][^5_12][^5_13][^5_14][^5_15][^5_16][^5_17][^5_18][^5_19][^5_2][^5_20][^5_21][^5_22][^5_23][^5_24][^5_25][^5_26][^5_27][^5_28][^5_29][^5_3][^5_30][^5_31][^5_32][^5_33][^5_34][^5_35][^5_36][^5_37][^5_38][^5_39][^5_4][^5_40][^5_41][^5_42][^5_43][^5_44][^5_45][^5_46][^5_47][^5_48][^5_49][^5_5][^5_50][^5_51][^5_52][^5_53][^5_54][^5_55][^5_56][^5_57][^5_58][^5_59][^5_6][^5_60][^5_61][^5_62][^5_63][^5_64][^5_65][^5_66][^5_67][^5_68][^5_69][^5_7][^5_70][^5_71][^5_72][^5_73][^5_74][^5_75][^5_76][^5_77][^5_78][^5_79][^5_8][^5_80][^5_81][^5_82][^5_83][^5_84][^5_85][^5_86][^5_87][^5_88][^5_89][^5_9][^5_90][^5_91][^5_92][^5_93][^5_94][^5_95][^5_96][^5_97][^5_98][^5_99]</span>

<div align="center">⁂</div>

[^5_1]: https://zenodo.org/records/18367541

[^5_2]: https://zenodo.org/records/18751582

[^5_3]: https://zenodo.org/records/17768670

[^5_4]: https://zenodo.org/records/10076267

[^5_5]: https://zenodo.org/records/19430961

[^5_6]: https://zenodo.org/records/10279664/files/Preprint.pdf

[^5_7]: https://zenodo.org/records/4896787/files/Manuscript-preprint.pdf

[^5_8]: https://zenodo.org/records/17991228

[^5_9]: https://zenodo.org/records/18036610

[^5_10]: https://www.arxiv.org/abs/1110.3795

[^5_11]: https://www.nature.com/articles/nphys2460

[^5_12]: https://link.springer.com/article/10.1007/s10701-014-9785-1?error=cookies_not_supported\&code=f4b9883c-8e87-4965-b1a2-d4632251c624

[^5_13]: https://indico.cern.ch/event/198153/contributions/1480317/attachments/293112/409600/Presentation_ICNFP13.pdf

[^5_14]: https://inspirehep.net/literature/2152469

[^5_15]: https://academic.oup.com/book/36528/chapter/321333331

[^5_16]: https://inspirehep.net/literature/2794254

[^5_17]: https://inspirehep.net/literature/1319444

[^5_18]: https://inspirehep.net/literature/2022759

[^5_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4980107/

[^5_20]: https://arxiv.org/abs/1808.05966

[^5_21]: https://scispace.com/papers/cosmic-bell-test-using-random-measurement-settings-from-high-1yebafsxjc

[^5_22]: https://arxiv.org/search/quant-ph?searchtype=author\&query=Benn,+C

[^5_23]: https://asfriedman.physics.ucsd.edu/CosmicBell/MIT_MKI_03.18.2019.pdf

[^5_24]: https://asfriedman.physics.ucsd.edu/Press/DerStandard_2018.pdf

[^5_25]: https://www.oeaw.ac.at/detail/news/quantenverschraenkung-erstmals-mit-licht-von-quasaren-bestaetigt

[^5_26]: https://asfriedman.physics.ucsd.edu/CosmicBell/UCSD_CASS.04.10.19_Best.pdf

[^5_27]: https://astronomy.sdsu.edu/dr-andrew-friedman-uc-san-diego/

[^5_28]: https://asfriedman.physics.ucsd.edu/Press/Podbregar_Wissenschaft_2018.pdf

[^5_29]: http://arxiv.org/search/quant-ph?searchtype=author\&query=Rauch,+D

[^5_30]: https://www.ias.edu/ideas/2013/primes-random-matrices

[^5_31]: https://arxiv.org/html/2602.04022v1

[^5_32]: https://arxiv.org/pdf/solv-int/9901003.pdf

[^5_33]: https://arxiv.org/pdf/1102.3764.pdf

[^5_34]: https://arxiv.org/pdf/chao-dyn/9412004.pdf

[^5_35]: https://arxiv.org/html/2406.12852v2

[^5_36]: https://arxiv.org/html/0708.4223v1

[^5_37]: https://cims.nyu.edu/~bourgade/papers/PoincareSeminar.pdf

[^5_38]: https://minerva-access.unimelb.edu.au/server/api/core/bitstreams/80919a97-a851-525c-9294-08e9eeb187d0/content

[^5_39]: https://math.uchicago.edu/~may/REU2021/REUPapers/Prodromidis.pdf

[^5_40]: https://link.aps.org/doi/10.1103/PhysRevA.90.062106

[^5_41]: https://inspirehep.net/literature/1395004

[^5_42]: http://arxiv.org/abs/1601.04832

[^5_43]: https://arxiv.org/pdf/2011.09881.pdf

[^5_44]: https://link.springer.com/content/pdf/10.1007/s11047-019-09762-6.pdf

[^5_45]: http://arxiv.org/pdf/1212.2839v1.pdf

[^5_46]: https://arxiv.org/pdf/1802.03911.pdf

[^5_47]: https://arxiv.org/pdf/1503.02229.pdf

[^5_48]: https://arxiv.org/search/quant-ph?searchtype=author\&query=Perinotti,+P

[^5_49]: https://quantum-journal.org/papers/q-2025-05-28-1756/

[^5_50]: https://www.wolframphysics.org/archives/index?i=Latest

[^5_51]: https://wolframinstitute.org/research/wolfram-physics-project

[^5_52]: https://www.linkedin.com/posts/stephenwolfram_we-also-just-finished-our-2026-wolfram-summer-activity-7485800436357152768-UNtD

[^5_53]: https://www.wolframscience.com/

[^5_54]: https://www.wolframphysics.org/archives/index?i=2026

[^5_55]: https://www.wolframphysics.org/technical-documents/

[^5_56]: https://wolframphysics.org/

[^5_57]: https://writings.stephenwolfram.com/all-by-date/

[^5_58]: https://blog.wolfram.com/author/wolfram-blog-team/

[^5_59]: https://blog.wolfram.com/category/events/

[^5_60]: https://www.arxiv.org/abs/1405.1548

[^5_61]: https://webspace.science.uu.nl/~hooft101/CAQu_Larsfest.pdf

[^5_62]: http://link.springer.com/10.1007/978-3-319-41285-6_10

[^5_63]: https://en.wikipedia.org/wiki/Digital_physics

[^5_64]: https://indico.cern.ch/event/199008/contributions/1481291/attachments/295151/412495/thooft-tam2013.pdf

[^5_65]: https://arxiv.org/html/1308.1007v1

[^5_66]: https://www.math.columbia.edu/~woit/wordpress/?p=9621

[^5_67]: https://link.springer.com/article/10.1134/S0040577923020101

[^5_68]: https://www.rug.nl/research/vsi/events/groenewold/thooft.pdf

[^5_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7515376/

[^5_70]: https://tegmark.org/dimensions.pdf

[^5_71]: https://academic.oup.com/book/35857/chapter/308271802?searchresult=1

[^5_72]: https://ar5iv.labs.arxiv.org/html/1909.01399

[^5_73]: https://www.physics.smu.edu/scalise/P4321/notes/MaxTegmark.pdf

[^5_74]: https://arxiv.org/pdf/0812.0210.pdf

[^5_75]: https://tegmark.org/dimensions.ps

[^5_76]: https://arxiv.org/pdf/2412.02428.pdf

[^5_77]: http://arxiv.org/pdf/0812.3869.pdf

[^5_78]: https://physics.stackexchange.com/questions/129829/why-doesnt-the-number-of-space-dimensions-equal-the-number-of-time-dimensions

[^5_79]: https://arxiv.org/pdf/2606.12457v2.pdf

[^5_80]: https://arxiv.org/abs/1912.06462

[^5_81]: https://agenda.infn.it/event/22106/contributions/113563/attachments/72525/91523/Hossenfelder.pdf

[^5_82]: https://philpapers.org/archive/BAAWDT.pdf

[^5_83]: https://inspirehep.net/literature/2116898

[^5_84]: https://inspirehep.net/files/4a6ebca10b93ef4b645c99dae7f8584d

[^5_85]: https://inspirehep.net/literature/2066122

[^5_86]: https://research-information.bris.ac.uk/ws/portalfiles/portal/444345375/2108.08144v1.pdf

[^5_87]: https://arxiv.org/pdf/2010.01324.pdf

[^5_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9954994/

[^5_89]: https://royalsocietypublishing.org/doi/pdf/10.1098/rspa.2021.0667

[^5_90]: http://arxiv.org/abs/2504.02808

[^5_91]: https://www.nature.com/articles/s41586-021-04160-4.pdf

[^5_92]: https://www.quantamagazine.org/physicists-take-the-imaginary-numbers-out-of-quantum-mechanics-20251107/

[^5_93]: https://arxiv.org/pdf/2504.07808.pdf

[^5_94]: https://www.arxiv.org/pdf/2502.20102.pdf

[^5_95]: https://arxiv.org/pdf/2604.19482v1.pdf

[^5_96]: https://arxiv.org/pdf/2610.03644.pdf

[^5_97]: https://inspirehep.net/literature/3178191

[^5_98]: https://arxiv.org/html/2603.19208v1

[^5_99]: https://arxiv.org/html/2609.23041v1

[^5_100]: https://algassert.com/post/2501

[^5_101]: https://ar5iv.labs.arxiv.org/html/2111.15128

[^5_102]: https://physics.aps.org/articles/pdf/10.1103/Physics.15.7

[^5_103]: http://arxiv.org/list/quant-ph/2021-01?skip=350\&show=50

[^5_104]: https://www.arxiv.org/pdf/2504.16838.pdf

[^5_105]: http://arxiv.org/search/quant-ph?searchtype=author\&query=Renou,+M

[^5_106]: https://repositum.tuwien.at/handle/20.500.12708/138464

[^5_107]: https://arxiv.org/pdf/2503.09724v1.pdf

[^5_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8695381/

[^5_109]: https://ar5iv.labs.arxiv.org/html/2506.08091


---

# What remains after reading FMT

I read the complete 167-page FMT v19, including its limitations and open questions. The attached Claude Code brief contains the synthesis, a correction ledger, prioritized work, and the original user–assistant dialogue verbatim, with my earlier errors preserved rather than silently rewritten.[^6_8]

## Where I revise my answer

- **Randomness:** Your objection identifies a genuine limit, but “we cannot certify fundamental randomness without assumptions” is different from “there is no true randomness.” Bell measurement independence concerns the relationship between settings and hidden variables, not whether the universe is deterministic; determinism alone does not establish the relevant dependence.[^6_116]
- **Quasar coupling:** Cosmic Bell experiments constrain specified common-cause explanations under stated assumptions, rather than proving independence from every possible underlying variable. My earlier assertion that everything with a shared deterministic past must be statistically correlated was wrong.[^6_93]
- **Fundamental dynamics:** I should not have answered your static-history argument by insisting that a universe “needs dynamics.” Your own SB-HC4A paper already distinguishes a timeless fixed-point condition on the whole block from its internally experienced process description.[^6_49]

I also overextended the finite-speed hidden-influence result: it constrains a particular class of causal models, not every possible substrate or nonlocal projection. Likewise, bounded propagation is not by itself a derivation of Lorentz geometry; the quantum-automaton construction I cited requires additional assumptions and a specified limiting regime ([D’Ariano and Perinotti](https://link.aps.org/doi/10.1103/PhysRevA.90.062106)).[^6_114]

## The substantive remainder

**The decisive question is not whether time fundamentally flows, but what constitutes an implementation.** A timeless whole containing the relevant dependency structure could potentially satisfy a process-based account without an external clock advancing it. A storage medium encoding a sequence of snapshots does not, merely by containing that sequence, establish that the encoded observer is instantiated.

That distinction matters because FMT explicitly separates a running self-referential computation from its complete description. The brief therefore asks Claude Code to clarify which intrinsic relations make something an instance, without smuggling fundamental temporal flow into the answer.[^6_8]

Two further questions remain:

- **Phenomenality:** FMT already acknowledges that its closure–phenomenality identity is argued for rather than derived, and that the other-minds limitation remains. Architectural and efficiency experiments can constrain its functional commitments, but should not be reported as independently proving experience.[^6_8]
- **Observer selection:** Your temporary-thought proposal is broader than the canonical thermal-fluctuation Boltzmann brain. I cannot rule it out from this discussion, but inability to refute solipsism does not favor that mechanism over alternatives; it still needs an implementation criterion, a generating model, and an observer measure.[^6_92]

The brief turns these into concrete editorial decisions and limited computational tests. It also flags a real synchronization issue between v19’s sufficiency conditions and the companion’s shorter formulation, rather than letting Claude silently choose between them (FMT v19, §3.7.3; in-silico companion, §2).[^6_50][^6_8]

Want me to draft the exact FMT paragraph reconciling “constitutively processual” consciousness with a timeless relational ontology?

<span style="display:none">[^6_1][^6_10][^6_100][^6_101][^6_102][^6_103][^6_104][^6_105][^6_106][^6_107][^6_108][^6_109][^6_11][^6_12][^6_13][^6_14][^6_15][^6_16][^6_17][^6_18][^6_19][^6_2][^6_20][^6_21][^6_22][^6_23][^6_24][^6_25][^6_26][^6_27][^6_28][^6_29][^6_3][^6_30][^6_31][^6_32][^6_33][^6_34][^6_35][^6_36][^6_37][^6_38][^6_39][^6_4][^6_40][^6_41][^6_42][^6_43][^6_44][^6_45][^6_46][^6_47][^6_48][^6_5][^6_51][^6_52][^6_53][^6_54][^6_55][^6_56][^6_57][^6_58][^6_59][^6_6][^6_60][^6_61][^6_62][^6_63][^6_64][^6_65][^6_66][^6_67][^6_68][^6_69][^6_7][^6_70][^6_71][^6_72][^6_73][^6_74][^6_75][^6_76][^6_77][^6_78][^6_79][^6_80][^6_81][^6_82][^6_83][^6_84][^6_85][^6_86][^6_87][^6_88][^6_89][^6_9][^6_90][^6_91][^6_94][^6_95][^6_96][^6_97][^6_98][^6_99]</span>

<div align="center">⁂</div>

[^6_1]: https://zenodo.org/records/23427746

[^6_2]: https://arxiv.org/pdf/1702.00850.pdf

[^6_3]: https://www.newscientist.com/article/mg23331133-200-universes-that-spawn-cosmic-brains-should-go-on-the-scrapheap/

[^6_4]: https://nautil.us/can-many_worlds-theory-rescue-us-from-boltzmann-brains-236559

[^6_5]: https://4gravitons.com/2017/02/10/boltzmann-brains-evil-demons-and-why-its-occasionally-a-good-idea-to-listen-to-philosophers/

[^6_6]: https://www.princeton.edu/~adame/bracketing-and-boltzmann-brains-for-rec/2024-04-15.9-bracketing-and-boltzmann-brains.pdf

[^6_7]: https://philsci-archive.pitt.edu/27059/1/EffectiveRealism_BoltzmannBrains.pdf

[^6_8]: https://static1.squarespace.com/static/6112a75f5429563751a31b7b/t/62d1a0d933eacc792f1dc319/1657905369868/BB.Published.small.pdf

[^6_9]: https://arxiv.org/pdf/1708.00449v1.pdf

[^6_10]: https://philarchive.org/archive/TURTOB-2

[^6_11]: https://preposterousuniverse.com/blog/2013/08/22/the-higgs-boson-vs-boltzmann-brains/

[^6_12]: https://www.alphaxiv.org/abs/1708.00449

[^6_13]: https://philarchive.org/archive/CHEWMI-2

[^6_14]: https://www.studocu.com/en-us/document/university-of-california-santa-cruz/mathematical-methods-in-physics-iii/sean-carroll-why-boltzmann-brains-are-bad-arxiv170200850v1/147429160

[^6_15]: http://schwitzsplinters.blogspot.com/2015/10/against-still-here-reply-to-boltzmann.html

[^6_16]: https://philpapers.org/archive/DOGWIA-6.pdf

[^6_17]: https://onlinelibrary.wiley.com/doi/full/10.1111/phib.12353

[^6_18]: https://onlinelibrary.wiley.com/doi/10.1111/phpr.70014

[^6_19]: https://onlinelibrary.wiley.com/doi/10.1111/phib.12353

[^6_20]: https://philpapers.org/archive/DOGDMT-2.pdf

[^6_21]: https://www.emergentmind.com/topics/boltzmann-brain-hypothesis

[^6_22]: https://arxiv.org/html/2003.11989v4

[^6_23]: https://link.springer.com/article/10.1007/s13194-025-00689-7

[^6_24]: https://www.academia.edu/74646666/Comment_on_Causal_Networks_and_Freedom_of_Choice_in_Bells_Theorem

[^6_25]: https://philarchive.org/archive/BAAWDT

[^6_26]: https://www.reddit.com/r/PhilosophyofScience/comments/14hyt14/superdeterminism_and_interpretations_of_quantum/

[^6_27]: https://ar5iv.labs.arxiv.org/html/2008.00631

[^6_28]: https://www.reddit.com/r/AskPhysics/comments/1ttnl6g/does_bells_theorem_disprove_determinism/

[^6_29]: https://en.wikipedia.org/wiki/Superdeterminism

[^6_30]: http://arxiv.org/pdf/1203.6587.pdf

[^6_31]: https://philarchive.org/archive/BERTFO-61

[^6_32]: https://link.springer.com/article/10.1007/s13194-025-00693-x?error=cookies_not_supported\&code=8d49bfd2-dc08-48f5-b42d-c5849ab373c9

[^6_33]: https://philarchive.org/archive/MENNUC

[^6_34]: https://link.springer.com/article/10.1007/s13194-023-00550-9

[^6_35]: https://plato.stanford.edu/entries/qm-retrocausality/

[^6_36]: https://www.math.ru.nl/~landsman/CatorLandsman.pdf

[^6_37]: http://arxiv.org/pdf/1503.00660.pdf

[^6_38]: https://philarchive.org/archive/BEREMC-3

[^6_39]: https://arxiv.org/html/2604.00311v1

[^6_40]: https://arxiv.org/html/2308.11262v3

[^6_41]: https://ar5iv.labs.arxiv.org/html/1411.4787

[^6_42]: https://zenodo.org/records/23242055

[^6_43]: https://zenodo.org/records/23216263

[^6_44]: https://courses.grainger.illinois.edu/phys513/sp2019/reading/week8/nphys2460.pdf

[^6_45]: https://www.arxiv.org/abs/1110.3795

[^6_46]: https://link.springer.com/chapter/10.1007/978-88-470-5217-8_12?error=cookies_not_supported\&code=339255ef-ffd7-43e8-988a-db46e7fd0352

[^6_47]: https://arxiv.org/pdf/1304.0532.pdf

[^6_48]: https://link.springer.com/book/9783319011820

[^6_49]: https://link.springer.com/article/10.1007/s10701-014-9785-1?error=cookies_not_supported\&code=f4b9883c-8e87-4965-b1a2-d4632251c624

[^6_50]: https://indico.cern.ch/event/198153/contributions/1480317/attachments/293112/409600/Presentation_ICNFP13.pdf

[^6_51]: https://inspirehep.net/literature/3188094

[^6_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6461635/

[^6_53]: https://inspirehep.net/literature/1319444

[^6_54]: https://oak.go.kr/central/journallist/articlepdf.do?article_seq=18740

[^6_55]: https://www.research.ed.ac.uk/files/8403025/Three_challenges_to_Chalmers_on_computational_implementation.pdf

[^6_56]: https://philarchive.org/archive/BARCTO-2

[^6_57]: https://openscholar.huji.ac.il/sites/default/files/oronshagrir/files/computation_implementation_cognition.pdf

[^6_58]: https://hrilab.tufts.edu/publications/scheutzcogsci12chalmers.pdf

[^6_59]: https://arxiv.org/html/2511.16582

[^6_60]: https://web-archive.southampton.ac.uk/cogprints.org/226/index.html

[^6_61]: https://link.springer.com/content/pdf/10.1007/s10670-024-00851-2.pdf?error=cookies_not_supported\&code=7556a989-188a-4903-934b-cb0e3a89ba99

[^6_62]: https://philarchive.org/archive/BISWCC-3

[^6_63]: https://marksprevak.com/pdf/paper/Sprevak---Triviality arguments about implementation.pdf

[^6_64]: https://arxiv.org/abs/2504.02808

[^6_65]: https://plato.stanford.edu/archives/spr2026/entries/spacetime-bebecome/

[^6_66]: https://plato.stanford.edu/archives/win2023/entries/spacetime-bebecome/

[^6_67]: https://plato.stanford.edu/entries/consciousness-temporal/

[^6_68]: https://plato.stanford.edu/archives/sum2026/entries/spacetime-bebecome/

[^6_69]: https://plato.stanford.edu/entries/spacetime-bebecome/

[^6_70]: https://plato.stanford.edu/archives/spr2025/entries/time/

[^6_71]: https://plato.stanford.edu/archives/spr2021/entries/time/

[^6_72]: https://plato.stanford.edu/archives/fall2022/entries/time/

[^6_73]: https://plato.stanford.edu/archives/win2020/entries/time/

[^6_74]: https://plato.stanford.edu/archives/spr2022/entries/time/

[^6_75]: https://www.math.uwo.ca/faculty/khalkhali/files/PresentationAcar.pdf

[^6_76]: https://www.math.nagoya-u.ac.jp/~richard/teaching/s2023/SML_Rafi_1.pdf

[^6_77]: https://arxiv.org/html/1704.03859v1

[^6_78]: https://math.ucr.edu/home//baez/qg-winter2001/qg11.2.html

[^6_79]: https://w3.impa.br/~linares/teoria-espectral-2021/lectures-2021/Lecture Stone's theorem.pdf

[^6_80]: https://en.wikipedia.org/wiki/Stone's_theorem_on_one-parameter_unitary_groups

[^6_81]: https://www.uni-math.gwdg.de/mkohlma/Documents/VL_10.pdf

[^6_82]: https://www.math.lmu.de/~tkoenig/16FA2/16FA2_ex14.pdf

[^6_83]: https://math.ou.edu/~cremling/teaching/lecturenotes/fa-new/ln13.pdf

[^6_84]: https://www.worldscientific.com/doi/pdf/10.1142/9789811211751_0001

[^6_85]: https://arxiv.org/abs/1702.00850

[^6_86]: https://arxiv.org/abs/1808.05966

[^6_87]: https://www.nobelprize.org/prizes/physics/1965/feynman/lecture/

[^6_88]: https://www.nobelprize.org/prizes/physics/1965/feynman/lecture/Quotes:/

[^6_89]: https://www.nobelprize.org/uploads/2018/06/dirac-lecture.pdf

[^6_90]: https://www.nobelprize.org/uploads/2018/06/weinberg-lecture.pdf

[^6_91]: https://www.nobelprize.org/prizes/physics/1936/anderson/lecture/

[^6_92]: https://www.nobelprize.org/prizes/physics/1933/dirac/lecture/

[^6_93]: https://www.nobelprize.org/prizes/themes/the-nobel-prize-in-physics-1901-2000/

[^6_94]: https://www.nobelprize.org/uploads/2018/06/ting-lecture.pdf

[^6_95]: https://www.nobelprize.org/prizes/physics/1965/feynman/other-resources/

[^6_96]: https://www.nobelprize.org/page/59/?np-prize-category=physics

[^6_97]: https://www.einstein-online.info/en/spotlight/changing_places/

[^6_98]: https://www.einstein-online.info/spotlight/rollentausch-von-raum-und-zeit/

[^6_99]: https://www.einstein-online.info/en/blackHoles/

[^6_100]: https://www.einstein-online.info/en/spotlight/singularities_bkl/

[^6_101]: https://www.einstein-online.info/en/spotlight/the-singularity-theorem/

[^6_102]: https://www.einstein-online.info/spotlight/fluginssl/

[^6_103]: https://www.einstein-online.info/spotlight/Rotierende-Schwarze-Loecher-Beobachtungen-und-die-Arbeit-in-der-Allgemeinen-Relativitaetstheorie/

[^6_104]: https://www.einstein-online.info/en/spotlight/accretion/

[^6_105]: https://www.einstein-online.info/en/spotlight/descent_bh/

[^6_106]: https://www.einstein-online.info/en/explandict/cosmic-censorship/

[^6_107]: https://www.nature.com/articles/nphys2460

[^6_108]: https://consc.net/papers/rock.html

[^6_109]: https://arxiv.org/abs/1912.06462


---

# Last argument, just reply, no need to update artifacts or anything: instantiation is not needed. FMT is a theory on our plane of existence, not fundamental. I am arguing the static layout on a disk might be all you need. It is not conscious from.our point of view obviously, as it is just a sequence of bits. But on its own plane of existence any interaction with any other conscious creature in it's plane: both will confirm to each other that they are conscious and experience time.

Yes. I was treating execution in our world as a prerequisite while you were explicitly questioning whether our world’s notion of execution has fundamental significance. On your proposal, the creatures’ interactions are relations within the complete structure, not operations that the disk must physically perform. Their memories, conversations, and apparent succession of events are internally ordered regardless of whether we read the disk, or in which order. If that structure supports experience, their experienced time belongs to those internal relations, not to our computer’s clock. Calling it “merely a description” would then assume the ontological distinction you are disputing, rather than establish it. FMT could describe the organization within their world without prescribing how that world must exist relative to ours.

Their mutual confirmation would not independently prove phenomenality, but neither would that be a special objection to their situation: you already acknowledge that reports cannot give another observer direct access to qualia. The remaining explanatory burden is therefore **which structures have an inside perspective**, not what makes their host substrate run. You would also need an interpretation-independent criterion distinguishing such a structure from an arbitrary reading imposed on unrelated bits; that criterion need not require host-level dynamics. Indeed, if the relational structure itself is sufficient, the disk might be unnecessary too: it would encode the world rather than bring its consciousness into existence. Your argument is consequently stronger than “a static simulation might work.” It is that consciousness could belong to a structured world intrinsically, with execution being only one way that world appears from another level.

<span style="display:none">[^7_1][^7_10][^7_100][^7_11][^7_12][^7_13][^7_14][^7_15][^7_16][^7_17][^7_18][^7_19][^7_2][^7_20][^7_21][^7_22][^7_23][^7_24][^7_25][^7_26][^7_27][^7_28][^7_29][^7_3][^7_30][^7_31][^7_32][^7_33][^7_34][^7_35][^7_36][^7_37][^7_38][^7_39][^7_4][^7_40][^7_41][^7_42][^7_43][^7_44][^7_45][^7_46][^7_47][^7_48][^7_49][^7_5][^7_50][^7_51][^7_52][^7_53][^7_54][^7_55][^7_56][^7_57][^7_58][^7_59][^7_6][^7_60][^7_61][^7_62][^7_63][^7_64][^7_65][^7_66][^7_67][^7_68][^7_69][^7_7][^7_70][^7_71][^7_72][^7_73][^7_74][^7_75][^7_76][^7_77][^7_78][^7_79][^7_8][^7_80][^7_81][^7_82][^7_83][^7_84][^7_85][^7_86][^7_87][^7_88][^7_89][^7_9][^7_90][^7_91][^7_92][^7_93][^7_94][^7_95][^7_96][^7_97][^7_98][^7_99]</span>

<div align="center">⁂</div>

[^7_1]: https://philarchive.org/archive/TURTOB-2

[^7_2]: https://preposterousuniverse.com/blog/2013/08/22/the-higgs-boson-vs-boltzmann-brains/

[^7_3]: https://www.alphaxiv.org/abs/1708.00449

[^7_4]: https://philarchive.org/archive/CHEWMI-2

[^7_5]: https://www.studocu.com/en-us/document/university-of-california-santa-cruz/mathematical-methods-in-physics-iii/sean-carroll-why-boltzmann-brains-are-bad-arxiv170200850v1/147429160

[^7_6]: http://schwitzsplinters.blogspot.com/2015/10/against-still-here-reply-to-boltzmann.html

[^7_7]: https://philpapers.org/archive/DOGWIA-6.pdf

[^7_8]: https://onlinelibrary.wiley.com/doi/full/10.1111/phib.12353

[^7_9]: https://onlinelibrary.wiley.com/doi/10.1111/phpr.70014

[^7_10]: https://onlinelibrary.wiley.com/doi/10.1111/phib.12353

[^7_11]: https://philpapers.org/archive/DOGDMT-2.pdf

[^7_12]: https://www.emergentmind.com/topics/boltzmann-brain-hypothesis

[^7_13]: https://arxiv.org/html/2003.11989v4

[^7_14]: https://link.springer.com/article/10.1007/s13194-025-00689-7

[^7_15]: https://www.academia.edu/74646666/Comment_on_Causal_Networks_and_Freedom_of_Choice_in_Bells_Theorem

[^7_16]: https://philarchive.org/archive/BAAWDT

[^7_17]: https://www.reddit.com/r/PhilosophyofScience/comments/14hyt14/superdeterminism_and_interpretations_of_quantum/

[^7_18]: https://ar5iv.labs.arxiv.org/html/2008.00631

[^7_19]: https://www.reddit.com/r/AskPhysics/comments/1ttnl6g/does_bells_theorem_disprove_determinism/

[^7_20]: https://en.wikipedia.org/wiki/Superdeterminism

[^7_21]: http://arxiv.org/pdf/1203.6587.pdf

[^7_22]: https://philarchive.org/archive/BERTFO-61

[^7_23]: https://link.springer.com/article/10.1007/s13194-025-00693-x?error=cookies_not_supported\&code=8d49bfd2-dc08-48f5-b42d-c5849ab373c9

[^7_24]: https://philarchive.org/archive/MENNUC

[^7_25]: https://link.springer.com/article/10.1007/s13194-023-00550-9

[^7_26]: https://plato.stanford.edu/entries/qm-retrocausality/

[^7_27]: https://www.math.ru.nl/~landsman/CatorLandsman.pdf

[^7_28]: http://arxiv.org/pdf/1503.00660.pdf

[^7_29]: https://philarchive.org/archive/BEREMC-3

[^7_30]: https://arxiv.org/html/2604.00311v1

[^7_31]: https://arxiv.org/html/2308.11262v3

[^7_32]: https://ar5iv.labs.arxiv.org/html/1411.4787

[^7_33]: https://zenodo.org/records/23242055

[^7_34]: https://zenodo.org/records/23216263

[^7_35]: https://courses.grainger.illinois.edu/phys513/sp2019/reading/week8/nphys2460.pdf

[^7_36]: https://www.arxiv.org/abs/1110.3795

[^7_37]: https://link.springer.com/chapter/10.1007/978-88-470-5217-8_12?error=cookies_not_supported\&code=339255ef-ffd7-43e8-988a-db46e7fd0352

[^7_38]: https://arxiv.org/pdf/1304.0532.pdf

[^7_39]: https://link.springer.com/book/9783319011820

[^7_40]: https://link.springer.com/article/10.1007/s10701-014-9785-1?error=cookies_not_supported\&code=f4b9883c-8e87-4965-b1a2-d4632251c624

[^7_41]: https://indico.cern.ch/event/198153/contributions/1480317/attachments/293112/409600/Presentation_ICNFP13.pdf

[^7_42]: https://inspirehep.net/literature/3188094

[^7_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6461635/

[^7_44]: https://inspirehep.net/literature/1319444

[^7_45]: https://oak.go.kr/central/journallist/articlepdf.do?article_seq=18740

[^7_46]: https://www.research.ed.ac.uk/files/8403025/Three_challenges_to_Chalmers_on_computational_implementation.pdf

[^7_47]: https://philarchive.org/archive/BARCTO-2

[^7_48]: https://openscholar.huji.ac.il/sites/default/files/oronshagrir/files/computation_implementation_cognition.pdf

[^7_49]: https://hrilab.tufts.edu/publications/scheutzcogsci12chalmers.pdf

[^7_50]: https://arxiv.org/html/2511.16582

[^7_51]: https://web-archive.southampton.ac.uk/cogprints.org/226/index.html

[^7_52]: https://link.springer.com/content/pdf/10.1007/s10670-024-00851-2.pdf?error=cookies_not_supported\&code=7556a989-188a-4903-934b-cb0e3a89ba99

[^7_53]: https://philarchive.org/archive/BISWCC-3

[^7_54]: https://marksprevak.com/pdf/paper/Sprevak---Triviality arguments about implementation.pdf

[^7_55]: https://arxiv.org/abs/2504.02808

[^7_56]: https://plato.stanford.edu/archives/spr2026/entries/spacetime-bebecome/

[^7_57]: https://plato.stanford.edu/archives/win2023/entries/spacetime-bebecome/

[^7_58]: https://plato.stanford.edu/entries/consciousness-temporal/

[^7_59]: https://plato.stanford.edu/archives/sum2026/entries/spacetime-bebecome/

[^7_60]: https://plato.stanford.edu/entries/spacetime-bebecome/

[^7_61]: https://plato.stanford.edu/archives/spr2025/entries/time/

[^7_62]: https://plato.stanford.edu/archives/spr2021/entries/time/

[^7_63]: https://plato.stanford.edu/archives/fall2022/entries/time/

[^7_64]: https://plato.stanford.edu/archives/win2020/entries/time/

[^7_65]: https://plato.stanford.edu/archives/spr2022/entries/time/

[^7_66]: https://www.math.uwo.ca/faculty/khalkhali/files/PresentationAcar.pdf

[^7_67]: https://www.math.nagoya-u.ac.jp/~richard/teaching/s2023/SML_Rafi_1.pdf

[^7_68]: https://arxiv.org/html/1704.03859v1

[^7_69]: https://math.ucr.edu/home//baez/qg-winter2001/qg11.2.html

[^7_70]: https://w3.impa.br/~linares/teoria-espectral-2021/lectures-2021/Lecture Stone's theorem.pdf

[^7_71]: https://en.wikipedia.org/wiki/Stone's_theorem_on_one-parameter_unitary_groups

[^7_72]: https://www.uni-math.gwdg.de/mkohlma/Documents/VL_10.pdf

[^7_73]: https://www.math.lmu.de/~tkoenig/16FA2/16FA2_ex14.pdf

[^7_74]: https://math.ou.edu/~cremling/teaching/lecturenotes/fa-new/ln13.pdf

[^7_75]: https://www.worldscientific.com/doi/pdf/10.1142/9789811211751_0001

[^7_76]: https://arxiv.org/abs/1702.00850

[^7_77]: https://arxiv.org/abs/1808.05966

[^7_78]: https://www.nobelprize.org/prizes/physics/1965/feynman/lecture/

[^7_79]: https://www.nobelprize.org/prizes/physics/1965/feynman/lecture/Quotes:/

[^7_80]: https://www.nobelprize.org/uploads/2018/06/dirac-lecture.pdf

[^7_81]: https://www.nobelprize.org/uploads/2018/06/weinberg-lecture.pdf

[^7_82]: https://www.nobelprize.org/prizes/physics/1936/anderson/lecture/

[^7_83]: https://www.nobelprize.org/prizes/physics/1933/dirac/lecture/

[^7_84]: https://www.nobelprize.org/prizes/themes/the-nobel-prize-in-physics-1901-2000/

[^7_85]: https://www.nobelprize.org/uploads/2018/06/ting-lecture.pdf

[^7_86]: https://www.nobelprize.org/prizes/physics/1965/feynman/other-resources/

[^7_87]: https://www.nobelprize.org/page/59/?np-prize-category=physics

[^7_88]: https://www.einstein-online.info/en/spotlight/changing_places/

[^7_89]: https://www.einstein-online.info/spotlight/rollentausch-von-raum-und-zeit/

[^7_90]: https://www.einstein-online.info/en/blackHoles/

[^7_91]: https://www.einstein-online.info/en/spotlight/singularities_bkl/

[^7_92]: https://www.einstein-online.info/en/spotlight/the-singularity-theorem/

[^7_93]: https://www.einstein-online.info/spotlight/fluginssl/

[^7_94]: https://www.einstein-online.info/spotlight/Rotierende-Schwarze-Loecher-Beobachtungen-und-die-Arbeit-in-der-Allgemeinen-Relativitaetstheorie/

[^7_95]: https://www.einstein-online.info/en/spotlight/accretion/

[^7_96]: https://www.einstein-online.info/en/spotlight/descent_bh/

[^7_97]: https://www.einstein-online.info/en/explandict/cosmic-censorship/

[^7_98]: https://www.nature.com/articles/nphys2460

[^7_99]: https://consc.net/papers/rock.html

[^7_100]: https://arxiv.org/abs/1912.06462

