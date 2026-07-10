from builders.terrain_builder import TerrainBuilder
from builders.map_builder import MapBuilder
from builders.city_builder import CityBuilder
from builders.road_builder import RoadBuilder
from builders.building_builder import BuildingBuilder
from builders.npc_builder import NPCBuilder
from builders.vehicle_builder import VehicleBuilder
from builders.mission_builder import MissionBuilder


class Builder:

    def __init__(self):

        self.terrain = TerrainBuilder()
        self.map = MapBuilder()
        self.city = CityBuilder()
        self.road = RoadBuilder()
        self.building = BuildingBuilder()
        self.npc = NPCBuilder()
        self.vehicle = VehicleBuilder()
        self.mission = MissionBuilder()

    def build_all(self, project_name):

        print("\n========== BUILD SYSTEM ==========\n")

        self.terrain.build(project_name)
        self.map.build(project_name)
        self.city.build(project_name)
        self.road.build(project_name)
        self.building.build(project_name)
        self.npc.build(project_name)
        self.vehicle.build(project_name)
        self.mission.build(project_name)

        print("\n========== BUILD COMPLETE ==========\n")