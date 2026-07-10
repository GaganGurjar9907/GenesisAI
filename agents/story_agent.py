from engine.story_generator import generate_story
from engine.memory_engine import load_project_data


class StoryAgent:

    def execute(self, project_name):

        print("[Story Agent] Generating Story...")

        data = load_project_data(project_name)

        game_idea = data.get("idea", "")

        story = generate_story(project_name, game_idea)

        print("✅ Story Generated Successfully")

        return story