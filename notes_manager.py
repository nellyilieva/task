import json
import os

STORAGE_PATH = os.path.join(os.path.dirname(__file__), "notes.json")


def load_notes():
    if not os.path.exists(STORAGE_PATH):
        return {"next_id": 1, "notes": []}
    with open(STORAGE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_notes(data):
    with open(STORAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)