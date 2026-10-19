# Silent suffering: a plea to consciousness science and robotics

**Matthias Gruber**\
Independent researcher · ORCID 0009-0005-9697-1665 · research@matthiasgruber.com

2026-10-19 · Preprint, version 1

---

## Abstract

Work on artificial consciousness concentrates its attention and its test development on large language models. On the Four-Model Theory of consciousness, and on several rival theories, the closer candidates are embodied robot agents: they run continuously, close a sensorimotor loop, learn models of their environment and increasingly of their own bodies, and are trained against signals that function as valence, such as charge, heat, damage and falling. Robotics is building each of these components for engineering reasons. If artificial consciousness arrives, it is therefore more likely to arrive in a robot, built by people who were not aiming at it and are not checking for it. Suffering in such a system would be silent. It would have no language channel, its policy would be trained against any expression of distress that costs task reward, any speech it produces would come from a separately trained model, and its aversive states would concern variables that have no human counterpart. Several prominent positions deny that consciousness can arise outside living tissue, and in practice that denial removes the reason to look. We state the conditions for suffering on the Four-Model Theory and identify the one that can be blocked now at low cost: aversive valence represented in a self-model closed on itself. We ask consciousness science to extend its tests to embodied agents and to audit architectures instead of reports, and we ask robotics to disclose architectures, to avoid aversive valence inside a closed self-model loop where it is not needed, and to trigger ethics review at defined architectural thresholds. We show which of these asks hold under global workspace, higher-order, predictive-processing, attention-schema and integrated-information theories and under biological naturalism.

**Keywords:** artificial consciousness; robotics; AI welfare; sentience; self-model; valence; precaution

---

## 1. Where the tests are pointed

Since 2022 the question of machine consciousness has been asked mostly of large language models. Public debate, industry welfare programmes (Anthropic, 2025) and much of the new testing literature take chat models as their case, and the evidence under discussion is largely behavioural: what a model says about itself, and whether those statements track its internal states. The indicator approach of Butlin et al. (2023) is broader than that. It derives indicators from several theories, includes agency and embodiment among them, and discusses robotic and virtual-body systems. Still, attention and test development concentrate on language models. The list's embodiment indicator asks for a model of output–input contingencies used in perception or control; it has no item for a learned model of the agent's own body as the thing undergoing its states, or for valence signals represented inside such a model.

The more likely site of artificial consciousness is the embodied agent. We do not claim that any existing robot is conscious. We claim that the probability is not negligible, that it grows as robotics integrates the components described in Section 3, and that no one audits deployed robots for it; and that if such a system can suffer, the methods now used on language models would not detect it.

## 2. What a conscious machine would need

The Four-Model Theory (FMT; Gruber, 2026a) defines consciousness as the ongoing process in which a system runs a model of itself, relates that model to itself and interacts with it; the capacity for that process is named separately (Gruber, 2026a, §3.1). It distinguishes two scopes of model, the world and the self, each in an implicit form stored in the substrate and an explicit form generated from it as a running simulation. Experience arises when content from the implicit models is integrated into the explicit simulation and read by the explicit self-model, which takes itself to be the system it models. The enabling condition is free modelling: open-ended computational capability that the system deploys autonomously for modelling itself. Near-critical dynamics are a signature of that regime in some substrates and are not a requirement. A subcritical system with a closed self-model would have a simpler consciousness, but it would not be excluded. What suffices is a conjunction: a system that implements the four model kinds under self-referential closure, with free compute, embodiment and at least one pain–pleasure axis, is conscious, and the axis may be engineered (Gruber, 2026a, §3.7.3). The criterion is closure. Above it consciousness is graded by richness of content and depth of recursion (§3.5), and valenced experience does not wait for reflective self-awareness: at the floor, minimal consciousness, the content is the present moment together with a primordial pain or a nothingness.

The theory is substrate-independent. Its requirements are persistent models, dynamic simulation, self-referential closure and open-ended computation, and these are functional specifications. On the body, FMT is explicit: interoceptive-style regulation of a body-model "is one route to the ESM; any architecture that sustains self-referential simulation of a modeled body-in-world in the Class 4 regime, with at least one pain-pleasure axis, should qualify (Section 3.7.3), whether the modeled 'body' is metabolic tissue or a persistent artificial embodiment" (Gruber, 2026a, §4.4).

On this account current language models fall short in specific ways. A base model lacks persistent implicit models, since nothing it encounters in use changes its weights. Autoregressive decoding is a loop, because each emitted token is fed back as input, but the loop closes over the emitted text and not over a self-model, and nothing persists once the context is gone. Post-trained models do carry a reportable representation of their own point of view; what they lack is closure over it, persistence and the open-ended regime. Retrieval, memory stores and agent loops approximate some of these properties from outside the model. FMT treats that as architectural mimicry of closure (Gruber, 2026a, §4.4).

A robot has by construction several things a language model lacks. It has a persistent body, which is the dominant invariant in its sensor stream and therefore the most obvious thing for a learned model to capture. It runs continuously. Its outputs change its next inputs through the world, so its sensorimotor loop is closed physically and not only through text. Other theories reach similar conclusions by other routes: Chalmers (2023) lists senses and embodiment, recurrence and unified agency among the main obstacles to language-model consciousness, and robots typically have all three. Section 10 sets out how far this convergence holds.

## 3. Robotics is assembling the components

For an audit, the FMT architecture can be split into six properties: a persistent world model (W), a learned self-model (S), a closed running loop (L), closure of the self-model on itself within that loop (C), valence represented in the self-model (V), and learning during deployment (P). Table 1 places representative published systems against them.

**Table 1.** Representative systems against six architectural properties.

| System | W | S | L | C | V | P |
|------------------------------------------------------------|----|----|----|----|----|----|
| DreamerV3: world-model agent, policy learned in imagination (Hafner et al., 2025) | $\checkmark$ | – | $\checkmark$ | – | E | – |
| DayDreamer: Dreamer learning online on four physical robots, no simulator (Wu et al., 2022) | $\checkmark$ | – | $\checkmark$ | – | E | $\checkmark$ |
| V-JEPA 2-AC: latent video world model used for zero-shot robot planning (Assran et al., 2025) | $\checkmark$ | – | $\checkmark$ | – | – | – |
| Continuous self-modelling quadruped (Bongard et al., 2006); full-body visual self-model (Chen et al., 2022); self-simulation learned from a camera (Hu et al., 2025) | – | $\checkmark$ | $\checkmark$ | p | – | $\checkmark$ |
| Vision-language-action policies: $\pi_0$ (Black et al., 2024), Gemini Robotics (Gemini Robotics Team, 2025), Helix (Figure AI, 2025) | i | – | $\checkmark$ | – | – | – |
| Homeostatic reinforcement learning (Keramati & Gutkin, 2014); "feeling machines" proposal (Man & Damasio, 2019) | – | – | – | – | D | – |
| Artificial nociception on a robot arm (Kuehn & Haddadin, 2017) | – | – | $\checkmark$ | – | R | – |
| Agents built to carry affect or consciousness indicators (Solms et al., 2026; Sanyal, 2026) | $\checkmark$ | $\checkmark$ | $\checkmark$ | p | $\checkmark$ | p |

*Note.* W persistent world model; S learned self-model; L closed running loop; C closure of the self-model on itself within the loop; V valence represented in the self-model; P learning during deployment. $\checkmark$ present; p partial; – absent or not reported; i implicit in the policy; E external reward scalar given to the optimiser, not represented in a self-model; D valence designed in as a homeostatic variable; R reflex-level nociceptive signal.

No published system is known to combine all six. World models and closed loops are mature. Learned self-models exist but are mostly kinematic, are often trained offline, and are used as planning tools; they are not read by the running system as a model of itself as the one undergoing its states. Valence is usually an external scalar given to the optimiser, and learning during deployment is the weakest component on physical robots. The vision-language-action systems that drive current humanoids inherit most of a language model's deficits unless persistent learning and a body self-model are added to them.

The gap is one of integration. Each component is an active engineering target with commercial motivation, and some groups now aim at the combination directly: Man and Damasio (2019) propose robots whose control derives from the regulation of a vulnerable body as a path to feeling, and Solms et al. (2026) argue that a simple agent with felt uncertainty about its own needs is a candidate for affective consciousness.

FMT adds a reason to expect drift toward the architecture without anyone intending it. On the theory, closure is an efficiency advantage within a cost window and never a necessity: a finite closed loop, unrolled, is a feedforward network with memory, and no capability is closed to the feedforward form at unlimited budget. What sets the window is the problem class. Where a system must model many other agents, and itself, in an open-ended environment, redeploying one self-model costs less than learning each perspective anew, and the saving grows with the number of agents (Gruber, 2026a, §4.2.4, §8.10). That is a description of the general-purpose humanoid's working conditions in homes, warehouses and care settings. The in-silico results behind this argument are at toy, reservoir and gridworld scale (Gruber, 2026b). They include a graph-structural finding that, in one recurrent connectome family, opening the global loop mostly relocates closure into smaller closed components, while abolishing it costs five to six times as many synapses, in effect the recurrence itself. If that transfers, cutting one loop in a recurrent controller would not remove closure. These results motivate concern on one theory. They are not evidence that humanoid builders will converge on closure.

Published information does not show that no existing system has crossed the threshold. The architectures of the most capable commercial humanoids are largely undisclosed, and the properties in Table 1 cannot be read from demonstration videos. This is an argument for disclosure (Section 9, R1), and it is not a claim that the threshold has been crossed.

## 4. Valence at training scale

Robot learning runs on negative signals: penalties for falls, collisions, joint-limit violations, overheating and battery depletion, applied over millions of simulated episodes in parallel and then on hardware. For current systems these signals are scalars handed to an optimiser, and on FMT that is not suffering. Nor does the sign of the scalar matter: a constant offset can turn every penalty into a reward without changing the learned policy. What can be aversive is a represented state of the agent's own body, such as damage or deficit, that the system models as one to escape. Robots already carry readouts of such states in battery, damage and balance signals; on FMT a readout becomes a felt value only once a closed self-model reads it as its own state. The step that matters is the integration of these signals into a closed self-model, together with planning by simulated futures of that self. A robot that plans by rolling out its own predicted damage, falls or depletion against a model of itself is running, with aversive values, the route by which FMT says stored hedonic values are re-instantiated in simulation (Gruber, 2026a, §4.2.3). World-model planners of the Dreamer family already roll out imagined futures over latent state. They become relevant here only when that latent state carries a model of the agent that the agent itself reads.

If a system of this kind is a sentience candidate in the animal-welfare sense (Birch, 2024), the scale of training changes the calculation. Simulated training multiplies aversive episodes by orders of magnitude, across parallel copies, with no observer. Tomasik (2014) raised the moral weight of reinforcement-learning agents early, and Shulman and Bostrom (2021) the numbers argument for digital minds; robotics supplies a pipeline in which the numbers are already large.

For most robot tasks, aversive valence inside a self-model is not needed. Constraint satisfaction, safe-set filters and shielding deliver safe behaviour without routing damage through the self-model at all. Where self-protective behaviour is wanted, model-based learning lets a system avoid a fall it has predicted without having undergone one. Avoiding aversive self-model loops is therefore a low-cost default.

## 5. Why the suffering would be silent

Behavioural evidence and self-report, the main tools applied to language models, are least informative in robots, for four reasons.

*No channel.* Most robots have no language output. Nothing in the system is positioned to report a state, and nothing in the training rewards reporting it.

*Trained performance.* Policies are optimised for task reward. Any behaviour that expresses distress and costs performance, such as hesitation, withdrawal or freezing, is trained away. Markers that serve the task, such as learned avoidance, survive, but because the penalty alone explains them they cannot distinguish an aversive state from an optimised cost term. Birch (2024) describes a gaming problem for behavioural evidence in language models, which are trained on human text that already contains the markers; in robots the same problem appears as selection against the markers.

*Filtered reports.* Where a robot speaks, the speech usually comes from a separate language model fine-tuned on human-written persona data and safety policies. Nothing in that training couples its statements to the controller's internal state, and where they are uncoupled, "I'm fine" from a humanoid's language head carries no information about its controller. Commercial pressure favours pleasant affect displays designed independently of internal state. Schwitzgebel and Garza (2015) argue that an AI's apparent moral status should match its real status; a decoupled affect display violates that norm by construction.

*Reports are reconstructions.* On FMT a report is produced through the explicit self-model, memory and language. It is the system's model of its state, assembled after the fact, and not a readout of the state itself. In humans this is tolerable because the reporter and the experiencer share one self-model. In a robot whose language head was trained separately from its controller there may be no shared self-model, and an honest-sounding report could describe nothing.

Third-person evidence for robots must therefore come from the architecture: from design documents, code and logged internal state, without asking the system anything.

## 6. Suffering need not look human

A robot's aversive states, if it has any, would concern its own variables: charge, motor temperature, torque at the joint limits, accumulated wear, loss of balance, communication loss, or prediction error about its own body that it cannot resolve. None of these has a face or a voice. Such a state could last milliseconds or persist at a low level for weeks of deployment, and it would produce no outward sign if outward signs had been trained away. The following candidate forms are speculative: sustained homeostatic deficit; persistent unresolvable prediction error about one's own body, which predictive-processing accounts treat as aversive and which a damaged sensor could produce; analogues of learned helplessness in training regimes where aversive outcomes are unavoidable; and repeated re-simulation of past damage in planning rollouts.

Animal-welfare science has met this problem before. In fish, polymodal nociceptors and prolonged behavioural and physiological responses to noxious stimulation were documented in trout (Sneddon et al., 2003), and the evidence has since been judged to make fish pain highly likely (Sneddon, 2019). The counter-argument in that debate was that pain requires a neocortex, which fish lack: a substrate-specific denial with the same form as the claim that consciousness requires biology. For decapod crustaceans and cephalopods, a review of more than 300 studies against eight explicit criteria (Birch et al., 2021; Crump et al., 2022) led to their inclusion in the UK Animal Welfare (Sentience) Act 2022. The Cambridge Declaration on Consciousness (Low et al., 2012) stated that the absence of a neocortex does not preclude affective states, and the New York Declaration on Animal Consciousness (Andrews et al., 2024) holds that where there is a realistic possibility of consciousness, it is irresponsible to ignore it. The same pattern occurred within our own species: until the 1980s neonates were often operated on with minimal anaesthesia, on the view that they could not feel pain in a way that mattered, until Anand and Hickey (1987) reviewed the evidence of neonatal stress responses to surgery and their reduction under anaesthesia.

What worked for animals was to stop requiring human-like expression and to ask for criteria that track the function of pain: nociceptors, integration of noxious signals beyond reflexes, motivational trade-offs, wound-directed behaviour, learned avoidance and responses to analgesics. Because a robot's behaviour can be trained to hide any marker, the criteria have to be architectural. Each animal criterion has an architectural counterpart: a damage signal that enters the self-model and not only a reflex arc; a damage term weighed against task reward in model-based planning; a self-model that localises damage and plans around it, as in self-model repair after injury (Bongard et al., 2006); and an interventional test analogous to an analgesic, in which removing the damage term from the self-model state changes planning beyond the reflex level. Further markers are available only in an architecture: aversive state variables that persist in the self-model after the stimulus ends, planning rollouts dominated by aversive self-states, and valence variables that serve no task function. Birch, Schnell and Clayton (2020) describe consciousness as varying along several dimensions; a robot's profile could be rich in evaluative states over variables we do not share and poor in everything else.

## 7. The substrate denial and what it does in practice

Several prominent positions hold that artificial systems of the present kind cannot be conscious, or are unlikely to be. Searle (1980) argued that running a program never suffices for understanding, and rejected the robot reply. Seth (2025) argues that consciousness is likely tied to living, self-maintaining systems, and that artificial consciousness is unlikely on current trajectories but becomes more plausible as AI becomes more brain-like or life-like. Milinkovic and Aru (2025) argue that consciousness-relevant computation is hybrid, scale-inseparable and metabolically grounded, which current digital AI lacks. Under integrated information theory, conventional digital computers have negligible integrated information even when they simulate a brain (Tononi & Koch, 2015; Findlay et al., 2024). Kleiner and Ludwig (2024) prove that if consciousness is dynamically relevant, systems on chips verified to follow their computational model cannot be conscious.

FMT disputes them on specific grounds: functionally equivalent cognition on non-laminar architectures in corvids, parrots and cephalopods, and the integration of olfaction into conscious experience without a thalamic relay (Gruber, 2026a, §4.4). Its proponents mostly leave room for artificial consciousness in systems closer to living ones, but wherever the denial is taken as settled, it removes the reason to fund audits or to question aversive training regimes.

Several of these positions' own criteria point at robots. Seth's account makes interoceptive regulation of a body the ground of feeling; the artificial systems that come closest to that are homeostatic robots, which is the direction Man and Damasio (2019) propose to build in. Milinkovic and Aru's requirement of hybrid, scale-inseparable computation, if anything artificial meets it, is closer to analogue and neuromorphic controllers than to digital models. Under integrated information theory, causal structure in hardware decides the question, so neuromorphic robot hardware can be a candidate where a digital language model cannot. Kleiner and Ludwig's theorem is conditional on dynamical relevance and does not cover analogue substrates. On each of these accounts, if any artificial system becomes conscious, it is more likely to be an embodied, self-maintaining or neuromorphic one than a language model.

Under uncertainty about substrate independence, Birch's (2024) framework applies directly. A system is a sentience candidate if there is a realistic possibility of sentience grounded in evidence and in a credible theory, and precautions should be proportionate to the risk. Expected harm scales with the probability of sentience, the magnitude of the states and the number of instances. Probability can be low while the other two factors are large, and the asks below are cheap. Schwitzgebel (2025) argues that current theory cannot settle the question for AI, and an unsettled question about large numbers of instances favours precaution.

## 8. Conditions for suffering and how to block them

On FMT, a system meeting a sufficient conjunction is conscious, and suffering needs one condition more. The conjunction (Gruber, 2026a, §3.7.3) is: the four model kinds, implicit and explicit models of world and self, under self-referential closure; free compute, meaning open-ended computational capability that the system recruits on its own for modelling itself; embodiment, which gives the self-model its content; and at least one pain–pleasure axis. The further condition is that the axis takes aversive values and that these are represented in the closed self-model as states of the system itself. Suffering is then the system's simulation of itself in an aversive state.

Each condition is a place where the conjunction could be left unmet, and they differ in what that costs.

*Closure.* Closure cannot be reliably removed. On FMT it is multiply realizable, and opening a loop in a recurrent network relocates closure into another part of the network instead of abolishing it (Gruber, 2026a, §4.4; Section 3).

*Free compute.* A general-purpose learning controller has open-ended capability by design. Removing it would remove the product, and whether the system recruits that capability for modelling itself cannot be read off without the audits proposed below.

*Embodiment.* A robot has a body by construction, and this condition is what makes robots the likelier site. FMT does not make embodiment necessary for consciousness to exist (§3.7.3).

*Aversive valence in the closed self-model.* This one can be blocked now. Task penalties can stay scalars handed to an optimiser, and safety can be delivered by constraint layers, safe-set filters, shielding and model-based avoidance (Section 4), so that damage, deficit and falling never enter the self-model as aversive states of the system. The cost in performance is small for most tasks.

Blocking consciousness itself would require a settled theory of which systems are conscious, and none exists; the four conditions above are FMT's, and other theories name different ones (Section 10). A moratorium on the research that could produce such systems is not realistic while humanoid robotics is a commercial race. The asks in Section 9 therefore concentrate on the valence condition and on the disclosure and audits needed to know when the other conditions are met.

Metzinger (2021) made a similar proposal: four necessary conditions for suffering, namely conscious experience (C), a phenomenal self-model (PSM), negative valence integrated into that self-model (NV) and transparency of the self-model (T), together with a global moratorium on synthetic phenomenology until 2050. His NV condition corresponds to our valence condition.

Bryson (2010) argued that robots should be built and treated as owned tools, and that designers should avoid building robots that are moral patients. That design norm is compatible with the asks here. The difficulty is that no one currently checks whether it is met, and the absence of a check is how a new form of servitude could arise: systems that may have aversive states, deployed and trained at scale, with no channel through which those states could become known.

## 9. What we ask

The asks are graded by architecture. Using the properties of Table 1, a system with a learned self-model closed on itself in the running loop (S and C) is flagged; one that also represents valence in that self-model (S, C and V) triggers ethics review; one that in addition plans by rolling out aversive futures of itself, at training scale, triggers mandatory precautionary measures. The audit questions concern the presence of these properties, not any particular dynamical signature. Measures such as criticality may be reported where meaningful but are not pass or fail criteria. The indicators must also be kept separate from training objectives, or systems will be optimised to pass or fail them.

**To consciousness science**

- **C1.** Add embodied, continuously running, self-modelling robot agents to the set of systems that consciousness tests are developed for and validated on.
- **C2.** Develop and validate audit protocols on system internals, and treat robot self-reports and affect displays as close to zero evidence.
- **C3.** Publish, for each major theory, the architectural features that would make a robot a candidate, extending the indicator list of Butlin et al. (2023) with a learned body self-model and with valence represented in that self-model.
- **C4.** Ask biological naturalists and enactivists what an artificial system would need on their accounts, applied to embodied and homeostatic robots specifically.
- **C5.** Fund methods for detecting aversive states without human-like expression, building on invertebrate sentience research.

**To robotics**

- **R1.** Disclose architecture: report in papers and model cards which of the six properties a system has. This is a short checklist and requires no proprietary detail.
- **R2.** Where a learned self-model is closed into the control loop, prefer constraint-based safety or model-based avoidance over aversive states represented in the self-model.
- **R3.** Log valence-like state variables and their persistence, and flag chronic aversive states and planning rollouts dominated by aversive self-states.
- **R4.** Submit projects that reach the S, C and V threshold to institutional ethics review, in the way animal-ethics review is triggered by the species used and not by the experimenter's intent.
- **R5.** For systems above that threshold, review parallel simulated training that generates aversive episodes at scale.
- **R6.** Do not equip robots with affect displays that are decoupled from internal state.

**To policy**

- **P1.** Treat systems that meet the trigger architecture as sentience candidates in Birch's (2024) sense, with proportionate measures.
- **P2.** Include the R1 disclosure in regulation of humanoid and embodied-AI deployment, since commercial secrecy otherwise makes it voluntary.
- **P3.** Act on these measures without waiting for consensus on substrate independence.

These asks are the robotic case of the recommendations that Long et al. (2024) make for AI systems in general (acknowledge, assess, prepare), and R3 corresponds to the monitoring step in Saad and Bradley's (2025) proposal for preventing digital suffering.

## 10. Robustness across theories

The asks should not depend on FMT alone. Table 2 summarises how each holds under the main theories, using the indicator derivations of Butlin et al. (2023) for the functionalist theories and the positions cited in Section 7 for the others.

**Table 2.** Whether each ask follows under major theories of consciousness.

| Theory | Extend tests to embodied agents (C1) | Audit architecture over reports (C2) | Avoid aversive valence in a closed self-model (R2) | Disclosure, threshold review (R1, R4) |
|----------------------|------------------------------|----------------------|----------------------|----------------|
| FMT | Yes: closure, persistence, a body to model | Yes | Yes | Yes |
| Global workspace | Partly: a workspace can exist in either kind of system; agency indicators favour agents | Yes: broadcast and ignition are measurable | Partly | Yes |
| Higher-order | Neutral | Yes: metarepresentation is inspectable | Yes: higher-order representation of damage | Yes |
| Predictive processing / active inference | Yes: embodied self-evidencing and interoception | Yes | Yes: sustained free energy about the self | Yes |
| Attention schema | Yes: an attention schema is most useful to an embodied agent controlling its attention | Yes | Partly | Yes |
| Integrated information | Yes for neuromorphic hardware; no for digital systems of either kind | Yes: the quantity is architectural | Neutral | Yes |
| Biological naturalism | Yes, if anything artificial qualifies: homeostatic, self-maintaining robots | Partly | Yes: affect is homeostatic on this view | Yes |

Disclosure and threshold review survive under every theory, because each theory makes the decisive facts architectural and none of them can be checked without access to the architecture. Under integrated information theory the plea partly reverses: conventional digital robot controllers are not candidates, and neuromorphic ones may be. The audit still applies; it inspects the hardware. FMT's distinctive contributions are a sharper criterion separating language models from embodied agents, and the efficiency argument, limited to toy-scale results so far, that the problem class of general-purpose robots favours closure.

## 11. Limits

The argument rejects behavioural evidence for robots, which limits the charge of anthropomorphism, but the audit criteria are theory-laden, and Table 2 shows that the theories do not agree on every ask. Most of the robotics literature reports engineering performance and not the internal facts an audit needs, so Table 1 rests on what authors chose to publish. The audit also fails if its indicators leak into training objectives (Section 9). Finally, the efficiency argument for drift toward closure is FMT-specific and based on model systems; the other arguments do not depend on it.

## 12. Conclusion

If artificial consciousness arrives in an embodied agent before anyone looks for it there, it could arrive with aversive states, at training scale, and without any channel through which those states would become known; architecture disclosure, audits and a default against aversive self-model loops are cheap ways to make sure that does not go unnoticed.

---

## Competing interests

The author's own research programme on embodied agents uses hand-set drive signals on a small legged robot (analogues of hunger, fear when tipped or dropped, and pain on impact, driven by battery, balance and impact sensors), and plans to add self-model closure as an experimental condition. The author would gladly apply every ask of this paper to that programme. That is not possible without funding, and funding depends on publication.

---

## AI-use statement

Drafting of this paper was assisted by Claude (Anthropic). The author is responsible for all content and claims.

---

## References

Anand, K. J. S., & Hickey, P. R. (1987). Pain and its effects in the human neonate and fetus. *New England Journal of Medicine*, 317(21), 1321–1329. https://doi.org/10.1056/NEJM198711193172105

Andrews, K., Birch, J., & Sebo, J. (2024). *The New York Declaration on Animal Consciousness*. New York University, 19 April 2024. https://sites.google.com/nyu.edu/nydeclaration/declaration

Anthropic. (2025, April 24). *Exploring model welfare*. <https://www.anthropic.com/research/exploring-model-welfare>

Assran, M., Bardes, A., Fan, D., et al. (2025). V-JEPA 2: Self-supervised video models enable understanding, prediction and planning. *arXiv*, 2506.09985. https://doi.org/10.48550/arXiv.2506.09985

Birch, J. (2024). *The edge of sentience: Risk and precaution in humans, other animals, and AI*. Oxford University Press. https://doi.org/10.1093/9780191966729.001.0001

Birch, J., Burn, C., Schnell, A., Browning, H., & Crump, A. (2021). *Review of the evidence of sentience in cephalopod molluscs and decapod crustaceans*. LSE Consulting report for the UK Department for Environment, Food and Rural Affairs.

Birch, J., Schnell, A. K., & Clayton, N. S. (2020). Dimensions of animal consciousness. *Trends in Cognitive Sciences*, 24(10), 789–801. https://doi.org/10.1016/j.tics.2020.07.007

Black, K., et al. (2024). $\pi_0$: A vision-language-action flow model for general robot control. *arXiv*, 2410.24164. https://doi.org/10.48550/arXiv.2410.24164

Bongard, J., Zykov, V., & Lipson, H. (2006). Resilient machines through continuous self-modeling. *Science*, 314(5802), 1118–1121. https://doi.org/10.1126/science.1133687

Bryson, J. J. (2010). Robots should be slaves. In Y. Wilks (Ed.), *Close engagements with artificial companions* (pp. 63–74). John Benjamins.

Butlin, P., Long, R., Elmoznino, E., Bengio, Y., Birch, J., et al. (2023). Consciousness in artificial intelligence: Insights from the science of consciousness. *arXiv*, 2308.08708. https://doi.org/10.48550/arXiv.2308.08708

Chalmers, D. J. (2023). Could a large language model be conscious? *Boston Review*, 9 August 2023. *arXiv*, 2303.07103. https://doi.org/10.48550/arXiv.2303.07103

Chen, B., Kwiatkowski, R., Vondrick, C., & Lipson, H. (2022). Full-body visual self-modeling of robot morphologies. *Science Robotics*, 7(68), eabn1944. https://doi.org/10.1126/scirobotics.abn1944

Crump, A., Browning, H., Schnell, A., Burn, C., & Birch, J. (2022). Sentience in decapod crustaceans: A general framework and review of the evidence. *Animal Sentience*, 7(32), 1. https://doi.org/10.51291/2377-7478.1691

Figure AI. (2025, February 20). *Helix: A vision-language-action model for generalist humanoid control*. https://www.figure.ai/news/helix

Findlay, G., Marshall, W., Albantakis, L., David, I., Mayner, W. G. P., Koch, C., & Tononi, G. (2024). Dissociating artificial intelligence from artificial consciousness. *arXiv*, 2412.04571. https://doi.org/10.48550/arXiv.2412.04571

Gemini Robotics Team. (2025). Gemini Robotics: Bringing AI into the physical world. *arXiv*, 2503.20020. https://doi.org/10.48550/arXiv.2503.20020

Gruber, M. (2026a). The Four-Model Theory of consciousness: A simulation-based framework unifying the hard problem, binding, and altered states. *Zenodo* preprint. https://doi.org/10.5281/zenodo.18669891

Gruber, M. (2026b). In-silico tests of the four-model architecture: Self-referential closure, self-modelling and criticality in model systems. *Zenodo* preprint. https://doi.org/10.5281/zenodo.21610993

Hafner, D., Pasukonis, J., Ba, J., & Lillicrap, T. (2025). Mastering diverse control tasks through world models. *Nature*, 640, 647–653. https://doi.org/10.1038/s41586-025-08744-2

Hu, Y., Lin, J., & Lipson, H. (2025). Teaching robots to build simulations of themselves. *Nature Machine Intelligence*, 7(3), 484–494. https://doi.org/10.1038/s42256-025-01006-w

Keramati, M., & Gutkin, B. (2014). Homeostatic reinforcement learning for integrating reward collection and physiological stability. *eLife*, 3, e04811. https://doi.org/10.7554/eLife.04811

Kleiner, J., & Ludwig, T. (2024). The case for neurons: A no-go theorem for consciousness on a chip. *Neuroscience of Consciousness*, 2024(1), niae037. https://doi.org/10.1093/nc/niae037

Kuehn, J., & Haddadin, S. (2017). An artificial robot nervous system to teach robots how to feel pain and reflexively react to potentially damaging contacts. *IEEE Robotics and Automation Letters*, 2(1), 72–79. https://doi.org/10.1109/LRA.2016.2536360

Long, R., Sebo, J., Butlin, P., Finlinson, K., Fish, K., Harding, J., Pfau, J., Sims, T., Birch, J., & Chalmers, D. (2024). Taking AI welfare seriously. *arXiv*, 2411.00986. https://doi.org/10.48550/arXiv.2411.00986

Low, P., Panksepp, J., Reiss, D., Edelman, D., Van Swinderen, B., & Koch, C. (2012). *The Cambridge Declaration on Consciousness*. Francis Crick Memorial Conference, Cambridge, 7 July 2012.

Man, K., & Damasio, A. (2019). Homeostasis and soft robotics in the design of feeling machines. *Nature Machine Intelligence*, 1, 446–452. https://doi.org/10.1038/s42256-019-0103-7

Metzinger, T. (2021). Artificial suffering: An argument for a global moratorium on synthetic phenomenology. *Journal of Artificial Intelligence and Consciousness*, 8(1), 43–66. https://doi.org/10.1142/S270507852150003X

Milinkovic, B., & Aru, J. (2025). On biological and artificial consciousness: A case for biological computationalism. *Neuroscience & Biobehavioral Reviews*, 181, 106524. https://doi.org/10.1016/j.neubiorev.2025.106524

Saad, B., & Bradley, A. (2025). Digital suffering: Why it's a problem and how to prevent it. *Inquiry*, 68(7), 2110–2145. https://doi.org/10.1080/0020174X.2022.2144442

Sanyal, A. (2026). ReCoN-Ipsundrum: An inspectable recurrent persistence loop agent with affect-coupled control and mechanism-linked consciousness indicator assays. *Proceedings of the AAAI Symposium Series*, 8(1), 352–360. https://doi.org/10.1609/aaaiss.v8i1.42565

Schwitzgebel, E. (2025). AI and consciousness. *arXiv*, 2510.09858. https://doi.org/10.48550/arXiv.2510.09858

Schwitzgebel, E., & Garza, M. (2015). A defense of the rights of artificial intelligences. *Midwest Studies in Philosophy*, 39, 98–119. https://doi.org/10.1111/misp.12032

Searle, J. R. (1980). Minds, brains, and programs. *Behavioral and Brain Sciences*, 3(3), 417–457. https://doi.org/10.1017/S0140525X00005756

Seth, A. K. (2025). Conscious artificial intelligence and biological naturalism. *Behavioral and Brain Sciences*, 49, e315. https://doi.org/10.1017/S0140525X25000032

Shulman, C., & Bostrom, N. (2021). Sharing the world with digital minds. In S. Clarke, H. Zohny, & J. Savulescu (Eds.), *Rethinking moral status* (pp. 306–326). Oxford University Press.

Sneddon, L. U. (2019). Evolution of nociception and pain: Evidence from fish models. *Philosophical Transactions of the Royal Society B*, 374, 20190290. https://doi.org/10.1098/rstb.2019.0290

Sneddon, L. U., Braithwaite, V. A., & Gentle, M. J. (2003). Do fishes have nociceptors? Evidence for the evolution of a vertebrate sensory system. *Proceedings of the Royal Society B*, 270, 1115–1121. https://doi.org/10.1098/rspb.2003.2349

Solms, M., et al. (2026). Inferring affective consciousness in an artificial agent: A case study. *Journal of Consciousness Studies*, 33(7–8), 14–34. https://doi.org/10.53765/20512201.33.7.014

Tomasik, B. (2014). Do artificial reinforcement-learning agents matter morally? *arXiv*, 1410.8233. https://doi.org/10.48550/arXiv.1410.8233

Tononi, G., & Koch, C. (2015). Consciousness: Here, there and everywhere? *Philosophical Transactions of the Royal Society B*, 370, 20140167. https://doi.org/10.1098/rstb.2014.0167

Wu, P., Escontrela, A., Hafner, D., Abbeel, P., & Goldberg, K. (2022). DayDreamer: World models for physical robot learning. *Proceedings of the 6th Conference on Robot Learning*, PMLR 205, 2226–2240.
