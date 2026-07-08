import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.generator import generate
from engine.project_manager import create_project
from engine.loader import list_projects
from app.config import VERSION
from app.menu import show_menu

print("=" * 60)
print(VERSION)
print("=" * 60)

choice = show_menu()

if choice == "1":

    project_name = input("\nProject Name: ")
    idea = input("Enter your game idea: ")

    if idea.lower() == "test":
        print("\n✅ Genesis AI Connected")
        exit()

    create_project(project_name)

    print("\nGenerating Game Design...")

    game_design = generate(
        f"Create a complete Game Design Document for this game:\n{idea}"
    )

    project_folder = f"projects/{project_name}"

    with open(
        f"{project_folder}/Docs/game_design.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(game_design)

    print("\n✅ Project Created Successfully!")
    print(f"Location: {project_folder}")

elif choice == "2":

    projects = list_projects()

    if len(projects) == 0:
        print("\nNo Projects Available.")

    else:
        project_no = int(input("\nSelect Project Number: "))

        selected_project = projects[project_no - 1]

        print(f"\n✅ Project Loaded: {selected_project}")

elif choice == "3":
    print("\n🤖 AI Chat - Coming Soon")

elif choice == "4":
    print("\n⚙️ Settings - Coming Soon")

elif choice == "5":
    print("\n👋 Goodbye!")

else:
    print("\n❌ Invalid Option")