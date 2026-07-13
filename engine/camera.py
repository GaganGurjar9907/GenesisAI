class Camera:

    def __init__(self):

        self.fov = 70
        self.near = 0.1
        self.far = 1000

    def set_fov(self, value):

        self.fov = value

    def set_clip(self, near, far):

        self.near = near
        self.far = far

    def show(self):

        print("\n===== Camera =====")

        print("FOV :", self.fov)
        print("Near:", self.near)
        print("Far :", self.far)