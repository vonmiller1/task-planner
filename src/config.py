import json
from pathlib import Path
from typing import Dict, Any


DEFAULT_CONFIG = {
    "max_tools": 5,
    "timeout_seconds": 30,
    "enable_logging": True,
    "log_dir": "logs",
    "auto_save_notes": True,
    "note_file_path": "data/notes.txt",
}


class ConfigManager:
    def __init__(self, config_file="config.json"):
        self.config_file = Path(config_file)
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file or use defaults."""
        config = DEFAULT_CONFIG.copy()
        if not self.config_file.exists():
            return config

        try:
            user_config = json.loads(
                self.config_file.read_text(encoding="utf-8")
            )
        except (json.JSONDecodeError, OSError) as error:
            print(f"Error reading {self.config_file}, using defaults: {error}")
            return config

        if not isinstance(user_config, dict):
            print(f"Invalid config in {self.config_file}, using defaults")
            return config

        config.update(user_config)
        self._validate_config(config)
        return config

    def _validate_config(self, config: Dict[str, Any]) -> None:
        max_tools = config.get("max_tools")
        if not isinstance(max_tools, int) or max_tools < 1:
            config["max_tools"] = DEFAULT_CONFIG["max_tools"]

        timeout_seconds = config.get("timeout_seconds")
        if not isinstance(timeout_seconds, (int, float)) or timeout_seconds <= 0:
            config["timeout_seconds"] = DEFAULT_CONFIG["timeout_seconds"]

    def save_config(self) -> None:
        """Save current configuration to file."""
        self.config_file.write_text(
            json.dumps(self.config, indent=2) + "\n",
            encoding="utf-8",
        )

    def get(self, key: str, default=None) -> Any:
        """Get configuration value."""
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set configuration value."""
        self.config[key] = value
