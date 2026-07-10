import json
import os


def generate_world(project_name):

    world = {

        "world_name": project_name,

        "world_type": "Open World",

        "cities": [
            "Metro City",
            "Old Town",
            "Industrial Area"
        ],

        "villages": [
            "Green Village",
            "River Village"
        ],

        "roads": [
            "Highway",
            "City Roads",
            "Village Roads"
        ],

        "mountains": [
            "North Mountains"
        ],

        "rivers": [
            "Blue River"
        ],

        "forest": [
            "Dark Forest"
        ]
    }

    world_file = os.path.join(
        "projects",
        project_name,
        "world.json"
    )

    with open(world_file, "w", encoding="utf-8") as file:
        json.dump(
            world,
            file,
            indent=4,
            ensure_ascii=False
        )

    return world