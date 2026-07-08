import json
import os


def save_project_data(project_name, data):

    file_path = os.path.join(
        "projects",
        project_name,
        "memory.json"
    )

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_project_data(project_name):

    file_path = os.path.join(
        "projects",
        project_name,
        "memory.json"
    )

    if not os.path.exists(file_path):
        return {}

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)