import os
from engine.generator import generate


def generate_npcs(project_name, count=25):

    folder = os.path.join(
        "projects",
        project_name,
        "Characters"
    )

    os.makedirs(folder, exist_ok=True)

    prompt = f"""
Create {count} unique NPCs.

For each NPC provide:

Name
Age
Occupation
Personality
Backstory
"""

    result = generate(prompt)

    with open(
        os.path.join(folder, "npcs.txt"),
        "w",
        encoding="utf-8"
    ) as file:
        file.write(result)

    return "✅ NPCs generated successfully."