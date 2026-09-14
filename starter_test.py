"""Smoke test: gold sets large enough that a single flipped answer is detectable-not-decisive, and
the hard judge verdicts exist. Passes out of the box."""
import os, json
D=os.path.join(os.path.dirname(__file__),"data")
def _rows(p): return [json.loads(l) for l in open(p) if l.strip()]
def test_gold_sets_are_big_enough_to_detect_a_regression():
    for n in ["cred","razorpay"]:
        g=_rows(os.path.join(D,n,"gold.jsonl"))
        slices={x["slice"] for x in g}
        assert len(g)>=30 and len(slices)>=4, f"{n}: gold too small ({len(g)} q / {len(slices)} slices)"
        per={s:sum(1 for x in g if x["slice"]==s) for s in slices}
        assert min(per.values())>=5, f"{n}: a slice too small to detect a regression: {per}"
def test_version_b_regresses_on_one_slice():
    g={x["id"]:x for x in _rows(os.path.join(D,"cred","gold.jsonl"))}
    vb=_rows(os.path.join(D,"cred","version_b.jsonl"))
    wrong_slices={g[v["id"]]["slice"] for v in vb if v["answer"]!=g[v["id"]]["reference"]}
    assert len(wrong_slices)==1, f"B should regress on exactly one slice, got {wrong_slices}"
def test_judge_has_the_hard_cases():
    ks={json.loads(l).get("kind") for l in open(os.path.join(D,"razorpay","judge_fixture.jsonl")) if l.strip()}
    assert {"low_confidence","self_inconsistent","malformed_json"} <= ks, ks
