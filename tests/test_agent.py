import unittest

from src.agent import TaskPlannerAgent, should_search_notes
from src.errors import InvalidGoalError


class TestTaskPlannerAgent(unittest.TestCase):
    def setUp(self):
        self.agent = TaskPlannerAgent()

    def test_run_selects_relevant_tools_and_builds_a_plan(self):
        result = self.agent.run(
            "Plan a RAG project for 3 days at 4 hours per day"
        )

        self.assertEqual(
            result["tools_used"],
            ["note_search", "calculator", "checklist_planner"],
        )
        self.assertTrue(result["notes"][0].startswith("RAG project steps"))
        self.assertIn("Time estimate: about 12 focused hours", result["plan"])

    def test_run_rejects_a_short_goal(self):
        with self.assertRaises(InvalidGoalError):
            self.agent.run("  ")

    def test_note_search_routing_matches_whole_keywords(self):
        self.assertTrue(should_search_notes("Prepare a RAG, workflow"))
        self.assertFalse(should_search_notes("Prepare a program"))


if __name__ == "__main__":
    unittest.main()
