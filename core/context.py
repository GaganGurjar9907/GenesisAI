class Context:

    def __init__(self):

        self.project = ""
        self.genre = ""
        self.platform = ""
        self.engine = ""

    def show(self):

        print("\n========== CONTEXT ==========")

        print(f"Project : {self.project}")
        print(f"Genre   : {self.genre}")
        print(f"Platform: {self.platform}")
        print(f"Engine  : {self.engine}")

        print("=============================\n")