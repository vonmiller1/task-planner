import json
import tempfile
import unittest
from pathlib import Path

from src.config import ConfigManager, DEFAULT_CONFIG
from src.tools import calculate_hours


class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.config_path = Path(self.temp_dir.name) / "config.json"
        self.config_manager = ConfigManager(self.config_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_default_config_values(self):
        """Test that default config has expected keys."""
        self.assertIn("max_tools", DEFAULT_CONFIG)
        self.assertIn("timeout_seconds", DEFAULT_CONFIG)
        self.assertEqual(DEFAULT_CONFIG["max_tools"], 5)

    def test_config_get_method(self):
        """Test getting configuration values."""
        self.assertEqual(
            self.config_manager.get("max_tools"),
            DEFAULT_CONFIG["max_tools"],
        )

    def test_config_set_method(self):
        """Test setting configuration values."""
        self.config_manager.set("max_tools", 10)
        self.assertEqual(self.config_manager.get("max_tools"), 10)

    def test_config_default_value(self):
        """Test default value when key doesn't exist."""
        result = self.config_manager.get("nonexistent", "default")
        self.assertEqual(result, "default")

    def test_invalid_json_falls_back_to_defaults(self):
        self.config_path.write_text("{not valid json", encoding="utf-8")
        manager = ConfigManager(self.config_path)
        self.assertEqual(manager.get("max_tools"), DEFAULT_CONFIG["max_tools"])

    def test_invalid_max_tools_is_corrected(self):
        self.config_path.write_text(
            json.dumps({"max_tools": 0}),
            encoding="utf-8",
        )
        manager = ConfigManager(self.config_path)
        self.assertEqual(manager.get("max_tools"), DEFAULT_CONFIG["max_tools"])


class TestToolsModule(unittest.TestCase):
    def test_calculate_hours_basic(self):
        """Test basic hour calculation."""
        result = calculate_hours("Plan for 3 days at 4 hours per day")
        self.assertEqual(result, 12)


if __name__ == "__main__":
    unittest.main()
