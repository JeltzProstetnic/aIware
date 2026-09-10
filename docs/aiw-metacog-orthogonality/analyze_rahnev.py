"""Rahnev_2013 (V1/Pz/sham TMS, pre/post) — secondary contrast.
Conditions: 1=pre_V1, 2=post_V1, 3=pre_Pz, 4=post_Pz, 5=pre_sham, 6=post_sham.
V1 TMS (post_V1 vs pre_V1) is expected to LOWER d' (perceptual). Question:
does it spare or also lower meta-d'? Confidence is only 2-point here, so
meta-d' is weakly identified -- treat as exploratory.
"""
import csv
import statistics as stats
import metad_mle as M
from analyze_shekhar import paired_t

CSV = "/home/jeltz/aIware/tmp/aiw47-data/conf-db/data_Rahnev_2013.csv"
COND = {"1": "pre_V1", "2": "post_V1", "3": "pre_Pz", "4": "post_Pz",
        "5": "pre_sham", "6": "post_sham"}
N_RATINGS = 2


def fit(trials):
    stim, resp, rat = [], [], []
    correct = n = 0
    for t in trials:
        if t["Response"] in ("NaN", "nan", "") or t["Confidence"] in ("NaN", "nan", ""):
            continue
        s = int(float(t["Stimulus"])); r = int(float(t["Response"])); c = int(float(t["Confidence"]))
        stim.append(s - 1); resp.append(r - 1); rat.append(c)
        n += 1
        if s == r:
            correct += 1
    nR_S1, nR_S2 = M.trials2counts(stim, resp, rat, N_RATINGS)
    meta_d, d1, c1 = M.fit_meta_d(nR_S1, nR_S2)
    return {"dprime": d1, "metad": meta_d,
            "mratio": meta_d / d1 if d1 else float("nan"),
            "acc": correct / n, "n": n}


def main():
    rows = list(csv.DictReader(open(CSV, newline="")))
    subs = sorted(set(r["Subj_idx"] for r in rows), key=lambda x: float(x))
    conds = ["1", "2", "3", "4", "5", "6"]
    res = {s: {} for s in subs}
    for s in subs:
        for c in conds:
            tr = [r for r in rows if r["Subj_idx"] == s and r["Condition"] == c]
            res[s][c] = fit(tr)

    print("=== GROUP MEANS by condition (N={}) ===".format(len(subs)))
    for c in conds:
        dp = [res[s][c]["dprime"] for s in subs]
        md = [res[s][c]["metad"] for s in subs]
        mr = [res[s][c]["mratio"] for s in subs]
        acc = [res[s][c]["acc"] for s in subs]
        print(f"  {COND[c]:>10}: acc={stats.mean(acc):.3f}  d'={stats.mean(dp):.3f}  "
              f"meta-d'={stats.mean(md):.3f}  M-ratio={stats.mean(mr):.3f}")

    print("\n=== KEY CONTRAST: post_V1 vs pre_V1 (within-subject) ===")
    for metric, lab in (("dprime", "d'      "), ("metad", "meta-d' "), ("mratio", "M-ratio ")):
        x = [res[s]["2"][metric] for s in subs]  # post_V1
        y = [res[s]["1"][metric] for s in subs]  # pre_V1
        r = paired_t(x, y)
        print(f"  {lab}: post={stats.mean(x):.3f} pre={stats.mean(y):.3f} "
              f"delta={r['mean']:+.3f}  t({r['df']})={r['t']:.2f}  p={r['p']:.4f}  dz={r['dz']:+.3f}")

    print("\n=== CONTROL CONTRAST: post_sham vs pre_sham ===")
    for metric, lab in (("dprime", "d'      "), ("metad", "meta-d' "), ("mratio", "M-ratio ")):
        x = [res[s]["6"][metric] for s in subs]
        y = [res[s]["5"][metric] for s in subs]
        r = paired_t(x, y)
        print(f"  {lab}: post={stats.mean(x):.3f} pre={stats.mean(y):.3f} "
              f"delta={r['mean']:+.3f}  t({r['df']})={r['t']:.2f}  p={r['p']:.4f}  dz={r['dz']:+.3f}")


if __name__ == "__main__":
    main()
