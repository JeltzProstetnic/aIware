# AIW-265 — Boredom: occupancy check and FMT placement (S321, 2026-09-23)

*Provenance: workflow with 4 readers (psych literature, computational literature, paper audit, crucible audit), one synthesis, and a red-team by Fable 5.1 and Opus, revised after it. The paper lines were checked against `paper/full/four-model-theory-full.md` and the p. 263 quotes against the monograph PDF.*

**MG, 2026-09-23 (crucible session), verbatim:**
1. *"emotions are missing boredom. that is crucial for a creature with consciousness and will."*
2. *"boredom is what drives exploration, experimentation, daydreaming etc"*
3. *"basically boredome is good-didnt happen gaining automatically due to blandness of experience"*
4. *"no bad happenings also cancel boredom"*

## 1. Verdict

Most of what MG said is already published.
- Claims 2 and 4 are held outright.
- Claim 3's "empty centre" reading is Pekrun's.
- Claim 1, as a requirement for consciousness, is supported by neither the paper nor the monograph.

The synthesis's candidate, "boredom is the self-model noticing it has gone flat", did not survive the red-team:
- The error-dynamics affect line already holds it.
- p. 263 does not derive it.
- Crucible's own self-state signal is already defeated by noise.
- The proposed test cannot separate it from its competitors.

Two things remain open:
- **A crucible experiment:** an implemented agent in which boredom gates decoupled simulation.
- **A paper-internal discrepancy larger than boredom:** the monograph makes affect necessary for qualia, and the paper does not.

**In one sentence: cite the drive and do not claim it; keep boredom out of the paper for now (Option D). The only open items are a crucible experiment and the p. 263 affect-for-qualia question, which should reach MG first.**

## 2. Claim by claim

| Claim | Who already holds it | What might still be FMT's own |
|---|---|---|
| (1) Missing from emotion lists; crucial for consciousness and will | **"Missing":** Pekrun et al. 2010 (10.1037/a0019243); Bench & Lench 2013 (10.3390/bs3030459); Gomez-Ramirez & Costa (read as bioRxiv 10.1101/104521). **Agency, for humans:** Elpidorou 2014/2017; Mugon et al. 2018. Wemelsfelder 1985 (10.1007/978-94-009-4998-0_8) runs the entailment the other way: boredom presupposes experience. | No text supports a requirement for consciousness (§4). What holds is weaker: a self-initiating agent needs an endogenous push out of settled states. |
| (2) Drives exploration, experimentation, daydreaming | **Exploration:** Schmidhuber 1991 (a simulated controller) and 2010 (10.1109/TAMD.2010.2056368); Geana 2016; Agrawal et al. 2022 (10.1037/rev0000309); Yu et al. 2019 (10.3389/fnbot.2018.00088). The first robots were Kismet and Bolland & Emami 2007. **Daydreaming:** Smith 1981 (10.1177/001872088102300308); Martarelli & Baillifard (10.31234/osf.io/a9538); Mittner et al. 2016 (10.1016/j.tics.2016.06.004); Sripada 2018. Metzinger 2013 (10.3389/fpsyg.2013.00931) puts mind-wandering onset inside SMT. The causal direction is contested: Bench & Lench say so, citing Eastwood 2012 (abstract read only). **Counter-model:** Agrawal assigns offline computation to *fatigue*. | Only the *implemented* gate, which is a crucible claim and a thin one: DAYDREAMER already uses idleness as a trigger. |
| (3) A good that did not happen, accruing from blandness | **Accrual:** Bench & Lench 2013; Smith 1981 ("monotony"); Agrawal 2022 (a temporally accruing opportunity cost). **Empty centre:** Pekrun 2006 (10.1007/s10648-006-9029-9): boredom is an activity of no value, positive or negative. | The placement is ambiguous. On the p. 226 grid, "good failed to happen" is *disappointment*, which needs an expectation. The other reading, the empty centre, is Pekrun's. Nothing about boredom was found in Rolls (full text unread). Fiske & Maddi and Berlyne are unchecked. |
| (4) Bad happenings cancel it too | **Seeking either valence:** Bench & Lench 2013 and 2019 (10.1037/emo0000433); Wilson et al. 2014; Meagher & Mason 2012. | A passive reset by a bad event is inferred, not tested. Against full symmetry: in Bench & Lench 2019 Study 3 bored people sought the *opposite* valence. |

## 3. The distinction that matters

| Blandness signal | Used by | Noise the agent cannot affect | Noise the agent controls | Unchanging bad state |
|---|---|---|---|---|
| Low change of raw input | Habituation (Marsland 2000) | Least boring | Not boring | Boring |
| **Low change of felt self-state** | **Crucible** (`felt = pos + neg + pain + nerv`, robot_affect.py:287) | Immune | Holds boredom at 0 if it reaches affect | Boring |
| Low pixel-level prediction error | Naive PE, RND | Not boring | Not boring (trap) | Boring once predicted |
| Low PE in agent-relevant features | ICM (Pathak 2017, 10.1109/CVPRW.2017.70) filters noise the agent cannot affect by design | Boring | Trap, as an empirical failure | Boring once predicted |
| Low learning progress / information gain | Schmidhuber, Oudeyer, Geana; Friston 2015 (10.1080/17588928.2015.1020053) | Boring | Boring | Boring once learned |
| Low arousal | Hebb, Kismet, mink | Not boring | Not boring | Not if intense |
| Low engagement / meaning | Goldilocks (Danckert & Elpidorou 2023), MAC (Westgate & Wilson 2018) | Boring | Boring | Can bore; so can overstimulation |

**What MG said:** "blandness of experience", which is ambiguous. Crucible chose change of felt self-state (decisions.md:11639–11660).

**What crucible measures is a crude self-state reading, not an input reading.** It ignores unvalenced noise and is defeated by valenced noise:
- The `fed` flag flickers at the voltage threshold (9 samples).
- A repeated flicker, or σ = 0.01 noise, holds boredom at 0.000 for 900 s.
- Offsetting axes cancel each other.
- Boredom has never been observed live.

**This is FMT's problem, not only crucible's.** The ESM is generated partly "from… current interoceptive and proprioceptive input" (line 223), so interoceptive noise moves it. Hysteresis on `fed` fixes the sensor. It does not make ESM change noise-proof.

**Bored of a bad state:** the change and learning-progress readings allow it, and Bench & Lench 2019 induced boredom with negative stimuli. The chronic-pain counter-case has no source.

## 4. Where it could sit in FMT

**Status.** Boredom is not a model kind. The drive half has no FMT content: mink and Kismet have it without closure, and price-not-barrier rules out "only conscious systems explore". The felt half could be a readout (line 594) of a temporal ESM statistic. That would need an integration step the paper lacks, because line 594's readout is per frame.

**Claim 1 and p. 263.** The paper defines consciousness as "the capacity for subjective experience" (line 144) and gets phenomenality from closure, with no affect term. The monograph says: *"Nicht unbedingt für das Bewusstsein, aber für die Qualia und für die „Subjektivität" sind die Bezugssysteme Gedächtnis und Emotionen, sowie zeitliches Erleben essentiell."* ("Not necessarily for consciousness, but for qualia and 'subjectivity', memory, emotions and temporal experience are essential.") In the paper's broader vocabulary, that makes affect necessary for what the paper calls consciousness, so the two texts disagree. The sentence concerns emotion in general and says nothing about boredom or will, so it does not rescue claim 1. **This decides the boredom question (Q-affect).**

**Option A: §4.2.3, lines 586–594. Boredom triggers decoupled simulation.**
- *Adds:* a trigger, which line 590 never names.
- *Risks:* Metzinger 2013 already says this inside SMT. Agrawal gives offline computation to fatigue. The causal direction is contested.
- *Tension:* a boredom *quale* that starts a daydream is line 594's causal-power clause ("recall or prospection is initiated by what some state felt like"). Line 590 makes onset substrate-determined. The consistent version is that the substrate starts the episode and the felt content steers it, and in that version the trigger carries no FMT content.

**Option B: §4.2.2, lines 564–570. Boredom as the counter-term to the dark room.**
- *Adds:* the strongest internal motive.
- *Risks:* it stacks a speculative claim onto a conceded gap. It must cite Friston, Thornton & Clark 2012 (10.3389/fpsyg.2012.00130) and Friston 2015.
- *Tension:* it forces a choice between the paper's will (line 564) and the 2015 will (p. 114).

**Option C: line 526 / line 708. Boredom as gain on the novelty generator.**
- *Risks:* the three-principle rule (AIW-138).
- *Tension:* line 708's logic predicts *redirection* under monotony ("latch onto whatever input dominates"), not a felt state.
- This is the weakest option.

**Option D: leave it out, or add at most one open question in §9 (near line 1033).**
- Claims 2 and 4 are citations only.
- Claim 1 is unsupported.
- Claim 3's cell is occupied or ill-defined.
- The candidate is occupied and has no working test.
- **Recommended.** The red-team strengthened this.

## 5. The FMT-specific candidate, and why it is not yet one

- **Source:** p. 263: *"die Essenz des bewussten Ich-Erlebens ist beim psychisch gesunden Menschen die scheinbar kontinuierliche, zeitlich scheinbar kausal zusammenhängende, und konsistent erscheinende Wahrnehmung der Veränderung unseres Ich-Modells."* ("In the mentally healthy person, the essence of conscious I-experience is the seemingly continuous, seemingly causally connected and consistent-appearing perception of change in our I-model.") The paper does not contain this, so using it adds a **new postulate** rather than a derivation.
- **Derivation gap:** if I-experience is the perception of ESM change, then zero change predicts *thinned* I-experience (depersonalisation, or Heron's sensory deprivation), not a positive felt state. A felt state needs a second-order monitor of the ESM's rate of change. "Noticing" smuggles that monitor in, which is the homunculus risk (pattern #39).
- **Occupancy:** affect as a rate readout of the agent's own predictive state is already published:
  - Carver & Scheier 1990 (10.1037/0033-295X.97.1.19)
  - Joffily & Coricelli 2013 (10.1371/journal.pcbi.1003094)
  - Kiverstein et al. 2019 (10.1007/s11229-017-1583-9)
  - Hesp et al. 2021 (10.1162/neco_a_01341; AIW-263 doc C2)
  - Miller et al. 2022 (10.1177/17540739211063851)
  - Van de Cruys 2017
  - Darling 2023 (10.1007/s11229-023-04380-3), which treats boredom as tracking "grip"

  This is predictive-processing home ground (pattern #36).
- **Why the test fails:**
  - *Contrast 1* ("self-irrelevant noise bores") has no real competitor. ICM, learning progress, information gain and MAC all predict boredom here.
  - *Contrast 2* ("a predictable self-relevant cycle does not bore") is confounded:
    - In food-monotony studies acceptance fell while the hunger cycle was unchanged: Siegel & Pilgrim 1958 (10.2307/1420336); Schutz & Pilgrim 1958 (10.2466/pr0.1958.4.3.559); Rolls et al. 1981 (10.1016/0031-9384(81)90310-3).
    - Hedonic adaptation (Brickman 1978, 10.1037/0022-3514.36.8.917) flattens the readout, which collapses the contrast into learning progress.
    - Hunger is interoceptive *input*.
  - Nothing fixes "ESM change" in advance, so either outcome can be rescued.
- **A usable test would need:**
  - a pre-registered, non-interoceptive proxy for ESM change;
  - a static-but-meaningful arm (at least 2×3);
  - engagement with the monotony and adaptation data;
  - a contrast separating "ESM changes while error dynamics stay flat" from its converse, since only that separates the candidate from Hesp and Darling;
  - pre-stated outcomes that beat Agrawal and MAC.

  Until then, "Option A later" does not apply.

## 6. A minimal crucible build for claim (2)

Simulation only. The robot would first need `allow_motion`, servos powered off, and `fall_signal(self_induced)`.

0. **Port.** Affect runs only on the robot, so couple it to the gridworld and `fmt_agent`. Add noisy-TV cells, one controllable and one uncontrollable.
1. **Signal.** Add hysteresis on `fed` and a noise floor on felt change. Keep the self-state reading: learning progress would test the competitor instead. Test against the flicker, σ-noise and dt ≠ 1.
2. **Drive.** Make ε (`fmt_agent.py:311–326`, fixed at 0.1 on l. 48) a function of boredom. Compare three arms:
   - fixed ε, matched to the mean ε of the boredom arm;
   - ε driven by boredom;
   - ε driven by a time-shuffled boredom trace.

   Measure coverage after the map changes, and time spent in each TV cell.
3. **Daydream.** When boredom is above threshold and nothing is pending, run goal-free `simulate_forward` rollouts (`models.py:218–235`). Compare against scheduled rollouts and against a fatigue-gated arm (for Agrawal). This is DAYDREAMER's idle trigger plus a threshold, so it gives an implementation result, not a theory claim.

Exploring cancels its own boredom, so the loop limits itself. Test that property explicitly.

## 7. Open questions for MG

- **Q-affect (first):** Does emotion need to be present for qualia? p. 263 says yes and the paper says no. (2015 / paper)
- **Q-requirement:** Does claim 1 go into print? (yes / no)
- **Q-signal:** What makes experience bland? (input change / self-state change / learning progress / engagement)
- **Q-noise:** Should noise the creature can affect bore it? (yes / no)
- **Q-pain:** Can a steady pain become boring? (yes / no)
- **Q-cell:** Is boredom the grid's empty centre, or disappointment without an expectation? (centre / disappointment)
- **Q-will:** Which definition of will holds? (paper / 2015)
- **Q-place:** Where in the paper? (A / B / C / D)
- **Q-drive:** Build the crucible drive before or after Copenhagen? (before / after)

**Where the evidence is thin:**
- Kismet, Cañamero and Frijda are known from secondary sources only.
- Mueller & Dyer: not checked.
- Fiske & Maddi, Berlyne, O'Hanlon, Heidegger, Schopenhauer: not read.
- Eastwood 2012 and Rolls: abstracts only.
- LLM mind-wandering preprints: not read.
- The noise finding rests on 9 samples.

## Red-team dispositions

All points are accepted unless marked otherwise.

| Point | Disposition |
|---|---|
| Fable 1 / Opus F1: contrast 1 is a strawman | Accepted. Dropped; §3 table corrected. |
| Fable 2 / Opus F8: contrast 2 is confounded | Accepted. **Rejected:** Opus's "already refuted by industrial monotony". Paid repetitive work is the static-but-meaningful arm, not changing self-relevance. |
| Fable 3: no fixed operationalisation | Accepted. |
| Fable 4 / Opus F10: p. 263 misread | Accepted. Full quote given; Q-affect added and asked first. |
| Fable 5 / Opus F5: the error-dynamics line occupies the candidate | Accepted. Candidate withdrawn. |
| Fable 6: Pekrun | Accepted. |
| Fable 7 / Opus F7: daydreaming and Metzinger | Accepted. Downgraded to a crucible claim. |
| Fable 8 / Opus F3: crucible's signal is self-state | Both accepted: the sensor fix is Fable's, and Opus's line-223 point stands. |
| Opus F2, F4, F6, F9, F11, F13 | Accepted (table split; monitor gap; Agrawal; 590/594 tension; Q-cell; build step 0 and matched ε). |
| Fable 9 / Opus F12: minor attributions | Accepted. |

## Addendum — MG's reframing, S321 2026-09-23 (after the analysis)

MG, verbatim, two messages:
- *"\"boredom\" is basically just a word for the cognitive level of an urge to forage for food."*
- *"which in a well fed high level creature results in play"*

**What this settles.** Boredom stops being a free-standing emotion and becomes the cognitive-level form of the foraging drive: the urge to leave a depleted patch, generalised to patches of experience. That answers several §7 questions at once:
- **Q-signal:** the bland-making signal is falling *yield* from the current patch — reward or information rate — not change of felt state. Crucible's CRU-182 reads the wrong quantity, which is also why valenced noise defeats it.
- **Q-noise / Q-pain:** a noisy TV yields nothing, so it bores; a steady pain yields nothing new, so it can bore.
- **Q-requirement (claim 1):** a foraging urge belongs to any forager, conscious or not, so boredom is not a requirement for consciousness. Consistent with Option D.
- **Play:** in a well-fed, safe, cognitively capable creature the urge fires with no food to find, and what comes out is play.

**Occupancy — both halves are published, so this is a citation, not a claim.** Crossref-verified:
- **Foraging → cognition:** Hills 2006, *Cognitive Science* 30, "Animal Foraging and the Evolution of Goal-Directed Cognition", `10.1207/s15516709cog0000_50` — argues goal-directed cognition evolved from foraging control. Hills, Todd, Lazer, Redish & the Cognitive Search Research Group 2015, *TiCS*, "Exploration versus exploitation in space, mind, and society", `10.1016/j.tics.2014.10.004`.
- **Boredom as a patch-leaving / opportunity-cost signal:** Agrawal, Mattar, Cohen & Daw 2022, *Psychological Review*, `10.1037/rev0000309` — a normative foraging-style account of boredom and cognitive fatigue.
- **Play from surplus:** Burghardt 2005, *The Genesis of Animal Play* (MIT Press), `10.7551/mitpress/3229.001.0001` — the surplus resource theory: play appears when animals are well fed, safe and have metabolic and cognitive surplus.

**What would still be FMT's own, if anything:** only the placement — which model kind carries the "patch" once foraging goes cognitive (the EWM's current activity, or the ESM's current occupation), and that play is the same urge run inside decoupled simulation when the world offers no deficit. Neither is tested; both would need the §5 occupancy standard before going into print.

**Consequence for crucible (CRU-182):** measure boredom as a declining yield rate of the current activity, with food as the base case, rather than as low change of felt state.

### Addendum 2 — play as a sign of consciousness, and the fly at the window (MG, S321)

MG, verbatim: *"and play is often seen as a sign of consciousness because abstract joy is derived from play, which seems to not serve direct purpose, so it is automatically seen as consciousness adjacent at least, but it is only consciousness adjacent if it causes fun in a scoial situation, because a fly hitting the window again and again could under a simple definition also be seen as play."*

**The fly problem is real and has now happened in print.** Galpayage Dona et al. 2022, *Animal Behaviour*, "Do bumble bees play?", `10.1016/j.anbehav.2022.08.013` — bees rolled balls with no reward and the authors argued it meets Burghardt's (2005) play criteria. So a purely behavioural play definition does let insects in, which is MG's point.

**The joy side, and it is social:** Panksepp & Burgdorf 2000, *Behav. Brain Res.*, `10.1016/s0166-4328(00)00238-2` (50-kHz chirping under tickling and in rough-and-tumble play) and 2003, *Physiol. Behav.*, "'Laughing' rats and the evolutionary antecedents of human joy?", `10.1016/s0031-9384(03)00159-8`.

**Where the criterion is exposed.** Two cases need an answer before this could go into print:
- **Solitary play:** a child or a raven playing alone with an object looks like play with fun but no social situation. Does the criterion exclude it, or is "social" standing in for something else (e.g. fun that is *shared or shareable*, i.e. modelled in another mind — which would make it an ESM-and-other-models criterion)?
- **The bees:** the criterion excludes them only if their object play has no social component, and it does not need to — which is exactly what it is for.

Status: recorded, not claimed. It sits with Q-requirement: none of this makes play or boredom a requirement for consciousness.
