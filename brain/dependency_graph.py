class DependencyGraph:

    def __init__(self):

        self.dependencies = {

            "Generate Config": [],

            "Generate Assets": [
                "Generate Config"
            ],

            "Generate Story": [
                "Generate Config"
            ],

            "Generate World": [
                "Generate Story"
            ],

            "Generate NPCs": [
                "Generate World"
            ],

            "Generate Vehicles": [
                "Generate World"
            ],

            "Generate Missions": [
                "Generate World",
                "Generate NPCs"
            ],

            "Save Project": [
                "Generate Missions"
            ]

        }

    def get_dependencies(self, task):

        return self.dependencies.get(task, [])

    def show(self):

        print("\n========== DEPENDENCY GRAPH ==========\n")

        for task, deps in self.dependencies.items():

            if deps:
                print(f"{task}")
                print(f"   depends on -> {', '.join(deps)}\n")

            else:
                print(f"{task}")
                print("   depends on -> None\n")