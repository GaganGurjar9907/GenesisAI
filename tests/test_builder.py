import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from builders.terrain_builder import TerrainBuilder
from builders.map_builder import MapBuilder
from builders.city_builder import CityBuilder
from builders.road_builder import RoadBuilder
from builders.building_builder import BuildingBuilder
from builders.npc_builder import NPCBuilder
from builders.vehicle_builder import VehicleBuilder
from builders.mission_builder import MissionBuilder

project = "GTA India"

TerrainBuilder().build(project)
MapBuilder().build(project)
CityBuilder().build(project)
RoadBuilder().build(project)
BuildingBuilder().build(project)
NPCBuilder().build(project)
VehicleBuilder().build(project)
MissionBuilder().build(project)