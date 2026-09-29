---
title: "Prediction 5: Qualia Structure Is Shareable but Absolute Encoding Is Not"
section: Predictions and Empirical Evidence
article_number: 101
description: "The relational structure of a subject's qualia space is recoverable across individuals; the absolute state that realizes a given quale is not."
keywords: [qualia, qualia structure, representational similarity, optimal transport, cross-individual alignment, decoding, novel prediction, FMT]
---

# Prediction 5: Qualia Structure Is Shareable but Absolute Encoding Is Not

**The relational structure of a subject's qualia space is recoverable across individuals; the absolute state that realizes a given quale is not.**

## The Prediction

Unsupervised, label-free alignment of qualia-similarity structures within a single modality will generalize across individuals. Gromov–Wasserstein optimal transport over representational dissimilarity matrices (Kriegeskorte et al., 2008) will recover above-chance cross-individual correspondence without shared labels. On the same data, a decoder trained to read one brain's absolute realizing state ("their red") will fail to generalize to another's.

The committed claim is the **dissociation**: structure transfers, absolute encoding does not.

## Derivation

The prediction follows directly from the third principle, with no intervening consequence. Qualia are properties of the running self-simulation, constituted at the computational level ([Virtual Qualia](../hard-problem/virtual-qualia.md)). Their *structure* is the relational organization of the explicit models; their *absolute encoding* is the specific substrate realization.

A relational invariant is recoverable by any procedure that preserves the relations. The encoding is fixed by an idiosyncratic mapping from substrate to content, which only instantiation transfers and description does not. Structure should therefore align across brains, while absolute decoding should not.

## Proposed Test

Similarity judgments within one modality (colour, pitch) yield a representational dissimilarity matrix per person. Two analyses then run on identical data:

1. **Structural arm.** Unsupervised cross-individual alignment of the matrices, with no labels shared.
2. **Encoding arm.** A supervised decoder trained on one person's absolute states and tested on another's.

The structural arm has been shown at the group level for colour similarity (Kawakita et al., 2025), and extended to preschool children and toddlers (Watanabe et al., 2026). Both aligned pooled groups of observers rather than individuals. The individual-level structural arm, like the encoding arm, is still untested, and the novel content is the *paired* failure of absolute cross-individual decoding.

## Falsification Conditions

- If cross-individual absolute-state decoding generalizes as well as, or better than, unsupervised structural alignment, the asymmetry is wrong.
- If label-free structural alignment fails to exceed chance across individuals within a modality, the shareable-structure claim is wrong.

## Distinguishing Power

- **Strong-privacy views** predict no cross-individual structural alignment.
- **Standard functionalism** predicts that the encoding transfers along with the structure.
- **The Four-Model Theory** predicts both halves together: structure travels as a relational invariant, and encoding does not, because it is realized and not described.

Confirmation would explain why qualia resist report. It would not explain why there is feeling at all; that part of the theory is argued for and not derived.

## Key Takeaway

Two people can share the shape of their colour experience without sharing the state that realizes any one colour. The test pairs a structural alignment that should succeed with an absolute decoder that should fail, on the same data.

## See Also

- [Qualia](../basics/qualia.md)
- [Virtual Qualia](../hard-problem/virtual-qualia.md)
- [The Explanatory Gap](../hard-problem/explanatory-gap.md)
- [Empirical Convergence](confirmed.md)

*Based on: Gruber, M. (2026). The Four-Model Theory of Consciousness, Section 8.6. Zenodo. [10.5281/zenodo.18669891](https://doi.org/10.5281/zenodo.18669891)*
