import json
import os


def generate_npcs(project_name):

    npcs = {

        "civilians": [
            "Citizen 1",
            "Citizen 2",
            "Citizen 3"
        ],

        "police": [
            "Police Officer 1",
            "Police Officer 2"
        ],

        "shopkeepers": [
            "Shopkeeper 1",
            "Shopkeeper 2"
        ],

        "doctors": [
            "Doctor 1"
        ],

        "gang_members": [
            "Gang Member 1",
            "Gang Member 2"
        ]
    }

    npc_file = os.path.join(
        "projects",
        project_name,
        "npc.json"
    )

    with open(npc_file, "w", encoding="utf-8") as file:
        json.dump(
            npcs,
            file,
            indent=4,
            ensure_ascii=False
        )

    return npcs