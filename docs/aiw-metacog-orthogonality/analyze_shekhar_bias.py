"""Reproduce the PUBLISHED Shekhar & Rahnev (2018) dissociation:
'DLPFC TMS decreased mean confidence without affecting metacognitive scores.'

This is itself a perception-vs-metacognition COMPONENT dissociation: a
metacognitive-bias change (mean confidence) dissociated from both type-1 d'
and type-2 sensitivity (meta-d'/M-ratio). We compute mean confidence per
subject x site and test DLPFC vs S1, alongside the d'/meta-d' nulls already
found. If mean-confidence drops under DLPFC while d' and meta-d' do not, we
have reproduced a real, published double-dissociation of components on open
data -- directly supporting the FMT claim that perception and the
self-monitoring layer are separable.
"""
import csv
import statistics as stats
from analyze_shekhar import paired_t

CSV = "/home/jeltz/aIware/tmp/aiw47-data/conf-db/data_Shekhar_2018.csv"
SITE = {"1": "S1_control", "2": "DLPFC", "3": "aPFC"}


def main():
    rows = list(csv.DictReader(open(CSV, newline="")))
    subs = sorted(set(r["Subj_idx"] for r in rows), key=lambda x: float(x))
    sites = ["1", "2", "3"]
    meanconf = {s: {} for s in subs}
    for s in subs:
        for st in sites:
            confs = [float(r["Confidence"]) for r in rows
                     if r["Subj_idx"] == s and r["TMSsite"] == st]
            meanconf[s][st] = stats.mean(confs)

    print("=== MEAN CONFIDENCE by site (N={}) ===".format(len(subs)))
    for st in sites:
        x = [meanconf[s][st] for s in subs]
        print(f"  {SITE[st]:>12}: mean_conf={stats.mean(x):.3f} (sd {stats.stdev(x):.3f})")

    print("\n=== PAIRED: mean confidence, site vs S1 control ===")
    for st in ("2", "3"):
        x = [meanconf[s][st] for s in subs]
        y = [meanconf[s]["1"] for s in subs]
        r = paired_t(x, y)
        print(f"  {SITE[st]:>6} vs S1: delta={r['mean']:+.3f}  "
              f"t({r['df']})={r['t']:.2f}  p={r['p']:.4f}  dz={r['dz']:+.3f}")


if __name__ == "__main__":
    main()
