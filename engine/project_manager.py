import os


def create_project(project_name):
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

    print(f"\n✅ Project '{project_name}' Created Successfully!")