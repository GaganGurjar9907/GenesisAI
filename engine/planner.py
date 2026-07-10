class Planner:

    def __init__(self):
        self.tasks = []

    def create_plan(self, blueprint):

        self.tasks = []

        genre = blueprint.data.get("genre", "")

        # Common tasks
        self.tasks.append("Create Project")
        self.tasks.append("Initialize Engine")
        self.tasks.append("Generate Story")
        self.tasks.append("Generate World")
        self.tasks.append("Generate NPCs")
        self.tasks.append("Generate Vehicles")
        self.tasks.append("Generate Missions")
        self.tasks.append("Build Scene")
        self.tasks.append("Compile Game")

        if "Open World" in genre:
            self.tasks.append("Generate Traffic")
            self.tasks.append("Generate Weather")
            self.tasks.append("Generate Economy")

        return self.tasks

    def show(self):

        print("\n========== BUILD PLAN ==========\n")

        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

        print("\n===============================\n")