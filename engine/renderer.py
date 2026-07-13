from engine.render_pipeline import RenderPipeline


class Renderer:

    def __init__(self):

        self.pipeline = RenderPipeline()

    def render(self, scene):

        print("\n========== GENESIS RENDERER ==========\n")

        print(f"Scene : {scene.name}\n")

        if not scene.objects:

            print("Scene Empty")

            return

        for obj in scene.objects:

            self.pipeline.submit(obj)

        self.pipeline.render()