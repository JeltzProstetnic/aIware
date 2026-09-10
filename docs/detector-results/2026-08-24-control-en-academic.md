# Detector exposure — control-en-academic

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
| chunks scored | 88 |
| sources | 2 |
| generated | 2026-08-24T10:48:12+00:00 |
| window | 320 |
| unit | words |
| corpus_files | 2 |

### Chunk score distribution — this artifact

n = 88 chunks

| min | p05 | q1 | median | q3 | p95 | max | mean | sd |
|---|---|---|---|---|---|---|---|---|
| 0.8541 | 0.8968 | 0.9275 | 0.9507 | 0.9750 | 1.0034 | 1.0167 | 0.9497 | 0.0349 |

### Control corpus (en, 319 chunks)

n = 319 chunks

| min | p05 | q1 | median | q3 | p95 | max | mean | sd |
|---|---|---|---|---|---|---|---|---|
| 0.8872 | 0.9320 | 0.9636 | 0.9837 | 1.0059 | 1.0321 | 1.0802 | 0.9836 | 0.0313 |

### Flag rates

| Threshold | where it comes from | control chunks flagged | artifact chunks flagged |
|---|---|---|---|
| 0.8536 | Binoculars published low-FPR threshold | 0.0% | 0.0% |
| 0.9015 | Binoculars published accuracy threshold | 0.6% | 8.0% |
| 0.9307 | this control corpus at a 5% flag rate | 4.7% | 28.4% |
| 0.9113 | this control corpus at a 1% flag rate | 0.9% | 10.2% |

Read each row as: at this threshold, k% of the author's known-human control chunks are flagged and j% of this artifact's chunks are flagged. The left-hand column is a property of the author's style; the right-hand column is a property of this text.

### Position relative to the control

- The artifact median (0.9507) sits at the 13th percentile of the control distribution.
- 27 of 88 artifact chunks fall past the control 5th percentile (0.9320).

### Per-chunk scores

| # | source | units | score | past control p05 |
|---|---|---|---|---|
| 0 | /home/jeltz/aIware/sources/book-2015/Holomatic Self Model Theory.docx | 320 | 0.9774 | no |
| 1 | /home/jeltz/aIware/sources/book-2015/Holomatic Self Model Theory.docx | 320 | 0.9411 | no |
| 2 | /home/jeltz/aIware/sources/book-2015/Holomatic Self Model Theory.docx | 320 | 0.9970 | no |
| 3 | /home/jeltz/aIware/sources/book-2015/Holomatic Self Model Theory.docx | 320 | 0.9830 | no |
| 4 | /home/jeltz/aIware/sources/book-2015/Holomatic Self Model Theory.docx | 320 | 1.0119 | no |
| 5 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9819 | no |
| 6 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9127 | yes |
| 7 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9278 | yes |
| 8 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9237 | yes |
| 9 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9605 | no |
| 10 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 1.0078 | no |
| 11 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9317 | yes |
| 12 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.8541 | yes |
| 13 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9238 | yes |
| 14 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.8959 | yes |
| 15 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9621 | no |
| 16 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9876 | no |
| 17 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9643 | no |
| 18 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9654 | no |
| 19 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9964 | no |
| 20 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9303 | yes |
| 21 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9836 | no |
| 22 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9916 | no |
| 23 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 1.0069 | no |
| 24 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9666 | no |
| 25 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9407 | no |
| 26 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9213 | yes |
| 27 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9416 | no |
| 28 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.8582 | yes |
| 29 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9182 | yes |
| 30 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9710 | no |
| 31 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9883 | no |
| 32 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9449 | no |
| 33 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9610 | no |
| 34 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9209 | yes |
| 35 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9351 | no |
| 36 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9641 | no |
| 37 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9708 | no |
| 38 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9594 | no |
| 39 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9436 | no |
| 40 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9146 | yes |
| 41 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9690 | no |
| 42 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 1.0167 | no |
| 43 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9667 | no |
| 44 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9576 | no |
| 45 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9349 | no |
| 46 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9265 | yes |
| 47 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9773 | no |
| 48 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9332 | no |
| 49 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9599 | no |
| 50 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9511 | no |
| 51 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9711 | no |
| 52 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9463 | no |
| 53 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.8985 | yes |
| 54 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.8599 | yes |
| 55 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9372 | no |
| 56 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9312 | yes |
| 57 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9159 | yes |
| 58 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.8711 | yes |
| 59 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9266 | yes |
| 60 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9226 | yes |
| 61 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9471 | no |
| 62 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9449 | no |
| 63 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9233 | yes |
| 64 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9320 | no |
| 65 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9099 | yes |
| 66 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9115 | yes |
| 67 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9756 | no |
| 68 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9510 | no |
| 69 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9668 | no |
| 70 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9868 | no |
| 71 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9412 | no |
| 72 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9505 | no |
| 73 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9891 | no |
| 74 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9968 | no |
| 75 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9516 | no |
| 76 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9003 | yes |
| 77 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9901 | no |
| 78 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9782 | no |
| 79 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9650 | no |
| 80 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9748 | no |
| 81 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 1.0083 | no |
| 82 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9043 | yes |
| 83 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9898 | no |
| 84 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9301 | yes |
| 85 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9347 | no |
| 86 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 320 | 0.9428 | no |
| 87 | /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx | 288 | 0.9619 | no |

## Sources

- /home/jeltz/aIware/sources/book-2015/Holomatic Self Model Theory.docx (docx): 10971 raw chars -> 10911 chars of prose (1683 words). Removed: citation 1x/4 chars, url 1x/54 chars, heading 1x/38 chars. 67 DOCX paragraphs.
- /mnt/c/Dropbox/DMS-Sync/Academic/publications-dissertation/_Dissertation/Dissertation.Full.Update2016.docx (docx): 179799 raw chars -> 177414 chars of prose (26528 words). Removed: table 1x/58 chars, citation 2x/6 chars, url 46x/1928 chars, markup 133x/174 chars, heading 104x/1687 chars. 1567 DOCX paragraphs.
