class Texture:

    def __init__(self, name="Default"):

        self.name = name
        self.path = ""

    def set_path(self, path):

        self.path = path

    def show(self):

        print("\n===== Texture =====")

        print("Texture :", self.name)
        print("Path    :", self.path)