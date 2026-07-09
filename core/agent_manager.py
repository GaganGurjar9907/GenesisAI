class AgentManager:

    def __init__(self):

        self.agents = [
            "Story Agent",
            "World Agent",
            "NPC Agent",
            "Vehicle Agent",
            "Mission Agent",
            "Code Agent",
            "UI Agent",
            "Audio Agent",
            "Testing Agent",
            "Export Agent"
        ]

    def show_agents(self):

        print("\n========== AI AGENTS ==========\n")

        for agent in self.agents:
            print(agent)

        print("\n===============================\n")