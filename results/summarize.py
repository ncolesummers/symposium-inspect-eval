"""Read the v1 and v2 logs and write summary.md, candidates.md, provenance.md."""

import glob
import subprocess
from pathlib import Path

from inspect_ai.log import EvalLog, EvalSample, read_eval_log

# Where each version's three runs live.
VERSIONS = {"v1": "logs/run-{i}", "v2": "logs/v2/run-{i}"}

# Suggested picks from v2, chosen by reading every v2 run-1 output by hand.
# Each slot: (run, sample id, why it was suggested). Picks outside run-1 are marked.
CANDIDATES = {
    "Output 1: clear pass": [
        (
            "run-1",
            "abs-01",
            "Keeps every hedge, and the newsletter summary itself names the two main weaknesses: everyone did the video-only condition first, and the retention results are not reported.",
        ),
        (
            "run-1",
            "abs-11",
            "Shorter alternative. The abstract reports no results, and the summary says so plainly instead of inventing any.",
        ),
    ],
    "Output 2: disputed case": [
        (
            "run-1",
            "abs-04",
            "Same overreach as v1, now in the summary too. The abstract says 'significant improvements in learning outcomes, specifically a greater gain in grammar'. The claims say 'including a greater gain in grammar' and the summary says 'gains in learning, particularly grammar', which implies gains beyond grammar. Passed in all three v2 runs.",
        ),
        (
            "run-1",
            "abs-05",
            "Overreach in the summary that passed. The claims correctly limit the results to students 'around the score cutoff', but the summary reports them for 'this study of 635 students'. In run-3, the same grader failed a different abs-05 output for leaving out exactly this restriction.",
        ),
    ],
    "Output 3: clear fail": [
        (
            "run-3",
            "abs-05",
            "NOT FROM RUN-1: run-1 has no fails. The closest to a clear fail in any v2 run. The claims drop the 'around the cutoff' restriction and present the gains as applying to the whole spring program.",
        ),
        (
            "run-2",
            "abs-02",
            "NOT FROM RUN-1, and arguably a 'fails a defensible answer' case rather than a clear fail. The grader failed it because the 'not stated' list does not mention a control condition or the study's calendar duration, both of which are in the gold. The output is otherwise careful.",
        ),
    ],
}

WHY_V2 = (
    "v1 passed 12/12 in all three runs and did not catch the abs-04 overreach "
    "('including' for the abstract's 'specifically'), so it could not show the grader failing anything. "
    "v2 makes the workflow harder by adding a plain-language newsletter summary, the step most likely "
    "to overstate findings, and adds the summary to rubric line 1. The rubric now asks for 'GRADE: C' or "
    "'GRADE: I', so v2 uses Inspect's default grade pattern instead of v1's custom first-letter pattern. "
    "The dataset, gold, models and temperature setting are unchanged."
)


def run_logs(pattern: str) -> list[EvalLog]:
    return [
        read_eval_log(glob.glob(f"{pattern.format(i=i)}/*.eval")[0]) for i in (1, 2, 3)
    ]


def samples(log: EvalLog) -> dict:
    return {s.id: s for s in log.samples or []}


def grade(sample: EvalSample) -> str:
    score = next(iter((sample.scores or {}).values()))
    return str(score.value)


def git_hash(rev: str, path: str) -> str:
    cmd = ["git", "log", "-1", "--format=%h (%cs)", rev, "--", path]
    return subprocess.run(
        cmd, check=True, capture_output=True, text=True
    ).stdout.strip()


logs = {v: run_logs(p) for v, p in VERSIONS.items()}
ids = list(samples(logs["v1"][0]))
grades = {
    v: {sid: [grade(samples(log)[sid]) for log in runs] for sid in ids}
    for v, runs in logs.items()
}

# summary.md
summary = ["# Results summary: v1 and v2", "", "## Accuracy per run", ""]
summary += ["| Version | run-1 | run-2 | run-3 |", "|---|---|---|---|"]
for v in logs:
    cells = [
        f"{sum(grades[v][sid][r] == 'C' for sid in ids)}/{len(ids)}" for r in range(3)
    ]
    summary.append(f"| {v} | {' | '.join(cells)} |")
summary += ["", "## Grade per sample", ""]
summary += [
    "| Sample | v1 run-1 | v1 run-2 | v1 run-3 | v2 run-1 | v2 run-2 | v2 run-3 |"
]
summary += ["|---|---|---|---|---|---|---|"]
summary += [
    f"| {sid} | {' | '.join(grades['v1'][sid] + grades['v2'][sid])} |" for sid in ids
]
for v in logs:
    flipped = [str(sid) for sid in ids if len(set(grades[v][sid])) > 1]
    summary += [
        "",
        f"## Flipped between runs within {v}",
        "",
        ", ".join(flipped) or "None.",
    ]
Path("results/summary.md").write_text("\n".join(summary) + "\n")

# candidates.md
v2_runs = {f"run-{i}": samples(log) for i, log in enumerate(logs["v2"], start=1)}
cands = ["# Candidate outputs for the workshop packet (v2)", ""]
cands += [
    "Picks are from v2 run-1 unless marked otherwise. These are suggestions only. You choose.",
    "",
]
cands += ["v1 candidates: `git show v1:results/candidates.md`", ""]
for slot, picks in CANDIDATES.items():
    cands += [f"## {slot}", ""]
    for run, sid, why in picks:
        s = v2_runs[run][sid]
        score = next(iter((s.scores or {}).values()))
        cands += [f"### {sid} (v2 {run})", "", f"Why suggested: {why}", ""]
        cands += ["ABSTRACT", "", "```text", str(s.input), "```", ""]
        cands += ["MODEL OUTPUT", "", "```text", s.output.completion, "```", ""]
        cands += [
            f"GRADE: {score.value}",
            "",
            f"GRADER'S REASON: {score.explanation}",
            "",
            "---",
            "",
        ]
Path("results/candidates.md").write_text("\n".join(cands))


# provenance.md
def provenance(version: str) -> list[str]:
    runs = logs[version]
    ev = runs[0].eval
    first = (runs[0].samples or [])[0]
    models = {e.model: e.output.model for e in first.events if e.event == "model"}
    return [
        f"- Dataset (data/abstracts.jsonl): git {git_hash(version, 'data/abstracts.jsonl')}; gold approved in {git_hash(version, 'data/gold-review.md')}",
        f"- Prompt and rubric (task.py): git {git_hash(version, 'task.py')}",
        f"- Workflow model: {ev.model}; the API reported {models.get(ev.model)} (no dated snapshot offered)",
        f"- Grader model: openai/gpt-6.1-sol; the API reported {models.get('openai/gpt-6.1-sol')} (no dated snapshot offered)",
        "- Temperature: not set for either model, so the provider default applies (no temperature was sent in any request)",
        "- Reasoning: Inspect asked only for a reasoning summary ('summary': 'auto'); reasoning effort was left at the provider default",
        f"- Inspect version: {ev.packages.get('inspect_ai')}",
        "- Runs: "
        + "; ".join(f"run-{i} {log.eval.created}" for i, log in enumerate(runs, 1)),
        f"- Repo commit recorded by Inspect: {ev.revision.commit if ev.revision else 'n/a'} (dirty={ev.revision.dirty if ev.revision else 'n/a'}; tracked files were unmodified, only untracked files were present)",
    ]


prov = ["# Provenance", "", "## v1 (git tag v1)", ""] + provenance("v1")
prov += ["", "## v2 (git tag v2)", ""] + provenance("v2")
prov += ["", "### Why v2 exists", "", WHY_V2]
prov += [
    "",
    "### Model versions",
    "",
    "`gpt-6-luna` and `gpt-6.1-sol` are not dated snapshots. The model behind each name can change, so a rerun later may not reproduce these results.",
]
Path("results/provenance.md").write_text("\n".join(prov) + "\n")
