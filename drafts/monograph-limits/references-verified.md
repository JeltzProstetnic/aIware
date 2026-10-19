<!--
META
purpose: citation verification pass over 00-architecture.md §5 "Permitted references" (S335, 2026-10-18)
method: 4 parallel research agents (Crossref API, OpenAlex API, arXiv, publisher pages) + 2 independent
        spot-checks by the orchestrating session on the flagged Dennett & Kinsbourne and Elga entries.
scope: all 38 non-Gruber entries in §5. The three Gruber self-citations (2015, 2026a, 2026b) were
       excluded from verification per instructions and are carried through unchanged below, marked as such.
-->

# Reference verification — No Outside (monograph-limits), §5

38 of 38 non-Gruber entries checked. **34 OK, 4 CORRECTED, 0 NOT FOUND.**

## Verification table

| Entry (short) | Status | Corrected full reference | DOI | Source URL used |
|---|---|---|---|---|
| Albert (2000) | OK | Albert, D. Z. (2000). *Time and Chance.* Harvard University Press. | none | https://www.hup.harvard.edu/books/9780674011328 |
| Bancal et al. (2012) | OK | Bancal, J.-D., Pironio, S., Acín, A., Liang, Y.-C., Scarani, V., & Gisin, N. (2012). Quantum non-locality based on finite-speed causal influences leads to superluminal signalling. *Nature Physics* 8, 867–870. | 10.1038/nphys2460 | https://doi.org/10.1038/nphys2460 |
| Barbour (1999) | OK | Barbour, J. (1999). *The End of Time.* Oxford University Press. | none | https://en.wikipedia.org/wiki/The_End_of_Time_(book) |
| Bennett (1973) | OK | Bennett, C. H. (1973). Logical reversibility of computation. *IBM Journal of Research and Development* 17, 525–532. | 10.1147/rd.176.0525 | https://doi.org/10.1147/rd.176.0525 |
| Carroll (2017) | OK | Carroll, S. M. (2017). Why Boltzmann brains are bad. arXiv:1702.00850. | 10.48550/arXiv.1702.00850 | https://arxiv.org/abs/1702.00850 |
| Chaitin (1966) | OK | Chaitin, G. J. (1966). On the length of programs for computing finite binary sequences. *Journal of the ACM* 13, 547–569. | 10.1145/321356.321363 | https://doi.org/10.1145/321356.321363 |
| Chalmers (1996) | OK | Chalmers, D. J. (1996). Does a rock implement every finite-state automaton? *Synthese* 108, 309–333. | 10.1007/BF00413692 | https://doi.org/10.1007/BF00413692 |
| Cook (2004) | OK | Cook, M. (2004). Universality in elementary cellular automata. *Complex Systems* 15, 1–40. | 10.25088/ComplexSystems.15.1.1 | https://www.complex-systems.com/abstracts/v15_i01_a01/ (checked against the publisher PDF directly — page-footer reads "Complex Systems, 15 (2004) 1–40") |
| Culik & Yu (1988) | **CORRECTED** | Culik, K., II, & Yu, S. (1988). Undecidability of CA classification schemes. *Complex Systems* 2, 177–190. | none | https://www.complex-systems.com/abstracts/v02_i02_a02/ (checked against the publisher PDF directly) |
| D'Ariano & Perinotti (2014) | OK | D'Ariano, G. M., & Perinotti, P. (2014). Derivation of the Dirac equation from principles of information processing. *Physical Review A* 90, 062106. | 10.1103/PhysRevA.90.062106 | https://doi.org/10.1103/PhysRevA.90.062106 |
| Dennett & Kinsbourne (1992) | **CORRECTED** | Dennett, D. C., & Kinsbourne, M. (1992). Time and the observer: the where and when of consciousness in the brain. *Behavioral and Brain Sciences* 15, 183–201. | 10.1017/S0140525X00068229 | https://api.crossref.org/works/10.1017/S0140525X00068229 |
| Eagleman & Sejnowski (2000) | OK | Eagleman, D. M., & Sejnowski, T. J. (2000). Motion integration and postdiction in visual awareness. *Science* 287, 2036–2038. | 10.1126/science.287.5460.2036 | https://api.crossref.org/works?query.bibliographic=Eagleman+Sejnowski+Motion+integration+and+postdiction+in+visual+awareness |
| Egan (1994) | OK | Egan, G. (1994). *Permutation City.* Millennium. | none | https://isfdb.org/cgi-bin/pl.cgi?25925= |
| Elga (2024) | **CORRECTED** | Elga, A. (2025). Boltzmann brains and cognitive instability. *Philosophy and Phenomenological Research* 111, 127–136. | 10.1111/phpr.70014 | https://onlinelibrary.wiley.com/doi/10.1111/phpr.70014 |
| Feynman (1965) | OK | Feynman, R. P. (1965). The development of the space-time view of quantum electrodynamics. Nobel Lecture. (S339: replaced in the clean list by Feynman 1985 *QED*, the source of "dippy process".) | none | https://www.nobelprize.org/prizes/physics/1965/feynman/lecture/ |
| Geldard & Sherrick (1972) | OK | Geldard, F. A., & Sherrick, C. E. (1972). The cutaneous "rabbit": a perceptual illusion. *Science* 178, 178–179. | 10.1126/science.178.4057.178 | https://api.crossref.org/works?query.bibliographic=Geldard+Sherrick+cutaneous+rabbit+perceptual+illusion |
| Gödel (1931) | OK | Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik* 38, 173–198. | 10.1007/BF01700692 | https://doi.org/10.1007/BF01700692 |
| Hardy (2001) | OK | Hardy, L. (2001). Quantum theory from five reasonable axioms. arXiv:quant-ph/0101012. | 10.48550/arXiv.quant-ph/0101012 | https://arxiv.org/abs/quant-ph/0101012 |
| Hoffreumon & Woods (2025) | OK | Hoffreumon, T., & Woods, M. P. (2025). Quantum theory does not need complex numbers. arXiv:2504.02808. | 10.48550/arXiv.2504.02808 | https://arxiv.org/abs/2504.02808 |
| Hossenfelder & Palmer (2020) | **CORRECTED** | Hossenfelder, S., & Palmer, T. (2020). Rethinking superdeterminism. *Frontiers in Physics* 8:139. | 10.3389/fphy.2020.00139 | https://api.crossref.org/works/10.3389/fphy.2020.00139 |
| Kolers & von Grünau (1976) | OK | Kolers, P. A., & von Grünau, M. (1976). Shape and color in apparent motion. *Vision Research* 16, 329–335. | 10.1016/0042-6989(76)90192-9 | https://api.crossref.org/works?query.bibliographic=Kolers+von+Grunau+shape+color+apparent+motion |
| Kolmogorov (1965) | OK | Kolmogorov, A. N. (1965). Three approaches to the quantitative definition of information. *Problems of Information Transmission* 1, 1–7. | none | https://cir.nii.ac.jp/crid/1573387451193285504 |
| Lakatos (1976) | OK | Lakatos, I. (1976). *Proofs and Refutations.* Cambridge University Press. | none | https://philpapers.org/rec/LAKPAR-8 |
| Minkowski (1908/1909) | OK | Minkowski, H. (1908/1909). Raum und Zeit. *Physikalische Zeitschrift* 10, 104–111. | none | https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=ufn&paperid=12509&option_lang=eng |
| Montgomery (1973) | OK | Montgomery, H. L. (1973). The pair correlation of zeros of the zeta function. *Proceedings of Symposia in Pure Mathematics* 24, 181–193. | 10.1090/pspum/024/9944 | https://api.crossref.org/works?query.bibliographic=Montgomery+pair+correlation+of+zeros+of+the+zeta+function |
| Odlyzko (1987) | OK | Odlyzko, A. M. (1987). On the distribution of spacings between zeros of the zeta function. *Mathematics of Computation* 48, 273–308. | 10.1090/S0025-5718-1987-0866115-0 | https://api.crossref.org/works?query.bibliographic=Odlyzko+distribution+of+spacings+between+zeros+of+the+zeta+function |
| Popper (1959) | OK | Popper, K. R. (1959). *The Logic of Scientific Discovery.* Hutchinson. | none | https://archive.org/details/logicofscientifi00popp |
| Putnam (1988) | OK | Putnam, H. (1988). *Representation and Reality.* MIT Press. | none | https://mitpress.mit.edu/9780262161084/representation-and-reality/ |
| Rauch et al. (2018) | OK | Rauch, D., et al. (2018). Cosmic Bell test using random measurement settings from high-redshift quasars. *Physical Review Letters* 121, 080403. | 10.1103/PhysRevLett.121.080403 | https://api.openalex.org/works?search=Rauch+Cosmic+Bell+test+using+random+measurement+settings+from+high-redshift+quasars |
| Redhead (1975) | OK | Redhead, M. (1975). Symmetry in intertheory relations. *Synthese* 32, 77–112. | 10.1007/BF00485113 | https://api.crossref.org/works?query.bibliographic=Redhead+Symmetry+in+intertheory+relations |
| Renou et al. (2021) | OK | Renou, M.-O., et al. (2021). Quantum theory based on real numbers can be experimentally falsified. *Nature* 600, 625–629. | 10.1038/s41586-021-04160-4 | https://api.openalex.org/works/doi:10.1038/s41586-021-04160-4 |
| Stone (1932) | OK | Stone, M. H. (1932). On one-parameter unitary groups in Hilbert space. *Annals of Mathematics* 33, 643–648. | 10.2307/1968538 | https://api.crossref.org/works?query.bibliographic=Stone+On+one-parameter+unitary+groups+in+Hilbert+space |
| Tegmark (1997) | OK | Tegmark, M. (1997). On the dimensionality of spacetime. *Classical and Quantum Gravity* 14, L69–L75. | 10.1088/0264-9381/14/4/002 | https://api.crossref.org/works?query.bibliographic=Tegmark+On+the+dimensionality+of+spacetime |
| Tegmark (2008) | OK | Tegmark, M. (2008). The mathematical universe. *Foundations of Physics* 38, 101–150. | 10.1007/s10701-007-9186-9 | https://link.springer.com/article/10.1007/s10701-007-9186-9 |
| 't Hooft (2016) | OK | 't Hooft, G. (2016). *The Cellular Automaton Interpretation of Quantum Mechanics.* Springer. | 10.1007/978-3-319-41285-6 | https://link.springer.com/book/10.1007/978-3-319-41285-6 |
| Turing (1936) | OK | Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society* s2-42, 230–265. | 10.1112/plms/s2-42.1.230 | https://api.crossref.org/works?query.bibliographic=Turing+On+computable+numbers+with+an+application+to+the+Entscheidungsproblem |
| Wigner (1960) | OK | Wigner, E. P. (1960). The unreasonable effectiveness of mathematics in the natural sciences. *Communications on Pure and Applied Mathematics* 13, 1–14. | 10.1002/cpa.3160130102 | https://api.crossref.org/works?query.bibliographic=Wigner+unreasonable+effectiveness+of+mathematics |
| Wolfram (2002) | OK | Wolfram, S. (2002). *A New Kind of Science.* Wolfram Media. | none | https://api.openalex.org/works?search=Wolfram%20A%20New%20Kind%20of%20Science |

## Notes on individual findings

- **Culik & Yu (1988):** title ("Undecidability of CA Classification Schemes"), volume (2), and pages (177–190)
  are all correct exactly as drafted — read directly off the publisher PDF, not a secondary citation. The one
  real error is the first author's name: he is **Karel Culik II** — "II" is part of his name, not an edition
  marker — so "Culik, K." should read "Culik, K., II". ACM's Digital Library lists a `10.5555/…` identifier for
  this paper, but that prefix is ACM's internal legacy placeholder and does not resolve via doi.org — treated
  as no real DOI.
- **Dennett & Kinsbourne (1992):** two issues. (1) The title is missing its subtitle — the full, DOI-registered
  title is "Time and the observer: the where and when of consciousness in the brain." (2) Pages: Crossref's
  record for the article's own DOI gives **183–201**. The **183–247** figure in the draft (and used by many
  secondary sources) is the page range of the *entire BBS treatment* — target article plus open peer commentary
  by many authors plus the authors' response — all printed under one continuous page run, which is a common and
  defensible citation convention for BBS target articles, but is not what the article's own DOI covers. Flagging
  for the author's own choice rather than silently picking one; the table above uses the DOI-registered range.
- **Elga — the flagged item:** "Bracketing and Boltzmann brains" was a 2024 Princeton working-paper draft. It is
  **no longer an unpublished manuscript**: the same argument, retitled "Boltzmann brains and cognitive
  instability," was published in *Philosophy and Phenomenological Research* vol. 111, issue 1, pp. 127–136
  (online April 2025, print July 2025), DOI 10.1111/phpr.70014. Confirmed independently twice (by the research
  agent and by a separate orchestrator spot-check against Crossref/Wiley/PhilArchive). If the author specifically
  wants the earlier/different framing of the 2024 draft, that is a judgment call, but as of 2026-10-18 the work
  is published, not a manuscript.
- **Hoffreumon & Woods (2025) — the flagged item:** the title in the draft, "Quantum theory does not need
  complex numbers," is **exactly correct** as the real title of arXiv:2504.02808 (confirmed from the page's own
  `citation_title` metadata, not a search summary). It reads as a provocative rebuttal title because it is one —
  a direct response to the 2021 Nature paper (Renou et al., also in this list) arguing complex numbers are
  necessary for quantum theory. No change needed.
- **Renou et al. (2021) — the flagged item:** page range 625–629 confirmed correct on *both* ends via Crossref
  and OpenAlex independently. Full 8-author list: Marc-Olivier Renou, David Trillo, Mirjam Weilenmann, Thinh P.
  Le, Armin Tavakoli, Nicolas Gisin, Antonio Acín, Miguel Navascués — the "et al." in the draft is a legitimate
  house-style shorthand and needs no change.
- **Rauch et al. (2018) — the flagged item:** "080403" is correctly an **article number** (PRL moved from page
  ranges to per-article numbers in 2016); "121, 080403" is in fact PRL's own normal citation format, so no
  notation change is needed. Full author list has 20 authors, with D. Rauch correctly first; "et al." in the
  draft is a legitimate house-style shorthand.
- **Hossenfelder & Palmer (2020) — the flagged item:** "139" is an **article number**, not a page number —
  Frontiers journals assign one article number per paper rather than page ranges. Frontiers' own citation
  convention writes this as "Front. Phys. 8:139" (colon, no comma) specifically to mark it as not a page locator.
  Corrected the draft's "8, 139" to "8:139" accordingly. Author is "Tim Palmer" (no middle initial in Crossref's
  byline), so "Palmer, T." was already correct.
- **Minkowski (1908/1909) — the flagged item:** the famous lecture was delivered 21 September 1908 in Cologne;
  the citable print appeared in *Physikalische Zeitschrift*, volume 10, the 1909 volume, pages 104–111. Volume
  10 and pages 104–111 are both correct as drafted. The dual-date "(1908/1909)" is a common convention flagging
  the talk/print-date split; a strict single-year citation would read "(1909)" alone, but the dual form is not
  wrong.
- **Cook (2004) — the flagged item:** checked directly against the publisher's own PDF (not a secondary
  citation) specifically because of the paper's long pre-publication delay (written ~1998–2000, not published
  until 2004) — the printed page range is exactly "1–40" as drafted, with no pagination mismatch.
- Several entries (Kolers & von Grünau, Montgomery, Odlyzko, 't Hooft) had their core facts already correct but
  lacked a DOI in the original draft; one has been added for each where the work has a real resolving one.
- Carroll (2017), Hardy (2001), and Hoffreumon & Woods (2025) are cited as arXiv preprints; each now has an
  arXiv-assigned DOI (`10.48550/arXiv....`) listed, which resolves via doi.org, though none has ever appeared in
  a peer-reviewed journal (Carroll's argument was separately reprinted as a 2017 Routledge book chapter, DOI
  10.4324/9781315713151-3, if the author prefers that citation instead).
- Feynman's Nobel Lecture itself carries no DOI on nobelprize.org; it was reprinted essentially verbatim as
  Feynman, R. P. (1966) in *Science* 153(3737), 699–708, DOI 10.1126/science.153.3737.699, if a DOI-bearing
  citation is wanted instead.
- No entry came back **NOT FOUND** — every one of the 38 checked works independently exists with the core facts
  claimed (modulo the corrections above).

## Clean corrected reference list (alphabetical, DOIs appended where they exist)

Adam, T., et al. (OPERA Collaboration) (2012). Measurement of the neutrino velocity with the OPERA detector in the CNGS beam. *Journal of High Energy Physics* 2012(10), 093. DOI: 10.1007/JHEP10(2012)093

Albert, D. Z. (2000). *Time and Chance.* Harvard University Press.

Banach, S., & Tarski, A. (1924). Sur la décomposition des ensembles de points en parties respectivement congruentes. *Fundamenta Mathematicae* 6, 244–277. DOI: 10.4064/fm-6-1-244-277

Bancal, J.-D., Pironio, S., Acín, A., Liang, Y.-C., Scarani, V., & Gisin, N. (2012). Quantum non-locality based on finite-speed causal influences leads to superluminal signalling. *Nature Physics* 8, 867–870. DOI: 10.1038/nphys2460

Barbour, J. (1999). *The End of Time.* Oxford University Press.

Barnes, E. (1991). The causal history of computational activity: Maudlin and Olympia. *Journal of Philosophy* 88(6), 304–316. DOI: 10.2307/2026687

Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika* 1(3), 195–200. DOI: 10.1103/PhysicsPhysiqueFizika.1.195

Bennett, C. H. (1973). Logical reversibility of computation. *IBM Journal of Research and Development* 17, 525–532. DOI: 10.1147/rd.176.0525

Breuer, T. (1995). The impossibility of accurate state self-measurements. *Philosophy of Science* 62(2), 197–214. DOI: 10.1086/289852

Carnielli, W., & Coniglio, M. E. (2016). *Paraconsistent Logic: Consistency, Contradiction and Negation.* Cham: Springer. DOI: 10.1007/978-3-319-33205-5

Carroll, S. M. (2017). Why Boltzmann brains are bad. arXiv:1702.00850. DOI: 10.48550/arXiv.1702.00850

Chaitin, G. J. (1966). On the length of programs for computing finite binary sequences. *Journal of the ACM* 13, 547–569. DOI: 10.1145/321356.321363

Chalmers, D. J. (1996). Does a rock implement every finite-state automaton? *Synthese* 108, 309–333. DOI: 10.1007/BF00413692

Chen, M.-C., et al. (2022). Ruling out real-valued standard formalism of quantum theory. *Physical Review Letters* 128, 040403. DOI: 10.1103/PhysRevLett.128.040403

Cole, F. N. (1903). On the factoring of large numbers. *Bulletin of the American Mathematical Society* 10(3), 134–137. DOI: 10.1090/S0002-9904-1903-01079-9

Cook, M. (2004). Universality in elementary cellular automata. *Complex Systems* 15, 1–40. DOI: 10.25088/ComplexSystems.15.1.1

Culik, K., II, & Yu, S. (1988). Undecidability of CA classification schemes. *Complex Systems* 2, 177–190.

Danek, A. H., & Wiley, J. (2017). What about false insights? Deconstructing the Aha! experience along its multiple dimensions for correct and incorrect solutions separately. *Frontiers in Psychology* 7, 2077. DOI: 10.3389/fpsyg.2016.02077

D'Ariano, G. M., & Perinotti, P. (2014). Derivation of the Dirac equation from principles of information processing. *Physical Review A* 90, 062106. DOI: 10.1103/PhysRevA.90.062106

Dennett, D. C., & Kinsbourne, M. (1992). Time and the observer: the where and when of consciousness in the brain. *Behavioral and Brain Sciences* 15, 183–201. DOI: 10.1017/S0140525X00068229

Eagleman, D. M., & Sejnowski, T. J. (2000). Motion integration and postdiction in visual awareness. *Science* 287, 2036–2038. DOI: 10.1126/science.287.5460.2036

Egan, G. (1994). *Permutation City.* Millennium.

Elga, A. (2025). Boltzmann brains and cognitive instability. *Philosophy and Phenomenological Research* 111, 127–136. DOI: 10.1111/phpr.70014

Evans, J. St. B. T., Barston, J. L., & Pollard, P. (1983). On the conflict between logic and belief in syllogistic reasoning. *Memory & Cognition* 11, 295–306. DOI: 10.3758/BF03196976

Feynman, R. P. (1985). *QED: The Strange Theory of Light and Matter.* Princeton: Princeton University Press.

Geldard, F. A., & Sherrick, C. E. (1972). The cutaneous "rabbit": a perceptual illusion. *Science* 178, 178–179. DOI: 10.1126/science.178.4057.178

Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik* 38, 173–198. DOI: 10.1007/BF01700692

Gruber, M. (2015). *Die Emergenz des Bewusstseins.* Self-published. ISBN 9781326652074.

*Gruber, M. (2026a). The Four-Model Theory of Consciousness, v19. Zenodo. https://doi.org/10.5281/zenodo.23427746 — self-citation, not verified per instructions, carried forward unchanged.*

*Gruber, M. (2026b). Emergent spacetime from self-referential computation: a hierarchical cellular automaton framework (SB-HC4A), v8. Zenodo. https://doi.org/10.5281/zenodo.23242055 — self-citation, not verified per instructions, carried forward unchanged.*

Hardy, L. (2001). Quantum theory from five reasonable axioms. arXiv:quant-ph/0101012. DOI: 10.48550/arXiv.quant-ph/0101012

Hoffreumon, T., & Woods, M. P. (2025). Quantum theory does not need complex numbers. arXiv:2504.02808. DOI: 10.48550/arXiv.2504.02808

Hossenfelder, S., & Palmer, T. (2020). Rethinking superdeterminism. *Frontiers in Physics* 8:139. DOI: 10.3389/fphy.2020.00139

Kleene, S. C. (1938). On notation for ordinal numbers. *Journal of Symbolic Logic* 3(4), 150–155. DOI: 10.2307/2267778

Kolers, P. A., & von Grünau, M. (1976). Shape and color in apparent motion. *Vision Research* 16, 329–335. DOI: 10.1016/0042-6989(76)90192-9

Kolmogorov, A. N. (1965). Three approaches to the quantitative definition of information. *Problems of Information Transmission* 1, 1–7.

Lakatos, I. (1976). *Proofs and Refutations.* Cambridge University Press.

Laukkonen, R. E., Kaveladze, B. T., Tangen, J. M., & Schooler, J. W. (2020). The dark side of Eureka: Artificially induced Aha moments make facts feel true. *Cognition* 196, 104122. DOI: 10.1016/j.cognition.2019.104122

Laukkonen, R. E., Webb, M., Salvi, C., Tangen, J. M., Slagter, H. A., & Schooler, J. W. (2023). Insight and the selection of ideas. *Neuroscience & Biobehavioral Reviews* 153, 105363. DOI: 10.1016/j.neubiorev.2023.105363

Lawvere, F. W. (1969). Diagonal arguments and cartesian closed categories. In *Category Theory, Homology Theory and their Applications II* (Lecture Notes in Mathematics 92), 134–145. Springer. DOI: 10.1007/bfb0080769

Li, Z.-D., et al. (2022). Testing real quantum theory in an optical quantum network. *Physical Review Letters* 128, 040402. DOI: 10.1103/PhysRevLett.128.040402

MacKay, D. M. (1960). On the logical indeterminacy of a free choice. *Mind* 69(273), 31–40. DOI: 10.1093/mind/lxix.273.31

Mackie, J. L. (1964). Self-refutation — a formal analysis. *Philosophical Quarterly* 14(56), 193–203. DOI: 10.2307/2955461

Mancosu, P., & Vailati, E. (1991). Torricelli's infinitely long solid and its philosophical reception in the seventeenth century. *Isis* 82, 50–70. DOI: 10.1086/355637

Maudlin, T. (1989). Computation and consciousness. *Journal of Philosophy* 86(8), 407–432. DOI: 10.2307/2026650

Minkowski, H. (1908/1909). Raum und Zeit. *Physikalische Zeitschrift* 10, 104–111.

Montgomery, H. L. (1973). The pair correlation of zeros of the zeta function. *Proceedings of Symposia in Pure Mathematics* 24, 181–193. DOI: 10.1090/pspum/024/9944

Mostowski, A. (1952). On direct products of theories. *Journal of Symbolic Logic* 17(1), 1–31. DOI: 10.2307/2267454

Odlyzko, A. M. (1987). On the distribution of spacings between zeros of the zeta function. *Mathematics of Computation* 48, 273–308. DOI: 10.1090/S0025-5718-1987-0866115-0

Oreskes, N. (1999). *The Rejection of Continental Drift: Theory and Method in American Earth Science.* New York: Oxford University Press. DOI: 10.1093/oso/9780195117325.001.0001

Palmer, E. D. (1954). Investigation of the gastric mucosa spirochetes of the human. *Gastroenterology* 27(2), 218–220. DOI: 10.1016/S0016-5085(19)36173-6

Popper, K. R. (1950). Indeterminism in quantum physics and in classical physics, Parts I and II. *British Journal for the Philosophy of Science* 1(2), 117–133; 1(3), 173–195. DOI: 10.1093/bjps/i.2.117; DOI: 10.1093/bjps/i.3.173

Popper, K. R. (1959). *The Logic of Scientific Discovery.* Hutchinson.

Popper, K. R. (1972). *Objective Knowledge: An Evolutionary Approach.* Oxford: Clarendon Press.

Presburger, M. (1929). Über die Vollständigkeit eines gewissen Systems der Arithmetik ganzer Zahlen, in welchem die Addition als einzige Operation hervortritt. *Comptes Rendus du I Congrès des Mathématiciens des Pays Slaves*, Warszawa, 92–101. English translation by D. Jacquette, *History and Philosophy of Logic* 12(2), 225–233 (1991). DOI: 10.1080/014453409108837187

Priest, G. (1994). The structure of the paradoxes of self-reference. *Mind* 103(409), 25–34. DOI: 10.1093/mind/103.409.25

Priest, G. (1995). *Beyond the Limits of Thought.* Cambridge: Cambridge University Press.

Priest, G. (2006). *In Contradiction: A Study of the Transconsistent*, 2nd ed. Oxford: Oxford University Press. DOI: 10.1093/acprof:oso/9780199263301.001.0001

Putnam, H. (1988). *Representation and Reality.* MIT Press.

Rauch, D., et al. (2018). Cosmic Bell test using random measurement settings from high-redshift quasars. *Physical Review Letters* 121, 080403. DOI: 10.1103/PhysRevLett.121.080403

Reber, R., & Unkelbach, C. (2010). The epistemic status of processing fluency as source for judgments of truth. *Review of Philosophy and Psychology* 1, 563–581. DOI: 10.1007/s13164-010-0039-7

Redhead, M. (1975). Symmetry in intertheory relations. *Synthese* 32, 77–112. DOI: 10.1007/BF00485113

Renou, M.-O., et al. (2021). Quantum theory based on real numbers can be experimentally falsified. *Nature* 600, 625–629. DOI: 10.1038/s41586-021-04160-4

Robinson, R. M. (1947). On the decomposition of spheres. *Fundamenta Mathematicae* 34, 246–260. DOI: 10.4064/fm-34-1-246-260

Rosser, B. (1936). Extensions of some theorems of Gödel and Church. *Journal of Symbolic Logic* 1(3), 87–91. DOI: 10.2307/2269028

Ryle, G. (1949). *The Concept of Mind*. London: Hutchinson. Routledge 2009 ed. DOI: 10.4324/9780203875858

Salvi, C., Bricolo, E., Kounios, J., Bowden, E., & Beeman, M. (2016). Insight solutions are correct more often than analytic solutions. *Thinking & Reasoning* 22, 443–460. DOI: 10.1080/13546783.2016.1141798

Shynkaruk, J. M., & Thompson, V. A. (2006). Confidence and accuracy in deductive reasoning. *Memory & Cognition* 34, 619–632. DOI: 10.3758/BF03193584

Solovay, R. M. (1970). A model of set-theory in which every set of reals is Lebesgue measurable. *Annals of Mathematics* 92, 1–56. DOI: 10.2307/1970696

Stone, M. H. (1932). On one-parameter unitary groups in Hilbert space. *Annals of Mathematics* 33, 643–648. DOI: 10.2307/1968538

Szangolies, J. (2018). Epistemic horizons and the foundations of quantum mechanics. *Foundations of Physics* 48(12), 1669–1697. DOI: 10.1007/s10701-018-0221-9

't Hooft, G. (2016). *The Cellular Automaton Interpretation of Quantum Mechanics.* Springer. DOI: 10.1007/978-3-319-41285-6

Tegmark, M. (1997). On the dimensionality of spacetime. *Classical and Quantum Gravity* 14, L69–L75. DOI: 10.1088/0264-9381/14/4/002

Tegmark, M. (2008). The mathematical universe. *Foundations of Physics* 38, 101–150. DOI: 10.1007/s10701-007-9186-9

Thagard, P. (1998). Ulcers and bacteria I: Discovery and acceptance. *Studies in History and Philosophy of Science Part C* 29(1), 107–136. DOI: 10.1016/S1369-8486(98)00006-5

Thompson, V. A., Evans, J. St. B. T., & Campbell, J. I. D. (2013). Matching bias on the selection task: It's fast and feels good. *Thinking & Reasoning* 19, 431–452. DOI: 10.1080/13546783.2013.820220

Thompson, V. A., Prowse Turner, J. A., & Pennycook, G. (2011). Intuition, reason, and metacognition. *Cognitive Psychology* 63, 107–140. DOI: 10.1016/j.cogpsych.2011.06.001

Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society* s2-42, 230–265. DOI: 10.1112/plms/s2-42.1.230

Warren, J. R., & Marshall, B. (1983). Unidentified curved bacilli on gastric epithelium in active chronic gastritis. *The Lancet* 321(8336), 1273–1275. DOI: 10.1016/S0140-6736(83)92719-8

Weber, Z. (2010). Transfinite numbers in paraconsistent set theory. *Review of Symbolic Logic* 3(1), 71–92. DOI: 10.1017/S1755020309990281

Wigner, E. P. (1960). The unreasonable effectiveness of mathematics in the natural sciences. *Communications on Pure and Applied Mathematics* 13, 1–14. DOI: 10.1002/cpa.3160130102

Wolfram, S. (2002). *A New Kind of Science.* Wolfram Media.

Wolpert, D. H. (2008). Physical limits of inference. *Physica D* 237(9), 1257–1281. DOI: 10.1016/j.physd.2008.03.040

Yanofsky, N. S. (2003). A universal approach to self-referential paradoxes, incompleteness and fixed points. *Bulletin of Symbolic Logic* 9(3), 362–386. DOI: 10.2178/bsl/1058448677
