import json
import os


class ResourceManager:

    def __init__(self, project_name):

        self.project_name = project_name

        self.project_path = os.path.join(
            "projects",
            project_name
        )

    def load(self, filename):

        path = os.path.join(
            self.project_path,
            filename
        )

        if not os.path.exists(path):
            return {}

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, filename, data):

        path = os.path.join(
            self.project_path,
            filename
        )

        with open(path, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4
            )