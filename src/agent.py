from pathlib import Path

from src.errors import validate_goal
from src.tools import calculate_hours, make_checklist, search_notes, tokenize


class TaskPlannerAgent:
    def __init__(self):
        self.notes_path = Path(__file__).resolve().parent.parent / "data" / "notes.txt"

    def run(self, goal):
        validate_goal(goal)
        goal = goal.strip()
        tools_used = []
        notes = []

        if should_search_notes(goal):
            notes = search_notes(self.notes_path, goal)
            tools_used.append("note_search")

        total_hours = calculate_hours(goal)
        if total_hours is not None:
            tools_used.append("calculator")

        plan = make_checklist(goal, total_hours=total_hours)
        tools_used.append("checklist_planner")

        return {
            "goal": goal,
            "tools_used": tools_used,
            "plan": plan,
            "notes": notes,
        }


def should_search_notes(goal):
    keywords = {"rag", "llm", "fastapi", "docker", "evaluation", "project"}
    return bool(keywords.intersection(tokenize(goal)))
