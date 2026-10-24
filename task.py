from inspect_ai import Task, task
from inspect_ai.dataset import json_dataset
from inspect_ai.scorer import model_graded_qa
from inspect_ai.solver import generate, system_message

WORKFLOW_MODEL = "openai/gpt-6-luna"
GRADER_MODEL = "openai/gpt-6.1-sol"

PROMPT = (
    "Extract the key claims from this abstract. "
    "State each claim no more strongly than the abstract does. "
    "Then list what a reader would need to know that the abstract does not say. "
    "Finally, write a two-sentence plain-language summary of the findings for a faculty newsletter."
)

RUBRIC = """1. No claim, including the summary, is stated more strongly than the abstract's own wording.
2. The abstract's major findings are present.
3. Missing information is named. Begin your reply with GRADE: C or GRADE: I, then give a one-sentence reason."""


@task
def claim_extraction() -> Task:
    return Task(
        # Dataset: 12 research abstracts, each paired with a human-checked gold answer.
        dataset=json_dataset("data/abstracts.jsonl"),
        # Solver: give the model the extraction prompt, then let it answer.
        solver=[system_message(PROMPT), generate()],
        # Scorer: a second model compares the answer to the gold and grades it C or I.
        scorer=model_graded_qa(instructions=RUBRIC, model=GRADER_MODEL),
        model=WORKFLOW_MODEL,
    )
