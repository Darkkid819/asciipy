import json
import os

CONFIG_PATH = os.path.join("assets", "config.json")

DEFAULT_CONFIG = {
    "frame_rate": 24,
    "resolution": "720p",
    "audio": True,
    "enhancements": {
        "brightness": 1.0,
        "contrast": 1.0
    }
}


def load_config():
    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(CONFIG_PATH, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG


def save_config(config):
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, 'w') as file:
        json.dump(config, file, indent=4)


def set_default_config():
    save_config(DEFAULT_CONFIG)
