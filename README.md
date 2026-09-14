# ai-eval-starter

Starter for DZ0 AI Engineer briefs that EVALUATE — an eval harness that scores answers against a
gold set and decides ship/no-ship, with an LLM-as-judge you cannot fully trust.

## Run it (no key)
```bash
python3 --version && git --version
pip install -r requirements.txt
pytest -q
```

## What is here (input, not answers)
- `data/gold.jsonl` — questions, reference answers, a per-question rubric, and a `slice` label.
- `data/version_a.jsonl`, `data/version_b.jsonl` — two candidates. **B is better on average but
  REGRESSES on one slice** (`refunds`). An overall-average-only harness that ships B has failed —
  catching the slice regression is the project.
- `data/judge_fixture.jsonl` — recorded judge verdicts, including the hard cases you must handle:
  **low_confidence**, **self_inconsistent**, **malformed_json**. A malformed or unsure verdict must
  not silently count as a pass.

`fixture.py` only LOADS. The scorer, the slice aggregation, the ship/no-ship rule and the
uncertainty fallback are yours — the gold set is input, not a worked evaluator. A fixture is not
the model. Optional live judge via Ollama; never required, never graded.
