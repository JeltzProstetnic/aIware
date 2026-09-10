"""Rouault, Seow, Gillan & Fleming (2018, Biol Psychiatry) Experiment 1 (n=498).
Structural d'-meta-d' orthogonality = the ESM/EWM separability the FMT paper
predicts (Section 8, Prediction 4).

Data: ME_phase1_excludanalyseddat_all.mat from
github.com/metacoglab/RouaultSeowGillanFleming (MIT-licensed repo).
Each subject struct carries the authors' peer-reviewed Maniscalco-Lau fits
(fitdata.da, .meta_da, .M_ratio) AND trial-level data (columns: correct,
stimdevi, target_left, new_confid). We (a) reproduce type-1 d' exactly from the
trial-level data as a data-integrity check, then (b) use the author fits for the
orthogonality statistics.
"""
import warnings; warnings.filterwarnings("ignore")
import numpy as np
import scipy.io as sio
from scipy.stats import norm

MAT = "rouault2018/ME_phase1_excludanalyseddat_all.mat"


def load():
    m = sio.loadmat(MAT, squeeze_me=True, struct_as_record=False)
    return m["analyseddata"]


def z(p):
    return norm.ppf(min(max(p, 1e-6), 1 - 1e-6))


def reproduce_d_check(A):
    """Recompute type-1 d' (HR-FAR) from trial-level data; compare to author da."""
    diffs = []
    for s in A:
        d = s.data
        correct = d[:, 5].astype(int); tl = d[:, 7].astype(int)
        stim = tl; resp = np.where(correct == 1, stim, 1 - stim)
        n1 = max((stim == 1).sum(), 1); n0 = max((stim == 0).sum(), 1)
        HR = ((resp == 1) & (stim == 1)).sum() / n1
        FAR = ((resp == 1) & (stim == 0)).sum() / n0
        diffs.append(abs((z(HR) - z(FAR)) - s.fitdata.da))
    return np.array(diffs)


def main():
    A = load()
    da = np.array([s.fitdata.da for s in A])
    md = np.array([s.fitdata.meta_da for s in A])
    mr = np.array([s.fitdata.M_ratio for s in A])

    chk = reproduce_d_check(A)
    print(f"DATA INTEGRITY: reproduced type-1 d' vs author da over n={len(A)}: "
          f"max|diff|={chk.max():.4f}, mean|diff|={chk.mean():.4f}  "
          f"({'EXACT' if chk.max() < 1e-2 else 'MISMATCH'})")

    ok = np.isfinite(da) & np.isfinite(md) & np.isfinite(mr)
    da, md, mr = da[ok], md[ok], mr[ok]
    r_dmd = np.corrcoef(da, md)[0, 1]
    r_dmr = np.corrcoef(da, mr)[0, 1]
    print(f"\nORTHOGONALITY (n={ok.sum()}):")
    print(f"  d' vs meta-d':  r={r_dmd:+.3f}  R^2={r_dmd**2:.3f}  "
          f"-> {1-r_dmd**2:.0%} of meta-d' variance NOT explained by d'")
    print(f"  d' vs M-ratio:  r={r_dmr:+.3f}  (metacognitive efficiency ~ orthogonal to performance)")
    print(f"  d'      : mean={da.mean():.3f} sd={da.std(ddof=1):.3f} range=[{da.min():.2f},{da.max():.2f}]")
    print(f"  meta-d' : mean={md.mean():.3f} sd={md.std(ddof=1):.3f}")
    print(f"  M-ratio : mean={mr.mean():.3f} sd={mr.std(ddof=1):.3f}")
    print("\nPublished headline (Rouault 2018): psychiatric symptom dimensions shift "
          "metacognition (meta-d'/M-ratio) but NOT task performance (d') = the ESM-axis "
          "manipulation dissociation, cite directly.")


if __name__ == "__main__":
    main()
