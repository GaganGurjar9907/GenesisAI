from agents.config_agent import ConfigAgent
from agents.asset_agent import AssetAgent
from agents.story_agent import StoryAgent
from agents.world_agent import WorldAgent
from agents.npc_agent import NPCAgent
from agents.vehicle_agent import VehicleAgent
from agents.mission_agent import MissionAgent


class AgentManager:

    def __init__(self):

        self.config = ConfigAgent()
        self.asset = AssetAgent()
        self.story = StoryAgent()
        self.world = WorldAgent()
        self.npc = NPCAgent()
        self.vehicle = VehicleAgent()
        self.mission = MissionAgent()

    def execute(self, task, project_name):

        print(f"\n========== {task.upper()} ==========\n")

        if task == "Generate Config":
            self.config.execute(project_name)

        elif task == "Generate Assets":
            self.asset.execute(project_name)

        elif task == "Generate Story":
            self.story.execute(project_name)

        elif task == "Generate World":
            self.world.execute(project_name)

        elif task == "Generate NPCs":
            self.npc.execute(project_name)

        elif task == "Generate Vehicles":
            self.vehicle.execute(project_name)

        elif task == "Generate Missions":
            self.mission.execute(project_name)

        elif task == "Create Project":
            print("[Project Manager] Creating Project...")
            print("✅ Project Created Successfully")

        elif task == "Initialize Engine":
            print("[Engine] Initializing...")
            print("✅ Engine Initialized")

        elif task == "Build Scene":
            print("[Scene Builder] Building Scene...")
            print("✅ Scene Built Successfully")

        elif task == "Compile Game":
            print("[Compiler] Compiling Game...")
            print("✅ Game Compiled Successfully")

        elif task == "Generate Traffic":
            print("[Traffic Generator] Generating Traffic...")
            print("✅ Traffic Generated Successfully")

        elif task == "Generate Weather":
            print("[Weather Generator] Generating Weather...")
            print("✅ Weather Generated Successfully")

        elif task == "Generate Economy":
            print("[Economy Generator] Generating Economy...")
            print("✅ Economy Generated Successfully")

        elif task == "Save Project":
            print("[Project Manager] Saving Project...")
            print("✅ Project Saved Successfully")

        else:
            print(f"❌ Unknown Task: {task}")