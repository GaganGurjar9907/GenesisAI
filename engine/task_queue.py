class TaskQueue:

    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append(
            {
                "name": name,
                "status": "Pending"
            }
        )

    def complete_task(self, name):

        for task in self.tasks:

            if task["name"] == name:
                task["status"] = "Completed"

    def show_tasks(self):

        print("\n========== TASK QUEUE ==========")

        for i, task in enumerate(self.tasks, 1):

            print(
                f"{i}. {task['name']}  [{task['status']}]"
            )

        print("===============================\n")