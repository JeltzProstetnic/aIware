# AIW-288 — definitional paragraph for "model" (FMT master)

Draft only. No paper file was edited. Responds to Kleiner's objection that "model" must be defined.

## (a) Proposed insertion point

**§3.1 Core Definition, as a new final paragraph**, directly after the paragraph ending:

> "What is unique to consciousness is not the distinction itself but what happens at the computational level: *self-referential closure*, the fact that the system's generated model includes a model of the system generating the model (see Section 3.4)."

and before `#### 3.1.1 Operational Definitions`.

Why there: §3.1 is where the definition of consciousness first uses "model" ("runs a model of itself"), and the next thing the reader meets is Table 1, whose **Model** row (write access, read access, boundary recognition) then reads as the operational form of this paragraph. Mirror it into `paper/full/latex/paper.tex` by hand (the `.tex` is hand-maintained and is not generated from the `.md`).

## (b) The paragraph

> A model, in this theory, is a state or structure *M* of a system, related to a target domain *T* by a mapping *h* from states of *T* to states of *M* that preserves the relations the system acts on, such that *M* can be evaluated: operating on *M* yields states that *h* relates to consequences in *T*, and the evaluation agrees with the target up to an error the system can register (Craik, 1943; Conant & Ashby, 1970). *T* fixes the model's boundary; updating *M* from that error and evaluating it are the write and read access of Table 1. A structure the system cannot evaluate is a data structure, not a model. This is the representational sense (Frigg & Hartmann, 2025), distinct from its model-theoretic sense, a structure in which the sentences of a theory are true (Tarski, 1954). It is the reference system of the 2015 definitions, which the monograph equates with "model" (Gruber, 2015, p. 21); knowledge is information assigned to it (Section 3.6). The four kinds differ in two respects: scope of the target (everything, or the self as a proper part of it) and mode (stored in connectivity and evaluated by substrate processing, or generated as running activity).^[Gruber (2015, p. 21): "Somit können wir die Begriffe Bezugssystem und Modell zumindest für unsere Zwecke gleichsetzen"; the reference system there admits "auch ein Modell oder ein virtuelles System".]

Length: ~200 words in the body including citations (~185 without), plus one footnote.

**LaTeX notes for the mirror:** `$M$`, `$T$`, `$h$` in math mode; citation keys below; footnote as `\footnote{...}` with the German in `\foreignlanguage{ngerman}{...}` if babel ngerman is loaded, otherwise plain quotes.

## (c) Citation verification

| Citation | Verified details | Source of verification | Status |
|---|---|---|---|
| Craik (1943) | Craik, K. J. W., *The Nature of Explanation*, Cambridge University Press, 1943, viii + 123 pp. Passage p. 61: "If the organism carries a 'small-scale model' of external reality and of its own possible actions within its head, it is able to try out various alternatives…" | Crossref: contemporaneous review, Ritchie, *Philosophy* 19(73), 173–174 (1944), doi:10.1017/s0031819100004733, gives title, publisher, year, pagination. Quote and p. 61 confirmed via web search (multiple secondary sources agree). | Bibliographic data verified. Quote verified from secondary sources only; check p. 61 against a physical/scanned copy before submission. No DOI (book). |
| Conant & Ashby (1970) | Conant, R. C., & Ashby, W. R. (1970). Every good regulator of a system must be a model of that system. *International Journal of Systems Science*, 1(2), 89–97. doi:10.1080/00207727008920220 | Crossref record (title, authors, volume, issue, pages, issued 1970-10). Content (the simplest optimal regulator is a homomorphic image of the regulated system; the mapping may lose information) confirmed via secondary sources; T&F abstract page did not render via curl. | Verified (bibliographic). Content claim verified from secondary sources. |
| Frigg & Hartmann (2025) | Frigg, R., & Hartmann, S. "Models in Science", *Stanford Encyclopedia of Philosophy*, first published 27 Feb 2006, substantive revision 2 Apr 2025. https://plato.stanford.edu/entries/models-science/ | Fetched the entry live: authors, dates. Text confirms both senses used in the paragraph: representational models "represent a selected part or aspect of the world, which is the model's target system" (§1), and in logic "a model is a structure … that makes all sentences of a theory true" (§4.1). | Verified. Edition label (e.g. "Summer 2025 Edition", editors Zalta & Nodelman) not confirmed — check the entry's "How to cite" page before finalising. |
| Tarski (1954) | Tarski, A. (1954). Contributions to the theory of models. I. *Indagationes Mathematicae (Proceedings)*, 57, 572–581. doi:10.1016/s1385-7258(54)50074-0 | Crossref record. Parts II (57, 582–588) and III (58, 56–64, 1955) also exist. | Verified (bibliographic). Alternative if a textbook source is preferred: Hodges, "Model Theory", SEP, or Chang & Keisler, *Model Theory* — not verified here. |
| Gruber (2015, p. 21) | Existing entry: Gruber, M. (2015). *Die Emergenz des Bewusstseins*. Self-published. ISBN 9781326652074. Bib key `Gruber2015`. | Quote taken verbatim from `.claude/knowledge/fmt-2015-definitions.md` (extracted from the PDF, page refs re-checked S334). | Verified via project KB; already in the reference list. |

None of Craik, Conant & Ashby, Frigg & Hartmann or Tarski is in `docs/references.md`, the master's reference list, or `paper/full/latex/references.bib` (grep, 2026-10-18).

## (d) New reference-list entries

**Markdown reference list (master's APA-like format, alphabetical placement):**

```
Conant, R.C., & Ashby, W.R. (1970). Every good regulator of a system must be a model of that system. *International Journal of Systems Science*, 1(2), 89-97. https://doi.org/10.1080/00207727008920220

Craik, K.J.W. (1943). *The Nature of Explanation*. Cambridge University Press.

Frigg, R., & Hartmann, S. (2025). Models in science. In *The Stanford Encyclopedia of Philosophy* (substantive revision April 2, 2025). https://plato.stanford.edu/entries/models-science/

Tarski, A. (1954). Contributions to the theory of models. I. *Indagationes Mathematicae (Proceedings)*, 57, 572-581. https://doi.org/10.1016/s1385-7258(54)50074-0
```

**BibTeX (`paper/full/latex/references.bib`, same field layout as existing entries):**

```bibtex
@article{ConantAshby1970,
  author    = {Conant, Roger C. and Ashby, W. Ross},
  title     = {Every good regulator of a system must be a model of that system},
  journal   = {International Journal of Systems Science},
  volume    = {1},
  number    = {2},
  pages     = {89--97},
  year      = {1970},
  doi       = {10.1080/00207727008920220},
}

@book{Craik1943,
  author    = {Craik, Kenneth J. W.},
  title     = {The Nature of Explanation},
  publisher = {Cambridge University Press},
  year      = {1943},
}

@misc{FriggHartmann2025,
  author    = {Frigg, Roman and Hartmann, Stephan},
  title     = {Models in Science},
  howpublished = {The Stanford Encyclopedia of Philosophy},
  year      = {2025},
  note      = {Substantive revision April 2, 2025},
  url       = {https://plato.stanford.edu/entries/models-science/},
}

@article{Tarski1954,
  author    = {Tarski, Alfred},
  title     = {Contributions to the theory of models. {I}},
  journal   = {Indagationes Mathematicae (Proceedings)},
  volume    = {57},
  pages     = {572--581},
  year      = {1954},
  doi       = {10.1016/s1385-7258(54)50074-0},
}
```

Also add the four to `docs/references.md` when the paragraph lands.

## (e) Risks

1. **The master already defines "model" — in Table 1, not in prose.** Row **Model**: "A non-trivial reference system with (1) write access …, (2) read access …, and (3) boundary recognition … (Gruber, 2015)." So the premise "no explicit definition" holds for the running text only. Kleiner's objection still stands, because "reference system" is never defined in the master; the paragraph supplies that and maps the three Table 1 criteria onto it (boundary = *T*, write = update from error, read = evaluation). Consider shortening the Table 1 row to point at §3.1 once the paragraph lands, so the paper does not carry two definitions that could drift apart.
2. **"Structure-preserving mapping" is a new formal commitment.** The master never says homomorphism or structure-preserving. It is the minimum needed for a mathematically stated definition and it adds no empirical claim, but MG should approve it as theory. "Up to an error the system can register" is there so the definition stays compatible with §3.1's statement that the explicit narrative is "filled with interpolations, simplifications, and outright confabulations"; a strict homomorphism would contradict that. Conant & Ashby's homomorphism is lossy as well, which fits.
3. **"Evaluated" versus "run".** The master uses "runs a model" for the explicit, generated side, and calls the implicit models stored structure, not running process. I put "evaluated" in the general clause and kept "running" for the explicit mode. That way pattern #29 (an unevaluable forward model is a data structure) applies to the implicit models too, without saying the IWM/ISM "run". This is consistent with the master's own wording that substrate processing is "guided by the implicit models" (Table 1b), and with the substrate-level forward-model argument in "Why four, not three?". Do not change it back to "run" in the mirror.
4. **"Two respects" and the blending caveat.** §3.2 says real neural models "blend across" the world/self boundary and that the four are "extremal points". The paragraph defines a model by its target domain, which is consistent with that (a blended model just has a mixed target), and it says the *four kinds* differ in two respects, the master's own two dimensions. It also follows §3.2 in treating scope as nesting ("the self as a proper part of it"), not as a disjoint world/self pair.
5. **Knowledge clause.** It restates only what §3.6 already says ("knowledge to be information assigned to a reference system"). I left out the 2015 *Bedeutung* definition (meaning as relation to the reference system) because the master does not carry it. Adding it would bring in a term the paper never uses again.
6. **Craik page/quote** is verified from secondary sources only (see table). The paragraph cites Craik without quoting him, so the risk is limited to the page number if one is added.
7. **Register.** Checked against `prose-register.md`: no self-narration, no throat-clearing, no banned words. One contrast remains ("a data structure, not a model"). It is the definitional exclusion from pattern #29, and removing it changes what the sentence says, so it passes the S320 test. Still run the added-lines density check against the master's baseline when mirroring.
