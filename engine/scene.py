class Scene:

    def __init__(self, name):

        self.name = name
        self.objects = []

    def add_object(self, game_object):

        self.objects.append(game_object)

        print(f"Added GameObject -> {game_object.name}")

    def find(self, name):

        for obj in self.objects:

            if obj.name == name:

                return obj

        return None

    def show(self):

        print(f"\n===== Scene : {self.name} =====")

        if not self.objects:

            print("Scene Empty")

            return

        print()

        for obj in self.objects:

            print(obj.name)