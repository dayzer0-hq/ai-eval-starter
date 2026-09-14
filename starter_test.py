"""Smoke test: gold set, two versions, and the tricky judge verdicts are present. B regresses on
one slice — catching that is the project, so this only checks the material is here."""
from fixture import gold, version, judge_cases
def test_gold_and_versions():
    assert gold() and version("a") and version("b")
def test_judge_has_the_hard_cases():
    kinds={c["kind"] for c in judge_cases()}
    assert {"low_confidence","self_inconsistent","malformed_json"} <= kinds, kinds
def test_a_slice_exists_to_regress_on():
    assert len({g["slice"] for g in gold()}) >= 2
