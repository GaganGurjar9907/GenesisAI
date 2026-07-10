from core.planner import Planner
from core.agent_manager import AgentManager

from brain.ai_brain import AIBrain


class Executor:

    def __init__(self):

        self.manager = AgentManager()
        self.planner = Planner()
        self.brain = AIBrain()

    def execute_project(self, project_name):

        tasks = self.planner.create_plan(project_name)

        print("\n========== GENESIS AI EXECUTOR ==========\n")

        for task in tasks:

            print(f"\nRequesting -> {task}")

            self.brain.execute_task(

                task,

                lambda t=task: self.manager.execute(
                    t,
                    project_name
                )

            )

        print("\n========== EXECUTION COMPLETE ==========\n")

        self.brain.show_status()