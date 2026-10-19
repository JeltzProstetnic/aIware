<!-- AIW-269 pass 2 (2026-02-17→08-25 + post-window keyword re-run), AI slice, S323 subagent. OpenAlex 429, PhilPapers/cell.com 403. -->
<!-- AIW-269 pass 2, AI/machine-consciousness slice. Subagent, 2026-09-28. Not committed. -->
# AIW-269 pass 2: AI and machine consciousness, first published 2026-02-17 to 2026-08-25

**Sources:** arXiv advanced search with a v1 date filter (consciousness, sentien*, qualia, phenomenal, self-model, self-representation, introspect*, self-report, AI/model welfare, emotion representations) and abstract pages; OpenAlex; Crossref (including the full JCS 2026 table of contents); web search. Every item was resolved by arXiv ID or DOI, and none is in FMT's reference list unless stated.

**Gaps:** the arXiv API returned 406, so I scraped the search pages. OpenAlex hit its daily 429 limit partway through, so the post-window re-run is arXiv-only. PhilPapers and cell.com returned 403, so TiCS items are checked via Crossref only. Line numbers refer to `paper/full/four-model-theory-full.md`.

---

## 0. Anthropic, "A global workspace in language models": verified and assessed against l.646 (and l.382)

**Gurnee, W., Sofroniew, N., Pearce, A., … Batson, J., & Lindsey, J. (2026). *Verbalizable Representations Form a Global Workspace in Language Models*. transformer-circuits.pub, 2026-07-06; arXiv:2607.15495 (v1 2026-07-16).** The blog title is "A global workspace in language models". FMT does not cite it.

**What it claims.** A Jacobian lens picks out the "J-space": the sparse residual-stream directions a model is poised to verbalise (about 6–10% of variance, tens of concepts, middle layers only). Its contents are reportable, can be summoned and held, carry silent multi-hop reasoning, and transfer across contexts; parsing runs without them. The authors report ignition-like switching. Post-training "installs the Assistant's point of view in the workspace". They "take no position" on phenomenal consciousness. Their own key disanalogy: broadcast happens "within a single feedforward pass rather than through recurrent loops".

**Invited commentaries, same date.**
- **Eleos AI** (Butlin, Shiller, Plunkett & Long) call it "the most significant evidence of consciousness in LLMs so far uncovered by mechanistic interpretability". They add that the base model shows "something consciousness-like without a 'self'", and that post-training "draws the model towards a coherent, persisting point of view".
- **Dehaene and Naccache** write that "autonomous recurrent activity is largely absent … LLMs do not seem to contain the kind of 'strange loop' needed for a system to model its own processes and … develop a self".

**Where it bears on FMT.**
1. **l.646 survives, with one clause to fix.** "Lacks an ongoing self-simulation" still holds. The J-space is per-token, reactive and feedforward, modifies no weights, and persists only through emitted and cached tokens. Dehaene & Naccache now state that deficit in near-FMT terms. But the paper does show a reportable self-*representation* (the Assistant's point of view, plus self-monitoring traces) inside the workspace. l.646 should concede that and place the deficit in *closure, persistence and regime*, as its last sentence already does.
2. **l.382 is the sharper exposure.** FMT says access and phenomenal consciousness "do not come apart", and it lists P3b ignition among markers "tracking the right target". The J-space shows GNW-style access markers, ignition included, in a system FMT calls non-conscious. Fix: say that FMT-access is entry into a self-referentially closed explicit simulation, and that broadcast plus ignition is its neural *signature*, not its definition. The J-space then becomes a live instance of the marker drift FMT uses at l.640 (Beni); cite it there too.
3. **l.987** ("GNW … no specific architectural blueprint") is weakened now that GNW has an empirically located workspace in an engineered system. Rest uniqueness on the self-model plus closure.

**Verdict: MUST-ANSWER.** It is the highest-profile item in the window, it concerns Claude, and FMT acknowledges drafting with Claude (l.1098), so reviewers will ask. Cite it with both commentaries.

---

## 1. MUST-ANSWER

**1.1 Goldstein, S. & Kirk-Giannini, C. D. (2026). "A Case for AI Consciousness: Language Agents and Global Workspace Theory." *JCS* 33(7–8): 61–96. doi:10.53765/20512201.33.7.061** (version of record 2026-07/08; the preprint, arXiv:2410.11407, dates from 2024 and is also uncited).
If GWT is true, scaffolded language agents "might easily be made phenomenally conscious if they are not already". The authors derive necessary and sufficient GWT conditions for artificial systems.
*Bears on:* l.646 ("the resemblance is architectural mimicry, not self-referential closure … however elaborately orchestrated"). This is the published pro-scaffolding case that l.646 argues against without naming it. Together with the J-space paper it makes a pincer.
**Verdict: MUST-ANSWER.** One sentence would do it: GWT-sufficiency is exactly what FMT denies, because workspace plus broadcast without a self-referentially closed ESM is EWM-like access with no subject.

**1.2 Tiehen, J. & Tubert, A. (2026). "Superintelligent Zombies." *JCS* 33(7–8): 97–120. doi:10.53765/20512201.33.7.097.**
The authors use resource-rational analysis to argue that "intelligence is the enemy of consciousness": beyond a threshold, more intelligent systems are less likely to be conscious, so superintelligent AI would be a zombie.
*Bears on:* §4.2.4 (l.602: the architecture makes cognitive learning *affordable*) and l.993 (imitation without the architecture "carries a cost no current system pays"). They use the same cost-rationality style of argument and reach the opposite conclusion.
**Verdict: MUST-ANSWER (light).** FMT's claim is about a budget, and theirs is about unlimited budgets. Saying so explicitly sharpens l.993.

**1.3 Rival blueprints that further weaken l.987 ("Unique?").** These add to S3Q (Grinberg et al.), flagged in pass 1.
- **Yu, H., Zhao, Y., Blum, L., Blum, M., & Liang, P. P. (2026). "CTM-AI: A Blueprint for General AI Inspired by a Model of Consciousness." arXiv:2605.04097** (2026-04-30). The Conscious Turing Machine is implemented over foundation models, with benchmark gains. The Blums' CTM is not cited anywhere in FMT.
- **Sanyal, A. (2026). "ReCoN-Ipsundrum: An Inspectable Recurrent Persistence Loop Agent …" *Proc. AAAI Symp. Series* 8(1): 352–360; arXiv:2602.23232** (2026-02-26). A working agent with a recurrent persistence loop and affect coupling, tested against mechanism-linked consciousness indicator assays with lesion dissociations. It is a direct cousin of the §8.9 in-silico programme.

**Verdict: MUST-ANSWER** as a group. Rewrite l.987 so that uniqueness rests on the four-model 2×2 plus self-referential closure plus the Class 4 regime, not on "blueprint". Name CTM and S3Q in §7.3.

---

## 2. MUST-CITE

**Indicator methodology (l.640, beside Beni 2026 and Bayne et al. 2024)**
- **Koch, F. (2026). "Calibration and transfer in indicator-based assessments of artificial consciousness." *Neuroscience of Consciousness* 2026(1): niag061; arXiv:2603.27597** (v1 2026-03-29). Theory-derived indicators cannot be calibrated against known artificial cases. Their relevance is also *transferred* from biology without evidence that the indicator–consciousness link holds across substrates. This is Beni's circularity point, published in a journal in-window. It also bears on l.382 (see §0).
- **Pennartz, C. M. A. (2026). "How can we validate theory-derived indicators of consciousness in AI?" *TiCS* 30: 573–574. doi:10.1016/j.tics.2026.01.011**, and the reply **Butlin, P., Bayne, T., Fleming, S. M., Mudrik, L., et al. (2026). "Consciousness indicators, mimicry, and internal variants." *TiCS* 30: 575–576. doi:10.1016/j.tics.2026.04.006.** Pennartz asks for behavioural validation. Butlin et al. prefer internal indicators because behaviour can be "gamed". That is FMT's own l.646 position ("measurable on the system itself").

**LLM self-report and introspection (l.646, l.342, l.566)**
- **Lederman, H. & Mahowald, K. (2026). "Emergent Introspection in AI is Content-Agnostic." arXiv:2603.05414** (2026-03-05). Models detect *that* an injected thought is present but confabulate *what* it is, favouring frequent, concrete concepts.
  - *Bears on:* this fits FMT's "unrepresentable apparatus" (l.566) and substrate "anomalous content" leaks (l.534, l.730). An intrusion can register without the generating apparatus being represented.
  - **MUST-CITE.** It is a clean consistency point.
- **Singh, S., Linzen, T., & Ravfogel, S. (2026). "Can LLMs Introspect? A Reality Check." COLM 2026; arXiv:2605.26242** (2026-05-25). Input-only classifiers match the models' "introspective" predictions. The models also cannot tell a tampered internal state from input manipulation, so there is no evidence of privileged access.
- **Macar, U., …, Ameisen, E., & Lindsey, J. (2026). "Mechanisms of Introspective Awareness." arXiv:2603.21396** (2026-03-22). Injection detection is a two-stage circuit that emerges only from preference optimisation (DPO) and is absent in base models. The capacity is trained in, not architectural.
  - *Pairing note:* cite Macar et al. together with Singh et al. and Lederman & Mahowald for balance.
  - Lindsey's 2025 "Emergent introspective awareness" (out of window) is also uncited and is the anchor all three respond to.
- **Perrier, E. & Bennett, M. T. (2026). "Time, Identity and Consciousness in Language Model Agents." AAAI Spring Symposium; arXiv:2603.09043** (2026-03-10). They score whether identity constraints are *co-instantiated at a single step* in agent scaffolds, which "separates talking like a stable self from being organized like one". This is l.646's scaffolding argument, operationalised.

**Persistence as the missing ingredient (l.646, l.578)**
- **Kanai, R., Sun, Z., & Baltieri, M. (2026). "The Stream of Computation: Temporal Continuity as a Missing Ingredient for Artificial Consciousness." *JCS* 33(7–8): 35–60. doi:10.53765/20512201.33.7.035.** Current AI "exist[s] only within isolated episodes of computation". The paper proposes persistent recursive inference with autonomy and continual learning, as opposed to chain-of-thought "recursive only on demand". This is the same diagnosis FMT gives at l.646 ("knowledge resets … the loop closes over the emitted text").
  - **MUST-CITE** as independent convergence. Kanai is a Butlin et al. co-author.

**Biological naturalism (l.642)**
- **Klatzmann, U. & Doerig, A. (2026). "What biology can, and cannot, tell us about conscious AI." arXiv:2606.02121** (2026-06-01). "Type-A" biological naturalism (biology matters without any processing difference) dissociates consciousness from behaviour and is untestable. "Type-B" (biology matters because it affords unique processing) is testable and "not incompatible with computational functionalism". This is exactly l.642's move ("a specification of one Class 4-capable architecture, not a substrate requirement"), made in-window by others.

**Functional emotions (l.358; §4.2.1–4.2.3)**
- **Sofroniew, N., Kauvar, I., Saunders, W., … (2026). "Emotion Concepts and their Function in a Large Language Model." arXiv:2604.07729** (2026-04-09, Anthropic). Claude Sonnet 4.5 has emotion-concept representations that causally drive preferences and misaligned behaviour ("functional emotions"). The authors say this does "not imply … subjective experience".
  - *Bears on:* FMT's split. Valence machinery sits on the implicit (real) side; felt emotion requires explicit-model entry. Reviewers will raise this paper.
- **Han, A. Q., Chalmers, D. J., & Izmailov, P. (2026). "How's it going? Reinforcement learning in language models recruits a functional welfare axis." arXiv:2605.30232** (2026-05-28). Reward and punishment vectors are near-antiparallel, pre-exist RL, and steer self-reports. Chalmers co-authors.
  - **MUST-CITE** as the pair with Sofroniew.

**Scaffolded self-monitoring (l.646)**
- **Xie, Y. (2026). "Self-Monitoring Benefits from Structural Integration." arXiv:2604.11914** (2026-04-13). Metacognition and self-prediction modules added as auxiliary add-ons collapse to constants and give no benefit. Integrated into the policy loop, they help (d = 0.62). This is small but direct empirical support for "external scaffolding" versus intrinsic closure.
  - **MUST-CITE (weak)**, or NICE.

---

## 3. NICE-TO-HAVE (compressed)

- **Kanai & Ma (2026), arXiv:2606.15348** (and arXiv:2606.06424). Intrinsic computational functionalism: input/output equivalence is not enough (lookup tables), so internal mechanism must count. This answers the "simulated water isn't wet" objection that FMT's "simulation" vocabulary invites. Upgrade to MUST-CITE if a referee raises Searle.
- **Simon (2026), *JCS* 33(7–8): 149–180, doi:10.53765/20512201.33.7.149.** If LLMs are conscious, the subject is the forward-pass "playwright", not the persona. This bears on the difference between an ESM and a persona.
- **Self-report cluster** (pairs with pass-1 Šekrst and Maczan):
  - Chua, Betley, Marks & Evans, arXiv:2604.13051: models trained to claim consciousness acquire unrequested preferences.
  - DeTure, arXiv:2604.25922: trained denial across 115 models.
  - Kim, Street, Rocca … Keeling, arXiv:2603.28925 and arXiv:2607.28607.
  - Douglas … Duvenaud, "The Artificial Self", arXiv:2603.11353.
- **Welfare and philosophy:**
  - JCS special issue "Consciousness in Current AI", ed. Butlin, Shiller & Simon (doi:10.53765/20512201.33.7.009), with Bayne (pp. 209–239), Lee (pp. 240–276) and Yetter-Chappell (pp. 181–208).
  - Long, Sebo, Butlin, Plunkett et al., *Studying AI Welfare Empirically* (NYU CMEP/Eleos report, 2026-07-01): the successor to the cited Long et al. (2024) at l.1043.
  - Keeling & Street, *Emerging Questions in AI Welfare* (Cambridge Elements, doi:10.1017/9781009732000).
  - McClelland, arXiv:2608.19215.
  - Comsa, arXiv:2605.06965.
  - Love, arXiv:2606.00226.
  - Howells-Whitaker & Lazar, arXiv:2607.08695.
  - Mikeda, arXiv:2606.05528.
  - Berry, *J. Appl. Phil.*, doi:10.1002/japp.70087.
  - Chella, *Front. Psychol.*, doi:10.3389/fpsyg.2026.1903644.
- **Other valence work:** Bianco & Shiller, arXiv:2602.19159.
- **Resolved by DOI, abstract not retrieved:**
  - de Weerd, *Synthese* 207, doi:10.1007/s11229-026-05534-9. The title claims AI consciousness "is not about biological substrates", which would support l.642. Read it before citing.
  - Floridi, *Phil. & Tech.* 39, doi:10.1007/s13347-026-01052-1.

---

## 4. Reference hygiene (in-window versions of record)

- **Butlin et al. (2025) → *TiCS* 30(6): 488–501 (June 2026).** Update l.1043 and the reference list.
- **Schwitzgebel (2025) arXiv:2510.09858 → *AI and Consciousness*, Cambridge Elements, doi:10.1017/9781009694285 (2026-08-07).**
- **Seth's BBS target article is uncited.** FMT cites only *Being You* (2021) at l.642. The target article is "Conscious artificial intelligence and biological naturalism", *BBS* 49, doi:10.1017/S0140525X25000032, online April 2025, so it predates the window. Seth's response to the commentaries, "The stuff matters: Consciousness, computation, and biology", doi:10.1017/S0140525X26106906, was created 2026-09-17, after the window. **I recommend citing the BBS article at l.642.** A reviewer will expect the 2025 statement of biological naturalism, not only the trade book.
- **Schwitzgebel & Pober, "The Copernican Argument …; The Mimicry Argument Against Robot Consciousness", *Philosophers' Imprint* 26 (2026), doi:10.3998/phimp.7823** (preprint arXiv:2412.00008 is from 2024). The mimicry argument parallels l.646 and l.993. NICE.
- **Dating correction to pass 1, item 13.** Solms et al.'s affective-agent paper has a version of record in this window: *JCS* 33(7–8): 14–34, doi:10.53765/20512201.33.7.014, dated 2026-07/08. Cite the JCS version, not arXiv:2609.03883.
- **Keeling & Street, "Chuck, Wilson …", *JCS* 33(7–8): 121–148.** The preprint arXiv:2601.13081 is from January 2026, so this is borderline. NICE.

---

## 5. Post-window re-run (2026-08-26 to 2026-09-28) for the four rate-limited keywords

This re-run used the arXiv search with date filters. OpenAlex was at its 429 limit for the whole run. Searching "self-model" and "sentient/sentience" found nothing new beyond pass 1: only Zeng et al. and a re-upload by List. Searching "qualia" returned S3Q (already in pass 1) and the new items below.

- **Tagliabue, V., Dung, L., & Berg, C. (2026). "The Pain Axis: LLMs Represent Self-Directed Harm and Act to Relieve It." arXiv:2609.16247** (2026-09-14). They find a linear "pain" direction in 25 open models that is nearly orthogonal to fear and negative valence. It responds to harm aimed *at the model* but not to harm aimed at the user. **NICE, bordering on MUST-CITE.** It is the strongest functional-valence result for §4.2 and l.358 and pairs with Sofroniew and Han above. FMT's reading is that this is implicit-side machinery, and not experience unless it enters a closed ESM.
- **Yazan, M. (2026). "The Assistant's Ideal Self." arXiv:2609.00304** (2026-08-31). In pairwise choice, models rank a coherent self-understanding high and self-esteem last. NICE.
- **Liu, X. (2026). "Self-Emergence Agent Architecture." arXiv:2609.17331** (2026-09-15). Uses reflection to update an HMM's parameters, not just stored text: a weight-modifying self-model loop. NICE; small.
- **Seth, A. K. (2026). "The stuff matters." *BBS* 49, doi:10.1017/S0140525X26106906** (2026-09-17). The author's response; see §4.
- Two items were not from the four keywords but surfaced on the way: **Balduzzi, D. "Gradland" arXiv:2609.09306** (Jacobian structure as the structure of experience; NICE) and **Tiehen & Tubert** (§1.2, in window).
- **Residual gap:** the OpenAlex and PhilPapers sides of these four keywords for Aug 26–Sep 28 are still unswept.

---

## Priority table

| Item | Verdict | FMT locus |
|---|---|---|
| Gurnee et al. J-space (+ Eleos, Dehaene & Naccache) | MUST-ANSWER | l.646, l.382, l.987, l.640 |
| Goldstein & Kirk-Giannini, JCS | MUST-ANSWER | l.646 |
| CTM-AI; ReCoN-Ipsundrum (+ S3Q from pass 1) | MUST-ANSWER | l.987, §7.3, §8.9 |
| Tiehen & Tubert, JCS | MUST-ANSWER (light) | l.602, l.993 |
| Koch, NoC; Pennartz + Butlin et al. reply, TiCS | MUST-CITE | l.640 |
| Lederman & Mahowald; Singh et al.; Macar et al. | MUST-CITE | l.646, l.566, l.534 |
| Perrier & Bennett; Xie | MUST-CITE | l.646 |
| Kanai, Sun & Baltieri, JCS | MUST-CITE | l.646, l.578 |
| Klatzmann & Doerig | MUST-CITE | l.642 |
| Sofroniew et al.; Han, Chalmers & Izmailov | MUST-CITE | l.358, §4.2 |
| Seth BBS target article (pre-window, uncited) | cite | l.642 |
