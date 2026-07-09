from core.builder import Builder
from core.agent_manager import AgentManager
from core.game_blueprint import GameBlueprint


class Brain:

    def __init__(self):

        self.builder = Builder()
        self.agent_manager = AgentManager()
        self.blueprint = GameBlueprint()

    def analyze(self, prompt):

        p = prompt.lower()

        self.blueprint.data["title"] = "Genesis Game"

        if "gta" in p:
            self.blueprint.data["genre"] = "Open World Action"
            self.blueprint.data["camera"] = "Third Person"
            self.blueprint.data["world_size"] = "Huge"

        if "india" in p:
            self.blueprint.data["theme"] = "India"

        self.blueprint.data["graphics"] = "Ultra"

        self.blueprint.data["platforms"] = [
            "Windows",
            "Android"
        ]

    def execute(self, project_name, prompt):

        print("\n========== GENESIS BRAIN ==========\n")

        self.analyze(prompt)

        self.blueprint.show()

        self.blueprint.save(project_name)

        self.agent_manager.show_agents()

        self.builder.build()

        print("\n✅ Build Started Successfully\n")