import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.planner import Planner
from engine.task_queue import TaskQueue
from core.agent_manager import AgentManager
from core.game_blueprint import GameBlueprint

bp = GameBlueprint()

bp.data["genre"] = "Open World Action"

planner = Planner()

tasks = planner.create_plan(bp)

queue = TaskQueue()

queue.add_tasks(tasks)

manager = AgentManager()

while not queue.is_empty():

    manager.execute(queue.get_next_task())