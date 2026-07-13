class Mesh:

    def __init__(self, mesh_name="Cube"):

        self.mesh_name = mesh_name

    def set_mesh(self, mesh_name):

        self.mesh_name = mesh_name

    def show(self):

        print("\n===== Mesh =====")

        print("Mesh :", self.mesh_name)