import os

def list_projects():
    projects_folder = "projects"

    if not os.path.exists(projects_folder):
        print("No projects found.")
        return []

    projects = [
        folder
        for folder in os.listdir(projects_folder)
        if os.path.isdir(os.path.join(projects_folder, folder))
    ]

    if not projects:
        print("No projects found.")
        return []

    print("\n========== PROJECTS ==========")

    for i, project in enumerate(projects, start=1):
        print(f"{i}. {project}")

    print("==============================")

    return projects