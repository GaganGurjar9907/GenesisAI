from brain.dependency_graph import DependencyGraph


class TaskManager:

    def __init__(self):

        self.graph = DependencyGraph()
        self.completed = []

    def can_execute(self, task):

        dependencies = self.graph.get_dependencies(task)

        for dependency in dependencies:

            if dependency not in self.completed:
                return False

        return True

    def complete_task(self, task):

        if task not in self.completed:
            self.completed.append(task)

    def show_completed(self):

        print("\n========== COMPLETED TASKS ==========\n")

        if not self.completed:
            print("No task completed.")

        for task in self.completed:
            print("✅", task)