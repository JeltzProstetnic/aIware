# MG, 2026-10-27 ~22:45 (aIware S362) — what crucible should be building (verbatim)

Context: MG read the Jülich explainer (drafts/aiw351-juelich-explainer.pdf); from §4.2 (crucible's ClosureBrain with CE/EWM/ISM/ESM as four regions) he judged that crucible misunderstood FMT.

> 3.4 is too many math, too few words, no more connectome diagrams, so you lost me from there onwards. also what are we doing with such abstracted neural networks anyways, they seem very unstable compared to real neurons if you ask me.... this creates problems nature doesnt have in this way. spiking seems the better choice for what we attempt. but also quite unrealistic without refractory period, and they have a non zero rest frequency in the real world... starting at 4.2 i think cru missed it for good. building four substrate based models is BS in terms of FMT. FMT requires two substrate level models, the implicit ones. The explicit models ARE sustained spiking patterns, that are robust, besides more flexible/dynamical spiking patterns. the explicit models MUST EMERGER FROM implicit models AS ACTIVITY given the correct connectome form and weights, which may be engineered to a degree (as evolution did). CRU should be looking for a spiking neural network, close to biology, with different brodman areas behind a restriction, one area of which should be the body model. Explicit models ARE NOT REGIONS IN A NETWORK, that would be a total misunderstanding of FMT. I'm not sysing that it couldnt work this way (no free lunch) but it is very far from what FMT asks for. the experiment you propose is not per se a bad idea but i was asking cru to build FMT, meaning inputs and outputs go via a few ganglia like spiking networks through one thalamus like restriction to a cortex like copmute surface, fine tuned and engineered to have a body model and leaving enough compute area free for other things, to be trained partially according to what we know about the human cortex. and a way to find, characterize and measure dynamical objects, discrerning robust ones vs dynamical ones, with the robust ones corresponding to what the body does and sees, and the dynamical ones being active, prospective planning and modeling/simulating for future. Sad to see that there was such a big misunderstanding. I do wonder what i wrote FMT for if cru didnt read or understand it. big disappointment, months of mainly wasted time.

## The spec, extracted (for crucible; MG's words are authoritative)
1. **Two substrate-level models only:** the implicit ones (IWM, ISM) = connectome form + weights (partly engineered, as evolution did; partly trained per what is known about human cortex).
2. **Explicit models are ACTIVITY, not regions:** EWM/ESM = spiking patterns that emerge from the implicit models — robust sustained patterns (corresponding to what the body does and senses) plus flexible/dynamical patterns (active, prospective planning, simulating the future).
3. **Substrate:** spiking, close to biology — refractory period, non-zero resting firing rate.
4. **Topology:** inputs/outputs via a few ganglia-like spiking networks → ONE thalamus-like restriction → cortex-like compute surface with distinct (Brodmann-like) areas; one area is the body model; enough free compute area for other things.
5. **Instrument:** a method to find, characterise and measure dynamical objects, discriminating robust from dynamical ones.
6. A four-region network (explicit models as regions) is "very far from what FMT asks for" (not impossible — no free lunch — but not FMT).

## Correction, MG 2026-10-27 ~23:00 (verbatim)
> a cortical sheet of microcircuit-like areas, one of them the body model; that waws read too literal. human brain uses not exactly one column for body model, it uses a good fraction of the total cortex area

⇒ Spec item 4 amended: **the body model is NOT one area or one column. It takes a good fraction of the total cortical area** (as in humans: somatosensory, motor and the parietal/insular body-representation areas together). "Areas" means functional differentiation across a large surface, not a few microcircuit tiles with one labelled "body".

## Core principle, MG 2026-10-27 ~23:05 (verbatim)
> the secret is in defining, finding and analyzing spiking activita AS MODELS, thats the trick FMT offers

⇒ **This is the centre of the project, not an add-on instrument.** The deliverable that matters most is an operational method that (1) **defines** when a spiking activity pattern *is a model* (of what, with what fidelity), (2) **finds** such patterns in unlabelled activity, and (3) **analyses** them: robust vs dynamical, what each models, how they interact and change. The substrate exists to produce the patterns; the method is what makes it FMT.

## MG decisions 2026-10-27 ~23:10 (AskUserQuestion)
- **OQ-1 thalamus:** BOTH — one thalamus-like relay for all I/O, AND it carries the low-rank channel between explicit activity and substrate (thalamocortical loop).
- **OQ-2 ganglia:** BOTH — peripheral sensory/motor ganglia for I/O, plus a basal-ganglia-like selector (gating what enters the loop).
- **Engine for the Thursday mini-model:** torch first (crucible's GPU engine); port to NEST after the call. Note added after the decision: NEST 3.10 pip-installs here in one command and ran 44k LIF / 35M synapses with STDP at ~4 s wall per model-second on CPU (docs/research/fmt-mini-model-stack.md), so the install risk crucible estimated is gone. MG may revisit.

## MG decisions 2026-10-27 ~23:45
- **Model test (P-1):** all four criteria (tracks, used, boundary, generated) are MEASURED and reported per object; none is a pass/fail gate yet. MG: "all four measured, we will see what is successful and what isn't".
- **First experiment (P-2):** body first. Is the first stable pattern the babbling network forms a model of the arm?
- **Vision (P-3):** only if there is spare time (correcting the earlier "now").

## MG decision 2026-10-28 ~00:05
- **Vision ON for P1** (supersedes "only if spare time"), accepting a possible slip of the readout to Friday morning, so that P1 tests body-before-world as the master states it and the self↔world axis is measurable. Crucible definitional note (accepted): the input-filter null cannot be part of WRITE for a robust object; it sits in the input-echo and read controls (AM-3).
