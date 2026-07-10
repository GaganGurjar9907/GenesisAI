from engine.config_generator import generate_config


class ConfigAgent:

    def execute(self, project_name):

        print("[Config Agent] Generating Config...")

        generate_config(project_name)

        print("✅ Config Generated Successfully")