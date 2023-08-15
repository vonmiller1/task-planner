import unittest
import json
import tempfile
import os

from src.config import ConfigManager, DEFAULT_CONFIG
from src.tools import calculate_hours


class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.config_manager = ConfigManager("test_config.json")
    
    def test_default_config_values(self):
        """Test that default config has expected keys."""
        self.assertIn("max_tools", DEFAULT_CONFIG)
        self.assertIn("timeout_seconds", DEFAULT_CONFIG)
        self.assertEqual(DEFAULT_CONFIG["max_tools"], 5)
    
    def test_config_get_method(self):
        """Test getting configuration values."""
        self.assertEqual(
            self.config_manager.get("max_tools"), 
            DEFAULT_CONFIG["max_tools"]
        )
    
    def test_config_set_method(self):
        """Test setting configuration values."""
        self.config_manager.set("max_tools", 10)
        self.assertEqual(self.config_manager.get("max_tools"), 10)
    
    def test_config_default_value(self):
        """Test default value when key doesn't exist."""
        result = self.config_manager.get("nonexistent", "default")
        self.assertEqual(result, "default")


class TestToolsModule(unittest.TestCase):
    def test_calculate_hours_basic(self):
        """Test basic hour calculation."""
        # This will fail because we're not importing tools
        result = calculate_hours("Plan for 3 days at 4 hours per day")
        self.assertEqual(result, 12)


if __name__ == "__main__":
    unittest.main()
