# AIW-269 — The brain's random generator, and what it means for L2 (v) / Sugiura et al. (2025)

Research note, 2026-09-29. Companion to `docs/aiw269-sugiura-l2.md`. Every reference below was checked
against Crossref (authors, year, venue, volume, pages, DOI); abstracts were read from PubMed, OpenAlex or
arXiv where quoted. Where a finding is stated from memory of the paper rather than from its abstract, it is
marked **[not re-read]**. Items marked **[inference]** are mine and appear in no cited source.

## (a) Bottom line

1. **The study MG remembers is most plausibly Murakami, Shteingart, Loewenstein & Mainen (2017, *Neuron*):** in
   rats, secondary motor cortex (M2) carries the trial-by-trial *stochastic* component of action timing while
   mPFC carries only the deterministic bias, so randomness is "injected by circuits downstream" of the
   deterministic ones; Mainen linked it to creativity in the press coverage (Inverse, 17 May 2017), and the paper does not.
   Runners-up: songbird LMAN, a dedicated variability generator for vocal exploration (Ölveczky et al., 2005), and
   rat ACC, switched into a "stochastic mode" by locus-coeruleus input (Tervo et al., 2014). See §6.
2. The brain has abundant intrinsic randomness (stochastic transmitter release with failure rates above 50 % at
   single CA1 contacts, channel noise), and balanced cortical networks amplify it into microscopic chaos: one extra
   spike yields ~28 extra spikes in its targets (London et al., 2010); release noise alone makes a detailed cortical
   model chaotic (Nolte et al., 2019).
3. A two-scale picture has direct support: chaotic or noisy microdynamics coexist with input-driven reliability and
   with near-critical collective dynamics (Lajoie et al., 2013; Monteforte & Wolf, 2012; Nolte et al., 2019;
   Dahmen et al., 2019; Wilting & Priesemann, 2019), and variability can be injected and gated on demand (§6).
4. Noise cannot supply what Sugiura's Theorem 3 asks for. Noise gives *unpredictability*, not *input resolution*;
   it caps resolution (London et al., 2010; Ganguli et al., 2008; Dambre et al., 2012; Hu et al., 2023), so exact
   (infinite-resolution, uniform-error) universality is out of reach for the brain in *any* dynamical regime.
5. The reconciliation for L2 therefore runs through finite resolution: in noisy or driven random networks the
   computational optimum sits where the *driven* dynamics are stable while the *undriven* network would be chaotic
   (Schuecker et al., 2018; Haruna & Nakajima, 2019; cf. Roig et al., 2026), which is the edge-of-stability claim in
   its defensible form. Stable fading-memory reservoirs are universal as a *family* under uniform error
   (Grigoryeva & Ortega, 2018), so Sugiura's pathology belongs to a single fixed reservoir with a varying readout only.

---

## 1. Sources of neural randomness

**Faisal, A. A., Selen, L. P. J., & Wolpert, D. M. (2008). Noise in the nervous system. *Nature Reviews
Neuroscience, 9*(4), 292–303. https://doi.org/10.1038/nrn2258**
Review of noise sources from molecular (channel gating, release) to behavioural level and of how the nervous system
counters or exploits them. *Relevance:* the anchor showing that noise enters at every level, including the input
stage, which already bounds the resolution with which any input can be represented.

**White, J. A., Rubinstein, J. T., & Kay, A. R. (2000). Channel noise in neurons. *Trends in Neurosciences, 23*(3),
131–137. https://doi.org/10.1016/S0166-2236(99)01521-0**
Review of stochastic ion-channel gating as a source of membrane-potential and spike-timing variability
**[not re-read]**. *Relevance:* thermodynamic, irreducible source.

**Faisal, A. A., White, J. A., & Laughlin, S. B. (2005). Ion-channel noise places limits on the miniaturization of the
brain's wiring. *Current Biology, 15*(12), 1143–1149. https://doi.org/10.1016/j.cub.2005.05.056**
Axons below 0.1 µm diameter become inoperable because single spontaneously opening Na⁺ channels trigger spurious action
potentials; anatomical surveys show the thinnest conducting axons sit at 0.08–0.1 µm. *Relevance:* quantifies channel
noise as a hard physical limit; the brain operates close to it.

**Schneidman, E., Freedman, B., & Segev, I. (1998). Ion channel stochasticity may be critical in determining the
reliability and precision of spike timing. *Neural Computation, 10*(7), 1679–1703.
https://doi.org/10.1162/089976698300017089**
Channel stochasticity sets spike-timing jitter, and its effect depends on the input regime **[not re-read]**.

**Mainen, Z. F., & Sejnowski, T. J. (1995). Reliability of spike timing in neocortical neurons. *Science, 268*(5216),
1503–1506. https://doi.org/10.1126/science.7770778**
Constant input gives imprecise spikes; fluctuating, synaptic-like input gives spike timing reproducible to < 1 ms, which
implies low intrinsic noise in spike generation itself. *Relevance:* the single neuron is a reliable, input-sensitive
device; the dominant randomness comes from synapses and from the network (see §2).

**Allen, C., & Stevens, C. F. (1994). An evaluation of causes for unreliability of synaptic transmission. *Proceedings
of the National Academy of Sciences, 91*(22), 10380–10383. https://doi.org/10.1073/pnas.91.22.10380**
At individual CA1 contacts more than half of arriving spikes fail to evoke a postsynaptic response; the cause is
probabilistic release at low-capacity synapses, not axonal failure or in-vitro artefacts.

**Branco, T., & Staras, K. (2009). The probability of neurotransmitter release: Variability and feedback control at
single synapses. *Nature Reviews Neuroscience, 10*(5), 373–383. https://doi.org/10.1038/nrn2634**
Release is stochastic and each terminal tunes its own release probability through local feedback. *Relevance:* the
brain's largest noise source is *regulated*, which is what "noise on demand" requires.

**Levy, W. B., & Baxter, R. A. (2002). Energy-efficient neuronal computation via quantal synaptic failures. *The
Journal of Neuroscience, 22*(11), 4746–4755. https://doi.org/10.1523/JNEUROSCI.22-11-04746.2002**
Synaptic failures can raise information processed per unit energy; the predicted optimal failure rate, f ≈ 4^(−H(p*)),
matches physiological values.

**Rusakov, D. A., Savtchenko, L. P., & Latham, P. E. (2020). Noisy synaptic conductance: Bug or a feature? *Trends in
Neurosciences, 43*(6), 363–372. https://doi.org/10.1016/j.tins.2020.03.009**
Action potentials more often than not fail to trigger release; synaptic noise improves information transmission only
in restricted conditions but improves information per release more broadly.

**Malkin, J., O'Donnell, C., Houghton, C. J., & Aitchison, L. (2024). Signatures of Bayesian inference emerge from
energy-efficient synapses. *eLife, 12*, RP92595. https://doi.org/10.7554/eLife.92595**
Synaptic variability that trades energy against reliability produces the variability pattern Bayesian synapses would
show **[not re-read]**. *Relevance:* recent case for release noise as encoded uncertainty.

**Destexhe, A., Rudolph, M., & Paré, D. (2003). The high-conductance state of neocortical neurons in vivo. *Nature
Reviews Neuroscience, 4*(9), 739–751. https://doi.org/10.1038/nrn1198**
In vivo, intense background synaptic bombardment puts cortical neurons in a high-conductance, fluctuation-driven
regime **[not re-read]**. *Relevance:* spontaneous activity is the brain's standing noise floor.

**McDonnell, M. D., & Ward, L. M. (2011). The benefits of noise in neural systems: Bridging theory and experiment.
*Nature Reviews Neuroscience, 12*(7), 415–425. https://doi.org/10.1038/nrn3061**
Noise can improve processing in nonlinear systems ("stochastic facilitation"), with stochastic resonance the best
documented case; theory and experiment are not yet reconciled.

**McDonnell, M. D., & Abbott, D. (2009). What is stochastic resonance? Definitions, misconceptions, debates, and its
relevance to biology. *PLoS Computational Biology, 5*(5), e1000348. https://doi.org/10.1371/journal.pcbi.1000348**
Clarifies what stochastic resonance does and does not show. *Relevance:* stochastic resonance raises sensitivity to
*sub-threshold* inputs; it lowers a detection threshold and cannot produce unbounded resolution.

**Moss, F., Ward, L. M., & Sannita, W. G. (2004). Stochastic resonance and sensory information processing: A tutorial
and review of application. *Clinical Neurophysiology, 115*(2), 267–281. https://doi.org/10.1016/j.clinph.2003.09.014**
Tutorial and review of stochastic resonance in sensory systems.

**Deco, G., Rolls, E. T., & Romo, R. (2009). Stochastic dynamics as a principle of brain function. *Progress in
Neurobiology, 88*(1), 1–16. https://doi.org/10.1016/j.pneurobio.2009.01.006**
Finite-size spiking noise drives transitions between attractors in decision and memory networks **[not re-read]**.
*Relevance:* noise as a functional driver near multistability, i.e. near a bifurcation.

## 2. Deterministic chaos in cortical networks as a randomness generator

**Sompolinsky, H., Crisanti, A., & Sommers, H. J. (1988). Chaos in random neural networks. *Physical Review Letters,
61*(3), 259–262. https://doi.org/10.1103/PhysRevLett.61.259**
Random rate networks undergo a sharp transition from a fixed point to chaos at coupling gain g = 1 in the large-N
limit. *Relevance:* the canonical "edge of chaos" for recurrent networks.

**van Vreeswijk, C., & Sompolinsky, H. (1996). Chaos in neuronal networks with balanced excitatory and inhibitory
activity. *Science, 274*(5293), 1724–1726. https://doi.org/10.1126/science.274.5293.1724**
Balanced E/I networks generate irregular, chaotic firing internally, with no external noise. *Relevance:* cortex can
be its own random generator by deterministic means.

**London, M., Roth, A., Beeren, L., Häusser, M., & Latham, P. E. (2010). Sensitivity to perturbations in vivo implies
high noise and suggests rate coding in cortex. *Nature, 466*(7302), 123–127. https://doi.org/10.1038/nature09086**
In rat barrel cortex in vivo, one extra spike in one neuron produces ~28 extra spikes in its postsynaptic targets; the
implied intrinsic membrane-potential variation is ±2.2–4.5 mV of "pure noise", so cortex likely uses a rate code.
*Relevance:* the strongest in-vivo evidence for microscopic chaos, and it cuts both ways: sensitivity is enormous, but
it destroys information at the spike-timing scale instead of resolving inputs more finely.

**Monteforte, M., & Wolf, F. (2010). Dynamical entropy production in spiking neuron networks in the balanced state.
*Physical Review Letters, 105*(26), 268104. https://doi.org/10.1103/PhysRevLett.105.268104**
Full Lyapunov spectra of balanced spiking networks; extensive chaos with an entropy production rate that sets how fast
information about initial conditions is lost **[not re-read]**.

**Monteforte, M., & Wolf, F. (2012). Dynamic flux tubes form reservoirs of stability in neuronal circuits. *Physical
Review X, 2*(4), 041007. https://doi.org/10.1103/PhysRevX.2.041007**
In balanced networks of fast-onset spiking neurons, phase space is partitioned into flux tubes: infinitesimal
perturbations decay (stable) while perturbations above a finite size push the trajectory into a different, exponentially
separating tube **[main result not re-read; the OpenAlex abstract is a press summary]**. *Relevance:* a literal
finite-resolution structure: stable below a threshold, chaotic above it. It is the closest known mechanism to the
"approach" that Sugiura et al. allow, and shows the approach saturates at a finite scale.

**Engelken, R., Wolf, F., & Abbott, L. F. (2023). Lyapunov spectra of chaotic recurrent neural networks. *Physical
Review Research, 5*(4), 043044. https://doi.org/10.1103/PhysRevResearch.5.043044**
Full Lyapunov spectra of rate networks, random-matrix approximations, dependence of attractor dimension and entropy
rate on coupling and input fluctuations; link from exponents to error propagation in trained networks. *Relevance:*
input fluctuations reduce entropy rate and dimension, i.e. drive tames chaos (see Rajan below).

**Rajan, K., Abbott, L. F., & Sompolinsky, H. (2010). Stimulus-dependent suppression of chaos in recurrent neural
networks. *Physical Review E, 82*(1), 011903. https://doi.org/10.1103/PhysRevE.82.011903**
Inputs actively suppress intrinsic chaos, up to a phase transition where chaos vanishes; suppression is strongest at a
resonant stimulus frequency. *Relevance:* the mechanism behind "chaotic when undriven, stable when driven".

**Molgedey, L., Schuchhardt, J., & Schuster, H. G. (1992). Suppressing chaos in neural networks by noise. *Physical
Review Letters, 69*(26), 3717–3719. https://doi.org/10.1103/PhysRevLett.69.3717**
Mean-field calculation of the maximal Lyapunov exponent as a function of gain and external noise; noise shifts the
chaos transition. *Relevance:* noise and chaos are not additive; noise can move a network back toward the edge.

**Lajoie, G., Lin, K. K., & Shea-Brown, E. (2013). Chaos and reliability in balanced spiking networks with temporal
drive. *Physical Review E, 87*(5), 052901. https://doi.org/10.1103/PhysRevE.87.052901**
Chaos persists under weak and strong drive, yet intermittent periods of highly reliable spiking coexist with unreliable
activity; chaos need not prevent precise responses.

**Nolte, M., Reimann, M. W., King, J. G., Markram, H., & Muller, E. B. (2019). Cortical reliability amid noise and
chaos. *Nature Communications, 10*(1), 3792. https://doi.org/10.1038/s41467-019-11633-8**
In a biophysical neocortical microcircuit, stochastic transmitter release is the critical source of internal variability
and causes rapidly diverging, chaotic dynamics; weak thalamocortical input transiently overcomes the chaos and yields
millisecond-reliable spikes. *Relevance:* the cleanest demonstration of the two-scale reading: synaptic noise seeds
chaos, input restores reliable (i.e. input-determined) responses.

**Toyoizumi, T., & Abbott, L. F. (2011). Beyond the edge of chaos: Amplification and temporal integration by recurrent
networks in the chaotic regime. *Physical Review E, 84*(5), 051908. https://doi.org/10.1103/PhysRevE.84.051908**
Reconstruction of small inputs from a sparse linear readout: gains and integration times peak at the edge and fall off
more slowly on the chaotic side, so good performance tolerates operating inside the chaotic regime.

**Laje, R., & Buonomano, D. V. (2013). Robust timing and motor patterns by taming chaos in recurrent neural networks.
*Nature Neuroscience, 16*(7), 925–933. https://doi.org/10.1038/nn.3405**
Training recurrent weights turns chaotic trajectories into locally stable channels that remain robust to noise
**[not re-read]**. *Relevance:* rich (chaotic) dynamics as raw material, stabilised where computation needs it.

**Mattera, A., Alfieri, V., Granato, G., & Baldassarre, G. (2025). Chaotic recurrent neural networks for brain
modelling: A review. *Neural Networks, 184*, 107079. https://doi.org/10.1016/j.neunet.2024.107079**
Recent review of chaotic RNNs as brain models **[not re-read]**.

## 3. Noise and chaos as a computational resource

**Maass, W. (2014). Noise as a resource for computation and learning in networks of spiking neurons. *Proceedings of
the IEEE, 102*(5), 860–880. https://doi.org/10.1109/JPROC.2014.2310593**
Review arguing that stochastic spiking implements sampling, probabilistic inference and exploration in learning
**[not re-read]**.

**Buesing, L., Bill, J., Nessler, B., & Maass, W. (2011). Neural dynamics as sampling: A model for stochastic
computation in recurrent networks of spiking neurons. *PLoS Computational Biology, 7*(11), e1002211.
https://doi.org/10.1371/journal.pcbi.1002211**
Stochastic spiking networks provably sample from Boltzmann distributions (MCMC in spike time) **[not re-read]**.

**Habenschuss, S., Jonke, Z., & Maass, W. (2013). Stochastic computations in cortical microcircuit models. *PLoS
Computational Biology, 9*(11), e1003311. https://doi.org/10.1371/journal.pcbi.1003311**
Extends sampling to data-based microcircuit models with stationary distributions **[not re-read]**.

**Orbán, G., Berkes, P., Fiser, J., & Lengyel, M. (2016). Neural variability and sampling-based probabilistic
representations in the visual cortex. *Neuron, 92*(2), 530–543. https://doi.org/10.1016/j.neuron.2016.09.038**
A sampling model accounts for stimulus-dependent variability, noise correlations and their modulation in V1
**[not re-read]**.

**Berkes, P., Orbán, G., Lengyel, M., & Fiser, J. (2011). Spontaneous cortical activity reveals hallmarks of an optimal
internal model of the environment. *Science, 331*(6013), 83–87. https://doi.org/10.1126/science.1195870**
In ferret V1, spontaneous activity becomes more similar to average evoked activity with development, as expected if it
samples the prior of an internal model **[not re-read]**. *Relevance to FMT:* spontaneous "noise" as the prior of a
world model.

**Echeveste, R., Aitchison, L., Hennequin, G., & Lengyel, M. (2020). Cortical-like dynamics in recurrent circuits
optimized for sampling-based probabilistic inference. *Nature Neuroscience, 23*(9), 1138–1149.
https://doi.org/10.1038/s41593-020-0671-1**
Networks trained only to sample correctly develop cortical signatures (stimulus-quenched variability, transient
overshoots, gamma oscillations) **[not re-read]**.

**Dhawale, A. K., Smith, M. A., & Ölveczky, B. P. (2017). The role of variability in motor learning. *Annual Review of
Neuroscience, 40*, 479–498. https://doi.org/10.1146/annurev-neuro-072116-031548**
Review: motor variability is partly actively generated and regulated for exploration **[not re-read]**.

**Wu, H. G., Miyamoto, Y. R., Gonzalez Castro, L. N., Ölveczky, B. P., & Smith, M. A. (2014). Temporal structure of
motor variability is dynamically regulated and predicts motor learning ability. *Nature Neuroscience, 17*(2),
312–321. https://doi.org/10.1038/nn.3616**
Higher task-relevant variability predicts faster learning in humans, and the nervous system reshapes variability toward
task-relevant dimensions **[not re-read]**.

**Tervo et al. (2014)** and **Murakami et al. (2017)** belong here too; they are listed in §6.

**Brembs, B. (2011). Towards a scientific concept of free will as a biological trait: Spontaneous actions and
decision-making in invertebrates. *Proceedings of the Royal Society B, 278*(1707), 930–939.
https://doi.org/10.1098/rspb.2010.2325**
Invertebrate spontaneous behaviour shows structured, nonlinear variability generated by the nervous system
**[not re-read]**.

*Human random-generation tasks (brief; a different topic).* Explicit random-number generation is poor and effortful
(repetition avoidance, counting bias; Brugger, P. (1997). Variables that influence the generation of random sequences:
An update. *Perceptual and Motor Skills, 84*(2), 627–661. https://doi.org/10.2466/pms.1997.84.2.627). Its algorithmic
complexity peaks around age 25 (Gauvrit, N., Zenil, H., Soler-Toscano, F., Delahaye, J.-P., & Brugger, P. (2017).
Human behavioral complexity peaks at age 25. *PLOS Computational Biology, 13*(4), e1005408.
https://doi.org/10.1371/journal.pcbi.1005408; the Zenil of L2 (v) is a co-author). These measure executive control of
output sequences, not the neural noise floor.

## 4. Noise and criticality; reservoirs with noise

**Maass, W., Natschläger, T., & Markram, H. (2002). Real-time computing without stable states: A new framework for
neural computation based on perturbations. *Neural Computation, 14*(11), 2531–2560.
https://doi.org/10.1162/089976602760407955**
The liquid state machine; universality for fading-memory filters needs a separation property (reservoir family) plus an
approximation property (readout) **[not re-read]**.

**Bertschinger, N., & Natschläger, T. (2004). Real-time computation at the edge of chaos in recurrent neural networks.
*Neural Computation, 16*(7), 1413–1436. https://doi.org/10.1162/089976604323057443**
In input-driven threshold networks, computational performance peaks at the order–chaos transition of the *driven*
system **[not re-read]**.

**Legenstein, R., & Maass, W. (2007). Edge of chaos and prediction of computational performance for neural circuit
models. *Neural Networks, 20*(3), 323–334. https://doi.org/10.1016/j.neunet.2007.04.017**
Performance predicted by the balance of kernel quality (separation) and generalisation (noise robustness), which
peaks near the edge **[not re-read]**. *Relevance:* the separation–robustness trade-off is exactly what a
finite-resolution reading of Sugiura needs.

**Schuecker, J., Goedeke, S., & Helias, M. (2018). Optimal sequence memory in driven random networks. *Physical Review
X, 8*(4), 041029. https://doi.org/10.1103/PhysRevX.8.041029**
Time-varying input suppresses chaos dynamically and shifts the transition to larger coupling than local stability
predicts; a regime of locally expansive but non-chaotic dynamics maximises sequential memory. *Relevance:* the strongest
analytical support for "locally sensitive, globally non-chaotic" as the optimum.

**Haruna, T., & Nakajima, K. (2019). Optimal short-term memory before the edge of chaos in driven random recurrent
networks. *Physical Review E, 100*(6), 062312. https://doi.org/10.1103/PhysRevE.100.062312**
Memory capacity, mutual and Fisher information peak before the edge of chaos, where the input-driven network is stable
while the same network without input is unstable. *Relevance:* same window as Roig et al. (2026), derived analytically.

**Ganguli, S., Huh, D., & Sompolinsky, H. (2008). Memory traces in dynamical systems. *Proceedings of the National
Academy of Sciences, 105*(48), 18970–18975. https://doi.org/10.1073/pnas.0804451105**
Fisher memory of past inputs in noisy linear networks is bounded by network size N **[not re-read]**. *Relevance:*
noise turns resolution into a finite budget.

**Dambre, J., Verstraeten, D., Schrauwen, B., & Massar, S. (2012). Information processing capacity of dynamical
systems. *Scientific Reports, 2*(1), 514. https://doi.org/10.1038/srep00514**
Total information-processing capacity of a fading-memory system is bounded by the number of state variables; noise
reduces it **[not re-read]**.

**Hu, F., Angelatos, G., Khan, S. A., Vives, M., Türeci, E., Bello, L., Rowlands, G. E., Ribeill, G. J., & Türeci, H. E.
(2023). Tackling sampling noise in physical systems for machine learning applications: Fundamental limits and
eigentasks. *Physical Review X, 13*(4), 041020. https://doi.org/10.1103/PhysRevX.13.041020**
Expressive capacity of any finitely sampled physical system is limited by noise; tight upper bound on the "resolvable
expressive capacity". *Relevance:* a general theorem that noisy physical reservoirs have finite resolution.

**Bishop, C. M. (1995). Training with noise is equivalent to Tikhonov regularization. *Neural Computation, 7*(1),
108–116. https://doi.org/10.1162/neco.1995.7.1.108**
Input noise during training is equivalent to a smoothness penalty. *Relevance:* noise pushes learned maps toward
continuity, the opposite of Theorem 3's dense discontinuity.

**Boedecker, J., Obst, O., Lizier, J. T., Mayer, N. M., & Asada, M. (2012). Information processing in echo state
networks at the edge of chaos. *Theory in Biosciences, 131*(3), 205–213. https://doi.org/10.1007/s12064-011-0146-8**
Information storage and transfer and memory capacity peak at the edge of chaos in ESNs **[not re-read]**.

**Carroll, T. L. (2020). Do reservoir computers work best at the edge of chaos? *Chaos, 30*(12), 121109.
https://doi.org/10.1063/5.0038163**
Counter-case: the edge can coincide with poor performance for some reservoirs and tasks **[not re-read]**.

**Morales, G. B., & Muñoz, M. A. (2021). Optimal input representation in neural systems at the edge of chaos.
*Biology, 10*(8), 702. https://doi.org/10.3390/biology10080702**
A reservoir reproduces the ~1/n covariance spectrum measured in mouse V1 only when set at the edge of chaos.

**Grigoryeva, L., & Ortega, J.-P. (2018). Echo state networks are universal. *Neural Networks, 108*, 495–508.
https://doi.org/10.1016/j.neunet.2018.08.025**
ESNs with linear readouts are universal *uniform* approximants of discrete-time fading-memory filters with uniformly
bounded inputs. *Relevance:* **[inference]** the approximating ESN is chosen per target (reservoir and readout), and
ESNs have the echo-state (contracting) property, so a *family* of stable, finite-dimensional reservoirs achieves
uniform universality. Sugiura's Theorem 3 constrains a *single fixed* reservoir whose readout alone varies. The
chaos requirement is a feature of that formulation.

**Gonon, L., & Ortega, J.-P. (2020). Reservoir computing universality with stochastic inputs. *IEEE Transactions on
Neural Networks and Learning Systems, 31*(1), 100–112. https://doi.org/10.1109/TNNLS.2019.2899649**
Universality with respect to L^p criteria for linear reservoirs, state-affine systems and ESNs with stochastic inputs,
without requiring uniform input bounds or fading memory in the target. *Relevance:* under an averaged error criterion
suited to noisy inputs, universality holds for stable reservoir families.

**Kinouchi, O., & Copelli, M. (2006). Optimal dynamical range of excitable networks at criticality. *Nature Physics,
2*(5), 348–351. https://doi.org/10.1038/nphys289**
Dynamic range (the span of stimulus intensities a noisy excitable network can discriminate) peaks at the critical
branching ratio **[not re-read]**. *Relevance:* criticality maximises *discriminable range*, a finite-resolution notion.

**Shew, W. L., Yang, H., Petermann, T., Roy, R., & Plenz, D. (2009). Neuronal avalanches imply maximum dynamic range in
cortical networks at criticality. *The Journal of Neuroscience, 29*(49), 15595–15600.
https://doi.org/10.1523/JNEUROSCI.3864-09.2009**
Experimental confirmation of Kinouchi–Copelli in cortex cultures **[not re-read]**.

**Priesemann, V., Wibral, M., Valderrama, M., Pröpper, R., Le Van Quyen, M., Geisel, T., Triesch, J., Nikolić, D., &
Munk, M. H. J. (2014). Spike avalanches in vivo suggest a driven, slightly subcritical brain state. *Frontiers in
Systems Neuroscience, 8*, 108. https://doi.org/10.3389/fnsys.2014.00108**
In vivo spike avalanches fit a driven, slightly subcritical state **[not re-read; full author list from memory,
Crossref returned the first author only]**.

**Wilting, J., & Priesemann, V. (2018). Inferring collective dynamical states from widely unobserved systems. *Nature
Communications, 9*(1), 2325. https://doi.org/10.1038/s41467-018-04725-4**
Subsampling-corrected estimator places cortex in a "reverberating" regime, close to but below criticality **[not
re-read]**.

**Wilting, J., & Priesemann, V. (2019). Between perfectly critical and fully irregular: A reverberating model captures
and predicts cortical spike propagation. *Cerebral Cortex, 29*(6), 2759–2770. https://doi.org/10.1093/cercor/bhz049**
Same regime, input-driven: activity is sustained by a mixture of external drive and near-critical propagation
**[not re-read]**.

**Dahmen, D., Grün, S., Diesmann, M., & Helias, M. (2019). Second type of criticality in the brain uncovers rich
multiple-neuron dynamics. *Proceedings of the National Academy of Sciences, 116*(26), 13051–13060.
https://doi.org/10.1073/pnas.1818972116**
Macaque motor cortex shows weak population fluctuations yet a large dispersion of pairwise correlations, the signature
of a second critical regime of balanced networks, hidden from macroscopic signals and useful for reservoir computing.
*Relevance:* microscopic criticality with macroscopic calm: a two-scale picture in data.

**Moretti, P., & Muñoz, M. A. (2013). Griffiths phases and the stretching of criticality in brain networks. *Nature
Communications, 4*(1), 2521. https://doi.org/10.1038/ncomms3521**
Hierarchical-modular structure stretches the critical point into an extended Griffiths phase **[not re-read]**.
*Relevance:* near-critical behaviour need not require fine tuning.

**Muñoz, M. A. (2018). Colloquium: Criticality and dynamical scaling in living systems. *Reviews of Modern Physics,
90*(3), 031001. https://doi.org/10.1103/RevModPhys.90.031001**; **Buendía, V., di Santo, S., Bonachela, J. A., & Muñoz,
M. A. (2020). Feedback mechanisms for self-organization to the edge of a phase transition. *Frontiers in Physics, 8*,
333. https://doi.org/10.3389/fphy.2020.00333**; **Kinouchi, O., Pazzini, R., & Copelli, M. (2020). Mechanisms of
self-organized quasicriticality in neuronal network models. *Frontiers in Physics, 8*, 583213.
https://doi.org/10.3389/fphy.2020.583213**
Reviews of self-organised *quasi*-criticality: with non-conservative dynamics and noise, homeostatic feedback holds a
system in a fluctuating band around the critical point **[not re-read]**. *Relevance:* "near the edge" is the realistic
statement; the band's width is set by noise and adaptation time scales.

**Toker, D., Pappas, I., Lendner, J. D., Frohlich, J., Mateos, D. M., Muthukumaraswamy, S., Carhart-Harris, R., Paff, M.,
Vespa, P. M., Monti, M. M., Sommer, F. T., Knight, R. T., & D'Esposito, M. (2022). Consciousness is supported by
near-critical slow cortical electrodynamics. *Proceedings of the National Academy of Sciences, 119*(7),
e2024455119. https://doi.org/10.1073/pnas.2024455119**
With a modified 0–1 chaos test on ECoG/MEG/EEG, waking low-frequency cortical dynamics sit near the edge-of-chaos
critical point; anaesthesia and seizures move away from it, psychedelics move closer. *Relevance:* direct empirical
support that the *macroscopic* (slow) scale sits at the stability–chaos boundary in conscious states.

**Metzner, C., Schilling, A., Maier, A., & Krauss, P. (2024). Recurrence resonance – noise-enhanced dynamics in
recurrent neural networks. *Frontiers in Complex Systems, 2*, 1479417. https://doi.org/10.3389/fcpxs.2024.1479417**
An optimal level of added noise increases information flux in recurrent networks trapped in few attractors.

## 5. Quantum-randomness claims (noted, not endorsed)

- **Hameroff, S., & Penrose, R. (2014). Consciousness in the universe: A review of the "Orch OR" theory. *Physics of Life
  Reviews, 11*(1), 39–78. https://doi.org/10.1016/j.plrev.2013.08.002** — orchestrated objective reduction in
  microtubules. Contested; no accepted evidence for a functional role.
- **Tegmark, M. (2000). Importance of quantum decoherence in brain processes. *Physical Review E, 61*(4), 4194–4206.
  https://doi.org/10.1103/PhysRevE.61.4194** — decoherence times (~10⁻¹³–10⁻²⁰ s) are far shorter than neural time
  scales **[figures not re-read]**; the standard rebuttal.
- **Fisher, M. P. A. (2015). Quantum cognition: The possibility of processing with nuclear spins in the brain. *Annals
  of Physics, 362*, 593–602. https://doi.org/10.1016/j.aop.2015.08.020** — Posner-molecule nuclear-spin hypothesis;
  speculative, partly tested in chemistry, not in neural function.
- **Jedlicka, P. (2017). Revisiting the quantum brain hypothesis: Toward quantum (neuro)biology? *Frontiers in Molecular
  Neuroscience, 10*, 366. https://doi.org/10.3389/fnmol.2017.00366** — balanced review of the state of the claims.

For L2 none of this is needed: classical channel and release noise are true thermal randomness at the scale that
matters, and microscopic chaos amplifies it (London et al., 2010; Nolte et al., 2019). Whether its ultimate origin is
thermal or quantum makes no difference to input resolution.

## 6. The "random generator linked to creativity" study (MG's lead)

**Best match: Murakami, M., Shteingart, H., Loewenstein, Y., & Mainen, Z. F. (2017). Distinct sources of deterministic
and stochastic components of action timing decisions in rodent frontal cortex. *Neuron, 94*(4), 908–919.e7.
https://doi.org/10.1016/j.neuron.2017.04.040** (PMID 28521140)
Rats in a waiting task; both mPFC and M2 are necessary. Both encode deterministic biases in action timing, **only M2
neurons reflect the stochastic trial-by-trial fluctuations**, and the two areas differ in time scale. The authors
propose "a two-stage model in which stochastic components of action timing decisions are injected by circuits
downstream of those carrying deterministic bias signals." The creativity link comes from Mainen's interview, not the
paper (Medrano, K., *Inverse*, 17 May 2017, "Our brains really do make lots of random decisions";
https://www.inverse.com/article/31679-random-brain-region-timing-predict-rats-human-action-behavior, fetched
2026-09-29): *"If you want creativity, the ability to come up with new ideas … that's in some ways random behavior,"*
and *"… do they really generate randomness, really just have dice inside?"* Why it fits MG's memory: one named region
that "is in on the randomness", explicitly tied to creativity in coverage.

**Strong alternative (causal, "actively used" in the strict sense): songbird LMAN.**
- **Ölveczky, B. P., Andalman, A. S., & Fee, M. S. (2005). Vocal experimentation in the juvenile songbird requires a
  basal ganglia circuit. *PLoS Biology, 3*(5), e153. https://doi.org/10.1371/journal.pbio.0030153** — inactivating LMAN
  rapidly and reversibly removes acoustic and sequence variability in juvenile song; LMAN neurons fire variably across
  renditions; "LMAN may act as a source of variability" for exploratory motor learning.
- **Kao, M. H., Doupe, A. J., & Brainard, M. S. (2005). Contributions of an avian basal ganglia–forebrain circuit to
  real-time modulation of song. *Nature, 433*(7026), 638–643. https://doi.org/10.1038/nature03127** — in adults, AFP
  activity variability tracks song variability, lesions abolish its modulation; frontal/basal-ganglia circuits may
  introduce "stochastic variability required for reinforcement learning".
- **Aronov, D., Andalman, A. S., & Fee, M. S. (2008). A specialized forebrain circuit for vocal babbling in the juvenile
  songbird. *Science, 320*(5876), 630–634. https://doi.org/10.1126/science.1155140** — babbling (subsong) needs LMAN,
  not HVC.
- **Andalman, A. S., & Fee, M. S. (2009). A basal ganglia–forebrain circuit in the songbird biases motor output to avoid
  vocal errors. *Proceedings of the National Academy of Sciences, 106*(30), 12518–12523.
  https://doi.org/10.1073/pnas.0903214106** — the same circuit also biases output, i.e. variability is steerable.

**Also a candidate: Tervo, D. G. R., Proskurin, M., Manakov, M., Kabra, M., Vollmer, A., Branson, K., & Karpova, A. Y.
(2014). Behavioral variability through stochastic choice and its gating by anterior cingulate cortex. *Cell, 159*(1),
21–32. https://doi.org/10.1016/j.cell.2014.08.037** — rats facing an unbeatable competitor switch to a "stochastic"
mode in which ACC engagement is suppressed; locus-coeruleus noradrenergic input into ACC controls the switch. Press
framed it as the brain choosing randomness; I found no creativity framing.

**Human DLPFC work (the human "random generation" literature; no creativity claim):** Jahanshahi, M., Profice, P., Brown,
R. G., Ridding, M. C., Dirnberger, G., & Rothwell, J. C. (1998). The effects of transcranial magnetic stimulation over
the dorsolateral prefrontal cortex on suppression of habitual counting during random number generation. *Brain,
121*(8), 1533–1544. https://doi.org/10.1093/brain/121.8.1533 ; Jahanshahi, M., & Dirnberger, G. (1999). The left
dorsolateral prefrontal cortex and random generation of responses: Studies with transcranial magnetic stimulation.
*Neuropsychologia, 37*(2), 181–190. https://doi.org/10.1016/S0028-3932(98)00092-X ; Jahanshahi, M., Dirnberger, G.,
Fuller, R., & Frith, C. D. (2000). The role of the dorsolateral prefrontal cortex in random number generation: A study
with positron emission tomography. *NeuroImage, 12*(6), 713–725. https://doi.org/10.1006/nimg.2000.0647 . Left DLPFC
*suppresses habitual counting* in an associative number network; it enforces randomness by inhibition and generates
none. Daniels et al. (2003, fMRI, *Neuroscience Letters*) **[unverified — DOI not resolved]**.

**Human creativity–noise link (no dedicated region):**
- **Bains, W. (2008). Random number generation and creativity. *Medical Hypotheses, 70*(1), 186–190.
  https://doi.org/10.1016/j.mehy.2007.08.004** — hypothesis paper: a basic, non-truly-random "creativity mechanism"
  supplies novelty against "closed programming loops". Speculative, n small.
- **Zhang, C., Zhang, W., Beste, C., & Hommel, B. (2026). Thinking out of the box: Divergent thinking is associated
  with increased aperiodic neural activity. *Journal of Cognitive Neuroscience, 38*(8), 1646–1657.
  https://doi.org/10.1162/JOCN.a.2521** (PMID 41779939; verified in PubMed, not in Crossref) — n = 51 EEG: divergent (not
  convergent) thinking raises aperiodic "neural noise" (flatter 1/f exponent), and the rise predicts idea novelty.
  **[inference]** The aperiodic exponent is also read as an E/I-balance and proximity-to-criticality marker, so this
  result sits at the junction of "noise" and "near-critical".

**Bearing on L2.** All three animal studies show variability that is *generated in a specific circuit, injected
downstream of deterministic computation, and switched by context or neuromodulation* (M2 vs mPFC; LMAN in juveniles
and in undirected adult song; LC→ACC). That is noise supplied on demand, which is compatible with a deterministic core
held near the edge of stability, and it supports a two-stage (two-scale) architecture. It does not supply what
Sugiura's Theorem 3 requires: injected variability makes *outputs* vary independently of inputs, and it reduces the
map's input resolution. It serves exploration and sampling, and has no bearing on input separation.

---

## (c) Assessment: does the literature support the two-scale reading?

**Supported, in this form:** microscopic chaos and synaptic noise supply unpredictability and sampling variability,
while collective, input-driven dynamics sit near but mostly below the edge.
- Micro: balanced-network chaos (van Vreeswijk & Sompolinsky, 1996), in-vivo single-spike amplification (London et
  al., 2010), release-noise-seeded chaos (Nolte et al., 2019).
- Macro: reverberating, slightly subcritical population dynamics (Priesemann et al., 2014; Wilting & Priesemann,
  2018, 2019); edge-of-chaos slow electrodynamics in wakefulness (Toker et al., 2022); correlation-dispersion
  criticality hidden from macroscopic signals (Dahmen et al., 2019).
- Coupling of the scales: input suppresses chaos (Rajan et al., 2010; Schuecker et al., 2018); drive restores reliability
  inside chaos (Lajoie et al., 2013; Nolte et al., 2019); flux tubes give stability below and chaos above a finite
  perturbation size (Monteforte & Wolf, 2012); dedicated circuits inject and gate variability (§6).
- Computational optimum: driven-stable/undriven-unstable window (Haruna & Nakajima, 2019; Schuecker et al., 2018;
  Bertschinger & Natschläger, 2004), with graceful extension into the chaotic side (Toyoizumi & Abbott, 2011).

**Strongest counter-evidence to "noise + near-criticality does what chaos does for Sugiura":**
1. *Noise bounds resolution.* London et al. (2010) conclude that amplified noise wipes out spike-timing information;
   Ganguli et al. (2008), Dambre et al. (2012) and Hu et al. (2023) bound capacity by N and noise. Sugiura's
   "infinite resolution" is therefore unreachable by the brain in any regime, chaotic ones included. Chaos in a noisy
   system amplifies noise as fast as it amplifies input differences, so it cannot beat the noise floor.
   **[inference]** Neither can exact universality survive noise as a concept: with noise the input→state map is a
   Markov kernel, and uniform approximation of a deterministic target is not well-posed.
2. *Noise regularises.* Training with noise enforces smoothness (Bishop, 1995); stochastic resonance only lowers a
   threshold (McDonnell & Abbott, 2009). Both push toward continuity, i.e. away from Theorem 3.
3. *The edge is not always optimal.* Carroll (2020); Du & Wang (2026, already in L2); Toyoizumi & Abbott (2011) show
   the optimum can lie inside the chaotic side.
4. *The pathology is formulation-specific.* Grigoryeva & Ortega (2018) and Gonon & Ortega (2020) obtain universality
   with stable, fading-memory reservoir families (uniform and L^p respectively). So "universality needs chaos" holds
   only for a single fixed reservoir with a varying readout, which weakens Sugiura's result as an argument about the
   brain in either direction.

**Net:** the literature supports a two-scale reading for *variability* (noise and microchaos generate it; the
collective scale stays near the edge), and gives no route by which noise supplies Sugiura's *unbounded input
sensitivity*. The coherent statement for L2 is that exact approximation universality is unreachable for any noisy
physical system; the relevant question is the finite-resolution optimum, which the driven-network theory places at
the edge of stability of the driven dynamics.

## (d) Candidate sentences for L2 (v)

Insert after the proposed Sugiura Theorem-3 sentence (see `docs/aiw269-sugiura-l2.md` §4).

> **S1.** Neural tissue supplies its own variability: stochastic transmitter release and channel noise, amplified by
> balanced recurrent circuits until one extra spike recruits about 28 further spikes (London et al., 2010; Nolte et
> al., 2019), and dedicated circuits that inject behavioural variability downstream of deterministic computation and
> are switched by context or neuromodulation (Ölveczky et al., 2005; Tervo et al., 2014; Murakami et al., 2017).

> **S2.** The same noise caps the resolution of any physical reservoir (London et al., 2010; Hu et al., 2023), so the
> infinite resolution of Sugiura et al.'s Theorem 3 is out of reach in every dynamical regime, and in driven random
> networks the finite-resolution optimum lies where the input-driven dynamics are stable although the undriven network
> would be chaotic (Schuecker et al., 2018; Haruna & Nakajima, 2019).

References to add to the roadmap bibliography if both are used: London et al. (2010); Nolte et al. (2019); Ölveczky et
al. (2005); Tervo et al. (2014); Murakami et al. (2017); Hu et al. (2023); Schuecker et al. (2018); Haruna & Nakajima
(2019). Optional addition if the formulation-specificity point is wanted: Grigoryeva & Ortega (2018).

Register check (prose-register.md): no not-X-but-Y construction, no self-narration, no throat-clearing, no banned
words; each claim carries its citation in the same sentence. S1's colon-list is two items, not a triad.
