"""EWM-axis test: a difficulty (stimulus-contrast) manipulation should move
first-order sensitivity d' (the EWM discriminating the world) while leaving
metacognitive efficiency M-ratio (the ESM reading out the EWM) approximately
invariant. This is the world-model half of the FMT ESM/EWM double dissociation.

Datasets (Confidence Database, OSF s46pr): Rahnev_2013 (2-pt confidence -> meta-d'
weakly identified, EXPLORATORY) and Shekhar_2018 (4-pt confidence, primary).
Per (subject x contrast level) d'/meta-d'/M-ratio via the validated Maniscalco-Lau
MLE (metad_mle, 4 passing tests). Within-subject contrast effect = highest vs
lowest contrast level, paired.
"""
import csv
import statistics as stats
import metad_mle as M
from analyze_shekhar import paired_t


def fit(trials, nratings):
    stim, resp, rat = [], [], []
    correct = 0
    for t in trials:
        if t["Response"] in ("NaN", "nan", "") or t["Confidence"] in ("NaN", "nan", ""):
            continue
        s = int(float(t["Stimulus"])); r = int(float(t["Response"])); c = int(float(t["Confidence"]))
        stim.append(s - 1); resp.append(r - 1); rat.append(c)
        if s == r:
            correct += 1
    n = len(stim)
    if n < 20:
        return None
    nR_S1, nR_S2 = M.trials2counts(stim, resp, rat, nratings)
    meta_d, d1, c1 = M.fit_meta_d(nR_S1, nR_S2)
    return {"dprime": d1, "metad": meta_d,
            "mratio": meta_d / d1 if d1 else float("nan"),
            "acc": correct / n, "n": n}


def run(path, nratings, label):
    rows = list(csv.DictReader(open(path, newline="")))
    levels = sorted(set(r["Contrast"] for r in rows), key=lambda x: float(x))
    subs = sorted(set(r["Subj_idx"] for r in rows), key=lambda x: float(x))
    res = {}
    for s in subs:
        res[s] = {}
        for lv in levels:
            tr = [r for r in rows if r["Subj_idx"] == s and r["Contrast"] == lv]
            res[s][lv] = fit(tr, nratings)

    print(f"\n========== {label}  (N={len(subs)}, contrast levels {levels}, "
          f"{nratings}-pt confidence) ==========")
    print("=== GROUP MEANS by contrast level ===")
    for lv in levels:
        good = [res[s][lv] for s in subs if res[s][lv]]
        dp = [g["dprime"] for g in good]; md = [g["metad"] for g in good]
        mr = [g["mratio"] for g in good if g["mratio"] == g["mratio"]]
        ac = [g["acc"] for g in good]
        print(f"  contrast {lv}: n={len(good):3d}  acc={stats.mean(ac):.3f}  "
              f"d'={stats.mean(dp):.3f}  meta-d'={stats.mean(md):.3f}  "
              f"M-ratio={stats.mean(mr):.3f}")

    lo, hi = levels[0], levels[-1]
    paired = [s for s in subs if res[s][lo] and res[s][hi]
              and res[s][lo]["mratio"] == res[s][lo]["mratio"]
              and res[s][hi]["mratio"] == res[s][hi]["mratio"]]
    print(f"\n=== WITHIN-SUBJECT EWM-axis CONTRAST: highest({hi}) vs lowest({lo}), "
          f"n_paired={len(paired)} ===")
    if len(paired) < 3:
        print("  [between-subject titrated contrast: no within-subject pairing -> "
              "see cross-sectional M-ratio vs d' invariance in the group means above]")
        return
    for metric, lab in (("dprime", "d'      "), ("metad", "meta-d' "), ("mratio", "M-ratio ")):
        x = [res[s][hi][metric] for s in paired]
        y = [res[s][lo][metric] for s in paired]
        r = paired_t(x, y)
        print(f"  {lab}: hi={stats.mean(x):.3f} lo={stats.mean(y):.3f} "
              f"delta={r['mean']:+.3f}  t({r['df']})={r['t']:.2f}  "
              f"p={r['p']:.4f}  dz={r['dz']:+.3f}")
    print("  FMT/EWM-axis expectation: d' rises strongly with contrast (manipulation "
          "check); M-ratio ~ flat (metacognitive efficiency invariant to difficulty).")


if __name__ == "__main__":
    run("conf-db/data_Shekhar_2018.csv", 4, "Shekhar_2018 (PRIMARY, 4-pt)")
    run("conf-db/data_Rahnev_2013.csv", 2, "Rahnev_2013 (EXPLORATORY, 2-pt)")
