<!-- Action: act. Source: Bartl-label Gmail intake, ingested aIware WSL 2026-07-31 S279. Tracked-by: AIW-135. -->
# Bartl intake — 2026-07-09 → 07-31 (aIware-relevant notes)

MG's self-sent intake notes to `bartl@`. **aIware/FMT/RIM content only** — cross-project notes
(life DSGVO incident, Ivoclar PLM database, Ivoclar UDI-DI/ruska, crucible spiking-brain, social
content angles) were routed to the cross-project inbox and are NOT duplicated here.

## Article reading-flags (MG wants each analysed for FMT/RIM relevance)

| Article | Link | MG's directive |
|---|---|---|
| The Neural Signal of Curiosity & Information Value (OFC) | neurosciencenews.com/ofc-curiosity-information-value-neuroscience-31156 | "Value of information is one of the first things a symbolic machine would learn/store." Ties to the old crucible relational/object-DB projects (~17 predefined dimensions/relations) = grandmother-neuron study opportunities. Maybe of interest to Arthur Stewart / "Scott?". → **bible-code analogy** (see below). |
| Intelligence: nature vs nurture (IQ predicts success) | zmescience.com/…/intelligence-nature-vs-nurture-rep | "Aiware **RIM**." IQ-predicts-success claim → RIM's within-person / anti-g framing. |
| Simulating everything: promise & limits of world models | arstechnica.com/ai/2026/07/simulating-everything-… | (also social) "Are they blind? These lines of thought should naturally lead to **FMT**, not some over-engineered artificial subset of modeling." FMT-vs-world-models positioning. |
| Electric fields help guide neural activity (ephaptic) | bcs.mit.edu/news/electric-fields-help-guide-neural-activity-… | "I find it not so surprising." → architecture-agnosticism / substrate-neutrality anchor (cf. AIW-89 olfaction). |
| A single human neuron far more powerful than thought | scitechdaily.com/a-single-human-neuron-is-far-more-powerful-… | (also crucible) "Proteomic networks are complex enough to compute & learn; obviously a cell would be too. Discuss implications for FMT & crucible." |
| Mirror-neuron decades-old debate settled | psypost.org/scientists-just-settled-…-mirror-neurons | "For every concept/fact you invent you'd find correlated neurons — like the **bible code**. Aiware: analyze, report useful stuff, consider for social/blog." |
| Why vivid dreams leave you exhausted (ATP/sleep) | neurosciencenews.com/atp-sleep-dreaming-memory-31149 | "Might contain evidence for our **FMT sleep explanation**." |
| Bat brain structure | share.google/aimode/xMOdj3dSJtBd387Xy | (low-priority reading flag; spatial/echolocation modeling.) |

## Recurring theme MG flagged twice → the "Bible-Code" didactic pattern
MG (notes on curiosity + mirror-neuron articles): in a brain of such high dimensionality, **every
conceivable mechanism can be — and often is — implemented**, so for *any* concept/fact/thing you
name you can find correlated neurons (grandmother-neuron, mirror-neuron, etc.). "It's like the bible
code, really." **MG explicitly wants this (a) blogged and (b) stored as a didactic pattern for a
future book chapter (Ed 3).** → added to `.claude/knowledge/didactic-patterns.md`; blog feeds AIW-122.
Caution for the pattern: it cuts BOTH ways — it's a caution against over-reading single-cell
correlational findings (post-hoc "you'll always find a neuron"), AND it supports FMT's
"any mechanism can be implemented on a high-dim substrate" (architecture-agnosticism).

## Block-universe / "why is now now" (Philip Goff "Am I a spacetime worm?" substack)
MG's musing (note 10): he accepts 4D spacetime/relativity; the open question is whether it's a
*static block universe* → then something like quantum immortality (every "stage" alive forever, and
"why is now now?"), OR time is genuinely different from space (each moment cut off from the past →
"an immortal trail but no simultaneous perpetual experience") → then "how to reconcile a universal
NOW with GR — it looks like a contradiction." Connects to FMT's **temporal-echo / computational-now**
mechanism (§3.4.4) and the **death/immortality note (AIW-79)**. Possible Goff-substack comment
(social owns engagement). 

## Turing 1936-vs-1952 / Pattee epistemic-cut — FMT §3.4.3 convergence (full source)
This is the full email behind the already-tracked cross-project inbox item ("aiware AND social",
2026-07-29/30). The preprint thesis + MG's pushback + the detailed rebuttal, preserved because the
citations are load-bearing for §3.4.3:

**The preprint's thesis (holds up factually — MG's verification):** the C. elegans-connectome, "could
a neuroscientist understand a microprocessor?" (Jonas & Kording 2017), and the Human Brain Project
(€607M, 2013–2023) failures are ONE structural failure — neuroscience inherited Turing's two
unconnected theories: **1936** universal machine (rate-independent symbol, substrate/speed-indifferent
→ top-down/computational neuroscience, connectome-as-graph) vs **1952** reaction-diffusion morphogenesis
(rate-dependent dynamics, the rates ARE the phenomenon → bottom-up/biophysical). "Mind" sits in the
unreached seam between them; von Neumann / Pattee (epistemic cut) / Harnad (symbol grounding) / Levin
(bioelectric morphogenetic code) all circle the same seam.

**MG's key correction (the connectome→behaviour point):** "a connectome should indeed allow deriving
behaviour — but not by *looking* at it, only by **instancing** it." The 1986 White et al. connectome
gives only topology (which neuron synapses onto which), not the weights/signs/channel-kinetics/membrane-
time-constants needed to instantiate. Three things make it worse than "missing parameters":
1. **Most C. elegans neurons don't spike** — graded/analog; "spiking net" is the wrong model class.
2. **~95% of the functional network is invisible to the synaptic connectome** — Ripoll-Sánchez et al.
   (Neuron 2023) mapped 31,479 neuropeptide ("wireless"/extrasynaptic) interactions, only ~5% overlap
   with the wired connectome.
3. **Randi, Sharma, Dvali & Leifer (Nature 2023):** optogenetic single-neuron activation across 23,433
   pairs — anatomy predicted activity *worse* than measured functional connectivity; real propagation
   between neurons with zero synapse (peptide volume transmission). **Flavell & Gordus (2022):** the
   *same fixed* connectome supports different functional circuits by internal state (fed/starved) via
   slow neuromodulatory gating — one wiring diagram, multiple effective machines. **OpenWorm** spent
   ~15y and never got past crude undulation; the one approach that works fits connectome-*constrained*
   weights from whole-brain optogenetic perturbation, not from the connectome itself.
   → "the connectome" (synapse topology alone) is **not a sufficient object to instantiate**; you need
   the wireless layer + state-dependent gating + closed-loop embodiment folded in. (Ties to the crucible
   sim-spiking-brain build — you INSTANCE it, you don't read it.)

**The FMT hook (§3.4.3):** FMT's two-level ontology (implicit substrate-level non-conscious dynamics
vs explicit virtual transient phenomenal models, "categorically incoherent" across levels) IS Pattee's
rate-independent-symbol vs rate-dependent-construction cut, relocated from genome/organism to
cortex/self-model. Pattee's unresolved problem (how rate-dependent dynamics come to CONSTITUTE a
rate-independent symbol) = exactly the mechanism FMT §3.4.3 argues for but does NOT derive
(self-referential closure = symbol = epistemic cut = morphogenetic code — four labels for one unclosed
seam). Harnad = the mirror-image (bridging the cut from the symbol side). Levin = the closest empirical
instance (rate-dependent voltage gradients condensing into a stable rewritable target-morphology that
then constrains construction). **Suggested:** fold as citable prior-art convergence into §3.4.3
("we name the seam honestly, and so does everyone else").

**Primary sources:** Pattee 2001 "The Physics of Symbols: Bridging the Epistemic Cut"; Jonas & Kording
2017 (PLOS Comp Biol); White, Southgate, Thomson & Brenner 1986; Ripoll-Sánchez et al. Neuron 2023;
Randi/Sharma/Dvali/Leifer Nature 2023; Flavell & Gordus 2022; Levin whitepaper (Allen Center, Tufts);
Turing 1936 & 1952.

## Older batch (Jun 26 – Jul 9) — additional aIware notes

### Sandamirskaya Dynamic-Field-Theory ↔ FMT/criticality synthesis (HIGH VALUE)
MG asked (Bartl, 2026-07-04) for an explanation of **Yulia Sandamirskaya's attractor work** and how it
relates to criticality + FMT/SB-HC4A. The returned synthesis is a rich resource for the **neuromorphic
pillar** (Sandamirskaya = the anchor contact, ZHAW) + FMT criticality formalization (AIW-94) + the crucible
spiking substrate. Key mapping (preserve):
- **DFT / Dynamic Neural Fields (DNF):** Amari-1977 field `τ u̇ = −u + h + ∫f(u)ω(x−x′)dx′ + I`, Mexican-hat
  kernel (short-range excitation, long-range inhibition). Four instabilities: **detection** (bump forms =
  supercritical pitchfork bifurcation), **forgetting**, **selection/WTA**, **sustained activation** (working
  memory). Bump-attractor on a ring = continuous attractor manifold; implemented on ROLLS/Loihi.
- **Attractor↔criticality bridge:** subcritical → rigid strong attractors (stuck basin); supercritical →
  no stable attractors; **edge-of-chaos → metastable attractor dynamics** (power-law avalanches) = DNFs'
  computationally richest regime. SOC (E/I balance) is the homeostatic mechanism holding it there. Working-
  memory attractors sit on the **supercritical side** (SST+/PV+ interneuron gradient sets each area's distance
  from criticality; prefrontal pushed supercritical, early sensory near/subcritical).
- **FMT map:** (1) criticality requirement = DNF detection instabilities ARE local phase transitions → predicts
  DNF circuits show criticality signatures; (2) implicit/explicit permeability ≡ controlling resting-level `h`
  + sigmoid gain `g` (psychedelics ↑permeability = lower threshold/higher gain → sub-threshold breaks through
  as bumps; anesthesia ↓); (3) self-referential closure = DNF+CoS (condition-of-satisfaction) coupled loops
  (a primitive closed self-referential system, "not yet FMT-grade closure but the building block"); (4) qualia
  modality-texture = different DNFs' characteristic dynamics (ω, τ) reverberating under closure; (5) two dims =
  depth (# coupled DNF layers) × extent (recurrent-dynamics : sensory-gain ratio) — both maxed = dream/psychedelic
  corner (locks into own attractor). **SB-HC4A map:** SOC critical point = attractor of the dynamics; weight-
  matrix:bump :: holographic boundary:interior; Bekenstein saturation = DNF at max activation (destroys capacity).
- **Testable prediction FMT gives Sandamirskaya's work:** if DNF neuromorphic architectures show criticality
  signatures (power-law avalanches, 1/f, max info-transfer at detection threshold) AND deepening CoS closure
  correlates with approaching critical dynamics → direct test of FMT's 2015 "criticality + closure are LINKED
  requirements, not independent." → **fold into Sandamirskaya outreach (co-authorship angle) + AIW-94.**

### "Algorithm Zero" (Dustin Sprenger) — uploading-identity paper → AIW-79
Researcher **Dustin Sprenger** (dsprenger@fastmail.com) emailed `research@matthiasgruber.com` (2026-07-03) a
short paper *"Algorithm Zero: Oscillatory Identity in Modular Arithmetic"* (on OSF + Internet Archive; PDF also
in the Bartl email). **Thesis:** internal structure can be preserved while *frame-relative relational properties*
fail to preserve across transfer (N ≡ −1 mod (N+1); algorithm-number A(N,B)=B−N−1 and DoF D(N,B)=B/gcd(N,B) are
base-coupled, not portable) → "structural duplication ≠ personal continuation." A formal wedge against conscious
uploading: preserving pattern-internal structure doesn't establish survival of the original subject unless one
proves the subject is *wholly* pattern-internal (not partly constituted by original frame-coupling) — else
"uploading is successor manufacture, not immortality." **Relevance:** directly engages FMT's mind-copy /
open-individualism / indiscernibility material (**AIW-79** death/immortality note) and the uploading discussion.
He requests technical criticism. → aIware: add Sprenger to contacts (researcher who reached out re FMT-adjacent
identity/uploading); consider for the AIW-79 piece + a possible considered reply. (Not yet a roster contact.)

### Minor
- **"Aiware" (2026-07-07):** just an X link `x.com/i/status/2074266804839464980` (no commentary) — flagged tweet to look at.

## Bartl's assessment (S279, delivered to MG in conversation)
Load-bearing points from reviewing the batch:
1. **The bible-code caution cuts both ways — apply it to FMT's own claims.** "You'll always find a correlated neuron" (mirror/grandmother) is right and worth a blog, BUT it also weakens FMT's "the brain implements the 2×2" and every "evidence for FMT" enthusiasm (dreams/ATP, single-neuron). Pair the pattern with **"correlation is cheap; intervention/ablation is the diagnostic"** — else it's a self-inflicted wound. The ATP-dreaming and single-neuron items are **"consistent with," not evidence** (honest-convergence rule) — don't cite them as confirmation.
2. **The connectome-instancing argument (note 11) is FMT's best §3.4.3 convergence AND an indictment of the crucible minimal-substrate ambition (AIW-91).** "You instance it, you don't read it" is well-supported (wireless peptidergic layer, state-gating, embodiment) — but the crucible substrate is a topology-only object missing exactly those layers. Own it: crucible demonstrates the *closure mechanism in the simplest sufficient system*, and "sufficient" may require more than recurrence. Ties to the CRU-57 fit-window null.
3. **FMT sits on Turing's 1952 (rate-dependent) side more than pure 1936 functionalism** — the criticality requirement IS a rate/dynamics constraint. Reconcile the "ephaptic = not surprising / substrate-agnostic" reflex with this: FMT is agnostic about *which* medium, NOT rate-independent. Make that explicit in §4.4/§3.4.3.
4. **World-models positioning:** they're building the EWM corner without ESM+closure — good "here's the other 3 corners" post, but DON'T publicly over-claim "they'll hit a wall without closure" while the in-silico evidence (CRU-57) is fit-dependent/small. Honesty tension.
5. **Goff/now:** FMT's edge = the NOW is a per-system *computational construct* (§3.4.4), so you DON'T need to reconcile a universal NOW with GR (that's a real contradiction). Presentism-at-the-simulation-level over block-universe-at-the-physics-level. Strong AIW-79 essay angle.
6. **Sandamirskaya DNF synthesis = highest-value deliverable** (concrete neuromorphic formalism for permeability=h/g, closure=DNF+CoS, + a hardware-runnable testable prediction; warm co-author). Some mappings are analogy not derivation (bump=qualia) — label as such. → AIW-94 + outreach.
7. **Sprenger "Algorithm Zero":** begs the question (asserts identity IS frame-coupling). FMT *dissolves* rather than shares the worry — the self is a virtual model; his "frame-coupling" is FMT's non-conscious implicit substrate. Easy FMT-grounded reply from §3.4.2/§4.2.5; he asked for criticism + came to us.
