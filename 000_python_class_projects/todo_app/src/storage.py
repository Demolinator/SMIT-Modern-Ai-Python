import json
from pathlib import Path

DATA_PATH = Path("data/tasks.json")

def load_tasks():
    if DATA_PATH.exists():
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_PATH, "w") as f:
        json.dump(tasks, f, indent=2)