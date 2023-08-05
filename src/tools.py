import re


def search_notes(path, query):
    if not path.exists():
        return []

    query_words = set(tokenize(query))
    notes = []

    for line in path.read_text(encoding="utf-8").splitlines():
        line_words = set(tokenize(line))
        if query_words & line_words:
            notes.append(line)

    return notes[:3]


def calculate_hours(goal):
    numbers = [int(value) for value in re.findall(r"\d+", goal)]

    if len(numbers) < 2:
        return None

    return numbers[0] * numbers[1]


def make_checklist(goal, total_hours=None):
    plan = [
        "Clarify the expected input and output",
        "Create a small working version first",
        "Test the main workflow with sample data",
        "Write setup instructions in the README",
    ]

    if "rag" in goal.lower():
        plan.insert(1, "Prepare document loading, chunking, retrieval, and answer generation")

    if "api" in goal.lower() or "fastapi" in goal.lower():
        plan.insert(2, "Expose the workflow through a simple API endpoint")

    if total_hours:
        plan.append(f"Time estimate: about {total_hours} focused hours")

    return plan


def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())

