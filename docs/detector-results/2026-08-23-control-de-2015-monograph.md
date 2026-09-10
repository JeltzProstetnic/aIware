# Detector exposure — control

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
| chunks scored | 284 |
| sources | 1 |
| generated | 2026-08-23T21:02:17+00:00 |
| window | 320 |
| unit | words |
| corpus_files | 1 |

### Chunk score distribution — this artifact

n = 284 chunks

| min | p05 | q1 | median | q3 | p95 | max | mean | sd |
|---|---|---|---|---|---|---|---|---|
| 0.7269 | 0.9491 | 0.9737 | 0.9887 | 1.0060 | 1.0380 | 1.0542 | 0.9887 | 0.0308 |

> ⚠ No control corpus was supplied, so this run cannot state a flag rate. Scores below are raw and mean nothing on their own (research doc §7).

> ⚠ This run defined the control corpus and wrote it to /home/jeltz/aIware/tmp/detector/control.json. Comparing it against itself would be circular, so no flag rates are shown here.

### Control corpus

None. Without known-human prose by the same author there is no baseline, so this run cannot say whether these scores are unusual.

### Per-chunk scores

| # | source | units | score |
|---|---|---|---|
| 0 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9254 |
| 1 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9387 |
| 2 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0142 |
| 3 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9635 |
| 4 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0416 |
| 5 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0024 |
| 6 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9803 |
| 7 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9813 |
| 8 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9802 |
| 9 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9492 |
| 10 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9742 |
| 11 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9653 |
| 12 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9911 |
| 13 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9754 |
| 14 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9741 |
| 15 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9144 |
| 16 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9875 |
| 17 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9760 |
| 18 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9962 |
| 19 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9862 |
| 20 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9823 |
| 21 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9957 |
| 22 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0119 |
| 23 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0213 |
| 24 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9992 |
| 25 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0064 |
| 26 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0400 |
| 27 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0064 |
| 28 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0053 |
| 29 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9900 |
| 30 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9810 |
| 31 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0510 |
| 32 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9714 |
| 33 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9940 |
| 34 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0303 |
| 35 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9836 |
| 36 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9509 |
| 37 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9618 |
| 38 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9770 |
| 39 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9593 |
| 40 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9245 |
| 41 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9834 |
| 42 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9837 |
| 43 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9887 |
| 44 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9985 |
| 45 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9855 |
| 46 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9907 |
| 47 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9924 |
| 48 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9781 |
| 49 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9956 |
| 50 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0174 |
| 51 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0280 |
| 52 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9694 |
| 53 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0137 |
| 54 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9859 |
| 55 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9832 |
| 56 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9738 |
| 57 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0398 |
| 58 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9848 |
| 59 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9325 |
| 60 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9592 |
| 61 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9575 |
| 62 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9557 |
| 63 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9351 |
| 64 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9538 |
| 65 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9261 |
| 66 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9891 |
| 67 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9946 |
| 68 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9642 |
| 69 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0003 |
| 70 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9813 |
| 71 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0317 |
| 72 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9930 |
| 73 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9909 |
| 74 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9843 |
| 75 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9719 |
| 76 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0056 |
| 77 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9877 |
| 78 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9874 |
| 79 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0150 |
| 80 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9745 |
| 81 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9895 |
| 82 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0004 |
| 83 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9905 |
| 84 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9782 |
| 85 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.7269 |
| 86 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0411 |
| 87 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9785 |
| 88 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0211 |
| 89 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0168 |
| 90 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9736 |
| 91 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9824 |
| 92 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9919 |
| 93 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9210 |
| 94 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0334 |
| 95 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9854 |
| 96 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9767 |
| 97 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9977 |
| 98 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0165 |
| 99 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0313 |
| 100 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9981 |
| 101 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0150 |
| 102 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9638 |
| 103 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0044 |
| 104 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9953 |
| 105 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0005 |
| 106 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0380 |
| 107 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9647 |
| 108 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0159 |
| 109 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0055 |
| 110 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9973 |
| 111 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9491 |
| 112 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0126 |
| 113 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9832 |
| 114 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0064 |
| 115 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9743 |
| 116 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9882 |
| 117 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9926 |
| 118 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9986 |
| 119 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0387 |
| 120 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9596 |
| 121 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9839 |
| 122 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9942 |
| 123 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0303 |
| 124 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9733 |
| 125 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0231 |
| 126 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9758 |
| 127 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9929 |
| 128 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9782 |
| 129 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9748 |
| 130 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0101 |
| 131 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0101 |
| 132 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9891 |
| 133 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9592 |
| 134 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0421 |
| 135 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9744 |
| 136 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0065 |
| 137 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0124 |
| 138 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9952 |
| 139 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9615 |
| 140 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9838 |
| 141 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9811 |
| 142 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0215 |
| 143 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9696 |
| 144 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0159 |
| 145 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9629 |
| 146 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9952 |
| 147 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0104 |
| 148 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9880 |
| 149 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9519 |
| 150 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9853 |
| 151 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0014 |
| 152 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9820 |
| 153 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0057 |
| 154 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9735 |
| 155 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9809 |
| 156 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9689 |
| 157 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9797 |
| 158 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9991 |
| 159 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0001 |
| 160 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9710 |
| 161 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0422 |
| 162 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9835 |
| 163 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9782 |
| 164 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9948 |
| 165 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9937 |
| 166 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0080 |
| 167 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0066 |
| 168 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9510 |
| 169 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9744 |
| 170 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9690 |
| 171 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9216 |
| 172 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9678 |
| 173 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0302 |
| 174 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0380 |
| 175 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9805 |
| 176 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9978 |
| 177 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9649 |
| 178 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0432 |
| 179 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9735 |
| 180 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0235 |
| 181 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0058 |
| 182 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0038 |
| 183 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9668 |
| 184 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0091 |
| 185 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9720 |
| 186 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9957 |
| 187 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0203 |
| 188 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0167 |
| 189 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0301 |
| 190 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9851 |
| 191 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9990 |
| 192 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9955 |
| 193 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0263 |
| 194 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0022 |
| 195 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9769 |
| 196 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9693 |
| 197 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0099 |
| 198 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0536 |
| 199 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9773 |
| 200 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9815 |
| 201 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9602 |
| 202 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0093 |
| 203 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9816 |
| 204 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9998 |
| 205 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9703 |
| 206 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9967 |
| 207 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0084 |
| 208 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9897 |
| 209 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0112 |
| 210 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0019 |
| 211 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9889 |
| 212 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9818 |
| 213 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9479 |
| 214 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9704 |
| 215 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0249 |
| 216 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0026 |
| 217 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9990 |
| 218 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9677 |
| 219 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0089 |
| 220 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9885 |
| 221 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9608 |
| 222 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9771 |
| 223 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9811 |
| 224 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9837 |
| 225 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9785 |
| 226 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9887 |
| 227 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9859 |
| 228 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9672 |
| 229 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9668 |
| 230 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0465 |
| 231 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9510 |
| 232 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9884 |
| 233 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9560 |
| 234 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9953 |
| 235 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0203 |
| 236 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0120 |
| 237 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9907 |
| 238 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9947 |
| 239 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9210 |
| 240 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9658 |
| 241 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9675 |
| 242 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0123 |
| 243 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9764 |
| 244 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9740 |
| 245 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9662 |
| 246 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9971 |
| 247 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0465 |
| 248 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9723 |
| 249 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0174 |
| 250 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0283 |
| 251 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0192 |
| 252 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9528 |
| 253 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9608 |
| 254 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0198 |
| 255 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9950 |
| 256 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9865 |
| 257 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9710 |
| 258 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9751 |
| 259 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9962 |
| 260 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9998 |
| 261 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9066 |
| 262 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9558 |
| 263 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9956 |
| 264 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9969 |
| 265 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9937 |
| 266 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9912 |
| 267 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9693 |
| 268 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0542 |
| 269 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9841 |
| 270 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9836 |
| 271 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9527 |
| 272 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9627 |
| 273 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9978 |
| 274 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0174 |
| 275 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0326 |
| 276 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0209 |
| 277 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9846 |
| 278 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9958 |
| 279 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 0.9625 |
| 280 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0024 |
| 281 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0211 |
| 282 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 320 | 1.0432 |
| 283 | /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf | 253 | 0.9379 |

## Sources

- /home/jeltz/aIware/sources/book-2015/Die Emergenz des Bewusstseins 6x9 lit.pdf (pdf): 668378 raw chars -> 650612 chars of prose (90813 words). Removed: citation 1x/3 chars, url 13x/470 chars, markup 7x/14 chars. 299 PDF pages.
