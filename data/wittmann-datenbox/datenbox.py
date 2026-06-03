"""
Datenboxzerlegung nach Wittmann (1985).

Multivariate cross-product decomposition of a 3D data box
(Persons x Situations/Timepoints x Variables) into variance components,
following Wittmann (1985) and Stemmler & Fahrenberg (1989).

Two analysis modes:
  - DatenboxWithout: no replication (datenbox1.sas)
  - DatenboxWith:    with replication / parallel test halves (datenbox2.sas)

Reference:
  Wittmann, W.W. (1985). Evaluationsforschung. Berlin: Springer.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.decomposition import FactorAnalysis


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _normalizer(M: np.ndarray) -> np.ndarray:
    """Return D = diag(1 / sqrt(diag(M))).

    Replicates the SAS IML ``IN`` subroutine:
        A = DIAG(1/SQRT(VECDIAG(G)))

    Elements that are zero or negative on the diagonal are left as zero
    (avoids division-by-zero for degenerate components).
    """
    d = np.diag(M).copy()
    safe = np.where(d > 0, d, np.nan)
    inv_sqrt = np.where(np.isnan(safe), 0.0, 1.0 / np.sqrt(safe))
    return np.diag(inv_sqrt)


def _sum_all(M: np.ndarray) -> float:
    """Sum of all elements — SAS IML ``M[+,+]``."""
    return float(M.sum())


def _normalize_corr(SS: np.ndarray) -> np.ndarray:
    """Correlation matrix normalized at its own diagonal (proper correlations)."""
    S = _normalizer(SS)
    return S @ SS @ S


def _normalize_at_total(SS: np.ndarray, S_total: np.ndarray) -> np.ndarray:
    """Correlation matrix normalized at the total cross-product diagonal.

    Yields eta^2 coefficients on the diagonal — proportion of total variance.
    """
    return S_total @ SS @ S_total


def _t_test_matrix(
    R: np.ndarray,
    df_r: float,
    df_t: float,
    q: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Element-wise t-test for off-diagonal correlations.

    T = r * sqrt(df_r) / sqrt(1 - r^2)

    Diagonal entries are set to 1 (T) and 0 (p) to match SAS output convention
    (diagonal correlations are trivially 1.0 and need no test).

    Parameters
    ----------
    R:
        Correlation matrix (self-normalized).
    df_r:
        Degrees of freedom inside the sqrt (determines t-statistic magnitude).
    df_t:
        Degrees of freedom for the t-distribution (determines p-value).
    q:
        Number of variables (used only to build the identity mask).
    """
    with np.errstate(divide="ignore", invalid="ignore"):
        denom = np.sqrt(np.maximum(1.0 - R**2, 0.0))
        T = np.where(denom > 0, R * np.sqrt(df_r) / denom, 0.0)
    # Replace diagonal with 1 (convention matching SAS: AII = DIAG(SHAPE(1,...)))
    np.fill_diagonal(T, 1.0)
    P = 2.0 * stats.t.sf(np.abs(T), df=df_t)
    np.fill_diagonal(P, 0.0)
    return T, P


def _t_test_matrix_gh(
    R: np.ndarray,
    df_r: float,
    df_t: float,
    q: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Same as _t_test_matrix but uses Greenhouse-Geisser corrected df."""
    return _t_test_matrix(R, df_r, df_t, q)


def _eigendecompose_descending(M: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Eigendecomposition with eigenvalues/vectors sorted descending.

    SAS IML ``eigvec()`` returns columns sorted by descending eigenvalue.
    numpy ``eigh`` returns ascending — we reverse here.
    """
    vals, vecs = np.linalg.eigh(M)
    idx = np.argsort(vals)[::-1]
    return vals[idx], vecs[:, idx]


def _reliability_coefficients(
    SStot: np.ndarray,
    components: dict[str, np.ndarray],
    q: int,
) -> dict[str, float]:
    """Compute all three Wittmann multivariate reliability indices.

    Parameters
    ----------
    SStot:
        Total cross-product matrix.
    components:
        Mapping of component name -> cross-product matrix.
        Keys must include at least 'bp', 'bs'; optionally 'pxs'.
    q:
        Number of variables.

    Returns
    -------
    dict with keys like 'RTT_bp', 'TT_bp', 'RMAX_bp', etc.
    """
    results: dict[str, float] = {}

    # --- RTT: sum-scale reliability ---
    ss_tot_total = _sum_all(SStot)
    for name, SS in components.items():
        results[f"RTT_{name}"] = _sum_all(SS) / ss_tot_total
    results["RTT_total"] = sum(
        results[f"RTT_{n}"] for n in components
        if n not in ("res", "ws", "wp")
    )

    # --- TT: trace correlation (all eigenvectors) ---
    _, Etot = _eigendecompose_descending(SStot)
    Ltot = np.diag(Etot.T @ SStot @ Etot)

    with np.errstate(divide="ignore", invalid="ignore"):
        for name, SS in components.items():
            L = np.diag(Etot.T @ SS @ Etot)
            ratio = np.where(Ltot != 0, L / Ltot, 0.0)
            results[f"TT_{name}"] = float(ratio.sum()) / q

    true_components = {n: SS for n, SS in components.items()
                       if n not in ("res", "ws", "wp")}
    SS_true = sum(true_components.values())
    L_true = np.diag(Etot.T @ SS_true @ Etot)
    ratio_true = np.where(Ltot != 0, L_true / Ltot, 0.0)
    results["TT_total"] = float(ratio_true.sum()) / q

    # --- RMAX: maximized reliability (first eigenvector only) ---
    _, Etot_full = _eigendecompose_descending(SStot)
    e1 = Etot_full[:, [0]]  # largest eigenvector, keep as column
    ltot_max = float((e1.T @ SStot @ e1).item())

    for name, SS in components.items():
        l_comp = float((e1.T @ SS @ e1).item())
        results[f"RMAX_{name}"] = l_comp / ltot_max if ltot_max != 0 else 0.0
    ss_true_sum = sum(true_components.values())
    results["RMAX_total"] = float((e1.T @ ss_true_sum @ e1).item()) / ltot_max if ltot_max != 0 else 0.0

    return results


def _generalizability(
    components: dict[str, np.ndarray],
    SSres: np.ndarray,
) -> dict[str, float]:
    """Multivariate generalizability coefficients U = SS_x / (SS_x + SS_res)."""
    res_sum = _sum_all(SSres)
    return {
        f"U_{name}": _sum_all(SS) / (_sum_all(SS) + res_sum)
        for name, SS in components.items()
    }


def _chi2_residual_identity(Rresc: np.ndarray, k: int, p: int, q: int) -> tuple[float, int, float]:
    """Chi^2 test H0: residual correlation matrix = identity.

    Formula from SAS: R_TEST = -2 * k * p * log(|det(Rresc)|)
    """
    sign, logdet = np.linalg.slogdet(Rresc)
    if sign <= 0:
        r_test = np.nan
    else:
        r_test = -2 * k * p * logdet
    df = q * (q - 1) // 2
    p_val = float(stats.chi2.sf(r_test, df)) if not np.isnan(r_test) else np.nan
    return float(r_test), df, p_val


def _factor_analysis(R: np.ndarray, n_factors: int | None = None) -> pd.DataFrame:
    """Varimax-rotated factor analysis of a correlation matrix.

    Uses sklearn FactorAnalysis (max-likelihood with varimax rotation).
    Returns a DataFrame of loadings (variables x factors).
    """
    q = R.shape[0]
    if n_factors is None:
        # Retain factors with eigenvalue > 1 (Kaiser criterion)
        evals, _ = np.linalg.eigh(R)
        n_factors = max(1, int((evals > 1).sum()))
        n_factors = min(n_factors, q - 1)

    fa = FactorAnalysis(n_components=n_factors, rotation="varimax", random_state=0)
    # FactorAnalysis expects an (n_samples x n_features) matrix.
    # Feeding the correlation matrix directly: each "sample" is a row of R.
    fa.fit(R)
    loadings = fa.components_.T  # shape: (q, n_factors)
    cols = [f"Factor{i+1}" for i in range(n_factors)]
    return pd.DataFrame(loadings, columns=cols)


# ---------------------------------------------------------------------------
# Result dataclasses
# ---------------------------------------------------------------------------

@dataclass
class CrossProductPartition:
    """Raw cross-product matrices from the decomposition."""
    SStot: np.ndarray
    SSbp: np.ndarray
    SSbs: np.ndarray
    SSres: np.ndarray
    SSws: np.ndarray
    SSwp: np.ndarray


@dataclass
class CrossProductPartitionWithRep(CrossProductPartition):
    """Extended partition including Person x Situation interaction."""
    SSpxs: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class CorrelationMatrices:
    """Correlation matrices, both normalized variants."""
    # Normalized at total covariance (eta^2 on diagonal)
    Rtot_eta: np.ndarray
    Rbp_eta: np.ndarray
    Rbs_eta: np.ndarray
    Rres_eta: np.ndarray
    Rws_eta: np.ndarray
    Rwp_eta: np.ndarray
    # Normalized at own covariance (proper correlations)
    Rtot: np.ndarray
    Rbp: np.ndarray
    Rbs: np.ndarray
    Rres: np.ndarray
    Rws: np.ndarray
    Rwp: np.ndarray


@dataclass
class CorrelationMatricesWithRep(CorrelationMatrices):
    """Extended correlation matrices including pxs component."""
    Rpxs_eta: np.ndarray = field(default_factory=lambda: np.array([]))
    Rpxs: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class TTestResults:
    """Element-wise t-test matrices and p-values for each correlation matrix."""
    T_tot: np.ndarray
    P_tot: np.ndarray
    T_bp: np.ndarray
    P_bp: np.ndarray
    T_bs: np.ndarray
    P_bs: np.ndarray
    T_wp: np.ndarray
    P_wp: np.ndarray
    T_ws: np.ndarray
    P_ws: np.ndarray
    T_res: np.ndarray
    P_res: np.ndarray
    # Greenhouse-Geisser corrected
    T_tot_gg: np.ndarray
    P_tot_gg: np.ndarray
    T_bp_gg: np.ndarray
    P_bp_gg: np.ndarray
    T_bs_gg: np.ndarray
    P_bs_gg: np.ndarray
    T_wp_gg: np.ndarray
    P_wp_gg: np.ndarray
    T_ws_gg: np.ndarray
    P_ws_gg: np.ndarray
    T_res_gg: np.ndarray
    P_res_gg: np.ndarray


@dataclass
class TTestResultsWithRep:
    """T-test results for the with-replication model (no GG correction in SAS)."""
    T_tot: np.ndarray
    P_tot: np.ndarray
    T_bp: np.ndarray
    P_bp: np.ndarray
    T_bs: np.ndarray
    P_bs: np.ndarray
    T_pxs: np.ndarray
    P_pxs: np.ndarray
    T_wp: np.ndarray
    P_wp: np.ndarray
    T_ws: np.ndarray
    P_ws: np.ndarray
    T_res: np.ndarray
    P_res: np.ndarray


@dataclass
class ReliabilityCoefficients:
    """Wittmann multivariate reliability and generalizability coefficients."""
    RTT_bp: float
    RTT_bs: float
    RTT_res: float
    RTT_total: float
    TT_bp: float
    TT_bs: float
    TT_res: float
    TT_total: float
    RMAX_bp: float
    RMAX_bs: float
    RMAX_res: float
    RMAX_total: float
    U_bp: float
    U_bs: float


@dataclass
class ReliabilityCoefficientsWithRep:
    """Reliability and generalizability for the with-replication model."""
    RTT_bp: float
    RTT_bs: float
    RTT_pxs: float
    RTT_total: float
    TT_bp: float
    TT_bs: float
    TT_pxs: float
    TT_total: float
    RMAX_bp: float
    RMAX_bs: float
    RMAX_pxs: float
    RMAX_total: float
    U_bp: float
    U_bs: float
    U_pxs: float


@dataclass
class Chi2Result:
    statistic: float
    df: int
    p_value: float


@dataclass
class ParallelTestQuality:
    """Parallel test quality checks per timepoint (datenbox2 only)."""
    timepoints: list[int]
    alpha_test1: list[float]
    alpha_test2: list[float]
    parallel_corr: list[float]
    spearman_brown: list[float]


@dataclass
class DatenboxResult:
    """Full result container for the without-replication analysis."""
    n_persons: int
    n_situations: int
    n_variables: int
    n_total: int
    variable_names: list[str]
    cross_products: CrossProductPartition
    correlations: CorrelationMatrices
    t_tests: TTestResults
    chi2_residual: Chi2Result
    reliability: ReliabilityCoefficients
    factor_loadings: dict[str, pd.DataFrame]


@dataclass
class DatenboxResultWithRep:
    """Full result container for the with-replication analysis."""
    n_persons: int
    n_situations: int
    n_variables: int
    n_total: int
    n_per_cell: int
    variable_names: list[str]
    parallel_test_quality: ParallelTestQuality
    cross_products: CrossProductPartitionWithRep
    correlations: CorrelationMatricesWithRep
    t_tests: TTestResultsWithRep
    chi2_residual: Chi2Result
    reliability: ReliabilityCoefficientsWithRep
    factor_loadings: dict[str, pd.DataFrame]


# ---------------------------------------------------------------------------
# Main analysis classes
# ---------------------------------------------------------------------------

class DatenboxWithout:
    """Datenbox decomposition WITHOUT replication (datenbox1.sas).

    Decomposes a P x K x Q data box into:
      - Between Persons (bp)
      - Between Situations (bs)
      - Residual (res)
      - Within Persons (wp) = tot - bp
      - Within Situations (ws) = tot - bs

    Parameters
    ----------
    df:
        DataFrame with columns [person_id, timepoint, var1, ..., varQ].
    person_col:
        Column name identifying persons.
    time_col:
        Column name identifying timepoints/situations.
    var_cols:
        List of variable column names. If None, all columns except
        person_col and time_col are used.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        person_col: str = "pnr",
        time_col: str = "time",
        var_cols: list[str] | None = None,
    ) -> None:
        self.df = df.copy()
        self.person_col = person_col
        self.time_col = time_col
        if var_cols is None:
            var_cols = [c for c in df.columns if c not in (person_col, time_col)]
        self.var_cols = var_cols

    def run(self) -> DatenboxResult:
        """Execute the full decomposition and return results."""
        df = self.df
        var_cols = self.var_cols
        person_col = self.person_col
        time_col = self.time_col

        # --- Raw data matrix ---
        X = df[var_cols].to_numpy(dtype=float)
        Ng = X.shape[0]
        Q = X.shape[1]

        # Sum vectors per person (XFP) — aggregate over timepoints
        XFP = (
            df.groupby(person_col)[var_cols].sum().to_numpy(dtype=float)
        )
        P = XFP.shape[0]

        # Sum vectors per situation (XFS) — aggregate over persons
        XFS = (
            df.groupby(time_col)[var_cols].sum().to_numpy(dtype=float)
        )
        k = XFS.shape[0]

        # Grand sum vector
        XG = X.sum(axis=0, keepdims=True)  # shape (1, Q)

        # --- Cross-product partitioning (SAS IML section 5.2) ---
        correction = XG.T @ XG / Ng  # (Q x Q) grand mean correction

        SStot = X.T @ X - correction
        SSbp = XFP.T @ XFP / k - correction
        SSbs = XFS.T @ XFS / P - correction
        SSres = SStot - SSbp - SSbs
        SSws = SStot - SSbs
        SSwp = SStot - SSbp

        cp = CrossProductPartition(
            SStot=SStot, SSbp=SSbp, SSbs=SSbs,
            SSres=SSres, SSws=SSws, SSwp=SSwp,
        )

        # --- Correlation matrices ---
        S = _normalizer(SStot)

        # Eta^2 (normalized at total)
        Rtot_eta = _normalize_at_total(SStot, S)
        Rbp_eta = _normalize_at_total(SSbp, S)
        Rbs_eta = _normalize_at_total(SSbs, S)
        Rres_eta = _normalize_at_total(SSres, S)
        Rws_eta = _normalize_at_total(SSws, S)
        Rwp_eta = _normalize_at_total(SSwp, S)

        # Proper correlations (normalized at own diagonal)
        Rtot = _normalize_corr(SStot)
        Rbp = _normalize_corr(SSbp)
        Rbs = _normalize_corr(SSbs)
        Rres = _normalize_corr(SSres)
        Rws = _normalize_corr(SSws)
        Rwp = _normalize_corr(SSwp)

        corr = CorrelationMatrices(
            Rtot_eta=Rtot_eta, Rbp_eta=Rbp_eta, Rbs_eta=Rbs_eta,
            Rres_eta=Rres_eta, Rws_eta=Rws_eta, Rwp_eta=Rwp_eta,
            Rtot=Rtot, Rbp=Rbp, Rbs=Rbs,
            Rres=Rres, Rws=Rws, Rwp=Rwp,
        )

        # --- T-tests (SAS section 5.3 and 5.4) ---
        # Without Greenhouse-Geisser correction
        T_tot, P_tot = _t_test_matrix(Rtot, k * P - 2, k * P - 1, Q)
        T_bp, P_bp = _t_test_matrix(Rbp, P - 2, P - 1, Q)
        T_bs, P_bs = _t_test_matrix(Rbs, k - 2, k - 1, Q)
        T_wp, P_wp = _t_test_matrix(Rwp, P * k - 2, P * (k - 1), Q)
        T_ws, P_ws = _t_test_matrix(Rws, k * P - 2, k * (P - 1), Q)
        T_res, P_res = _t_test_matrix(Rres, k * P - 2, (k - 1) * (P - 1), Q)

        # With Greenhouse-Geisser correction
        T_tot_gg, P_tot_gg = _t_test_matrix_gh(Rtot, 2 * P - 2, 2 * P - 1, Q)
        T_bp_gg, P_bp_gg = _t_test_matrix_gh(Rbp, P - 2, P - 1, Q)
        # GG for bs: SAS uses no sqrt(k-2) factor, just r/(sqrt(1-r^2))
        with np.errstate(divide="ignore", invalid="ignore"):
            denom_bs = np.sqrt(np.maximum(1.0 - Rbs**2, 0.0))
            T_bs_gg = np.where(denom_bs > 0, Rbs / denom_bs, 0.0)
            np.fill_diagonal(T_bs_gg, 1.0)
        P_bs_gg = 2.0 * stats.t.sf(np.abs(T_bs_gg), df=k - 1)
        np.fill_diagonal(P_bs_gg, 0.0)

        T_wp_gg, P_wp_gg = _t_test_matrix_gh(Rwp, P - 2, P, Q)
        T_ws_gg, P_ws_gg = _t_test_matrix_gh(Rws, 2 * P - 2, 2 * (P - 1), Q)
        T_res_gg, P_res_gg = _t_test_matrix_gh(Rres, P - 2, P - 1, Q)

        t_tests = TTestResults(
            T_tot=T_tot, P_tot=P_tot,
            T_bp=T_bp, P_bp=P_bp,
            T_bs=T_bs, P_bs=P_bs,
            T_wp=T_wp, P_wp=P_wp,
            T_ws=T_ws, P_ws=P_ws,
            T_res=T_res, P_res=P_res,
            T_tot_gg=T_tot_gg, P_tot_gg=P_tot_gg,
            T_bp_gg=T_bp_gg, P_bp_gg=P_bp_gg,
            T_bs_gg=T_bs_gg, P_bs_gg=P_bs_gg,
            T_wp_gg=T_wp_gg, P_wp_gg=P_wp_gg,
            T_ws_gg=T_ws_gg, P_ws_gg=P_ws_gg,
            T_res_gg=T_res_gg, P_res_gg=P_res_gg,
        )

        # --- Chi^2 test: Rres = Identity ---
        chi2_stat, chi2_df, chi2_p = _chi2_residual_identity(Rres, k, P, Q)
        chi2_result = Chi2Result(statistic=chi2_stat, df=chi2_df, p_value=chi2_p)

        # --- Reliability (SAS section 6) ---
        rel_components = {"bp": SSbp, "bs": SSbs, "res": SSres}
        rel_raw = _reliability_coefficients(SStot, rel_components, Q)
        gen = _generalizability({"bp": SSbp, "bs": SSbs}, SSres)

        reliability = ReliabilityCoefficients(
            RTT_bp=rel_raw["RTT_bp"],
            RTT_bs=rel_raw["RTT_bs"],
            RTT_res=rel_raw["RTT_res"],
            RTT_total=rel_raw["RTT_bp"] + rel_raw["RTT_bs"],
            TT_bp=rel_raw["TT_bp"],
            TT_bs=rel_raw["TT_bs"],
            TT_res=rel_raw["TT_res"],
            TT_total=rel_raw["TT_total"],
            RMAX_bp=rel_raw["RMAX_bp"],
            RMAX_bs=rel_raw["RMAX_bs"],
            RMAX_res=rel_raw["RMAX_res"],
            RMAX_total=rel_raw["RMAX_total"],
            U_bp=gen["U_bp"],
            U_bs=gen["U_bs"],
        )

        # --- Factor analyses ---
        fa_matrices = {
            "total": Rtot,
            "bp": Rbp,
            "bs": Rbs,
            "wp": Rwp,
            "ws": Rws,
            "res": Rres,
        }
        factor_loadings = {}
        for name, R_mat in fa_matrices.items():
            try:
                factor_loadings[name] = _factor_analysis(R_mat)
            except Exception:
                factor_loadings[name] = pd.DataFrame()

        return DatenboxResult(
            n_persons=P,
            n_situations=k,
            n_variables=Q,
            n_total=Ng,
            variable_names=var_cols,
            cross_products=cp,
            correlations=corr,
            t_tests=t_tests,
            chi2_residual=chi2_result,
            reliability=reliability,
            factor_loadings=factor_loadings,
        )


class DatenboxWith:
    """Datenbox decomposition WITH replication (datenbox2.sas).

    Extends the without-replication model by adding a Person x Situation
    interaction component (SSpxs). Requires a test-half identifier column.

    Decomposition:
      SStot = SSbp + SSbs + SSpxs + SSres

    Parameters
    ----------
    df:
        DataFrame with columns [person_id, timepoint, test_half, var1, ..., varQ].
    person_col:
        Column identifying persons.
    time_col:
        Column identifying timepoints/situations.
    test_col:
        Column identifying parallel test halves (replication dimension).
    var_cols:
        Variable column names. If None, all remaining columns are used.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        person_col: str = "pnr",
        time_col: str = "time",
        test_col: str = "test",
        var_cols: list[str] | None = None,
    ) -> None:
        self.df = df.copy()
        self.person_col = person_col
        self.time_col = time_col
        self.test_col = test_col
        if var_cols is None:
            var_cols = [
                c for c in df.columns
                if c not in (person_col, time_col, test_col)
            ]
        self.var_cols = var_cols

    def _parallel_test_quality(self) -> ParallelTestQuality:
        """Compute Cronbach alpha, parallel-test correlation, Spearman-Brown per timepoint."""
        df = self.df
        var_cols = self.var_cols
        person_col = self.person_col
        time_col = self.time_col
        test_col = self.test_col

        timepoints = sorted(df[time_col].unique().tolist())
        test_halves = sorted(df[test_col].unique().tolist())
        alpha1_list, alpha2_list, rttp_list, rttspea_list = [], [], [], []

        if len(test_halves) < 2:
            # Only one test half — parallel-test statistics are undefined
            nans = [np.nan] * len(timepoints)
            return ParallelTestQuality(
                timepoints=timepoints,
                alpha_test1=nans,
                alpha_test2=nans,
                parallel_corr=nans,
                spearman_brown=nans,
            )

        for tp in timepoints:
            tp_data = df[df[time_col] == tp]
            t1 = tp_data[tp_data[test_col] == test_halves[0]][var_cols].to_numpy(dtype=float)
            t2 = tp_data[tp_data[test_col] == test_halves[1]][var_cols].to_numpy(dtype=float)

            def cronbach_alpha(X: np.ndarray) -> float:
                n, k = X.shape
                if k < 2 or n < 2:
                    return np.nan
                item_var = X.var(axis=0, ddof=1)
                total_var = X.sum(axis=1).var(ddof=1)
                if total_var == 0:
                    return np.nan
                return float(k / (k - 1) * (1 - item_var.sum() / total_var))

            alpha1_list.append(cronbach_alpha(t1))
            alpha2_list.append(cronbach_alpha(t2))

            # Parallel-test correlation: correlation of sum scores
            score1 = t1.sum(axis=1)
            score2 = t2.sum(axis=1)
            if len(score1) >= 2 and score1.std() > 0 and score2.std() > 0:
                rttp = float(np.corrcoef(score1, score2)[0, 1])
            else:
                rttp = np.nan
            rttp_list.append(rttp)
            sb = float(2 * rttp / (1 + rttp)) if not np.isnan(rttp) else np.nan
            rttspea_list.append(sb)

        return ParallelTestQuality(
            timepoints=timepoints,
            alpha_test1=alpha1_list,
            alpha_test2=alpha2_list,
            parallel_corr=rttp_list,
            spearman_brown=rttspea_list,
        )

    def run(self) -> DatenboxResultWithRep:
        """Execute the full decomposition and return results."""
        df = self.df
        var_cols = self.var_cols
        person_col = self.person_col
        time_col = self.time_col
        test_col = self.test_col

        # --- Parallel test quality (pre-analysis) ---
        ptq = self._parallel_test_quality()

        # --- Sum vectors matching SAS proc summary _type_ flags ---
        # _type_=0: grand sum (XG)
        XG = df[var_cols].sum().to_numpy(dtype=float, na_value=0.0).reshape(1, -1)
        Ng = len(df)

        # _type_=2: sum over TEST for each PERSON (XFP)
        XFP = df.groupby(person_col)[var_cols].sum().to_numpy(dtype=float)
        P = XFP.shape[0]

        # _type_=1: sum over TEST for each ZEITP (XFS)
        XFS = df.groupby(time_col)[var_cols].sum().to_numpy(dtype=float)
        K = XFS.shape[0]

        # _type_=3: sum over TEST for each PERSON x ZEITP cell (XFI)
        XFI = (
            df.groupby([person_col, time_col])[var_cols]
            .sum()
            .to_numpy(dtype=float)
        )

        # _type_=7: individual observations per PERSON x ZEITP x TEST cell (X)
        # With 1 observation per cell this is just the raw data sorted by cell
        X = (
            df.sort_values([person_col, time_col, test_col])[var_cols]
            .to_numpy(dtype=float)
        )

        Q = X.shape[1]
        n = Ng // (P * K)  # observations per cell (number of test halves)

        # --- Cross-product partitioning (SAS section 3.2) ---
        correction = XG.T @ XG / Ng

        SStot = X.T @ X - correction
        SSbp = XFP.T @ XFP / (K * n) - correction
        SSbs = XFS.T @ XFS / (P * n) - correction
        SSpxs = XFI.T @ XFI / n - SSbp - SSbs - correction
        SSres = SStot - SSbp - SSbs - SSpxs
        SSws = SStot - SSbs
        SSwp = SStot - SSbp

        cp = CrossProductPartitionWithRep(
            SStot=SStot, SSbp=SSbp, SSbs=SSbs,
            SSres=SSres, SSws=SSws, SSwp=SSwp,
            SSpxs=SSpxs,
        )

        # --- Correlation matrices ---
        S = _normalizer(SStot)

        # Normalized at total (eta^2)
        Rtot_eta = _normalize_at_total(SStot, S)
        Rbp_eta = _normalize_at_total(SSbp, S)
        Rbs_eta = _normalize_at_total(SSbs, S)
        Rpxs_eta = _normalize_at_total(SSpxs, S)
        Rres_eta = _normalize_at_total(SSres, S)
        Rws_eta = _normalize_at_total(SSws, S)
        Rwp_eta = _normalize_at_total(SSwp, S)

        # Proper correlations
        Rtot = _normalize_corr(SStot)
        Rbp = _normalize_corr(SSbp)
        Rbs = _normalize_corr(SSbs)
        Rpxs = _normalize_corr(SSpxs)
        Rres = _normalize_corr(SSres)
        Rws = _normalize_corr(SSws)
        Rwp = _normalize_corr(SSwp)

        corr = CorrelationMatricesWithRep(
            Rtot_eta=Rtot_eta, Rbp_eta=Rbp_eta, Rbs_eta=Rbs_eta,
            Rres_eta=Rres_eta, Rws_eta=Rws_eta, Rwp_eta=Rwp_eta,
            Rtot=Rtot, Rbp=Rbp, Rbs=Rbs,
            Rres=Rres, Rws=Rws, Rwp=Rwp,
            Rpxs_eta=Rpxs_eta, Rpxs=Rpxs,
        )

        # --- T-tests (SAS section 4.6) ---
        T_tot, P_tot = _t_test_matrix(Rtot, K * P * n - 2, K * P * n - 1, Q)
        T_bp, P_bp = _t_test_matrix(Rbp, P - 2, P - 1, Q)
        T_bs, P_bs = _t_test_matrix(Rbs, K - 2, K - 1, Q)
        T_pxs, P_pxs = _t_test_matrix(Rpxs, K * P - 2, (K - 1) * (P - 1), Q)
        T_wp, P_wp = _t_test_matrix(Rwp, P * K * n - 2, P * (K * n - 1), Q)
        T_ws, P_ws = _t_test_matrix(Rws, K * P * n - 2, K * (P * n - 1), Q)
        T_res, P_res = _t_test_matrix(Rres, P * K * n - 2, P * K * (n - 1), Q)

        t_tests = TTestResultsWithRep(
            T_tot=T_tot, P_tot=P_tot,
            T_bp=T_bp, P_bp=P_bp,
            T_bs=T_bs, P_bs=P_bs,
            T_pxs=T_pxs, P_pxs=P_pxs,
            T_wp=T_wp, P_wp=P_wp,
            T_ws=T_ws, P_ws=P_ws,
            T_res=T_res, P_res=P_res,
        )

        # --- Chi^2 test ---
        chi2_stat, chi2_df, chi2_p = _chi2_residual_identity(Rres, K, P, Q)
        chi2_result = Chi2Result(statistic=chi2_stat, df=chi2_df, p_value=chi2_p)

        # --- Reliability ---
        rel_components = {"bp": SSbp, "bs": SSbs, "pxs": SSpxs, "res": SSres}
        rel_raw = _reliability_coefficients(SStot, rel_components, Q)
        gen = _generalizability({"bp": SSbp, "bs": SSbs, "pxs": SSpxs}, SSres)

        reliability = ReliabilityCoefficientsWithRep(
            RTT_bp=rel_raw["RTT_bp"],
            RTT_bs=rel_raw["RTT_bs"],
            RTT_pxs=rel_raw["RTT_pxs"],
            RTT_total=rel_raw["RTT_bp"] + rel_raw["RTT_bs"] + rel_raw["RTT_pxs"],
            TT_bp=rel_raw["TT_bp"],
            TT_bs=rel_raw["TT_bs"],
            TT_pxs=rel_raw["TT_pxs"],
            TT_total=rel_raw["TT_total"],
            RMAX_bp=rel_raw["RMAX_bp"],
            RMAX_bs=rel_raw["RMAX_bs"],
            RMAX_pxs=rel_raw["RMAX_pxs"],
            RMAX_total=rel_raw["RMAX_total"],
            U_bp=gen["U_bp"],
            U_bs=gen["U_bs"],
            U_pxs=gen["U_pxs"],
        )

        # --- Factor analyses ---
        fa_matrices = {
            "total": Rtot,
            "bp": Rbp,
            "bs": Rbs,
            "pxs": Rpxs,
            "res": Rres,
        }
        factor_loadings = {}
        for name, R_mat in fa_matrices.items():
            try:
                factor_loadings[name] = _factor_analysis(R_mat)
            except Exception:
                factor_loadings[name] = pd.DataFrame()

        return DatenboxResultWithRep(
            n_persons=P,
            n_situations=K,
            n_variables=Q,
            n_total=Ng,
            n_per_cell=n,
            variable_names=var_cols,
            parallel_test_quality=ptq,
            cross_products=cp,
            correlations=corr,
            t_tests=t_tests,
            chi2_residual=chi2_result,
            reliability=reliability,
            factor_loadings=factor_loadings,
        )
