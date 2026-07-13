class Transform:

    def __init__(self):

        self.position = [0, 0, 0]
        self.rotation = [0, 0, 0]
        self.scale = [1, 1, 1]

    def set_position(self, x, y, z):

        self.position = [x, y, z]

    def set_rotation(self, x, y, z):

        self.rotation = [x, y, z]

    def set_scale(self, x, y, z):

        self.scale = [x, y, z]

    def show(self):

        print("\n===== Transform =====")

        print("Position :", self.position)
        print("Rotation :", self.rotation)
        print("Scale    :", self.scale)