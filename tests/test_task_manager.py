import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from brain.task_manager import TaskManager

manager = TaskManager()

tasks = [

    "Generate Config",
    "Generate Assets",
    "Generate Story",
    "Generate World",
    "Generate NPCs",
    "Generate Vehicles",
    "Generate Missions",
    "Save Project"

]

for task in tasks:

    if manager.can_execute(task):

        print(f"Executing -> {task}")

        manager.complete_task(task)

    else:

        print(f"Waiting -> {task}")

manager.show_completed()