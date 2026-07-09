from engine.mission_generator import generate_missions
from engine.npc_generator import generate_npcs
from engine.vehicle_generator import generate_vehicles
from engine.map_generator import generate_map


def execute_command(project_name, command):

    cmd = command.lower()

    if "mission" in cmd:
        return generate_missions(project_name)

    elif "npc" in cmd or "character" in cmd:
        return generate_npcs(project_name)

    elif "vehicle" in cmd or "car" in cmd:
        return generate_vehicles(project_name)

    elif "map" in cmd or "world" in cmd or "city" in cmd:
        return generate_map(project_name)

    return None