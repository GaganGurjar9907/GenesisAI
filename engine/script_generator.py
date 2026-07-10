import json
import os


class ScriptGenerator:

    def __init__(self, project_name):

        self.project_name = project_name

        self.project_path = os.path.join(
            "projects",
            project_name
        )

    def generate(self, script_name, code):

        file_path = os.path.join(
            self.project_path,
            f"{script_name}.py"
        )

        with open(file_path, "w", encoding="utf-8") as file:

            file.write(code)

        print(f"✅ Script Generated -> {script_name}.py")