class GSLParser:

    def __init__(self):
        self.data = {}

    def parse(self, text):

        self.data = {}

        lines = text.split("\n")

        for line in lines:

            line = line.strip()

            if line == "":
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)

            key = key.strip()
            value = value.strip()

            self.data[key] = value

        return self.data

    def show(self):

        print("\n========== GSL DATA ==========\n")

        for key, value in self.data.items():
            print(f"{key} : {value}")

        print("\n==============================")