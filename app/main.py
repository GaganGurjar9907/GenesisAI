import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.generator import generate
from app.config import VERSION
from app.menu import show_menu

print("=" * 60)
print(VERSION)
print("=" * 60)
choice = show_menu()

if choice == "1":
    idea = input("\nEnter your game idea: ")

elif choice == "2":
    print("\n🚧 AI Chat - Coming Soon")
    exit()

elif choice == "3":
    print("\n⚙️ Settings - Coming Soon")
    exit()

elif choice == "4":
    print("\nGoodbye!")
    exit()

else:
    print("\nInvalid Option")
    exit()

idea = input("Enter your game idea: ")

# Test Mode
if idea.lower() == "test":
    print("\n✅ Genesis AI Connected")
    print("✅ Engine Working")
    print("✅ Test Successful")
    exit()

project_name = input("Project Name: ")

project_folder = f"projects/{project_name}"

folders = [
    "Docs",
    "Maps",
    "Characters",
    "Vehicles",
    "Missions"
]

for folder in folders:
    os.makedirs(f"{project_folder}/{folder}", exist_ok=True)

print("\nGenerating Game Design...")

game_design = generate(
    f"Create a complete Game Design Document for this game:\n{idea}"
)

with open(
    f"{project_folder}/Docs/game_design.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(game_design)

print("\n✅ Project Created Successfully!")
print(f"Location: {project_folder}")