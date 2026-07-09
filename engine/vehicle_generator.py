import os
from engine.generator import generate


def generate_vehicles(project_name, count=30):

    folder = os.path.join(
        "projects",
        project_name,
        "Vehicles"
    )

    os.makedirs(folder, exist_ok=True)

    prompt = f"""
Create {count} vehicles.

Include:

Vehicle Name
Category
Top Speed
Description
"""

    result = generate(prompt)

    with open(
        os.path.join(folder, "vehicles.txt"),
        "w",
        encoding="utf-8"
    ) as file:
        file.write(result)

    return "✅ Vehicles generated successfully."