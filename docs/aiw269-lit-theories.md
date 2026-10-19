<!-- AIW-269 half (b), theories/tests slice, S323 2026-09-28 subagent. arXiv date queries returned empty; coverage via q-bio.NC listings + OpenAlex. Citations unverified by main loop. Out-of-window but on-topic: Dijkstra, Fleming & Shea, NC niag048 (online 2026-08-20). -->
# AIW-269 literature sweep: rival theories, tests, dreaming and reality monitoring

Window: first published 2026-08-26 to 2026-09-28. Paper: FMT master v15 (`paper/full/four-model-theory-full.md`).
Sources searched: OpenAlex (title/abstract filters, 45 queries), the bioRxiv API (all 7,235 records in the window, keyword-filtered), PsyArXiv through the OSF API, arXiv q-bio.NC monthly listings plus abstract pages, Crossref, Semantic Scholar and web search. **Every item below has been resolved by DOI or arXiv ID**, and its title, authors and date were checked against the resolved record. One gap: the arXiv query API returned empty bodies for date-filtered queries, so arXiv coverage relies on the q-bio.NC listings plus OpenAlex's arXiv index. cs.AI/cs.CL items belong mostly to another quarter.

## MUST-ANSWER

**1. Basri, J., BarAvi, P., & Hemmo, M. (2026).** Functionalist theories of consciousness: unfolding, substitution and the indeterminacy of function by the physics of the brain. *Consciousness and Cognition* (Nov 2026 issue), online 2026-09-08. doi:10.1016/j.concog.2026.104121
- **Boundary case.** An SSRN precursor with a different title ("…theories of mind…", doi:10.2139/ssrn.5867565) is dated Dec 2025. Keep or drop it on that basis; it is flagged here because of what it targets.
- **Claim.** The paper argues that the unfolding argument is unsound, because the universal-approximation theorems do not support it. It then argues something harder: by a Putnam/Hemmo–Shenker theorem, brain physics cannot uniquely fix any formal structure. Every functionalist theory is therefore left facing the substitution argument, and the authors' only stated way out is reductive identity theory ("Flat Physicalism").
- **Bears on:** §7.2, lines ~863–869 (the unfolding argument, where FMT concedes that "on an unbounded substrate the unfolded chain reproduces the behavior"), and §4.4 substrate independence.
- **Two sides.** The first half is a potential ally: FMT currently concedes more to the unfolding argument than these authors think is owed. The second half cuts at FMT's functionalist commitments, and FMT answers the substitution argument nowhere.

**2. Nakamura, T., Michel, M., & Lau, H. (2026).** Hitting and missing on consciousness. *Psychiatry and Clinical Neurosciences*, online 2026-09-17. doi:10.1111/pcn.70136
- **Claim.** In Hit-and-Miss detection contrasts, the outcome is confounded by decision criteria, perceptual capacity and prestimulus state. The authors argue that the Perceptual Awareness Scale, binocular rivalry and **no-report paradigms** do not fully resolve this, and they recommend dissociation designs in the style of blindsight studies instead.
- **Bears on:** Table 1, line 196, which names "No-report paradigms (Tsuchiya et al., 2015) + targeted TMS during metacognition" as the empirical handle for self-referential closure. Their recommended alternative is consistent with the type-2 d′/meta-d′ dissociation already used in §9 (line 1025). Citing it there costs one sentence.

**3. Skipper, J.I., Timmermann, C., McAlpine, R., et al. (2026).** What is it like to be a blob? A distributed, decentred and context-sensitive neurobiology of consciousness. *bioRxiv*, 2026-09-09. doi:10.64898/2026.09.02.745341
- **Claim.** A meta-analysis of 579 consciousness neuroimaging studies found seven domains, no invariant cross-domain core, and maps spanning 91% of brain regions. "Theory-associated regional loci added no additional meaningful prediction" beyond distributed cognitive, sensorimotor and organismic-affective maps.
- **Bears on:** line 767 ("this hot zone corresponds to the neural substrate generating the EWM") and Prediction 4's DMN localisation of the ESM (line 957). FMT already calls that localisation "not derived from FMT's architecture". The finding is consistent with FMT's "patchwork of overlapping generators" (§7.3, Multiple Generator paragraph), but it undercuts the region-level identifications FMT leans on.

## MUST-CITE

**4. Sahakian, A., van der Stigchel, S., Dijkstra, N., Gayet, S., & Strauch, C. (2026).** Humans learn to distinguish imagination from reality with age. *PsyArXiv*, 2026-08-28. doi:10.31234/osf.io/xm9wf_v1
- **Claim.** A close replication of Dijkstra & Fleming (2023), extended down to age 5: children confuse imagery with perception, and the confusion declines steadily to none with age, independent of perceptual ability and imagery vividness. On this evidence reality monitoring is a learned skill, not innate.
- **Bears on:** §6.0, lines 718–720 ("source attribution is the fragile term, the first to degrade under perturbation"). A capacity that is learned late and lies on top of intact experience is consistent with that ordering, and this is the Dijkstra line the paragraph already cites.

**5. Bates, C., Ring, L., Tolfrey, M., & Martin, A. (2026).** Causal contributions of the dorsolateral prefrontal cortex and temporoparietal junction to source and reality monitoring. *bioRxiv*, 2026-08-27. doi:10.64898/2026.08.25.746632
- **Claim.** A focal-tDCS study (N=100): anodal TPJ stimulation **reduced** perceived-versus-imagined (reality-monitoring) discrimination, while dlPFC stimulation modulated self-versus-other source discrimination. Neither effect showed up in response criterion.
- **Bears on:** lines 718–720, and §9 line 1027, which proposes "targeted TMS to medial prefrontal cortex and temporoparietal junction". This is the first causal evidence in the window that a cortical perturbation degrades source attribution. It supports the perturbation half of the ordering claim; the "before phenomenal experience" half remains untested.

**6. Watanabe, R., Wang, J., Oizumi, M., Saji, N., & Moriguchi, Y. (2026).** Unsupervised alignment reveals shared but locally refined colour qualia structure from toddlerhood to adulthood. *bioRxiv*, 2026-09-21. doi:10.64898/2026.09.14.751604
- **Claim.** Gromov–Wasserstein alignment of colour-similarity structures shows that preschoolers' and adults' structures align perfectly. Toddlers' structures align once late-labelled colours are removed, and toddlers' fit tracks their colour-word knowledge.
- **Bears on:** Prediction 5, line 973 ("The structural arm is demonstrated at the group level for color similarity (Kawakita et al., 2025)…"). This extends the structural arm across development, consistent with it, but it is still a group-averaged result. The individual-level arm and the decoding arm remain untested, so line 973's caveat stands unchanged.

**7. Bieberich, E. (2026).** RIFT: A fractal-holographic theory of consciousness and autopoietic control. *Brain Sciences*, 16(9), 983, online 2026-09-16. doi:10.3390/brainsci16090983
- **Citation maintenance, not new work.** The version of record of a preprint FMT already cites (reference line 1170, bioRxiv 10.64898/2026.03.23.713535). Update the reference in §7.3 ("Convergent theoretical developments").

**8. Bassler, M., & Pennartz, C.M.A. (2026).** Overcoming essentialism: evaluation of theories of consciousness by the lawful regularities they predict. *PsyArXiv*, 2026-09-07/08. doi:10.31234/osf.io/zmghj_v1
- **Claim.** A Popperian argument that no consensus on the essential features of consciousness is possible or needed, and that theories should be judged by the novel law-like regularities they predict, not by their descriptions of experience.
- **Bears on:** §1.2 ("What Would Count as Progress?") and the §7.1 scoring matrix. It is compatible with FMT's emphasis on prospective prediction (§1.1, the Yaron et al. sentence), but it is a direct methodological counterpoint to ranking theories on the eight requirements. A one-clause acknowledgement would pre-empt a reviewer.

## NICE-TO-HAVE

- **Canales-Johnson, A., Rebbin, D., Milinkovic, B., Ince, R.A.A., & Vinck, M. (2026).** From synergy to redundancy: an information-relation account of consciousness. *PsyArXiv*, 2026-09-04. doi:10.31234/osf.io/cz4bw_v1. Proposes synergy and redundancy among neural sources as a common language for IIT, RPT and GNW: contents are built synergistically and stabilised redundantly. Relevant to §7.2 "Additional frameworks" (the Storm et al. integration) and §5.1 binding.
- **Zheng, Z., Truebutschek, D., Cai, Y., & Melloni, L. (2026).** Long-timescale dynamics shape visual conscious awareness. *bioRxiv*, 2026-09-08. doi:10.64898/2026.09.03.748970. Across 20 datasets (N=335), subjective visibility shows autocorrelation over more than 5 s, which is not reducible to criterion shifts; TMS points to a dlPFC readout. Loosely consistent with §3.4.4's "temporal smearing", but on a much slower timescale.
- **Wang, W., & Reid, F. (2026).** Looped transformers under the Jacobian lens: does the global workspace survive recurrence? arXiv:2609.01924, 2026-09-01. A workspace-like band forms in weight-tied recurrent transformers as well as in feedforward ones. Relevant to §7.2's recurrent-versus-unfolded efficiency argument.
- **van Rooyen, P. (2026).** The Cross-Substrate Access Assay. arXiv:2609.22300, v1 2026-09-14. Sets out what a GNW bimodality test must declare before it can be transferred from EEG to language models. Relevant to §8.7/§8.9 and the in-silico programme.
- **Bonamino, C., & Peters, E. (2026).** Lucid dream control: mechanisms, challenges and future directions. *Journal of Sleep Research*, online 2026-09-11. doi:10.1111/jsr.70449. A review arguing that lucidity, agency and control dissociate. Relevant to §6.3 and Prediction 4, which treat lucid onset as the ESM transition; control would be a separate variable.
- **Stecher, R., & Kaiser, D. (2026).** A neuro-computational approximation of the qualities of mental images. *bioRxiv*, 2026-09-02. doi:10.64898/2026.08.25.747062. EEG alignment finds imagery best matched by blurred, low-contrast images. Consistent with line 718's point that imagery lacks perception's bottom-up drive.
- **Orsenigo, D., Luppi, A.I., …, Tamietto, M. (2026).** Preserved brain hierarchy supports residual vision without awareness after visual cortex damage. *bioRxiv*, 2026-09-01. doi:10.64898/2026.08.26.747212. Relevant to §6.5, clinical dissociations.
- **Leung, A., Kawashima, Y., & Tsuchiya, N. (2026).** Registered report on the "consistency assumption" in contrastive analysis of neural correlates of consciousness (NCC), using inattentional-blindness EEG. *PsyArXiv*, 2026-09-09. doi:10.31234/osf.io/qjm48_v1. Methodological companion to item 2.
- **Staller, M.S., & Körner, S. (2026).** From consciousness to observation. *Frontiers in Psychology*, 2026-08-26. doi:10.3389/fpsyg.2026.1762212. A systems-theoretic commentary on Cleeremans et al. (2025); bears only on the §1.1 framing.

## Nothing found in the window

- **IIT.** No new primary IIT paper. Grasso, Hendren & Tononi (arXiv:2608.11398) and Robinson, Tononi, Tsuchiya & Grasso (arXiv:2608.12030) are dated 11–12 Aug, and Corcoran et al.'s IIT×PP adversarial review (NBR, doi:10.1016/j.neubiorev.2026.106742) is dated May 2026. All three fall just outside the window.
- **GNW.** Only items 1 and 3 above plus the machine-side NICE items. Kanai's control-theoretic GNW (arXiv:2608.15926) is dated 16 Aug, outside the window.
- **COGITATE.** The **experiment 2 datasets** were deposited 2026-08-30 (MPDL, e.g. doi:10.17617/1.3xq4-kr38 and doi:10.17617/1.nnma-zh62), but no results paper or preprint has been found yet. Expect one soon; §1.1's COGITATE sentence may then need updating.
- **Predictive processing / active inference, attention schema, recurrent processing theory, Metzinger and self-model theory.** No in-window hits of substance. The only self-model item is Lahoz-Beltra (arXiv:2609.29984), a DMN spiking toy model that is not worth citing.
- **Higher-order theories.** Only item 2.
- **Dreaming.** Only Bonamino & Peters. No new in-window REM/NREM or posterior "hot zone" study was found.
