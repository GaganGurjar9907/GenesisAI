from engine.map_generator import generate_map
from engine.memory_engine import load_project_data


class WorldAgent:

    def execute(self, project_name):

        print("[World Agent] Generating World...")

        data = load_project_data(project_name)

        game_idea = data.get("idea", "")

        world = generate_map(project_name, game_idea)

        print("✅ World Generated Successfully")

        return world