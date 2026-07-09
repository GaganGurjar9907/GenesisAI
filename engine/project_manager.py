import os
from engine.memory_engine import save_project_data


def create_project(project_name, idea=""):

    folders = [
        "Docs",
        "Maps",
        "Characters",
        "Vehicles",
        "Missions",
        "Scripts",
        "Audio",
        "UI"
    ]

    base = os.path.join("projects", project_name)

    os.makedirs(base, exist_ok=True)

    for folder in folders:
        os.makedirs(os.path.join(base, folder), exist_ok=True)

    memory = {
        "project_name": project_name,
        "idea": idea,
        "story": "",
        "characters": [],
        "vehicles": [],
        "missions": [],
        "map": "",
        "version": "0.4"
    }

    save_project_data(project_name, memory)

    print(f"\n✅ Project '{project_name}' Created Successfully!")