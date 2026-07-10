class Context:

    def __init__(self):

        self.data = {}

    def set(self, key, value):

        self.data[key] = value

    def get(self, key, default=None):

        return self.data.get(key, default)

    def update(self, values):

        self.data.update(values)

    def clear(self):

        self.data.clear()

    def show(self):

        print("\n========== CONTEXT ==========\n")

        for key, value in self.data.items():
            print(f"{key} : {value}")

        print("\n=============================\n")