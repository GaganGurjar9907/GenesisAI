from engine.scene_manager import SceneManager
from engine.renderer import Renderer
from engine.update_manager import UpdateManager
from engine.input_manager import InputManager
from engine.runtime import Runtime
from engine.engine_config import EngineConfig
from engine.console import Console
from engine.window import EngineWindow


class Engine:

    def __init__(self):

        self.config = EngineConfig()

        Console.success(
            f"{self.config.engine_name} v{self.config.version}"
        )

        self.scene_manager = SceneManager()

        self.renderer = Renderer()

        self.update_manager = UpdateManager()

        self.input_manager = InputManager()

        self.window = EngineWindow(
            self.config,
            self.input_manager
        )

        self.runtime = Runtime(
            self.renderer,
            self.update_manager,
            self.input_manager,
            self.window
        )

        Console.success("Engine Initialized")

    def add_scene(self, scene):

        self.scene_manager.add_scene(scene)

    def load_scene(self, scene_name):

        self.scene_manager.load_scene(scene_name)

    def register_object(self, game_object):

        self.update_manager.register(game_object)

    def post_event(self, event):

        self.runtime.post_event(event)

    def run(self):

        scene = self.scene_manager.get_active_scene()

        if scene is None:

            Console.error("No Active Scene")

            return

        Console.info(
            f"Starting Runtime ({self.config.target_fps} FPS)"
        )

        self.runtime.start(
            scene,
            fps=self.config.target_fps
        )

    def stop(self):

        self.runtime.stop()

        Console.info("Engine Stopped")