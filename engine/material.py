class Material:

    def __init__(self, name="Default"):

        self.name = name
        self.shader = "Standard"
        self.texture = None

    def set_shader(self, shader):

        self.shader = shader

    def set_texture(self, texture):

        self.texture = texture

    def show(self):

        print("\n===== Material =====")

        print("Name    :", self.name)
        print("Shader  :", self.shader)
        print("Texture :", self.texture)