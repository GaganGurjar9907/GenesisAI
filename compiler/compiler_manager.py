class CompilerManager:

    def __init__(self):

        self.steps = [

            "Validate Project",
            "Load Project",
            "Build World",
            "Build NPCs",
            "Build Vehicles",
            "Build Missions",
            "Package Game"

        ]

    def compile(self, project_name):

        print("\n========== GENESIS COMPILER ==========\n")

        for step in self.steps:

            print(f"Running -> {step}")

        print("\n✅ Compile Pipeline Finished")