import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from brain.dependency_graph import DependencyGraph

graph = DependencyGraph()

graph.show()