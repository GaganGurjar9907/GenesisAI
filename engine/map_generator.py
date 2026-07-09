import os
from engine.generator import generate


def generate_map(project_name):

    folder = os.path.join(
        "projects",
        project_name,
        "Maps"
    )

    os.makedirs(folder, exist_ok=True)

    prompt = """
Design a complete open world game map.

Include:

Cities
Villages
Roads
Forest
Airport
Police Station
Hospital
Military Base
"""

    result = generate(prompt)

    with open(
        os.path.join(folder, "map.txt"),
        "w",
        encoding="utf-8"
    ) as file:
        file.write(result)

    return "✅ Map generated successfully."