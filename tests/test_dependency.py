import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.dependency_graph import DependencyGraph

graph = DependencyGraph()

task = "Generate Missions"

print("Task :", task)

print("\nDependencies:")

for dep in graph.get_dependencies(task):
    print("-", dep)