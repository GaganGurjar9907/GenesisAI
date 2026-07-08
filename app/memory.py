import json
import os


def save_memory(project_name, data):
    folder = os.path.join("projects", project_name)
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, "memory.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("✅ Memory Saved Successfully")


def load_memory(project_name):
    file_path = os.path.join("projects", project_name, "memory.json")

    if not os.path.exists(file_path):
        return {}

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)