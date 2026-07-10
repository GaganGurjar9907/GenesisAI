from engine.npc_generator import generate_npcs


class NPCAgent:

    def execute(self, project_name):

        print("[NPC Agent] Generating NPCs...")

        generate_npcs(project_name)

        print("✅ NPC Generation Complete")