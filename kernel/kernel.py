class GenesisKernel:

    def __init__(self):

        self.version = "0.9"

        self.modules = [
            "Brain",
            "Planner",
            "Builder",
            "Scene Engine",
            "Render Engine",
            "Physics Engine",
            "Animation Engine",
            "Audio Engine",
            "Compiler",
            "Exporter"
        ]

    def boot(self):

        print("\n=================================")
        print("      GENESIS KERNEL BOOT")
        print("=================================\n")

        for module in self.modules:
            print(f"[ OK ] {module}")

        print("\nGenesis Kernel Ready.\n")