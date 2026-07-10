from engine.vehicle_generator import generate_vehicles


class VehicleAgent:

    def execute(self, project_name):

        print("[Vehicle Agent] Generating Vehicles...")

        generate_vehicles(project_name)

        print("✅ Vehicle Generation Complete")