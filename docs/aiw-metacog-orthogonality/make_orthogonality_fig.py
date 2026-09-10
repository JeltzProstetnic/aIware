"""Two-panel figure for the FMT d'-meta-d' orthogonality (ESM/EWM double
dissociation) open-data reanalysis.
A) Structural orthogonality: Rouault 2018 Expt1 (n=498) M-ratio vs d' (author fits).
B) EWM-axis manipulation: Rahnev 2013 contrast levels -> d' moves, M-ratio invariant.
"""
import warnings; warnings.filterwarnings("ignore")
import numpy as np, csv
import scipy.io as sio
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import metad_mle as M

# --- Panel A data: Rouault Expt1 author fits ---
m = sio.loadmat("rouault2018/ME_phase1_excludanalyseddat_all.mat", squeeze_me=True, struct_as_record=False)
da = np.array([s.fitdata.da for s in m["analyseddata"]])
mr = np.array([s.fitdata.M_ratio for s in m["analyseddata"]])
ok = np.isfinite(da) & np.isfinite(mr) & (np.abs(mr) < 3)  # trim a few extreme ratio outliers for display
da_p, mr_p = da[ok], mr[ok]
r = np.corrcoef(da_p, mr_p)[0, 1]
b1, b0 = np.polyfit(da_p, mr_p, 1)

# --- Panel B data: Rahnev contrast levels ---
rows = list(csv.DictReader(open("conf-db/data_Rahnev_2013.csv", newline="")))
levels = ["1", "2", "3"]
subs = sorted(set(r_["Subj_idx"] for r_ in rows), key=lambda x: float(x))
def fit(tr):
    stim, resp, rat = [], [], []
    for t in tr:
        if t["Response"] in ("NaN", "") or t["Confidence"] in ("NaN", ""):
            continue
        stim.append(int(float(t["Stimulus"]))-1); resp.append(int(float(t["Response"]))-1)
        rat.append(int(float(t["Confidence"])))
    nR1, nR2 = M.trials2counts(stim, resp, rat, 2)
    md, d1, _ = M.fit_meta_d(nR1, nR2)
    return d1, md/d1 if d1 else np.nan
dvals = {lv: [] for lv in levels}; mvals = {lv: [] for lv in levels}
for s in subs:
    for lv in levels:
        tr = [r_ for r_ in rows if r_["Subj_idx"] == s and r_["Contrast"] == lv]
        d1, mrat = fit(tr); dvals[lv].append(d1); mvals[lv].append(mrat)
d_mean = [np.nanmean(dvals[lv]) for lv in levels]
d_se = [np.nanstd(dvals[lv], ddof=1)/np.sqrt(len(subs)) for lv in levels]
m_mean = [np.nanmean(mvals[lv]) for lv in levels]
m_se = [np.nanstd(mvals[lv], ddof=1)/np.sqrt(len(subs)) for lv in levels]

# --- plot ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))

ax1.scatter(da_p, mr_p, s=14, alpha=0.35, color="#2b6cb0", edgecolor="none")
xs = np.linspace(da_p.min(), da_p.max(), 50)
ax1.plot(xs, b0 + b1*xs, color="#c53030", lw=2,
         label=f"slope={b1:+.2f}  (r={r:+.2f})")
ax1.axhline(1.0, color="gray", ls=":", lw=1)
ax1.set_xlabel("d′  (first-order sensitivity — EWM)")
ax1.set_ylabel("M-ratio = meta-d′/d′  (metacognitive efficiency — ESM)")
ax1.set_title("A. Structural orthogonality\nRouault et al. 2018, Expt 1 (n=%d)" % len(da_p), fontsize=11)
ax1.legend(loc="upper right", fontsize=9, frameon=False)
ax1.spines[["top", "right"]].set_visible(False)

x = np.arange(3); w = 0.36
ax2.bar(x - w/2, d_mean, w, yerr=d_se, capsize=3, color="#dd6b20", label="d′ (EWM)")
ax2.bar(x + w/2, m_mean, w, yerr=m_se, capsize=3, color="#38a169", label="M-ratio (ESM)")
ax2.set_xticks(x); ax2.set_xticklabels(["low", "mid", "high"])
ax2.set_xlabel("stimulus contrast (difficulty manipulation)")
ax2.set_ylabel("value")
ax2.set_title("B. EWM-axis manipulation\nRahnev 2013 contrast (n=%d): d′↑3×, M-ratio flat" % len(subs), fontsize=11)
ax2.legend(loc="upper left", fontsize=9, frameon=False)
ax2.spines[["top", "right"]].set_visible(False)

fig.tight_layout()
fig.savefig("orthogonality_figure.png", dpi=200)
print("d' spread:", da_p.min(), da_p.max(), "| M-ratio vs d' r=", round(r, 3), "slope=", round(b1, 3))
print("Rahnev d' means:", [round(v,3) for v in d_mean], "| M-ratio means:", [round(v,3) for v in m_mean])
print("saved orthogonality_figure.png")
