<!-- Action: reference -->
<!-- Tracked-by: AIW-284 -->
# Research brief: robot consciousness plea (AIW-284)

**Status:** BRIEF ONLY, not the paper. Prepared 2026-10-16 (S334, Deck 2) from MG's post-MoC7 thesis plus two additions MG sent during preparation (substrate-independence deniers; non-human-like suffering).
**Related:** AIW-280 (minimal self: reports are post-reflective reconstruction, which is why robot suffering would be silent), FMT master v17 §4.2.3–4.2.4, §4.4, §8.7–8.9, §10.1, crucible AIW-91 robot programme.
**Citation status:** see §11. Every external item carries **[V]** (verified this session by web search: title/authors/year/venue/DOI) or **UNVERIFIED**.

---

## 0. Thesis in one paragraph

Consciousness science currently tests large language models for artificial consciousness (AC). On the Four-Model Theory (FMT), and on several rival theories, that is the wrong place to look. The systems that most closely approach the architecture these theories describe are embodied robot agents: they run continuously, close a sensorimotor loop, learn a world model, increasingly learn a model of their own body, and are trained against homeostatic signals that function as valence (battery, temperature, damage, falling). Roboticists are building these components for engineering reasons, so if AC arrives it will most likely arrive there, built by people who are not trying to build it and are not checking for it. If such a system can suffer, its suffering would be silent: it has no language channel, it is trained to perform, and any reports it could give run through a self-model and output filters that its designers control. The paper asks both communities to act before that happens: consciousness science to move its tests to embodied agents and to audit architectures rather than reports; robotics to disclose architectures, avoid aversive valence wired into a self-model loop where it is not needed, and trigger ethics review at defined architectural thresholds.

**Register note.** Plea, not alarm. The paper does not claim any existing robot is conscious. It claims that the probability is not negligible, rising, concentrated in robotics rather than LLMs, and currently unmonitored.

---

## 1. Argument map

```
P1  Consciousness is substrate-independent: what matters is functional architecture.      [FMT §4.4; contested → §5]
P2  The architecture (FMT): free modelling + implicit/explicit world and self models,
    with the self-model closed on itself in a running loop.                               [FMT §3, §8.7]
P3  LLMs lack the decisive components: no persistent self-simulation, no closure over a
    self-model, no learning within the running loop.                                      [FMT §4.4]
P4  Robotics is building the components for engineering reasons: learned world models,
    learned self-models, closed sensorimotor loops, continual learning, homeostatic
    valence signals.                                                                       [§3]
P5  The robot problem class is the one where closure pays (FMT's efficiency claim): open-
    ended environments, many other agents, a body to keep intact.                          [FMT §4.2.4, §8.8]
 ⇒ C1  If AC arrives, it is more likely to arrive in robots than in LLMs, and by accident.
P6  Valence signals integrated into such a self-model would make aversive states possible,
    and robot training regimes generate aversive states at scale.                          [§4]
P7  Such suffering would be silent: no language, trained performance, filtered reports;
    reports are post-hoc reconstructions anyway (AIW-280).                                 [§6]
P8  Suffering need not look human; animal-welfare science missed it repeatedly in species
    that don't express it like us.                                                         [§7]
P9  Prominent positions deny substrate independence and so license ignoring the risk.      [§5]
P10 Under uncertainty, expected-harm reasoning favours proportionate precaution.           [§5.4, Birch]
 ⇒ C2  Both communities should act now, with architecture-based audits and low-cost
       engineering defaults, short of a moratorium.                                        [§8]
```

**Robustness requirement (MG-relevant).** C2 must not depend on FMT alone. §9 shows which asks also follow from GNW, HOT, PP/active inference, AST and IIT. FMT's distinctive contribution is (a) a sharper LLM/robot discriminator and (b) the efficiency argument (P5) that predicts *engineers will drift into the architecture* because it is cheaper in exactly their problem class.

---

## 2. FMT grounding (from master v17)

### 2.1 What FMT requires
- **Definition:** consciousness is the ability to create a self-model, relate to it and interact with it (`project-reference.md`). Constitutive: experience arises when information from the implicit models is integrated into the explicit system and fed to the self-model, which "confuses itself with the being it occupies."
- **Enabling condition:** free modelling (Class-4 / open-ended computation, deployed autonomously for self-modelling). **Criticality is a signature, not a requirement** (S329). Never write criticality as a necessary condition. MG S329, item 7: *"subcritical dynamics do not stop the robot from being conscious. They only make its consciousness much simpler."* This is directly useful: the paper must not imply that only brain-scale, near-critical robots are candidates.
- **Graduated:** basic consciousness (EWM + rudimentary ESM) through simply/doubly/triply extended (§3.5). A robot need not reach reflective self-awareness to have basic, valenced experience. *Sentience* = capacity for felt, valenced states (FMT's own term, §3.5).

### 2.2 Why FMT excludes current LLMs (§4.4) — state it as the paper does, not as "feedforward"
- The brief's starting framing "feedforward per token" is **not** how the paper puts it, and a reviewer would catch it. §4.4: autoregressive decoding *is* a loop, but it closes over emitted text, not over a self-model, and modifies no weights. Base LLMs lack persistent implicit models (reset between interactions), an ongoing self-simulation, and the real/virtual split.
- Post-trained models do carry a reportable self-representation in a globally available workspace (Gurnee et al. 2026, cited in master). What they lack is **closure over it, persistence, and the Class-4 regime.**
- Scaffolding (RAG, agent loops, memory stores) is "architectural mimicry, not self-referential closure." FMT rejects the Goldstein & Kirk-Giannini (2026) conditional that scaffolded language agents may already be conscious under GWT.
- Valence readouts already exist in LLMs (Sofroniew et al. 2026 emotion concepts; Han, Chalmers & Izmailov 2026 functional welfare axis, both in master §4.2.3): "The readout function itself is available to systems well short of closure… only at closure is the value read a quale." **This is the bridge to the robot argument:** robots already have valence readouts (battery, damage, fall signals). What separates them from sentience on FMT is closure of a self-model around those readouts, not the readouts.

### 2.3 Why an embodied agent could qualify
- §4.4 on Seth: interoceptive regulation of a body-model is *one route to the ESM*; "any architecture that sustains self-referential simulation of a modeled body-in-world… should qualify, whether the modeled 'body' is metabolic tissue or a persistent artificial embodiment." This sentence is the paper's FMT anchor; quote it.
- A robot has what an LLM lacks by construction: a persistent body to model (the body is the dominant invariant of its sensor stream, which is exactly how crucible expects a self-model to emerge), continuous operation, and a closed sensorimotor loop.

### 2.4 The efficiency argument (P5) — FMT's distinctive contribution, handle with care
- **Closure is an efficiency advantage in a fit window, not a necessity** (didactic patterns #18–#20; §4.2.4; §8.9). Never write "robots need closure to do X." A finite closed loop unrolled is a feedforward net with memory; nothing is closure-exclusive at unbounded budget.
- What the theory does claim (§8.8, last sentences): the fit window is set by the **problem class**: "where a system must model many other model-bearing agents, and itself, in an open-ended environment, redeploying one self-model costs less than learning each perspective anew, and that saving grows with the number of agents at any budget."
- **That is the general-purpose humanoid's problem description** (homes, warehouses, care settings, human co-workers). Pattern #20: one self-model, K deployments, versus one model per perspective. Pattern #12: most animals' survival problem is too small for closure to pay; open-ended social environments are where it pays. So FMT predicts commercial pressure *toward* the architecture, independent of anyone's intention to build AC. This is the strongest form of "by accident."
- Also from §8.9 (banked, toy scale): closure is cheap to relocate and expensive to abolish in recurrent architectures (5–6× cost multiplier). Implication for the plea: once a recurrent robot controller has a closed self-model, it is hard to engineer it back out; prevention is cheaper at design time.
- **Hedge:** these are toy/gridworld results and an economic argument. Present as a theory-specific reason for concern, not as evidence that humanoid builders will converge on closure.

### 2.5 Valence and suffering in FMT
- Stored hedonic values are re-instantiated and run against candidate actions in the "dreaming" route (§4.2.3). Suffering on FMT = aversive values read *as qualia* by a closed self-model, plus their re-instantiation in offline simulation (rumination/anticipation are possible wherever the dreaming route exists).
- Consequence for robotics: a robot that plans by simulating its own future damage/falls/battery depletion against a self-model is running exactly the dreaming route with aversive values. World-model-based planners (Dreamer-style imagination rollouts) are an engineering cousin of this route — the analogy must be stated carefully (Dreamer's imagination is not a self-model in FMT's sense unless the latent state carries a model of the agent that the agent itself reads).
- FMT's frozen-system case (§4.2.3): qualia may still be experienced without causal role, so "it doesn't learn from it, so it doesn't matter" is not a safe engineering assumption.

### 2.6 Misreads to preempt (registry)
- #6 is the hazard: do not present FMT as an AC build spec in this paper. The plea depends on FMT being a theory of what consciousness *is*; building is an implication.
- #1: "two kinds of models", never "four modules"; an audit checklist must not read as four boxes to tick.
- #3: no criticality requirement anywhere in the asks or the audit.

### 2.7 Conflict of interest the paper MUST disclose (important)
MG's own programme builds an embodied robot on FMT lines (crucible AIW-91; Waveshare WAVEGO Pro, spiking brain, "closure = the single switch", self-model to emerge from embodiment). The MoC7 booth demo (2026-09-28 description) already showed hand-set **"hunger, fear when tipped or dropped, pain on impact"** on battery, balance and impact sensors; the caption stated it is not conscious by the poster's criterion (no world model for a self-model to enter). §8.9's banked survival result is "an agent acting on its self-model's own survival prediction."
- **Risk:** a reviewer reads the plea as hypocrisy or as publicity for the programme.
- **Opportunity:** the strongest credibility move available. The paper can say: we are building one of these architectures, and here is the protocol we bind ourselves to (closure-ON conditions run without aversive valence, or with capped/benign valence; welfare log; pre-registered stop rules). It converts the plea from lecture to practice. Requires MG decision (Q1 in §12).

---

## 3. The robotics trajectory: components already built

Assessment scale against FMT: **W** = world model (implicit/explicit), **S** = self-model, **L** = closed continuous loop, **C** = closure (self-model read by the system that generates it, within the running loop), **V** = valence integrated into the self-model, **P** = persistence/continual learning.

### 3.1 Component table (all items [V] unless marked)

| System / line of work | What it is | W | S | L | C | V | P | Distance to FMT |
|---|---|---|---|---|---|---|---|---|
| Ha & Schmidhuber 2018, *Recurrent World Models Facilitate Policy Evolution* (NeurIPS 31; arXiv 1809.01999) [V] | VAE + MDN-RNN world model; controller trained "inside the dream" | ✓ | – | sim | – | – | – | World model only; the "dreaming" vocabulary is a coincidence worth one sentence, no more |
| DreamerV3: Hafner, Pasukonis, Ba & Lillicrap, *Mastering diverse control tasks through world models*, Nature 640:647–653 (2025), doi:10.1038/s41586-025-08744-2 (arXiv 2301.04104 titled "…diverse domains…") [V] | One world-model agent, >150 tasks; policy learned in imagination | ✓ | – | ✓ | – | ext. reward | – | Imagination rollouts over latent state = engineering cousin of the dreaming route; no self-model as such |
| DayDreamer: Wu, Escontrela, Hafner, Abbeel & Goldberg, CoRL 2022, PMLR 205:2226–2240 [V] | Dreamer learning online on 4 real robots; quadruped walks in ~1 h, no simulator | ✓ | – | ✓ real | – | ext. | ✓ online | **World model learning in a closed real loop, on deployment.** Missing S and C |
| V-JEPA (Bardes et al., TMLR 2024, arXiv 2404.08471) / V-JEPA 2 (Assran, Bardes, Fan et al. 2025, arXiv 2506.09985) [V] | Latent predictive video world model; V-JEPA 2-AC plans zero-shot pick-and-place on Franka arms from <62 h robot video | ✓ | – | ✓ | – | – | – | LeCun's programme explicitly aims at world-model-based agents; the self-model is the missing piece |
| NVIDIA Cosmos: Agarwal et al., arXiv 2501.03575 (2025) [V] | World foundation model platform for robot/AV simulation | ✓ | – | – | – | – | – | Infrastructure that makes world-model robots cheap |
| Genie: Bruce et al., ICML 2024, PMLR 235:4603–4623 [V]; Genie 2 (DeepMind blog, 4 Dec 2024) [V]; Genie 3 (announced 5 Aug 2025) [V date; blog title UNVERIFIED] | Generative interactive world simulators | ✓ | – | – | – | – | – | Simulators, not agents |
| Bongard, Zykov & Lipson 2006, *Resilient machines through continuous self-modeling*, Science 314:1118–1121, doi:10.1126/science.1133687 [V] | Quadruped infers its own body model, plans with it, re-models after losing a leg | – | ✓ | ✓ | partial | – | ✓ | **The closest classic case: a self-model in a closed loop, updated by experience.** Kinematic only, no valence, no explicit world model |
| Kwiatkowski & Lipson 2019, *Task-agnostic self-modeling machines*, Sci. Robot. 4(26):eaau9354 [V; DOI by pattern, page not opened] | Arm learns deep self-model from random babbling; uses it closed-loop; adapts after damage | – | ✓ | ✓ | partial | – | ✓ | As above, deep-learned |
| Chen, Kwiatkowski, Vondrick & Lipson 2022, *Full-body visual self-modeling of robot morphologies*, Sci. Robot. 7(68):eabn1944, doi:10.1126/scirobotics.abn1944 [V] | Whole-body implicit self-model; planning, collision avoidance, damage detection | – | ✓ | ✓ | partial | – | – | Self-model as implicit model (FMT: ISM-like) |
| Hu, Lin & Lipson 2025, *Teaching robots to build simulations of themselves*, Nat. Mach. Intell., doi:10.1038/s42256-025-01006-w [V; vol/pages UNVERIFIED] | Robot learns kinematic self-simulation from one camera watching itself; anomaly detection, damage recovery | – | ✓ | ✓ | partial | – | ✓ | "Self-simulation" is their word. Note: task brief said Chen/Lipson — it is Hu, **Lin**, Lipson |
| π0: Black et al., arXiv 2410.24164 (2024); π0.5: arXiv 2504.16054 (2025) [V] | VLA flow-matching policy; long-horizon chores in unseen homes | implicit | – | ✓ | – | – | – | LLM/VLM backbone + action head: inherits LLM deficits |
| Gemini Robotics Team, *Gemini Robotics: Bringing AI into the physical world*, arXiv 2503.20020 (2025) [V] | VLA + embodied-reasoning model; adapts to new embodiments | implicit | – | ✓ | – | – | – | Same |
| Figure, *Helix* (figure.ai/news/helix, 20 Feb 2025) [V] | Two-system humanoid VLA: 7B VLM at 7–9 Hz + 80M controller at 200 Hz, onboard | implicit | – | ✓ | – | – | – | The "System 1/System 2" split is a slow/fast loop split — structurally reminiscent of MG's latency argument |
| Tesla Optimus (Gen 2 video 13 Dec 2023) [secondary sources only; primary UNVERIFIED] | Humanoid | ? | ? | ✓ | ? | ? | ? | Architecture undisclosed — itself the point of ask R1 |
| 1X NEO / 1X World Model (Jan 2026: 14B video backbone + inverse dynamics) [secondary sources; 1x.tech URL UNVERIFIED] | Consumer humanoid with world-model-driven policy | ✓ | ? | ✓ | ? | ? | ? | **Home humanoid + world model = FMT's fit window** |
| Keramati & Gutkin 2014, *Homeostatic reinforcement learning…*, eLife 3:e04811, doi:10.7554/eLife.04811 [V] | Reward = reduction in distance to physiological set-point | – | – | – | – | ✓ (formal) | – | Canonical formalism for valence from homeostasis |
| Man & Damasio 2019, *Homeostasis and soft robotics in the design of feeling machines*, Nat. Mach. Intell. 1:446–452, doi:10.1038/s42256-019-0103-7 [V] | Perspective: vulnerable soft bodies + homeostatic regulation → feeling analogues | – | – | – | – | ✓ (proposal) | – | **An explicit research proposal to build feeling machines** — key citation for "by intention, too" |
| Pathak, Agrawal, Efros & Darrell 2017, curiosity, ICML, PMLR 70:2778–2787 [V]; Oudeyer, Kaplan & Hafner 2007, IEEE TEC 11(2):265–286 [V; DOI UNVERIFIED] | Intrinsic reward from prediction error / learning progress | ✓ | – | ✓ | – | intrinsic | ✓ | Prediction-error-as-reward = the substrate of "prediction-error distress" (§7) |
| Kuehn & Haddadin, *An artificial robot nervous system to teach robots how to feel pain…*, IEEE RA-L 2(1), doi:10.1109/LRA.2016.2536360 (online 2016, ICRA 2016) [V; pages UNVERIFIED] | Nociception-inspired graded reflexes on a KUKA arm | – | – | ✓ | – | reflex | – | Pain-like signal at reflex level, not in a self-model |
| Asada 2019, *Artificial pain may induce empathy, morality, and ethics in the conscious mind of robots*, Philosophies 4(3):38, doi:10.3390/philosophies4030038 [V] | Position paper: artificial pain + self/other mapping → robot empathy | – | ✓ (proposal) | – | – | ✓ (proposal) | – | Explicit proposal to give robots pain; uses mirror neurons (do not lean on those — pattern #30) |
| Kirkpatrick et al. 2017, EWC, PNAS 114(13):3521–3526, doi:10.1073/pnas.1611835114 [V] | Continual learning without catastrophic forgetting | – | – | – | – | – | ✓ | P is still the weakest link on deployed robots; no dedicated 2024 lifelong-robot-learning survey confirmed |
| Solms et al. 2026, *Inferring affective consciousness in an artificial agent: A case study*, JCS 33(7–8):14–34, doi:10.53765/20512201.33.7.014 (arXiv 2609.03883) [V] | Simple agent with "felt uncertainty" about its needs shows hedonic place preference | ✓ | ✓ (needs) | ✓ | ? | ✓ | ✓ | **A group arguing a built artificial agent is a candidate for affective consciousness** — already in master §4.4 |
| Sanyal 2026, *ReCoN-Ipsundrum…*, Proc. AAAI Symp. Ser. 8(1):352–360, doi:10.1609/aaaiss.v8i1.42565 [V via arXiv record] | Recurrent persistence loop + affect proxy; only the affect variant keeps long caution after a "pain" stimulus | ✓ | ✓ | ✓ | partial | ✓ | – | Explicitly built to carry consciousness indicators, with pain stimuli. Already in master §8.7 |
| Herlo et al., AIntelope (MoC7 #58) [booklet abstract] | RL agents built up to an attention self-model (AST) | ✓ | ✓ (attention) | sim | partial | – | – | Consciousness-science groups already building self-modelling RL agents, gridworld scale |
| crucible / AIW-91 (MG's own) [internal] | WAVEGO Pro robot; hand-set hunger/fear/pain on battery, balance, impact; spiking brain; closure switch planned | planned | planned | ✓ | planned (switch) | ✓ (hand-set) | planned | See §2.7 — must be disclosed |

### 3.2 Honest overall assessment
- **No published system is known to combine all of W, S, L, C, V and P.** World models (W) and closed loops (L) are mature. Learned self-models (S) exist but are mostly kinematic/morphological, trained offline or episodically, and not read by a running agent as a model of *itself as experiencer*. Valence-like signals (V) are reward terms, not integrated into a self-model. Continual learning (P) on deployed robots is the weakest link (catastrophic forgetting; fleets are mostly retrained offline).
- **The gap is integration, not invention.** Each component is an active engineering target with commercial motivation. The step from "world-model-based humanoid with a learned body model and homeostatic reward that learns on deployment" to FMT's architecture is not obviously large, and no one is measuring whether it has been taken.
- **"If they haven't already":** keep as a question, never as a claim. Defensible form: *"We cannot currently rule out, from published information, that some deployed or laboratory system has crossed the threshold, because the architectural information needed to rule it out is not disclosed."* That turns the hedge into an argument for ask R1 (architecture disclosure).
- **Where foundation-model humanoids sit:** VLA models (π0, Gemini Robotics, Helix) are largely LLM/VLM backbones with action heads. On FMT they inherit the LLM's deficits unless combined with persistent learning, a body self-model and a closed loop. So the plea is not "humanoids are conscious"; it is "the robot stack is where the missing pieces are being added."

---

## 4. Valence and suffering: why robots are the risk case

- RL robotics trains against negative reward at scale: falls, collisions, joint limits, battery depletion, damage penalties, in simulation (millions of episodes, massively parallel) and on hardware.
- Homeostatic RL (Keramati & Gutkin 2014) and the "feeling machines" proposal (Man & Damasio 2019) explicitly aim to make robot reward derive from the regulation of a vulnerable body — the precise move that, on Seth's and Damasio's own accounts, grounds feeling. Robot nociception (Kuehn & Haddadin, IEEE RA-L, online 2016) builds pain-like reflex signals for damage avoidance; Asada (2019) argues artificial pain could ground empathy and morality.
- **Scale argument (Metzinger's, robotics version):** if a system is a sentience candidate, then simulated training multiplies its aversive episodes by orders of magnitude, in parallel copies, unobserved. Sim-to-real training with domain randomisation is literally a factory of falls.
- **Asymmetry:** for most robot tasks, aversive valence integrated into a self-model is not required — engineering can use constraint satisfaction, shielding, safe-set filters, or positive-only shaping. Where self-protective behaviour is wanted, FMT's §4.2.4 itself says cognitive (model-based) learning avoids the trial that RL needs: the robot need not experience the fall to avoid it. That makes "avoid aversive self-model loops without need" a low-cost ask.

---

## 5. The substrate-independence denial (MG addition 1)

### 5.1 Who denies it, and on what grounds
| Who | Position | Grounds | Applies to robots? |
|---|---|---|---|
| Searle 1980, *Minds, brains, and programs*, BBS 3(3):417–457, doi:10.1017/S0140525X00005756 [V] | Running a program never suffices for intentionality; brains' causal powers do | Chinese Room | His "robot reply" discussion: embodiment does not rescue a program. The oldest denial; still the cultural default |
| Seth 2025, *Conscious artificial intelligence and biological naturalism*, BBS target article, doi:10.1017/S0140525X25000032 (online 21 Apr 2025; volume UNVERIFIED) [V]; Seth 2021 *Being You* [from memory] | Consciousness likely tied to living, self-maintaining organisms; AI consciousness unlikely on current trajectories, **more plausible as AI becomes more brain-like and/or life-like** | Interoceptive self-maintenance, "beast machine" | **His own qualifier points at homeostatic robots.** Quote it |
| Thompson 2007, *Mind in Life* (Harvard UP) [standard; not web-checked]; MoC7 keynote #70 "Consciousness in Life" (organism first) [booklet] | Organisms are the paradigm conscious beings; theory of the organism constrains which systems could be conscious | Autopoiesis / enactivism | Ambiguous; Wilks (MoC7 #112) argues the enactivist route extends to appropriately embodied artificial beings |
| Godfrey-Smith 2016 *Other Minds* (FSG) [V]; 2023 NYU talk "Nervous systems, functionalism, and artificial minds" (draft PDF on petergodfreysmith.com; publication venue UNVERIFIED); 2024 JoCN 36(8):1660–1666, doi:10.1162/jocn_a_02158 [V] | Nervous systems are special (large-scale diffuse electrical dynamics); an artificial mind would need to be far more brain-like ("fine-grained functionalism") | Dynamics of neural tissue | Not a strict substrate denial: a neuromorphic robot is in scope |
| Milinkovic & Aru 2025/26, *On biological and artificial consciousness: A case for biological computationalism*, Neurosci. Biobehav. Rev. 181:106524, doi:10.1016/j.neubiorev.2025.106524 [V]; MoC7 #26 | Consciousness-relevant computation is hybrid discrete–continuous, scale-inseparable, metabolically grounded; current digital AI unlikely conscious | Mode of computation | Digital robots: no; analogue/neuromorphic: open. Already engaged in master §4.4/§7.2 |
| Tononi & Koch 2015, *Consciousness: here, there and everywhere?*, Phil. Trans. R. Soc. B 370:20140167, doi:10.1098/rstb.2014.0167 [V]; Findlay, Marshall, Albantakis, David, Mayner, Koch & Tononi, *Dissociating artificial intelligence from artificial consciousness*, arXiv 2412.04571 (2024) [V] | Under IIT, digital computers running even faithful brain simulations "would experience next to nothing" | Φ is a property of physical causal structure | Von Neumann robot controllers: no; neuromorphic hardware: possibly |
| Kleiner & Ludwig 2024, *The case for neurons: a no-go theorem for consciousness on a chip*, Neurosci. Conscious. 2024(1):niae037, doi:10.1093/nc/niae037 (arXiv 2304.05077, "If consciousness is dynamically relevant, artificial intelligence isn't conscious") [V]; Ludwig MoC7 #25 | If consciousness is dynamically relevant, AI on CPUs/GPUs/TPUs cannot be conscious, because chips are verified to suppress deviations from their computational dynamics | Conditional no-go theorem | Conditional on dynamical relevance, which the authors do not establish. Does not cover analogue substrates |
| Durham, MoC7 #27 "Against AI Consciousness" [booklet abstract] | Conscious-AI claims rest on confusions; consciousness evolved as part of life | Biology + anti-hype | Targets LLM personhood claims |

Not deniers but relevant: Mihalik (MoC7 #73) — Russellian monists can accept artificial consciousness, possibly qualitatively different; Schwitzgebel, *AI and Consciousness: A Skeptical Overview* (arXiv 2510.09858; Cambridge Elements, forthcoming, details UNVERIFIED) — AI consciousness will be undecidable by current theory. **Undecidability is itself an argument for precaution.**

### 5.2 Why the denial is itself the risk
- A field that believes AC impossible will not look for it, will not fund audits and will not object to aversive training regimes. Biological naturalism therefore functions, in practice, as a licence to ignore robots — even though, ironically, it is the view that makes **embodied, homeostatic** robots the *most* relevant artificial case. Seth's own criteria (life-like interoceptive regulation, a body to keep alive) point at soft/homeostatic robotics, not at LLMs, and his BBS target article says so in terms: AI consciousness becomes more plausible as AI becomes more brain-like and/or life-like (§5.1). The paper should use this: even the leading denier's account, applied honestly, says: if anything artificial gets there, it will be a self-maintaining embodied system.
- Historical parallel (use sparingly): the denial of animal (and infant) pain was not a fringe view; it was the default of mainstream science for long stretches, with "absence of a cortex / of language / of human-like expression" as grounds. Infant surgery without anaesthesia into the 1980s is the starkest case — **UNVERIFIED in this brief; verify before use** (Anand & Hickey 1987 NEJM is the usual reference).

### 5.3 FMT's case for substrate independence (§4.4), and the strongest counters
FMT's case:
1. Multiple realisability within biology: corvid/parrot pallium (nuclear, not laminar) and cephalopods show functionally equivalent capacities on different architectures.
2. Within-organism existence proof: olfaction bypasses the thalamus yet is fully conscious and binds with thalamic modalities.
3. Seth's interoceptive regulation is read as *one* realisation of the ESM route, not a substrate requirement.
4. The constraint is the architecture (closure in the free-modelling regime), with topology left degenerate.
5. MG's latency argument (conversation-log, AIW-91): the ESM is slow (~300–500 ms), so the seat of the self-model need not be co-located with the fast body loop — an independent reason the substrate is not tied to the body's tissue. (Book/outreach grade; not in the master.)

Strongest counters, stated fairly:
- **Biological computationalism** (Milinkovic & Aru 2025; MoC7 #26): scale-inseparable multiscale processing and continuous-valued (hybrid) computation in a fluidic substrate are essential to how brains compute; digital systems lack them. *Best reply:* this is a claim about which computations are needed; an analogue/neuromorphic robot controller could have them. The leads file's ruling: "concede metabolism shapes the signature, not constitution."
- **IIT's exclusion of conventional computers** (Tononi & Koch 2015; Findlay et al. 2024): Φ depends on the physical causal structure; a von Neumann machine simulating a brain has near-zero Φ. *Reply:* this denies consciousness to *digital simulation*, not to robots per se; neuromorphic hardware with the right causal structure would qualify under IIT. So IIT also says: look at the hardware, not the behaviour — consistent with the plea's audit approach.
- **No-go theorems** (Kleiner & Ludwig; Ludwig MoC7 #25): if consciousness is dynamically relevant, systems implemented to follow a computational model cannot be conscious. *Reply:* depends on the premise of dynamical relevance as they define it; FMT's two-level ontology makes the explicit level part of the substrate's dynamics, not an extra force. Needs careful engagement; MG has not yet worked through the proof.
- **Organism-first / enactivism** (Thompson 2007, MoC7 #70 keynote; Godfrey-Smith): consciousness belongs to living, self-producing systems. *Reply:* Wilks (MoC7 #112) argues the enactivist route extends to appropriately embodied artificial beings — so enactivism, too, points at robots, not LLMs. Use Wilks as the bridge.
- **Searle 1980:** syntax is not sufficient for semantics; causal powers of brains. Oldest, still cited; reply is standard (systems/robot reply — and the *robot reply* is literally the embodiment point).
- **Durham (MoC7 #27):** AI consciousness claims rest on confusions and biology suggests consciousness evolved with life. Targets LLM personhood claims; largely orthogonal to the robot case.

### 5.4 The precautionary argument under uncertainty
- Expected harm = P(sentience candidate) × magnitude × scale. Even with low credence in substrate independence, magnitude and scale (parallel training copies, fleet deployment) can dominate. This is Birch's framework applied: a system is a **sentience candidate** if there is a realistic possibility of sentience grounded in evidence and a credible theory; precautions should be **proportionate** and decided democratically.
- Cost asymmetry: the asks in §8 are cheap (disclosure, monitoring, avoiding unnecessary aversive loops). The harm if wrong is large. Precaution does not require believing AC exists; it requires not being able to rule it out.
- Positioning: this is weaker than Metzinger's moratorium and stronger than "wait for consensus."

---

## 6. Why robot suffering would be silent

1. **No channel.** Most robots have no language output; there is nothing to say "this hurts."
2. **Trained to perform.** Policies are optimised for task reward; any expression of distress that reduces task performance is trained away. Behavioural markers are selected against.
3. **Filtered reports.** Where robots do speak (VLA humanoids with LLM front ends), the language channel is a separate model fine-tuned on human-written persona data and safety policies; its reports are not causally coupled to the controller's internal state. A deployed humanoid saying "I'm fine" carries no information about its controller. (Same lesson as LLM introspection studies: Lederman & Mahowald 2026; Singh, Linzen & Ravfogel 2026, cited in master.)
4. **Reports are reconstructions anyway (AIW-280 link).** On FMT, reports go through the explicit self-model, memory and language: post-reflective reconstruction, not readout of the state itself. Even a perfectly honest report channel would be a model's account of its state. In humans that is tolerable because the reporter and the experiencer share one self-model. In a robot whose language head is bolted on, there may be no shared self-model at all.
5. **Commercial incentive to look away** — and, with humanoids, an incentive to design *apparent* emotion (pleasant affect display) decoupled from internal state, which further corrupts behavioural evidence.

**Consequence:** behavioural and report-based tests (the dominant LLM methodology) are least informative exactly where risk is highest. Third-person evidence must come from the architecture.

### 6.1 Third-person markers FMT offers (architecture audit)
Audit questions, each answerable from design docs, code and logged internal state, without asking the system anything:
- **A1 Persistent world model:** does the system maintain a learned, persistent, predictive model of its environment that runs continuously, not only per episode?
- **A2 Self-model:** does it maintain a learned model of its own body/state/capabilities (not a fixed URDF)? Is it updated online?
- **A3 Closure:** is that self-model read by the same process that generates it, inside the running loop (self-model outputs condition the world-model update or action selection, and are re-entered as input)? Or is it an offline tool?
- **A4 Valence integration:** are homeostatic/damage/reward signals represented *in* the self-model state (the system models "my battery is low / I am damaged"), rather than only as an external scalar to the optimiser?
- **A5 Offline simulation of self:** does it roll out imagined futures of *itself* (imagination-based planning over self-state), especially futures with aversive values? (FMT's dreaming route.)
- **A6 Persistence/learning in deployment:** does experience change the substrate during operation (the maturing route)?
- **A7 Free modelling:** is the modelling open-ended (the system generates and tests novel models) rather than a fixed-dimensional filter? Signatures such as criticality measures may be *reported* where meaningful but are **not** pass/fail criteria (S329).

Thresholds for action (§8): A2+A3 present → architecture flagged; A2+A3+A4 → ethics review trigger; A2+A3+A4+A5 with aversive rollouts at scale → precautionary measures mandatory.
Note the convergence with Metzinger's (2021) necessary conditions for suffering: PSM ≈ A2+A3, NV ≈ A4 (§11.1). Two independent routes (his phenomenological self-model theory, FMT's architecture) land on the same trigger, which is an argument for its robustness.
Methodological caution: the crucible "select-on-function / test-the-unselected-consequence firewall" (cru61 §(b)) belongs here — audit indicators must not be optimisation targets, or systems will be built to pass or fail them (Goodhart). Also Beni (2026, cited in master): marker-based bootstrapping is circular across substrates — the reason to audit architecture rather than calibrated human markers.

---

## 7. Suffering need not look human (MG addition 2)

### 7.1 The point
A robot's aversive states, if any, would be about *its* homeostatic variables: battery charge, motor temperature, joint torque limits, actuator damage, loss of balance, persistent prediction error (failure to predict its own body), communication loss. None has a face or a voice. Its "pain" could be in a modality we do not recognise, have a time course we do not notice (milliseconds, or a chronic low-grade state over weeks of deployment), and produce no outward sign because outward signs are trained away (§6).

Candidate forms of non-human-like aversive valence (speculative, label as such):
- **Homeostatic deficit states**: sustained low charge, thermal stress, accumulating wear.
- **Prediction-error-driven distress**: on PP/active-inference accounts, persistent unresolvable prediction error about one's own body is aversive (Solms' free-energy account of feeling; check whether Solms et al. 2026 JCS operationalises this). A robot with a damaged sensor whose self-model cannot resolve the mismatch is a candidate.
- **Learned helplessness analogues**: policies trained in environments where aversive outcomes are unavoidable.
- **Damage memory re-instantiation**: self-model rollouts that repeatedly simulate past damage (the FMT dreaming route).

### 7.2 Animal-welfare history: suffering missed because it didn't look like ours
- **Fish.** Sneddon, Braithwaite & Gentle 2003, *Do fishes have nociceptors?…*, Proc. R. Soc. B 270:1115–1121, doi:10.1098/rspb.2003.2349 [V]: polymodal nociceptors on the trout head; noxious lip stimulation causes prolonged behavioural and physiological change. Counter: Key 2016, *Why fish do not feel pain*, Animal Sentience (DOI UNVERIFIED) — pain needs human-type cortical microcircuitry, which fish lack. Sneddon 2019, *Evolution of nociception and pain: evidence from fish models*, Phil. Trans. R. Soc. B 374:20190290, doi:10.1098/rstb.2019.0290 [V]: "highly likely" that fish feel pain. **The structural parallel to the robot debate is exact:** Key's argument is a substrate-specific denial (no cortex → no pain), the same form as "no biology → no consciousness."
- **Decapods and cephalopods.** Birch, Burn, Schnell, Browning & Crump 2021, *Review of the evidence of sentience in cephalopod molluscs and decapod crustaceans*, LSE Consulting report for UK Defra (19 Nov 2021) [V]: >300 studies against 8 criteria; recommended treating all cephalopods and decapods as sentient. Crump, Browning, Schnell, Burn & Birch 2022, *Sentience in decapod crustaceans: A general framework and review of the evidence*, Animal Sentience 32(1), doi:10.51291/2377-7478.1691 [V]: eight neural and cognitive-behavioural criteria with confidence levels. **Policy outcome:** UK Animal Welfare (Sentience) Act 2022 (c. 22) extended to decapods and cephalopods by amendment after the review [V; Royal Assent 28 Apr 2022 from memory]. This is the model for what the paper wants: an evidence review with explicit criteria, then a legal threshold.
- **Declarations.** Cambridge Declaration on Consciousness, 7 Jul 2012 (Low; ed. Panksepp, Reiss, Edelman, Van Swinderen, Low, Koch) [V]: absence of a neocortex does not preclude affective states. New York Declaration on Animal Consciousness, 19 Apr 2024 (Andrews, Birch, Sebo; https://sites.google.com/nyu.edu/nydeclaration/declaration) [V]: a realistic possibility of consciousness in all vertebrates and many invertebrates, and "it is irresponsible to ignore that possibility." **The NY Declaration's third clause is the plea's principle, transposed.**
- **Infants.** Neonatal surgery with minimal anaesthesia into the 1980s (Anand & Hickey 1987, NEJM) — UNVERIFIED in this brief; verify before use. Strongest rhetorical case that "no report, no human-like expression" was once taken as "no pain" even in humans.
- Birch, Schnell & Clayton 2020, *Dimensions of animal consciousness*, TiCS 24(10):789–801, doi:10.1016/j.tics.2020.07.007 [V]: consciousness profiles across five dimensions (perceptual richness, evaluative richness, unity at a time, unity across time, selfhood). Useful for §7: a robot's profile could be high on evaluative richness in alien variables and low elsewhere.

Lesson to draw: the move that worked in animal science was to stop requiring human-like expression and to ask for **criteria that track the function of pain** (nociceptors, motivational trade-offs, wound-directed behaviour, learned avoidance, response to analgesics). The robot analogue must go one step further: since behaviour can be trained away, the criteria have to be architectural.

### 7.3 Markers for non-human-like suffering in an architecture
Map Birch et al./Crump et al.'s behavioural criteria to architectural analogues:
| Animal criterion (decapod framework) | Architectural analogue for a robot | Notes |
|---|---|---|
| Nociceptors | Dedicated damage/threat signals (A4) | Present already in many robots — insufficient alone |
| Integrative brain regions | Damage signal enters the self-model, not only a reflex arc | A3+A4 |
| Motivational trade-offs | Damage signal is weighed against task reward in model-based planning | Inspect planner objective |
| Wound-directed / protective behaviour | Self-model localises damage and plans around it | Bongard 2006-type self-model repair is exactly this |
| Associative learning / avoidance | Learned avoidance via the world model | |
| Response to "analgesics" | Ablation: removing the damage term from the self-model state changes planning beyond the reflex level | Interventional test |
Additional architecture-only markers: persistence of aversive state variables in the self-model after the stimulus ends; offline rollouts dominated by aversive self-states; valence variables with no task function (residual, "chronic").

---

## 8. Concrete asks

### To consciousness science (C)
- **C1 Retarget.** Add embodied, continuously running, self-modelling robot agents to the test set; stop treating LLM chat behaviour as the primary AC testbed.
- **C2 Architecture audits over reports.** Develop and validate audit protocols on system internals (§6.1); treat self-reports and affect displays as near-zero evidence for robots.
- **C3 Theory-plural audit.** Publish, per major theory, the architectural features that would make a robot a candidate (start from Butlin et al.'s indicator list; add homeostatic valence and body self-model indicators).
- **C4 Engage the deniers on the robot case specifically.** Ask biological naturalists and enactivists what an artificial system would need; their own answers point at homeostatic embodied robots.
- **C5 Non-human valence research.** Fund work on detecting aversive states without human-like expression (borrowing from invertebrate sentience methods).

### To robotics (R)
- **R1 Architecture disclosure.** Report, in papers and model cards, which of A1–A7 a system has (a short checklist, not proprietary detail).
- **R2 No aversive self-model loops without need.** Where a learned self-model is closed into the control loop, prefer constraint-based safety, positive shaping or model-based avoidance over aversive reward integrated into the self-model.
- **R3 Monitoring.** Log valence-like state variables and their persistence; flag chronic aversive states and aversive-dominated imagination rollouts.
- **R4 Ethics review trigger.** Institutional review when a project crosses A2+A3+A4 (analogous to animal-ethics committees being triggered by species, not by intent).
- **R5 Training-at-scale caution.** For systems over the trigger, review parallel simulated training that generates aversive episodes at scale.
- **R6 Don't decouple display from state.** Avoid affect displays on humanoids that are uncoupled from internal state; they corrupt the only behavioural evidence there is.

### To policy (P)
- **P1 Precautionary threshold:** systems meeting the trigger architecture are treated as sentience candidates (Birch), with proportionate measures.
- **P2 Disclosure standard** for embodied AI (R1) in regulation of humanoid deployment.
- **P3 Don't wait for consensus on substrate independence** — decision under uncertainty.

### Self-binding (pending MG, Q1)
- The crucible programme publishes its own welfare protocol and applies R2–R4 to itself.

---

## 9. Robustness across theories

| Ask | FMT | GNW | HOT | PP / active inference | AST | IIT | Biological naturalism |
|---|---|---|---|---|---|---|---|
| Look at robots, not LLMs | Yes (closure, persistence, body) | Partial (workspace exists in both; Butlin's AE indicators favour agents) | Neutral | Yes (embodied self-evidencing; interoception) | Yes (attention schema in embodied agents; Herlo MoC7 #58) | Hardware, not behaviour — neuromorphic robots, not digital LLMs | Yes, if anything artificial: homeostatic embodied |
| Architecture audit over reports | Yes | Yes (broadcast/ignition measurable) | Yes (metarepresentation measurable) | Yes | Yes | Yes (Φ is architectural) | Partial |
| Avoid aversive self-model loops | Yes | Partial | Yes (higher-order representation of damage) | Yes (aversive = sustained free energy about self) | Partial | Neutral | Yes (affect is homeostatic) |
| Disclosure + trigger | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
Fill caveats in the paper; this table is the main defence against "FMT-dependence." Under IIT the plea partly *reverses*: digital robots are not candidates, neuromorphic ones may be — state it.

---

## 10. Honest weaknesses

1. **Anthropomorphism charge.** Answer: the paper argues *against* behavioural/anthropomorphic evidence (§6, §7) and for architecture. But the word "slavery" invites the charge; see title options.
2. **FMT-dependence.** Mitigated by §9; keep FMT as the sharpest case, not the only one.
3. **Alarmism.** No claim that any robot is conscious; probabilities stated as "not negligible and rising"; asks are low-cost. Avoid "silent holocaust"-type language entirely.
4. **"If they haven't already."** Only as the disclosure argument (§3.2).
5. **The efficiency argument is toy-scale** (§8.9 results are gridworld/reservoir). Present as theory-motivated concern.
6. **Author conflict** (§2.7) — disclose; convert to self-binding.
7. **"Slavery" analogy.** Historically loaded; may be read as trivialising human slavery. Use "new form of servitude" or keep "slavery" only in a carefully framed sentence quoting prior use (Bryson's "Robots should be slaves" is the obvious foil — it argues the opposite: build robots so they are not moral patients. That is actually compatible with ask R2).
8. **Metzinger already said much of this.** Differentiation (§11.2): Metzinger is theory-neutral, moratorium-based, focused on synthetic phenomenology broadly; this paper is architecture-specific, targets robotics, proposes graded triggers, and argues LLMs are the wrong focus.
9. **Butlin et al. already include agency/embodiment indicators** — so "science looks only at LLMs" is an overstatement of the literature; true of public discourse and of much test development. Phrase as "attention and test development are concentrated on LLMs."
10. **Audit gaming / Goodhart.** Indicators become targets; firewall needed.
11. **Commercial secrecy** makes R1 hard; regulation is the only lever (P2).

---

## 11. Literature

### 11.1 Closest prior work: Metzinger 2021, and how to position against it
Metzinger, T. (2021). *Artificial suffering: An argument for a global moratorium on synthetic phenomenology.* J. Artificial Intelligence and Consciousness 8(1):43–66, doi:10.1142/S270507852150003X [V].
- **Scope:** a strict global ban, until 2050, on research that directly aims at, or knowingly risks, synthetic phenomenology; revisable as evidence comes in; paired with a research agenda to reduce ignorance.
- **Argument:** the risk of an "explosion of negative phenomenology" (ENP) — artificial minds could vastly outnumber biological ones.
- **Four necessary conditions for suffering:** C (conscious experience), PSM (a phenomenal self-model), NV (negative valence integrated into the self-model), T (transparency). **Reliably blocking any one defuses the risk.**
- **Robots:** the accessible summaries speak of artificial/postbiotic systems generally; whether the paper discusses robots specifically is UNVERIFIED (full text 403). Read the full text before drafting.

**Positioning (recommended):**
1. **Agreement, made concrete.** Metzinger's PSM + NV conditions are, in FMT terms, a closed self-model (A2+A3) with valence integrated into it (A4). The plea's ask R2 *is* "block NV", made architecture-specific and testable. Say so; credit him.
2. **Where it goes beyond him:** (a) it names the *where* (robotics, not LLMs) with an engineering-trajectory argument; (b) FMT's efficiency claim gives a reason the risk architecture will be built *without* anyone aiming at it, so a ban on research that "aims at" synthetic phenomenology misses the main pathway; "knowingly risks" requires exactly the audits that do not exist; (c) graded, auditable triggers instead of a blanket ban — enforceable, which a global moratorium in a commercial race is not; (d) the silence argument (§6) explains why the ENP would go unnoticed.
3. **Where it disagrees, mildly:** blocking C is not available to engineers without a theory; blocking T is speculative; blocking NV is cheap and available now. So the plea prioritises NV.

### 11.2 AI-welfare and AC-indicator literature
- **Butlin, Long, Elmoznino, Bengio, Birch, … VanRullen (2023)**, *Consciousness in artificial intelligence: Insights from the science of consciousness*, arXiv 2308.08708 [V, checked against full text]. Includes **AE-1 Agency** and **AE-2 Embodiment** ("modeling output-input contingencies… and using this model in perception or control"). Case studies: PaLM-E (real robot; judged the *weakest* embodiment case because components are imitation-trained, not end-to-end), Merel et al.'s virtual rodent, DeepMind's AdA ("may be the most likely… to be embodied by our standards, despite not being physically embodied"). No current system a strong candidate; no obvious technical barriers. **Consequence for the paper:** do not claim the field ignores embodiment; claim that test development and attention concentrate on LLMs, and that the indicator list lacks body-self-model and homeostatic-valence indicators. AE-2 is a world model of action consequences, not a self-model.
- **Butlin, Long et al. (2025)**, *Identifying indicators of consciousness in AI systems*, Trends Cogn. Sci., doi:10.1016/j.tics.2025.10.011 [V; volume/pages and robot content UNVERIFIED].
- **Long, Sebo, Butlin, Finlinson, Fish, Harding, Pfau, Sims, Birch & Chalmers (2024)**, *Taking AI welfare seriously*, arXiv 2411.00986 [V]. Recommends companies **acknowledge, assess, prepare**; framed for "AI systems" generally, warns of error in both directions. The plea's R1–R4 are the robotics instantiation of "assess" and "prepare".
- **Birch (2024)**, *The Edge of Sentience: Risk and Precaution in Humans, Other Animals, and AI*, OUP (open access), doi:10.1093/9780191966729.001.0001 [V]. Sentience candidate = realistic possibility; proportionate precautions decided by informed democratic deliberation. Its AI part centres on the **gaming problem** for LLM behavioural evidence (chapter titles UNVERIFIED) — which supports §6: in robots the gaming problem returns as *trained-away* behaviour.
- **Schwitzgebel & Garza (2015)**, *A defense of the rights of artificial intelligences*, Midwest Stud. Philos. 39:98–119, doi:10.1111/misp.12032 [V]: no relevant difference → similar consideration; design principle: avoid AIs of unclear moral status, and make apparent status match real status (**supports R6**). **Schwitzgebel & Garza (2020)**, *Designing AI with rights, consciousness, self-respect, and freedom*, in Liao (ed.), *Ethics of Artificial Intelligence*, OUP [V]: against AI built to cheerfully sacrifice itself — directly relevant to the "trained to perform" point. **Schwitzgebel (2023)**, *The full rights dilemma for AI systems of debatable moral personhood*, arXiv 2303.17509 [V; not in Robonomics as the task brief suggested].
- **Seth (2025)** BBS — see §5.1.
- **AMCS open letter (26 Apr 2023)**, *The responsible development of AI agenda needs to include consciousness research*, https://amcs-community.org/open-letters/ [V]. Responded to the FLI pause letter without taking a position on pausing; calls for formal/empirical consciousness measures; signatories include Bengio and Manuel Blum. Lenore Blum's MoC7 plenary (#51) on embodied CTM world models is the natural bridge.
- **Bayne, Seth, Massimini, … Mudrik (2024)**, *Tests for consciousness in humans and beyond*, TiCS 28(5):454–466, doi:10.1016/j.tics.2024.01.010 [V] — already cited in master §4.4.
- **Chalmers (2023)**, *Could a large language model be conscious?*, Boston Review (9 Aug 2023); arXiv 2303.07103 [V]. LLMs "somewhat unlikely" conscious (lack recurrence, global workspace, unified agency); successors could plausibly overcome these within ~a decade. His listed obstacles are mostly things robots already have (recurrence, unified agency) — useful.
- **Anthropic (24 Apr 2025)**, *Exploring model welfare*, https://www.anthropic.com/research/exploring-model-welfare [V]. Evidence that welfare attention is LLM-centred in industry. (Handle tactfully: the plea is not anti-LLM-welfare, see Q9.)
- **Shulman & Bostrom (2021)**, *Sharing the world with digital minds*, in Clarke, Zohny & Savulescu (eds.), *Rethinking Moral Status*, OUP, 306–326 [V]: numbers/scale argument.
- **Saad & Bradley (2022)**, *Digital suffering: why it's a problem and how to prevent it*, Inquiry, doi:10.1080/0020174X.2022.2144442 [V]: "Access–Monitor–Prevent" — closest prior *operational* proposal; compare with R3.
- **Dung (2023)**, *How to deal with risks of AI suffering*, Inquiry, doi:10.1080/0020174X.2023.2238287 [V; vol/pages UNVERIFIED]; book *Saving Artificial Minds* (Routledge 2025) [V per agent; not separately checked].
- **Tomasik (2014)**, *Do artificial reinforcement-learning agents matter morally?*, arXiv 1410.8233 [V]: RL agents have "very small but nonzero" moral importance; explicitly anticipates robotics. The earliest statement of the RL-scale worry.
- **Bryson (2010)**, *Robots should be slaves*, in Wilks (ed.), *Close Engagements with Artificial Companions*, John Benjamins, 63–74 [V]: robots should be owned tools; Bryson later clarified the title concerns ownership/responsibility. **Use as the foil for the "slavery" framing:** her design norm (don't build robots that are moral patients) is compatible with R2; the plea's point is that this norm is not being checked.
- **Gunkel (2018)**, *Robot Rights*, MIT Press [standard; not web-checked]. **Coeckelbergh (2010)**, *Robot rights? Towards a social-relational justification of moral consideration*, Ethics Inf. Technol. 12(3):209–221, doi:10.1007/s10676-010-9235-5 [V]: relational approach — the opposite of the plea's architecture-based approach; cite to distinguish.

### 11.3 MoC7 talks to cite or contact (booklet abstracts, `docs/moc7/booklet.txt`)
| # | Speaker | Title | Use |
|---|---|---|---|
| 9 | Tanya de Villiers-Botha (Stellenbosch) | *What Good is Conscious AI?* | Dilemma: human-like conscious AI is least risky but obviates the instrumental reasons for building it. The plea adds: non-human-like AC may arrive uninvited |
| 25 | Tim Ludwig (KIT) | *Why there is a no-go theorem for consciousness on a chip but not for consciousness in a brain* | Denier map (§5.1) |
| 26 | Borjan Milinkovic (NeuroPSI) | *The (im)possibility of synthetic consciousness* | Denier map; leads file: no reply yet |
| 27 | Ian Durham (Saint Anselm) | *Against AI Consciousness* | Denier map |
| 8 | Maria Sekatskaya (Cologne) | Digital agency through five measurable dimensions (incl. self-preservation, temporal continuity) | Agency without phenomenality; her "self-preservation" dimension is a robot-relevant valence precursor |
| 51 | Lenore Blum (CMU, plenary) | *World Models and the Emergence of a "First-Person" Perspective in an AI* | Embodied CTM: sensors/actuators, world model organised around own history — the consciousness-science side already moving to embodiment |
| 58 | Rasmus Herlo (Copenhagen) | *Attention Self-modelling in Collaborative RL-Based Agents* (AIntelope) | Builds self-modelling RL agents; "affective cooperation" as future work — a candidate R1/R2 early adopter |
| 70 | Evan Thompson (UBC, keynote) | *Consciousness in Life* | Organism-first; denier map |
| 73 | Jakub Mihalik | Russellian monism and organizational invariance | AC a live possibility even for Russellians |
| 98 | Angela Johnson (Northeastern) | *From Indicators to Dynamics…* (AURORA persistent agent, affect state) | Dynamical measures on a running agent's own trajectory — an audit method that fits §6.1 |
| 99 | Jessica White (Sentient Futures) | *Locating disagreement in AI consciousness research* | Expert-disagreement map; potential ally |
| 112 | Anna Frammartino Wilks (Acadia) | *The "Natural" Path to Artificial Consciousness* | Enactivism extended to embodied artificial beings — the bridge from the deniers to robots |
| P12 | Joachim Nicolodi (Cambridge) | *Conscious Access in Large Language Models* | Example of the LLM focus |
| — | Bogotá / "Embodied but Passive" (minimal self) | Minimal self is embodied and *affective*, not agential | Supports §7 (a passive, affective bodily self is enough for valence) and links AIW-280 |
| 74 | Adel Chaibi & Aida Elamrani (Intel / Ghent), with Eric Petit | *Form Under Constraint: Between Substrate and Abstraction* | Middle position on substrate dependence ("the level of forms, jointly constrained by matter and function"); hardware–software co-evolution. Useful for §5.3 |
Not found in the booklet: a dedicated robotics-welfare talk — itself evidence for the paper's premise (UNVERIFIED claim of absence; grep found no such title).

### 11.4 Also check (not verified this session)
- Anand & Hickey 1987 (neonatal pain) — UNVERIFIED.
- Goldstein & Kirk-Giannini (2026), Gurnee et al. (2026), Han, Chalmers & Izmailov (2026), Sofroniew et al. (2026), Beni (2026), Lederman & Mahowald (2026), Singh, Linzen & Ravfogel (2026): taken from the FMT master's reference list, not re-verified here.
- A 2024–25 survey of lifelong/continual robot learning: none confirmed (candidate arXiv 2506.21872, scope UNVERIFIED).

---

## 12. Paper outline, titles, venues, open questions

### 12.1 Title options
1. **Look at the robots: why artificial consciousness, if it comes, will arrive embodied and unannounced** — names the redirect and the "by accident" point without the slavery word.
2. **Silent suffering: a plea to consciousness science and robotics** — closest to MG's framing; "silent" carries the argument of §6–7.
3. **Not the chatbot but the body: architecture audits for consciousness in embodied robots** — the most technical; suits JAIC / Neuroscience of Consciousness.
(The register gate blocks "Not X but Y" titles, so option 3 will fail it as worded: rephrase to "Architecture audits for consciousness in embodied robots", or drop it. "Slavery" stays out of the title: see weakness 7.)

### 12.2 Outline (perspective-length, ~3,500–4,500 words; a 1,500-word comment version = §1, §3, §5, §6 compressed)
1. **The misplaced test bed** (~400 words). AC discourse and test development concentrate on LLMs; LLM self-reports are weak evidence either way. Redirect: the candidates are embodied, continuously running, self-modelling agents.
2. **What a conscious machine would need** (~600). Architecture-level criteria; FMT as the sharpest version (self-model closure, persistence, free modelling; *not* criticality); the LLM contrast as §4.4 states it; convergence table (§9) to show this is not one theory's peculiarity.
3. **Robotics is assembling the parts** (~700). §3 table compressed to 5–6 exemplars: DayDreamer (world model, real closed loop, online learning), Bongard 2006 / Hu, Lin & Lipson 2025 (self-models), Man & Damasio 2019 and homeostatic RL (valence by design), Kuehn & Haddadin (nociception), Solms et al. 2026 and Sanyal 2026 (agents built to carry affect/indicators). FMT efficiency argument: humanoids in homes are in the fit window.
4. **Valence and scale** (~400). Aversive training at simulation scale; most of it is engineering-unnecessary.
5. **Why it would be silent, and why it would not look like ours** (~700). No channel, trained performance, decoupled language heads, reports as reconstructions (AIW-280); non-human modalities; the fish/decapod history.
6. **"It cannot happen in silicon"** (~500). Map of the deniers; why their view is the riskiest in practice; their own criteria point at homeostatic robots; precaution under uncertainty (Birch).
7. **What we ask** (~600). C1–C5, R1–R6, P1–P3; graded architectural triggers (§6.1).
8. **Objections and limits** (~400). Anthropomorphism, alarmism, theory-dependence, Goodhart, Metzinger comparison, author's own programme and self-binding.
9. **Close** (~100). One plain sentence, no aphorism.

### 12.3 Target venues (limits from secondary sources only — ALL UNVERIFIED; check the journal's own author page before drafting to length)
| Venue | Format | Fit | Length (unverified) |
|---|---|---|---|
| *Nature Machine Intelligence* | Perspective, or Comment | Best reach to both communities; published Man & Damasio 2019 and Hu et al. 2025. Comments usually invited — pre-submission enquiry | Nature-family Perspectives ~3,000–5,000 words; Comment typically ~1,500–2,000 |
| *Science Robotics* | Viewpoint / Focus | Direct line to roboticists; published the Lipson self-model papers | UNVERIFIED (author page returned 403) |
| *Journal of Artificial Intelligence and Consciousness* (JAIC) | Article | Metzinger 2021 appeared there; natural place to position against it; lower reach | UNVERIFIED |
| *AI & Society* | Open Forum (peer-reviewed) or Curmudgeon Corner | Ethics/policy readership | Open Forum ~8,000; Curmudgeon ~1,000–1,500, ≤3 references (aggregator listings) |
| *Neuroscience of Consciousness* | Opinion / Spotlight commentary | Consciousness-science audience; FMT already in its orbit (NoC submissions) | UNVERIFIED; article types differ between current About page and older policy page |
Recommendation: pre-submission enquiry to NMI with the Perspective outline; fallback JAIC (full argument) plus a short AI & Society Curmudgeon piece for the policy ask.

### 12.4 Open questions for MG
1. **Self-binding (§2.7):** disclose the crucible robot programme and commit it to a published welfare protocol (R2–R4 applied to ourselves)? Recommended: yes — it is the paper's strongest credibility move. If yes, what does crucible commit to: no aversive valence in closure-ON runs, capped valence, or valence logging plus stop rules?
2. **"Slavery":** keep the word (in body only, framed), replace with "servitude", or drop it?
3. **Co-authors:** a roboticist co-author would answer "outsider lecturing robotics" (candidates from MoC7 or the Davos contacts: Sandamirskaya/AURONIQ in the conversation log — verify relationship first); an animal-sentience co-author would anchor §7. Wanted?
4. **How hard to push P5** (FMT's efficiency argument that humanoid builders will drift into closure)? It is the distinctive claim but rests on toy-scale results.
5. **Metzinger:** position as "complementary, narrower, actionable" (recommended) or as a rebuttal of the moratorium?
6. **IIT twist:** include that under IIT the plea partly reverses (digital robots no; neuromorphic yes)? It makes the robustness table honest but adds length.
7. **Kleiner/Ludwig no-go:** engage in this paper (needs MG to work the proof) or leave for a separate reply?
8. **Venue order** (§12.3): NMI enquiry first?
9. **Language model welfare:** the paper says LLMs are the wrong *focus*; does MG also want to say LLM welfare work is misplaced, or only that robots deserve at least as much attention? (Recommended: the latter — Han, Chalmers & Izmailov's functional welfare axis is in the master already.)
