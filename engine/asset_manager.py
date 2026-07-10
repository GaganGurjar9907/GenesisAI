import os
import json


def create_asset_structure(project_name):

    project_folder = os.path.join(
        "projects",
        project_name
    )

    asset_folder = os.path.join(
        project_folder,
        "Assets"
    )

    folders = [

        "Models",
        "Textures",
        "Sounds",
        "Animations",
        "Scripts",
        "UI"

    ]

    os.makedirs(asset_folder, exist_ok=True)

    for folder in folders:

        os.makedirs(
            os.path.join(asset_folder, folder),
            exist_ok=True
        )

    assets = {

        "models": [],
        "textures": [],
        "sounds": [],
        "animations": [],
        "scripts": [],
        "ui": []

    }

    asset_file = os.path.join(
        project_folder,
        "assets.json"
    )

    with open(asset_file, "w", encoding="utf-8") as file:

        json.dump(
            assets,
            file,
            indent=4,
            ensure_ascii=False
        )

    return assets