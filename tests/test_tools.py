import unittest
from pathlib import Path

from src.tools import calculate_hours, make_checklist, search_notes


NOTES_PATH = Path(__file__).resolve().parent.parent / "data" / "notes.txt"


class TestTools(unittest.TestCase):
    def test_calculate_hours_from_days_then_daily_hours(self):
        self.assertEqual(
            calculate_hours("Plan for 3 days at 4 hours per day"),
            12,
        )

    def test_calculate_hours_from_daily_hours_then_days(self):
        self.assertEqual(
            calculate_hours("Work 4 hours per day for 3 days"),
            12,
        )

    def test_calculate_hours_ignores_unrelated_numbers(self):
        self.assertIsNone(calculate_hours("Build version 2 with 3 useful features"))

    def test_checklist_uses_whole_terms(self):
        plan = make_checklist("Build a RAG API")

        self.assertIn(
            "Prepare document loading, chunking, retrieval, and answer generation",
            plan,
        )
        self.assertIn(
            "Expose the workflow through a simple API endpoint",
            plan,
        )
        self.assertNotIn(
            "Expose the workflow through a simple API endpoint",
            make_checklist("Build a rapid prototype"),
        )

    def test_search_notes_prioritizes_relevant_lines(self):
        self.assertEqual(
            search_notes(NOTES_PATH, "RAG retrieval"),
            [
                "RAG project steps include document loading, chunking, "
                "retrieval, and answer generation."
            ],
        )

    def test_search_notes_ignores_generic_queries_and_missing_files(self):
        missing_path = Path(__file__).with_name("missing-notes.txt")

        self.assertEqual(search_notes(NOTES_PATH, "the and a"), [])
        self.assertEqual(search_notes(missing_path, "RAG retrieval"), [])


if __name__ == "__main__":
    unittest.main()
