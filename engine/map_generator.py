import os

from engine.generator import generate
from engine.memory_engine import (
    load_project_data,
    save_project_data
)


def generate_map(project_name, game_idea):

    folder = os.path.join(
        "projects",
        project_name,
        "Maps"
    )

    os.makedirs(folder, exist_ok=True)

    prompt = f"""
Design a complete game world.

Game Idea:
{game_idea}

Create:

- World Theme
- Cities
- Villages
- Highways
- Small Roads
- Forests
- Rivers
- Mountains
- Airport
- Railway Station
- Police Stations
- Hospitals
- Military Bases
- Ports
- Industrial Areas
- Tourist Places

Explain every location in detail.
"""

    world = generate(prompt)

    with open(
        os.path.join(folder, "map.txt"),
        "w",
        encoding="utf-8"
    ) as file:
        file.write(world)

    data = load_project_data(project_name)

    data["map"] = world

    save_project_data(project_name, data)

    return world