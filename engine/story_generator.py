import json
import os
from engine.memory_engine import save_project_data


def generate_story(project_name, game_idea):

    story = {
        "title": project_name,
        "genre": "Open World Action",
        "game_idea": game_idea,

        "story": (
            f"{project_name} is an open world action game based on "
            f"{game_idea}. The player explores a huge world, completes "
            f"missions, earns money, buys vehicles and properties, "
            f"and builds their own criminal empire."
        )
    }

    # Save memory
    save_project_data(project_name, story)

    # Save story.json
    story_file = os.path.join(
        "projects",
        project_name,
        "story.json"
    )

    with open(story_file, "w", encoding="utf-8") as file:
        json.dump(
            story,
            file,
            indent=4,
            ensure_ascii=False
        )

    return story