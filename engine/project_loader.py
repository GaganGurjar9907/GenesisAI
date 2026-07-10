import json
import os


class ProjectLoader:

    def load(self, project_name):

        project_folder = os.path.join(
            "projects",
            project_name
        )

        files = [

            "config.json",
            "story.json",
            "world.json",
            "npc.json",
            "vehicles.json",
            "missions.json",
            "assets.json",
            "memory.json"

        ]

        data = {}

        for file in files:

            path = os.path.join(project_folder, file)

            if os.path.exists(path):

                with open(path, "r", encoding="utf-8") as f:

                    data[file] = json.load(f)

        print("✅ Project Loaded Successfully")

        return data