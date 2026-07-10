class DependencyGraph:

    def __init__(self):

        self.dependencies = {

            "Generate Story": [],

            "Generate World": [
                "Generate Story"
            ],

            "Generate NPCs": [
                "Generate Story",
                "Generate World"
            ],

            "Generate Vehicles": [
                "Generate World"
            ],

            "Generate Missions": [
                "Generate Story",
                "Generate World",
                "Generate NPCs"
            ],

            "Build Scene": [
                "Generate World",
                "Generate NPCs",
                "Generate Vehicles"
            ],

            "Compile Game": [
                "Build Scene"
            ]
        }

    def get_dependencies(self, task):

        return self.dependencies.get(task, [])