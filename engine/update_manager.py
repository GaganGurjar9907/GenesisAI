class UpdateManager:

    def __init__(self):

        self.objects = []

    def register(self, game_object):

        self.objects.append(game_object)

        print(f"Registered -> {game_object.name}")

    def update(self):

        print("\n========== UPDATE ==========\n")

        for obj in self.objects:

            print(f"Updating -> {obj.name}")

            for component in obj.components:

                if hasattr(component, "update"):

                    component.update()

        print("\n✅ Update Complete")