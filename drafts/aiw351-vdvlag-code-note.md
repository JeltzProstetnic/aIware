---
title: "DFA and Lyapunov routines in TVB-Reservoir: a run-verified check"
author: "Matthias Gruber · 30 October 2026"
---

We ran the DFA and Lyapunov routines from github.com/DeLaVlag/TVB-Reservoir, commit `8606b72` (2025-11-06), on signals whose answers are known. The DFA routine, as the pipeline calls it, does not measure the DFA exponent. It returns about 0.59 whether the true exponent is 0.3, 0.5, 0.7 or 0.9, and its value changes with the units of the signal. Four separate defects cause this, and each one alone breaks the estimate. The Lyapunov core (Rosenstein) is correct. Its output is 10× too large because of a units factor, and in a driven system a positive value does not by itself show chaos.

## How the code was run

- `computeDFA_gpu` and `computeLYA_gpu` were imported from the repository and called unmodified.
- The CUDA C source was compiled unchanged with NVRTC through CuPy, behind a minimal pycuda stand-in. The only text change replaces the `<math.h>`/`<float.h>` includes with `#define FLT_MAX 3.402823466e+38F`. On a small random input the GPU kernel and an independent float32 numpy port agree to 8.9e-8.
- Inputs have the shape the pipeline passes, (sims, regions, time) float32: 16 × 68 × 625 for DFA and 250 steps for λ. The calls are `montbrio-pazo-roxin_reservoir.py:1274-1278`, identical in `larter-breakspear_reservoir.py:1177-1181`. The log comment at :1282 reads `# 16,68,625`.

## Summary

| | Where | Effect | Fix |
|---|---|---|---|
| A1 | `gpu_dfa.py:32, 48` | each region reads all 68 regions | index region-major |
| A2 | `gpu_dfa.py:80` | no profile (cumulative sum) | `cumsum` before the kernel |
| A3 | `gpu_dfa.py:52, 57` | F(n) summed over windows | mean, then `sqrt` |
| A4 | `gpu_dfa.py:59, 110` | median of log F / log n | slope of log F vs log n |
| B1 | `montbrio…py:1278` | λ ×10 (`dt` vs sample spacing) | divide by the sample spacing |
| B3 | `montbrio…py:1277` | driven window: noise reads λ > 0 | autonomous λ, or a null |

## Part A: DFA (`metrics/gpu_dfa.py`)

### A1. The kernel indexes time-major data; the array is region-major

Lines 32 and 48 read

```c
float y = data[(sim_idx * num_regions * num_steps)
               + (j * num_regions) + region_idx];
```

That is right for a (time, region) layout, but the pipeline passes (region, time). The thread for region 0 therefore reads element 68·j: it walks across all 68 regions and takes only 10 of its own 625 samples.

**Test.** White noise in every region, then only region 5 replaced by a random walk. Shipped: the α of all 68 regions changes. With the index fixed: only region 5 changes.

**Fix** (lines 32 and 48), or pass the array time-major:

```c
float y = data[(sim_idx * num_regions + region_idx)
               * num_steps + j];
```

### A2. No profile step

Standard DFA (Peng et al. 1994) first integrates the mean-removed series, y(t) = Σ(x − mean(x)), and detrends windows of y. The code detrends the raw signal; the paper's Eq. 3 also defines y(i) as the raw series. Without the profile the estimate shifts to about H − 1, and stationary signals collapse near 0.

| signal | expected α | all fixed | only A2 left in |
|---|---:|---:|---:|
| fGn H = 0.3 | 0.3 | 0.299 | 0.013 |
| fGn H = 0.7 | 0.7 | 0.687 | 0.059 |
| random walk | 1.5 | 1.454 | 0.492 |

**Fix** (host side, before line 80):

```python
data = np.cumsum(data - data.mean(axis=2, keepdims=True),
                 axis=2)
```

### A3. F(n) is the sum of the per-window RMS, not the mean

There are T/n windows, so summing multiplies F(n) by a factor proportional to 1/n and lowers the log–log slope by 1. With only this defect left in, every exponent drops by about 1.03: fGn 0.3 / 0.5 / 0.7 / 0.9 read −0.74 / −0.54 / −0.35 / −0.16. Negative values in a DFA figure have this signature.

**Fix** (lines 52 and 57), the standard F(n) = sqrt(mean of squared residuals):

```c
fluctuation += rms / window_size;                 // l.52
float log_fluctuation =
    logf(sqrtf(fluctuation / num_windows));       // l.57
```

### A4. α is the median over n of log F(n) / log n, not a regression slope

Line 59 stores `log_fluctuation / log_window_size`, and line 110 returns the median of that over window sizes. If F(n) = c·n^α, then log F / log n = α + log c / log n. The intercept term does not vanish, so the result depends on the amplitude of the signal and on the window range. The paper's p.6 describes a regression and calls the exponent amplitude-independent; the shipped code is neither.

| the same fGn H = 0.7, scaled by | shipped | all fixed |
|---|---:|---:|
| ×0.01 | −0.559 | 0.683 |
| ×1 | 0.590 | 0.683 |
| ×100 | 1.739 | 0.683 |

Across a parameter sweep the activity amplitude changes, so the reported α moves with amplitude even where the correlation structure does not. A range of −0.2 to 1.2, as in Fig. 2, fits this pattern.

**Fix** (line 59 stores `log_fluctuation`; then on the host):

```python
logn = np.log(window_sizes)
alpha = np.polyfit(logn, logF.reshape(-1, len(logn)).T, 1)[0]
```

### All four together

T = 625, 16 × 68 series, mean ± sd. The reference is an independently validated DFA run on the same window sizes (10 log-spaced, 10 … T/2).

| signal | expected | shipped | all four fixed |
|---|---:|---:|---:|
| fGn H = 0.3 | 0.3 | 0.590 ± 0.007 | 0.302 ± 0.042 |
| fGn H = 0.5 | 0.5 | 0.590 ± 0.008 | 0.490 ± 0.058 |
| fGn H = 0.7 | 0.7 | 0.590 ± 0.007 | 0.680 ± 0.071 |
| fGn H = 0.9 | 0.9 | 0.582 ± 0.009 | 0.877 ± 0.079 |
| white noise | 0.5 | 0.590 ± 0.008 | 0.492 ± 0.059 |
| random walk | 1.5 | 1.272 ± 0.022 | 1.451 ± 0.106 |

More data does not help: at T = 10,000 the shipped routine reads 0.68–0.71 for every fGn and for white noise, while the fixed one reads 0.300 / 0.499 / 0.690 / 0.889. The shipped spread (sd ≈ 0.008) is far smaller than the honest spread at T = 625 (sd 0.04–0.08): the value is precise, but it carries no information about correlation.

## Part B: Lyapunov exponent (`metrics/gpu_lya.py`)

### B0. The core algorithm is correct

On the Lorenz x-series (4,000 samples, spacing 0.05, your settings: embedding 4, lag 5, Theiler window 10, 50-step fit) it returns 0.955 ± 0.038 against the true 0.906, the usual small upward bias of Rosenstein with a fixed fit range. On a noise-free stable oscillator with exact λ = −0.314 it returns −0.3143.

### B1. `tau = self.dt` while the samples are 0.1 apart: λ is 10× too large

The slope is per sample. The recorded samples are 10-step averages (`tavg_period = .1`, :87), but the call divides by `dt = 0.01` (:1278, :189). Every reported λ is exactly 10× the exponent per model time unit: on Lorenz, 0.955 becomes 9.550. Sign and ordering are unchanged, so the location of λ = 0 is not affected; the axis values are.

**Fix:** pass `tau=self.tavg_period`, which equals `self.dt * self.n_inner_steps`.

### B2. 250 samples make the estimate sensitive to the sampling

Lorenz, correct `tau`, 24 trajectories, true value 0.906:

| spacing | n = 250 (your window) | n = 4000 |
|---|---:|---:|
| 0.01 | 2.310 ± 1.010 | 2.720 ± 0.224 |
| 0.05 | 0.901 ± 0.134 | 0.955 ± 0.038 |
| 0.1 | 0.382 ± 0.071 | 0.708 ± 0.019 |

Whether this biases your runs depends on the reservoir's own time scale, which we did not simulate. At 250 samples the per-run spread is 15–45 % of the value. Longer windows, and fitting only the initial linear part of the divergence curve (Rosenstein et al. 1993), reduce it.

### B3. In a driven system a positive λ does not show chaos

λ is measured in the prediction window (:1277), where the network is driven by its own fed-back output and by noise. Noise separates nearby states whatever the stability of the flow.

| same stable oscillator (λ = −0.314), spacing | noise-free | noise-driven |
|---|---:|---:|
| 0.05 | −0.314 ± 0.000 | +0.315 ± 0.124 |
| 0.1 | −0.229 ± 0.011 | +0.070 ± 0.049 |

White noise with no dynamics at all reads +0.005 per sample, which is +0.53 after the division by 0.01: inside the 0.2–0.5 range the paper reports on p.8. Two ways to measure the exponent of the flow itself: run two copies with identical input and feedback and measure how fast they separate, or propagate a tangent vector through the model's Jacobian. Alternatively, report the driven exponent as a driven ("conditional") one.

## What this may change in the chapter

- The DFA panels of Figs 2 and 3, and the DFA = 0.5 masks in Fig. 4B and 4D.
- The p.8 statement that the system "remains in a chaotic regime (λ > 0)", and the absolute λ values in Figs 2 and 3.
- We cannot tell whether this commit produced the published figures: it post-dates the submission, although the README names it as the paper's code. PCI and the task MSE were not checked.

## Reproduction

The stand-in runtime and two scripts (`verify.py`, `isolate.py`) run in a few minutes on one GPU and reproduce every number above. We are glad to send them.
