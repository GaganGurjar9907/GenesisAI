import json
import os


def generate_config(project_name):

    config = {

        "project_name": project_name,

        "engine": "Genesis AI",

        "version": "0.7",

        "genre": "Open World Action",

        "language": "Python",

        "target_engine": "Genesis Engine",

        "build": "Development",

        "author": "Genesis AI",

        "status": "In Development"
    }

    config_file = os.path.join(
        "projects",
        project_name,
        "config.json"
    )

    with open(config_file, "w", encoding="utf-8") as file:

        json.dump(
            config,
            file,
            indent=4,
            ensure_ascii=False
        )

    return config