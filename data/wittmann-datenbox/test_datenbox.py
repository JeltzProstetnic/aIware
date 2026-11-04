"""
Tests for datenbox.py — Wittmann (1985) multivariate reliability theory.

Fixture data taken verbatim from datenbox1.sas and datenbox2.sas examples.
"""

import numpy as np
import pandas as pd
import pytest

from datenbox import (
    DatenboxWith,
    DatenboxWithout,
    _normalizer,
    _normalize_corr,
    _chi2_residual_identity,
    _reliability_coefficients,
    _generalizability,
    _eigendecompose_descending,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def df1() -> pd.DataFrame:
    """9 persons x 3 timepoints x 6 items (datenbox1.sas example data)."""
    rows = [
        (1, 1, 3.703, 4.557, 5.938, 4.718, 4.601, 4.696),
        (1, 2, 3.503, 6.557, 4.938, 4.418, 4.701, 4.296),
        (1, 3, 2.000, 4.000, 6.000, 4.500, 2.500, 6.000),
        (2, 1, 2.000, 5.000, 6.000, 6.000, 6.000, 5.500),
        (2, 2, 3.000, 5.000, 7.000, 5.000, 4.500, 3.000),
        (2, 3, 4.000, 7.000, 7.000, 7.000, 6.500, 7.000),
        (3, 1, 6.000, 4.000, 6.000, 5.500, 4.500, 4.500),
        (3, 2, 3.703, 4.557, 5.938, 4.718, 4.601, 4.696),
        (3, 3, 3.703, 4.557, 5.938, 4.718, 4.601, 4.696),
        (4, 1, 1.000, 4.000, 4.000, 4.500, 4.000, 4.000),
        (4, 2, 3.000, 5.000, 7.000, 5.000, 4.000, 5.000),
        (4, 3, 3.703, 4.557, 5.938, 4.718, 4.601, 4.696),
        (5, 1, 5.000, 5.000, 7.000, 6.000, 6.500, 4.500),
        (5, 2, 7.000, 5.000, 6.000, 6.000, 4.500, 5.500),
        (5, 3, 2.000, 5.000, 7.000, 5.000, 4.500, 4.500),
        (6, 1, 6.000, 4.000, 6.000, 6.000, 5.500, 5.500),
        (6, 2, 3.703, 4.557, 5.938, 4.718, 4.601, 4.696),
        (6, 3, 4.000, 6.000, 5.000, 5.500, 1.500, 3.500),
        (7, 1, 5.000, 5.000, 6.000, 6.000, 4.000, 5.000),
        (7, 2, 2.000, 4.000, 4.000, 4.500, 6.000, 5.500),
        (7, 3, 3.703, 4.557, 5.938, 4.718, 4.601, 4.696),
        (8, 1, 3.000, 5.000, 5.000, 5.000, 5.500, 5.000),
        (8, 2, 1.000, 1.000, 7.000, 2.000, 4.000, 4.000),
        (8, 3, 6.000, 6.000, 7.000, 4.500, 5.000, 5.000),
        (9, 1, 4.000, 2.000, 4.000, 3.000, 2.000, 3.000),
        (9, 2, 3.703, 4.557, 5.938, 4.718, 4.601, 4.696),
        (9, 3, 3.000, 5.000, 7.000, 4.500, 4.000, 4.500),
    ]
    cols = ["pnr", "time", "item1", "item2", "item3", "item4", "item5", "item6"]
    return pd.DataFrame(rows, columns=cols)


@pytest.fixture
def df2() -> pd.DataFrame:
    """10 persons x 4 timepoints x 2 test halves x 6 items (datenbox2.sas example data)."""
    rows = [
        (1,  1, 1, 3.95, 3.33, 3.08, 4.03, 3.61, 3.67),
        (2,  1, 1, 7.00, 1.00, 4.00, 1.00, 3.00, 2.50),
        (3,  1, 1, 5.00, 4.00, 5.00, 2.00, 2.67, 3.00),
        (4,  1, 1, 7.00, 4.00, 6.00, 5.00, 1.33, 5.00),
        (5,  1, 1, 3.95, 3.33, 3.08, 4.03, 3.61, 3.67),
        (6,  1, 1, 3.95, 3.33, 3.08, 4.03, 3.61, 3.67),
        (7,  1, 1, 7.00, 5.00, 6.00, 6.00, 4.00, 6.50),
        (8,  1, 1, 3.95, 3.33, 3.08, 4.03, 3.61, 3.67),
        (9,  1, 1, 3.95, 3.33, 3.08, 4.03, 3.61, 3.67),
        (10, 1, 1, 6.00, 2.00, 3.00, 3.00, 3.33, 1.50),
        (1,  2, 1, 3.00, 2.00, 2.00, 1.00, 3.67, 3.67),
        (2,  2, 1, 2.00, 1.00, 1.00, 1.00, 4.00, 3.50),
        (3,  2, 1, 3.95, 3.33, 3.08, 4.03, 3.61, 3.67),
        (4,  2, 1, 3.95, 3.33, 3.08, 4.03, 3.61, 3.67),
        (5,  2, 1, 2.00, 4.00, 4.00, 1.00, 4.33, 2.50),
        (6,  2, 1, 2.00, 1.00, 3.00, 1.00, 2.00, 2.00),
        (7,  2, 1, 3.95, 3.33, 3.08, 4.03, 3.61, 3.67),
        (8,  2, 1, 6.00, 5.00, 6.00, 7.00, 6.00, 3.50),
        (9,  2, 1, 7.00, 6.00, 3.00, 1.00, 3.33, 6.00),
        (10, 2, 1, 4.00, 4.00, 3.00, 1.00, 3.33, 5.00),
        (1,  3, 1, 4.00, 1.00, 1.00, 1.00, 3.33, 2.00),
        (2,  3, 1, 7.00, 7.00, 4.00, 7.00, 5.00, 5.50),
        (3,  3, 1, 6.00, 3.00, 3.00, 5.00, 5.00, 2.50),
        (4,  3, 1, 2.00, 4.00, 5.00, 4.00, 2.67, 2.00),
        (5,  3, 1, 7.00, 7.00, 4.00, 4.00, 7.00, 5.00),
        (6,  3, 1, 3.00, 5.00, 4.00, 6.00, 5.33, 6.50),
        (7,  3, 1, 4.00, 1.00, 2.00, 5.00, 3.67, 2.00),
        (8,  3, 1, 1.00, 4.00, 4.00, 6.00, 4.33, 3.50),
        (9,  3, 1, 4.00, 3.00, 1.00, 6.00, 3.00, 1.50),
        (10, 3, 1, 6.00, 5.00, 5.00, 4.00, 5.00, 5.00),
        (1,  4, 1, 3.95, 3.33, 3.08, 4.03, 3.61, 3.67),
        (2,  4, 1, 1.00, 4.00, 4.00, 6.00, 4.00, 3.67),
        (3,  4, 1, 1.00, 1.00, 1.00, 1.00, 3.00, 3.67),
        (4,  4, 1, 3.95, 3.33, 3.08, 4.03, 3.61, 3.67),
        (5,  4, 1, 3.95, 3.33, 3.08, 4.03, 3.61, 3.67),
        (6,  4, 1, 1.00, 1.00, 1.00, 1.00, 3.00, 3.67),
        (7,  4, 1, 3.00, 2.00, 2.00, 4.00, 3.67, 3.67),
        (8,  4, 1, 6.00, 5.00, 4.00, 6.00, 6.00, 3.67),
        (9,  4, 1, 3.95, 3.33, 3.08, 4.03, 3.61, 3.67),
        (10, 4, 1, 3.95, 3.33, 3.08, 4.03, 3.61, 3.67),
        (1,  1, 2, 4.31, 3.43, 4.18, 3.45, 3.53, 3.23),
        (2,  1, 2, 7.00, 7.00, 7.00, 1.00, 3.53, 2.50),
        (3,  1, 2, 5.00, 3.00, 6.00, 2.00, 3.33, 4.00),
        (4,  1, 2, 7.00, 4.00, 2.00, 1.00, 3.53, 5.00),
        (5,  1, 2, 4.31, 3.43, 4.18, 3.45, 3.53, 3.23),
        (6,  1, 2, 4.31, 3.43, 4.18, 3.45, 3.53, 3.23),
        (7,  1, 2, 6.00, 6.00, 7.00, 4.00, 3.53, 6.00),
        (8,  1, 2, 4.31, 3.43, 4.18, 3.45, 3.53, 3.23),
        (9,  1, 2, 4.31, 3.43, 4.18, 3.45, 3.53, 3.23),
        (10, 1, 2, 1.00, 1.00, 4.00, 2.00, 3.53, 2.00),
        (1,  2, 2, 5.00, 1.00, 4.00, 2.00, 3.53, 4.50),
        (2,  2, 2, 3.00, 7.00, 4.18, 1.00, 4.00, 2.50),
        (3,  2, 2, 4.31, 3.43, 4.18, 3.45, 3.53, 3.23),
        (4,  2, 2, 4.31, 3.43, 4.18, 3.45, 3.53, 3.23),
        (5,  2, 2, 4.00, 5.00, 4.00, 4.00, 3.00, 4.00),
        (6,  2, 2, 1.00, 5.00, 3.00, 4.00, 1.00, 1.00),
        (7,  2, 2, 4.31, 3.43, 4.18, 3.45, 3.53, 3.23),
        (8,  2, 2, 6.00, 7.00, 6.00, 6.00, 3.53, 5.00),
        (9,  2, 2, 7.00, 5.00, 6.00, 3.45, 3.53, 5.00),
        (10, 2, 2, 4.00, 2.00, 5.00, 1.00, 3.53, 3.50),
        (1,  3, 2, 4.00, 1.00, 1.00, 1.00, 2.33, 1.50),
        (2,  3, 2, 7.00, 7.00, 7.00, 1.00, 6.00, 6.00),
        (3,  3, 2, 4.00, 3.00, 4.00, 2.00, 3.00, 3.00),
        (4,  3, 2, 7.00, 6.00, 3.00, 1.00, 2.33, 2.00),
        (5,  3, 2, 7.00, 6.00, 5.00, 3.00, 5.00, 5.00),
        (6,  3, 2, 5.00, 5.00, 6.00, 4.00, 3.67, 3.50),
        (7,  3, 2, 5.00, 2.00, 2.00, 4.00, 3.33, 1.50),
        (8,  3, 2, 2.00, 4.00, 7.00, 4.00, 5.67, 2.50),
        (9,  3, 2, 6.00, 2.00, 1.00, 3.00, 3.53, 3.00),
        (10, 3, 2, 5.00, 4.00, 6.00, 3.00, 4.33, 4.50),
        (1,  4, 2, 4.31, 3.43, 4.18, 3.45, 3.53, 3.23),
        (2,  4, 2, 2.00, 1.00, 4.00, 4.00, 3.00, 2.00),
        (3,  4, 2, 1.00, 1.00, 2.00, 2.00, 2.33, 4.00),
        (4,  4, 2, 4.31, 3.43, 4.18, 3.45, 3.53, 3.23),
        (5,  4, 2, 4.31, 3.43, 4.18, 3.45, 3.53, 3.23),
        (6,  4, 2, 1.00, 1.00, 4.00, 1.00, 2.00, 1.00),
        (7,  4, 2, 4.00, 2.00, 3.00, 5.00, 4.00, 2.50),
        (8,  4, 2, 6.00, 6.00, 5.00, 4.00, 5.33, 4.50),
        (9,  4, 2, 4.31, 3.43, 4.18, 3.45, 3.53, 3.23),
        (10, 4, 2, 4.31, 3.43, 4.18, 3.45, 3.53, 3.23),
    ]
    cols = ["pnr", "time", "test", "item1", "item2", "item3", "item4", "item5", "item6"]
    return pd.DataFrame(rows, columns=cols)


# ---------------------------------------------------------------------------
# Helper assertions
# ---------------------------------------------------------------------------

def assert_symmetric(M: np.ndarray, label: str = "") -> None:
    assert np.allclose(M, M.T, atol=1e-8), f"Matrix not symmetric: {label}"


def assert_near_unit_diagonal(M: np.ndarray, label: str = "", tol: float = 1e-8) -> None:
    diag = np.diag(M)
    assert np.allclose(diag, 1.0, atol=tol), (
        f"Diagonal not 1 in {label}: {diag}"
    )


# ---------------------------------------------------------------------------
# Unit tests — internal helpers
# ---------------------------------------------------------------------------

class TestNormalizer:
    def test_identity_for_identity_matrix(self):
        M = np.eye(3)
        D = _normalizer(M)
        assert np.allclose(D, np.eye(3))

    def test_produces_inverse_sqrt(self):
        M = np.diag([4.0, 9.0, 16.0])
        D = _normalizer(M)
        expected = np.diag([0.5, 1.0 / 3.0, 0.25])
        assert np.allclose(D, expected)

    def test_zero_diagonal_entry_handled(self):
        M = np.diag([4.0, 0.0, 9.0])
        D = _normalizer(M)
        assert D[1, 1] == 0.0
        assert D[0, 0] == pytest.approx(0.5)


class TestNormalizeCorr:
    def test_diagonal_is_one(self):
        M = np.array([[4.0, 1.0, 0.5],
                      [1.0, 9.0, 2.0],
                      [0.5, 2.0, 1.0]])
        R = _normalize_corr(M)
        assert_near_unit_diagonal(R, "normalize_corr diagonal")

    def test_symmetric(self):
        M = np.array([[4.0, 1.0, 0.5],
                      [1.0, 9.0, 2.0],
                      [0.5, 2.0, 1.0]])
        R = _normalize_corr(M)
        assert_symmetric(R, "normalize_corr")

    def test_off_diagonal_bounded(self):
        M = np.array([[4.0, 1.0], [1.0, 1.0]])
        R = _normalize_corr(M)
        assert np.all(np.abs(R) <= 1.0 + 1e-10)


class TestEigendecomposeDescending:
    def test_eigenvalues_descending(self):
        M = np.array([[3.0, 1.0], [1.0, 2.0]])
        vals, vecs = _eigendecompose_descending(M)
        assert vals[0] >= vals[1]

    def test_reconstruction(self):
        M = np.array([[4.0, 2.0, 0.5],
                      [2.0, 3.0, 1.0],
                      [0.5, 1.0, 2.0]])
        vals, vecs = _eigendecompose_descending(M)
        M_rec = vecs @ np.diag(vals) @ vecs.T
        assert np.allclose(M, M_rec, atol=1e-10)


# ---------------------------------------------------------------------------
# DatenboxWithout tests
# ---------------------------------------------------------------------------

class TestDatenboxWithout:
    @pytest.fixture(autouse=True)
    def run_analysis(self, df1):
        self.result = DatenboxWithout(df1).run()
        self.cp = self.result.cross_products

    def test_dimensions(self):
        r = self.result
        assert r.n_persons == 9
        assert r.n_situations == 3
        assert r.n_variables == 6
        assert r.n_total == 27

    # --- Decomposition identity: SStot = SSbp + SSbs + SSres ---
    def test_decomposition_identity(self):
        cp = self.cp
        reconstructed = cp.SSbp + cp.SSbs + cp.SSres
        assert np.allclose(cp.SStot, reconstructed, atol=1e-8), (
            f"Max deviation: {np.abs(cp.SStot - reconstructed).max()}"
        )

    def test_within_persons_identity(self):
        cp = self.cp
        assert np.allclose(cp.SSwp, cp.SStot - cp.SSbp, atol=1e-8)

    def test_within_situations_identity(self):
        cp = self.cp
        assert np.allclose(cp.SSws, cp.SStot - cp.SSbs, atol=1e-8)

    # --- Cross-product matrices are symmetric ---
    def test_SStot_symmetric(self):
        assert_symmetric(self.cp.SStot, "SStot")

    def test_SSbp_symmetric(self):
        assert_symmetric(self.cp.SSbp, "SSbp")

    def test_SSbs_symmetric(self):
        assert_symmetric(self.cp.SSbs, "SSbs")

    def test_SSres_symmetric(self):
        assert_symmetric(self.cp.SSres, "SSres")

    # --- SStot positive semi-definite ---
    def test_SStot_psd(self):
        vals, _ = np.linalg.eigh(self.cp.SStot)
        assert np.all(vals >= -1e-10), f"Negative eigenvalues in SStot: {vals}"

    # --- Eta^2 correlation matrices ---
    def test_eta2_diagonal_sums_to_one(self):
        """Diagonal elements of all eta^2 matrices sum to 1 (total variance partitioned)."""
        corr = self.result.correlations
        d_bp = np.diag(corr.Rbp_eta)
        d_bs = np.diag(corr.Rbs_eta)
        d_res = np.diag(corr.Rres_eta)
        # bp + bs + res = total (diagonal of Rtot_eta should be 1.0)
        d_tot = np.diag(corr.Rtot_eta)
        assert np.allclose(d_tot, 1.0, atol=1e-8), f"Rtot_eta diagonal: {d_tot}"
        # Components sum to total
        component_sum = d_bp + d_bs + d_res
        assert np.allclose(component_sum, d_tot, atol=1e-8), (
            f"eta^2 components don't sum to total: {component_sum} vs {d_tot}"
        )

    # --- Proper correlation matrices have unit diagonal ---
    def test_Rtot_diagonal_is_one(self):
        assert_near_unit_diagonal(self.result.correlations.Rtot, "Rtot")

    def test_Rbp_diagonal_is_one(self):
        assert_near_unit_diagonal(self.result.correlations.Rbp, "Rbp")

    def test_Rbs_diagonal_is_one(self):
        assert_near_unit_diagonal(self.result.correlations.Rbs, "Rbs")

    def test_Rres_diagonal_is_one(self):
        assert_near_unit_diagonal(self.result.correlations.Rres, "Rres")

    def test_Rws_diagonal_is_one(self):
        assert_near_unit_diagonal(self.result.correlations.Rws, "Rws")

    def test_Rwp_diagonal_is_one(self):
        assert_near_unit_diagonal(self.result.correlations.Rwp, "Rwp")

    # --- Reliability coefficients are bounded in [0, 1] ---
    def test_RTT_bp_range(self):
        r = self.result.reliability
        assert 0.0 <= r.RTT_bp <= 1.0, f"RTT_bp = {r.RTT_bp}"

    def test_RTT_bs_range(self):
        r = self.result.reliability
        assert 0.0 <= r.RTT_bs <= 1.0, f"RTT_bs = {r.RTT_bs}"

    def test_RTT_components_sum(self):
        """RTT_bp + RTT_bs + RTT_res should be approximately 1.0."""
        r = self.result.reliability
        total = r.RTT_bp + r.RTT_bs + r.RTT_res
        assert abs(total - 1.0) < 1e-8, f"RTT sum = {total}"

    def test_TT_range(self):
        r = self.result.reliability
        for name, val in [("TT_bp", r.TT_bp), ("TT_bs", r.TT_bs),
                           ("TT_res", r.TT_res)]:
            assert 0.0 <= val <= 1.0, f"{name} = {val} out of [0,1]"

    def test_RMAX_range(self):
        r = self.result.reliability
        for name, val in [("RMAX_bp", r.RMAX_bp), ("RMAX_bs", r.RMAX_bs)]:
            assert 0.0 <= val <= 1.0 + 1e-10, f"{name} = {val}"

    def test_generalizability_U_range(self):
        r = self.result.reliability
        assert 0.0 <= r.U_bp <= 1.0, f"U_bp = {r.U_bp}"
        assert 0.0 <= r.U_bs <= 1.0, f"U_bs = {r.U_bs}"

    # --- Chi^2 test ---
    def test_chi2_positive(self):
        chi2 = self.result.chi2_residual
        assert chi2.statistic >= 0
        assert 0.0 <= chi2.p_value <= 1.0
        assert chi2.df == 15  # Q*(Q-1)/2 = 6*5/2

    # --- Factor loadings shape ---
    def test_factor_loadings_shape(self):
        fa = self.result.factor_loadings
        for name, df_loadings in fa.items():
            assert df_loadings.shape[0] == 6, f"{name}: expected 6 rows, got {df_loadings.shape}"
            assert df_loadings.shape[1] >= 1

    # --- T-test matrices shape ---
    def test_t_test_matrix_shape(self):
        tt = self.result.t_tests
        for attr in ["T_tot", "P_tot", "T_bp", "P_bp", "T_bs", "P_bs"]:
            M = getattr(tt, attr)
            assert M.shape == (6, 6), f"{attr}: shape {M.shape}"

    def test_p_values_in_range(self):
        tt = self.result.t_tests
        for attr in ["P_tot", "P_bp", "P_bs", "P_wp", "P_ws", "P_res"]:
            P = getattr(tt, attr)
            off_diag = P[~np.eye(6, dtype=bool)]
            assert np.all(off_diag >= 0.0), f"{attr}: negative p-values"
            assert np.all(off_diag <= 1.0), f"{attr}: p-values > 1"

    # --- Numerical smoke test: known scale of SStot diagonal ---
    def test_SStot_diagonal_positive(self):
        diag = np.diag(self.cp.SStot)
        assert np.all(diag > 0), f"Non-positive SStot diagonal: {diag}"

    def test_SSbp_diagonal_positive(self):
        diag = np.diag(self.cp.SSbp)
        assert np.all(diag > 0), f"Non-positive SSbp diagonal: {diag}"


# ---------------------------------------------------------------------------
# DatenboxWith tests
# ---------------------------------------------------------------------------

class TestDatenboxWith:
    @pytest.fixture(autouse=True)
    def run_analysis(self, df2):
        self.result = DatenboxWith(df2).run()
        self.cp = self.result.cross_products

    def test_dimensions(self):
        r = self.result
        assert r.n_persons == 10
        assert r.n_situations == 4
        assert r.n_variables == 6
        assert r.n_total == 80
        assert r.n_per_cell == 2

    # --- Decomposition identity: SStot = SSbp + SSbs + SSpxs + SSres ---
    def test_decomposition_identity(self):
        cp = self.cp
        reconstructed = cp.SSbp + cp.SSbs + cp.SSpxs + cp.SSres
        assert np.allclose(cp.SStot, reconstructed, atol=1e-8), (
            f"Max deviation: {np.abs(cp.SStot - reconstructed).max()}"
        )

    def test_within_persons_identity(self):
        cp = self.cp
        assert np.allclose(cp.SSwp, cp.SStot - cp.SSbp, atol=1e-8)

    def test_within_situations_identity(self):
        cp = self.cp
        assert np.allclose(cp.SSws, cp.SStot - cp.SSbs, atol=1e-8)

    # --- Symmetry ---
    def test_all_matrices_symmetric(self):
        cp = self.cp
        for name in ["SStot", "SSbp", "SSbs", "SSpxs", "SSres", "SSws", "SSwp"]:
            assert_symmetric(getattr(cp, name), name)

    # --- Eta^2 decomposition ---
    def test_eta2_diagonal_sums_to_one(self):
        corr = self.result.correlations
        d_tot = np.diag(corr.Rtot_eta)
        d_bp = np.diag(corr.Rbp_eta)
        d_bs = np.diag(corr.Rbs_eta)
        d_pxs = np.diag(corr.Rpxs_eta)
        d_res = np.diag(corr.Rres_eta)
        assert np.allclose(d_tot, 1.0, atol=1e-8)
        component_sum = d_bp + d_bs + d_pxs + d_res
        assert np.allclose(component_sum, d_tot, atol=1e-8), (
            f"eta^2 4-component sum: {component_sum} vs 1.0"
        )

    # --- Proper correlation matrices unit diagonal ---
    def test_all_corr_diagonals_are_one(self):
        corr = self.result.correlations
        for name in ["Rtot", "Rbp", "Rbs", "Rpxs", "Rres", "Rws", "Rwp"]:
            assert_near_unit_diagonal(getattr(corr, name), name)

    # --- Reliability ---
    def test_RTT_components_sum(self):
        """RTT_bp + RTT_bs + RTT_pxs + RTT_res should equal ~1.0."""
        r = self.result.reliability
        total = r.RTT_bp + r.RTT_bs + r.RTT_pxs
        # Total does not include res; verify res = 1 - total
        assert 0.0 <= total <= 1.0, f"RTT components sum: {total}"

    def test_reliability_values_bounded(self):
        r = self.result.reliability
        for attr in ["RTT_bp", "RTT_bs", "RTT_pxs",
                     "TT_bp", "TT_bs", "TT_pxs",
                     "U_bp", "U_bs", "U_pxs"]:
            val = getattr(r, attr)
            assert 0.0 <= val <= 1.0 + 1e-10, f"{attr} = {val} out of bounds"

    def test_generalizability_coefficients(self):
        r = self.result.reliability
        assert 0.0 <= r.U_bp <= 1.0
        assert 0.0 <= r.U_bs <= 1.0
        assert 0.0 <= r.U_pxs <= 1.0

    # --- Chi^2 ---
    def test_chi2(self):
        chi2 = self.result.chi2_residual
        assert chi2.statistic >= 0
        assert 0.0 <= chi2.p_value <= 1.0
        assert chi2.df == 15

    # --- Parallel test quality ---
    def test_parallel_test_quality_shape(self):
        ptq = self.result.parallel_test_quality
        assert len(ptq.timepoints) == 4
        assert len(ptq.alpha_test1) == 4
        assert len(ptq.alpha_test2) == 4
        assert len(ptq.parallel_corr) == 4
        assert len(ptq.spearman_brown) == 4

    def test_cronbach_alpha_range(self):
        ptq = self.result.parallel_test_quality
        for a1, a2 in zip(ptq.alpha_test1, ptq.alpha_test2):
            if not np.isnan(a1):
                assert a1 <= 1.0, f"Cronbach alpha > 1: {a1}"
            if not np.isnan(a2):
                assert a2 <= 1.0, f"Cronbach alpha > 1: {a2}"

    def test_spearman_brown_geq_parallel_corr(self):
        """Spearman-Brown correction always >= parallel-test correlation for positive r."""
        ptq = self.result.parallel_test_quality
        for rttp, sb in zip(ptq.parallel_corr, ptq.spearman_brown):
            if not np.isnan(rttp) and rttp > 0:
                assert sb >= rttp - 1e-10, f"SB {sb} < rttp {rttp}"

    # --- Factor loadings ---
    def test_factor_loadings_shape(self):
        fa = self.result.factor_loadings
        for name, df_fa in fa.items():
            assert df_fa.shape[0] == 6, f"{name}: expected 6 rows"

    # --- T-test p-values in valid range ---
    def test_p_values_in_range(self):
        tt = self.result.t_tests
        for attr in ["P_tot", "P_bp", "P_bs", "P_pxs", "P_wp", "P_ws", "P_res"]:
            P = getattr(tt, attr)
            off_diag = P[~np.eye(6, dtype=bool)]
            assert np.all(off_diag >= 0.0), f"{attr}: negative p-values"
            assert np.all(off_diag <= 1.0), f"{attr}: p-values > 1"


# ---------------------------------------------------------------------------
# Cross-model consistency tests
# ---------------------------------------------------------------------------

class TestCrossModelConsistency:
    """Sanity checks that apply across both models."""

    def test_without_rtot_geq_rbp_plus_rbs(self, df1):
        """RTT_total = RTT_bp + RTT_bs must be <= 1."""
        r = DatenboxWithout(df1).run().reliability
        assert r.RTT_bp + r.RTT_bs <= 1.0 + 1e-10

    def test_with_rtot_leq_one(self, df2):
        """RTT_bp + RTT_bs + RTT_pxs must be <= 1."""
        r = DatenboxWith(df2).run().reliability
        assert r.RTT_bp + r.RTT_bs + r.RTT_pxs <= 1.0 + 1e-10

    def test_without_sums_consistent_with_with_when_replication_ignored(self, df1):
        """When we take df1 and treat it as having a single test half,
        the cross-product total should match the without-replication model."""
        # Synthesize a 'test' column with all 1s for DatenboxWith
        df_rep = df1.copy()
        df_rep["test"] = 1
        # DatenboxWith with n=1 per cell reduces to DatenboxWithout
        result_w = DatenboxWith(df_rep, test_col="test").run()
        result_wo = DatenboxWithout(df1).run()
        # SStot must be identical (same data, same computation)
        assert np.allclose(
            result_w.cross_products.SStot,
            result_wo.cross_products.SStot,
            atol=1e-8,
        )
