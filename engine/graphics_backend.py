class GraphicsBackend:

    def __init__(self):

        self.backend = None

    def initialize(self):

        self.backend = "Software Renderer"

        print("\n========== GRAPHICS BACKEND ==========\n")

        print(f"Backend : {self.backend}")

        print("Graphics Backend Initialized Successfully")

    def get_backend(self):

        return self.backend