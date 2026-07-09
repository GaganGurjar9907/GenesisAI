from core.brain import Brain


class MasterController:

    def __init__(self):

        self.brain = Brain()

    def build_game(self, project_name, prompt):

        print("\n====================================")
        print("      GENESIS MASTER CONTROLLER")
        print("====================================")

        print("\nReceiving User Request...")

        self.brain.execute(project_name, prompt)

        print("\n====================================")
        print(" GAME BUILD PROCESS STARTED")
        print("====================================")