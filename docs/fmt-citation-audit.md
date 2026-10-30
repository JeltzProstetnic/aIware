# FMT Full Paper — Recent / Preprint Citation Audit

**Source paper:** `paper/full/four-model-theory-full.md` (reference list, lines 929–1313)
**Master list:** `docs/references.md` (note: file is at `docs/`, not project root — the task brief's path `/home/jeltz/aIware/references.md` does not exist)
**Audit date:** 2026-06-10
**Scope:** Every citation dated 2024–2026 plus all preprint / in-press / arXiv / bioRxiv / PsyArXiv / OSF / Zenodo / institute-report entries.
**Method:** Web verification via title-in-quotes search + author/year + DOI resolution (Crossref, publisher pages, arXiv, PubMed, bioRxiv, OSF, Zenodo). DOIs were resolved, not assumed. No bibliographic detail was fabricated — where the web could not confirm, the entry is marked UNVERIFIABLE.

## Status legend
- **CONFIRMED** — title, authors, venue, year, DOI all match a real published/posted record.
- **DETAIL-WRONG** — record exists but a cited field (title / year / venue / author / volume / DOI) is incorrect.
- **PREPRINT-ONLY** — exists but is not peer-reviewed/published; flag if the paper leans on it as established.
- **UNVERIFIABLE** — could not confirm via web after genuine effort.

---

## Status table — Priority (load-bearing) targets

| Citation as cited in FMT | Verified details | DOI | STATUS | Note |
|---|---|---|---|---|
| Toker, D., Pappas, I., … Suthana, N. (2026). *Adversarial AI reveals mechanisms and treatments for disorders of consciousness.* Nature Neuroscience, 29, 964–977. | Title, authors, venue, vol/pages all match. Nature Neuroscience 2026. | 10.1038/s41593-026-02220-4 | **CONFIRMED** | Resolves; PubMed 41876853. Load-bearing criticality-loss claim well supported. |
| Tucker, D.M., Luu, P., & Friston, K. (2025). *The criticality of consciousness…* Entropy, 27(8), 829. | Exact title/authors/venue/vol match. | 10.3390/e27080829 | **CONFIRMED** | Open access (MDPI/PMC12385856). |
| Laukkonen, R.E., Friston, K.J., & Chandaria, S. (2025). *A beautiful loop…* Neurosci. Biobehav. Rev., 176, 106296. | Title/authors/venue match. PubMed 40750007; ScienceDirect S0149763425002970. | 10.1016/j.neubiorev.2025.106296 | **CONFIRMED** | — |
| Mago, J., … Lifshitz, M. (2026). *Meditative absorption shifts brain dynamics toward criticality.* arXiv:2511.20990. | Title/authors match. arXiv posted **Nov 26 2025** (id 2511 = Nov 2025). Also OSF PsyArXiv 10.31234/osf.io/2hjq6. | 10.48550/arXiv.2511.20990 | **PREPRINT-ONLY** (+minor year) | Cited "(2026)" but arXiv id/posting = 2025. Not peer-reviewed. FMT presents it as "recent empirical support" — fine as preprint, but flag the 2026 year. |
| Chowdhury, A., Staudigl, T., Kaufmann, E., et al. (2026). *A thalamic oscillation marks states of consciousness in humans.* Nature Human Behaviour. | DOI resolves. **Published title = "Thalamic oscillations distinguish natural states of consciousness in humans"** (Chowdhury … Kaufmann, Staudigl [senior, last]). | 10.1038/s41562-026-02446-z | **DETAIL-WRONG (title; author order)** | Cited title is a paraphrase, not the real title. Staudigl is last (senior) author, not 2nd. This is a load-bearing dual-loop / 20–45 Hz claim — fix the title. |
| Alnagger, N., … Carhart-Harris, R. (2026). *A virtual clinical trial of psychedelics…* Advanced Science, 13(11), e202511780. | Title/venue/vol match. Advanced Science 13(11) 2026. PubMed 41261994. | 10.1002/advs.202511780 | **CONFIRMED** | First author full name Alnagger, N.L.N. Self-consistent. |
| Algom, I. & Shriki, O. (2026). *The concrit framework…* Neurosci. Biobehav. Rev., 180, 106483. | Title/authors/venue/vol match (lowercase "concrit" in title is the publisher's own styling). | 10.1016/j.neubiorev.2025.106483 (S0149763425004841) | **CONFIRMED** | This — not Alnagger — is FMT's "ConCrit framework". Load-bearing 140-dataset criticality claim. OK. |
| Bach, J. & Sorensen, H. (2026). *The Machine Consciousness Hypothesis…* California Institute for Machine Consciousness. (substack) | Exists: essay by Joscha Bach & Hikari Sorensen, CIMC, 2025/26. Non-archival (substack / cimc.ai PDF). | none (no DOI) | **PREPRINT-ONLY / non-peer-reviewed** | Institute essay, not a journal article. FMT cites it for a convergence claim — acceptable but flag as grey literature with no DOI. |
| Bieberich, E. (2026). *RIFT: A fractal-holographic theory…* bioRxiv preprint. https://doi.org/10.1101/2026.03.23.713535 | Record exists on bioRxiv (posted Mar 27 2026, NIH-funded). **Cited DOI `10.1101/…` returns 404.** Valid DOI = `10.64898/2026.03.23.713535` (bioRxiv migrated prefix). PubMed 41929211. | 10.64898/2026.03.23.713535 | **DETAIL-WRONG (DOI) + PREPRINT-ONLY** | Wrong/dead DOI prefix. Also unpublished preprint — FMT correctly labels "bioRxiv preprint". Fix DOI. |
| Hengen, K.B. & Shew, W.L. (2025). *Is criticality a unified setpoint of brain function?* Neuron, 113(16), 2582–2598. | Exact match. Meta-analysis of 140 datasets (2003–2024). | 10.1016/j.neuron.2025.05.020 | **CONFIRMED** | Load-bearing convergence claim well supported. |
| Barrett, A.B., … Seth, A.K. (2026). *Integrated information theory: The good, the bad and the misunderstood.* arXiv:2604.11482. | Title (lowercase in source) + 7-author list match exactly. arXiv Apr 2026. | 10.48550/arXiv.2604.11482 | **CONFIRMED (as preprint)** | FMT correctly labels "arXiv preprint". Not yet peer-reviewed. |
| Katlowitz, K.A., et al. (2026). *Hippocampal neurons process language during propofol sedation.* Nature, 642, 195–203. | DOI/first author (Kalman A. Katlowitz) confirmed. **Published title = "Plasticity and language in the anaesthetized human hippocampus"** (Nature 2026). | 10.1038/s41586-026-10448-0 | **DETAIL-WRONG (title; no DOI in cite)** | Cited title is a paraphrase, not the real title; FMT cite also omits the DOI. Load-bearing implicit-integrity / anesthesia claim — fix title + add DOI. |

## Status table — Other 2024–2026 / preprint entries

| Citation as cited in FMT | Verified details | DOI | STATUS | Note |
|---|---|---|---|---|
| Anthropic (2025). *Exploring model welfare.* Research report. | Published 24 Apr 2025, anthropic.com/research/exploring-model-welfare. | n/a (corporate report) | **CONFIRMED** | Grey literature, correctly labeled. |
| Bhatt, D.K., et al. (2024). *Sleep restores an optimal computational regime in cortical networks.* Nature Neuroscience, 27, 328–338. | Paper real (NN 27, 328–338, 2024). **First author = Yifan Xu** (Xu, Schneider, Wessel, Hengen). "Bhatt, D.K." is NOT an author. | 10.1038/s41593-023-01536-9 | **DETAIL-WRONG (wrong author)** | Likely cross-contamination — a "Bhatt, D.K." appears in the Toker 2026 author list. Correct first author to Xu et al. Load-bearing post-publication evidence claim. |
| Birch, J. (2025). *AI consciousness: A centrist manifesto.* PhilPapers. | Real manuscript, Jonathan Birch (LSE), posted Sep 1 2025 (PhilArchive/PhilPapers). | n/a | **CONFIRMED (preprint/manuscript)** | Not peer-reviewed; host correct. |
| Butlin, P., et al. (2025). *Identifying indicators of consciousness in AI systems.* Trends in Cognitive Sciences. | Title/venue match; 20-author group (Butlin, Long, Bayne, Bengio, Birch, Chalmers, …). | 10.1016/j.tics.2025.10.011 | **CONFIRMED** | — |
| Byczynski, G. & D'Angiulli, A. (2025). *Vivid imagery of objects primes perception of subliminal spatial information.* Neurosci. Conscious., 2025(1), niaf026. | Exact match. | 10.1093/nc/niaf026 | **CONFIRMED** | — |
| Beni, M. (2026). *Bootstrapping and its discontents in consciousness science.* Rev. Phil. Psych. | Exact match, Majid D. Beni, Springer 2026. | 10.1007/s13164-026-00803-5 | **CONFIRMED** | — |
| COGITATE Consortium (2025). *An adversarial collaboration to critically evaluate theories of consciousness.* Nature. | **Cited title = the 2023 bioRxiv preprint title.** Published Nature 2025 paper is "Adversarial testing of global neuronal workspace and integrated information theories of consciousness", Nature 642(8066), 133–142. | 10.1038/s41586-025-08888-1 (published version) | **DETAIL-WRONG (title)** | Preprint title applied to a 2025 published-paper citation. Update title (and add the real DOI/vol/pages) or relabel as the 2023 preprint. |
| Ellia, F. & Tsuchiya, N. (2025). *Beyond accommodation…* Neurosci. Conscious., 2025(1), niaf014. | Exact match. | 10.1093/nc/niaf014 | **CONFIRMED** | — |
| Fitz, S. (2025). *Testing the Machine Consciousness Hypothesis.* arXiv:2512.01081. | Title/author (Stephen Fitz) match. arXiv submitted Nov 30 2025. | 10.48550/arXiv.2512.01081 | **CONFIRMED (preprint)** | Correctly labeled. |
| Fleming, S.M. & Shea, N. (2024). *Quality space computations for consciousness.* Trends Cogn. Sci., 28(10), 896–906. | Exact match. | 10.1016/j.tics.2024.06.007 | **CONFIRMED** | — |
| Gomez-Marin, A. & Seth, A.K. (2025). *A science of consciousness beyond pseudo-science and pseudo-consciousness.* Nature Neuroscience, 28, 703–706. | Exact match. | 10.1038/s41593-025-01913-6 | **CONFIRMED** | — |
| Graziano, M.S.A. (2024). *Illusionism big and small…* eNeuro, 11(10), ENEURO.0210-24.2024. | Exact match. | 10.1523/ENEURO.0210-24.2024 | **CONFIRMED** | — |
| Gruber, M. (2026a). *Why intelligence models must include motivation: A recursive framework.* PsyArXiv. https://osf.io/preprints/osf/kctvg | OSF page is JS-rendered; record did not surface via web search/fetch. Author's own RIM preprint. | (OSF id kctvg) | **UNVERIFIABLE (self-citation)** | Could not confirm independently via web. Author can confirm existence/title; verify the OSF URL resolves before resubmission. Preprint, not peer-reviewed. |
| Gruber, M. (2026b). *Toward a mathematical formalization of the Four-Model Theory.* Manuscript. | Author's own unpublished manuscript. | n/a | **PREPRINT-ONLY (self, unpublished)** | Not externally verifiable by design ("Manuscript"). |
| Gruber, M. (2026c). *The Singularity-Bounded Holographic Class 4 Automaton: A computational model of cosmological structure.* Zenodo. https://doi.org/10.5281/zenodo.18698605 | Zenodo record exists (Matthias Gruber). **Record title = "Emergent Spacetime from Self-Referential Computation: A Hierarchical Cellular Automaton Framework"** (concept = SB-HC4A; v2 = 10.5281/zenodo.20294692, May 2026). | 10.5281/zenodo.18698605 | **DETAIL-WRONG (title) — self-citation** | Cited title ≠ Zenodo record title. Reconcile the title (and confirm which version DOI to cite). Self-deposit = effectively preprint. |
| IIT-Concerned, Klincewicz, M., Cheng, T., et al. (2025). *What makes a theory of consciousness unscientific?* Nature Neuroscience, 28, 689–693. | Exact match. | 10.1038/s41593-025-01881-x | **CONFIRMED** | — |
| Katlowitz — see priority table (DETAIL-WRONG, title). | | | | |
| Kirkeby-Hinrup, A., Fink, S.B., & Overgaard, M. (2025b). *Methodological issues in consciousness research…* Frontiers in Psychology, 16, 1633907. | Title/venue/vol/DOI confirmed via publisher. **Authors = Kirkeby-Hinrup, Stephens, Balogh Sjöstrand, Overgaard.** Sascha B. Fink is NOT an author. | 10.3389/fpsyg.2025.1633907 | **DETAIL-WRONG (authors)** | Fink wrongly inserted (likely carried over from the niaf035 paper, which IS Kirkeby-Hinrup/Fink/Overgaard). Replace Fink → Stephens & Balogh Sjöstrand. |
| Kirkeby-Hinrup, A., Fink, S.B., & Overgaard, M. (2025). *The Multiple Generator Hypothesis.* Neurosci. Conscious., 2025(1), niaf035. | Authors (Kirkeby-Hinrup, Fink, Overgaard) correct. **Published title = "The multiple generator hypothesis of consciousness"** ("of consciousness" suffix omitted in FMT). | 10.1093/nc/niaf035 | **DETAIL-WRONG (title, minor)** | Add "of consciousness" to the title. |
| Kleiner, J. (2024). *What is a mathematical structure of conscious experience?* Synthese, 202, 196. | Title/DOI correct. **Crossref: Synthese vol 203, issue 3, article 89** — not "202, 196". | 10.1007/s11229-024-04503-4 | **DETAIL-WRONG (volume + article number)** | Fix volume (203) and article (89). DOI is right. |
| Li, J., … Grossman, N. (2025). *Falling asleep follows a predictable bifurcation dynamic.* Nature Neuroscience, 28(12), 2515–2525. | Title/authors/venue match. | 10.1038/s41593-025-02091-1 | **CONFIRMED** | — |
| Long, R., Sebo, J., Butlin, P., Birch, J., Chalmers, D., et al. (2024). *Taking AI welfare seriously.* arXiv:2411.00986. | Exact match (posted 4 Nov 2024). | 10.48550/arXiv.2411.00986 | **CONFIRMED (preprint)** | Correctly labeled. |
| Milinkovic, B. & Aru, J. (2025). *Biological computationalism.* Neurosci. Biobehav. Rev., 181, 106524. | Venue/vol/article confirmed. **Published title = "On biological and artificial consciousness: A case for biological computationalism".** | 10.1016/j.neubiorev.2025.106524 | **DETAIL-WRONG (title)** | Title truncated/paraphrased; restore full title. |
| Schwitzgebel, E. (2025). *AI and consciousness.* arXiv:2510.09858. | Exact match (Eric Schwitzgebel, posted Oct 2025). | 10.48550/arXiv.2510.09858 | **CONFIRMED (preprint)** | Correctly labeled. |
| Tononi, G., Albantakis, L., Barbosa, L., et al. (2025). *Consciousness or pseudo-consciousness? A clash of two paradigms.* Nature Neuroscience, 28, 694–702. | Exact match. | 10.1038/s41593-025-01880-y | **CONFIRMED** | — |
| Wagner-Altendorf, T. (2024). *Progress in understanding consciousness?…* Acta Analytica, 39, 719–736. | Exact match (Tobias A. Wagner-Altendorf). | 10.1007/s12136-024-00584-5 | **CONFIRMED** | — |

> Older-but-DOI'd entries spot-checked and not flagged: Albantakis et al. 2023 (IIT 4.0), Butlin et al. 2023 (arXiv:2308.08708), Phillips 2021 (10.1037/rev0000254), Touboul & Destexhe 2017. These predate the 2024–2026 window and were not in scope; no errors observed in passing.

---

## ACTION LIST — must fix before resubmission

### A. Bibliographic errors to correct (factual, will fail reviewer/copy-editor checks)

1. **Chowdhury et al. (2026)** — title is wrong. Change to **"Thalamic oscillations distinguish natural states of consciousness in humans"**. Fix author order (Staudigl is senior/last author, not second). DOI 10.1038/s41562-026-02446-z is correct. *(Load-bearing: dual-loop / 20–45 Hz thalamic claim, cited 3× in body — lines ~490, 538, 625.)*
2. **Katlowitz et al. (2026)** — title is a paraphrase. Change to **"Plasticity and language in the anaesthetized human hippocampus"**; add DOI **10.1038/s41586-026-10448-0**. *(Load-bearing: implicit-integrity-under-anesthesia claim, cited 3× — lines ~183, 607, 609.)*
3. **Bhatt, D.K., et al. (2024)** — WRONG FIRST AUTHOR. The paper "Sleep restores an optimal computational regime…" (NN 27, 328–338, DOI 10.1038/s41593-023-01536-9) is **Xu, Y., Schneider, A., Wessel, R., & Hengen, K.B.** "Bhatt, D.K." is not an author (it appears in the *Toker* author list — likely a copy error). Correct to **Xu et al. (2024)** throughout (abstract + lines ~748). *(Load-bearing post-publication evidence.)*
4. **Bieberich (2026)** — DOI dead. Replace `10.1101/2026.03.23.713535` with **`10.64898/2026.03.23.713535`** (bioRxiv's current prefix).
5. **Kirkeby-Hinrup et al. (2025b)** — wrong authors. Replace "Fink, S.B." with the real co-authors **Stephens, A., & Balogh Sjöstrand, A.** (Fink belongs only on the niaf035 paper).
6. **Kleiner (2024)** — wrong volume/article. Change "Synthese, 202, 196" → **"Synthese, 203(3), 89"**. DOI is correct.
7. **Milinkovic & Aru (2025)** — restore full title: **"On biological and artificial consciousness: A case for biological computationalism."**
8. **Kirkeby-Hinrup et al. (2025) [niaf035]** — restore full title: **"The multiple generator hypothesis of consciousness."**
9. **COGITATE Consortium (2025)** — the cited title is the 2023 *preprint* title. Either (a) update to the published title **"Adversarial testing of global neuronal workspace and integrated information theories of consciousness," Nature 642(8066), 133–142 (2025), DOI 10.1038/s41586-025-08888-1**, or (b) relabel the entry as the 2023 bioRxiv preprint. Pick one consistently.
10. **Gruber (2026c)** [self] — cited title ≠ Zenodo record title ("Emergent Spacetime from Self-Referential Computation: A Hierarchical Cellular Automaton Framework"). Reconcile the title and confirm which version DOI to cite (a v2 at 10.5281/zenodo.20294692 exists, May 2026).

### B. Year/label fixes
11. **Mago et al.** — cited "(2026)" but arXiv id 2511.20990 = posted **November 2025**. Use 2025 (or note "2025 preprint") unless a 2026 published version now exists.

### C. Resubmission RISK — load-bearing claims resting on still-unpublished preprints / grey literature

The reviewer's concern is legitimate: several convergence/support claims rest on sources that are **not peer-reviewed**. If a reviewer discounts unpublished work, these weaken:

- **Mago et al. (2026)** — arXiv preprint, cited as "recent empirical support for the criticality prerequisite" (meditation→criticality, line ~448). *Soften to "a recent preprint reports…" and check for a published version before resubmission.*
- **Bieberich (2026) RIFT** — bioRxiv preprint, used as one of two "convergent theoretical developments" (line ~722). Acceptable as preprint if framed as such; the dead DOI must be fixed.
- **Bach & Sorensen (2026) MCH** — substack/institute essay, no DOI, not peer-reviewed; anchors a convergence paragraph (line ~724). Frame explicitly as grey literature.
- **Barrett et al. (2026)** — arXiv preprint (fine, already labeled).
- **Fitz (2025), Schwitzgebel (2025), Long et al. (2024), Birch (2025), Anthropic (2025)** — all preprints/grey literature, correctly labeled; low risk (used for context, not load-bearing).
- **Gruber 2026a/b/c** [self] — one preprint (RIM/OSF) is currently **UNVERIFIABLE via web**; 2026b is an unpublished manuscript; 2026c is a Zenodo self-deposit with a title mismatch. Self-citations to non-peer-reviewed work are a known reviewer sensitivity — confirm all three URLs resolve and consider minimizing reliance.

**Bottom line for the flagged reviewer point:** the *core* criticality-convergence claims that are genuinely load-bearing — **Toker (2026), Hengen & Shew (2025), Algom & Shriki (2026), Tucker/Luu/Friston (2025), Alnagger (2026), Chowdhury (2026), Katlowitz (2026)** — are all **real, peer-reviewed, published** papers (Chowdhury and Katlowitz need title fixes, but the papers exist and say what FMT claims). The convergence is NOT resting on vapor. The remaining preprint-only items (Mago, Bieberich, Bach, Barrett) are framed as convergent/illustrative rather than as primary evidence. Fix the 10 bibliographic errors above and explicitly flag preprints as preprints, and the reviewer's "could not independently verify" objection is fully answerable.
