"""fixture.py — loader for the eval gold set, candidate answers and judge verdicts. Loads only:
the scoring, the aggregation, the ship/no-ship rule and the uncertainty handling are your project."""
import json, os
_H=os.path.dirname(__file__)
def _read(name):
    with open(os.path.join(_H,"data",name),encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]
def gold(): return _read("gold.jsonl")
def version(name): return _read(f"version_{name}.jsonl")   # 'a','b'
def judge_cases(): return _read("judge_fixture.jsonl")
