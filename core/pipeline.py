from engine.planner import Planner
from engine.task_queue import TaskQueue
from core.agent_manager import AgentManager


class Pipeline:

    def __init__(self):

        self.planner = Planner()
        self.queue = TaskQueue()
        self.manager = AgentManager()

    def execute(self, blueprint):

        print("\n========== GENESIS PIPELINE ==========\n")

        tasks = self.planner.create_plan(blueprint)

        self.queue.add_tasks(tasks)

        while not self.queue.is_empty():

            task = self.queue.get_next_task()

            self.manager.execute(task)

        print("\n========== PIPELINE COMPLETE ==========\n")