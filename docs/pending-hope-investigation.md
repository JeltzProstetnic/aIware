<!-- Tracked-by: AIW-131 -->
Action: reference

# HOPE framework — investigate (function-not-weights NN analysis)

**Flagged by MG 2026-07-28 (S274):** "track investigating this before end … might be interesting for
CRU [crucible] especially." Primary owner = **crucible** (routed via cross-project inbox); aIware keeps
this note for the **FMT↔ICCR↔HOPE theory-convergence** angle.

## MG's summary (as received — TREAT AS UNVERIFIED social-paraphrase; verify vs primary source)

> Google DeepMind and UC Berkeley introduce **HOPE**, a framework that analyzes neural networks by what
> their neurons **do as functions**, not by how large their weights look. It moves compression into a
> **Hilbert space** where pruning, merging, and block removal can be scored mathematically **without
> training data**.
>
> Weight magnitude can mislead: **scale symmetries** can make big weights look important and small
> weights hide real features. HOPE reads the function instead, modeling each neuron as a **rank-1
> Hilbert-Schmidt operator** and using **Batch Norm statistics** to build a **maximum-entropy Gaussian
> surrogate** for exact functional energy estimates.
>
> In CIFAR→SVHN transfer, their **DEFT** algorithm reaches **89.79%** target accuracy while retaining
> **52.14%** on the source task, **65.82 H-Score**. Full fine-tuning reaches 94.09% target but collapses
> source retention to 7.52% — HOPE preserves a **Universal Core** while freeing **Plastic Slack** for new
> learning.

## Investigation steps (for whoever picks this up)
1. **Locate the primary source** — WebSearch "HOPE Hilbert-Schmidt operator neural network pruning DeepMind Berkeley DEFT H-Score". Pin the arXiv ID + authors + date. The summary above reads like a hype post — verify every number and claim against the paper before relying on it.
2. Extract the actual method: rank-1 Hilbert-Schmidt operator per neuron; BatchNorm → max-entropy Gaussian surrogate; the "functional energy" score; how pruning/merging/block-removal are scored data-free.
3. Assess **crucible relevance** (primary): could DEFT's Universal-Core / Plastic-Slack split inform the AC-implementation substrate (Design 15) — functional (not weight-magnitude) analysis of the minimal critical spiking net; a data-free way to identify the load-bearing functional core vs. plastic remainder?

## Why aIware cares (theory-convergence angle — secondary, but real)
"**Judge the network by its function, not the magnitude of its weights**" is the same move, one level down,
as **Kanai's ICCR** ("judge by *intrinsic* causal-computational organization, not the external
description/substrate", `drafts/kanai-iccr-vs-fmt-comparison-2026-07-28.md`) and **FMT** ("consciousness
tracks intrinsic realized *structure*, not the substrate"). HOPE's **scale-symmetry** point — big weights
can look important without being functionally load-bearing — rhymes with FMT/ICCR's rejection of
surface-equivalence (boundary-behavioral / weight-magnitude) in favour of intrinsic function under
intervention. Possible **Universal Core ↔ implicit/stable models, Plastic Slack ↔ explicit/plastic
models** mapping — speculative, worth one careful look. If it holds up, a citable methodological
convergence for a future note (or a Lane B footnote: a data-free functional-identification method in the
same spirit as the closure-at-criticality detector). **Do not overclaim before reading the paper.**
