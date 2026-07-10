from brain.task_manager import TaskManager


class DecisionEngine:

    def __init__(self):

        self.manager = TaskManager()

    def should_execute(self, task):

        return self.manager.can_execute(task)

    def task_completed(self, task):

        self.manager.complete_task(task)

    def show_status(self):

        self.manager.show_completed()