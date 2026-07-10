class GameBlueprint:

    def __init__(self):

        self.data = {
            "title": "",
            "genre": "",
            "theme": "",
            "platform": [],
            "graphics": "",
            "camera": "",
            "players": 1,
            "map_size": "",
            "story": "",
            "weather": "",
            "time_cycle": "",
            "physics": "",
            "ai_level": "",
            "language": "English"
        }

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def load(self, data):
        self.data.update(data)

    def show(self):

        print("\n========== GAME BLUEPRINT ==========\n")

        for key, value in self.data.items():
            print(f"{key} : {value}")

        print("\n====================================\n")