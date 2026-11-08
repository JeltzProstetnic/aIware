"""Figure 1: report category across deciles of slow-wave activity (exploratory, AIW-192).

Reads the frozen run's outputs (docs/aiw192-results/2f30cc2b): the primary model's category curves
(posterior median and 95 % HDI per decile) and the model-free shares from deciles.csv.
Writes figure1.pdf and figure1.png next to this script.
"""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
# In the repository the run sits under docs/; in the deposited archive the script sits beside it.
RUN = HERE if (HERE / "results" / "primary.json").exists() else \
    HERE.parent.parent / "docs" / "aiw192-results" / "2f30cc2b"
CATS = ("E", "EWR", "NE")
LABEL = {"E": "experience (E)", "EWR": "without recall (EWR)", "NE": "no experience (NE)"}
COLOR = {"E": "#2a78d6", "EWR": "#eb6834", "NE": "#1baf7a"}   # validated, 3 slots, all pairs
MARKER = {"E": "o", "EWR": "s", "NE": "^"}


def load_panels(run=RUN):
    primary = json.loads((run / "results" / "primary.json").read_text())
    rows = list(csv.DictReader((run / "model-inputs" / "deciles.csv").open()))
    out = {}
    for basis, key in (("within", "decile_curves_within"), ("z", "decile_curves_z")):
        curves = primary[key]
        model = {c: {s: [curves[f"decile{d}"][c][s] for d in range(1, 11)]
                     for s in ("median", "lo", "hi")} for c in CATS}
        pooled = sorted((r for r in rows if r["basis"] == basis and r["group"] == "pooled"),
                        key=lambda r: int(r["decile"]))
        n = [int(r["n"]) for r in pooled]
        observed = {"n": n}
        for c in CATS:
            observed[c] = [int(r[c]) / k for r, k in zip(pooled, n)]
        out[basis] = {"model": model, "observed": observed}
    return out


def draw(data, path_stem):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5,
                         "axes.edgecolor": "#8a8984", "axes.linewidth": 0.6,
                         "xtick.color": "#52514e", "ytick.color": "#52514e"})
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0), sharey=True)
    titles = {"within": "A  Within-person SWA (registered axis)",
              "z": "B  Standardised SWA, between and within"}
    x = list(range(1, 11))
    for ax, basis in zip(axes, ("within", "z")):
        panel = data[basis]
        for c in CATS:
            m = panel["model"][c]
            ax.fill_between(x, m["lo"], m["hi"], color=COLOR[c], alpha=0.16, linewidth=0)
            ax.plot(x, m["median"], color=COLOR[c], linewidth=1.6)
            ax.plot(x, panel["observed"][c], linestyle="none", marker=MARKER[c], markersize=3.6,
                    markerfacecolor="white", markeredgecolor=COLOR[c], markeredgewidth=0.9)
        ax.set_title(titles[basis], loc="left", fontsize=8.5, color="#0b0b0b")
        ax.set_xticks(x)
        ax.set_xlabel("decile of slow-wave activity (1 = lowest)", color="#52514e")
        ax.set_xlim(0.6, 10.4)
        ax.set_ylim(0, 0.75)
        ax.grid(axis="y", color="#e4e3df", linewidth=0.5)
        ax.set_axisbelow(True)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
    axes[0].set_ylabel("share of awakenings", color="#52514e")
    # direct labels on panel B, right end, in text ink beside a colour key
    for c in CATS:
        yb = data["z"]["model"][c]["median"][9]
        axes[1].annotate(LABEL[c], xy=(10.15, yb), xytext=(10.55, yb), fontsize=7.5,
                         color="#0b0b0b", va="center", annotation_clip=False,
                         arrowprops=dict(arrowstyle="-", color=COLOR[c], linewidth=1.2))
    handles = [plt.Line2D([], [], color=COLOR[c], marker=MARKER[c], markerfacecolor="white",
                          markersize=4, linewidth=1.6, label=LABEL[c]) for c in CATS]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False, fontsize=7.5,
               bbox_to_anchor=(0.44, 0.0))
    fig.subplots_adjust(left=0.08, right=0.80, top=0.9, bottom=0.25, wspace=0.08)
    fig.savefig(f"{path_stem}.pdf")
    fig.savefig(f"{path_stem}.png", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    draw(load_panels(), str(HERE / "figure1"))
    print("wrote", HERE / "figure1.pdf")
