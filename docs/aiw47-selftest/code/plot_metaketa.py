"""3-panel figure for the MetaKeta-II reanalysis: d', meta-d', M-ratio,
Ketamine vs Placebo, per-subject points + group mean ± SE.
Reads results_metaketa_persubject.csv (already fitted). Runs in the venv
(matplotlib + numpy). Saves PNG + SVG to docs/aiw47-selftest/.
"""
import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CSV = "/home/jeltz/aIware/tmp/aiw47-data/results_metaketa_persubject.csv"
OUT = "/home/jeltz/aIware/docs/aiw47-selftest/ketamine_metad"

rng = np.random.default_rng(20260611)
rows = list(csv.DictReader(open(CSV)))
ket = {k: np.array([float(r[k]) for r in rows if r["drug"] == "1"]) for k in
       ("d1", "metad", "mratio")}
pla = {k: np.array([float(r[k]) for r in rows if r["drug"] == "2"]) for k in
       ("d1", "metad", "mratio")}

panels = [("d1", "d'  (type-1 sensitivity)", "p=0.11  ns"),
          ("metad", "meta-d'  (type-2 sensitivity)", "p=0.019  g=-0.75  *"),
          ("mratio", "M-ratio  (meta-d'/d')", "p=0.15  ns")]
COL = {"ket": "#c0392b", "pla": "#2980b9"}

fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.0))
for ax, (key, title, annot) in zip(axes, panels):
    groups = [("Ketamine", ket[key], COL["ket"]), ("Placebo", pla[key], COL["pla"])]
    for i, (label, vals, c) in enumerate(groups):
        x = i + 1
        jit = rng.uniform(-0.08, 0.08, size=len(vals))
        ax.scatter(np.full(len(vals), x) + jit, vals, s=22, color=c, alpha=0.45,
                   edgecolor="none", zorder=2)
        m = vals.mean()
        se = vals.std(ddof=1) / np.sqrt(len(vals))
        ax.errorbar(x, m, yerr=se, fmt="o", color=c, ms=9, capsize=5,
                    elinewidth=2, markeredgecolor="black", zorder=3)
        ax.text(x, ax.get_ylim()[0], f"{m:.2f}", ha="center", va="bottom",
                fontsize=8, color=c)
    ax.set_xticks([1, 2])
    ax.set_xticklabels([f"Ketamine\n(n={len(ket[key])})",
                        f"Placebo\n(n={len(pla[key])})"], fontsize=9)
    ax.set_xlim(0.5, 2.5)
    ax.set_title(title, fontsize=10)
    ax.annotate(annot, xy=(0.5, 0.96), xycoords="axes fraction", ha="center",
                va="top", fontsize=9,
                fontweight="bold" if "*" in annot else "normal",
                color="#c0392b" if "*" in annot else "#555")
    ax.grid(axis="y", alpha=0.25)
    ax.spines[["top", "right"]].set_visible(False)

fig.suptitle("Ketamine selectively lowers metacognitive sensitivity (meta-d'), "
             "type-1 d' statistically preserved\n"
             "Independent reanalysis of Lehmann et al. (2022) MetaKeta-II  "
             "— Maniscalco-Lau MLE, between-subjects (26 vs 19)",
             fontsize=10.5, y=1.02)
fig.tight_layout()
fig.savefig(OUT + ".png", dpi=200, bbox_inches="tight")
fig.savefig(OUT + ".svg", bbox_inches="tight")
print("saved", OUT + ".png /.svg")
