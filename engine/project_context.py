import os


class ProjectContext:

    def __init__(self, project_name):

        self.project_name = project_name

        self.project_path = os.path.join(
            "projects",
            project_name
        )

    def path(self):

        return self.project_path

    def file(self, filename):

        return os.path.join(
            self.project_path,
            filename
        )

    def exists(self):

        return os.path.exists(
            self.project_path
        )