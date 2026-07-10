from engine.asset_manager import create_asset_structure


class AssetAgent:

    def execute(self, project_name):

        print("[Asset Agent] Creating Asset Structure...")

        create_asset_structure(project_name)

        print("✅ Asset Structure Created Successfully")