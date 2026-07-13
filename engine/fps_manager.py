import time


class FPSManager:

    def __init__(self):

        self.frame_count = 0
        self.start_time = time.time()
        self.fps = 0

    def update(self):

        self.frame_count += 1

        current_time = time.time()

        elapsed = current_time - self.start_time

        if elapsed >= 1:

            self.fps = self.frame_count / elapsed

            print(f"FPS : {self.fps:.2f}")

            self.frame_count = 0

            self.start_time = current_time

    def get_fps(self):

        return self.fps