import json
from pathlib import Path
from typing import Dict, Any


DEFAULT_CONFIG = {
    "max_tools": 5,
    "timeout_seconds": 30,
    "enable_logging": True,
    "log_dir": "logs",
    "auto_save_notes": True,
    "note_file_path": "data/notes.txt"
}


class ConfigManager:
    def __init__(self, config_file="config.json"):
        self.config_file = Path(config_file)
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file or use defaults."""
        config = DEFAULT_CONFIG.copy()  # Start with defaults
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    user_config = json.load(f)
                    # Merge user config with defaults
                    config.update(user_config)
                    return config
            except json.JSONDecodeError:
                print(f"Error reading {self.config_file}, using defaults")
                return config
        return config
    
    def save_config(self) -> None:
        """Save current configuration to file."""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def get(self, key: str, default=None) -> Any:
        """Get configuration value."""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value."""
        self.config[key] = value
