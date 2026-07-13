class EngineConfig:

    def __init__(self):

        self.engine_name = "Genesis Engine"

        self.version = "0.7 Alpha"

        self.screen_width = 1280

        self.screen_height = 720

        self.target_fps = 60

        self.fullscreen = False

    def show(self):

        print("\n========== ENGINE CONFIG ==========\n")

        print(f"Engine      : {self.engine_name}")
        print(f"Version     : {self.version}")
        print(f"Resolution  : {self.screen_width} x {self.screen_height}")
        print(f"FPS         : {self.target_fps}")
        print(f"Fullscreen  : {self.fullscreen}")