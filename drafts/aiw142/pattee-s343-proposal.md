# AIW-142 (1) — Pattee 2001 + Jonas & Kording 2017 → FMT master

Proposal only. Nothing here has been applied to `paper/full/four-model-theory-full.md` or the `.tex`
(both are hand-maintained, so an accepted insertion goes into both). Target: published v20,
DOI 10.5281/zenodo.23477765.

## What was read

| Source | Access | Verified |
|---|---|---|
| Pattee, H.H. (2001). The physics of symbols: bridging the epistemic cut. *BioSystems* 60(1–3), 5–21. | **Full text** (author's copy, casci.binghamton.edu/publications/pattee/pattee.html; matches the journal citation) | Crossref: DOI `10.1016/S0303-2647(01)00104-6`, vol 60, issue 1–3, pp. 5–21, May 2001, sole author Howard H. Pattee |
| Jonas, E. & Kording, K.P. (2017). Could a neuroscientist understand a microprocessor? *PLOS Computational Biology* 13(1), e1005268. | **Abstract in full** (Europe PMC) plus two Discussion sentences via the journal page. The body was not read. | Crossref: DOI `10.1371/journal.pcbi.1005268`, vol 13, issue 1, e1005268, published 2017-01-12, authors Eric Jonas, Konrad Paul Kording |

Neither work is currently cited in the master (checked by grep; the master cites Benjamin & Kording 2023
only).

## What Pattee actually claims (from the full text, section numbers his)

- **The cut.** Evolution requires "a primeval epistemic cut that separates energy-degenerate,
  rate-independent genetic symbols from the rate-dependent dynamics of construction that they control"
  (Abstract). Control runs from quiescent symbol to dynamics; measurement runs the other way, coding a
  dynamical state into quiescent symbols (Abstract, §5).
- **Irreducibility, and its kind.** Following von Neumann's measurement regress: a measuring or
  controlling constraint can be described by the same laws as what it measures, but "if you choose to do
  so you will lose the function of M as a measuring device"; laws "cannot describe the pragmatic function
  of measurement even if they can correctly and completely describe the detailed dynamics" (§9).
  **"This epistemic irreducibility does not imply any ontological dualism"** (§9); the cut "is an
  epistemic necessity, not an ontological condition" (§10).
- **What bridges it.** Non-integrable (non-holonomic) constraints — enzymes, switches, escapements — that
  read a rate-independent memory so as to control rate-dependent dynamics (§8).
- **Semantic closure.** The subject side of the cut needs a further "self-referent condition": genes
  control protein synthesis only through previously synthesised enzymes; he calls this semantic (semiotic)
  closure (§10).
- **What he does not claim.** He states "only … some necessary but by no means sufficient conditions" for
  symbolic control (§5), says of the cut's origin "The origin problem is still a mystery" (§10), and
  mentions the mind–brain cut only as one instance of the general epistemic problem (§5). He offers no
  account of consciousness.

## How the parallel holds, and where the backlog wording overclaims

The inbox note behind AIW-142 reads the explicit self-model as Pattee's *symbol* ("self-referential
closure = symbol = epistemic cut"). Against the text this mapping is inverted. On Pattee's terms the
**symbol side is the quiescent, stored, rate-independent memory**, and the **dynamics side is the running
construction**. In FMT the implicit models are stored structure (weights, connectivity — §3.7.1 level 4)
and the explicit models are running activity ("The explicit self-model is activity rather than stored
structure", §3.4.3). So the faithful mapping is:

| Pattee | FMT |
|---|---|
| rate-independent memory (genome) | implicit models (stored structure) |
| control: memory constrains construction | generation of the explicit models from the implicit ones |
| measurement: dynamics coded into memory | learning: changes at the topological level (§3.7.1) |
| rate-dependent dynamics (phenotype construction) | explicit models — where FMT places phenomenality |
| semantic closure (self-reference on the subject side) | self-referential closure (§3.4.3) |
| cut is epistemic, not ontological | FMT's level properties are *ontologically* level-specific (§3.4.1) |

Three consequences for the insertion:

1. The structural shape is a genuine precedent: two levels, one constraining the other, a function lost
   when the whole is described in the vocabulary of the lower level, and a self-referent closure condition
   on the subject side.
2. Phenomenality sits on Pattee's *dynamics* side, not his symbol side. The insertion must not say the
   self-model "is" a symbol.
3. Pattee supports the irreducibility of function to dynamical description. He explicitly declines the
   ontological reading, so he gives no support to FMT's constitutive reading. The insertion says so.

The backlog's "Pattee's unresolved problem (how rate-dependent dynamics come to constitute a
rate-independent symbol)" is closer to his measurement direction than to his central problem; what he
himself flags as open is the *origin* of the cut and the gap between his necessary conditions and
sufficient ones. The insertion uses his wording.

## Proposed insertion — §3.4.3

**Place:** a new paragraph immediately after the paragraph ending

> "If the asymmetry is only *epistemic*, the question stands. The theory's single bridging commitment is
> the constitutive reading."

and before the paragraph beginning "This commitment is motivated rather than merely posited."

**Text (3 sentences):**

> The two-level shape of this argument has a precedent in theoretical biology. Pattee (2001) argued that
> any system that measures or controls requires an epistemic cut between rate-independent memory and the
> rate-dependent dynamics it constrains, that describing the combined system by dynamical laws alone
> loses the measuring or controlling function even when every physical detail is described correctly,
> and that the subject side of the cut requires a self-referent condition he called semantic closure. The
> implicit/explicit split has this shape, with the stored implicit models on the side of memory and the
> running explicit models, where the theory places phenomenality, on the side of dynamics; Pattee,
> however, holds the cut to be epistemic and not ontological, and states only necessary conditions for
> bridging it, so his argument supports the claim that an outside description does not exhaust what such
> a system does and leaves the constitutive reading as this theory's own commitment.

Register sweep on the insertion: no banned phrases (load-bearing / bite / worth -ing / gate / "not X but
Y" for rhythm / self-narration). "has a precedent" is a plain attribution, not a priority claim. "however"
marks a real disagreement (epistemic vs constitutive), which is content.

**Alternative placement**, if MG prefers it near the ontology rather than the closure argument: §3.4.6,
after "The level distinction is not merely convenient; the regress argument forces it wherever the entire
substrate would have to appear as content within its own simulation." Pattee's own regress (§9, from von
Neumann) is the same form as the §3.4.6 regress, which makes that a natural second anchor. Use one
location, not both.

## Optional — Jonas & Kording 2017, §3.4.5

The closest home in v20 is not §3.4.3 but the decompiler passage in §3.4.5, which already makes the
claim J&K tested: a connectome "is raw substrate parameters rather than an authored abstraction, so the
compact structure a developer reads off ten thousand lines of source would have to be *rediscovered* from
the weights, which is the open problem of neuroscience rather than a decompiler's output."

**Proposed edit** — append to that sentence, before the full stop:

> "…rather than a decompiler's output; applied to a microprocessor whose function is known at every
> level, standard neuroscience analyses revealed structure in the data without recovering its hierarchy
> of information processing (Jonas & Kording, 2017)."

The clause restates the abstract's own finding ("reveal interesting structure in the data but do not
meaningfully describe the hierarchy of information processing in the microprocessor") and claims nothing
from the unread body.

## Reference-list entries (master style)

```
Jonas, E., & Kording, K.P. (2017). Could a neuroscientist understand a microprocessor? *PLOS Computational Biology*, 13(1), e1005268. https://doi.org/10.1371/journal.pcbi.1005268

Pattee, H.H. (2001). The physics of symbols: Bridging the epistemic cut. *BioSystems*, 60(1-3), 5-21. https://doi.org/10.1016/S0303-2647(01)00104-6
```

Alphabetical slots: Jonas after `Johnson, M.K., Hashtroudi…` (currently the last J entry); Pattee after
`Passos-Ferreira, C. & Chalmers…` and before `Pawlak, V., & Kerr…` (Pas < Pat < Paw). Both need `references.bib` entries
and a `verify_references.py --update` run (network, tmux) before the next deposit.

## The "preprint MG stress-tested" (Turing 1936 vs 1952)

**Not identifiable.** The fullest record is `docs/bartl-intake-2026-07-31.md` §"Turing 1936-vs-1952 /
Pattee epistemic-cut", which preserves the preprint's thesis, MG's pushback and the sources it cites, but
not its title, author or location; the cfg inbox-archive entry (line 483) and the backlog item carry the
same summary. A web search for the thesis returned nothing matching. If MG still has the bartl@ email of
2026-07-29, the title is there. Without it the insertion does not cite the preprint, and nothing in it
depends on the preprint.

Not re-verified here, and not used in the insertion: the preprint's HBP figure (€607M, 2013–2023), and
the C. elegans sources in the intake note (White et al. 1986; Ripoll-Sánchez et al. 2023; Randi et al.
2023; Flavell & Gordus 2022; the Levin whitepaper).
