from brain.decision_engine import DecisionEngine


class AIBrain:

    def __init__(self):

        self.decision = DecisionEngine()

    def execute_task(self, task, callback):

        if self.decision.should_execute(task):

            print(f"[AI Brain] Approved -> {task}")

            callback()

            self.decision.task_completed(task)

        else:

            print(f"[AI Brain] Waiting -> {task}")

    def show_status(self):

        self.decision.show_status()