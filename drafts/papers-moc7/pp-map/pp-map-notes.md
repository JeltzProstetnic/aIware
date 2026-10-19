# PP prediction map: source notes

Map file: `pp-prediction-map.json`. 46 claims, 62 arrows, 45 references. Drawn by Matthias Gruber
from PP's published sources, not by PP's proponents or by Negro et al. Follows the claim-map
method of Negro, Elbaz, Fischer, Schreiber & Mudrik (2026), using the "cognitive" level layout.
Reference numbers below match `references[].n` in the JSON.

All 44 DOIs were resolved against `api.crossref.org/works/<doi>` on 2026-10-19, and author, year,
title and venue were matched. Being You (ref. 6) has no DOI and was checked by ISBN
9780571337705 (Open Library). Where a claim rests on a passage that was read, the passage is named.
"abstract" means the OpenAlex abstract was read. "book" means a book-level attribution whose page
was not checked in this pass.

## Per claim

- **A1**: Friston 2010 [1] (FEP and the brain as a hierarchical model); Clark 2013 [2] §1–2 (the brain as a prediction machine; action and perception); Hohwy 2013 [4] (book, part I); Clark 2016 [3] (book). Seth & Bayne 2022 [7] (accepted manuscript p. 10) also covers perception and active inference.
- **A2**: Seth & Bayne 2022 [7], ms p. 10 (local states are given by "the content of top-down perceptual predictions ... the brain's 'best guess'") and the Fig. 4 legend. "Controlled hallucination": Seth 2021 [6] (book) and Clark 2016 [3] (book). Hohwy 2013 [4] (book).
- **A3**: Seth & Tsakiris 2018 [22], abstract ("instrumental interoceptive inference", allostatic regulation, "because of, and not in spite of, our nature as 'beast machines'"); Seth 2021 [6] (book, Part III); Seth 2013 [5], abstract. Hohwy & Seth 2020 [8], p. 20, calls it a "beast-machine theory of consciousness".
- **B1**: Friston 2005 [19]; Rao & Ballard 1999 [38]; Clark 2013 [2]. Hohwy & Seth 2020 [8] p. 15: "posteriors at one level form (empirical) priors for the level below".
- **B2**: Feldman & Friston 2010 [11], abstract; Hohwy 2013 [4] (book); Carhart-Harris & Friston 2019 [9], full text (precision = inverse variance).
- **B3**: Feldman & Friston 2010 [11], abstract; Hohwy 2012 [26], abstract ("attention as the optimization of precision expectations"); Seth & Bayne 2022 [7], ms p. 11 ("gain").
- **B4**: Seth & Bayne 2022 [7], ms p. 10 (conscious vs unconscious = "part of a current 'best guess' (or optimal posterior)"); Hohwy & Seth 2020 [8], p. 21 ("represented by the posterior with the most evidence", citing Hohwy et al. 2008 [10]).
- **B5**: Hohwy & Seth 2020 [8], pp. 18–19 (policies inferred from expected prediction error; goals as priors; actions fulfil proprioceptive predictions); Friston et al. 2017 [25]; Brown et al. 2013 [39], abstract.
- **B6**: Friston 2010 [1]; Friston 2018 [24], abstract (self-evidencing, Lyapunov function = surprise).
- **B7**: Seth 2013 [5], abstract ("subjective feeling states (emotions) as arising from actively-inferred generative (predictive) models of the causes of interoceptive afferents"); Seth & Friston 2016 [36]; Seth & Bayne 2022 [7], ms p. 10.
- **B8**: Seth 2021 [6] (book, Part III, "the self is a perception too"); Seth 2013 [5], abstract (body ownership and selfhood); Seth & Tsakiris 2018 [22].
- **B9**: Seth & Bayne 2022 [7], Box 1 ("explain, predict and control"; "real problem"); Seth 2021 [6] (book, ch. 1); Hohwy & Seth 2020 [8] (systematic mapping between mechanisms and phenomenology).
- **C1**: Marchi & Hohwy 2022 [32], as summarised in Corcoran et al. 2026 [29], §2.1.3 p. 12 ("only a privileged subset of posterior beliefs ... spanning spatiotemporal scales relevant for embodied interaction"). The Erkenntnis full text was not read.
- **C2**: Corcoran et al. 2026 [29], §2.1.3 pp. 12–13 (AI-C: "active inference is necessary (but may not be sufficient) for a change in conscious content"; covert "mental actions"); Whyte et al. 2026 [30] (source of AI-C; abstract only); Seth & Bayne 2022 [7], ms pp. 10–11.
- **C3**: Friston 2018 [24], abstract ("temporal thickness or counterfactual depth"); Corcoran et al. 2026 [29] p. 12; Hohwy & Seth 2020 [8] p. 26.
- **C4**: Seth 2014 [23], abstract; Hohwy & Seth 2020 [8] p. 23; Seth & Bayne 2022 [7] ms p. 10 (objecthood through conditional sensorimotor predictions).
- **C5**: Corlett et al. 2019 [15], abstract ("strong, overly precise priors can engender hallucinations"); Powers et al. 2017 [16]; "uncontrolled perception": Seth 2021 [6] (book).
- **C6**: Adams et al. 2013 [34], abstract ("various expressions of the same core pathology: namely, an aberrant encoding of precision"); Fletcher & Frith 2009 [17]; Sterzer et al. 2018 [35].
- **C7**: Carhart-Harris & Friston 2019 [9], abstract and §I ("ascending prediction errors ... can find freer register in conscious experience").
- **C8**: Seth & Bayne 2022 [7], ms p. 10 (the rivalry cycle, citing Hohwy et al. 2008); Hohwy et al. 2008 [10]; Hohwy 2013 [4] (book).
- **C9**: Seth & Bayne 2022 [7], Fig. 4 legend ("expectations shape both the content of, and speed of access to, conscious perception"); Pinto et al. 2015 [13], abstract (last sentence: "conscious access depends on verification of perceptual predictions"); de Lange et al. 2018 [28].
- **C10**: Suzuki et al. 2013 [42], abstract; Seth 2013 [5].
- **D1**: Pinto et al. 2015 [13], abstract (four experiments; larger effect for ambiguous input); Hohwy & Seth 2020 [8] p. 22.
- **D2**: Powers et al. 2017 [16], abstract; Corlett et al. 2019 [15], abstract.
- **D3**: Corcoran et al. 2026 [29], §3.3 pp. 28–29 ("AI-C predicts no bias but reduced accuracy"; "other than a regression to prior expectations"; filling-in).
- **D4**: Corcoran et al. 2026 [29], §3.4 pp. 30–31 (active saccade vs passive replay in motion-induced blindness; shorter reappearance times predicted); protocol in Robinson et al. 2025 [31].
- **D5**: Brown et al. 2013 [39], abstract (force-matching; removing attenuation yields "false (delusional) inferences about agency"); Hohwy & Seth 2020 [8] p. 23.
- **D6**: Seth 2014 [23], abstract.
- **D7**: Carhart-Harris & Friston 2019 [9], full text ("At low doses, subjective effects may be felt most tangibly at the perceptual level and particularly within the visual domain ... at higher doses ... functioning of higher levels of the global hierarchy become significantly disrupted"; ego dissolution is discussed there).
- **D8**: Suzuki et al. 2013 [42], abstract.
- **D9**: Hohwy & Seth 2020 [8], p. 20 ("primates (probably all mammals)"; the FEP "may apply literally to every thing") and pp. 25–26 (viruses; temporally deep and counterfactual models); Friston 2018 [24], abstract.
- **D10**: Seth 2025 [37], abstract (biological naturalism; conscious AI "unlikely along current trajectories but becomes more plausible as AI becomes more brain-like and/or life-like"); Seth 2021 [6] (book, final part).
- **D11**: Friston 2026 [44], full text (UCL Discovery accepted manuscript, 3 pp.): von Neumann "immortal computation ... could simulate but not realise mortal computation" and "mortal computation can only be realised with in-memory processing" (p. 2); "rapid developments in neuromorphic and in-memory processing speak to the prospect of creating conscious artefacts ... one will never know whether they are conscious or not" (p. 3). Wiese & Friston 2021 [45], full text (publisher PDF): "compatible with the possibility of synthetic phenomenology, but does not entail that every computer that performs the right computations is conscious" (p. 3); a desktop PC "might simulate consciousness, but will never be conscious" (p. 22); "not about silicon- vs. carbon-based systems" (p. 23). PP's in-house split with D10 and with A3's grounding in the living body: Friston agrees that Turing computation alone does not suffice, but places the requirement in how the computation is physically realised, not in being alive. Stated in the claim text, not drawn as an arrow, because arrows mean "in virtue of". Added S341 on MG's decision (PP-2), taking the map past its 45-claim cap. Not used: Solms & Friston 2018 (JCS, no DOI), which grounds feeling in "the minimal thermodynamic conditions for being alive" and is closer to Seth.
- **E1**: Bastos et al. 2012 [18] (canonical microcircuit; the paper also proposes gamma for forward and alpha/beta for backward signalling, which was left out to keep the claim minimal); Seth & Bayne 2022 [7], Fig. 4.
- **E2**: Adams et al. 2013 [34], abstract ("precision is thought to be encoded by the post-synaptic gain of neurons reporting prediction error ... NMDA receptor function and (dopaminergic) neuromodulation"); Feldman & Friston 2010 [11]; Sterzer et al. 2018 [35].
- **E3**: Barrett & Simmons 2015 [43] (agranular visceromotor cortex as the source of interoceptive predictions; full text not read in this pass); Seth 2013 [5] (anterior insula; abstract only).
- **E4**: Carhart-Harris & Friston 2019 [9], full text ("psychedelics act preferentially via stimulating 5-HT2ARs on deep pyramidal cells ... Deep-layer pyramidal neurons are thought to encode posterior expectations, priors, or beliefs").
- **F1**: Summerfield et al. 2008 [27]; de Lange et al. 2018 [28].
- **F2**: Kok, Jehee & de Lange 2012 [12] (title and main result).
- **F3**: Kok et al. 2012 [41], abstract ("attention reverses the sensory attenuation of predicted signals"); Hohwy & Seth 2020 [8] pp. 22–23.
- **F4**: Garrido et al. 2009 [20] (MMN as prediction error; DCM evidence for forward and backward connection changes).
- **F5**: Kok, Failing & de Lange 2014 [40], abstract; SanMiguel et al. 2013 [21], abstract.
- **F6**: Melloni et al. 2011 [14], abstract (~300 ms without and ~200 ms with expectations); Hohwy & Seth 2020 [8] p. 22.
- **F7**: Weilnhammer et al. 2017 [33], abstract (bilateral inferior frontal gyri and anterior insulae); Hohwy & Seth 2020 [8] p. 21 (prefrontal involvement before transitions).
- **F8**: Carhart-Harris & Friston 2019 [9], full text (entropy measured by e.g. Lempel–Ziv complexity; bottom-up information flow measurable by effective connectivity; disintegration of high-level networks such as the DMN).
- **F9**: Seth & Bayne 2022 [7], Fig. 4 legend ("These theories would be challenged by evidence that top-down signalling or PP occurs in the absence of consciousness, or that changes in these processes do not affect conscious states"); Hohwy & Seth 2020 [8] pp. 19–22 (the top-down signalling constraint).

## Left out, and why

- **The disclaimer that PP "is not itself a theory of consciousness"** (Hohwy & Seth 2020 [8], abstract and p. 26). On the map owner's instruction, the map presents PP as an account of conscious experience.
- **Bastos et al.'s frequency claims** (gamma forward, alpha/beta backward): these are real PP claims, but they were dropped to keep the map at 45 claims (the cap D11 later exceeded on MG's decision). They would be an E/F pair.
- **Global states** (Whyte et al. 2026: deep sleep as disconnection of hierarchical levels, as summarised in Corcoran et al. 2026 pp. 17–18). Left out because only a secondary summary was read and the brief did not list global states. They would fit as a C → E → F chain.
- **Rivalry dominance set by priors** (Hohwy et al. 2008). Left out because the full text could not be retrieved (philpapers blocked the download) to confirm how the paper frames dominance as a prediction. C8 and F7 carry rivalry.
- **Attention–consciousness dissociation** (Hohwy 2012, beyond its abstract) and inattentional blindness under PP. Left out because only the abstract was read.
- **Hallucination Machine** (Suzuki, Roseboom, Schwartzman & Seth 2017, doi 10.1038/s41598-017-16316-2, verified). Left out because its abstract presents it as a simulation tool rather than as a test of a PP prediction, so tying it to over-weighted priors would go beyond the source.
- **Conscious self-evidencing** (Hohwy 2022, doi 10.1007/s13164-021-00578-x, verified). Its full text could not be retrieved, so C3 is carried by Friston 2018 and Corcoran et al. 2026 instead.
- **Interoceptive neural predictions** (e.g., heartbeat-evoked potentials as interoceptive prediction error) and **sensory attenuation in schizophrenia as a patient-level prediction**. No verified PP source was read for either in this pass.
- **Hybrid PP-workspace models** (Whyte & Smith 2021; Whyte, Hohwy & Smith 2022). Left out because they import another theory's architecture, which the brief excludes.
- **Infants, disorders of consciousness, non-verbal animals beyond D9**: Hohwy & Seth 2020 p. 26 explicitly leaves these open, so no claim was made.
- **The INTREPID optogenetic "inactive neurons" experiment** (Corcoran et al. §3.2). There AI-C predicts no effect and makes no positive claim, so it is not a commitment of PP.
