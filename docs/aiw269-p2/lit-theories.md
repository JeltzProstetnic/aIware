<!-- AIW-269 pass 2 (2026-02-17→08-25), theories slice, S323 subagent. OpenAlex 429; bioRxiv 7020/7656, PsyArXiv 5100/7303 records pulled — re-run advised before deposit. -->
<!-- AIW-269 pass 2, theories/tests slice, subagent 2026-09-28. Window 2026-02-17 to 2026-08-25. Not verified by the main loop. -->
# AIW-269 pass 2: rival theories, tests, dreaming and reality monitoring (2026-02-17 to 2026-08-25)

Paper: `paper/full/four-model-theory-full.md`. Items from 08-26 onwards are in `docs/aiw269-lit-theories.md` and are not repeated here. Every item below was resolved by DOI or arXiv/OSF ID, with title, authors and date checked. Each first author was grepped against the reference list (lines 1118–1638), and none of the items below is cited yet. Barrett et al. 2026 (arXiv:2604.11482) was found but is **already cited**.

**Coverage and gaps.** Sources used:
- Crossref keyword queries, plus full journal listings in the window for *Neuroscience of Consciousness* (52 items), *Consciousness and Cognition* (68) and *Philosophy and the Mind Sciences* (42).
- arXiv q-bio.NC monthly listings, Feb–Aug.
- bioRxiv neuroscience via the API. **Partial:** 7,020 of 7,656 records were pulled, so the last days before 08-25 may be under-sampled.
- PsyArXiv via the OSF API. **Partial:** 5,100 of 7,303 records, and the early-window months are the weakest.
- The *Consciousness: A Comprehensive Reference* chapter list.
- Web search.

**Gap:** OpenAlex returned HTTP 429 for most of the session, including the daily limit, so its broad title sweep failed after about 12 queries. A re-run of the OpenAlex and PsyArXiv sweeps is advisable before the deposit.

## MUST-ANSWER

**1. Sikka, P., Hu, S., & Heifets, B.D. (2026).** Dreaming during anaesthesia: a scoping review. *British Journal of Anaesthesia* 137(2):506–524, online 2026-06-11. doi:10.1016/j.bja.2026.05.002
- **Claim.** Dreaming under anaesthesia is common and depends on the agent. Recall of such dreams is 0–64% for **propofol** clinically and 0–77% experimentally, and ketamine is highest. Recall is not associated with intraoperative awareness. Whether the dreams occur during maintenance or only at emergence is unresolved, and the authors call for serial awakening with EEG.
- **Bears on:** Table 4 (line 687, "Propofol | Forced subcritical | EWM/ESM suppressed | **Absent**") and line 694 ("patients report no experience during propofol anesthesia"). The flat "absent" is now contestable in print.
- **Cheap answer.** The emergence/maintenance ambiguity is exactly FMT's escape route: dreams would be generated as the substrate climbs back toward criticality. The row should then say so, and cite this review.

**2. Corcoran, A.W., Haun, A., Dorman, R., Tononi, G., Friston, K., Pennartz, C., et al. (2026).** Integrated information and predictive processing theories of consciousness: an adversarial collaborative review. *Neuroscience & Biobehavioral Reviews*, 106742, 2026-05-09. doi:10.1016/j.neubiorev.2026.106742
- **Claim.** A second adversarial collaboration (IIT vs. Neurorepresentationalism vs. **Active Inference**) sets out core claims, key hypotheses for multi-site experiments, and a scheme for pooling evidence across experiments into a quantitative measure of support for each theory.
- **Bears on two places:**
  - §7.2 PP paragraph (line 857), which relies on Hohwy & Seth: "PP is not itself a theory of consciousness". Friston's camp is now a registered contender with testable predictions, so the dismissal needs one qualifying sentence.
  - Line 31, which names only COGITATE. The field now has a second adversarial collaboration.

## MUST-CITE

**3. Dijkstra, N., Fleming, S.M., & Shea, N. (2026).** Why do we need imagination–reality monitoring? *Neuroscience of Consciousness* niag048, online 2026-08-20. doi:10.1093/nc/niag048
- **Claim.** Imagination reuses perceptual machinery to make it predictive, and this creates the risk of mistaking simulation for reality. The authors reject both a partial-recruitment solution and a pure control-signature solution. They favour a flexible prefrontal metacognitive evaluation that integrates sensory richness and controllability.
- **Bears on:** §6.0, lines 716–718. It is consistent with "posits no marker affixed to internally generated states", and it is the newest statement of the Dijkstra line FMT already relies on (three Dijkstra refs cited).

**4. Tzioridou, S., Bovy, L., Sattler, S., & Dresler, M. (2026).** Why dream amnesia may be adaptive: dream recall frequency predicts dream-reality confusion. *PsyArXiv*, 2026-07-08. doi:10.31234/osf.io/ad43f_v1
- **Claim.** In a population survey (N=4,961), more frequent dream recall goes with more dream-reality confusion. This supports the view that dream amnesia protects source attribution.
- **Bears on:** line 720 ("dreaming is the everyday instance — experience fully present, source attribution absent"). It is consistent with source attribution being the fragile term.

**5. Bandara, K.H., Rowe, E., & Garrido, M.I. (2026).** Testing the spatiotemporal predictions of GNWT and IIT. *bioRxiv*, 2026-07-22. doi:10.64898/2026.07.16.738188
- **Claim.** A dynamic causal modelling reanalysis of COGITATE's MEG data (N=100) found prefrontal ignition **at both stimulus onset and offset**. The offset ignition was not seen in COGITATE's original analysis. For IIT, the result is only a weak, conservatively interpreted fit for sustained intrinsic fusiform connectivity.
- **Bears on:** line 31's summary ("stronger posterior cortical involvement than GNW predicted") and line 851 ("largely confirmed"). The COGITATE verdict is now contested, so add a clause.

**6. Gibbons, M., McBride, E.G., Holenarasipura Venkatasubbaiah, R., et al. (2026).** Protocol for testing GNW and IIT in non-human primates and mice. *PLOS ONE* e0342770, 2026-02-25. doi:10.1371/journal.pone.0342770
- **Claim.** A preregistered cross-species adversarial protocol: Neuropixels recordings in visual, auditory, parietal and prefrontal cortex, a go/no-go task that controls for report, and causal perturbation of prefrontal cortex.
- **Bears on:** line 31 (Melloni et al. 2023 is the only protocol cited) and §6.4 on animal consciousness.

**7. O'Reilly-Shah, V.N., Selvitella, A., & Schurger, A. (2026).** A caveat regarding the unfolding argument: implications of plasticity. *Neuroscience of Consciousness* niag027, 2026-06-16. doi:10.1093/nc/niag027
- **Claim.** Mathematical proofs that **rapid, history-dependent synaptic plasticity breaks the functional equivalence** between a recurrent network and its unfolded feedforward version. Schurger is a co-author of the unfolding argument.
- **Bears on:** §7.2, lines 863–865, where FMT concedes that the unfolded chain "might reproduce the same input-output function". This is an ally, consistent with FMT's reply, and it strengthens that reply.

**8. Fleming, S.M., & Michel, M. — BBS treatment of "Sensory horizons and the functions of conscious vision".** The target article is *Behavioral and Brain Sciences*, doi:10.1017/S0140525X25000068 (online 2025-04). The commentaries and the authors' response landed **2026-06-25** (response: doi:10.1017/S0140525X26104543).
- **Claim.** Conscious vision serves model-based planning beyond the organism's sensory horizon, and it is tied to reality monitoring.
- **Bears on:** §4.2.4 (line 602), the cognitive-learning advantage (simulate the poisonous food rather than eat it). This is a convergent functional account, consistent with FMT's cost-not-possibility claim.
- **Boundary case.** The target article predates the window; only the BBS treatment falls inside it.

**9. Selte, A., Haworth, S.E., Vannasse, T.J., et al. (2026).** Neural signatures of conscious experience during sleep: a serial awakening study using high-density EEG. *bioRxiv*, 2026-08-20. doi:10.64898/2026.08.16.745040
- **Claim.** 256-channel EEG, N=140, 699 NREM awakenings. Dreaming tracked a posterior spectral shift (less alpha and delta, more gamma) and changes in network organisation, and was classified at ROC-AUC 0.80.
- **Bears on:** line 767 (the "hot zone" as the EWM substrate). It is a large replication consistent with the posterior localisation. It partly offsets pass-1's Skipper et al. "blob" finding.

**10. Overgaard, M., Dietz, M., & Waade, P.T. (2026).** Systematic theory–method dependencies in consciousness research. *PsyArXiv* v2, 2026-08-16. doi:10.31234/osf.io/3rqbk_v2
- **Claim.** In the updated ConTraSt database (518 experiments), experimental method predicts decisively whether a study supports, challenges or ignores a given theory. Theories occupy distinct methodological niches, which limits direct comparison.
- **Bears on:** line 31 and the §7.1 scoring matrix. It is a caveat on cross-theory scoring (Yaron et al. 2022 is already cited).

**11. Mallavarapu, A., & Percy, C. (2026).** A no-go theorem for process theories of consciousness. *PsyArXiv*, 2026-08-10. doi:10.31234/osf.io/w3n6v_v1
- **Claim.** Given present-state determinism plus the assumption that consciousness makes a behavioural difference, consciousness must be attributed to a system's present state, not to temporally extended processes. The paper names broadcasting, recurrence, predictive updating and computation as its targets.
- **Bears on:** §4.1 (line 548, "constituted by the *process* of self-simulation") and §3.4.4's temporal echo.
- **Likely answer, in one sentence:** in a recurrent system the process is carried in the present state.
- **Caveat:** this is a preprint by lesser-known authors. Upgrade to MUST-ANSWER if it lands in a journal.

**12. Changeux, J.-P., & Farisco, M. (2026).** The Global Neuronal Workspace as a multilevel model of conscious processing. *Trends in Cognitive Sciences* 30:477–479, 2026-04-01. doi:10.1016/j.tics.2026.03.004
- **Claim.** GNW is a multilevel theory running from molecular to network level. On this reading it is **not a computational-functionalist theory**, unlike Baars's GWT, with which it is often conflated.
- **Bears on:** line 851, which cites Baars 1988 and Dehaene & Changeux together under "GNW", and §4.4 substrate independence. GNW's founders now disown the functionalist reading that FMT's comparison assumes.

## NICE-TO-HAVE

**IIT and the pseudoscience dispute**
- **Barberá-Tomás, Signorelli & Díaz-Faes (2026).** *SocArXiv*, 2026-03-27, doi:10.31235/osf.io/tewnh_v1. A sociology of the IIT controversy that treats the 124 "IIT-Concerned" signatories as a counter-movement. Relevant to line 31.
- **Ponce de Leon & Yoshimi (2026).** *Neuroscience of Consciousness* niag037, doi:10.1093/nc/niag037. On the testability of IIT's silent-neuron predictions.
- **Marshall, Findlay, Albantakis & Tononi (2026).** "Intrinsic units: identifying a system's causal grain." *Neuroscience of Consciousness* niag013, doi:10.1093/nc/niag013. Gives a way to identify macro units that maximise φ. This speaks to FMT's second computational level, whose patterns are "individuated by their mutual effects" (abstract).
- **Grasso, Hendren & Tononi (2026-08-11),** arXiv:2608.11398, "Consciousness as intrinsic structure", and **Robinson, Tononi, Tsuchiya & Grasso (2026-08-12),** arXiv:2608.12030, "The Rosetta Stone…". Both are relevant to Prediction 5 and the structural arm.
- **Langer, van Oostrum & Ay (2026-08-14),** arXiv:2608.14165. Applies integrated information to active-inference agents.

**GNW and theory comparison**
- **Kanai (2026-08-16),** arXiv:2608.15926. A control-theoretic "Global Mediation Workspace".
- **Kanai & Ma (2026-06-13),** arXiv:2606.15348. Intrinsic computational functionalism and simulated consciousness. Relevant to §4.4.
- **Klatzmann & Doerig (2026-06-01),** arXiv:2606.02121. Argues that biological naturalism is untestable unless it cashes out as information processing. Consistent with FMT's handling of biological computationalism in §7.3.
- **Herzog, Schurger & Doerig (2026).** *Scientific Theories of Consciousness*, CUP, 2026-04-23, doi:10.1017/9781009244701. A book-length evaluation by the unfolding-argument authors, with chapters on causal structure theories and illusionism. Relevant to §7.
- **Melloni, Aru & Schlicht (2026).** "What consciousness is should be determined empirically, not a priori." *Trends in Cognitive Sciences* 30:769–770, doi:10.1016/j.tics.2026.04.005. A letter. Relevant to §2's a-priori requirements.
- **Ludwig (2026).** "Against the search for a general theory of consciousness." *Psychology of Consciousness*, doi:10.1037/cns0000494.
- **Beni (2026).** "Against (theory-neutral) method." *Neuroscience of Consciousness* niag003, doi:10.1093/nc/niag003.
- **McQueen & Mueller (2026-07-17),** arXiv:2607.16374. A template for theoretical adversarial collaboration.
- **Devor & Baron (2026).** "Brainstem theory of consciousness." *The Neuroscientist*, 2026-08-25, doi:10.1177/10738584261470362. A cortex-free account of sentience that bears on §6.4. Its date is the last day of the window.

**PP / active inference**
- **Da Costa, Seth, Friston, et al. (2026).** "A Rosetta Stone hypothesis for neurophenomenology." *Neuroscience of Consciousness* niag026, doi:10.1093/nc/niag026.

**Higher-order theories**
- **Weisberg & Rosenthal (2026).** Higher-order theories chapter in *Consciousness: A Comprehensive Reference*, doi:10.1016/B978-0-443-29258-3.00032-X.
- **Peters & Azimi Asrari (2026).** *Philosophy and the Mind Sciences*, doi:10.33735/phimisci.2026.12269.

**Report and no-report**
- **He, L., et al. (2026).** "Report-modulated prefrontal activity and consistent posterior representations during conscious visual perception." *Consciousness and Cognition* 104075, doi:10.1016/j.concog.2026.104075. Relevant to Table 1, line 196. Checked by title only; no abstract was available.

**Reality monitoring**
- **Özsu, Petrova, Dekker & Dijkstra (2026).** *PsyArXiv*, 2026-05-07, doi:10.31234/osf.io/n3fbv_v1. Argues that world models co-develop with a GAN-like imagination/reality discriminator. Close to FMT's EWM framing.
- **Martín-Luengo et al. (2026).** A source/reality-monitoring fMRI meta-analysis. *Human Brain Mapping*, doi:10.1002/hbm.70614.
- **Bates, Lingawi, Perry, Gallagher & Martin (2026).** *bioRxiv*, 2026-08-13, doi:10.64898/2026.08.07.743488. Noisy vestibular stimulation lowered both reality-monitoring and source-monitoring accuracy. This is a second perturbation result alongside pass-1's tDCS study (Bates et al.), consistent with line 718.
- **Maldonado & Moreno-Bote (2026).** *PsyArXiv*, 2026-04-24, doi:10.31234/osf.io/hwt3a_v1. Proposes that consciousness arises from switching between large-scale mental simulation and coupling to the environment. **Close to FMT's simulation framing; worth reading in full.**

**Dreaming**
- **Rochas, …, Tononi & Perogamvros.** "Content-specific and temporally evolving neural correlates of dream experiences." *PsyArXiv* v3 2026-05-07; **v1 is dated 2025-10-30**, outside the window.
- **Ataei, …, Dresler (2026).** Dream recall and awakenings. *bioRxiv*, doi:10.64898/2026.05.20.722678.
- **Temel Başer et al. (2026).** "CSCS-REM", a scale comparing REM and waking consciousness. *Neuroscience of Consciousness* niag038.
- **Solms** (doi:…00045-8) and **Camaioni, De Gennaro & Scarpelli** (doi:…00035-5). Dreaming chapters in *Consciousness: A Comprehensive Reference*.

**Lucid dreaming** (relevant to Prediction 4, line 957, which predicts a discontinuous onset of lucidity)
- **Wang, Peters, Strelen, et al. (2026).** EEG microstates in lucid vs. non-lucid REM, N=8 dreamers. *Consciousness and Cognition* 104047, doi:10.1016/j.concog.2026.104047.
- **Peters et al. (2026).** Muscle and vestibular cueing for lucid dreaming. *SLEEP Advances* zpag074, doi:10.1093/sleepadvances/zpag074.
- **Mallett (2026).** A corpus of 55k lucid and non-lucid dream reports. arXiv:2603.26992.
- **Raczek & Dresler (2026).** Lucid-dreaming chapter, doi:10.1016/B978-0-443-29258-3.00016-1.

## Nothing found / dropped
- **Attention schema theory.** No in-window primary paper.
- **Recurrent processing theory.** Only minor empirical items (e.g. Loo & Buchsbaum, *Consciousness and Cognition* 104100, on aphantasia).
- **Metzinger and self-model theory.** Only German theology-journal commentaries (*ZThK* 148(1)) and MPE modelling (Lopez-Sola et al., *Philosophy and the Mind Sciences* 12136). Nothing that bears on FMT's claims.
- **COGITATE.** No experiment-2 results paper in the window; see Bandara (item 5). One NC item (niag020) was found, but it is only a correction to a GNW response paper.
- **Dropped as out of window:**
  - Dijkstra & Fleming, "Distinguishing imagery and perception in generative models" (PsyArXiv v1 2025-07-23).
  - Zheng, …, Andrillon, "Loops all the way up" (v1 2025-09-02).
