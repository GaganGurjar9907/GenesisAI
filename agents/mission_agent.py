from engine.mission_generator import generate_missions


class MissionAgent:

    def execute(self, project_name):

        print("[Mission Agent] Generating Missions...")

        generate_missions(project_name)

        print("✅ Mission Generation Complete")