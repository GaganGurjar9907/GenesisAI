import json
import os


class ProjectCreator:

    def create(self, project_name):

        project_path = os.path.join("projects", project_name)

        os.makedirs(project_path, exist_ok=True)

        files = {
            "config.json": {
                "project_name": project_name,
                "engine_version": "Genesis AI v0.7"
            },

            "story.json": {},

            "world.json": {},

            "npc.json": {},

            "vehicles.json": {},

            "missions.json": {},

            "economy.json": {},

            "traffic.json": {},

            "weather.json": {},

            "memory.json": {}
        }

        for filename, data in files.items():

            file_path = os.path.join(project_path, filename)

            if not os.path.exists(file_path):

                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"✅ Project '{project_name}' created successfully.")