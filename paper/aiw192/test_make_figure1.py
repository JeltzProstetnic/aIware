"""Figure 1 must plot the frozen run's numbers, not a re-derivation of them."""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("make_figure1", HERE / "make_figure1.py")
mf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mf)


def test_model_curves_come_from_primary_json():
    data = mf.load_panels()
    within, z = data["within"], data["z"]
    assert within["model"]["EWR"]["median"][9] == 0.278350920014038
    assert within["model"]["NE"]["lo"][0] == 0.22139474736371
    assert abs(z["model"]["NE"]["median"][9] - 0.397) < 1e-3
    assert len(within["model"]["E"]["hi"]) == 10


def test_observed_shares_come_from_pooled_decile_table():
    data = mf.load_panels()
    obs = data["z"]["observed"]
    # pooled z decile 10: 36 E, 11 EWR, 31 NE of 78
    assert obs["n"][9] == 78
    assert abs(obs["E"][9] - 36 / 78) < 1e-12
    assert abs(obs["EWR"][9] - 11 / 78) < 1e-12
    assert abs(obs["NE"][9] - 31 / 78) < 1e-12
    within = data["within"]["observed"]
    assert within["n"] == [78, 75, 72, 74, 67, 78, 74, 85, 75, 78]
