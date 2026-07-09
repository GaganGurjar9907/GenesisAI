import os
from engine.generator import generate


def generate_missions(project_name, count=10):

    missions_folder = os.path.join(
        "projects",
        project_name,
        "Missions"
    )

    os.makedirs(missions_folder, exist_ok=True)

    prompt = f"""
Create {count} unique game missions.
For each mission provide:
- Mission Title
- Objective
- Reward
"""

    result = generate(prompt)

    with open(
        os.path.join(missions_folder, "missions.txt"),
        "w",
        encoding="utf-8"
    ) as file:
        file.write(result)

    return "✅ Missions generated successfully."