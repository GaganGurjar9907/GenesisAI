class RenderPipeline:

    def __init__(self):

        self.render_queue = []

    def submit(self, game_object):

        self.render_queue.append(game_object)

    def render(self):

        print("\n========== RENDER PIPELINE ==========\n")

        if not self.render_queue:

            print("Nothing To Render")

            return

        for obj in self.render_queue:

            print(f"Rendering -> {obj.name}")

        self.render_queue.clear()

        print("\n✅ Frame Rendered")