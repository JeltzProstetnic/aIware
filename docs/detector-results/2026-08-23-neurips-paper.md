# Detector exposure — neurips-ai-and-the-self-2026.md

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
| chunks scored | 8 |
| sources | 1 |
| generated | 2026-08-23T21:02:29+00:00 |
| window | 320 |
| unit | words |
| corpus_files | 1 |

### Chunk score distribution — this artifact

n = 8 chunks

| min | p05 | q1 | median | q3 | p95 | max | mean | sd |
|---|---|---|---|---|---|---|---|---|
| 1.0107 | 1.0143 | 1.0286 | 1.0414 | 1.0513 | 1.0655 | 1.0726 | 1.0402 | 0.0196 |

> ⚠ Language mismatch: the control corpus is de and this artifact is unknown. Binoculars is English-tuned, so the distribution shifts and the two are not directly comparable (research doc §7).

### Control corpus (de, 284 chunks)

n = 284 chunks

| min | p05 | q1 | median | q3 | p95 | max | mean | sd |
|---|---|---|---|---|---|---|---|---|
| 0.7269 | 0.9491 | 0.9737 | 0.9887 | 1.0060 | 1.0380 | 1.0542 | 0.9887 | 0.0308 |

### Flag rates

| Threshold | where it comes from | control chunks flagged | artifact chunks flagged |
|---|---|---|---|
| 0.8536 | Binoculars published low-FPR threshold | 0.4% | 0.0% |
| 0.9015 | Binoculars published accuracy threshold | 0.4% | 0.0% |
| 0.9491 | this control corpus at a 5% flag rate | 4.9% | 0.0% |
| 0.9144 | this control corpus at a 1% flag rate | 0.7% | 0.0% |

Read each row as: at this threshold, k% of the author's known-human control chunks are flagged and j% of this artifact's chunks are flagged. The left-hand column is a property of the author's style; the right-hand column is a property of this text.

### Position relative to the control

- The artifact median (1.0414) sits at the 96th percentile of the control distribution.
- 0 of 8 artifact chunks fall past the control 5th percentile (0.9491).

### Per-chunk scores

| # | source | units | score | past control p05 |
|---|---|---|---|---|
| 0 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0210 | no |
| 1 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0311 | no |
| 2 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0508 | no |
| 3 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0468 | no |
| 4 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0107 | no |
| 5 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0360 | no |
| 6 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0726 | no |
| 7 | /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md | 320 | 1.0525 | no |

## Sources

- /home/jeltz/aIware/drafts/neurips-ai-and-the-self-2026.md (md): 19944 raw chars -> 17801 chars of prose (2731 words). Removed: bibliography 1x/1603 chars, markup 29x/78 chars, heading 9x/443 chars.
