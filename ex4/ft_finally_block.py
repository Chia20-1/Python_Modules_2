#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error."):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error."):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error."):
        super().__init__(message)


# --------------------------------------------------------------


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water:"
                         f" '{plant_name}'")


# --------------------------------------------------------------


def test_watering_system() -> None:
    valid_plants = ["Tomato", "Lettuce", "Carrot"]
    invalid_plants = ["Tomato", "lettuce", "Carrot"]
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for plant in valid_plants:
            water_plant(plant)
    except PlantError as e:
        print("Caught PlantError:", e)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for plant in invalid_plants:
            water_plant(plant)
    except PlantError as e:
        print("Caught PlantError:", e)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
