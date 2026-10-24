"""Fetch 12 arXiv abstracts and draft gold targets with the grader model (Sol)."""

import json
import re
import urllib.request
import xml.etree.ElementTree as ET

from openai import OpenAI

ARXIV_IDS = [
    "2604.15334", "2601.09965", "2512.11882", "2409.15981",
    "2605.11155", "2504.09720", "2609.38029", "2512.04109",
    "2506.18941", "2501.10551", "2604.16213", "2507.20995",
]  # fmt: skip
GRADER_MODEL = "gpt-6.1-sol"
DRAFT_PROMPT = """Below is a research abstract. Write the gold answer for a claim-extraction task.
First write "Key claims:" and list two to four key claims, each stated no more strongly than the abstract states it. Keep every hedge (for example "suggest", "may", "preliminary", "pilot").
Then write "Not stated in the abstract:" and list what a reader would need to know that the abstract does not say (for example sample size, control condition, duration, population).
Use only the abstract. Plain text, no markdown formatting."""

ATOM = {"a": "http://www.w3.org/2005/Atom"}
url = "https://export.arxiv.org/api/query?max_results=20&id_list=" + ",".join(ARXIV_IDS)
feed = ET.fromstring(urllib.request.urlopen(url).read())
entries = {}
for e in feed.findall("a:entry", ATOM):
    versioned = e.findtext("a:id", namespaces=ATOM, default="").rsplit("/abs/", 1)[1]
    entries[re.sub(r"v\d+$", "", versioned)] = (versioned, e)

client = OpenAI()
rows = []
for n, arxiv_id in enumerate(ARXIV_IDS, start=1):
    versioned, e = entries[arxiv_id]
    abstract = " ".join(e.findtext("a:summary", namespaces=ATOM, default="").split())
    assert len(abstract.split()) < 250, arxiv_id
    draft = client.responses.create(
        model=GRADER_MODEL, instructions=DRAFT_PROMPT, input=abstract
    )
    rows.append(
        {
            "id": f"abs-{n:02d}",
            "title": " ".join(
                e.findtext("a:title", namespaces=ATOM, default="").split()
            ),
            "arxiv_id": versioned,
            "source_url": f"https://arxiv.org/abs/{versioned}",
            "input": abstract,
            "target": draft.output_text.strip(),
        }
    )
    print(rows[-1]["id"], draft.model)

with open("data/abstracts.jsonl", "w") as f:
    f.writelines(json.dumps(r) + "\n" for r in rows)
