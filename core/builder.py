from core.pipeline import BuildPipeline


class Builder:

    def __init__(self):

        self.pipeline = BuildPipeline()

        self.modules = [
            "Story",
            "World",
            "Characters",
            "Vehicles",
            "Missions",
            "UI",
            "Audio",
            "Physics"
        ]

    def build(self):

        print("\n========== BUILD STARTED ==========\n")

        # Run Build Pipeline
        self.pipeline.run()

        # Build Modules
        for module in self.modules:
            print(f"Building {module}...")

        print("\n========== BUILD COMPLETE ==========\n")