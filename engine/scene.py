class Scene:

    def __init__(self, name):

        self.name = name
        self.objects = []

    def add_object(self, obj):

        self.objects.append(obj)

        print(f"Added -> {obj}")

    def show(self):

        print(f"\n===== Scene : {self.name} =====\n")

        if not self.objects:

            print("Scene Empty")

        for obj in self.objects:

            print(obj)