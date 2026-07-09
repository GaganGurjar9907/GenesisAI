import os
from engine.generator import generate


def execute_command(project_name, command):

    command = command.lower()

    if "mission" in command:

        missions_folder = os.path.join(
            "projects",
            project_name,
            "Missions"
        )

        os.makedirs(missions_folder, exist_ok=True)

        prompt = (
            "Create 10 game missions with title and description "
            "for this game:\n" + command
        )

        result = generate(prompt)

        with open(
            os.path.join(missions_folder, "missions.txt"),
            "w",
            encoding="utf-8"
        ) as file:
            file.write(result)

        return "✅ Missions generated successfully."

    return None