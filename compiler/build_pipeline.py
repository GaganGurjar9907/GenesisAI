class BuildPipeline:

    def __init__(self):

        self.pipeline = [

            "Project Validation",

            "Project Loading",

            "Asset Loading",

            "World Building",

            "City Building",

            "Road Building",

            "Building Placement",

            "NPC Placement",

            "Vehicle Placement",

            "Mission Placement",

            "Packaging"

        ]

    def run(self):

        print("\n========== BUILD PIPELINE ==========\n")

        for step in self.pipeline:

            print(f"Running -> {step}")

        print("\n✅ Build Pipeline Finished")