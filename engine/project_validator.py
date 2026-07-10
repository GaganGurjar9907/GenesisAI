import os


class ProjectValidator:

    REQUIRED_FILES = [

        "config.json",
        "story.json",
        "world.json",
        "npc.json",
        "vehicles.json",
        "missions.json",
        "assets.json",
        "memory.json"

    ]

    def validate(self, project_name):

        project_path = os.path.join(
            "projects",
            project_name
        )

        print("\n========== PROJECT VALIDATION ==========\n")

        success = True

        for file in self.REQUIRED_FILES:

            path = os.path.join(project_path, file)

            if os.path.exists(path):

                print(f"✅ {file}")

            else:

                print(f"❌ {file}")

                success = False

        print()

        if success:

            print("✅ Project Validation Passed")

        else:

            print("❌ Project Validation Failed")

        return success