---
title: "Explainer for the Jülich call brief (AIW-351)"
subtitle: "Reservoirs, spiking networks, Lyapunov exponents, DFA, branching and PCI, from first principles"
date: "2026-10-27"
---

# 0. How to use this

Companion to `drafts/aiw351-juelich-call-brief.md`. Terms are introduced as picture, then formula, then a small number example; the glossary at the end collects them. Numbers about our work come from crucible's substance file (`~/crucible/docs/cru226-juelich-substance.md`) and the crucible code; numbers about Michiel's work come from his public repository `DeLaVlag/TVB-Reservoir` and the research note `docs/research/aiw351-vandervlag-jsc-research.md`. Where the code and the substance file differ, the code wins and the difference is flagged with **[Flag]**.

**One notation trap before anything else.** The letter $\sigma$ means two different things in our own documents:

- in the brief and in the criticality code, $\sigma$ is the **branching ratio** (section 6.3);
- in the CRU-203 results and in `edge_peak.py`, $\sigma$ is the **spectral radius** of a weight matrix (section 3.3).

In this explainer the spectral radius is always $\rho$ and the branching ratio is always $\sigma$. When the substance file says "medium-task peak at $\sigma \approx 1.05$", that is $\rho \approx 1.05$. The brief's "never say $\sigma \approx 1$" is about the branching ratio.

# 1. The big picture

Michiel and crucible both build networks whose internal activity is a rich, fast-changing pattern, and both ask the same question of them: in which dynamical regime does such a network compute best? Michiel's networks are whole-brain simulations, 96 brain regions wired by a measured connectome; ours are artificial spiking networks of 22,000 to 30,000 model neurons. He measures the regime after the run with three standard instruments (Lyapunov exponent, DFA, PCI) and reports that "edge-of-chaos dynamics correspond to enhanced memory and prediction accuracy". We measured the regime carefully on our simplest networks and found the best performance in the ordered regime, well away from the edge. Neither side has built the step that FMT cares about: a network that carries a model of its own dynamics, predicts its own regime, and uses that prediction to steer itself. The call is the chance to design that experiment together, with his substrate and HPC machinery and our control arms and tested estimators, and to get a named route to the Jülich supercomputers, which only a German-employed PI can open for us.

# 2. Neural networks from zero

## 2.1 A neuron is a weighted sum followed by a squashing function

A model neuron takes several input numbers, multiplies each by a weight, adds them up, and passes the sum through a fixed nonlinear function. The weights decide which inputs matter and with what sign: a positive weight excites, a negative weight inhibits.

With inputs $u_1, \dots, u_n$, weights $w_1, \dots, w_n$, a bias $b$ and a nonlinearity $f$:

$$y = f\Big(\sum_{j=1}^{n} w_j u_j + b\Big).$$

A common choice is $f = \tanh$, which maps any real number into $(-1, 1)$, is close to the identity near $0$ (slope $1$) and flattens out ("saturates") for large positive or negative arguments. Its derivative is $\tanh'(z) = 1 - \tanh^{2}(z)$, which is $1$ at $z = 0$ and drops toward $0$ as $|z|$ grows. That derivative returns in the Lyapunov exponent.

**Example.** Inputs $u = (1, -2)$, weights $w = (0.5, 0.25)$, bias $b = 0.1$. The weighted sum is $0.5 \cdot 1 + 0.25 \cdot (-2) + 0.1 = 0.1$, and $y = \tanh(0.1) \approx 0.0997$.

<!-- FIGURE: neuron-weighted-sum | A model neuron multiplies each input by a weight, sums, adds a bias and squashes the result. | Left-to-right diagram. Three input circles labelled u_1=1, u_2=-2, u_3 (greyed, "...") on the left; arrows into a central circle, arrows labelled w_1=0.5, w_2=0.25; a small "+b, b=0.1" tag entering the circle from below; inside the circle the symbol Σ, then an arrow to a box drawing the tanh curve (x from -3 to 3, y from -1 to 1, curve passes through origin with slope 1, flattens near ±1), then an arrow to output y ≈ 0.0997. Under the tanh box, a tiny inset of its derivative 1 - tanh^2(z): a bump of height 1 at z=0 falling to near 0 at |z|=3, labelled "slope: 1 at centre, ~0 when saturated". -->
![A model neuron multiplies each input by a weight, sums, adds a bias and squashes the result.](figures/neuron-weighted-sum.png)

## 2.2 Many neurons at once: the matrix-vector form

Put $N$ neurons side by side. Their outputs form a vector $x \in \mathbb{R}^{N}$. If each neuron also reads the outputs of the others, the weights form an $N \times N$ matrix $W$, where entry $W_{ij}$ is the weight from neuron $j$ (presynaptic, the sender) to neuron $i$ (postsynaptic, the receiver). All $N$ weighted sums are then one matrix-vector product, $W x$, whose $i$-th entry is $\sum_j W_{ij} x_j$.

**Example.** $W = \begin{pmatrix} 0 & 0.5 \\ -1 & 0 \end{pmatrix}$, $x = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$. Then $Wx = \begin{pmatrix} 0 \cdot 2 + 0.5 \cdot 1 \\ -1 \cdot 2 + 0 \cdot 1 \end{pmatrix} = \begin{pmatrix} 0.5 \\ -2 \end{pmatrix}$.

A network is **recurrent** when the outputs feed back as inputs at the next time step, so the state evolves in time: $x_{t+1} = f(W x_t + \dots)$. A recurrent network has memory, because today's state carries traces of yesterday's input.

A **sparse** network has most $W_{ij}$ equal to zero. "Fan-in $K$" means each neuron receives from $K$ others. With $N = 30{,}000$ and $K = 2{,}000$, only $2{,}000 / 30{,}000 \approx 6.7\%$ of the possible connections exist, and the matrix has $N K = 6 \times 10^{7}$ nonzero entries ("edges").

## 2.3 Training versus fixed weights

**Training** means adjusting weights so the network's output matches a target. In ordinary deep learning every weight is trained, usually by gradient descent: compute an error $E$, take its derivative $\partial E / \partial w$ with respect to each weight, and move each weight a small step downhill, $w \leftarrow w - \eta \, \partial E / \partial w$ with a learning rate $\eta$. Doing this through a recurrent network is expensive and often unstable, because the derivative has to be propagated back through many time steps.

**Fixed weights** means the recurrent matrix $W$ is drawn at random once and never changed. Reservoir computing (next section) uses fixed recurrent weights and trains only the output layer. In the brief, "frozen weights" and "plasticity" refer to this distinction for our spiking networks: frozen means $W$ is fixed during the run; plastic means a learning rule changes $W$ while the network runs, which costs about $12\times$ more compute per step on our hardware.

# 3. Reservoir computing

## 3.1 The idea

Take a large recurrent network with fixed random weights, the **reservoir**. Drive it with an input signal. Because it is recurrent and nonlinear, its state at each moment is a complicated function of the recent input history, and that state holds many nonlinear combinations of past inputs. Then train only a **linear readout**: one weighted sum of the reservoir state per output, fitted so that it reproduces the target. Training a linear readout is a single least-squares problem, with no gradients through time.

Picture a pond. You throw stones (the input) into it; the ripples (the state) mix every recent throw. You never shape the pond; you only learn which places on the surface to watch and how to weight them so that their sum tells you what you want.

<!-- FIGURE: reservoir-schematic | A reservoir: input drives a fixed random recurrent pool; only the linear readout is trained. | Three blocks left to right. Left: an input signal u(t) drawn as a wiggly time series, arrow labelled "W_in (fixed, random)". Centre: a large circle containing ~25 dots with ~40 random directed arrows between them (some red = negative, blue = positive), labelled "reservoir W (fixed, random), state x(t)", with a curved arrow from the circle back into itself labelled "recurrence". Right: arrows from about 10 of the dots converge on one output node labelled "y(t) = W_out x(t)", and the arrows to it are drawn thicker and in orange with the label "W_out: the ONLY trained weights (ridge regression)". Below the right block, the target time series y_target(t) in grey overlaid with the output in orange. -->
![A reservoir: input drives a fixed random recurrent pool; only the linear readout is trained.](figures/reservoir-schematic.png)

## 3.2 The rate reservoir (echo-state network)

The simplest reservoir has neurons whose output is a real number, read as a firing rate. Hence "rate reservoir". The standard form is the **echo-state network** (ESN). With input vector $u_t$, input weights $W_{\text{in}}$, recurrent weights $W$ and a **leak rate** $a \in (0, 1]$:

$$x_{t+1} = (1 - a)\, x_t + a \tanh\!\big(W_{\text{in}} u_t + W x_t\big).$$

The leak blends the old state with the new one: $a = 1$ replaces the state each step; $a = 0.3$ keeps $70\%$ of the old state, which makes the reservoir slower and gives it longer memory.

**Our ESN exactly as built** (`crucible/fmt/reservoir/esn.py`, used by `experiments/edge_peak.py` for CRU-203): $N = 300$ neurons; $W_{\text{in}}$ entries uniform in $[-1, 1]$ times an input scaling of $2$; $W$ entries uniform in $[-1, 1]$, each kept with probability $0.1$ (so about $30$ nonzero inputs per neuron), then rescaled to a chosen spectral radius $\rho$; leak $a = 1$ in the primary arm, $0.3$ in a sensitivity arm. The input is two channels, $u_t = (s_t, 1)$, where $s_t$ is a random $\pm 1$ symbol each step and the constant $1$ acts as a bias. The task asks the readout for the product of two past symbols, $y_t = s_{t-k_1} s_{t-k_2}$, scored by whether the sign is right. Easy uses lags $(1, 2)$, medium $(2, 6)$, hard $(4, 11)$. Chance is $0.5$.

## 3.3 Spectral radius, and why it controls stability

The **eigenvalues** of a square matrix $W$ are the numbers $\mu$ for which some nonzero vector $v$ satisfies $W v = \mu v$: along that direction, $W$ only stretches (or shrinks, or flips). The **spectral radius** is the largest eigenvalue magnitude:

$$\rho(W) = \max_i |\mu_i|.$$

For a purely linear recurrence $x_{t+1} = W x_t$, after $t$ steps the component along an eigenvector is multiplied by $\mu^{t}$. If $\rho < 1$ every component shrinks and the network forgets its past; if $\rho > 1$ some component grows without bound. So $\rho$ sets whether activity dies out or blows up, and how slowly it dies out, which is memory.

**Example.** $W = \begin{pmatrix} 0.9 & 0 \\ 0 & 0.5 \end{pmatrix}$ has eigenvalues $0.9$ and $0.5$, so $\rho = 0.9$. A state $(1, 1)$ becomes $(0.9^{10}, 0.5^{10}) \approx (0.35, 0.001)$ after 10 steps. The slow direction remembers; the fast one has forgotten. Multiply $W$ by $2$ and $\rho = 1.8$: the first component grows as $1.8^{10} \approx 357$.

With $\tanh$, the picture changes in one useful way. The effective gain of each neuron at a given moment is its slope $1 - \tanh^{2}$, which is below $1$ whenever the neuron is pushed away from zero by input or bias. A strongly driven reservoir is partly saturated, its effective gains are smaller than $1$, and it can tolerate a larger $\rho$ before it becomes unstable. This is why, in CRU-203, the measured boundary sits at $\rho \approx 2.3$, not at $\rho = 1$.

## 3.4 The ridge-regression readout

Collect the reservoir states over $T$ training steps as rows of a matrix $X$ ($T \times N$, often with a column of ones appended for a bias), and the targets as a vector $y$ ($T$ entries). The readout weights $w_{\text{out}}$ minimise squared error plus a penalty on large weights:

$$w_{\text{out}} = \arg\min_w \; \|X w - y\|^{2} + \beta \|w\|^{2} = (X^{\top} X + \beta I)^{-1} X^{\top} y.$$

$\beta > 0$ is the **ridge** (regularisation) parameter and $I$ the identity matrix. Larger $\beta$ means smaller, smoother weights and ignores small-amplitude features of the state.

**Example (one state variable).** $X = (1, 2, 3)^{\top}$, $y = (2, 4, 7)^{\top}$, $\beta = 1$. Then $X^{\top} X = 14$, $X^{\top} y = 2 + 8 + 21 = 31$, and $w = 31 / (14 + 1) \approx 2.07$. With $\beta = 0$ it would be $31/14 \approx 2.21$.

The ridge matters for our datum. CRU-203 found that the left flank of the medium-task peak exists only when the readout is regularised ($\beta \ge 10^{-2}$): a weakly ordered reservoir still carries the lag-6 symbol, at small amplitude, and the ridge decides whether the readout can use it. Michiel's code uses $\beta = 2.5 \times 10^{-4}$ for the main fit and $10^{-4}$ for its in-loop refits.

## 3.5 Spiking reservoirs and the leaky integrate-and-fire neuron

Real neurons communicate with brief voltage pulses, **spikes**. A spiking model keeps a membrane voltage $v$ per neuron, lets it drift and integrate input, and emits a spike when $v$ crosses a threshold.

The **leaky integrate-and-fire** (LIF) neuron in continuous time:

$$\tau_m \frac{dv}{dt} = -(v - v_{\text{rest}}) + R\, I(t),$$

where $\tau_m$ is the **membrane time constant** (how fast the voltage forgets), $v_{\text{rest}}$ the resting voltage and $I(t)$ the input current. When $v \ge v_{\text{th}}$ (threshold), the neuron spikes and $v$ is **reset** to $v_{\text{reset}}$. Many models add a **refractory period** $t_{\text{ref}}$ during which the neuron cannot fire again.

In discrete time steps of length $\Delta t$, the leak becomes a multiplication by $L = e^{-\Delta t / \tau_m}$ per step. With $\Delta t = 1$ ms and $\tau_m = 20$ ms, $L = e^{-0.05} \approx 0.951$: without input, $4.9\%$ of the distance to rest is lost each millisecond.

The **synaptic time constant** $\tau_{\text{syn}}$ describes how long a spike keeps acting on its target. With $\tau_{\text{syn}} = 0$ a spike delivers its whole effect in one step. With $\tau_{\text{syn}} > 0$ the spike train is smoothed first, $g_t = A\, g_{t-1} + (1 - A)\, s_t$ with $A = e^{-\Delta t / \tau_{\text{syn}}}$, and the smoothed $g$ drives the target. Real synapses have $\tau_{\text{syn}}$ of roughly 2–10 ms (fast excitatory and inhibitory) up to 50–150 ms (slow NMDA), per the comment in `sparse_lif.py`.

**Rate coding versus spike coding.** In rate coding the information is in how often a neuron fires over a window (spikes per second). In spike (temporal) coding the information is in the precise timing of individual spikes. A rate reservoir assumes rate coding; a spiking reservoir can in principle use both.

<!-- FIGURE: lif-trace | A leaky integrate-and-fire neuron with crucible's default parameters: the voltage sits just under threshold, noise and input push it over, it spikes and resets to zero. | Single panel, x-axis time 0–100 steps (1 step = 1 ms), y-axis membrane voltage v from -0.1 to 1.2 (threshold units). Horizontal dashed red line at v_th = 1.0 labelled "threshold"; dotted grey line at v* = 0.9 labelled "resting level v* = 0.9 (rest_frac)"; solid grey line at v_reset = 0 labelled "reset". Trace: starts at 0.9, small noise (std 0.015 per step), input pulses of +0.08 at t = 20, 22, 24, 50, 51, 52, 53 drive it above 1.0 at t = 22 and t = 54 (as simulated with these values); at each crossing draw a vertical tick (spike) above the panel and drop v to 0; between, v recovers exponentially toward 0.9 with time constant 20 steps (v(t) = 0.9 - 0.9 e^{-t/20} after reset). Annotate one recovery segment "leak L = e^{-1/20} ≈ 0.951 per step". Note in corner: "no refractory period, no lower voltage bound (crucible defaults)". -->
![A leaky integrate-and-fire neuron with crucible's default parameters: the voltage sits just under threshold, noise and input push it over, it spikes and resets to zero.](figures/lif-trace.png)

# 4. Our networks, exactly as built

## 4.1 The spiking pool: `SparseLifPool`

`crucible/spiking/sparse_lif.py` holds the spiking substrate. Per neuron $i$, per step of $\Delta t = 1$ (one simulated millisecond), the update is:

$$v_i \leftarrow L\, v_i + \bar{b} + g \sum_j W_{ij}\, s_j^{\text{prev}} + \xi_i, \qquad \xi_i \sim \mathcal{N}(0,\, 0.015^{2}),$$

$$s_i = \begin{cases} 1 & v_i \ge \theta \\ 0 & \text{otherwise} \end{cases}, \qquad v_i \leftarrow v_{\text{reset}} = 0 \;\text{ if } s_i = 1.$$

The symbols, with their defaults in the code:

- $L = e^{-\Delta t / \tau_m}$, $\tau_m = 20$ steps (so $L \approx 0.951$);
- $\theta = 1$ is the threshold, $v_{\text{reset}} = 0$;
- $\bar{b} = 0.9\, \theta\, (1 - L)$ is a constant background drive, chosen so that without spikes the voltage settles at $v^{*} = 0.9$, just under threshold ("rest_frac" $= 0.9$);
- $\xi_i$ is fresh Gaussian noise each step (standard deviation $0.015$); it pushes the near-threshold tail across and seeds spontaneous activity;
- $g$ is a global **gain** that scales all recurrent input, and the main knob in regime sweeps;
- $s^{\text{prev}}$ is the 0/1 spike vector of the previous step.

**Defaults the brief does not mention.** There is no refractory period by default (`t_ref=None`), no lower bound on $v$ (`v_floor=None`, the "unbounded membrane" that the artifact audit of 2026-10-07 found behind several falsified results), and no synaptic smoothing (`tau_syn=None`: spikes act in one step). All three can be switched on; CRU-69's $\tau_{\text{syn}}$ sweep used the smoothing.

**Connectivity rule.** In the homogeneous pool each neuron receives exactly $K$ inputs (`target_fanin`), drawn uniformly at random from all $N$ neurons, with magnitudes uniform in $(0, 1)$. $80\%$ of neurons are excitatory, $20\%$ inhibitory (`exc_fraction=0.8`), and the sign follows the sender ("Dale's law": every outgoing weight of an excitatory neuron is positive, of an inhibitory one negative). Each sender's outgoing magnitudes are normalised to sum to $0.45$ (`syn_scale`), so one spike delivers a total of $0.45$ threshold units, spread over its targets. The matrix is stored in compressed sparse-row form, so a 1M-neuron pool with $K = 2{,}000$ is $2 \times 10^{9}$ stored edges.

**Optional homeostasis.** `_homeostatic_step`, off by default, keeps a running average $\bar{r}_i$ of each neuron's firing and moves its threshold, $\theta_i \leftarrow \theta_i + \eta\,(\bar{r}_i - 0.04)$ with $\eta = 0.02$: fire more than 4% of steps and your threshold rises. This is the only online self-regulation in crucible. It regulates rate, neuron by neuron, with no model of anything.

## 4.2 The closure brain: `ClosureBrain`

`crucible/spiking/closure_brain.py` builds one `SparseLifPool` whose neurons are split into four named **circuits** (regions) with default sizes summing to 22,000:

| circuit | size | role in the code |
|---|---:|---|
| CE | 8,000 | "criticality engine", strongest internal recurrence |
| EWM | 6,000 | world / sensory baseline |
| ISM | 4,000 | interoceptive self-body core |
| ESM | 4,000 | the self region: reads the rest and re-enters into it |

The connectome is built block by block (`StructuredConnectome`): for each ordered pair (source circuit, target circuit) every possible edge exists independently with a fixed probability $p$ (a Bernoulli draw, unlike the fixed fan-in of the homogeneous pool). The defaults: within-circuit $p = 0.06$ (CE, ESM) or $0.05$ (EWM, ISM); CE$\leftrightarrow$EWM and CE$\leftrightarrow$ISM $0.02$; EWM$\leftrightarrow$ISM $0.01$; every rest circuit $\to$ ESM $0.03$ ("ESM reads"); ESM $\to$ every rest circuit $0.03$ ("re-entry"). Dale's law and the $0.45$ per-sender normalisation hold globally. The calibrated per-circuit dynamics (`DEFAULT_REGIONAL`) give ISM and ESM a slower membrane, $\tau_m = 40$, and ISM a resting level $0.925$.

**[Flag]** The code comments describe CE as sustaining "$\sigma \approx 1$" and the regional profile as calibrated to per-region $\sigma \in [0.8, 1.2]$. Those are calibration targets read with the naive branching ratio, which CRU-194 later showed reads firing rate. The substance file's rule stands: no "$\sigma \approx 1$" claim. **Corrected 2026-10-27:** crucible rewrote these comments (and the same wording in four more modules) to read "fires at a matched rate", never criticality.

## 4.3 What "closure" and "re-entry" mean in this code

**Closure** is the ESM $\to$ rest block of $W$: the self region's spikes flowing back into the circuits it reads. One switch, `closure_enabled`, controls it.

- **Closed (ON):** the ESM $\to$ rest block is live. ESM reads CE, EWM and ISM, computes on what it read, and its output re-enters them, so the rest is driven by a summary of itself.
- **Cut (OFF):** that block is zeroed. ESM still reads the rest and still spikes, but sends nothing back. The rest is then byte-identical to a run with ESM deleted (`ablate_esm=True`), and the tests check this exactly.

The **loop** in CRU-69 and CRU-108 is a narrower object: a low-rank pathway that reads a span of circuits and writes back into the same span through $k$ intermediate channels. It is billed $2 \cdot |\text{span}| \cdot k$ connections (read $|\text{span}| \times k$, write $k \times |\text{span}|$). **Example:** the loop over EWM alone costs $96{,}000$ in CRU-69; with $|\text{span}| = 6{,}000$ that is $2 \cdot 6{,}000 \cdot k = 96{,}000$, so $k = 8$. An all-to-all ("dense") connection over the same span costs $6{,}000 \times 5{,}999 = 35{,}994{,}000$, which is the `dense` entry in the CRU-69 table.

## 4.4 What the self-model is in this code

`crucible/spiking/self_model.py` (CRU-196) installs a self-model on the robot-bodied variant of the closure brain. ESM's incoming connections from the rest are made plastic, everything else is frozen, and ten fixed readouts of ESM activity (each the difference of two random halves of ESM) are trained to predict the body one tick later: its own motion $(dx, dy, d\psi)$, tilt, free fall, touch, being on the table, and three felt-state variables (distress, pain, nervousness). The learning rule is a three-factor rule: an eligibility trace per edge, multiplied by a supplied error signal. **The self-model predicts the body, and leaves the network's own dynamical regime unmodelled.** No crucible code reads $\lambda$, DFA or $\sigma$ online and acts on it; this gap is the opening the brief names.

The closest thing to a model of its own dynamics is `rate/route_a.py`'s `top_model_task`, which predicts its own layers one step ahead.

**[Flag]** CRU-222 rules that no result from FlowBody-based runs is quotable, and it lists the CRU-206 self-model properties among the affected work. Describe the self-model as built and tested code, and do not quote its results.

## 4.5 The control arms

Each arm exists to remove one alternative explanation of "the closed network did better".

| arm | what changes | what it rules out |
|---|---|---|
| closed | the loop is on | (the condition under test) |
| cut | the self region computes, but its output is not fed back | that merely having the extra circuit computing helps |
| capacity-matched open | the cut, plus every deleted re-entry edge re-placed elsewhere in the rest, keeping edge count and magnitudes (`capacity_matched_open`) | that the closed network won by having more synapses |
| scrambled / decoy | same wiring statistics, but the fed-back content no longer carries the self region's information (decoy brain: a matched loop of a different geometry; scrambled: shuffled re-entry) | that any feedback of matched strength helps, whatever it says |
| frozen tape | the re-entry signal recorded once and replayed, so it no longer depends on the current state | that a fixed time-varying drive does the job |
| AUX (CRU-69) | identical wiring, self region renamed | that the name of the region matters; CRU-69 tied exactly, $288{,}000$ vs $288{,}000$ |

The code docstring for `capacity_matched_open` states its own limit: CRU-58 showed that cutting the re-entry decomposes one closed system into two, because ESM's internal recurrence survives. The arm removes the cost confound and nothing more; its honest name is "efferent disconnection of the self region".

<!-- FIGURE: closurebrain-arms | The 22,000-neuron closure brain and its control arms. | Two rows. Top row, one large panel: four circles sized by neuron count — CE 8,000 (largest), EWM 6,000, ISM 4,000, ESM 4,000 — CE in the centre, EWM left, ISM right, ESM above. Each circle has a self-arrow labelled with its within-circuit p (CE 0.06, EWM 0.05, ISM 0.05, ESM 0.06). Grey two-way arrows CE-EWM (0.02), CE-ISM (0.02), EWM-ISM (0.01). Blue arrows from CE, EWM, ISM up to ESM labelled "reads, p=0.03". Red arrows from ESM down to CE, EWM, ISM labelled "re-entry (closure knob), p=0.03". Side note: "fan-out per sender normalised to 0.45; 80% excitatory; tau_m 20 (CE, EWM), 40 (ISM, ESM)". Bottom row, five small copies of the same layout, titled: (1) "closed" — red arrows solid; (2) "cut" — red arrows deleted, ESM still receives blue arrows and still spikes; (3) "capacity-matched open" — red arrows deleted, same number of extra grey arrows drawn inside the CE/EWM/ISM group in orange, label "edges re-placed, count kept"; (4) "scrambled / decoy" — red arrows present but drawn dashed with a shuffle icon, label "matched strength, wrong content"; (5) "frozen tape" — red arrows replaced by a cassette icon feeding CE/EWM/ISM, label "recorded re-entry replayed". -->
![The 22,000-neuron closure brain and its control arms.](figures/closurebrain-arms.png)

## 4.6 Cost at matched function, with the two numbers we quote

A capability test asks: can the closed network do the task and the cut one cannot? The stationary-closure theorem makes that question unanswerable in our favour by construction: any finite closed loop run for a finite time can be unrolled into a feedforward network with memory, so in principle anything the loop does, a big enough open system also does. The question that survives is about **cost**: how many synapses (or parameters) does each architecture need to reach the **same** performance, and does the gap grow as the task becomes more open-ended?

The procedure: fix a criterion in advance, give each arm a ladder of budgets, and find the smallest budget at which it reaches the criterion. The ratio of those budgets is the cost gap.

**CRU-69 (22,000-neuron closure brain, 8 seeds, ~11 h on the RTX 4090).** Task: complete a stored pattern on a never-cued half; criterion $c^{*} = 0.90$, fixed before any arm was built. The loop reached it at $96{,}000$ / $160{,}000$ / $288{,}000$ synapses for three content conditions (world, world+body, integrated). The best closure-free rival reached it at $2{,}531{,}790$ / $7{,}038{,}520$ / $22{,}777{,}110$, i.e. $26\times$, $44\times$ and $79\times$ the loop's cost. Check: $2{,}531{,}790 / 96{,}000 \approx 26.4$, and $22{,}777{,}110 / 288{,}000 \approx 79.1$. Of the five pre-registered falsifiers, F4 ("does rank alone explain the ordering?") came out "no-separation": not a pass. A follow-up sweep with synaptic smoothing reproduced every falsifier at $\tau_{\text{syn}} = 2$; at $\tau_{\text{syn}} = 10$ the criterion lies above what the architecture reaches even at full rank, so the comparison can no longer be scored. The boundary lies in $(5, 10]$.

**CRU-108 (spiking closure brain, relays physically wired as up/down pairs, 192 configurations, 8 individuals).** At matched performance the loop needed $575{,}488$ connections against $22{,}744{,}284$ for its rival, $39.5\times$ fewer, at a cost of about 4 points of ceiling ($\sim 0.995 \to \sim 0.954$).

**What the numbers count.** In CRU-69 the loop arms were billed as low-rank products but simulated as dense matrices (billed $125{,}888$ connections, simulated $323{,}424{,}256$, a factor $2{,}569$). So these ratios are statements about storage and wiring. They say nothing about dynamics or metabolic energy, and the CRU-108 energy result is withdrawn. The CRU-108 connection result, which does wire the bottleneck, stands.

<!-- FIGURE: cost-matched-function | Cost at matched function: each arm's performance against its synapse budget; the gap is read horizontally at the criterion line. | One panel, log x-axis "synapse budget" from 10^4 to 10^9, y-axis "completion accuracy" 0 to 1. Horizontal dashed line at c* = 0.90 labelled "criterion fixed in advance". Three schematic rising curves for the 'integrated' condition of CRU-69: (a) "loop:ALL" crossing 0.90 at 288,000; (b) "best closure-free rival (off_tau_direct)" crossing 0.90 at 22,777,110; (c) "dense" crossing 0.90 at 323,982,000. Mark each crossing with a dot and its value. Draw a horizontal double arrow along the criterion line from 288,000 to 22,777,110 labelled "79x". Small inset table in the lower right: "world: 96,000 vs 2,531,790 (26x); world+body: 160,000 vs 7,038,520 (44x); integrated: 288,000 vs 22,777,110 (79x)". Footnote: "curve shapes between the marked points are illustrative; the crossing values are measured". -->
![Cost at matched function: each arm's performance against its synapse budget; the gap is read horizontally at the criterion line.](figures/cost-matched-function.png)

## 4.7 How fast the substrate runs

The cost of one step is dominated by reading every stored edge once (the sparse matrix-vector product), at about $20.6$ picoseconds per edge on the RTX 4090. Memory is about $46.6$ KB per neuron.

**Worked example at 1M neurons.** $N K = 10^{6} \times 2{,}000 = 2 \times 10^{9}$ edges, times $20.6 \times 10^{-12}$ s, gives $\approx 41$ ms per step. A run of $24{,}000$ steps then takes $24{,}000 \times 0.041 \approx 984$ s $\approx 16$ minutes. Memory $10^{6} \times 46.6$ KB $\approx 46.6$ GB, which does not fit the 4090's 24 GB. A 1M-neuron pool has never been run.

| neurons | edges | ms per step | faster or slower than real time | memory |
|---:|---:|---:|---|---:|
| 30k | $6 \times 10^{7}$ | 1.233 | $0.81\times$ (1 ms simulated in 1.233 ms) | 1.40 GB |
| 100k | $2 \times 10^{8}$ | 4.107 | $0.24\times$ | 4.66 GB |
| 1M | $2 \times 10^{9}$ | ~41 (extrapolated) | ~$0.024\times$ | ~46.6 GB |

Plasticity is the expensive part: at $122{,}880$ neurons ($471.8$M edges), a frozen step costs $6.1$ ms and $3.78$ GB, a plastic step $77.7$ ms and $26.9$ GB. That ratio, $77.7 / 6.1 \approx 12.7$, is the "$\sim 12\times$" behind the brief's plasticity estimate.

# 5. His networks: The Virtual Brain reservoir

## 5.1 The Virtual Brain and the connectome

**The Virtual Brain (TVB)** is a simulation platform for whole-brain models. A whole-brain model divides the brain into regions and simulates one small dynamical system per region. The regions are coupled by a **connectome**: a matrix of connection strengths $w_{ij}$ between regions, measured from diffusion MRI tractography, plus a matrix of **tract lengths** $\ell_{ij}$. Signals travel along fibres at a finite **conduction speed** $c$, so region $i$ hears region $j$ with a delay $d_{ij} = \ell_{ij} / c$.

Michiel's code loads TVB's `connectivity_96` (96 regions). It normalises each column of the weight matrix to sum to one and rescales the whole matrix to spectral radius $0.95$. The coupling is then multiplied by a global coupling constant $G$ (fixed at $20$ in the paper configuration of the Montbrió code).

## 5.2 Neural-mass models: a population as a few equations

A brain region holds millions of neurons. A **neural-mass model** replaces them by a few variables describing the population average, and a few ordinary differential equations (ODEs) for how those averages change. One region becomes a point in a two- to five-dimensional state space instead of millions of spiking units.

**Montbrió–Pazó–Roxin (MPR).** For an infinite population of quadratic integrate-and-fire neurons whose excitabilities follow a Lorentzian (Cauchy) distribution, Montbrió, Pazó and Roxin (2015) showed that the population firing rate $r$ and mean membrane voltage $V$ obey two exact ODEs. In Michiel's kernel (`models/montbrio_heun.c`, time constant $\tau = 1$):

$$\tau \dot{r} = \frac{\Delta}{\pi \tau} + 2 r V,$$

$$\tau \dot{V} = V^{2} - \pi^{2} \tau^{2} r^{2} + \eta + J \tau r + I + c_r \, G \sum_j w_{ij}\, r_j(t - d_{ij}).$$

Here $\Delta$ is the spread of excitabilities, $\eta$ their centre, $J$ the strength of recurrent synapses inside the region, $I$ an external current, $c_r = 1$ the weight of the coupling through $r$, and the sum is the delayed input from other regions. Noise is added to both variables. The kernel integrates with forward Euler at $\Delta t = 0.01$ (a Heun integrator is present but switched off). **Gist:** each region is an excitable population that can sit quiet, fire steadily, or oscillate, depending on $\eta$, $J$ and $I$; the connectome lets regions push each other between those states.

**Larter–Breakspear** is an older, more detailed neural-mass model with voltage-gated ion channels (sodium, potassium, calcium) and excitatory and inhibitory subpopulations; it has its own kernel in the repository.

## 5.3 How his reservoir is used

The code maps the reservoir roles onto named regions. The Lorenz signal enters by overwriting the firing rate $r$ of three **input regions** (10, 17, 30). The readout is a ridge regression from the firing rates of the remaining 90 regions (96 minus three input and three output regions) to the three Lorenz coordinates. The fitted readout weights are then written into the connectome itself, as connections from those 90 regions into three **output regions** (16, 21, 23: paracentral lobule, postcentral gyrus, precentral gyrus, per the code's comment).

**The task: Lorenz prediction.** The Lorenz system is a three-variable chaotic ODE,

$$\dot{x} = s(y - x), \qquad \dot{y} = x(\varrho - z) - y, \qquad \dot{z} = x y - \beta z,$$

with the classic values $s = 10$, $\varrho = 28$, $\beta = 8/3$ used in his `utils/lorentz.py`. ($\varrho$ and $\beta$ here are Lorenz's parameters, unrelated to the spectral radius and the ridge.) Its trajectory never repeats and is sensitive to its starting point, so predicting it some way ahead is a standard benchmark for reservoirs. The score is the mean squared error (MSE) between predicted and true trajectory.

**His "closed loop".** During the prediction phase the code periodically refits a readout on the recent past, predicts the next stretch of the Lorenz trajectory, and writes those predictions back into the three input regions in place of the true signal (`gpu_data['thoughts']`). The network then runs on its own forecast. This is **output feedback**: the network's estimate of the external signal re-enters as if it were input. It carries no representation of the network's own state or dynamics, which is what a self-model would be.

## 5.4 His parameter sweeps

A **parameter sweep** runs the same model at many parameter settings to map where it behaves well. With three parameters on 16 grid points each, the grid has $16^{3} = 4{,}096$ points. In the MPR configuration the swept parameters are $I$ (from $-20$ to $10$), $J$ (from $-6$ to $30$) and $\eta$ (from $-10$ to $10$); the active launch script sweeps three Larter–Breakspear parameters 16 ways each. Every grid point is an independent simulation, so the sweep spreads over many GPUs: his JUWELS Booster script asks for 8 nodes with 4 GPUs each, 32 MPI ranks. After each run the code computes his three regime measures on the 90 reservoir regions.

<!-- FIGURE: tvb-setup | Michiel's TVB reservoir: a 96-region connectome of neural-mass nodes, Lorenz input into three regions, a ridge readout from 90 regions written back as connections to three output regions, and the prediction fed back into the input regions. | Left: a stylised brain outline (top view) with 96 small dots for regions and ~60 faint grey lines for connectome edges; three dots coloured green and labelled "input regions 10, 17, 30"; three dots coloured orange and labelled "output regions 16, 21, 23"; remaining 90 dots blue, labelled "reservoir regions (90)". A magnifier from one blue dot to a box showing the two MPR equations (r-dot and V-dot as in the text) and a tiny phase portrait (r on x, V on y). A small inset on one edge: "delay d_ij = tract length / conduction speed". Top left: a 3-D Lorenz butterfly with arrow "x, y, z overwrite r of input regions". Right: arrow from the 90 blue dots to a box "ridge readout, beta = 2.5e-4 -> predicted x, y, z", then an arrow labelled "readout weights written into connectome -> output regions". A curved arrow from the prediction box back to the green input regions labelled "closed loop = OUTPUT feedback (prediction replaces input)". A separate dashed box, unconnected, labelled "self-model of own dynamics: absent". Bottom strip: "sweep: 16 x 16 x 16 = 4,096 parameter sets; JUWELS Booster 8 nodes x 4 GPUs = 32 MPI ranks". -->
![Michiel's TVB reservoir: a 96-region connectome of neural-mass nodes, Lorenz input into three regions, a ridge readout from 90 regions written back as connections to three output regions, and the prediction fed back into the input regions.](figures/tvb-setup.png)

# 6. The measures

## 6.1 The Lyapunov exponent $\lambda$

**Intuition.** Start two copies of the same system from almost the same state and watch the distance between them. In an **ordered** system the distance shrinks: the system forgets small differences. In a **chaotic** system it grows exponentially: tiny differences explode. On the boundary it neither grows nor shrinks on average. The largest Lyapunov exponent $\lambda$ is the average exponential rate:

$$\delta(t) \approx \delta(0)\, e^{\lambda t}, \qquad \lambda = \lim_{t \to \infty} \frac{1}{t} \ln \frac{\delta(t)}{\delta(0)}.$$

$\lambda < 0$: ordered. $\lambda = 0$: the boundary, the "edge of chaos". $\lambda > 0$: chaotic. Units are "nats per step" (natural-log units per time step) or per second.

**Example.** Our CRU-203 peak sits at $\lambda = -0.682$ nats/step. Per step, a small difference is multiplied by $e^{-0.682} \approx 0.51$: it halves every step, and after 10 steps it is $e^{-6.82} \approx 0.001$ of its start. At $\lambda = +0.21$ (measured at $\rho = 3.18$) it is multiplied by $e^{0.21} \approx 1.23$ per step, and after 10 steps by $e^{2.1} \approx 8.2$.

<!-- FIGURE: lyapunov-divergence | Two nearby trajectories: in the ordered regime the gap shrinks as e^{lambda t} with lambda < 0, in the chaotic regime it grows with lambda > 0. | Two panels side by side, shared style. Each: top half shows two curves x(t) and x'(t) over t = 0..20 steps starting 0.01 apart. Bottom half: log-scale y-axis "separation delta(t)" from 1e-6 to 1e1, x-axis t = 0..20 steps, a straight line. Left panel title "ordered, lambda = -0.682 nats/step (CRU-203 peak)": separation starts at 0.01 and falls as 0.01 * e^{-0.682 t}, reaching ~1.1e-5 at t = 10; label "halves each step". Right panel title "chaotic, lambda = +0.21 nats/step (CRU-203 at rho = 3.18)": separation starts at 0.01, grows as 0.01 * e^{0.21 t}, reaching ~0.082 at t = 10 and ~0.67 at t = 20. Between panels a small centred note: "lambda = 0: separation flat on average = the edge". -->
![Two nearby trajectories: in the ordered regime the gap shrinks as e^{lambda t} with lambda < 0, in the chaotic regime it grows with lambda > 0.](figures/lyapunov-divergence.png)

**Three ways to measure it.**

1. **Benettin two-trajectory method.** Run the system and a twin started a distance $d_0$ away (we use $d_0 = 10^{-7}$). After every step, measure the distance $d_t$, add $\ln(d_t / d_0)$ to a running sum, and pull the twin back to distance $d_0$ along the same direction. $\lambda$ is the average of the summed logs. Our `two_trajectory_lyapunov` does this; it needs only the ability to run the model.

2. **Jacobian (tangent) method.** The **Jacobian** $J_t$ is the matrix of partial derivatives of the update map: entry $(i, j)$ is $\partial x_{t+1, i} / \partial x_{t, j}$, how much a nudge to neuron $j$ now moves neuron $i$ next step. An infinitesimal difference vector $v$ evolves exactly by $v_{t+1} = J_t v_t$. For our ESN,
$$J_t = (1 - a) I + a\, \mathrm{diag}\big(1 - \tanh^{2}(p_t)\big)\, W,$$
where $p_t = W_{\text{in}} u_t + W x_t$ is the vector of pre-activations. `driven_lyapunov` propagates one vector $v$ through $J_t$ along the actual trajectory, renormalises it every step, and averages $\ln \|J_t v_t\|$. This is "exact-Jacobian Lyapunov" in the brief. The two methods agree within $0.01$ and recover known answers to $10^{-9}$ in 21 tests. The formula also shows the saturation effect: the factor $1 - \tanh^{2}$ shrinks the Jacobian whenever neurons are driven hard.

3. **Rosenstein method, from a time series.** When you only have a recorded signal (EEG, or one region's output), you rebuild a state space from delayed copies: the point at time $t$ is $(x_t, x_{t+L}, x_{t+2L}, \dots, x_{t+(m-1)L})$, with embedding dimension $m$ and lag $L$. For each point, find its nearest neighbour that is far enough away in time (more than a minimum separation), follow both forward $k$ steps, and average the log distance over all pairs. The slope of mean log distance against $k$ is $\lambda$. Michiel's `gpu_lya.py` uses this with $m = 4$, $L = 5$, minimum separation $10$, $k$ up to $50$.

**Why "driven" matters.** A reservoir always runs under input. If both twins receive the same input, $\lambda$ measures whether the network's response is reproducible: with $\lambda < 0$ the state becomes a function of the input history alone and the initial state is forgotten. Reservoir people call this the **echo-state property**, and it is what a readout needs. That is the driven exponent our code measures. An **autonomous** exponent describes the system with no input. Rosenstein on a driven time series measures something in between: the recorded signal contains the input's own dynamics, and the Lorenz input is itself chaotic (its largest exponent is about $0.9$ per Lorenz time unit), so a positive estimate can come from the input instead of the reservoir.

## 6.2 Edge of chaos and "criticality"

**Edge of chaos** is the parameter region where $\lambda$ crosses zero. A long-standing hypothesis says computation is best there: ordered enough to hold information, close enough to chaos to mix it richly.

**Criticality** is a broader term from statistical physics: a system tuned to a phase transition, where fluctuations occur at all scales and many quantities follow power laws. In neuroscience it usually refers to "neuronal avalanches" with branching ratio $1$ and long-range temporal correlations.

**Our rule, from MG's ruling:** criticality is a signature, not a requirement. A system may show critical signatures without needing them, and may compute well away from them. Our one measured edge-related peak sits in the ordered regime.

<!-- FIGURE: regime-strip | Measured Lyapunov exponent and task accuracy against spectral radius for crucible's 300-neuron ESN (CRU-203, 30 seeds): the edge is at rho = 2.29, the medium-task peak at rho = 1.05, deep in the ordered regime. | Two vertically stacked panels sharing a log-scale x-axis "spectral radius rho" from 0.25 to 6.0. Background bands across both panels: blue from 0.25 to 2.29 labelled "ordered (lambda < 0)", a thin grey band 2.23-2.43 labelled "edge (lambda = 0), range across seeds", red from 2.29 to 6.0 labelled "chaotic (lambda > 0)". Top panel, y "lambda (nats/step)" from -2.2 to +0.7: points and line through (0.25, -2.04), (0.47, -1.41), (0.65, -1.11), (0.89, -0.80), (1.22, -0.51), (1.68, -0.24), (2.31, 0.00), (3.18, 0.21), (4.37, 0.39), (6.00, 0.55); horizontal dashed line at 0. Bottom panel, y "sign accuracy" 0.45-1.02, three curves at the same rho values — easy (1,2): 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.94, 0.71, 0.55; medium (2,6): 0.50, 0.58, 0.96, 1.00, 1.00, 0.98, 0.84, 0.68, 0.56, 0.51; hard (4,11): 0.50, 0.50, 0.50, 0.50, 0.52, 0.53, 0.54, 0.52, 0.51, 0.50; dotted line at 0.5 "chance". Vertical line through both panels at rho = 1.05 labelled "medium peak, lambda = -0.682 [CI -0.698, -0.666]"; vertical line at rho = 2.29 labelled "measured edge; medium accuracy there 0.84". Footnote: "leak 1, input scaling 2, ridge 1e-2, N = 300; 0/30 seeds within +/-0.05 of lambda = 0". -->
![Measured Lyapunov exponent and task accuracy against spectral radius for crucible's 300-neuron ESN (CRU-203, 30 seeds): the edge is at rho = 2.29, the medium-task peak at rho = 1.05, deep in the ordered regime.](figures/regime-strip.png)

## 6.3 The branching ratio $\sigma$

**Intuition.** Count how many neurons fire in each time bin, $A(t)$. A burst of activity that starts from one spike and spreads until the network falls silent again is an **avalanche**. If on average each active neuron causes $\sigma$ active neurons in the next bin, then $\sigma < 1$ makes avalanches die out quickly (subcritical), $\sigma > 1$ makes them grow into runaway activity (supercritical), and $\sigma = 1$ is the critical case, with avalanches of all sizes and a power-law size distribution.

**Formula (our `branching_sigma`, the Beggs–Plenz style estimator):**

$$\sigma = \frac{1}{|\mathcal{T}|} \sum_{t \in \mathcal{T}} \frac{A(t+1)}{A(t)}, \qquad \mathcal{T} = \{ t : A(t) > 0 \}.$$

**Example.** $A = (2, 3, 3, 4, 0, 1, 1, 0)$. Bins with $A(t) > 0$ and a successor: $3/2 = 1.5$, $3/3 = 1$, $4/3 \approx 1.33$, $0/4 = 0$, $1/1 = 1$, $0/1 = 0$. Mean $\approx 4.83 / 6 \approx 0.81$.

**Why it reads firing rate.** Take $N$ neurons that are **not connected at all**, each firing independently with probability $p$ per bin. Then $A(t)$ is a binomial count with mean $\mu = Np$, consecutive counts are independent, and $\mathbb{E}[A(t+1)/A(t)] = \mu \cdot \mathbb{E}[1/A(t)]$. Because $1/A$ is convex, $\mathbb{E}[1/A] \ge 1/\mu$, so the estimate comes out at about $1 + (1 - p)/(Np)$: slightly **above** 1, with no causal spreading at all. A network can therefore look "critical" on this estimator from its firing rate alone. CRU-194 measured exactly this on our demo brain: $\sigma = 1.021$ on 256 channels, against $1.038$ for a time-shuffled copy, and unwired random cells reproduced both $\sigma$ and the avalanche exponent.

**The rate-matched null.** Shuffle each neuron's spike train in time, independently of every other neuron (`rate_matched_shuffle`). Every neuron keeps its exact spike count, so all firing rates are preserved; all timing relations between neurons are destroyed. Compute $\sigma$ on the shuffled data. Only the **excess** $\sigma - \sigma_{\text{shuffled}}$ can be attributed to spreading through the wiring. `regime_battery` reports $\sigma$ always beside this surrogate. A second estimator, the multistep regression of Wilting and Priesemann (`mr_branching`), fits the decay of autocorrelations $r_k = b\, m^{k}$ over lags $k$ and is insensitive to rate and to subsampling; it reports $m$ only when the fitted amplitude $b$ is clearly nonzero.

<!-- FIGURE: branching-avalanches | Branching ratio: each active unit triggers on average sigma units in the next bin; and why the raw estimate needs a rate-matched null. | Top row, three small trees drawn as time bins left to right (5 bins), each node a filled circle, edges from a node to the nodes it activates. Left tree "sigma = 0.5 (subcritical)": 2 -> 1 -> 1 -> 0, dies fast. Middle tree "sigma = 1 (critical)": 1 -> 1 -> 2 -> 1 -> 1. Right tree "sigma = 1.5 (supercritical)": 2 -> 3 -> 5 -> 7, arrow off the edge "runaway". Bottom row, two panels. Left: raster of 20 unconnected neurons over 40 bins, each firing independently with p = 0.1 (random dots), with the population count A(t) below it as a bar plot; caption inside "unwired cells: sigma estimate ~ 1 + (1-p)/(Np) ≈ 1.45 here, no spreading at all". Right: a two-bar chart "CRU-194 demo brain, 256 channels": bar "measured sigma" = 1.021, bar "time-shuffled surrogate" = 1.038; y-axis 0.95-1.06; label "excess = measured - surrogate ≈ -0.017: no spreading beyond rate". -->
![Branching ratio: each active unit triggers on average sigma units in the next bin; and why the raw estimate needs a rate-matched null.](figures/branching-avalanches.png)

## 6.4 DFA, the exponent $\alpha$, and the Hurst exponent $H$

**Intuition.** Does the signal have long memory? In white noise each sample is independent of the last. In many natural signals (heartbeat intervals, alpha-band power in the EEG) a high value tends to be followed by more high values, over many time scales. Detrended fluctuation analysis (DFA) measures how the typical size of fluctuations grows with the length of the window you look at.

**The algorithm, step by step.** Given a signal $x_1, \dots, x_n$:

1. **Profile.** Subtract the mean and take the cumulative sum, $Y(k) = \sum_{i=1}^{k} (x_i - \bar{x})$. This turns the signal into a "random walk" whose wandering reflects the signal's memory.
2. **Windows.** Cut $Y$ into non-overlapping windows of length $n_w$.
3. **Detrend.** In each window, fit a straight line by least squares and subtract it (DFA-1).
4. **Fluctuation.** $F(n_w)$ is the root-mean-square of what remains, over all windows.
5. **Repeat** for many window lengths and plot $\log F$ against $\log n_w$. The **slope** is $\alpha$:
$$F(n_w) \propto n_w^{\alpha}.$$

**Reading $\alpha$.** $\alpha = 0.5$: white noise, no memory. $0.5 < \alpha < 1$: persistent long-range correlations. $\alpha = 1$: pink ($1/f$) noise, the textbook critical signature. $\alpha = 1.5$: brown noise, the random walk itself. $\alpha < 0.5$: anti-persistent, high tends to be followed by low.

**Example.** If doubling the window length from $16$ to $32$ raises $F$ from $2.0$ to $2.83$, then $\alpha = \log(2.83/2.0) / \log 2 \approx 0.50$: white noise. If it raised $F$ to $4.0$, $\alpha = 1$.

**Hurst exponent.** **Fractional Gaussian noise** (fGn) is the standard family of stationary Gaussian signals with a tunable memory parameter $H \in (0, 1)$, the **Hurst exponent**: $H = 0.5$ is white noise, $H > 0.5$ persistent, $H < 0.5$ anti-persistent. For fGn, DFA returns $\alpha \approx H$. That gives a test with known answers: generate fGn at $H = 0.3, 0.5, 0.7, 0.9$, run DFA, and check that it returns the $H$ you put in. Our `dfa_alpha` recovers $H$ from $0.3$ to $0.9$ within $\pm 0.06$. That is the "DFA recovering Hurst $\pm 0.06$" in the brief. `dfa_split` also reports $\alpha$ separately over short ($\le 64$ steps) and long ($\ge 128$ steps) windows, because a process with a correlation time of 10–30 steps reads $\alpha > 0.5$ at short windows and $0.5$ at long ones; one pooled $\alpha$ on a short recording would mistake that for long-range memory. CRU-194 found our demo brain anti-persistent ($\alpha \approx 0.25$) above about 300 ms.

<!-- FIGURE: dfa-steps | DFA in four steps: signal, cumulative profile, windows with straight-line fits, and the log-log slope alpha. | Four panels in a row. (1) "signal x_i": 512 samples of white noise (grey). (2) "profile Y(k) = cumulative sum of (x - mean)": the resulting random-walk curve. (3) "windows, n_w = 64": the same profile with vertical dashed lines every 64 samples and a red straight-line fit drawn in each of the 8 windows; shade the residual between curve and line in light red; label "F(64) = RMS of shaded residuals". (4) "log F vs log n_w": log-log axes, n_w = 8, 16, 32, 64, 128 on x; three straight lines with slopes 0.5 (grey, "white noise, H = 0.5"), 1.0 (pink, "pink noise"), 1.5 (brown, "brown noise / random walk"), plus a dashed line of slope 0.25 (blue, "anti-persistent; CRU-194 demo brain above ~300 ms"). Under panel 4, a small strip: "fGn known-answer test: H in = 0.3, 0.5, 0.7, 0.9 -> crucible dfa_alpha within +/-0.06". -->
![DFA in four steps: signal, cumulative profile, windows with straight-line fits, and the log-log slope alpha.](figures/dfa-steps.png)

## 6.5 PCI, the perturbational complexity index

**Intuition.** Knock the system and watch the echo. A system that is integrated but undifferentiated answers with one big uniform wave (low complexity); a system of disconnected parts answers locally and briefly (also low). A system that is both integrated and differentiated answers with a widespread but structured, varied response. PCI turns that intuition into one number by asking how well the response pattern compresses.

**Origin.** Casali and colleagues (2013) introduced PCI for humans: a pulse of transcranial magnetic stimulation (TMS) perturbs the cortex, EEG records the response, and PCI separates wakefulness from deep sleep and anaesthesia within the same person.

**Steps.**

1. **Perturb** one site (in a model: kick one region's state) and record all channels or regions afterwards.
2. **Binarise.** For each channel and time point, mark $1$ if the response exceeds what the pre-stimulus baseline would produce by chance (the threshold comes from shuffled baseline surrogates), else $0$. The result is a binary matrix, channels by time.
3. **Compress.** Count the **Lempel–Ziv complexity**: scan the binary string left to right and cut it into the shortest phrases that have not appeared before. More new phrases means less compressible.
4. **Normalise** by the complexity a random string of the same length and the same fraction of ones would have, so PCI lies roughly between $0$ (fully compressible) and $1$ (random-like).

**Lempel–Ziv example (the textbook case).** The string $0001101001000101$ parses as $0 \cdot 001 \cdot 10 \cdot 100 \cdot 1000 \cdot 101$: six phrases, complexity $6$. A constant string of sixteen zeros parses as $0 \cdot 000000000000000$: two phrases.

Michiel computes PCI on his reservoir runs with a CUDA kernel (`metrics/pci.c`, `pci_driver.py`) that follows these steps. We have no PCI implementation.

<!-- FIGURE: pci-steps | PCI: perturb, record the response, binarise against the baseline, compress with Lempel-Ziv. | Four panels left to right. (1) "perturb": a small network sketch (12 nodes) with a lightning bolt on one node, labelled "kick at t = 0". (2) "response": 12 stacked traces (one per node) over time -100 to +300 steps, a vertical line at t = 0; before 0 small noise, after 0 varied bumps in about 7 of the 12 traces. (3) "binarise": the same layout as a 12 x 30 grid of black (1) and white (0) cells after t = 0, with a label "1 = above shuffled-baseline threshold". (4) "compress": three example binary strings side by side with their Lempel-Ziv phrase cuts shown by vertical bars and the phrase count — "0000000000000000 -> 2 phrases (uniform wave: low)", "0001101001000101 -> 6 phrases", and a note "normalise by a random string with the same number of 1s -> PCI between ~0 and ~1". Footer: "origin: TMS-EEG in humans (Casali et al. 2013); in Michiel's code: a GPU kernel on the 96-region reservoir". -->
![PCI: perturb, record the response, binarise against the baseline, compress with Lempel-Ziv.](figures/pci-steps.png)

## 6.6 Spectral radius, once more

In the brief, "spectral radius" is the knob that most simply moves a reservoir between order and chaos, and the quantity Michiel uses to normalise his connectome ($0.95$). The point to carry into the call: the nominal spectral radius is a property of the weight matrix alone; whether the running system is ordered or chaotic also depends on the input, the bias and the leak, so the regime has to be **measured**, with $\lambda$. CRU-27 and CRU-203 both found the measured edge far from $\rho = 1$ (at $\rho \approx 2.6$ and $2.29$).

## 6.7 GPU-hours, GH200, MPI, job arrays

A **GPU-hour** is one graphics processor busy for one hour; computing allocations are granted in GPU-hours (or node-hours). The **GH200** (NVIDIA Grace Hopper) is the chip in Jülich's JUPITER Booster: an ARM CPU and an H100-class GPU on one module, with 96 GB of fast HBM memory and roughly four times the memory bandwidth of our RTX 4090, which matters because our step is limited by memory bandwidth. **MPI** (Message Passing Interface) is the standard library for programs that run across many processes and nodes and exchange data; it is needed when one simulation is too big for one GPU and has to be split. A **job array** is the opposite case: many independent runs (different seeds, arms, budgets), each fitting on one GPU, submitted together to the scheduler. Up to about 1M neurons, one of our runs fits one GH200, so the whole sweep is a job array with no MPI. Beyond 1–2M neurons the network would have to be partitioned across GPUs, and we have no code for that (ask 5). Michiel's sweeps already use MPI, but only to distribute independent parameter points over 32 ranks.

# 7. Our honest datum: the peak sits in the ordered regime

CRU-40 Part A had reported a medium-task accuracy peak "at the edge", but the edge there was assumed from the nominal spectral radius, never measured. CRU-203 replicated the experiment with $\lambda$ measured at every grid point, under a pre-registration committed before any confirmatory seed ran.

**Setup.** The ESN of section 3.2, $N = 300$, 41 spectral-radius points from $0.25$ to $6.0$, 30 fresh seeds; sensitivity arms for ridge, state noise and leak $0.3$; a scale arm at $N = 1{,}000$ and $2{,}000$. In total 140 jobs, about 14 minutes on 10 CPU processes.

**Result.**

- The **measured edge** ($\lambda = 0$) is at $\rho = 2.29$ (median; range $2.23$–$2.43$ across seeds).
- The **medium-task peak** is at $\rho = 1.05$ (range $0.89$–$1.13$), where $\lambda = -0.682$ nats/step (95% confidence interval $[-0.698, -0.666]$). **0 of 30** seeds have their peak within $\pm 0.05$ of $\lambda = 0$. The pre-registered verdict is FAIL-ORDERED: the peak is in the ordered regime.
- At the measured edge the medium accuracy has already fallen to $0.84$.
- The **shape** replicates: the easy task is flat across the ordered range, the medium task has an interior peak in 30/30 seeds, the hard task stays near chance at $N = 300$. Only the **location** moved.
- The peak is the **operand-memory peak**: it sits exactly where linear recall of the older symbol, $s_{t-6}$, peaks (paired difference in $\lambda$: $-0.008$, CI $[-0.032, +0.016]$). The network is best where it best remembers six steps back.
- The hard task improves with size ($0.558 \to 0.633 \to 0.718$ at $N = 300 / 1{,}000 / 2{,}000$), and its peak also stays ordered ($\lambda = -0.33$ and $-0.38$).
- No tested setting at leak $1$ brings the peak within $0.4$ nats/step of the edge. Stronger regularisation or noise moves it toward the edge. In the leak-0.3 arm the peak is at $\lambda = -0.14$, but accuracies there are low throughout, so that arm is descriptive only.

CRU-27 (leaky ESN, $N = 1{,}024$: edge at $\rho \approx 2.6$–$2.7$, memory and XOR peaking at $\rho$ 1.7–1.9 with $\lambda \approx -0.05$) and CRU-204 c5 (best $\rho$ at $\lambda$ between $-0.4$ and $-1.1$) point the same way; the spiking half of CRU-203 was uninformative, because the spiking pool's memory came from the membrane time constant, not from the recurrence.

**What this means for the call.** It contradicts the simple reading of his abstract on our simplest substrate, and it is a contrast to offer, not a refutation: his substrate differs, and his figures are unread. The useful question it raises is the one in the brief: do his three measures agree on where the edge is, and where is his performance peak when $\lambda$ is measured with an estimator whose known answers have been checked?

# 8. The joint experiment, step by step

**The question.** Does a network that carries a model of its own dynamics, and uses it to steer itself, need fewer resources than the alternatives to keep performing when the world changes?

**The substrate.** Two, in parallel: his TVB reservoir (96 neural-mass regions) and our sparse spiking pool. Running both tests whether a result depends on the kind of network.

**The task: non-stationary prediction.** The network predicts the Lorenz system, but the system changes during the run. Either its parameter $\varrho$ drifts slowly (the attractor gradually changes shape), or the source switches between Lorenz and the **Rössler** system, another three-variable chaotic ODE with a different geometry,
$$\dot{x} = -y - z, \qquad \dot{y} = x + a y, \qquad \dot{z} = b + z(x - c),$$
classically with $a = 0.2$, $b = 0.2$, $c = 5.7$. A fixed setting tuned for one regime of the input will be wrong after the drift; the drift rate is the "openness" axis.

**The self-model.** A small module that, every window:

- **reads** the reservoir's own state;
- **predicts** the reservoir's near-future regime ($\lambda$, DFA $\alpha$, $\sigma$ beside its null) and its own upcoming task error;
- **acts** by setting one global knob: the gain in our pool, or the global coupling $G$ in TVB.

It is a model of the network itself, used to regulate the network. That is the step neither side has taken.

**The arms, and what each rules out.**

| arm | what it does | if it matches the closed arm, the explanation is |
|---|---|---|
| closed | self-model's prediction drives the knob | (the condition under test) |
| cut | self-model computes, the knob ignores it | computing the prediction helped by itself, not using it |
| capacity-matched open | no self-model; the same parameter budget spent on a bigger readout | extra parameters, not the loop |
| scrambled | self-model's output shuffled before it drives the knob | any changing control signal helps, whatever its content |
| plain homeostasis | a regulator holding firing rate at a target, no model | rate regulation suffices; no model needed |
| fixed best-gain oracle | the single best fixed knob setting, found by search with hindsight | nothing needs regulating at this drift rate |

**The outcome measure: cost at matched function.** For each drift rate, find the parameters or synapses each arm needs to reach the closed arm's prediction error. The question is whether that cost gap exists, and whether it **grows** as the drift grows.

**Both instrument sets on every regime reading.** His Rosenstein $\lambda$, DFA and PCI, and our tangent $\lambda$, tested DFA and rate-matched $\sigma$, are computed on the same runs. Where they agree, the regime claim is solid; where they disagree, that disagreement is itself a result about the instruments.

<!-- FIGURE: joint-arms | The joint experiment: a self-model reads the reservoir, predicts its own regime and error, and sets the gain; six arms change one element each. | Top: one large loop diagram. Box "reservoir (TVB 96 regions OR crucible spiking pool)" receives "drifting Lorenz (rho drifts) / switching Lorenz <-> Rossler" from the left and sends "prediction -> MSE" to the right. A box above it, "self-model", with an arrow from the reservoir labelled "reads state" and a text block inside "predicts: lambda, DFA alpha, sigma vs null, own task error (next window)". An arrow from the self-model down to a knob icon on the reservoir labelled "sets global gain g / coupling G". Bottom: six small panels in a row, each a miniature of the loop with the changed element in red: (1) "closed" — full loop; (2) "cut" — arrow from self-model to knob broken; (3) "capacity-matched open" — self-model removed, readout box drawn larger with label "same parameters in readout"; (4) "scrambled" — shuffle icon on the self-model-to-knob arrow; (5) "plain homeostasis" — self-model replaced by a thermostat icon with "rate target"; (6) "fixed best-gain oracle" — knob locked, label "best fixed g, chosen with hindsight". Footer line: "DV: synapses/parameters each arm needs to reach the closed arm's MSE, as a function of drift rate; every regime read with BOTH instrument sets". -->
![The joint experiment: a self-model reads the reservoir, predicts its own regime and error, and sets the gain; six arms change one element each.](figures/joint-arms.png)

**What each result would mean.**

- **Closed cheaper than every other arm, and the gap grows with drift**, on both substrates: a model of the network's own regime is worth its cost exactly when the world keeps changing. That is the cost-window claim FMT makes for closure, observed in a regulated reservoir.
- **Closed equals capacity-matched open:** the loop adds nothing that the same budget in a bigger readout does not.
- **Closed equals scrambled:** feedback helps as perturbation or drive; its content does not matter.
- **Closed equals plain homeostasis:** keeping firing rates in range is all the regulation the task needs; a model of the regime is superfluous.
- **Oracle matches or beats closed at every drift rate:** a single good setting suffices; there is nothing for a self-model to track.
- **Cut equals closed:** the self-model's computation helps, but feeding its prediction back does not.
- **Result on one substrate only:** the effect depends on the network type; report it as such.
- **The two instrument sets disagree on the regime:** settle the measurement first, before reading any regime-based explanation.

<!-- FIGURE: decision-tree | What each outcome of the joint experiment would mean. | Top-down decision tree. Root box: "Does the closed arm reach the target MSE at lower cost than ALL other arms?" No-branches (left side), each a box: "...beaten or matched by capacity-matched open -> extra parameters, not the loop"; "...matched by scrambled -> any changing feedback helps; content irrelevant"; "...matched by plain homeostasis -> rate regulation suffices; no model needed"; "...matched by the oracle -> nothing to regulate at this drift"; "...matched by cut -> computing helps, feeding back does not". Yes-branch (right) -> box "Does the cost gap GROW with drift rate?" -> No: "advantage exists but is not tied to openness"; Yes -> box "Same on BOTH substrates (TVB and spiking)?" -> No: "substrate-specific effect; report as such"; Yes -> green box "a model of its own regime pays off when the world keeps changing: the FMT cost-window claim, in a regulated reservoir". A side box attached to the root with a dashed line: "Before reading any branch: do the two instrument sets (his Rosenstein/DFA/PCI, our tangent lambda/tested DFA/rate-matched sigma) agree on the regime? If not, resolve the instruments first." -->
![What each outcome of the joint experiment would mean.](figures/decision-tree.png)

# 9. The asks and the questions

## 9.1 What JSC would provide

**Size, seeds and plasticity.** Our rate reservoirs run in CPU minutes, so they need no supercomputer. Our largest spiking results are 22,000–30,000 neurons, which fit the RTX 4090. The open question needs 100k to 1M neurons, at least three openness levels (stationary, drifting, novel structure), four arms, 8–10 seeds, and a synapse-budget sweep per configuration to locate the matched-function point.

**The estimate, derived.** About 3 sizes $\times$ 4 openness levels $\times$ 4 arms $\times$ 8 seeds $\times$ 10 budget points $\approx 3{,}840$, call it 4,000 runs, dominated by the 1M-neuron ones. One 1M run of 24,000 steps takes about 16 minutes on 4090-class bandwidth, about 4 minutes on a GH200. That gives on the order of $10^{2}$–$10^{3}$ GH200 GPU-hours with frozen weights. Plasticity costs about $12\times$ per step, which gives $10^{3}$–$10^{4}$, and more memory. These are our estimates from measured per-step costs, not a design.

## 9.2 The five asks

**1. Instrument exchange now.** We run our tested estimators (tangent $\lambda$, DFA, rate-matched $\sigma$) on his public reservoir; he runs TVB-Reservoir against our controls.
*Why first:* it needs no compute allocation and no proposal, it can start next week on our own GPU, and it produces the first shared result.
*Good answer:* yes, with a named contact for questions about his code and his parameter files.
*Bad answer:* interest without commitment, or a request to wait for a proposal.

**2. A JSC test project hosted by him or the SDL.** Test projects are open all year, run up to four months, and can include some SDL support.
*Why:* JSC's regular routes require a PI employed at a German institution, so we cannot apply alone.
*Good answer:* he or the SDL agrees to host, and names the system (JURECA, JUWELS Cluster, JUPITER Booster) and a time frame.
*Bad answer:* "apply yourself", which is impossible under the rules, or a host role with no support behind it.

**3. A joint proposal with him as PI:** the next NIC window (11 Jan–15 Feb 2027, allocation from 1 May 2027), or EuroHPC Development Access once the Alpine Institute is registered (monthly cut-offs, one year, JUPITER among the systems).
*Why:* a test project is too small for the full sweep.
*Good answer:* agreement in principle and a rough timeline back from the January window.
*Bad answer:* no PI role on offer, leaving EuroHPC as our only route, which waits on the institute.

**4. A co-authored, pre-registered paper** on the joint experiment.
*Why:* pre-registration fixes the outcome measure and the arms before data exist, which is how crucible already works (CRU-69, CRU-203), and makes the result credible to both communities.
*Good answer:* agreement to co-author and to pre-register the cost-at-matched-function measure.
*Bad answer:* resistance to pre-registration, or a plan to publish the sweep without the control arms.

**5. Later: SDL help porting our spiking pool to multi-GPU** for more than 1M neurons.
*Why:* beyond one GH200's memory the network must be partitioned and the partitions must exchange spikes every step, and we have no such code. GPU code generation is his group's strength.
*Good answer:* "possible after a first phase".
*Bad answer:* a hard no is acceptable; the 1M-neuron sweep does not depend on it.

## 9.3 The four questions

**"Could an online $\lambda$ estimate drive the reservoir's own regulation?"**
*Meaning:* his $\lambda$ is computed after the run from a recorded series. A self-model needs a running estimate over a sliding window (a finite-time Lyapunov exponent), available fast enough to act on.
*Why ask:* this is the measurement the self-model would predict and the controller would use. For a rate model with a known Jacobian, the tangent method gives it cheaply; for spiking networks it needs twin runs.
*Good answer:* a concrete view on window length and noise, or a sign he has tried it.
*Bad answer:* none here; any answer tells us what he has.

**"How would he control for a self-model whose predictions change what it predicts?"**
*Meaning:* the self-model predicts the regime and then changes the knob that sets the regime. Its predictions are partly self-fulfilling: a model that predicts "ordered" and then lowers the gain makes itself right. Accuracy of prediction alone therefore proves little.
*Why ask:* this is the design problem of the experiment, and his research note mentions a "meta-reservoir" poster that may have met it. Our answer so far is the arm set: cut, scrambled and homeostasis separate a model from a regulator matched on the metrics.
*Good answer:* an additional control we have not thought of.
*Bad answer:* "the predictions will be accurate", which misses the point.

**"Do Lyapunov, DFA and PCI peak at the same parameters in his sweeps?"**
*Meaning:* if three measures all tracked one underlying "edge", they would agree on where it is. If they come apart (for example with noise or conduction speed), at least one is tracking something else.
*Why ask:* the self-model needs one quantity to predict and control, and our own branching-ratio experience says a single measure can mislead.
*Good answer:* a specific statement about agreement or disagreement, with conditions.
*Bad answer:* "they all show the edge", without the parameter locations.

**"Can an outside collaborator be added to his existing JSC projects?"**
*Meaning:* his scripts run under the JSC accounts `slns` and `vbt`. JSC manages project membership through its user portal (JuDoor), and whether an external person can join is unverified.
*Why ask:* if yes, this is the fastest start, faster than any test project.
*Good answer:* yes, with the steps.
*Bad answer:* no, which sends us back to ask 2.

# 10. The "do not say" list, explained

**"Our systems operate at criticality" or "$\sigma \approx 1$".** The naive branching ratio reads firing rate: unwired cells reproduce it, and on our demo brain the measured $\sigma$ equals its shuffled surrogate. The "six confirmations" of criticality, audited in CRU-201, turned out to be toy nulls or anti-edge results; the CRU-40 regime verdicts for steps 1, 3, 5, 6 and 7 are withdrawn or at risk. The one measured edge-related peak sits in the ordered regime. MG's ruling: criticality is a signature, not a requirement.

**That closure is necessary for capability.** Five results killed that claim, and the stationary-closure theorem shows it cannot hold in principle for a finite loop over a finite horizon. Route A found closed approximately equal to capacity-matched open; "closure maintains a model" is withdrawn; the self/world split in our brains is built in by construction, not emerged. The claim that survives is about cost at matched function.

**Any result from FlowBody runs (CRU-222).** The noise in those runs was never reseeded between repetitions, so their standard errors are understated and every significance statement on them is unreliable. Affected: route A S2/S3/S4, route B S0, the CRU-206 self-model properties, CRU-210.

**A ready 1M-neuron pipeline.** Nothing above 30k neurons has had a task or a criticality measurement; 100k was run only for throughput and a plasticity check; 1M has never run and would not fit our card. A plastic 30k pool already exceeds 24 GB. The scaled matched-function test has no design yet: workload, sizes, arms and budget are all open. It is a protocol to co-design.

**Anything about his figures.** The chapter is behind a bot-check wall and was not read; what we know comes from the abstract and the public code. Characterising his results beyond the abstract would be guessing.

**Smaller items from the substance file, in case they come up.** CRU-69's F4 is "no-separation", not a pass. CRU-74 is not adjudicable. CRU-139's 240-neuron claim is withdrawn. CRU-108's energy result is withdrawn; its connection result stands. The sentence in the companion paper (§8) that a wired bottleneck "has not run on the spiking substrate" predates CRU-108 and is wrong; do not repeat it. And the unbounded-membrane artifact falsified several older results (CRU-87 ladder, CRU-153 K1/K3, CRU-204b readings, CRU-204 depth rungs $\ge 1$) and puts others at risk.

## 10.1 Your call: the cross-check on his code

Crucible ran his own CUDA kernels unchanged on our RTX 4090 (repo pinned at commit 8606b72), called exactly as his pipeline calls them, on test signals whose right answer is known. Full record: `~/crucible/docs/cru226-vdvlag-code-verification.md`. In the terms of section 6:

- **DFA (`metrics/gpu_dfa.py`) does not measure the DFA exponent. Confirmed by run, four separate defects,** each shown to matter on its own by putting it back into a fixed kernel:
  1. *Indexing.* The kernel reads the data as if time were the outer index, while the array has region outer, so each region's "time series" is stitched from all regions. Changing only region 5 moves the result for all 68 regions.
  2. *No profile step.* The cumulative sum is missing, so the kernel detrends the signal rather than its random walk. On its own, this alone shifts every exponent down by one: a random walk, which should read 1.5, reads 0.5.
  3. *Sum instead of mean.* $F(n)$ adds the per-window values, so it also grows with the number of windows.
  4. *Ratio instead of slope.* $\alpha$ is the median of $\log F(n)/\log n$ rather than the slope of $\log F$ against $\log n$, so it shifts with the signal's overall amplitude.

  The result, as shipped: about $0.59$ for test signals whose true exponent is $0.3$, $0.5$, $0.7$ or $0.9$, and the value moves with scale alone ($-0.56$, $0.59$, $1.74$ for the same signal multiplied by $0.01$, $1$, $100$). A four-line fix recovers the known answers ($0.302$, $0.490$, $0.680$, $0.877$; random walk $1.451$).
- **Lyapunov (`metrics/gpu_lya.py`): the core algorithm is correct,** recovering Lorenz's exponent ($0.955$ against $0.906$). Three qualifications, all measured:
  - the exponent comes out exactly $10\times$ too large, because the code divides by $\Delta t = 0.01$ while samples are $0.1$ apart; the sign and the ordering are unaffected;
  - the 250-sample window makes it very sensitive to sampling; whether that biases his runs is not known;
  - **a provably stable linear system, driven by noise, reads positive** ($+0.31$ against a true $-0.31$). In a reservoir that is being driven, a positive value is therefore not by itself evidence of chaos, and this may affect where his "edge" sits.

**Not claimed:** anything about his chapter's figures (we have not read it), PCI, or the task error, and whether this November 2025 commit produced his published figures. Offer it kindly, as a cross-check, once the instrument exchange is agreed. The repro (a few minutes on one GPU) can be handed over as it is. Crucible withdrew its own branching-ratio readings for a similar driven-system confound, so this is "what our instruments taught us the hard way", which is true.

# 11. Glossary

| term | one-line meaning |
|---|---|
| activation function | the fixed nonlinearity applied to a neuron's weighted sum, e.g. $\tanh$ |
| autonomous (Lyapunov exponent) | measured on the system running without input |
| avalanche | a run of consecutive time bins with nonzero activity, bounded by silence |
| Benettin method | $\lambda$ from a twin trajectory renormalised to a fixed distance every step |
| branching ratio $\sigma$ | average number of active units in the next bin per active unit now |
| capacity-matched open | the loop removed and its budget given back elsewhere, so the cost comparison is fair |
| closure (crucible) | the self region's output re-entering the circuits it reads (ESM $\to$ rest) |
| connectome | matrix of connection strengths (and tract lengths) between brain regions |
| conduction speed / delay | how fast signals travel along fibres; delay = length / speed |
| cost at matched function | resources each architecture needs to reach the same performance |
| criticality | being tuned to a phase transition; signatures are $\sigma = 1$, power laws, $\alpha \approx 1$ |
| cut (arm) | the self region still computes, but its output is not fed back |
| Dale's law | each neuron's outgoing synapses all share one sign |
| DFA | detrended fluctuation analysis: how fluctuations grow with window length |
| DFA exponent $\alpha$ | slope of $\log F$ against $\log n$; 0.5 white, 1 pink, 1.5 brown |
| driven (Lyapunov exponent) | measured with the same input fed to both twins; $\lambda < 0$ means reproducible response |
| echo-state network (ESN) | rate reservoir $x_{t+1} = (1-a)x_t + a\tanh(W_{\text{in}} u_t + W x_t)$ |
| echo-state property | the reservoir state depends only on input history, not on its starting point |
| edge of chaos | where $\lambda$ crosses zero |
| eigenvalue | a number $\mu$ with $Wv = \mu v$ for some nonzero $v$ |
| fan-in $K$ | number of inputs each neuron receives |
| fractional Gaussian noise | Gaussian signal with tunable memory set by the Hurst exponent |
| frozen weights | recurrent weights fixed during the run |
| frozen tape | a recorded re-entry signal replayed, independent of current state |
| gain $g$ | global multiplier on recurrent input; the main regime knob |
| GH200 | NVIDIA Grace Hopper module in JUPITER Booster, 96 GB HBM |
| global coupling $G$ | TVB's multiplier on inter-region input |
| GPU-hour | one GPU busy for one hour; the unit of allocations |
| homeostasis | a rule that adjusts each neuron's threshold to hold its firing rate at a target |
| Hurst exponent $H$ | memory parameter; 0.5 none, above persistent, below anti-persistent |
| Jacobian | matrix of partial derivatives of the update map; moves small differences one step |
| job array | many independent single-GPU runs submitted together |
| JSC | Jülich Supercomputing Centre |
| leak rate $a$ | how much of the state an ESN replaces each step |
| Lempel–Ziv complexity | number of new phrases when a string is parsed left to right |
| LIF neuron | leaky integrate-and-fire: voltage leaks, integrates input, spikes at threshold, resets |
| Lorenz system | three-variable chaotic ODE, the standard prediction benchmark |
| Lyapunov exponent $\lambda$ | average exponential rate at which nearby trajectories separate |
| membrane time constant $\tau_m$ | how fast a neuron's voltage forgets |
| Montbrió–Pazó–Roxin | exact two-variable (rate, voltage) neural-mass model |
| MPI | library for programs split across many processes and nodes |
| MR estimator | multistep-regression branching estimate, insensitive to rate and subsampling |
| MSE | mean squared error |
| neural-mass model | a few ODEs for a population's average activity |
| NIC | John von Neumann Institute for Computing, which allocates JSC time |
| nats per step | units of $\lambda$ using natural logs |
| output feedback | the network's prediction re-entering as input (his "closed loop") |
| PCI | perturbational complexity index: compressibility of the response to a perturbation |
| plasticity | a learning rule changing weights during the run |
| pre-registration | fixing hypotheses, measures and analysis before collecting data |
| rate coding | information in how often a neuron fires |
| rate-matched null | per-neuron time shuffle: same rates, timing destroyed |
| reservoir computing | fixed random recurrent network plus a trained linear readout |
| ridge regression | least squares with a penalty $\beta \|w\|^{2}$ on weight size |
| Rosenstein method | $\lambda$ from one recorded series via delay embedding and nearest neighbours |
| Rössler system | another three-variable chaotic ODE |
| scrambled (arm) | feedback of matched strength with its content destroyed |
| SDL | Simulation and Data Lab (here: Neuroscience, at JSC) |
| self-model (joint experiment) | a module predicting the network's own regime and error, and setting its gain |
| spectral radius $\rho$ | largest eigenvalue magnitude of a weight matrix |
| spike coding | information in the precise timing of spikes |
| synaptic time constant $\tau_{\text{syn}}$ | how long one spike keeps acting on its target |
| TVB | The Virtual Brain, a whole-brain simulation platform |
| tangent method | $\lambda$ by pushing a difference vector through the exact Jacobian |
