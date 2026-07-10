class GameObject:

    def __init__(self, name):

        self.name = name
        self.components = []

    def add_component(self, component):

        self.components.append(component)

        print(f"{component} added to {self.name}")

    def show(self):

        print(f"\n===== {self.name} =====")

        if not self.components:

            print("No Components")

        for component in self.components:

            print(component)