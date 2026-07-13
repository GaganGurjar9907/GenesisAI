import tkinter as tk


class EngineWindow:

    def __init__(self, config, input_manager):

        self.window = tk.Tk()

        self.window.title(config.engine_name)

        self.window.geometry(
            f"{config.screen_width}x{config.screen_height}"
        )

        self.window.configure(bg="black")

        self.input_manager = input_manager

        self.window.bind(
            "<KeyPress>",
            self.input_manager.key_press
        )

        self.window.bind(
            "<KeyRelease>",
            self.input_manager.key_release
        )

    def update(self):

        self.window.update_idletasks()
        self.window.update()

    def close(self):

        self.window.destroy()