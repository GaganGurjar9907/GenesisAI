from collections import deque


class TaskQueue:

    def __init__(self):
        self.queue = deque()

    def add_tasks(self, tasks):
        for task in tasks:
            self.queue.append(task)

    def get_next_task(self):
        if len(self.queue) == 0:
            return None

        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def show(self):

        print("\n========== TASK QUEUE ==========\n")

        for i, task in enumerate(self.queue, start=1):
            print(f"{i}. {task}")

        print("\n===============================\n")