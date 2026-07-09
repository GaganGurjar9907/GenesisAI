import json
import os


class GameBlueprint:

    def __init__(self):

        self.data = {
            "title": "",
            "genre": "",
            "theme": "",
            "camera": "",
            "graphics": "",
            "world_size": "",
            "platforms": [],
            "players": 1,
            "target_fps": 60
        }

    def save(self, project_name):

        folder = os.path.join("projects", project_name)

        os.makedirs(folder, exist_ok=True)

        file_path = os.path.join(folder, "blueprint.json")

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)

        print("✅ Blueprint Saved")

    def load(self, project_name):

        file_path = os.path.join(
            "projects",
            project_name,
            "blueprint.json"
        )

        if not os.path.exists(file_path):
            return False

        with open(file_path, "r", encoding="utf-8") as file:
            self.data = json.load(file)

        return True

    def show(self):

        print("\n========== GAME BLUEPRINT ==========\n")

        for key, value in self.data.items():
            print(f"{key} : {value}")

        print("\n====================================")