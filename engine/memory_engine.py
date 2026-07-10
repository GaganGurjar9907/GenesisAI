import json
import os


def save_project_data(project_name, data):
    """
    Save project memory data.
    Automatically creates the project folder if it doesn't exist.
    """

    project_folder = os.path.join("projects", project_name)

    # Create folder if it doesn't exist
    os.makedirs(project_folder, exist_ok=True)

    file_path = os.path.join(project_folder, "memory.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_project_data(project_name):
    """
    Load project memory data.
    Returns an empty dictionary if no memory file exists.
    """

    project_folder = os.path.join("projects", project_name)
    file_path = os.path.join(project_folder, "memory.json")

    if not os.path.exists(file_path):
        return {}

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)