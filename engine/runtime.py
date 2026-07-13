import time

from engine.time_manager import TimeManager
from engine.fps_manager import FPSManager
from engine.event_manager import EventManager


class Runtime:

    def __init__(
        self,
        renderer,
        update_manager,
        input_manager,
        window
    ):

        self.renderer = renderer
        self.update_manager = update_manager
        self.input_manager = input_manager
        self.window = window

        self.time = TimeManager()
        self.fps = FPSManager()
        self.events = EventManager()

        self.running = False

    def start(self, scene, fps=60, frames=300):

        self.running = True

        delay = 1 / fps

        print("\n========== GENESIS ENGINE ==========\n")

        while self.running and frames > 0:

            self.time.update()

            self.events.process_events()

            self.input_manager.update()

            self.update_manager.update()

            self.renderer.render(scene)

            self.window.update()

            self.fps.update()

            frames -= 1

            time.sleep(delay)

        self.window.close()

        print("\n✅ Engine Shutdown")

    def stop(self):

        self.running = False

    def post_event(self, event):

        self.events.add_event(event)