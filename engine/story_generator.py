from engine.generator import generate
from engine.memory_engine import (
    load_project_data,
    save_project_data
)


def generate_story(project_name, game_idea):

    prompt = f"""
Write a complete game story for this game.

Game Idea:
{game_idea}

The story should include:

- Background
- Main Character
- Goal
- Villain
- Ending
"""

    story = generate(prompt)

    data = load_project_data(project_name)

    data["story"] = story

    save_project_data(project_name, data)

    return story