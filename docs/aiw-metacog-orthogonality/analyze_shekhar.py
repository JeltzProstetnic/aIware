"""AIW-47 self-test analysis on Shekhar & Rahnev (2018) TMS metacognition data
(Confidence Database, OSF s46pr). Pipeline rehearsal + dissociation test.

Per subject x TMS site (1=S1 [somatosensory control], 2=DLPFC, 3=aPFC) we
compute type-1 d' and meta-d' / M-ratio via the from-scratch Maniscalco-Lau MLE
(validated in test_metad_mle.py). Then within-subject paired comparisons.

Hypothesis frame (FMT): prefrontal (DLPFC/aPFC) TMS is an 'architectural'
perturbation -> should move metacognition (meta-d'/M-ratio) more than first-order
perception (d'). S1 is the perceptual/control site.
"""
import csv
import math
import statistics as stats
import metad_mle as M

CSV = "/home/jeltz/aIware/tmp/aiw47-data/conf-db/data_Shekhar_2018.csv"
SITE = {"1": "S1_control", "2": "DLPFC", "3": "aPFC"}
N_RATINGS = 4


def load():
    rows = []
    with open(CSV, newline="") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def fit_subject_site(trials):
    """trials: list of dicts with Stimulus, Response, Confidence (strings).
    Stimulus/Response in {1,2} -> map to {0,1}. Returns d', meta_d, mratio, acc, n."""
    stim, resp, rat = [], [], []
    correct = 0
    for t in trials:
        s = int(float(t["Stimulus"]))
        r = int(float(t["Response"]))
        c = int(float(t["Confidence"]))
        stim.append(s - 1)
        resp.append(r - 1)
        rat.append(c)
        if s == r:
            correct += 1
    n = len(stim)
    nR_S1, nR_S2 = M.trials2counts(stim, resp, rat, N_RATINGS)
    meta_d, d1, c1 = M.fit_meta_d(nR_S1, nR_S2)
    return {"dprime": d1, "metad": meta_d, "mratio": meta_d / d1 if d1 != 0 else float("nan"),
            "mdiff": meta_d - d1, "acc": correct / n, "n": n, "c1": c1}


def paired_t(x, y):
    """Paired t-test (x-y). Returns mean diff, t, df, two-sided p (via t-dist
    approx), Cohen's dz."""
    d = [a - b for a, b in zip(x, y)]
    n = len(d)
    m = stats.mean(d)
    sd = stats.stdev(d)
    se = sd / math.sqrt(n)
    t = m / se if se > 0 else float("nan")
    df = n - 1
    dz = m / sd if sd > 0 else float("nan")
    p = two_sided_p_t(t, df)
    return {"mean": m, "sd": sd, "t": t, "df": df, "p": p, "dz": dz, "n": n}


def two_sided_p_t(t, df):
    """Two-sided p-value for Student's t via the regularized incomplete beta.
    Pure stdlib."""
    t = abs(t)
    x = df / (df + t * t)
    p = betai(df / 2.0, 0.5, x)  # = 2*P(T>t) for two-sided
    return p


def betai(a, b, x):
    """Regularized incomplete beta I_x(a,b) (Numerical Recipes), stdlib only."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(lbeta + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return front * betacf(a, b, x) / a
    else:
        return 1 - front * betacf(b, a, 1 - x) / b


def betacf(a, b, x):
    MAXIT, EPS, FPMIN = 200, 3e-12, 1e-30
    qab, qap, qam = a + b, a + 1, a - 1
    c = 1.0
    d = 1 - qab * x / qap
    if abs(d) < FPMIN:
        d = FPMIN
    d = 1 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1 / d
        de = d * c
        h *= de
        if abs(de - 1) < EPS:
            break
    return h


def main():
    rows = load()
    subjects = sorted(set(r["Subj_idx"] for r in rows), key=lambda x: float(x))
    sites = ["1", "2", "3"]
    # results[subj][site] = metrics dict
    results = {}
    for s in subjects:
        results[s] = {}
        for site in sites:
            trials = [r for r in rows if r["Subj_idx"] == s and r["TMSsite"] == site]
            results[s][site] = fit_subject_site(trials)

    # per-subject table
    print("=== PER-SUBJECT d' / meta-d' / M-ratio by TMS site ===")
    hdr = f"{'subj':>4} | " + " | ".join(
        f"{SITE[st]:>22}" for st in sites)
    print(hdr)
    for s in subjects:
        cells = []
        for st in sites:
            m = results[s][st]
            cells.append(f"d'={m['dprime']:.2f} md={m['metad']:.2f} Mr={m['mratio']:.2f}")
        print(f"{s:>4} | " + " | ".join(f"{c:>22}" for c in cells))

    # group means per site
    print("\n=== GROUP MEANS (N={}) ===".format(len(subjects)))
    for st in sites:
        dp = [results[s][st]["dprime"] for s in subjects]
        md = [results[s][st]["metad"] for s in subjects]
        mr = [results[s][st]["mratio"] for s in subjects]
        acc = [results[s][st]["acc"] for s in subjects]
        print(f"  {SITE[st]:>12}: acc={stats.mean(acc):.3f}  "
              f"d'={stats.mean(dp):.3f}(sd{stats.stdev(dp):.3f})  "
              f"meta-d'={stats.mean(md):.3f}(sd{stats.stdev(md):.3f})  "
              f"M-ratio={stats.mean(mr):.3f}(sd{stats.stdev(mr):.3f})")

    # within-subject paired contrasts vs S1 control
    print("\n=== WITHIN-SUBJECT PAIRED CONTRASTS (site vs S1 control) ===")
    for st in ("2", "3"):
        print(f"\n--- {SITE[st]} vs S1_control ---")
        for metric in ("dprime", "metad", "mratio"):
            x = [results[s][st][metric] for s in subjects]
            y = [results[s]["1"][metric] for s in subjects]
            r = paired_t(x, y)
            label = {"dprime": "d'      ", "metad": "meta-d' ", "mratio": "M-ratio "}[metric]
            print(f"  {label}: mean({SITE[st]})={stats.mean(x):.3f} "
                  f"mean(S1)={stats.mean(y):.3f} "
                  f"delta={r['mean']:+.3f}  t({r['df']})={r['t']:.2f}  "
                  f"p={r['p']:.4f}  dz={r['dz']:+.3f}")

    # direct DLPFC vs aPFC contrast (both prefrontal)
    print("\n--- DLPFC vs aPFC (both prefrontal) ---")
    for metric in ("dprime", "metad", "mratio"):
        x = [results[s]["2"][metric] for s in subjects]
        y = [results[s]["3"][metric] for s in subjects]
        r = paired_t(x, y)
        label = {"dprime": "d'      ", "metad": "meta-d' ", "mratio": "M-ratio "}[metric]
        print(f"  {label}: delta(DLPFC-aPFC)={r['mean']:+.3f}  "
              f"t({r['df']})={r['t']:.2f}  p={r['p']:.4f}  dz={r['dz']:+.3f}")

    return results, subjects, sites


if __name__ == "__main__":
    main()
