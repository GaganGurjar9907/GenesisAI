import json
import os


def generate_vehicles(project_name):

    vehicles = {

        "cars": [
            "Sedan",
            "SUV",
            "Sports Car"
        ],

        "bikes": [
            "Street Bike",
            "Off Road Bike"
        ],

        "trucks": [
            "Cargo Truck"
        ],

        "buses": [
            "City Bus"
        ],

        "emergency": [
            "Police Car",
            "Ambulance",
            "Fire Truck"
        ]
    }

    vehicle_file = os.path.join(
        "projects",
        project_name,
        "vehicles.json"
    )

    with open(vehicle_file, "w", encoding="utf-8") as file:
        json.dump(
            vehicles,
            file,
            indent=4,
            ensure_ascii=False
        )

    return vehicles