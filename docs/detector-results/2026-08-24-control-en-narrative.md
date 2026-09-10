# Detector exposure — control-en

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
| chunks scored | 319 |
| sources | 3 |
| generated | 2026-08-24T10:39:11+00:00 |
| window | 320 |
| unit | words |
| corpus_files | 3 |

### Chunk score distribution — this artifact

n = 319 chunks

| min | p05 | q1 | median | q3 | p95 | max | mean | sd |
|---|---|---|---|---|---|---|---|---|
| 0.8872 | 0.9320 | 0.9636 | 0.9837 | 1.0059 | 1.0321 | 1.0802 | 0.9836 | 0.0313 |

> ⚠ No control corpus was supplied, so this run cannot state a flag rate. Scores below are raw and mean nothing on their own (research doc §7).

> ⚠ This run defined the control corpus and wrote it to tmp/detector/control-en-calibration.json. Comparing it against itself would be circular, so no flag rates are shown here.

### Control corpus

None. Without known-human prose by the same author there is no baseline, so this run cannot say whether these scores are unusual.

### Per-chunk scores

| # | source | units | score |
|---|---|---|---|
| 0 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9739 |
| 1 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9669 |
| 2 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9723 |
| 3 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9761 |
| 4 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9259 |
| 5 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9891 |
| 6 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0056 |
| 7 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9593 |
| 8 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9785 |
| 9 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9538 |
| 10 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9844 |
| 11 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9923 |
| 12 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9550 |
| 13 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9116 |
| 14 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9459 |
| 15 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9946 |
| 16 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9349 |
| 17 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0151 |
| 18 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9346 |
| 19 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9484 |
| 20 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0011 |
| 21 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9383 |
| 22 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0342 |
| 23 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9649 |
| 24 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9989 |
| 25 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9435 |
| 26 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9454 |
| 27 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9791 |
| 28 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0041 |
| 29 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9456 |
| 30 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9430 |
| 31 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9587 |
| 32 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9250 |
| 33 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0533 |
| 34 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9539 |
| 35 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0118 |
| 36 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0291 |
| 37 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0373 |
| 38 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9828 |
| 39 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0629 |
| 40 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0037 |
| 41 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9931 |
| 42 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0113 |
| 43 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9797 |
| 44 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0026 |
| 45 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0489 |
| 46 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9759 |
| 47 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9763 |
| 48 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9691 |
| 49 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9797 |
| 50 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0204 |
| 51 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9701 |
| 52 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9808 |
| 53 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0297 |
| 54 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9626 |
| 55 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9856 |
| 56 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0410 |
| 57 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9551 |
| 58 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9968 |
| 59 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0202 |
| 60 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9709 |
| 61 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0242 |
| 62 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9929 |
| 63 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0152 |
| 64 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9884 |
| 65 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0079 |
| 66 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9896 |
| 67 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0080 |
| 68 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9516 |
| 69 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9745 |
| 70 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9609 |
| 71 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0046 |
| 72 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0094 |
| 73 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0155 |
| 74 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9761 |
| 75 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0245 |
| 76 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9777 |
| 77 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9942 |
| 78 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0176 |
| 79 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9574 |
| 80 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0057 |
| 81 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9959 |
| 82 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9873 |
| 83 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0149 |
| 84 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9686 |
| 85 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9938 |
| 86 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9276 |
| 87 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9742 |
| 88 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9248 |
| 89 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9944 |
| 90 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0136 |
| 91 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9762 |
| 92 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9809 |
| 93 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0222 |
| 94 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 1.0032 |
| 95 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx | 320 | 0.9802 |
| 96 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9415 |
| 97 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9661 |
| 98 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0253 |
| 99 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0118 |
| 100 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0266 |
| 101 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9902 |
| 102 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9728 |
| 103 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9620 |
| 104 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9664 |
| 105 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0099 |
| 106 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9622 |
| 107 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0114 |
| 108 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9790 |
| 109 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0240 |
| 110 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9567 |
| 111 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9806 |
| 112 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9641 |
| 113 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9620 |
| 114 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9128 |
| 115 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9509 |
| 116 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9895 |
| 117 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9321 |
| 118 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9773 |
| 119 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9540 |
| 120 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9390 |
| 121 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9373 |
| 122 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9680 |
| 123 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9733 |
| 124 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9421 |
| 125 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9862 |
| 126 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0125 |
| 127 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9701 |
| 128 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.8872 |
| 129 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9877 |
| 130 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9338 |
| 131 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9734 |
| 132 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0407 |
| 133 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0711 |
| 134 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0354 |
| 135 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9430 |
| 136 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9159 |
| 137 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9507 |
| 138 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9893 |
| 139 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9932 |
| 140 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9926 |
| 141 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9681 |
| 142 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0270 |
| 143 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9004 |
| 144 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9841 |
| 145 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9691 |
| 146 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0182 |
| 147 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9245 |
| 148 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0112 |
| 149 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9858 |
| 150 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0249 |
| 151 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9918 |
| 152 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9749 |
| 153 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9551 |
| 154 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9658 |
| 155 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9689 |
| 156 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9377 |
| 157 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9386 |
| 158 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0114 |
| 159 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9626 |
| 160 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9609 |
| 161 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9657 |
| 162 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9848 |
| 163 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9668 |
| 164 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9602 |
| 165 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9742 |
| 166 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0006 |
| 167 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0074 |
| 168 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 0.9960 |
| 169 | /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx | 320 | 1.0121 |
| 170 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9673 |
| 171 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9576 |
| 172 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0300 |
| 173 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9830 |
| 174 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9911 |
| 175 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9940 |
| 176 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0265 |
| 177 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9968 |
| 178 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9994 |
| 179 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0083 |
| 180 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9855 |
| 181 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0181 |
| 182 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0317 |
| 183 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9898 |
| 184 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9518 |
| 185 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9758 |
| 186 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9680 |
| 187 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0220 |
| 188 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0085 |
| 189 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9830 |
| 190 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9658 |
| 191 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9809 |
| 192 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0110 |
| 193 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9757 |
| 194 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0313 |
| 195 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0169 |
| 196 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9640 |
| 197 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9551 |
| 198 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9731 |
| 199 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0130 |
| 200 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9935 |
| 201 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0355 |
| 202 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0150 |
| 203 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9747 |
| 204 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9891 |
| 205 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0157 |
| 206 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9728 |
| 207 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9837 |
| 208 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9564 |
| 209 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9730 |
| 210 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9921 |
| 211 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0061 |
| 212 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9944 |
| 213 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0243 |
| 214 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9563 |
| 215 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0066 |
| 216 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9688 |
| 217 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0208 |
| 218 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9722 |
| 219 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0248 |
| 220 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0464 |
| 221 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0802 |
| 222 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9971 |
| 223 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0004 |
| 224 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0039 |
| 225 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9985 |
| 226 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9837 |
| 227 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0081 |
| 228 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0192 |
| 229 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9486 |
| 230 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0274 |
| 231 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9565 |
| 232 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0060 |
| 233 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9370 |
| 234 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9896 |
| 235 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9983 |
| 236 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9692 |
| 237 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9445 |
| 238 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9963 |
| 239 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9930 |
| 240 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0338 |
| 241 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9708 |
| 242 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9573 |
| 243 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9461 |
| 244 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9832 |
| 245 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9710 |
| 246 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0127 |
| 247 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0526 |
| 248 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9573 |
| 249 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9307 |
| 250 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9413 |
| 251 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9917 |
| 252 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9601 |
| 253 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9704 |
| 254 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9831 |
| 255 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9919 |
| 256 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0538 |
| 257 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9656 |
| 258 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0175 |
| 259 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9834 |
| 260 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0319 |
| 261 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9935 |
| 262 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9665 |
| 263 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9880 |
| 264 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9887 |
| 265 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9813 |
| 266 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9508 |
| 267 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0152 |
| 268 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9930 |
| 269 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0195 |
| 270 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9876 |
| 271 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9709 |
| 272 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9944 |
| 273 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9713 |
| 274 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9854 |
| 275 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9474 |
| 276 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9631 |
| 277 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9742 |
| 278 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9266 |
| 279 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9478 |
| 280 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9631 |
| 281 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9113 |
| 282 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9606 |
| 283 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9220 |
| 284 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0026 |
| 285 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9615 |
| 286 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9870 |
| 287 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9814 |
| 288 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9921 |
| 289 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9814 |
| 290 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9730 |
| 291 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0029 |
| 292 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9110 |
| 293 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0061 |
| 294 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9910 |
| 295 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9673 |
| 296 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9493 |
| 297 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9837 |
| 298 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0192 |
| 299 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9908 |
| 300 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9153 |
| 301 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0232 |
| 302 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9988 |
| 303 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9877 |
| 304 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9753 |
| 305 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9875 |
| 306 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0420 |
| 307 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9540 |
| 308 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9701 |
| 309 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9510 |
| 310 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0079 |
| 311 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9854 |
| 312 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0077 |
| 313 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9935 |
| 314 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9520 |
| 315 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9917 |
| 316 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9958 |
| 317 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 1.0033 |
| 318 | /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx | 320 | 0.9782 |

## Sources

- /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/8PWC BLACK BOOK/Eight Pattern Wing Chun Kuen/8PWC.hardcover.en.docx (docx): 176354 raw chars -> 176259 chars of prose (30935 words). Removed: table 500x/167842 chars, markup 20x/71 chars, heading 126x/1978 chars. 1820 DOCX paragraphs.
- /mnt/wsl/data8tb/__FMS__/Creative/_8pwc/unordered/8PWCS/8PWCS.docx (docx): 140481 raw chars -> 140169 chars of prose (23854 words). Removed: table 1x/590 chars, url 1x/14 chars, markup 26x/277 chars, heading 56x/1038 chars. 607 DOCX paragraphs.
- /mnt/wsl/data8tb/__FMS__/Creative/_Roman/_X2/The Billion Year Countdown.docx (docx): 267326 raw chars -> 267277 chars of prose (47805 words). Removed: table 3x/13019 chars, url 1x/22 chars, markup 4x/8 chars, heading 20x/316 chars. 1043 DOCX paragraphs.
