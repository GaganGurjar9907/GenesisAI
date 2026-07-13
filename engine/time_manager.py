import time


class TimeManager:

    def __init__(self):

        self.last_time = time.time()
        self.delta_time = 0.0

    def update(self):

        current_time = time.time()

        self.delta_time = current_time - self.last_time

        self.last_time = current_time

    def get_delta_time(self):

        return self.delta_time