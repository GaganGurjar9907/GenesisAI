from core.master_controller import MasterController


class Executor:

    def __init__(self):

        self.master = MasterController()

    def execute(self, project_name, prompt):

        self.master.build_game(
            project_name,
            prompt
        )