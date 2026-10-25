# Testing for Failure: a small Inspect evaluation

## What this is

A small evaluation of an AI workflow that extracts key claims from research abstracts, built for the workshop "Testing for Failure: Evaluating AI Research Workflows with Inspect" at the University of Idaho AI Symposium, October 29, 2026. It uses 12 public arXiv abstracts about AI tutoring, one prompt, and a scorer in which a second AI model grades each answer. Two versions were each run three times.

## What it found

| Version | run-1 | run-2 | run-3 |
|---|---|---|---|
| v1 | 12/12 | 12/12 | 12/12 |
| v2 | 12/12 | 11/12 | 11/12 |

v1 passed everything, including an abs-04 answer that turned the abstract's "specifically a greater gain in grammar" into "including a greater gain in grammar". So v2 made the workflow harder by adding a plain-language summary for the grader to check.

In v2, abs-02 failed only in run-2 and abs-05 only in run-3, with identical settings. The abs-04 overreach passed all three v2 runs.

This is bounded evidence: 12 samples, 3 runs per version. It shows these failures can happen and that the grader can miss them. It does not measure how often the model fails.

## How it works

All in `task.py`:

- **Dataset** (line 25): the abstracts in `data/abstracts.jsonl`, each with a gold answer drafted by the grader model and reviewed by a person.
- **Solver** (line 27): gives `gpt-6-luna` the prompt (lines 9 to 14) and the abstract.
- **Scorer** (line 29): `gpt-6.1-sol` compares the answer with the gold answer and grades it C (pass) or I (fail), with a reason.
- **Log**: Inspect saves one `.eval` file per run with every prompt, answer, grade and reason.

Temperature is not set, so OpenAI's default applies. The v2 rubric as it ran (lines 16 to 18):

```text
1. No claim, including the summary, is stated more strongly than the abstract's own wording.
2. The abstract's major findings are present.
3. Missing information is named. Begin your reply with GRADE: C or GRADE: I, then give a one-sentence reason.
```

v1's rubric lacked "including the summary" and ended "Grade C if all three hold, otherwise I. Give a one-sentence reason."

## How to rerun it

You need [uv](https://docs.astral.sh/uv/) and an OpenAI API key.

```sh
git clone https://github.com/ncolesummers/symposium-inspect-eval
cd symposium-inspect-eval
uv sync
export OPENAI_API_KEY=your-key-here
uv run inspect eval task.py --model openai/gpt-6-luna --log-dir logs/my-run
uv run inspect view --log-dir logs/my-run
```

For v1, run `git checkout v1` first. Each version makes 36 generations and 36 grades; at October 2026 prices that cost about 4 cents per run, or 10 to 15 cents per version. `gpt-6-luna` and `gpt-6.1-sol` are not dated snapshots, so results will drift.

## Files

| Path | Contents |
|---|---|
| `data/` | abstracts, gold answers, review sheet, build script |
| `task.py` | the evaluation |
| `logs/run-1..3` | v1 logs |
| `logs/v2/run-1..3` | v2 logs |
| `results/summary.md` | every grade, per run |
| `results/candidates.md` | example outputs for the workshop |
| `results/provenance.md` | versions, hashes, run dates |
| `results/scorer-check.md` | grader check on hand-written answers |

The code is MIT licensed. The abstracts in `data/abstracts.jsonl` are the authors' own words, taken from arXiv and quoted for evaluation and teaching: [abs-01](https://arxiv.org/abs/2604.15334v1), [02](https://arxiv.org/abs/2601.09965v1), [03](https://arxiv.org/abs/2512.11882v1), [04](https://arxiv.org/abs/2409.15981v1), [05](https://arxiv.org/abs/2605.11155v1), [06](https://arxiv.org/abs/2504.09720v3), [07](https://arxiv.org/abs/2609.38029v1), [08](https://arxiv.org/abs/2512.04109v1), [09](https://arxiv.org/abs/2506.18941v1), [10](https://arxiv.org/abs/2501.10551v5), [11](https://arxiv.org/abs/2604.16213v1), [12](https://arxiv.org/abs/2507.20995v1).

## Provenance

See [`results/provenance.md`](results/provenance.md) and the tags [v1](https://github.com/ncolesummers/symposium-inspect-eval/tree/v1) and [v2](https://github.com/ncolesummers/symposium-inspect-eval/tree/v2).

## Workshop

Presented at the University of Idaho AI Symposium on October 29, 2026. Companion artifact: [claude.ai/artifact/7gmuhExTHzYgXrMZuVp1KR](https://claude.ai/artifact/7gmuhExTHzYgXrMZuVp1KR#delegate).
