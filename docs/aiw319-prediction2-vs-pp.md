<!-- Action: reference -->
<!-- Tracked-by: AIW-319 -->
# AIW-319 — Prediction 2 (ego-dissolution content) against predictive processing

Checked 2026-10-21 against `paper/full/four-model-theory-full.md` (v23 source) and
`docs/perplexity-2026-10-20-assessment.md` points #2 and #5.

**Verdict: (b).** The experiment in §8.3 cannot separate FMT from predictive processing (PP). A PP model
with modality-specific sensory precision and relaxed self-priors predicts the same modality-specific
tracking, from the same inputs and on the same observables. There is one candidate divergence,
dominance vs. self-contingency (§3.2 below), but it discriminates only if FMT commits to an answer it does
not give now. That choice is MG's.

Line numbers refer to the current file. The "stops short" sentence the brief placed at ~l.947 is at **l.929**.

---

## 1. Prediction 2 as the master states it

**Statement (§8.3, l.973).** "During psychedelic ego dissolution, the content of the altered identity
experience — what the subject reports 'being' or 'becoming' — tracks the dominant sensory input. By
controlling the sensory environment during ego dissolution, the identity content can be predicted and
directed."

**Mechanism (l.975).** Principles 2 and 3 → redirection of the modeling resource + variable permeability.
The ESM is a generated process dependent on input; when permeability rises past the point where normal
self-referential input is disrupted, it "latches onto whatever input dominates the available stream". §6.1
(l.759–761) adds that the ESM is redirected, not abolished, and that tracking should be "input-dependent and
dose-dependent".

**Manipulation and observables (l.975).** Vary the dominant sensory modality (visual, auditory, tactile)
during ego dissolution; measure correspondence between controlled input and reported identity content
with blinded raters and the Ego Dissolution Inventory (Nour et al., 2016).

**Falsification (l.977).** "If identity content during ego dissolution shows no systematic relationship to
the sensory environment — if subjects report identity transformations uncorrelated with the dominant
input — then the redirectable-ESM mechanism is wrong."

**Distinguishing claim (l.979, echoed at l.763, l.877, l.925, l.929, l.1124, l.1158).** PP "predicts
general sensory-driven updating without specifying the modality-specific tracking pattern"; a
modality-specific result "favors FMT's ESM-redirection mechanism over PP's general prior-relaxation
account."

Two properties of the prediction matter for what follows:

- **"Dominant" is undefined.** The master gives no measure of dominance that is independent of the outcome
  (intensity, salience, attention, reliability, or something else).
- **The falsifier tests only the null.** It fires on "no systematic relationship". Any account in which
  identity content is input-driven survives it, so passing it cannot favour FMT over such an account.

---

## 2. The strongest rival

### 2.1 Precision-weighted PP / active inference (REBUS-style)

**Generative model.** A latent self-state *s* (what and where "I" am), world latents, and sensory channels
*m* ∈ {visual, auditory, tactile, interoceptive}, each with likelihood precision π_m. The prior over *s*
has precision π_self, a high-level prior. Posterior belief about *s* weighs the prior by π_self and each
channel's evidence by π_m.

**Psychedelic manipulation.** REBUS: psychedelics relax the precision of high-level priors (Carhart-Harris &
Friston, 2019). Here that means π_self falls with dose.

**What follows.** As π_self falls, the posterior over *s* is set by the evidence, weighted by π_m. The
channel with the highest precision supplies most of the content the system takes itself to be. Raise visual
precision (a bright, structured, attended scene, other channels quiet) and identity content tracks the
visual scene; switch to dominant sound and it tracks the sound. That is modality-specific tracking, derived
in one step.

**Each ingredient is standard PP:**

- Attention is modelled as precision weighting, set per channel (Feldman & Friston, 2010).
- Cue combination weights each modality by its reliability; the more reliable channel dominates the
  percept (Ernst & Banks, 2002; a behavioural result that the precision formalism reproduces).
- Self-attribution is an inference over which sensory signals are best explained as "me" (Apps &
  Tsakiris, 2014; Limanowski & Blankenburg, 2013). The rubber-hand illusion, in which seen stroking
  captures felt ownership (Botvinick & Cohen, 1998), is the waking case of modality-specific capture of
  self-content, and Apps & Tsakiris (2014) treat it as precision-weighted multisensory inference.
- Ego dissolution has published PP/active-inference accounts: self-representation as a hierarchical
  binding posit whose disruption dissolves the self (Letheby & Gerrans, 2017), and deep self-models in
  active inference (Deane, 2021).

**Published vs. derived.** None of the papers above states modality-specific identity tracking under
psychedelics as a prediction; I found none that does. The derivation in this subsection is mine. So l.929
is literally true of REBUS as published. A reviewer will not accept that as a separation, because the step
from REBUS plus per-channel precision to modality-specific tracking is short and uses only standard parts.

**Same inputs, same observables.** Same manipulation (controlled dominant modality during ego dissolution),
same outcome (blinded correspondence between modality and reported identity, EDI score). PP predicts the
result FMT predicts in every arm.

**Free parameters and fitting freedom.**

| Model | Free parameters | Freedom to fit the result |
|---|---|---|
| PP (REBUS + per-channel precision) | π_m for each channel (3–4); π_self and its dose curve; structure of the self-hypothesis space (exclusive → one identity at a time; compositional → blended identity); the map from stimulus properties to π_m | **High.** π_m is not measured independently in the §8.3 design, so any modality outcome can be fitted after the fact by assigning precision. ALBUS (Safron et al., 2025) adds a further dial: at some doses priors strengthen, which imposes expectation on content and lets PP absorb a *failure* of input tracking too. |
| FMT (redirectable ESM) | Definition of "dominant"; the permeability level at which normal self-input is "disrupted"; dose dependence | **Also high.** Without a fixed, prior measure of dominance, "the identity tracked input X, so X was dominant" is circular. |

Fixing dominance in advance would constrain both models, but it constrains them equally. Measure channel
reliability or salience before dosing (e.g. waking cue-combination psychophysics in each participant) and
use it to define the dominant channel: FMT predicts identity follows it, and PP, with π_m set from the same
measurement, predicts the same thing.

**Categorical vs. blended identity is not a separator either.** "Latches onto" suggests one identity at a
time, which a precision-weighted average would not give. PP produces winner-take-all alternation whenever
the hypothesis space is mutually exclusive, as in its account of binocular rivalry (Hohwy, Roepstorff &
Friston, 2008). The hypothesis-space structure is a free choice, so a balanced-input condition (two channels
matched in precision) yields rivalry-like alternation under both models if the modeller chooses so.

### 2.2 IWMT (Safron, 2020)

IWMT makes consciousness depend on a system generating models with spatial, temporal and causal coherence
"for self and world" from a perspectival reference frame, with body-centric networks as the main source of
phenomenal binding (Safron, 2020, abstract). Applied to ego dissolution (my extrapolation; IWMT does not
state it): when the body-centric anchor weakens, the reference frame re-anchors on whichever input best
supplies spatiotemporally coherent structure, and identity content follows that input. This predicts
tracking as well, and plausibly a bias toward the channel with the richest spatial structure (vision, then
touch, then audition) independent of intensity. FMT says nothing about spatial structure, so a
"structure vs. intensity" contrast could in principle split IWMT from FMT. IWMT has the same
free-parameter problem as PP (which input counts as most coherent), it has not committed to this
extrapolation, and Safron's later psychedelic work (ALBUS, above) is built on PP rather than on a
spatial-anchoring rule. It is not a cleaner test than §3.2.

---

## 3. Verdict

### 3.1 (b) — the §8.3 experiment does not discriminate

1. PP with per-channel precision derives modality-specific identity tracking from REBUS in one step,
   using standard components.
2. FMT's "dominant" and PP's "most precise" are both unmeasured in the design. Measuring either beforehand
   fixes both models to the same prediction.
3. The falsifier tests only "no systematic relationship", which PP rejects as well.

The experiment is still worth running. It tests a claim FMT and PP share: identity content during ego
dissolution is input-driven, not random, and can be steered. Read that way it is a test of the redirectable
ESM against IIT, GNW, HOT and AST, which have no mechanism for it. It does not test FMT against PP.

### 3.2 A candidate divergence, conditional on a theory commitment

PP and active-inference accounts of bodily self place self-attribution on **contingency** between a
signal and the agent's own action and interoception, not on the signal's strength. Feedback synchronised
with the participant's heartbeat increases ownership of a rubber hand (Suzuki et al., 2013) and shifts
self-identification and self-location toward a virtual body (Aspell et al., 2013). The master's mechanism is
worded in terms of **dominance**. If those two come apart, the models can too.

**Design sketch (only if MG commits FMT to dominance).**

- *Manipulation:* 2 × 2 within-subject, during ego dissolution (psilocybin, high dose, EDI-confirmed).
  Factor 1: which modality is intense (auditory vs. visual). Factor 2: which modality is self-contingent,
  i.e. pulsed in synchrony with the participant's heartbeat or breathing. Key cells: intense-but-unsynchronised
  in one modality, faint-but-synchronised in the other. Asynchronous-feedback control as in Suzuki et al.
  (2013).
- *Measure:* blinded rating of which modality's content the reported identity draws on; EDI; dominance
  defined in advance (intensity/salience ratings from a waking session).
- *Predictions:* FMT as worded: identity follows the intense modality regardless of synchrony. PP with
  intact contingency inference: identity follows the synchronised modality even when it is fainter.

**Why this is not verdict (a).** Neither side is pinned down.

- PP can predict the FMT outcome too: if REBUS relaxes the agency/contingency inference along with other
  high-level priors, contingency loses its pull and precision alone decides. Whether contingency inference
  survives high doses is a free parameter in PP.
- FMT may already be committed to contingency. Per project notes on the 2015 monograph (Gruber, 2015,
  p. 260), the self/world boundary is drawn by direct vs. indirect feedback, which is a contingency
  criterion. If that criterion governs what the ESM latches onto during dissolution, FMT and PP predict
  the same cell. This page reference is from `project-reference.md`/memory notes; I did not re-read the
  monograph.

So the 2 × 2 discriminates only if MG states that during ego dissolution the ESM follows dominance and
not self-contingency, and only if PP proponents accept that contingency inference persists at the dose
used. The first is a decision for MG; the second is a pre-registration question.

A second, weaker candidate: FMT says the ESM is redirected, not abolished (l.759), which suggests every
ego-dissolution episode carries some identity content. PP permits content-free dissolution when both
π_self and all π_m are low (eyeshades and silence, as in standard psilocybin sessions). If MG commits FMT
to "no content-free dissolution while the ESM runs", the proportion of void reports under sensory
deprivation becomes a test. Without that commitment it is not one.

### 3.3 Replacement text (proposed, not applied)

**§8.3, Distinguishing power (replaces l.979 in full):**

> **Distinguishing power.** IIT, GNW, HOT, and AST have no mechanism for specifying what a subject will
> "become" during ego dissolution. Predictive processing has one. Under REBUS (Carhart-Harris & Friston,
> 2019), psychedelics relax the precision of high-level priors, including priors about the self; when
> sensory channels carry different precisions, belief about the self is then set mainly by the most
> precise channel, and identity content tracks that channel. Precision-weighted accounts of bodily
> self-attribution produce the same pattern in waking, where seen touch captures felt ownership (Botvinick
> & Cohen, 1998; Apps & Tsakiris, 2014). On the observables proposed here, the redirectable ESM and a
> precision-weighted predictive-processing account make the same prediction. The experiment tests their
> shared claim, that identity content during ego dissolution is driven by input rather than random, against
> theories with no mechanism for it.

*Optional final sentence, only if MG commits FMT to dominance (§3.2):*

> The two accounts come apart where the input that dominates by intensity differs from the input that is
> contingent on the subject's own heartbeat or movement: the redirectable ESM follows the first, while
> predictive accounts of bodily self-attribution follow the second (Suzuki et al., 2013; Aspell et al.,
> 2013). Crossing intensity with self-contingency during ego dissolution separates them.

**l.763 (§6.1, replaces the paragraph):**

> IIT, GNW, HOT, and AST have no mechanism for identity content tracking during ego dissolution.
> Predictive processing derives the same tracking from relaxed self-related priors combined with
> modality-specific sensory precision (Section 8.3). It is stated formally in Section 8 as Prediction 2.

**l.877 (end of the PP paragraph; replaces from "particularly the psychedelic-anosognosia connection"):**

> particularly the psychedelic-anosognosia connection (Prediction 1). The identity-content determination
> during ego dissolution (Prediction 2) is shared with predictive processing, which derives it from relaxed
> self-priors and modality-specific sensory precision (Section 8.3).

**l.925 (item 3):**

> 3. **The redirectable and forkable ESM**: A mechanism for identity-content determination during ego
> dissolution (Prediction 2, by redirection; the observable is shared with predictive processing, Section
> 8.3) and for the self-referential representational gradient across alter states in DID (Prediction 3,
> by forking).

**l.929 (replaces the sentence beginning "Neither framework predicts…" and the "stops short" clause):**

> Neither framework predicts a specific relationship between sensory input and identity content during ego
> dissolution. A precision-weighted predictive-processing model does, in one step from REBUS's relaxed
> self-priors (Section 8.3), so this relationship does not separate the theory from predictive processing;
> it separates it from SMT, which describes the conditions for ego dissolution without specifying what
> content replaces the self as a function of incoming stimulation.

(The next sentence in the file, "The specific relationship follows from FMT's permeability mechanism but
not from SMT, …", is absorbed by the replacement and should be deleted.) l.929 is in the "independent
explanatory content" argument. With Prediction 2 shared, that argument rests on Predictions 1 and 3 and the
anesthesia derivation, which the paragraph already lists.

**l.1124 (§10.2, item 2):**

> 2. **Design controlled ego-dissolution experiments** (Prediction 2) — a test of the claim, shared with
> predictive processing, that identity content during ego dissolution follows the dominant sensory input
> (Section 8.3).

If the optional dominance sentence goes into §8.3, append: "; crossing input intensity with
self-contingency separates the redirectable ESM from predictive accounts." Without it, consider dropping
item 2 from this list, which is framed as a change in experimental priorities for adjudicating theories.

**l.1158 (Conclusion; replaces the sentence "Predictions 1 and 2 are coarsely derivable from REBUS, …
(Sections 8.2–8.3)"):**

> Predictions 3 and 4 are distinctive to the Four-Model Theory; Prediction 1 is coarsely derivable from
> REBUS, with the theory's differential content lying in its fine structure (Section 8.2); Prediction 2 is
> shared with precision-weighted predictive processing on the observables proposed (Section 8.3); and
> Prediction 5's structural claim …

**Knock-on, outside the master (not edited):** `.claude/knowledge/prediction-framing.md`, "FMT's strongest
discriminating predictions", item 2 ("PP could converge but FMT's mechanism is more specific") should be
revised to say the observable is shared with PP. `.tex` mirror (`paper/full/latex/paper.tex`) needs the same
changes once MG approves.

---

## 4. Rival predictions for the closure intervention (Table 1b, row "Self-ref. closure", l.198)

FMT's row: disrupting the self-modeling loop degrades *experience*, not merely *report*; falsified if
disrupting the loop itself leaves no-report markers of experience intact.

**GNW.** Conscious access is ignition and global broadcast in a frontoparietal workspace (Dehaene &
Changeux, 2011). Self-referential processing is one class of content the workspace can carry, not a
condition of access. GNW therefore predicts that a disruption confined to the self-modeling loop, with
long-range ignition intact, removes self-related content (ownership, self-relevance judgements) while the
no-report signatures of access to external stimuli survive. That is the result Table 1b names as FMT's
falsifier. If the disruption reaches workspace nodes, GNW predicts that report and no-report markers fall
together, which FMT also predicts. The two theories diverge only for a disruption that removes closure and
spares broadcast; §7.2 (l.873) states no such manipulation exists in brains. In silico the dissociation can
be built, but an ablation can show only functional differences, and FMT claims no capability the
self-model has that the world-model lacks, only differences in cost (l.619). An in-silico closure-off
ablation can therefore separate FMT from GNW only through a cost measure (sample efficiency, depth reached
per unit compute), which GNW makes no prediction about.

**Active inference.** The published active-inference theories of consciousness put a recursive loop at the
centre and so mostly predict FMT's direction. The Beautiful Loop theory (Laukkonen, Friston & Chandaria,
2025) requires "epistemic depth", the recurrent sharing of beliefs throughout a hierarchy via a hyper-model
for precision control, and says explicitly that this is distinct from self-consciousness. It predicts that
disrupting that reflexive loop degrades experience and not only report, as FMT does, but that removing
self-model content while the loop stays intact leaves experience in place. FMT's closure needs a self-model
component that enters the world-model's update rule; the Beautiful Loop needs only the world model's
recursion over its own beliefs. They therefore diverge for a disruption that removes the self-model while
sparing global precision control: Beautiful Loop predicts experience survives, FMT predicts it degrades.
Deane (2021) grounds phenomenal consciousness in a deep self-model's inference about the precision of
action outcomes. On that version, disrupting the self-model degrades experience, which is FMT's
prediction. The difference from FMT is what the loop closes over (action-outcome precision vs. mutual
self/world update), not the direction of the effect. Whyte et al. (2024) state that a minimal, testable
theory is implicit in active-inference models; the abstract does not list its commitments, so I make no
claim about its prediction for this intervention (UNVERIFIED beyond the abstract).

Summary for Table 1b: GNW gives a genuinely opposed prediction for the closure intervention; the
active-inference theories largely share FMT's direction and differ on what must be disrupted.

---

## 5. References (each checked 2026-10-21 against Crossref, OpenAlex or arXiv metadata)

- Apps, M.A.J., & Tsakiris, M. (2014). The free-energy self: A predictive coding account of
  self-recognition. *Neuroscience & Biobehavioral Reviews*, 41, 85–97. doi:10.1016/j.neubiorev.2013.01.029
- Aspell, J.E., Heydrich, L., Marillier, G., Lavanchy, T., Herbelin, B., & Blanke, O. (2013). Turning body
  and self inside out: Visualized heartbeats alter bodily self-consciousness and tactile perception.
  *Psychological Science*, 24(12), 2445–2453. doi:10.1177/0956797613498395 (subtitle from memory; Crossref
  returned the main title only)
- Botvinick, M., & Cohen, J. (1998). Rubber hands "feel" touch that eyes see. *Nature*, 391, 756.
  doi:10.1038/35784
- Carhart-Harris, R.L., & Friston, K.J. (2019). REBUS and the anarchic brain: Toward a unified model of the
  brain action of psychedelics. *Pharmacological Reviews*, 71(3), 316–344. doi:10.1124/pr.118.017160
- Deane, G. (2021). Consciousness in active inference: Deep self-models, other minds, and the challenge of
  psychedelic-induced ego-dissolution. *Neuroscience of Consciousness*, 2021(2), niab024.
  doi:10.1093/nc/niab024 (issue number not checked)
- Dehaene, S., & Changeux, J.-P. (2011). Experimental and theoretical approaches to conscious processing.
  *Neuron*, 70(2), 200–227. doi:10.1016/j.neuron.2011.03.018
- Ernst, M.O., & Banks, M.S. (2002). Humans integrate visual and haptic information in a statistically
  optimal fashion. *Nature*, 415, 429–433. doi:10.1038/415429a
- Feldman, H., & Friston, K.J. (2010). Attention, uncertainty, and free-energy. *Frontiers in Human
  Neuroscience*, 4, 215. doi:10.3389/fnhum.2010.00215
- Hohwy, J., Roepstorff, A., & Friston, K. (2008). Predictive coding explains binocular rivalry: An
  epistemological review. *Cognition*, 108(3), 687–701. doi:10.1016/j.cognition.2008.05.010
- Laukkonen, R.E., Friston, K.J., & Chandaria, S. (2025). A beautiful loop: An active inference theory of
  consciousness. *Neuroscience & Biobehavioral Reviews*, 176, 106296. doi:10.1016/j.neubiorev.2025.106296
- Letheby, C., & Gerrans, P. (2017). Self unbound: Ego dissolution in psychedelic experience. *Neuroscience
  of Consciousness*, 2017(1), nix016. doi:10.1093/nc/nix016
- Limanowski, J., & Blankenburg, F. (2013). Minimal self-models and the free energy principle. *Frontiers in
  Human Neuroscience*, 7, 547. doi:10.3389/fnhum.2013.00547
- Nour, M.M., Evans, L., Nutt, D., & Carhart-Harris, R.L. (2016). Ego-dissolution and psychedelics:
  Validation of the Ego-Dissolution Inventory (EDI). *Frontiers in Human Neuroscience*, 10, 269.
  doi:10.3389/fnhum.2016.00269
- Safron, A. (2020). An Integrated World Modeling Theory (IWMT) of consciousness: Combining integrated
  information and global neuronal workspace theories with the free energy principle and active inference
  framework; toward solving the hard problem and characterizing agentic causation. *Frontiers in Artificial
  Intelligence*, 3, 30. doi:10.3389/frai.2020.00030
- Safron, A., Juliani, A., Reggente, N., Klimaj, V., & Johnson, M. (2025). On the varieties of conscious
  experiences: Altered Beliefs Under Psychedelics (ALBUS). *Neuroscience of Consciousness*, niae038.
  doi:10.1093/nc/niae038
- Suzuki, K., Garfinkel, S.N., Critchley, H.D., & Seth, A.K. (2013). Multisensory integration across
  exteroceptive and interoceptive domains modulates self-experience in the rubber-hand illusion.
  *Neuropsychologia*, 51(13), 2909–2917. doi:10.1016/j.neuropsychologia.2013.08.014
- Whyte, C.J., Corcoran, A.W., Robinson, J., Smith, R., Moran, R.J., Parr, T., Friston, K.J., Seth, A.K., &
  Hohwy, J. (2024). On the minimal theory of consciousness implicit in active inference. *arXiv*
  2410.06633.

Not used: Millière (2017), Kaelen et al. (2015); verified but not needed. A DOI I had for a Kaelen et al.
2016 music-imagery paper resolved to an unrelated article and was dropped. No mirror-neuron literature is
cited.

**What each citation supports here.** Ernst & Banks, Botvinick & Cohen, Suzuki et al., and Aspell et al.
are waking studies; they establish that self-attribution and percepts follow precision and contingency
in waking, and are cited as *consistent with* the PP derivation, not as tests of it under psychedelics. No
cited paper tests identity content under controlled sensory input during ego dissolution.


## MG ruling (S348, 2026-10-21) — salience, not synchrony

Asked whether the redirected ESM follows input dominance or body-contingent synchrony, MG answered with a
first-person report: *"under salvia when you watch a movie you become the main character or object the movie
displays at that moment, or you become prominent objects in the room."*

What this commits FMT to: identity content follows the **most salient** content in the scene (the movie's
main character, a prominent object), and that content is **not synchronised** with the subject's heartbeat or
movement. That is the dominance/salience reading. PP accounts of bodily self-attribution that rely on
contingency (Suzuki et al. 2013; Aspell et al. 2013) predict self-attribution to synchronised input and none to
non-contingent screen content. So the 2×2 intensity × synchrony design sketched above becomes the
discriminating test, with "salience" as the manipulated variable on FMT's side.

**Update (MG, same day):** *"actually i had a second person confirming that several times."* So the report is two people, the second on several occasions, not one.

Status of the reports: **still a vehicle, not citable evidence** — two informal, retrospective, uncontrolled first-person reports under a strong dissociative, not a study. They are stronger than one (independent and repeated), which makes the salience reading a well-motivated hypothesis worth a controlled test; they cannot stand in for that test, the same
discipline as `R5` and the salvia flight case in `didactic-patterns.md` #34. It fixes which reading FMT asserts;
it does not support the reading. Caveat to carry: PP's precision includes attention, so a PP model in which
salience sets precision and contingency inference is switched off under the drug would predict the same; the
design must therefore measure contingency inference independently (e.g. intact rubber-hand synchrony effect
under the drug) for the result to discriminate.


## MG ruling (S349, 2026-10-21) — salvinorin A, not psilocybin

MG: the data is from salvinorin A / Salvia divinorum; psilocybin may not produce outward ego migration because it leaks too much internal processing into consciousness. Applied to master §8.3: drug = salvinorin A (Roth et al. 2002), short action and no significant HR/BP rise (Johnson et al. 2011), dose window below the external-input gating and body-awareness loss reported by Maqueda et al. (2015); the psilocybin question stated as open. MG approved the rest of the AIW-319 text.
