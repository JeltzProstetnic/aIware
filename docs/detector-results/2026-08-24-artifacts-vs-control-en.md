# Detector exposure — artifacts

**What this is.** Per-chunk detector scores for one corpus, and the flag rate those scores
produce at a stated threshold, shown next to the flag rate the same threshold produces on
the author's known-human control corpus. That control rate is a *personal* false-positive
rate: the paper-independent prior that this author's style trips this detector.

**What this is not.** Not a verdict, and not a percentage of machine authorship. A
Binoculars score is a ratio of two cross-entropies; it is not calibrated to any probability,
and absolute values are not comparable across detectors. Vendor "percent" figures are
thresholded scores mapped through the vendor's own calibration corpus (research doc §7).

**The stronger evidence is not here.** Research doc §4: the remedy NeurIPS actually accepted
was documented version history. This repository's git log is that artifact and is worth more
than any score below, because it is evidence about process rather than a number about prose.


### Run

| field | value |
|---|---|
| detector | binoculars |
| direction | lower_is_machine |
| observer | tiiuae/falcon-7b |
| performer | tiiuae/falcon-7b-instruct |
| chunks scored | 997 |
| sources | 94 |
| generated | 2026-08-24T11:32:34+00:00 |
| window | 320 |
| unit | words |
| corpus_files | 98 |

### Chunk score distribution — this artifact

n = 997 chunks

| min | p05 | q1 | median | q3 | p95 | max | mean | sd |
|---|---|---|---|---|---|---|---|---|
| 0.8708 | 0.9428 | 0.9907 | 1.0200 | 1.0448 | 1.0773 | 1.1416 | 1.0162 | 0.0411 |

### Control corpus (en, 319 chunks)

n = 319 chunks

| min | p05 | q1 | median | q3 | p95 | max | mean | sd |
|---|---|---|---|---|---|---|---|---|
| 0.8872 | 0.9320 | 0.9636 | 0.9837 | 1.0059 | 1.0321 | 1.0802 | 0.9836 | 0.0313 |

### Flag rates

| Threshold | where it comes from | control chunks flagged | artifact chunks flagged |
|---|---|---|---|
| 0.8536 | Binoculars published low-FPR threshold | 0.0% | 0.0% |
| 0.9015 | Binoculars published accuracy threshold | 0.6% | 0.6% |
| 0.9307 | this control corpus at a 5% flag rate | 4.7% | 2.9% |
| 0.9113 | this control corpus at a 1% flag rate | 0.9% | 1.1% |

Read each row as: at this threshold, k% of the author's known-human control chunks are flagged and j% of this artifact's chunks are flagged. The left-hand column is a property of the author's style; the right-hand column is a property of this text.

### Position relative to the control

- The artifact median (1.0200) sits at the 88th percentile of the control distribution.
- 34 of 997 artifact chunks fall past the control 5th percentile (0.9320).

### Per-chunk scores

| # | source | units | score | past control p05 |
|---|---|---|---|---|
| 0 | /home/jeltz/aIware/drafts/aiw-el-interior-fable-review.md | 320 | 1.0059 | no |
| 1 | /home/jeltz/aIware/drafts/aiw-el-interior-fable-review.md | 320 | 1.0409 | no |
| 2 | /home/jeltz/aIware/drafts/aiw-ko-interior-fable-review.md | 269 | 1.0914 | no |
| 3 | /home/jeltz/aIware/drafts/aiw-nl-interior-fable-review.md | 320 | 1.0740 | no |
| 4 | /home/jeltz/aIware/drafts/aiw-nl-interior-fable-review.md | 320 | 1.0288 | no |
| 5 | /home/jeltz/aIware/drafts/aiw-nl-interior-fable-review.md | 320 | 1.0350 | no |
| 6 | /home/jeltz/aIware/drafts/aiw-nl-interior-fable-review.md | 320 | 1.0560 | no |
| 7 | /home/jeltz/aIware/drafts/aiw-nl-interior-fable-review.md | 320 | 1.0369 | no |
| 8 | /home/jeltz/aIware/drafts/aiw-operationalization-review.md | 320 | 1.0744 | no |
| 9 | /home/jeltz/aIware/drafts/aiw-operationalization-review.md | 320 | 1.0017 | no |
| 10 | /home/jeltz/aIware/drafts/aiw-operationalization-review.md | 320 | 1.0247 | no |
| 11 | /home/jeltz/aIware/drafts/aiw-operationalization-review.md | 320 | 1.0467 | no |
| 12 | /home/jeltz/aIware/drafts/aiw-operationalization-review.md | 320 | 1.0170 | no |
| 13 | /home/jeltz/aIware/drafts/aiw-operationalization-review.md | 320 | 1.0460 | no |
| 14 | /home/jeltz/aIware/drafts/aiw-operationalization-review.md | 320 | 1.0884 | no |
| 15 | /home/jeltz/aIware/drafts/aiw-operationalization-review.md | 320 | 1.0697 | no |
| 16 | /home/jeltz/aIware/drafts/aiw-operationalization-review.md | 320 | 1.0632 | no |
| 17 | /home/jeltz/aIware/drafts/aiw-operationalization-review.md | 320 | 1.0520 | no |
| 18 | /home/jeltz/aIware/drafts/aiw-operationalization-review.md | 320 | 1.0941 | no |
| 19 | /home/jeltz/aIware/drafts/aiw-operationalization-review.md | 320 | 1.0800 | no |
| 20 | /home/jeltz/aIware/drafts/aiw-operationalization-review.md | 320 | 1.0252 | no |
| 21 | /home/jeltz/aIware/drafts/aiw105-qualia-privacy-paper-draft.md | 320 | 1.0638 | no |
| 22 | /home/jeltz/aIware/drafts/aiw105-qualia-privacy-paper-draft.md | 320 | 1.0737 | no |
| 23 | /home/jeltz/aIware/drafts/aiw105-qualia-privacy-paper-draft.md | 320 | 1.0376 | no |
| 24 | /home/jeltz/aIware/drafts/aiw105-qualia-privacy-paper-draft.md | 320 | 1.0149 | no |
| 25 | /home/jeltz/aIware/drafts/aiw105-qualia-privacy-paper-draft.md | 320 | 0.9896 | no |
| 26 | /home/jeltz/aIware/drafts/aiw105-qualia-privacy-paper-draft.md | 320 | 1.0676 | no |
| 27 | /home/jeltz/aIware/drafts/aiw105-qualia-privacy-paper-draft.md | 320 | 1.0700 | no |
| 28 | /home/jeltz/aIware/drafts/aiw105-qualia-privacy-paper-draft.md | 320 | 1.1416 | no |
| 29 | /home/jeltz/aIware/drafts/aiw105-qualia-privacy-paper-draft.md | 320 | 1.0535 | no |
| 30 | /home/jeltz/aIware/drafts/aiw105-qualia-privacy-paper-draft.md | 320 | 1.0005 | no |
| 31 | /home/jeltz/aIware/drafts/aiw105-qualia-privacy-paper-draft.md | 320 | 1.0224 | no |
| 32 | /home/jeltz/aIware/drafts/aiw105-qualia-privacy-paper-draft.md | 320 | 1.0517 | no |
| 33 | /home/jeltz/aIware/drafts/aiw107-kalk-scan-findings.md | 320 | 1.0510 | no |
| 34 | /home/jeltz/aIware/drafts/aiw107-kalk-scan-findings.md | 320 | 1.0010 | no |
| 35 | /home/jeltz/aIware/drafts/aiw107-kalk-scan-findings.md | 320 | 1.0231 | no |
| 36 | /home/jeltz/aIware/drafts/aiw107-kalk-scan-findings.md | 320 | 1.0561 | no |
| 37 | /home/jeltz/aIware/drafts/aiw107-kalk-scan-findings.md | 299 | 1.0551 | no |
| 38 | /home/jeltz/aIware/drafts/aiw108-cross-edition-qa-findings.md | 320 | 1.0263 | no |
| 39 | /home/jeltz/aIware/drafts/aiw108-cross-edition-qa-findings.md | 320 | 1.0455 | no |
| 40 | /home/jeltz/aIware/drafts/aiw108-cross-edition-qa-findings.md | 320 | 1.0752 | no |
| 41 | /home/jeltz/aIware/drafts/aiw108-cross-edition-qa-findings.md | 320 | 1.0850 | no |
| 42 | /home/jeltz/aIware/drafts/aiw108-de-fable-final-review.md | 320 | 1.0107 | no |
| 43 | /home/jeltz/aIware/drafts/aiw108-de-fable-final-review.md | 320 | 1.0521 | no |
| 44 | /home/jeltz/aIware/drafts/aiw108-en-fable-final-review.md | 311 | 1.0183 | no |
| 45 | /home/jeltz/aIware/drafts/aiw108-es-kalk-findings.md | 320 | 1.0354 | no |
| 46 | /home/jeltz/aIware/drafts/aiw108-es-kalk-findings.md | 320 | 0.9715 | no |
| 47 | /home/jeltz/aIware/drafts/aiw108-es-kalk-findings.md | 320 | 1.0097 | no |
| 48 | /home/jeltz/aIware/drafts/aiw108-es-kalk-findings.md | 320 | 1.0099 | no |
| 49 | /home/jeltz/aIware/drafts/aiw108-es-kalk-findings.md | 320 | 1.0238 | no |
| 50 | /home/jeltz/aIware/drafts/aiw108-es-kalk-findings.md | 320 | 0.9481 | no |
| 51 | /home/jeltz/aIware/drafts/aiw108-es-kalk-findings.md | 320 | 1.0048 | no |
| 52 | /home/jeltz/aIware/drafts/aiw108-es-kalk-findings.md | 320 | 1.0377 | no |
| 53 | /home/jeltz/aIware/drafts/aiw108-es-kalk-findings.md | 320 | 1.0114 | no |
| 54 | /home/jeltz/aIware/drafts/aiw108-es-kalk-findings.md | 320 | 1.0342 | no |
| 55 | /home/jeltz/aIware/drafts/aiw108-es-kalk-findings.md | 320 | 0.9854 | no |
| 56 | /home/jeltz/aIware/drafts/aiw108-es-kalk-findings.md | 300 | 1.0234 | no |
| 57 | /home/jeltz/aIware/drafts/aiw108-fr-coherence-findings.md | 320 | 1.0130 | no |
| 58 | /home/jeltz/aIware/drafts/aiw108-fr-coherence-findings.md | 320 | 0.9899 | no |
| 59 | /home/jeltz/aIware/drafts/aiw108-fr-coherence-findings.md | 320 | 0.9875 | no |
| 60 | /home/jeltz/aIware/drafts/aiw108-fr-coherence-findings.md | 320 | 0.9987 | no |
| 61 | /home/jeltz/aIware/drafts/aiw108-fr-coherence-findings.md | 320 | 1.0062 | no |
| 62 | /home/jeltz/aIware/drafts/aiw108-fr-coherence-findings.md | 320 | 1.0010 | no |
| 63 | /home/jeltz/aIware/drafts/aiw108-fr-coherence-findings.md | 320 | 1.0228 | no |
| 64 | /home/jeltz/aIware/drafts/aiw108-fr-coherence-findings.md | 264 | 1.0205 | no |
| 65 | /home/jeltz/aIware/drafts/aiw108-fr-kalk-findings.md | 320 | 1.0448 | no |
| 66 | /home/jeltz/aIware/drafts/aiw108-fr-kalk-findings.md | 320 | 1.0190 | no |
| 67 | /home/jeltz/aIware/drafts/aiw108-fr-kalk-findings.md | 320 | 1.0582 | no |
| 68 | /home/jeltz/aIware/drafts/aiw108-fr-kalk-findings.md | 320 | 1.0490 | no |
| 69 | /home/jeltz/aIware/drafts/aiw108-it-kalk-findings.md | 320 | 1.0169 | no |
| 70 | /home/jeltz/aIware/drafts/aiw108-it-kalk-findings.md | 320 | 0.9496 | no |
| 71 | /home/jeltz/aIware/drafts/aiw108-it-kalk-findings.md | 320 | 0.9020 | yes |
| 72 | /home/jeltz/aIware/drafts/aiw108-it-kalk-findings.md | 320 | 0.9503 | no |
| 73 | /home/jeltz/aIware/drafts/aiw108-it-kalk-findings.md | 320 | 0.9226 | yes |
| 74 | /home/jeltz/aIware/drafts/aiw108-it-kalk-findings.md | 320 | 0.8996 | yes |
| 75 | /home/jeltz/aIware/drafts/aiw108-it-kalk-findings.md | 320 | 0.9281 | yes |
| 76 | /home/jeltz/aIware/drafts/aiw108-it-kalk-findings.md | 320 | 0.9663 | no |
| 77 | /home/jeltz/aIware/drafts/aiw108-it-kalk-findings.md | 320 | 1.0269 | no |
| 78 | /home/jeltz/aIware/drafts/aiw108-ja-kalk-findings.md | 320 | 1.0444 | no |
| 79 | /home/jeltz/aIware/drafts/aiw108-ja-kalk-findings.md | 320 | 1.0118 | no |
| 80 | /home/jeltz/aIware/drafts/aiw108-ja-kalk-findings.md | 320 | 1.0314 | no |
| 81 | /home/jeltz/aIware/drafts/aiw108-ja-kalk-findings.md | 320 | 0.9907 | no |
| 82 | /home/jeltz/aIware/drafts/aiw108-ja-kalk-findings.md | 320 | 0.9658 | no |
| 83 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0266 | no |
| 84 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0130 | no |
| 85 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0758 | no |
| 86 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0860 | no |
| 87 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.1008 | no |
| 88 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0327 | no |
| 89 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0467 | no |
| 90 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0680 | no |
| 91 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 0.9877 | no |
| 92 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0078 | no |
| 93 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0367 | no |
| 94 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0119 | no |
| 95 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0454 | no |
| 96 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0186 | no |
| 97 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0115 | no |
| 98 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0993 | no |
| 99 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0009 | no |
| 100 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 0.9976 | no |
| 101 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0273 | no |
| 102 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0561 | no |
| 103 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0573 | no |
| 104 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0408 | no |
| 105 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0088 | no |
| 106 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0744 | no |
| 107 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0273 | no |
| 108 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 0.9941 | no |
| 109 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0604 | no |
| 110 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0156 | no |
| 111 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 1.0248 | no |
| 112 | /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md | 320 | 0.9929 | no |
| 113 | /home/jeltz/aIware/drafts/aiw108-pt-kalk-findings.md | 320 | 1.0278 | no |
| 114 | /home/jeltz/aIware/drafts/aiw108-pt-kalk-findings.md | 320 | 0.9979 | no |
| 115 | /home/jeltz/aIware/drafts/aiw108-pt-kalk-findings.md | 320 | 0.9646 | no |
| 116 | /home/jeltz/aIware/drafts/aiw108-pt-kalk-findings.md | 320 | 0.9802 | no |
| 117 | /home/jeltz/aIware/drafts/aiw108-pt-kalk-findings.md | 320 | 1.0594 | no |
| 118 | /home/jeltz/aIware/drafts/aiw108-zh-kalk-findings.md | 320 | 1.0499 | no |
| 119 | /home/jeltz/aIware/drafts/aiw109-combined-cross-language-findings-S259.md | 320 | 1.0151 | no |
| 120 | /home/jeltz/aIware/drafts/aiw109-combined-cross-language-findings-S259.md | 320 | 1.0800 | no |
| 121 | /home/jeltz/aIware/drafts/aiw109-combined-cross-language-findings-S259.md | 320 | 1.0241 | no |
| 122 | /home/jeltz/aIware/drafts/aiw109-combined-cross-language-findings-S259.md | 320 | 1.1010 | no |
| 123 | /home/jeltz/aIware/drafts/aiw109-combined-cross-language-findings-S259.md | 320 | 1.1046 | no |
| 124 | /home/jeltz/aIware/drafts/aiw109-es-interior-fable-review-S259.md | 320 | 1.0545 | no |
| 125 | /home/jeltz/aIware/drafts/aiw109-es-interior-fable-review-S259.md | 320 | 1.0606 | no |
| 126 | /home/jeltz/aIware/drafts/aiw109-es-interior-fable-review-S259.md | 320 | 1.0285 | no |
| 127 | /home/jeltz/aIware/drafts/aiw109-es-interior-fable-review-S259.md | 320 | 1.0280 | no |
| 128 | /home/jeltz/aIware/drafts/aiw109-final-review-S264.md | 320 | 1.0409 | no |
| 129 | /home/jeltz/aIware/drafts/aiw109-final-review-S264.md | 320 | 1.0735 | no |
| 130 | /home/jeltz/aIware/drafts/aiw109-final-review-S264.md | 320 | 1.0362 | no |
| 131 | /home/jeltz/aIware/drafts/aiw109-final-review-S264.md | 320 | 1.0675 | no |
| 132 | /home/jeltz/aIware/drafts/aiw109-fix-spec.md | 320 | 1.0544 | no |
| 133 | /home/jeltz/aIware/drafts/aiw109-fix-spec.md | 320 | 1.1042 | no |
| 134 | /home/jeltz/aIware/drafts/aiw109-fix-spec.md | 320 | 1.0552 | no |
| 135 | /home/jeltz/aIware/drafts/aiw109-fix-spec.md | 320 | 1.0755 | no |
| 136 | /home/jeltz/aIware/drafts/aiw109-fr-interior-fable-review-S259.md | 320 | 1.0567 | no |
| 137 | /home/jeltz/aIware/drafts/aiw109-fr-interior-fable-review-S259.md | 320 | 1.0114 | no |
| 138 | /home/jeltz/aIware/drafts/aiw109-fr-interior-fable-review-S259.md | 320 | 1.0655 | no |
| 139 | /home/jeltz/aIware/drafts/aiw109-fr-interior-fable-review-S259.md | 320 | 1.0254 | no |
| 140 | /home/jeltz/aIware/drafts/aiw109-fr-interior-fable-review-S259.md | 259 | 1.0596 | no |
| 141 | /home/jeltz/aIware/drafts/aiw109-it-interior-fable-review-S259.md | 320 | 1.0833 | no |
| 142 | /home/jeltz/aIware/drafts/aiw109-it-interior-fable-review-S259.md | 320 | 1.0701 | no |
| 143 | /home/jeltz/aIware/drafts/aiw109-it-interior-fable-review-S259.md | 320 | 1.0011 | no |
| 144 | /home/jeltz/aIware/drafts/aiw109-it-interior-fable-review-S259.md | 320 | 1.0514 | no |
| 145 | /home/jeltz/aIware/drafts/aiw109-it-interior-fable-review-S259.md | 320 | 1.0553 | no |
| 146 | /home/jeltz/aIware/drafts/aiw109-it-interior-fable-review-S259.md | 266 | 1.0283 | no |
| 147 | /home/jeltz/aIware/drafts/aiw109-ja-interior-fable-review-S259.md | 320 | 1.0742 | no |
| 148 | /home/jeltz/aIware/drafts/aiw109-ja-interior-fable-review-S259.md | 320 | 1.0113 | no |
| 149 | /home/jeltz/aIware/drafts/aiw109-pt-interior-fable-review-S259.md | 320 | 1.0224 | no |
| 150 | /home/jeltz/aIware/drafts/aiw109-pt-interior-fable-review-S259.md | 320 | 1.0762 | no |
| 151 | /home/jeltz/aIware/drafts/aiw109-pt-interior-fable-review-S259.md | 320 | 1.1145 | no |
| 152 | /home/jeltz/aIware/drafts/aiw109-pt-interior-fable-review-S259.md | 320 | 1.0773 | no |
| 153 | /home/jeltz/aIware/drafts/aiw109-pt-interior-fable-review-S259.md | 320 | 1.0275 | no |
| 154 | /home/jeltz/aIware/drafts/aiw109-zh-interior-fable-review-S259.md | 320 | 1.0846 | no |
| 155 | /home/jeltz/aIware/drafts/aiw109-zh-interior-fable-review-S259.md | 320 | 1.0614 | no |
| 156 | /home/jeltz/aIware/drafts/aiw109-zh-interior-fable-review-S259.md | 320 | 1.0632 | no |
| 157 | /home/jeltz/aIware/drafts/aiw119-iwmt-fmt-convergence-note.md | 320 | 1.0715 | no |
| 158 | /home/jeltz/aIware/drafts/aiw119-iwmt-fmt-convergence-note.md | 320 | 1.0221 | no |
| 159 | /home/jeltz/aIware/drafts/aiw119-iwmt-fmt-convergence-note.md | 320 | 1.0483 | no |
| 160 | /home/jeltz/aIware/drafts/aiw119-iwmt-fmt-convergence-note.md | 320 | 1.0493 | no |
| 161 | /home/jeltz/aIware/drafts/aiw119-iwmt-fmt-convergence-note.md | 320 | 1.0410 | no |
| 162 | /home/jeltz/aIware/drafts/aiw119-iwmt-fmt-convergence-note.md | 320 | 1.0355 | no |
| 163 | /home/jeltz/aIware/drafts/aiw119-iwmt-fmt-convergence-note.md | 320 | 1.0655 | no |
| 164 | /home/jeltz/aIware/drafts/aiw119-iwmt-fmt-convergence-note.md | 320 | 1.0189 | no |
| 165 | /home/jeltz/aIware/drafts/aiw119-iwmt-fmt-convergence-note.md | 318 | 1.0410 | no |
| 166 | /home/jeltz/aIware/drafts/aiw120-olinyk-crc-fmt-convergence.md | 320 | 1.0266 | no |
| 167 | /home/jeltz/aIware/drafts/aiw120-olinyk-crc-fmt-convergence.md | 320 | 0.9947 | no |
| 168 | /home/jeltz/aIware/drafts/aiw120-olinyk-crc-fmt-convergence.md | 320 | 1.0563 | no |
| 169 | /home/jeltz/aIware/drafts/aiw120-olinyk-crc-fmt-convergence.md | 320 | 1.0607 | no |
| 170 | /home/jeltz/aIware/drafts/aiw120-olinyk-crc-fmt-convergence.md | 320 | 1.0468 | no |
| 171 | /home/jeltz/aIware/drafts/aiw120-olinyk-crc-fmt-convergence.md | 320 | 1.0227 | no |
| 172 | /home/jeltz/aIware/drafts/aiw130-PROPOSE.md | 320 | 1.0248 | no |
| 173 | /home/jeltz/aIware/drafts/aiw130-PROPOSE.md | 320 | 1.0708 | no |
| 174 | /home/jeltz/aIware/drafts/aiw130-PROPOSE.md | 320 | 1.0445 | no |
| 175 | /home/jeltz/aIware/drafts/aiw130-PROPOSE.md | 320 | 1.0841 | no |
| 176 | /home/jeltz/aIware/drafts/aiw130-jaic-cover-letter.md | 320 | 1.0513 | no |
| 177 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0428 | no |
| 178 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0261 | no |
| 179 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0094 | no |
| 180 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0752 | no |
| 181 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0613 | no |
| 182 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0149 | no |
| 183 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 0.9787 | no |
| 184 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 0.9970 | no |
| 185 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0281 | no |
| 186 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0321 | no |
| 187 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0815 | no |
| 188 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0437 | no |
| 189 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0512 | no |
| 190 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0612 | no |
| 191 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0552 | no |
| 192 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0062 | no |
| 193 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0135 | no |
| 194 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0339 | no |
| 195 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0533 | no |
| 196 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0184 | no |
| 197 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0302 | no |
| 198 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0731 | no |
| 199 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0478 | no |
| 200 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 0.9989 | no |
| 201 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0758 | no |
| 202 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0594 | no |
| 203 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0345 | no |
| 204 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0117 | no |
| 205 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0568 | no |
| 206 | /home/jeltz/aIware/drafts/aiw130-jaic-draft.md | 320 | 1.0245 | no |
| 207 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0360 | no |
| 208 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0821 | no |
| 209 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0647 | no |
| 210 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0142 | no |
| 211 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0444 | no |
| 212 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 0.9918 | no |
| 213 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0118 | no |
| 214 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0093 | no |
| 215 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0400 | no |
| 216 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0208 | no |
| 217 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0531 | no |
| 218 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0424 | no |
| 219 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0655 | no |
| 220 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0371 | no |
| 221 | /home/jeltz/aIware/drafts/aiw130-jaic-plan.md | 320 | 1.0244 | no |
| 222 | /home/jeltz/aIware/drafts/aiw130-noc-cover-letter.md | 320 | 1.0070 | no |
| 223 | /home/jeltz/aIware/drafts/aiw130-noc-cover-letter.md | 320 | 1.0219 | no |
| 224 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0619 | no |
| 225 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0086 | no |
| 226 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0942 | no |
| 227 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 0.9855 | no |
| 228 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0079 | no |
| 229 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0435 | no |
| 230 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0918 | no |
| 231 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 0.9825 | no |
| 232 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0281 | no |
| 233 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0395 | no |
| 234 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0466 | no |
| 235 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0721 | no |
| 236 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0624 | no |
| 237 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0148 | no |
| 238 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0269 | no |
| 239 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 0.9910 | no |
| 240 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0216 | no |
| 241 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0378 | no |
| 242 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0071 | no |
| 243 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0590 | no |
| 244 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0624 | no |
| 245 | /home/jeltz/aIware/drafts/aiw130-noc-draft.md | 320 | 1.0155 | no |
| 246 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0749 | no |
| 247 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0737 | no |
| 248 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0310 | no |
| 249 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0558 | no |
| 250 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0545 | no |
| 251 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0445 | no |
| 252 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0571 | no |
| 253 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0930 | no |
| 254 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0653 | no |
| 255 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0887 | no |
| 256 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0259 | no |
| 257 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0585 | no |
| 258 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0765 | no |
| 259 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0112 | no |
| 260 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0508 | no |
| 261 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0951 | no |
| 262 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0287 | no |
| 263 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0593 | no |
| 264 | /home/jeltz/aIware/drafts/aiw130-noc-plan.md | 320 | 1.0226 | no |
| 265 | /home/jeltz/aIware/drafts/aiw130-verified-citations.md | 320 | 1.0376 | no |
| 266 | /home/jeltz/aIware/drafts/aiw130-verified-citations.md | 320 | 1.0111 | no |
| 267 | /home/jeltz/aIware/drafts/aiw130-verified-citations.md | 320 | 1.0134 | no |
| 268 | /home/jeltz/aIware/drafts/aiw130-verified-citations.md | 320 | 1.0202 | no |
| 269 | /home/jeltz/aIware/drafts/aiw130-verified-citations.md | 302 | 1.0079 | no |
| 270 | /home/jeltz/aIware/drafts/aiw138-abstract-variants.md | 320 | 1.0437 | no |
| 271 | /home/jeltz/aIware/drafts/aiw138-abstract-variants.md | 320 | 1.0390 | no |
| 272 | /home/jeltz/aIware/drafts/aiw138-abstract-variants.md | 320 | 1.0725 | no |
| 273 | /home/jeltz/aIware/drafts/aiw166-cosmos-transfer.md | 320 | 1.0749 | no |
| 274 | /home/jeltz/aIware/drafts/aiw166-cosmos-transfer.md | 320 | 1.0776 | no |
| 275 | /home/jeltz/aIware/drafts/aiw166-cosmos-transfer.md | 320 | 1.0001 | no |
| 276 | /home/jeltz/aIware/drafts/aiw166-cosmos-transfer.md | 320 | 1.0481 | no |
| 277 | /home/jeltz/aIware/drafts/aiw166-cosmos-transfer.md | 320 | 1.0457 | no |
| 278 | /home/jeltz/aIware/drafts/aiw166-cosmos-transfer.md | 320 | 1.0363 | no |
| 279 | /home/jeltz/aIware/drafts/aiw166-cosmos-transfer.md | 320 | 1.0175 | no |
| 280 | /home/jeltz/aIware/drafts/aiw166-cosmos-transfer.md | 320 | 0.9886 | no |
| 281 | /home/jeltz/aIware/drafts/aiw166-cosmos-transfer.md | 320 | 1.0508 | no |
| 282 | /home/jeltz/aIware/drafts/aiw166-cosmos-transfer.md | 320 | 1.0036 | no |
| 283 | /home/jeltz/aIware/drafts/aiw166-cosmos-transfer.md | 295 | 1.0339 | no |
| 284 | /home/jeltz/aIware/drafts/aiw174-entanglement-wedge-postulate.md | 320 | 1.0287 | no |
| 285 | /home/jeltz/aIware/drafts/aiw174-entanglement-wedge-postulate.md | 320 | 1.0058 | no |
| 286 | /home/jeltz/aIware/drafts/aiw174-entanglement-wedge-postulate.md | 320 | 1.0084 | no |
| 287 | /home/jeltz/aIware/drafts/aiw174-entanglement-wedge-postulate.md | 320 | 1.0630 | no |
| 288 | /home/jeltz/aIware/drafts/aiw174-entanglement-wedge-postulate.md | 320 | 1.0198 | no |
| 289 | /home/jeltz/aIware/drafts/aiw174-entanglement-wedge-postulate.md | 320 | 1.0514 | no |
| 290 | /home/jeltz/aIware/drafts/aiw174-entanglement-wedge-postulate.md | 320 | 1.0218 | no |
| 291 | /home/jeltz/aIware/drafts/aiw174-entanglement-wedge-postulate.md | 320 | 1.0701 | no |
| 292 | /home/jeltz/aIware/drafts/aiw174-entanglement-wedge-postulate.md | 286 | 1.0164 | no |
| 293 | /home/jeltz/aIware/drafts/aiw174-tsirelson-from-capacity.md | 320 | 1.0456 | no |
| 294 | /home/jeltz/aIware/drafts/aiw174-tsirelson-from-capacity.md | 320 | 1.0230 | no |
| 295 | /home/jeltz/aIware/drafts/aiw174-tsirelson-from-capacity.md | 320 | 1.0450 | no |
| 296 | /home/jeltz/aIware/drafts/aiw174-tsirelson-from-capacity.md | 320 | 1.0320 | no |
| 297 | /home/jeltz/aIware/drafts/aiw174-tsirelson-from-capacity.md | 320 | 1.0012 | no |
| 298 | /home/jeltz/aIware/drafts/aiw174-tsirelson-from-capacity.md | 320 | 1.0577 | no |
| 299 | /home/jeltz/aIware/drafts/aiw186-vacuity-regime.md | 320 | 1.0237 | no |
| 300 | /home/jeltz/aIware/drafts/aiw186-vacuity-regime.md | 320 | 1.0390 | no |
| 301 | /home/jeltz/aIware/drafts/aiw186-vacuity-regime.md | 320 | 1.0426 | no |
| 302 | /home/jeltz/aIware/drafts/aiw186-vacuity-regime.md | 320 | 0.9942 | no |
| 303 | /home/jeltz/aIware/drafts/aiw186-vacuity-regime.md | 320 | 1.0431 | no |
| 304 | /home/jeltz/aIware/drafts/aiw186-vacuity-regime.md | 320 | 1.0321 | no |
| 305 | /home/jeltz/aIware/drafts/aiw186-vacuity-regime.md | 320 | 1.0227 | no |
| 306 | /home/jeltz/aIware/drafts/aiw186-vacuity-regime.md | 320 | 1.0067 | no |
| 307 | /home/jeltz/aIware/drafts/aiw186-vacuity-regime.md | 320 | 1.0236 | no |
| 308 | /home/jeltz/aIware/drafts/aiw186-vacuity-regime.md | 320 | 0.9954 | no |
| 309 | /home/jeltz/aIware/drafts/aiw186-vacuity-regime.md | 270 | 1.0340 | no |
| 310 | /home/jeltz/aIware/drafts/aiw187-allocation.md | 320 | 1.0279 | no |
| 311 | /home/jeltz/aIware/drafts/aiw187-allocation.md | 320 | 1.0257 | no |
| 312 | /home/jeltz/aIware/drafts/aiw187-allocation.md | 320 | 1.0780 | no |
| 313 | /home/jeltz/aIware/drafts/aiw192-dream-database-reanalysis.md | 320 | 1.0251 | no |
| 314 | /home/jeltz/aIware/drafts/aiw192-dream-database-reanalysis.md | 320 | 1.0800 | no |
| 315 | /home/jeltz/aIware/drafts/aiw203-chapter-en.md | 320 | 1.0314 | no |
| 316 | /home/jeltz/aIware/drafts/aiw203-chapter-en.md | 320 | 0.9900 | no |
| 317 | /home/jeltz/aIware/drafts/aiw203-chapter-en.md | 320 | 0.9997 | no |
| 318 | /home/jeltz/aIware/drafts/aiw203-chapter-en.md | 320 | 1.0251 | no |
| 319 | /home/jeltz/aIware/drafts/aiw203-chapter-en.md | 320 | 1.0305 | no |
| 320 | /home/jeltz/aIware/drafts/aiw203-chapter-en.md | 320 | 1.0672 | no |
| 321 | /home/jeltz/aIware/drafts/aiw203-chapter-en.md | 320 | 1.0256 | no |
| 322 | /home/jeltz/aIware/drafts/aiw203-chapter-en.md | 320 | 1.0051 | no |
| 323 | /home/jeltz/aIware/drafts/aiw203-chapter-en.md | 320 | 1.0116 | no |
| 324 | /home/jeltz/aIware/drafts/aiw203-chapter-en.md | 320 | 1.0034 | no |
| 325 | /home/jeltz/aIware/drafts/aiw47-eneuro/outreach-email-DRAFT.md | 320 | 1.0529 | no |
| 326 | /home/jeltz/aIware/drafts/aiw47-eneuro/outreach-email-DRAFT.md | 291 | 1.0512 | no |
| 327 | /home/jeltz/aIware/drafts/bbs-seth-commentary.md | 320 | 0.9871 | no |
| 328 | /home/jeltz/aIware/drafts/bbs-seth-commentary.md | 320 | 1.0071 | no |
| 329 | /home/jeltz/aIware/drafts/bbs-seth-commentary.md | 320 | 0.9875 | no |
| 330 | /home/jeltz/aIware/drafts/bbs-seth-proposal.md | 320 | 1.0685 | no |
| 331 | /home/jeltz/aIware/drafts/blog-fmt-misreadings.md | 320 | 0.9838 | no |
| 332 | /home/jeltz/aIware/drafts/blog-fmt-misreadings.md | 320 | 1.0306 | no |
| 333 | /home/jeltz/aIware/drafts/blog-laukkonen-beautiful-loop-fmt.md | 320 | 0.9978 | no |
| 334 | /home/jeltz/aIware/drafts/blog-laukkonen-beautiful-loop-fmt.md | 320 | 1.0121 | no |
| 335 | /home/jeltz/aIware/drafts/blog-laukkonen-beautiful-loop-fmt.md | 320 | 1.0484 | no |
| 336 | /home/jeltz/aIware/drafts/blog-laukkonen-beautiful-loop-fmt.md | 320 | 0.9769 | no |
| 337 | /home/jeltz/aIware/drafts/book-ed2-de-new-prose.md | 320 | 1.0411 | no |
| 338 | /home/jeltz/aIware/drafts/book-ed2-de-new-prose.md | 320 | 1.0110 | no |
| 339 | /home/jeltz/aIware/drafts/book-ed2-de-new-prose.md | 320 | 1.0042 | no |
| 340 | /home/jeltz/aIware/drafts/book-ed2-de-new-prose.md | 320 | 1.0064 | no |
| 341 | /home/jeltz/aIware/drafts/book-ed2-de-new-prose.md | 320 | 1.0115 | no |
| 342 | /home/jeltz/aIware/drafts/book-ed2-de-new-prose.md | 320 | 0.9951 | no |
| 343 | /home/jeltz/aIware/drafts/book-ed2-de-new-prose.md | 320 | 0.9499 | no |
| 344 | /home/jeltz/aIware/drafts/book-ed2-de-new-prose.md | 320 | 1.0113 | no |
| 345 | /home/jeltz/aIware/drafts/book-ed2-de-new-prose.md | 320 | 0.9719 | no |
| 346 | /home/jeltz/aIware/drafts/book-ed2-de-new-prose.md | 320 | 0.9934 | no |
| 347 | /home/jeltz/aIware/drafts/cogito-antragsskizze.md | 320 | 0.9978 | no |
| 348 | /home/jeltz/aIware/drafts/cogito-antragsskizze.md | 320 | 1.0519 | no |
| 349 | /home/jeltz/aIware/drafts/cogito-antragsskizze.md | 320 | 0.9762 | no |
| 350 | /home/jeltz/aIware/drafts/companion-computational-paper-draft.md | 320 | 1.0625 | no |
| 351 | /home/jeltz/aIware/drafts/companion-computational-paper-draft.md | 320 | 1.0086 | no |
| 352 | /home/jeltz/aIware/drafts/companion-computational-paper-draft.md | 320 | 1.0126 | no |
| 353 | /home/jeltz/aIware/drafts/companion-computational-paper-draft.md | 320 | 1.0397 | no |
| 354 | /home/jeltz/aIware/drafts/companion-computational-paper-draft.md | 320 | 1.1005 | no |
| 355 | /home/jeltz/aIware/drafts/companion-computational-paper-draft.md | 320 | 1.0105 | no |
| 356 | /home/jeltz/aIware/drafts/companion-computational-paper-draft.md | 320 | 1.0017 | no |
| 357 | /home/jeltz/aIware/drafts/companion-computational-paper-draft.md | 320 | 1.0397 | no |
| 358 | /home/jeltz/aIware/drafts/companion-computational-paper-draft.md | 320 | 1.0476 | no |
| 359 | /home/jeltz/aIware/drafts/companion-computational-paper-draft.md | 320 | 1.0102 | no |
| 360 | /home/jeltz/aIware/drafts/companion-computational-paper-draft.md | 320 | 1.0795 | no |
| 361 | /home/jeltz/aIware/drafts/companion-computational-paper-draft.md | 320 | 1.0838 | no |
| 362 | /home/jeltz/aIware/drafts/companion-computational-paper-draft.md | 320 | 1.0278 | no |
| 363 | /home/jeltz/aIware/drafts/crucible-fmt-adversary-risks-2026-07-07.md | 320 | 1.0406 | no |
| 364 | /home/jeltz/aIware/drafts/crucible-fmt-adversary-risks-2026-07-07.md | 320 | 1.0710 | no |
| 365 | /home/jeltz/aIware/drafts/crucible-fmt-adversary-risks-2026-07-07.md | 320 | 1.0445 | no |
| 366 | /home/jeltz/aIware/drafts/crucible-fmt-adversary-risks-2026-07-07.md | 320 | 1.0362 | no |
| 367 | /home/jeltz/aIware/drafts/crucible-fmt-adversary-risks-2026-07-07.md | 320 | 1.0736 | no |
| 368 | /home/jeltz/aIware/drafts/crucible-fmt-adversary-risks-2026-07-07.md | 320 | 1.0451 | no |
| 369 | /home/jeltz/aIware/drafts/davos-target-list.md | 320 | 1.0697 | no |
| 370 | /home/jeltz/aIware/drafts/davos-target-list.md | 320 | 1.0276 | no |
| 371 | /home/jeltz/aIware/drafts/davos-target-list.md | 298 | 1.0495 | no |
| 372 | /home/jeltz/aIware/drafts/kanai-iccr-vs-fmt-comparison-2026-07-28.md | 320 | 1.0541 | no |
| 373 | /home/jeltz/aIware/drafts/kanai-iccr-vs-fmt-comparison-2026-07-28.md | 320 | 1.0573 | no |
| 374 | /home/jeltz/aIware/drafts/kanai-iccr-vs-fmt-comparison-2026-07-28.md | 320 | 1.0484 | no |
| 375 | /home/jeltz/aIware/drafts/kanai-iccr-vs-fmt-comparison-2026-07-28.md | 263 | 1.0389 | no |
| 376 | /home/jeltz/aIware/drafts/moc7-accommodation-shortlist.md | 320 | 1.0255 | no |
| 377 | /home/jeltz/aIware/drafts/moc7-accommodation-shortlist.md | 320 | 1.0618 | no |
| 378 | /home/jeltz/aIware/drafts/moc7-accommodation-shortlist.md | 320 | 1.0347 | no |
| 379 | /home/jeltz/aIware/drafts/moc7-accommodation-shortlist.md | 320 | 1.0155 | no |
| 380 | /home/jeltz/aIware/drafts/moc7-handout-a4.md | 320 | 1.0164 | no |
| 381 | /home/jeltz/aIware/drafts/moc7-handout-a4.md | 320 | 1.0552 | no |
| 382 | /home/jeltz/aIware/drafts/moc7-poster-content.md | 320 | 1.0619 | no |
| 383 | /home/jeltz/aIware/drafts/moc7-poster-content.md | 320 | 1.0377 | no |
| 384 | /home/jeltz/aIware/drafts/moc7-poster-content.md | 320 | 1.0278 | no |
| 385 | /home/jeltz/aIware/drafts/moc7-poster-content.md | 318 | 1.0316 | no |
| 386 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0206 | no |
| 387 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0307 | no |
| 388 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0513 | no |
| 389 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0471 | no |
| 390 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0100 | no |
| 391 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0359 | no |
| 392 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0719 | no |
| 393 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0523 | no |
| 394 | /home/jeltz/aIware/drafts/noc-reference-repairs-for-mg.md | 320 | 1.0473 | no |
| 395 | /home/jeltz/aIware/drafts/pitch-aeon.md | 320 | 0.9707 | no |
| 396 | /home/jeltz/aIware/drafts/pitch-aeon.md | 320 | 0.9659 | no |
| 397 | /home/jeltz/aIware/drafts/pitch-nautilus.md | 320 | 0.9425 | no |
| 398 | /home/jeltz/aIware/drafts/pitch-nautilus.md | 320 | 1.0083 | no |
| 399 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0289 | no |
| 400 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0792 | no |
| 401 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0374 | no |
| 402 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0109 | no |
| 403 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0266 | no |
| 404 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0371 | no |
| 405 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0655 | no |
| 406 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 0.9902 | no |
| 407 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0130 | no |
| 408 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0234 | no |
| 409 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0287 | no |
| 410 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0318 | no |
| 411 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0402 | no |
| 412 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0153 | no |
| 413 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 0.9908 | no |
| 414 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0259 | no |
| 415 | /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md | 320 | 1.0125 | no |
| 416 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 1.0401 | no |
| 417 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 0.9952 | no |
| 418 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 0.9790 | no |
| 419 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 1.0358 | no |
| 420 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 0.9613 | no |
| 421 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 0.9605 | no |
| 422 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 1.0551 | no |
| 423 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 1.0557 | no |
| 424 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 1.0241 | no |
| 425 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 1.0291 | no |
| 426 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 0.9914 | no |
| 427 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 0.9636 | no |
| 428 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 1.0360 | no |
| 429 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 1.0051 | no |
| 430 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 0.9896 | no |
| 431 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 1.0257 | no |
| 432 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 0.9602 | no |
| 433 | /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md | 320 | 1.0000 | no |
| 434 | /home/jeltz/aIware/drafts/return-vs-closure-vocabulary-ruling.md | 320 | 1.0479 | no |
| 435 | /home/jeltz/aIware/drafts/return-vs-closure-vocabulary-ruling.md | 320 | 1.0296 | no |
| 436 | /home/jeltz/aIware/drafts/return-vs-closure-vocabulary-ruling.md | 320 | 1.0238 | no |
| 437 | /home/jeltz/aIware/drafts/rim-edwards-deyoung-cite.md | 320 | 1.0776 | no |
| 438 | /home/jeltz/aIware/drafts/rim-motivation-revision.md | 320 | 0.9736 | no |
| 439 | /home/jeltz/aIware/drafts/rim-motivation-revision.md | 320 | 1.0359 | no |
| 440 | /home/jeltz/aIware/drafts/rim-motivation-revision.md | 320 | 0.9807 | no |
| 441 | /home/jeltz/aIware/drafts/rim-priorart-citations-verification.md | 320 | 0.9595 | no |
| 442 | /home/jeltz/aIware/drafts/rim-priorart-citations-verification.md | 320 | 0.9628 | no |
| 443 | /home/jeltz/aIware/drafts/rim-priorart-citations-verification.md | 320 | 0.9689 | no |
| 444 | /home/jeltz/aIware/drafts/rim-priorart-citations-verification.md | 303 | 1.0433 | no |
| 445 | /home/jeltz/aIware/drafts/rim-priorart-convergence.md | 320 | 1.0683 | no |
| 446 | /home/jeltz/aIware/drafts/rim-priorart-convergence.md | 320 | 1.0875 | no |
| 447 | /home/jeltz/aIware/drafts/sjalv-manual-brief-for-perplexity.md | 320 | 1.0307 | no |
| 448 | /home/jeltz/aIware/drafts/sjalv-manual-brief-for-perplexity.md | 320 | 1.0293 | no |
| 449 | /home/jeltz/aIware/drafts/sjalv-manual-brief-for-perplexity.md | 320 | 1.0337 | no |
| 450 | /home/jeltz/aIware/drafts/sjalv-manual-brief-for-perplexity.md | 320 | 1.0198 | no |
| 451 | /home/jeltz/aIware/drafts/sjalv-manual-brief-for-perplexity.md | 320 | 1.0758 | no |
| 452 | /home/jeltz/aIware/drafts/sjalv-manual-brief-for-perplexity.md | 320 | 1.0408 | no |
| 453 | /home/jeltz/aIware/drafts/sjalv-manual-brief-for-perplexity.md | 320 | 1.0384 | no |
| 454 | /home/jeltz/aIware/drafts/sjalv-manual-brief-for-perplexity.md | 320 | 0.9951 | no |
| 455 | /home/jeltz/aIware/drafts/sjalv-manual-brief-for-perplexity.md | 320 | 1.0178 | no |
| 456 | /home/jeltz/aIware/drafts/styropyro-note.md | 320 | 1.0070 | no |
| 457 | /home/jeltz/aIware/drafts/translation-nl-el-ko/control/culture-guide-el.md | 320 | 1.0303 | no |
| 458 | /home/jeltz/aIware/drafts/translation-nl-el-ko/control/culture-guide-el.md | 320 | 1.0429 | no |
| 459 | /home/jeltz/aIware/drafts/translation-nl-el-ko/control/culture-guide-el.md | 320 | 1.0699 | no |
| 460 | /home/jeltz/aIware/drafts/translation-nl-el-ko/control/culture-guide-ko.md | 320 | 0.9777 | no |
| 461 | /home/jeltz/aIware/drafts/translation-nl-el-ko/control/culture-guide-ko.md | 320 | 1.0088 | no |
| 462 | /home/jeltz/aIware/drafts/translation-nl-el-ko/control/culture-guide-nl.md | 320 | 1.0327 | no |
| 463 | /home/jeltz/aIware/drafts/translation-nl-el-ko/control/culture-guide-nl.md | 320 | 1.0329 | no |
| 464 | /home/jeltz/aIware/drafts/translation-nl-el-ko/control/culture-guide-nl.md | 320 | 1.0663 | no |
| 465 | /home/jeltz/aIware/drafts/translation-nl-el-ko/control/glossary-el.md | 320 | 1.0640 | no |
| 466 | /home/jeltz/aIware/drafts/translation-nl-el-ko/control/glossary-el.md | 320 | 1.0979 | no |
| 467 | /home/jeltz/aIware/drafts/translation-nl-el-ko/control/glossary-ko.md | 320 | 0.9775 | no |
| 468 | /home/jeltz/aIware/drafts/translation-nl-el-ko/control/glossary-nl.md | 320 | 1.1303 | no |
| 469 | /home/jeltz/aIware/drafts/translation-nl-el-ko/control/glossary-nl.md | 283 | 1.0319 | no |
| 470 | /home/jeltz/aIware/paper/aiw47/aiw47-eneuro-opinion.md | 320 | 1.0188 | no |
| 471 | /home/jeltz/aIware/paper/aiw47/aiw47-eneuro-opinion.md | 320 | 1.0097 | no |
| 472 | /home/jeltz/aIware/paper/aiw47/aiw47-eneuro-opinion.md | 320 | 1.0124 | no |
| 473 | /home/jeltz/aIware/paper/aiw47/aiw47-eneuro-opinion.md | 320 | 1.0386 | no |
| 474 | /home/jeltz/aIware/paper/aiw47/aiw47-eneuro-opinion.md | 320 | 1.0083 | no |
| 475 | /home/jeltz/aIware/paper/aiw47/aiw47-eneuro-opinion.md | 320 | 1.0865 | no |
| 476 | /home/jeltz/aIware/paper/aiw47/aiw47-eneuro-opinion.md | 320 | 1.0261 | no |
| 477 | /home/jeltz/aIware/paper/aiw47/aiw47-eneuro-opinion.md | 320 | 1.1054 | no |
| 478 | /home/jeltz/aIware/paper/aiw47/aiw47-eneuro-opinion.md | 320 | 1.0141 | no |
| 479 | /home/jeltz/aIware/paper/aiw47/aiw47-eneuro-opinion.md | 314 | 1.0340 | no |
| 480 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0455 | no |
| 481 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9542 | no |
| 482 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9729 | no |
| 483 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9828 | no |
| 484 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9704 | no |
| 485 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.8708 | yes |
| 486 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9580 | no |
| 487 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9932 | no |
| 488 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9549 | no |
| 489 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9091 | yes |
| 490 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9891 | no |
| 491 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9868 | no |
| 492 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9722 | no |
| 493 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0292 | no |
| 494 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0140 | no |
| 495 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0013 | no |
| 496 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0086 | no |
| 497 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0194 | no |
| 498 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9849 | no |
| 499 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0219 | no |
| 500 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0393 | no |
| 501 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9736 | no |
| 502 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9593 | no |
| 503 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0831 | no |
| 504 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0454 | no |
| 505 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0259 | no |
| 506 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0060 | no |
| 507 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 0.9439 | no |
| 508 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0024 | no |
| 509 | /home/jeltz/aIware/paper/cc/four-model-theory-cc.md | 320 | 1.0124 | no |
| 510 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 1.0716 | no |
| 511 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 0.9920 | no |
| 512 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 0.9772 | no |
| 513 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 0.9791 | no |
| 514 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 0.9736 | no |
| 515 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 0.9662 | no |
| 516 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 0.9564 | no |
| 517 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 0.9848 | no |
| 518 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 0.9985 | no |
| 519 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 1.0509 | no |
| 520 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 0.9996 | no |
| 521 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 0.9611 | no |
| 522 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 1.0246 | no |
| 523 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 0.9874 | no |
| 524 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 0.9977 | no |
| 525 | /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md | 320 | 1.0191 | no |
| 526 | /home/jeltz/aIware/paper/cosmology/perplexity literature findings.md | 320 | 1.0264 | no |
| 527 | /home/jeltz/aIware/paper/cosmology/perplexity literature findings.md | 320 | 1.0072 | no |
| 528 | /home/jeltz/aIware/paper/cosmology/perplexity literature findings.md | 320 | 1.0115 | no |
| 529 | /home/jeltz/aIware/paper/cosmology/perplexity literature findings.md | 320 | 0.9997 | no |
| 530 | /home/jeltz/aIware/paper/cosmology/perplexity literature findings.md | 320 | 0.9831 | no |
| 531 | /home/jeltz/aIware/paper/cosmology/perplexity literature findings.md | 320 | 1.0237 | no |
| 532 | /home/jeltz/aIware/paper/cosmology/perplexity literature findings.md | 253 | 1.0057 | no |
| 533 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0048 | no |
| 534 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9638 | no |
| 535 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9583 | no |
| 536 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0047 | no |
| 537 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9974 | no |
| 538 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0068 | no |
| 539 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0189 | no |
| 540 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0385 | no |
| 541 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0288 | no |
| 542 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0414 | no |
| 543 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9583 | no |
| 544 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0010 | no |
| 545 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0698 | no |
| 546 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9982 | no |
| 547 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9907 | no |
| 548 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0133 | no |
| 549 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9653 | no |
| 550 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0301 | no |
| 551 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9957 | no |
| 552 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0371 | no |
| 553 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9799 | no |
| 554 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0063 | no |
| 555 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0082 | no |
| 556 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0502 | no |
| 557 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0353 | no |
| 558 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0200 | no |
| 559 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0613 | no |
| 560 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0952 | no |
| 561 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0289 | no |
| 562 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0359 | no |
| 563 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0226 | no |
| 564 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0330 | no |
| 565 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0057 | no |
| 566 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9735 | no |
| 567 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.1058 | no |
| 568 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9862 | no |
| 569 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9626 | no |
| 570 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0611 | no |
| 571 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9451 | no |
| 572 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0539 | no |
| 573 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0247 | no |
| 574 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0308 | no |
| 575 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9991 | no |
| 576 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9916 | no |
| 577 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9805 | no |
| 578 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0020 | no |
| 579 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9362 | no |
| 580 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0156 | no |
| 581 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0217 | no |
| 582 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9715 | no |
| 583 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0063 | no |
| 584 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0154 | no |
| 585 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0612 | no |
| 586 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0456 | no |
| 587 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0645 | no |
| 588 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0557 | no |
| 589 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0639 | no |
| 590 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.1213 | no |
| 591 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9872 | no |
| 592 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9939 | no |
| 593 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9551 | no |
| 594 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0368 | no |
| 595 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0096 | no |
| 596 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0530 | no |
| 597 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0020 | no |
| 598 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9832 | no |
| 599 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9278 | yes |
| 600 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9907 | no |
| 601 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9578 | no |
| 602 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0598 | no |
| 603 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0184 | no |
| 604 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9697 | no |
| 605 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9807 | no |
| 606 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9552 | no |
| 607 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9817 | no |
| 608 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9865 | no |
| 609 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0101 | no |
| 610 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9518 | no |
| 611 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 0.9465 | no |
| 612 | /home/jeltz/aIware/paper/cosmology/sb-hc4a.md | 320 | 1.0238 | no |
| 613 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0219 | no |
| 614 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9629 | no |
| 615 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9600 | no |
| 616 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0359 | no |
| 617 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9698 | no |
| 618 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0175 | no |
| 619 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9822 | no |
| 620 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9942 | no |
| 621 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0466 | no |
| 622 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9817 | no |
| 623 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0185 | no |
| 624 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9763 | no |
| 625 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9227 | yes |
| 626 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9612 | no |
| 627 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9911 | no |
| 628 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0155 | no |
| 629 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0465 | no |
| 630 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0519 | no |
| 631 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9631 | no |
| 632 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9367 | no |
| 633 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0129 | no |
| 634 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0118 | no |
| 635 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0626 | no |
| 636 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0436 | no |
| 637 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0231 | no |
| 638 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.8874 | yes |
| 639 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9027 | yes |
| 640 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9557 | no |
| 641 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9754 | no |
| 642 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9863 | no |
| 643 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9983 | no |
| 644 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9335 | no |
| 645 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0114 | no |
| 646 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9374 | no |
| 647 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9417 | no |
| 648 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0293 | no |
| 649 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9626 | no |
| 650 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9043 | yes |
| 651 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9912 | no |
| 652 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9512 | no |
| 653 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9906 | no |
| 654 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9791 | no |
| 655 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0151 | no |
| 656 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9702 | no |
| 657 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9614 | no |
| 658 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 1.0634 | no |
| 659 | /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md | 320 | 0.9796 | no |
| 660 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0137 | no |
| 661 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0542 | no |
| 662 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 0.9333 | no |
| 663 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0002 | no |
| 664 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 0.9685 | no |
| 665 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 0.9732 | no |
| 666 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0074 | no |
| 667 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0244 | no |
| 668 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0160 | no |
| 669 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0439 | no |
| 670 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 0.9991 | no |
| 671 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0142 | no |
| 672 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0035 | no |
| 673 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 0.9953 | no |
| 674 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0092 | no |
| 675 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0121 | no |
| 676 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0403 | no |
| 677 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0131 | no |
| 678 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0605 | no |
| 679 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0415 | no |
| 680 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0506 | no |
| 681 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0238 | no |
| 682 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0708 | no |
| 683 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0001 | no |
| 684 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 0.9587 | no |
| 685 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0122 | no |
| 686 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 0.9689 | no |
| 687 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 0.9786 | no |
| 688 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 0.9833 | no |
| 689 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0042 | no |
| 690 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0525 | no |
| 691 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0272 | no |
| 692 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0268 | no |
| 693 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0383 | no |
| 694 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 1.0516 | no |
| 695 | /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md | 320 | 0.9912 | no |
| 696 | /home/jeltz/aIware/paper/fmt_permeability_criticality/fmt-permeability-criticality.md | 320 | 1.0915 | no |
| 697 | /home/jeltz/aIware/paper/fmt_permeability_criticality/fmt-permeability-criticality.md | 320 | 1.0658 | no |
| 698 | /home/jeltz/aIware/paper/fmt_permeability_criticality/fmt-permeability-criticality.md | 320 | 1.0182 | no |
| 699 | /home/jeltz/aIware/paper/fmt_permeability_criticality/fmt-permeability-criticality.md | 320 | 1.0279 | no |
| 700 | /home/jeltz/aIware/paper/fmt_permeability_criticality/fmt-permeability-criticality.md | 320 | 1.0436 | no |
| 701 | /home/jeltz/aIware/paper/fmt_permeability_criticality/fmt-permeability-criticality.md | 320 | 1.0530 | no |
| 702 | /home/jeltz/aIware/paper/fmt_permeability_criticality/fmt-permeability-criticality.md | 320 | 1.0447 | no |
| 703 | /home/jeltz/aIware/paper/fmt_permeability_criticality/fmt-permeability-criticality.md | 320 | 1.0445 | no |
| 704 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9669 | no |
| 705 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 1.0545 | no |
| 706 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9321 | no |
| 707 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9675 | no |
| 708 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9853 | no |
| 709 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9730 | no |
| 710 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9317 | yes |
| 711 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9168 | yes |
| 712 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9269 | yes |
| 713 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9472 | no |
| 714 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9281 | yes |
| 715 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.8977 | yes |
| 716 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9520 | no |
| 717 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9721 | no |
| 718 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9916 | no |
| 719 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9385 | no |
| 720 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9877 | no |
| 721 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 1.0099 | no |
| 722 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 1.0352 | no |
| 723 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9834 | no |
| 724 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 1.0001 | no |
| 725 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9579 | no |
| 726 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 1.0169 | no |
| 727 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9901 | no |
| 728 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9578 | no |
| 729 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9960 | no |
| 730 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9458 | no |
| 731 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9516 | no |
| 732 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9643 | no |
| 733 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9541 | no |
| 734 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 1.0123 | no |
| 735 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9750 | no |
| 736 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9367 | no |
| 737 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9799 | no |
| 738 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9422 | no |
| 739 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9745 | no |
| 740 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9485 | no |
| 741 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 1.0006 | no |
| 742 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9639 | no |
| 743 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9915 | no |
| 744 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 1.0171 | no |
| 745 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9586 | no |
| 746 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9649 | no |
| 747 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 1.0027 | no |
| 748 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9516 | no |
| 749 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.8978 | yes |
| 750 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9423 | no |
| 751 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 1.0176 | no |
| 752 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9531 | no |
| 753 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 1.0033 | no |
| 754 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9869 | no |
| 755 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 0.9699 | no |
| 756 | /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md | 320 | 1.0020 | no |
| 757 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0459 | no |
| 758 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0212 | no |
| 759 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9620 | no |
| 760 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0638 | no |
| 761 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0225 | no |
| 762 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0245 | no |
| 763 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9878 | no |
| 764 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9858 | no |
| 765 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9378 | no |
| 766 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0056 | no |
| 767 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9409 | no |
| 768 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9948 | no |
| 769 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9976 | no |
| 770 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0296 | no |
| 771 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0065 | no |
| 772 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9973 | no |
| 773 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9317 | yes |
| 774 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9656 | no |
| 775 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9809 | no |
| 776 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0516 | no |
| 777 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9780 | no |
| 778 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0342 | no |
| 779 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0587 | no |
| 780 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0457 | no |
| 781 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9791 | no |
| 782 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0098 | no |
| 783 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0373 | no |
| 784 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9731 | no |
| 785 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9866 | no |
| 786 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9412 | no |
| 787 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0367 | no |
| 788 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0125 | no |
| 789 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0030 | no |
| 790 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0515 | no |
| 791 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9304 | yes |
| 792 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9311 | yes |
| 793 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9672 | no |
| 794 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0286 | no |
| 795 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9731 | no |
| 796 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0218 | no |
| 797 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9325 | no |
| 798 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0718 | no |
| 799 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9747 | no |
| 800 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9706 | no |
| 801 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0273 | no |
| 802 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0009 | no |
| 803 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9814 | no |
| 804 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0219 | no |
| 805 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0651 | no |
| 806 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0523 | no |
| 807 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0272 | no |
| 808 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0101 | no |
| 809 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0322 | no |
| 810 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0369 | no |
| 811 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0405 | no |
| 812 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0592 | no |
| 813 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0602 | no |
| 814 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0240 | no |
| 815 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0793 | no |
| 816 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0137 | no |
| 817 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9790 | no |
| 818 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9921 | no |
| 819 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0262 | no |
| 820 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0615 | no |
| 821 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0548 | no |
| 822 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9749 | no |
| 823 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9994 | no |
| 824 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9894 | no |
| 825 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9714 | no |
| 826 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0505 | no |
| 827 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9873 | no |
| 828 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0056 | no |
| 829 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9972 | no |
| 830 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0414 | no |
| 831 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0246 | no |
| 832 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0888 | no |
| 833 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0701 | no |
| 834 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9950 | no |
| 835 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0211 | no |
| 836 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0500 | no |
| 837 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0335 | no |
| 838 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9836 | no |
| 839 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0165 | no |
| 840 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9627 | no |
| 841 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0883 | no |
| 842 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0352 | no |
| 843 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0342 | no |
| 844 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9760 | no |
| 845 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0336 | no |
| 846 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0042 | no |
| 847 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9702 | no |
| 848 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9999 | no |
| 849 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0613 | no |
| 850 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9317 | yes |
| 851 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0473 | no |
| 852 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0025 | no |
| 853 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9455 | no |
| 854 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0292 | no |
| 855 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9826 | no |
| 856 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0231 | no |
| 857 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9879 | no |
| 858 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0351 | no |
| 859 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9973 | no |
| 860 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0259 | no |
| 861 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0440 | no |
| 862 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0482 | no |
| 863 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0265 | no |
| 864 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0165 | no |
| 865 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0166 | no |
| 866 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0935 | no |
| 867 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0259 | no |
| 868 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0587 | no |
| 869 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0508 | no |
| 870 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0216 | no |
| 871 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0375 | no |
| 872 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0580 | no |
| 873 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0350 | no |
| 874 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0296 | no |
| 875 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0532 | no |
| 876 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0213 | no |
| 877 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9850 | no |
| 878 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0304 | no |
| 879 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0068 | no |
| 880 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0534 | no |
| 881 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9540 | no |
| 882 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0638 | no |
| 883 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0218 | no |
| 884 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0494 | no |
| 885 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.1092 | no |
| 886 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0829 | no |
| 887 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0205 | no |
| 888 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0551 | no |
| 889 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9512 | no |
| 890 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0133 | no |
| 891 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0210 | no |
| 892 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0095 | no |
| 893 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0439 | no |
| 894 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0120 | no |
| 895 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 0.9844 | no |
| 896 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0078 | no |
| 897 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0226 | no |
| 898 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 320 | 1.0212 | no |
| 899 | /home/jeltz/aIware/paper/full/four-model-theory-full.md | 286 | 1.0185 | no |
| 900 | /home/jeltz/aIware/paper/intelligence/literature-research.md | 320 | 1.0262 | no |
| 901 | /home/jeltz/aIware/paper/intelligence/literature-research.md | 320 | 1.0187 | no |
| 902 | /home/jeltz/aIware/paper/intelligence/literature-research.md | 320 | 1.0193 | no |
| 903 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0074 | no |
| 904 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9452 | no |
| 905 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9844 | no |
| 906 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9502 | no |
| 907 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9213 | yes |
| 908 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9462 | no |
| 909 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9869 | no |
| 910 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0505 | no |
| 911 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0283 | no |
| 912 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0228 | no |
| 913 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9234 | yes |
| 914 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.8999 | yes |
| 915 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0121 | no |
| 916 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9197 | yes |
| 917 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0051 | no |
| 918 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0181 | no |
| 919 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0389 | no |
| 920 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0388 | no |
| 921 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9158 | yes |
| 922 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9203 | yes |
| 923 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9655 | no |
| 924 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0321 | no |
| 925 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0100 | no |
| 926 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9642 | no |
| 927 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9444 | no |
| 928 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9973 | no |
| 929 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0258 | no |
| 930 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9712 | no |
| 931 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9535 | no |
| 932 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0411 | no |
| 933 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0300 | no |
| 934 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0124 | no |
| 935 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9863 | no |
| 936 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0773 | no |
| 937 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0214 | no |
| 938 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9822 | no |
| 939 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0506 | no |
| 940 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0663 | no |
| 941 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0444 | no |
| 942 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0459 | no |
| 943 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0699 | no |
| 944 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0340 | no |
| 945 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 1.0286 | no |
| 946 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9319 | yes |
| 947 | /home/jeltz/aIware/paper/intelligence/paper.md | 320 | 0.9228 | yes |
| 948 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 0.9614 | no |
| 949 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 1.0101 | no |
| 950 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 0.9535 | no |
| 951 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 0.9651 | no |
| 952 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 1.0212 | no |
| 953 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 0.9670 | no |
| 954 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 1.0200 | no |
| 955 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 0.9773 | no |
| 956 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 0.9194 | yes |
| 957 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 0.9741 | no |
| 958 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 0.9929 | no |
| 959 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 1.0121 | no |
| 960 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 1.0026 | no |
| 961 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 1.0101 | no |
| 962 | /home/jeltz/aIware/paper/rim_formal/rim-formalization.md | 320 | 0.9693 | no |
| 963 | /home/jeltz/aIware/paper/seth-commentary/seth-commentary.md | 320 | 1.0618 | no |
| 964 | /home/jeltz/aIware/paper/seth-commentary/seth-commentary.md | 320 | 1.0705 | no |
| 965 | /home/jeltz/aIware/paper/seth-commentary/seth-commentary.md | 320 | 1.0997 | no |
| 966 | /home/jeltz/aIware/paper/trimmed/noc/SUBMISSION-CHECKLIST.md | 320 | 0.9748 | no |
| 967 | /home/jeltz/aIware/paper/trimmed/noc/figure-alt-text.md | 320 | 0.9449 | no |
| 968 | /home/jeltz/aIware/paper/trimmed/noc/figure-alt-text.md | 320 | 1.0129 | no |
| 969 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 1.0539 | no |
| 970 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9664 | no |
| 971 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9792 | no |
| 972 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9631 | no |
| 973 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9619 | no |
| 974 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9170 | yes |
| 975 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9139 | yes |
| 976 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9900 | no |
| 977 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9648 | no |
| 978 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9061 | yes |
| 979 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9213 | yes |
| 980 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9576 | no |
| 981 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 1.0195 | no |
| 982 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 1.0539 | no |
| 983 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9908 | no |
| 984 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9847 | no |
| 985 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 1.0159 | no |
| 986 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 1.0164 | no |
| 987 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9530 | no |
| 988 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 1.0123 | no |
| 989 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 1.0169 | no |
| 990 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9774 | no |
| 991 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9908 | no |
| 992 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 1.0381 | no |
| 993 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 1.0278 | no |
| 994 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9429 | no |
| 995 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 1.0443 | no |
| 996 | /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md | 320 | 0.9763 | no |

## Sources

- /home/jeltz/aIware/drafts/aiw-el-interior-fable-review.md (md): 33121 raw chars -> 4975 chars of prose (688 words). Removed: code 2x/10 chars, math 1x/10 chars, table 9x/26711 chars, markup 18x/63 chars, heading 10x/1321 chars.
- /home/jeltz/aIware/drafts/aiw-ko-interior-fable-review.md (md): 28398 raw chars -> 1930 chars of prose (269 words). Removed: table 9x/25062 chars, markup 4x/15 chars, heading 10x/1367 chars.
- /home/jeltz/aIware/drafts/aiw-nl-interior-fable-review.md (md): 30826 raw chars -> 10591 chars of prose (1624 words). Removed: code 6x/48 chars, table 9x/18606 chars, markup 51x/187 chars, heading 10x/1348 chars.
- /home/jeltz/aIware/drafts/aiw-operationalization-review.md (md): 29875 raw chars -> 27157 chars of prose (4321 words). Removed: comment 1x/695 chars, code 16x/536 chars, bibliography 1x/890 chars, markup 80x/238 chars, heading 9x/340 chars.
- /home/jeltz/aIware/drafts/aiw105-qualia-privacy-paper-draft.md (md): 29696 raw chars -> 27742 chars of prose (4083 words). Removed: comment 1x/397 chars, markup 189x/512 chars, heading 16x/994 chars.
- /home/jeltz/aIware/drafts/aiw107-kalk-scan-findings.md (md): 11575 raw chars -> 10550 chars of prose (1579 words). Removed: code 7x/188 chars, markup 117x/346 chars, heading 7x/482 chars.
- /home/jeltz/aIware/drafts/aiw108-cross-edition-qa-findings.md (md): 14176 raw chars -> 9037 chars of prose (1283 words). Removed: comment 2x/81 chars, code 19x/476 chars, table 3x/3762 chars, markup 85x/323 chars, heading 9x/464 chars.
- /home/jeltz/aIware/drafts/aiw108-de-fable-final-review.md (md): 12469 raw chars -> 5414 chars of prose (730 words). Removed: comment 1x/76 chars, code 5x/62 chars, table 2x/6175 chars, markup 70x/216 chars, heading 10x/506 chars.
- /home/jeltz/aIware/drafts/aiw108-el-kalk-findings.md (md): 214157 raw chars -> 269 chars of prose (47 words). Removed: code 2x/42 chars, table 4x/213563 chars, markup 7x/23 chars, heading 5x/242 chars.
- /home/jeltz/aIware/drafts/aiw108-en-fable-final-review.md (md): 8498 raw chars -> 2049 chars of prose (311 words). Removed: comment 1x/76 chars, code 3x/31 chars, table 5x/5881 chars, markup 26x/87 chars, heading 9x/347 chars.
- /home/jeltz/aIware/drafts/aiw108-es-kalk-findings.md (md): 25458 raw chars -> 23801 chars of prose (3820 words). Removed: code 8x/121 chars, markup 234x/704 chars, heading 7x/415 chars.
- /home/jeltz/aIware/drafts/aiw108-fr-coherence-findings.md (md): 15875 raw chars -> 14528 chars of prose (2504 words). Removed: code 2x/43 chars, markup 116x/351 chars, heading 15x/934 chars.
- /home/jeltz/aIware/drafts/aiw108-fr-kalk-findings.md (md): 9181 raw chars -> 8228 chars of prose (1415 words). Removed: code 5x/136 chars, markup 77x/238 chars, heading 8x/448 chars.
- /home/jeltz/aIware/drafts/aiw108-it-kalk-findings.md (md): 18318 raw chars -> 16847 chars of prose (2903 words). Removed: code 7x/137 chars, markup 234x/683 chars, heading 7x/362 chars.
- /home/jeltz/aIware/drafts/aiw108-ja-kalk-findings.md (md): 17489 raw chars -> 16376 chars of prose (1725 words). Removed: code 9x/122 chars, markup 196x/604 chars, heading 6x/376 chars.
- /home/jeltz/aIware/drafts/aiw108-nl-kalk-findings.md (md): 110468 raw chars -> 68139 chars of prose (9826 words). Removed: code 915x/35686 chars, markup 1391x/3727 chars, heading 12x/615 chars.
- /home/jeltz/aIware/drafts/aiw108-pt-kalk-findings.md (md): 11927 raw chars -> 10905 chars of prose (1748 words). Removed: code 5x/136 chars, markup 103x/312 chars, heading 6x/387 chars.
- /home/jeltz/aIware/drafts/aiw108-zh-kalk-findings.md (md): 3641 raw chars -> 3171 chars of prose (423 words). Removed: code 3x/55 chars, markup 28x/98 chars, heading 5x/308 chars.
- /home/jeltz/aIware/drafts/aiw109-combined-cross-language-findings-S259.md (md): 35755 raw chars -> 10297 chars of prose (1606 words). Removed: code 19x/198 chars, table 11x/23968 chars, markup 144x/499 chars, heading 18x/728 chars.
- /home/jeltz/aIware/drafts/aiw109-es-interior-fable-review-S259.md (md): 33926 raw chars -> 9796 chars of prose (1362 words). Removed: code 13x/418 chars, table 9x/22864 chars, markup 49x/137 chars, heading 11x/651 chars.
- /home/jeltz/aIware/drafts/aiw109-final-review-S264.md (md): 10522 raw chars -> 8915 chars of prose (1421 words). Removed: code 29x/642 chars, table 1x/297 chars, markup 78x/275 chars, heading 8x/324 chars.
- /home/jeltz/aIware/drafts/aiw109-fix-spec.md (md): 10483 raw chars -> 8438 chars of prose (1286 words). Removed: comment 2x/143 chars, code 3x/16 chars, markup 84x/279 chars, heading 11x/1584 chars.
- /home/jeltz/aIware/drafts/aiw109-fr-interior-fable-review-S259.md (md): 36312 raw chars -> 9829 chars of prose (1539 words). Removed: code 37x/248 chars, table 9x/25285 chars, markup 18x/61 chars, heading 10x/832 chars.
- /home/jeltz/aIware/drafts/aiw109-it-interior-fable-review-S259.md (md): 35961 raw chars -> 12345 chars of prose (1866 words). Removed: code 60x/1082 chars, table 9x/21569 chars, markup 70x/239 chars, heading 10x/644 chars.
- /home/jeltz/aIware/drafts/aiw109-ja-interior-fable-review-S259.md (md): 20019 raw chars -> 5008 chars of prose (644 words). Removed: code 2x/6 chars, table 9x/14179 chars, markup 12x/39 chars, heading 10x/740 chars.
- /home/jeltz/aIware/drafts/aiw109-print-reupload-S264.md (md): 3271 raw chars -> 1563 chars of prose (237 words). Removed: code 27x/655 chars, table 2x/691 chars, markup 12x/38 chars, heading 6x/321 chars.
- /home/jeltz/aIware/drafts/aiw109-pt-interior-fable-review-S259.md (md): 34018 raw chars -> 11188 chars of prose (1602 words). Removed: code 22x/377 chars, math 1x/10 chars, table 9x/21429 chars, citation 1x/6 chars, markup 67x/187 chars, heading 16x/747 chars.
- /home/jeltz/aIware/drafts/aiw109-zh-interior-fable-review-S259.md (md): 23990 raw chars -> 7627 chars of prose (994 words). Removed: code 9x/285 chars, table 9x/15143 chars, markup 27x/67 chars, heading 13x/809 chars.
- /home/jeltz/aIware/drafts/aiw119-iwmt-fmt-convergence-note.md (md): 20849 raw chars -> 20403 chars of prose (2878 words). Removed: markup 89x/221 chars, heading 6x/210 chars.
- /home/jeltz/aIware/drafts/aiw120-olinyk-crc-fmt-convergence.md (md): 16760 raw chars -> 14908 chars of prose (2165 words). Removed: bibliography 1x/1127 chars, markup 82x/240 chars, heading 9x/436 chars.
- /home/jeltz/aIware/drafts/aiw130-PROPOSE.md (md): 11205 raw chars -> 9054 chars of prose (1340 words). Removed: comment 1x/85 chars, code 16x/421 chars, table 1x/1038 chars, markup 83x/273 chars, heading 7x/317 chars.
- /home/jeltz/aIware/drafts/aiw130-jaic-cover-letter.md (md): 3836 raw chars -> 3607 chars of prose (477 words). Removed: comment 1x/95 chars, markup 17x/61 chars, heading 1x/69 chars.
- /home/jeltz/aIware/drafts/aiw130-jaic-draft.md (md): 74267 raw chars -> 65780 chars of prose (9847 words). Removed: bibliography 1x/5295 chars, math 98x/1913 chars, image 3x/99 chars, markup 202x/461 chars, heading 14x/610 chars.
- /home/jeltz/aIware/drafts/aiw130-jaic-plan.md (md): 37432 raw chars -> 35659 chars of prose (4889 words). Removed: comment 1x/115 chars, url 1x/26 chars, markup 146x/420 chars, heading 22x/1186 chars.
- /home/jeltz/aIware/drafts/aiw130-noc-cover-letter.md (md): 5618 raw chars -> 5371 chars of prose (737 words). Removed: comment 1x/94 chars, markup 28x/89 chars, heading 1x/60 chars.
- /home/jeltz/aIware/drafts/aiw130-noc-draft.md (md): 62003 raw chars -> 49601 chars of prose (7180 words). Removed: comment 2x/2712 chars, bibliography 1x/8403 chars, image 3x/96 chars, markup 82x/204 chars, heading 21x/932 chars.
- /home/jeltz/aIware/drafts/aiw130-noc-plan.md (md): 47443 raw chars -> 45901 chars of prose (6225 words). Removed: comment 1x/115 chars, code 6x/96 chars, markup 120x/324 chars, heading 21x/975 chars.
- /home/jeltz/aIware/drafts/aiw130-verified-citations.md (md): 12571 raw chars -> 11182 chars of prose (1582 words). Removed: comment 1x/134 chars, code 2x/68 chars, markup 178x/484 chars, heading 12x/688 chars.
- /home/jeltz/aIware/drafts/aiw138-abstract-variants.md (md): 7314 raw chars -> 6736 chars of prose (996 words). Removed: comment 3x/157 chars, code 4x/127 chars, markup 20x/51 chars, heading 5x/210 chars.
- /home/jeltz/aIware/drafts/aiw166-cosmos-transfer.md (md): 24084 raw chars -> 21824 chars of prose (3495 words). Removed: comment 2x/54 chars, code 29x/475 chars, table 1x/357 chars, footnote 1x/4 chars, markup 166x/539 chars, heading 11x/600 chars.
- /home/jeltz/aIware/drafts/aiw174-entanglement-wedge-postulate.md (md): 23254 raw chars -> 18101 chars of prose (2846 words). Removed: code 2x/51 chars, bibliography 1x/2860 chars, table 1x/1293 chars, markup 95x/273 chars, heading 10x/500 chars.
- /home/jeltz/aIware/drafts/aiw174-tsirelson-from-capacity.md (md): 16129 raw chars -> 13376 chars of prose (2121 words). Removed: code 6x/111 chars, bibliography 1x/1439 chars, table 2x/303 chars, markup 107x/275 chars, heading 10x/556 chars.
- /home/jeltz/aIware/drafts/aiw186-vacuity-regime.md (md): 24347 raw chars -> 21509 chars of prose (3470 words). Removed: comment 2x/54 chars, code 28x/457 chars, table 2x/1044 chars, markup 163x/498 chars, heading 11x/636 chars.
- /home/jeltz/aIware/drafts/aiw187-allocation.md (md): 7990 raw chars -> 7021 chars of prose (1140 words). Removed: comment 2x/54 chars, code 34x/348 chars, markup 47x/153 chars, heading 7x/373 chars.
- /home/jeltz/aIware/drafts/aiw192-dream-database-reanalysis.md (md): 6626 raw chars -> 5250 chars of prose (856 words). Removed: comment 2x/63 chars, code 5x/92 chars, table 2x/614 chars, markup 55x/182 chars, heading 7x/367 chars.
- /home/jeltz/aIware/drafts/aiw203-chapter-en.md (md): 20406 raw chars -> 19704 chars of prose (3388 words). Removed: code 4x/81 chars, markup 57x/137 chars, heading 8x/459 chars.
- /home/jeltz/aIware/drafts/aiw47-eneuro/outreach-email-DRAFT.md (md): 5314 raw chars -> 4678 chars of prose (611 words). Removed: comment 1x/511 chars, markup 3x/12 chars, heading 1x/109 chars.
- /home/jeltz/aIware/drafts/bbs-seth-commentary.md (md): 7631 raw chars -> 7381 chars of prose (994 words). Removed: url 4x/121 chars, markup 25x/68 chars, heading 1x/50 chars.
- /home/jeltz/aIware/drafts/bbs-seth-proposal.md (md): 3510 raw chars -> 3254 chars of prose (402 words). Removed: code 1x/31 chars, url 2x/65 chars, markup 20x/62 chars, heading 3x/84 chars.
- /home/jeltz/aIware/drafts/blog-fmt-misreadings.md (md): 5765 raw chars -> 5118 chars of prose (812 words). Removed: comment 1x/304 chars, markup 10x/21 chars, heading 5x/308 chars.
- /home/jeltz/aIware/drafts/blog-laukkonen-beautiful-loop-fmt.md (md): 9605 raw chars -> 9045 chars of prose (1452 words). Removed: comment 1x/235 chars, markup 34x/94 chars, heading 5x/218 chars.
- /home/jeltz/aIware/drafts/book-ed2-de-new-prose.md (md): 23442 raw chars -> 22181 chars of prose (3419 words). Removed: image 1x/212 chars, markup 50x/150 chars, heading 13x/847 chars.
- /home/jeltz/aIware/drafts/cogito-antragsskizze.md (md): 10499 raw chars -> 8815 chars of prose (990 words). Removed: table 2x/1003 chars, url 2x/68 chars, markup 74x/216 chars, heading 11x/366 chars.
- /home/jeltz/aIware/drafts/companion-computational-paper-draft.md (md): 33176 raw chars -> 28090 chars of prose (4379 words). Removed: comment 2x/1893 chars, code 17x/374 chars, bibliography 1x/1653 chars, markup 79x/175 chars, heading 17x/947 chars.
- /home/jeltz/aIware/drafts/corrigendum-ed2.md (md): 1621 raw chars -> 1419 chars of prose (229 words). Removed: front_matter 1x/54 chars, markup 24x/86 chars, heading 2x/54 chars.
- /home/jeltz/aIware/drafts/crucible-fmt-adversary-risks-2026-07-07.md (md): 17228 raw chars -> 15020 chars of prose (2121 words). Removed: comment 1x/116 chars, code 26x/323 chars, table 1x/351 chars, markup 175x/558 chars, heading 10x/805 chars.
- /home/jeltz/aIware/drafts/davos-target-list.md (md): 10364 raw chars -> 6660 chars of prose (938 words). Removed: code 2x/21 chars, table 2x/2849 chars, markup 77x/220 chars, heading 13x/563 chars.
- /home/jeltz/aIware/drafts/kanai-iccr-vs-fmt-comparison-2026-07-28.md (md): 9732 raw chars -> 8902 chars of prose (1223 words). Removed: code 1x/35 chars, markup 86x/273 chars, heading 8x/366 chars.
- /home/jeltz/aIware/drafts/moc7-accommodation-shortlist.md (md): 10404 raw chars -> 8188 chars of prose (1419 words). Removed: comment 2x/52 chars, table 1x/1335 chars, markup 182x/524 chars, heading 6x/224 chars.
- /home/jeltz/aIware/drafts/moc7-handout-a4.md (md): 7865 raw chars -> 4948 chars of prose (716 words). Removed: front_matter 1x/318 chars, math 11x/288 chars, table 3x/1829 chars, image 1x/23 chars, link 2x/82 chars, markup 44x/133 chars, heading 7x/196 chars.
- /home/jeltz/aIware/drafts/moc7-poster-content.md (md): 15340 raw chars -> 8290 chars of prose (1278 words). Removed: comment 9x/2413 chars, code 17x/503 chars, table 4x/3351 chars, url 2x/80 chars, markup 81x/246 chars, heading 10x/363 chars.
- /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md (md): 19944 raw chars -> 17801 chars of prose (2731 words). Removed: bibliography 1x/1603 chars, markup 29x/78 chars, heading 9x/443 chars.
- /home/jeltz/aIware/drafts/noc-reference-repairs-for-mg.md (md): 4038 raw chars -> 3195 chars of prose (547 words). Removed: code 29x/423 chars, markup 40x/131 chars, heading 4x/255 chars.
- /home/jeltz/aIware/drafts/pitch-aeon.md (md): 5208 raw chars -> 5042 chars of prose (777 words). Removed: url 1x/30 chars, markup 27x/83 chars, heading 3x/42 chars.
- /home/jeltz/aIware/drafts/pitch-nautilus.md (md): 5103 raw chars -> 4939 chars of prose (700 words). Removed: math 1x/7 chars, url 1x/30 chars, markup 20x/64 chars, heading 3x/52 chars.
- /home/jeltz/aIware/drafts/podcast-script-event-horizon-v2.md (md): 33601 raw chars -> 33533 chars of prose (5599 words). Removed: markup 32x/65 chars.
- /home/jeltz/aIware/drafts/podcast-simulation-you-call-i.md (md): 34881 raw chars -> 33930 chars of prose (5906 words). Removed: markup 275x/876 chars, heading 1x/56 chars.
- /home/jeltz/aIware/drafts/return-vs-closure-vocabulary-ruling.md (md): 8755 raw chars -> 6626 chars of prose (1095 words). Removed: code 27x/316 chars, table 2x/897 chars, markup 84x/256 chars, heading 11x/625 chars.
- /home/jeltz/aIware/drafts/rim-edwards-deyoung-cite.md (md): 3490 raw chars -> 3093 chars of prose (414 words). Removed: code 1x/38 chars, url 1x/36 chars, markup 17x/42 chars, heading 5x/273 chars.
- /home/jeltz/aIware/drafts/rim-motivation-revision.md (md): 8417 raw chars -> 8102 chars of prose (1104 words). Removed: code 1x/29 chars, markup 40x/112 chars, heading 5x/154 chars.
- /home/jeltz/aIware/drafts/rim-priorart-citations-verification.md (md): 10662 raw chars -> 9362 chars of prose (1263 words). Removed: url 6x/218 chars, markup 107x/306 chars, heading 12x/704 chars.
- /home/jeltz/aIware/drafts/rim-priorart-convergence.md (md): 6332 raw chars -> 4719 chars of prose (669 words). Removed: code 5x/115 chars, bibliography 1x/1085 chars, markup 34x/103 chars, heading 4x/296 chars.
- /home/jeltz/aIware/drafts/sjalv-manual-brief-for-perplexity.md (md): 24120 raw chars -> 17915 chars of prose (2952 words). Removed: comment 3x/215 chars, code 2x/123 chars, table 6x/3777 chars, url 2x/78 chars, markup 148x/492 chars, heading 27x/1243 chars.
- /home/jeltz/aIware/drafts/styropyro-note.md (md): 2155 raw chars -> 2020 chars of prose (346 words). Removed: code 1x/8 chars, url 1x/40 chars, markup 9x/21 chars, heading 1x/59 chars.
- /home/jeltz/aIware/drafts/translation-nl-el-ko/control/culture-guide-el.md (md): 6772 raw chars -> 6243 chars of prose (965 words). Removed: code 1x/4 chars, markup 66x/202 chars, heading 7x/223 chars.
- /home/jeltz/aIware/drafts/translation-nl-el-ko/control/culture-guide-ko.md (md): 3734 raw chars -> 3323 chars of prose (770 words). Removed: code 1x/4 chars, markup 61x/182 chars, heading 7x/137 chars.
- /home/jeltz/aIware/drafts/translation-nl-el-ko/control/culture-guide-nl.md (md): 6838 raw chars -> 6412 chars of prose (1000 words). Removed: code 2x/9 chars, markup 61x/184 chars, heading 7x/223 chars.
- /home/jeltz/aIware/drafts/translation-nl-el-ko/control/glossary-el.md (md): 10219 raw chars -> 4703 chars of prose (700 words). Removed: table 3x/4898 chars, markup 46x/145 chars, heading 6x/401 chars.
- /home/jeltz/aIware/drafts/translation-nl-el-ko/control/glossary-ko.md (md): 5748 raw chars -> 2169 chars of prose (451 words). Removed: table 3x/3197 chars, markup 34x/105 chars, heading 6x/219 chars.
- /home/jeltz/aIware/drafts/translation-nl-el-ko/control/glossary-nl.md (md): 10067 raw chars -> 4148 chars of prose (603 words). Removed: table 3x/5337 chars, markup 48x/155 chars, heading 6x/409 chars.
- /home/jeltz/aIware/paper/aiw47/aiw47-eneuro-opinion.md (md): 28101 raw chars -> 21996 chars of prose (3194 words). Removed: front_matter 1x/136 chars, comment 1x/348 chars, bibliography 1x/3959 chars, table 1x/996 chars, image 2x/56 chars, markup 76x/176 chars, heading 10x/408 chars.
- /home/jeltz/aIware/paper/cc/four-model-theory-cc.md (md): 93066 raw chars -> 70929 chars of prose (9793 words). Removed: bibliography 1x/15996 chars, table 4x/2520 chars, link 1x/365 chars, footnote 1x/10 chars, markup 205x/674 chars, heading 64x/2400 chars.
- /home/jeltz/aIware/paper/cmb_mfdfa/cmb-mfdfa.md (md): 45204 raw chars -> 35508 chars of prose (5121 words). Removed: code 6x/114 chars, bibliography 1x/5583 chars, table 7x/2566 chars, url 3x/82 chars, markup 59x/181 chars, heading 32x/1088 chars.
- /home/jeltz/aIware/paper/cosmology/perplexity literature findings.md (md): 28031 raw chars -> 15613 chars of prose (2173 words). Removed: bibliography 1x/9028 chars, table 1x/1433 chars, link 10x/64 chars, footnote 41x/192 chars, markup 142x/430 chars, heading 25x/1207 chars.
- /home/jeltz/aIware/paper/cosmology/sb-hc4a.md (md): 198495 raw chars -> 173783 chars of prose (25757 words). Removed: bibliography 1x/19094 chars, math 1x/19 chars, table 3x/1920 chars, markup 351x/991 chars, heading 60x/2534 chars.
- /home/jeltz/aIware/paper/cosmology_formal/sb-hc4a-formalization.md (md): 120033 raw chars -> 104639 chars of prose (15089 words). Removed: bibliography 1x/8983 chars, table 4x/2528 chars, markup 413x/1080 chars, heading 66x/2637 chars.
- /home/jeltz/aIware/paper/fmt_formal/fmt-formalization.md (md): 90744 raw chars -> 79556 chars of prose (11555 words). Removed: bibliography 1x/6647 chars, table 2x/1297 chars, citation 5x/27 chars, markup 332x/846 chars, heading 53x/2225 chars.
- /home/jeltz/aIware/paper/fmt_permeability_criticality/fmt-permeability-criticality.md (md): 24872 raw chars -> 19608 chars of prose (2788 words). Removed: bibliography 1x/2422 chars, table 1x/1253 chars, citation 1x/5 chars, markup 175x/427 chars, heading 24x/1088 chars.
- /home/jeltz/aIware/paper/full/four-model-theory-full-tracked.md (md): 147009 raw chars -> 123067 chars of prose (17093 words). Removed: comment 16x/1880 chars, code 5x/39 chars, bibliography 1x/14478 chars, table 5x/3112 chars, link 1x/365 chars, footnote 1x/10 chars, markup 356x/1147 chars, heading 70x/2705 chars.
- /home/jeltz/aIware/paper/full/four-model-theory-full.md (md): 372265 raw chars -> 321294 chars of prose (45726 words). Removed: bibliography 1x/39118 chars, table 6x/5435 chars, image 3x/920 chars, footnote 7x/25 chars, markup 661x/1890 chars, heading 82x/3370 chars.
- /home/jeltz/aIware/paper/intelligence/literature-research.md (md): 9922 raw chars -> 7565 chars of prose (1043 words). Removed: code 9x/259 chars, table 1x/1402 chars, markup 71x/240 chars, heading 9x/433 chars.
- /home/jeltz/aIware/paper/intelligence/paper.md (md): 119568 raw chars -> 100433 chars of prose (14590 words). Removed: comment 1x/477 chars, bibliography 1x/16777 chars, markup 134x/356 chars, heading 37x/1406 chars.
- /home/jeltz/aIware/paper/rim_formal/rim-formalization.md (md): 44522 raw chars -> 35400 chars of prose (4898 words). Removed: bibliography 1x/2644 chars, math 23x/2608 chars, table 2x/1450 chars, citation 9x/38 chars, markup 168x/479 chars, heading 47x/1735 chars.
- /home/jeltz/aIware/paper/seth-commentary/seth-commentary.md (md): 10477 raw chars -> 7923 chars of prose (1086 words). Removed: front_matter 1x/963 chars, bibliography 1x/1576 chars, markup 6x/12 chars.
- /home/jeltz/aIware/paper/trimmed/noc/SUBMISSION-CHECKLIST.md (md): 3452 raw chars -> 2604 chars of prose (352 words). Removed: code 10x/332 chars, math 1x/10 chars, citation 2x/13 chars, url 2x/64 chars, markup 79x/257 chars, heading 7x/150 chars.
- /home/jeltz/aIware/paper/trimmed/noc/figure-alt-text.md (md): 5251 raw chars -> 5018 chars of prose (740 words). Removed: markup 10x/29 chars, heading 5x/187 chars.
- /home/jeltz/aIware/paper/trimmed/noc/four-model-theory-noc.md (md): 85541 raw chars -> 64804 chars of prose (9018 words). Removed: comment 3x/365 chars, bibliography 1x/14139 chars, table 4x/2523 chars, link 1x/365 chars, footnote 1x/10 chars, markup 208x/682 chars, heading 66x/2474 chars.
- /home/jeltz/aIware/paper/trimmed/noc/highlights.md (md): 1284 raw chars -> 1259 chars of prose (155 words). Removed: markup 5x/10 chars, heading 1x/12 chars.
