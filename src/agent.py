from pathlib import Path

from src.tools import calculate_hours, make_checklist, search_notes


class TaskPlannerAgent:
    def __init__(self):
        self.notes_path = Path("data/notes.txt")

    def run(self, goal):
        tools_used = []
        notes = []

        if should_search_notes(goal):
            notes = search_notes(self.notes_path, goal)
            tools_used.append("note_search")

        total_hours = calculate_hours(goal)
        if total_hours:
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
    keywords = ["rag", "llm", "fastapi", "docker", "evaluation", "project"]
    lowered = goal.lower()
    return any(keyword in lowered for keyword in keywords)

