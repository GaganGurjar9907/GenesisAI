class BuildPipeline:

    def __init__(self):

        self.stages = [
            "Planning",
            "Story",
            "World",
            "Characters",
            "Vehicles",
            "Missions",
            "Scene",
            "Physics",
            "Rendering",
            "Testing",
            "Export"
        ]

    def run(self):

        print("\n========== BUILD PIPELINE ==========\n")

        for stage in self.stages:
            print(f"Running: {stage}")

        print("\n========== PIPELINE COMPLETE ==========\n")