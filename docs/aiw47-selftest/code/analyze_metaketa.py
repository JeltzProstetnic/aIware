"""Independent meta-d'/M-ratio reanalysis of Lehmann et al. (2022) MetaKeta-II.

Data: nR_S1 / nR_S2 response-count vectors per participant, supplied by
M. Lehmann (Univ. Bonn) on 2026-06-11, with the Drug condition variable
(1 = Ketamine, 2 = Placebo). 45 participants, each in ONE condition only
(between-subjects as delivered; no within-subject pairing key present).

Tests FMT's prediction (metacognition / evaluation-model axis): an acute
NMDA-antagonist (ketamine) should selectively lower metacognitive sensitivity
(meta-d', M-ratio) while leaving first-order perceptual sensitivity (d')
roughly intact (the staircase holds d' constant by design).

Pure stdlib + openpyxl (read only). meta-d' from metad_mle.fit_meta_d
(Maniscalco & Lau 2012, equal-variance SDT, 1/(2K) cell padding).
Statistics (Welch t, Mann-Whitney U, Cohen's d) implemented from scratch;
p-values via the regularised incomplete beta and math.erfc.
"""
import math
import csv
import openpyxl
from metad_mle import fit_meta_d

DATA = "data/MetaKetaII_nRS1_nRS2.xlsx"


# ---------- statistics (stdlib) ----------
def _betacf(a, b, x):
    MAXIT, EPS, FPMIN = 200, 3e-12, 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < FPMIN:
        d = FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < EPS:
            break
    return h


def betai(a, b, x):
    """Regularised incomplete beta I_x(a,b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    bt = math.exp(lbeta + a * math.log(x) + b * math.log1p(-x))
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _betacf(a, b, x) / a
    return 1.0 - bt * _betacf(b, a, 1.0 - x) / b


def t_sf_two_sided(t, df):
    """Two-sided p-value for Student-t."""
    x = df / (df + t * t)
    return betai(df / 2.0, 0.5, x)


def norm_sf(z):
    return 0.5 * math.erfc(z / math.sqrt(2.0))


def mean(xs):
    return sum(xs) / len(xs)


def var(xs):
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - 1)


def welch(a, b):
    n1, n2 = len(a), len(b)
    m1, m2 = mean(a), mean(b)
    v1, v2 = var(a), var(b)
    se = math.sqrt(v1 / n1 + v2 / n2)
    t = (m1 - m2) / se
    df = (v1 / n1 + v2 / n2) ** 2 / (
        (v1 / n1) ** 2 / (n1 - 1) + (v2 / n2) ** 2 / (n2 - 1))
    p = t_sf_two_sided(abs(t), df)
    # Hedges g (pooled SD, small-sample corrected)
    sp = math.sqrt(((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2))
    d = (m1 - m2) / sp
    J = 1.0 - 3.0 / (4 * (n1 + n2) - 9)
    return dict(m1=m1, m2=m2, sd1=math.sqrt(v1), sd2=math.sqrt(v2),
                t=t, df=df, p=p, cohens_d=d, hedges_g=d * J)


def mannwhitney(a, b):
    """Two-sided Mann-Whitney U with tie-corrected normal approximation."""
    n1, n2 = len(a), len(b)
    combined = sorted([(v, 0) for v in a] + [(v, 1) for v in b])
    # average ranks with tie handling
    ranks = [0.0] * len(combined)
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        avg = (i + 1 + j + 1) / 2.0
        for k in range(i, j + 1):
            ranks[k] = avg
        i = j + 1
    R1 = sum(r for r, (_, g) in zip(ranks, combined) if g == 0)
    U1 = R1 - n1 * (n1 + 1) / 2.0
    U2 = n1 * n2 - U1
    U = min(U1, U2)
    mu = n1 * n2 / 2.0
    # tie correction
    from collections import Counter
    tie = Counter(v for v, _ in combined)
    N = n1 + n2
    tcorr = sum(t ** 3 - t for t in tie.values())
    sigma = math.sqrt(n1 * n2 / 12.0 * ((N + 1) - tcorr / (N * (N - 1))))
    z = (U - mu) / sigma
    p = 2 * norm_sf(abs(z))
    return dict(U=U, z=z, p=p)


# ---------- load + fit ----------
def load():
    wb = openpyxl.load_workbook(DATA, data_only=True)
    ws = wb["included"]
    out = []
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0] is None:
            continue
        subj = int(r[0])
        drug = int(r[1])  # 1=Ketamine, 2=Placebo
        nR_S1 = [float(x) for x in r[2:14]]
        nR_S2 = [float(x) for x in r[14:26]]
        out.append((subj, drug, nR_S1, nR_S2))
    return out


def main():
    rows = load()
    results = []
    for subj, drug, nR_S1, nR_S2 in rows:
        meta_d, d1, c1 = fit_meta_d(nR_S1, nR_S2)
        mratio = meta_d / d1 if d1 > 0 else float("nan")
        mdiff = meta_d - d1
        ntrials = sum(nR_S1) + sum(nR_S2)
        results.append(dict(subj=subj, drug=drug, d1=d1, metad=meta_d,
                            c1=c1, mratio=mratio, mdiff=mdiff, n=ntrials))

    # save per-subject
    with open("results_metaketa_persubject.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["subj", "drug", "n", "d1", "metad",
                                          "c1", "mratio", "mdiff"])
        w.writeheader()
        for r in results:
            w.writerow({k: (round(r[k], 5) if isinstance(r[k], float) else r[k])
                        for k in w.fieldnames})

    ket = [r for r in results if r["drug"] == 1]
    pla = [r for r in results if r["drug"] == 2]

    def grp(rs, key):
        return [r[key] for r in rs if not math.isnan(r[key])]

    lines = []
    P = lines.append
    P("=" * 72)
    P("META-d' REANALYSIS — Lehmann et al. (2022) MetaKeta-II")
    P("Independent (between-subjects) test of FMT metacognition-axis prediction")
    P("=" * 72)
    P(f"N = {len(results)}  (Ketamine {len(ket)}, Placebo {len(pla)}); "
      f"6 confidence levels; meta-d' = Maniscalco-Lau MLE, 1/(2K) padding")
    P(f"Trials/subj: median {sorted(r['n'] for r in results)[len(results)//2]:.0f}")
    P("")
    P(f"{'measure':10s} {'Ketamine (mean±SD)':>22s} {'Placebo (mean±SD)':>22s} "
      f"{'Welch t':>9s} {'df':>6s} {'p':>9s} {'Hedges g':>9s} {'MWU p':>9s}")
    P("-" * 100)
    for key, label in [("d1", "d'"), ("metad", "meta-d'"),
                       ("mratio", "M-ratio"), ("mdiff", "M-diff"),
                       ("c1", "crit c")]:
        ka, pa = grp(ket, key), grp(pla, key)
        w = welch(ka, pa)
        mw = mannwhitney(ka, pa)
        P(f"{label:10s} {w['m1']:>11.3f}±{w['sd1']:<9.3f} "
          f"{w['m2']:>11.3f}±{w['sd2']:<9.3f} "
          f"{w['t']:>9.3f} {w['df']:>6.1f} {w['p']:>9.4f} "
          f"{w['hedges_g']:>9.3f} {mw['p']:>9.4f}")
    P("-" * 100)
    P("Direction key: t>0 and g>0 => Ketamine HIGHER than Placebo;")
    P("FMT predicts meta-d' & M-ratio LOWER under ketamine (t<0, g<0),")
    P("with d' NOT significantly different between groups.")
    P("")
    # explicit FMT verdict
    md = welch(grp(ket, "metad"), grp(pla, "metad"))
    mr = welch(grp(ket, "mratio"), grp(pla, "mratio"))
    d1w = welch(grp(ket, "d1"), grp(pla, "d1"))
    P("FMT-relevant reading:")
    P(f"  d'      : ket {d1w['m1']:.3f} vs pla {d1w['m2']:.3f}  "
      f"(p={d1w['p']:.3f}) -> {'PRESERVED' if d1w['p']>0.05 else 'DIFFERS'}")
    P(f"  meta-d' : ket {md['m1']:.3f} vs pla {md['m2']:.3f}  "
      f"(p={md['p']:.3f}, g={md['hedges_g']:.2f}) -> "
      f"{'LOWER under ketamine' if md['m1']<md['m2'] else 'higher under ketamine'}")
    P(f"  M-ratio : ket {mr['m1']:.3f} vs pla {mr['m2']:.3f}  "
      f"(p={mr['p']:.3f}, g={mr['hedges_g']:.2f}) -> "
      f"{'LOWER under ketamine' if mr['m1']<mr['m2'] else 'higher under ketamine'}")

    report = "\n".join(lines)
    print(report)
    with open("results_metaketa_summary.txt", "w") as f:
        f.write(report + "\n")


if __name__ == "__main__":
    main()
