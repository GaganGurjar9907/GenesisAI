class SceneManager:

    def __init__(self):

        self.scenes = {}
        self.active_scene = None

    def add_scene(self, scene):

        self.scenes[scene.name] = scene

        print(f"Scene Added -> {scene.name}")

    def load_scene(self, name):

        if name in self.scenes:

            self.active_scene = self.scenes[name]

            print(f"Loaded Scene -> {name}")

        else:

            print(f"Scene '{name}' Not Found")

    def get_active_scene(self):

        return self.active_scene

    def show_scenes(self):

        print("\n===== Registered Scenes =====\n")

        for scene_name in self.scenes:

            print(scene_name)