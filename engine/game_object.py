class GameObject:

    def __init__(self, name):

        self.name = name
        self.components = []
        self.children = []
        self.parent = None

    def add_component(self, component):

        self.components.append(component)

    def add_child(self, child):

        child.parent = self
        self.children.append(child)

        print(f"{child.name} added to {self.name}")

    def show(self, level=0):

        print("  " * level + self.name)

        for child in self.children:

            child.show(level + 1)