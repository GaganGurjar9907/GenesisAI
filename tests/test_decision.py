import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.decision import DecisionEngine

engine = DecisionEngine()

tasks = engine.resolve("Compile Game")

print("\nExecution Order:\n")

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")