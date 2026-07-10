from core.dependency_graph import DependencyGraph


class DecisionEngine:

    def __init__(self):
        self.graph = DependencyGraph()

    def resolve(self, task):

        ordered = []
        visited = set()

        def visit(current):

            if current in visited:
                return

            visited.add(current)

            for dep in self.graph.get_dependencies(current):
                visit(dep)

            ordered.append(current)

        visit(task)

        return ordered