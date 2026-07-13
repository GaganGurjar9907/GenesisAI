class InputManager:

    def __init__(self):

        self.keys = set()

    def key_press(self, event):

        self.keys.add(event.keysym.lower())

    def key_release(self, event):

        self.keys.discard(event.keysym.lower())

    def is_pressed(self, key):

        return key.lower() in self.keys

    def update(self):

        if self.is_pressed("w"):
            print("Move Forward")

        if self.is_pressed("s"):
            print("Move Backward")

        if self.is_pressed("a"):
            print("Move Left")

        if self.is_pressed("d"):
            print("Move Right")