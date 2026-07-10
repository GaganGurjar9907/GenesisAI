import json
import os


def generate_missions(project_name):

    missions = {

        "main_missions": [
            "First Job",
            "Escape Mission",
            "Gang War"
        ],

        "side_missions": [
            "Taxi Driver",
            "Delivery",
            "Street Race"
        ],

        "rewards": {
            "money": 5000,
            "xp": 250
        },

        "difficulty": "Normal"
    }

    mission_file = os.path.join(
        "projects",
        project_name,
        "missions.json"
    )

    with open(mission_file, "w", encoding="utf-8") as file:
        json.dump(
            missions,
            file,
            indent=4,
            ensure_ascii=False
        )

    return missions