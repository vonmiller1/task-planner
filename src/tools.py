import re


STOP_WORDS = frozenset(
    {
        "a", "an", "and", "are", "as", "at", "be", "by", "create", "for",
        "from", "goal", "help", "hours", "in", "into", "is", "it", "make",
        "of", "on", "or", "per", "plan", "project", "day", "days", "small",
        "task", "that", "the", "this", "to", "with", "work",
    }
)


def search_notes(path, query):
    if not path.is_file():
        return []

    query_words = {
        word for word in tokenize(query)
        if word not in STOP_WORDS and not word.isdigit()
    }
    if not query_words:
        return []

    matches = []
    for index, line in enumerate(path.read_text(encoding="utf-8").splitlines()):
        line_words = {
            word for word in tokenize(line)
            if word not in STOP_WORDS and not word.isdigit()
        }
        overlap = query_words.intersection(line_words)
        if overlap:
            matches.append((len(overlap), index, line))

    matches.sort(key=lambda match: (-match[0], match[1]))
    return [line for _, _, line in matches[:3]]


def calculate_hours(goal):
    patterns = (
        (
            r"\b(\d+)\s+days?\b.{0,40}?\b(\d+)\s+hours?\s+(?:per|a)\s+day\b",
            lambda match: int(match.group(1)) * int(match.group(2)),
        ),
        (
            r"\b(\d+)\s+hours?\s+(?:per|a)\s+day\b.{0,40}?\b(\d+)\s+days?\b",
            lambda match: int(match.group(1)) * int(match.group(2)),
        ),
    )
    for pattern, calculate in patterns:
        match = re.search(pattern, goal.lower())
        if match:
            return calculate(match)
    return None


def make_checklist(goal, total_hours=None):
    plan = [
        "Clarify the expected input and output",
        "Create a small working version first",
        "Test the main workflow with sample data",
        "Write setup instructions in the README",
    ]
    goal_words = set(tokenize(goal))

    if "rag" in goal_words:
        plan.insert(1, "Prepare document loading, chunking, retrieval, and answer generation")

    if {"api", "fastapi"}.intersection(goal_words):
        plan.insert(2, "Expose the workflow through a simple API endpoint")

    if total_hours is not None:
        plan.append(f"Time estimate: about {total_hours} focused hours")

    return plan


def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())
