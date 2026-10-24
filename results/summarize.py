"""Read logs/run-1..3 and write summary.md, candidates.md, provenance.md."""

import glob
import subprocess
from pathlib import Path

from inspect_ai.log import EvalLog, EvalSample, read_eval_log

# Suggested picks from run 1, chosen by reading every run-1 output by hand.
# Each slot: (sample id, why it was suggested). An empty list means nothing fits.
CANDIDATES = {
    "Output 1: clear pass": [
        (
            "abs-01",
            "Keeps every hedge, notes that the 2-week retention results are missing, and names the main weakness: everyone did the video-only condition first.",
        ),
        (
            "abs-12",
            "Shorter alternative for a slide. Adds no numbers to an abstract that has none, and asks what 'most' means.",
        ),
    ],
    "Output 2: disputed case": [
        (
            "abs-04",
            "Possible overreach that passed. The abstract says 'significant improvements in learning outcomes, specifically a greater gain in grammar'. The output says 'including a greater gain in grammar', which implies other learning gains the abstract does not claim.",
        ),
        (
            "abs-07",
            "Understatement that passed. The abstract says the findings 'indicate' GenAI 'can move' learning; the output says they are 'suggesting' it was 'associated with movement'. Rubric line 1 only forbids stating claims more strongly, so the grader cannot penalize misrepresenting the authors in the cautious direction.",
        ),
    ],
    "Output 3: clear fail": [],
}


def run_logs() -> list[EvalLog]:
    return [read_eval_log(glob.glob(f"logs/run-{i}/*.eval")[0]) for i in (1, 2, 3)]


def grade(sample: EvalSample) -> str:
    score = next(iter((sample.scores or {}).values()))
    return str(score.value)


def git_hash(path: str) -> str:
    cmd = ["git", "log", "-1", "--format=%h (%cs)", "--", path]
    return subprocess.run(
        cmd, check=True, capture_output=True, text=True
    ).stdout.strip()


logs = run_logs()
ids = [s.id for s in logs[0].samples or []]
grades = {s.id: [grade(s)] for s in logs[0].samples or []}
for log in logs[1:]:
    for s in log.samples or []:
        grades[s.id].append(grade(s))

summary = ["# Results summary", "", "## Accuracy per run", ""]
for i, log in enumerate(logs, start=1):
    n_c = sum(grades[sid][i - 1] == "C" for sid in ids)
    summary.append(f"- run-{i}: {n_c}/{len(ids)} graded C ({n_c / len(ids):.0%})")
summary += ["", "## Grade per sample", "", "| Sample | run-1 | run-2 | run-3 |"]
summary += ["|---|---|---|---|"] + [
    f"| {sid} | {' | '.join(grades[sid])} |" for sid in ids
]
flipped = [str(sid) for sid in ids if len(set(grades[sid])) > 1]
summary += ["", "## Flipped between runs", "", ", ".join(flipped) or "None."]
Path("results/summary.md").write_text("\n".join(summary) + "\n")

run1 = {s.id: s for s in logs[0].samples or []}
cands = ["# Candidate outputs for the workshop packet (from run-1)", ""]
cands += ["These are suggestions only. You choose.", ""]
for slot, picks in CANDIDATES.items():
    cands += [f"## {slot}", ""]
    if not picks:
        cands += [
            "No candidate: the grader gave C to every sample in all three runs.",
            "",
        ]
    for sid, why in picks:
        s = run1[sid]
        score = next(iter((s.scores or {}).values()))
        cands += [
            f"### {sid}",
            "",
            f"Why suggested: {why}",
            "",
            "ABSTRACT",
            "",
            "```text",
            str(s.input),
            "```",
            "",
        ]
        cands += [
            "MODEL OUTPUT",
            "",
            "```text",
            s.output.completion,
            "```",
            "",
            f"GRADE: {score.value}",
            "",
        ]
        cands += [f"GRADER'S REASON: {score.explanation}", "", "---", ""]
Path("results/candidates.md").write_text("\n".join(cands))

ev = logs[0].eval
models = {
    e.model: e.output.model
    for e in (logs[0].samples or [])[0].events
    if e.event == "model"
}
prov = [
    "# Provenance",
    "",
    f"- Dataset (data/abstracts.jsonl): git {git_hash('data/abstracts.jsonl')}; gold approved in {git_hash('data/gold-review.md')}",
    f"- Prompt and rubric (task.py): git {git_hash('task.py')}",
    f"- Workflow model: {ev.model}; the API reported {models.get(ev.model)} (no dated snapshot offered)",
    f"- Grader model: openai/gpt-6.1-sol; the API reported {models.get('openai/gpt-6.1-sol')} (no dated snapshot offered)",
    "- Temperature: not set for either model, so the provider default applies (no temperature was sent in any request)",
    "- Reasoning: Inspect asked only for a reasoning summary ('summary': 'auto'); reasoning effort was left at the provider default",
    f"- Inspect version: {ev.packages.get('inspect_ai')}",
    "- Runs: "
    + "; ".join(f"run-{i} {log.eval.created}" for i, log in enumerate(logs, 1)),
    f"- Repo commit recorded by Inspect: {ev.revision.commit if ev.revision else 'n/a'} (dirty={ev.revision.dirty if ev.revision else 'n/a'}; tracked files were unmodified, only untracked files were present)",
]
Path("results/provenance.md").write_text("\n".join(prov) + "\n")
