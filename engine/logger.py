from datetime import datetime
import os


class Logger:

    def __init__(self, project_name):

        self.project_name = project_name

        self.log_file = os.path.join(
            "projects",
            project_name,
            "genesis.log"
        )

    def log(self, message):

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.log_file, "a", encoding="utf-8") as file:

            file.write(f"[{time}] {message}\n")

        print(f"[LOG] {message}")