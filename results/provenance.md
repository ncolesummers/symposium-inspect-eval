# Provenance

## v1 (git tag v1)

- Dataset (data/abstracts.jsonl): git 4abd54f (2026-10-24); gold approved in bb14124 (2026-10-24)
- Prompt and rubric (task.py): git df9cf1d (2026-10-24)
- Workflow model: openai/gpt-6-luna; the API reported gpt-6-luna (no dated snapshot offered)
- Grader model: openai/gpt-6.1-sol; the API reported gpt-6.1-sol (no dated snapshot offered)
- Temperature: not set for either model, so the provider default applies (no temperature was sent in any request)
- Reasoning: Inspect asked only for a reasoning summary ('summary': 'auto'); reasoning effort was left at the provider default
- Inspect version: 0.3.278
- Runs: run-1 2026-10-24T21:17:40+00:00; run-2 2026-10-24T21:17:58+00:00; run-3 2026-10-24T21:18:15+00:00
- Repo commit recorded by Inspect: df9cf1d (dirty=True; tracked files were unmodified, only untracked files were present)

## v2 (git tag v2)

- Dataset (data/abstracts.jsonl): git 4abd54f (2026-10-24); gold approved in bb14124 (2026-10-24)
- Prompt and rubric (task.py): git b1b7f5d (2026-10-24)
- Workflow model: openai/gpt-6-luna; the API reported gpt-6-luna (no dated snapshot offered)
- Grader model: openai/gpt-6.1-sol; the API reported gpt-6.1-sol (no dated snapshot offered)
- Temperature: not set for either model, so the provider default applies (no temperature was sent in any request)
- Reasoning: Inspect asked only for a reasoning summary ('summary': 'auto'); reasoning effort was left at the provider default
- Inspect version: 0.3.278
- Runs: run-1 2026-10-24T21:34:14+00:00; run-2 2026-10-24T21:34:32+00:00; run-3 2026-10-24T21:34:54+00:00
- Repo commit recorded by Inspect: b1b7f5d (dirty=True; tracked files were unmodified, only untracked files were present)

### Why v2 exists

v1 passed 12/12 in all three runs and did not catch the abs-04 overreach ('including' for the abstract's 'specifically'), so it could not show the grader failing anything. v2 makes the workflow harder by adding a plain-language newsletter summary, the step most likely to overstate findings, and adds the summary to rubric line 1. The rubric now asks for 'GRADE: C' or 'GRADE: I', so v2 uses Inspect's default grade pattern instead of v1's custom first-letter pattern. The dataset, gold, models and temperature setting are unchanged.

### Model versions

`gpt-6-luna` and `gpt-6.1-sol` are not dated snapshots. The model behind each name can change, so a rerun later may not reproduce these results.
