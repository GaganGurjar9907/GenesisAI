import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from brain.decision_engine import DecisionEngine

engine = DecisionEngine()

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

    if engine.should_execute(task):

        print(f"AI Approved -> {task}")

        engine.task_completed(task)

    else:

        print(f"AI Rejected -> {task}")

engine.show_status()