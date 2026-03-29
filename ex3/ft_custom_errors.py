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


def trigger_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def trigger_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


# --------------------------------------------------------------


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        trigger_plant_error()
    except PlantError as e:
        print("Caught PlantError:", e)
    print("\nTesting WaterError...")
    try:
        trigger_water_error()
    except WaterError as e:
        print("Caught WaterError:", e)
    print("\nTesting catching all garden errors...")
    try:
        trigger_plant_error()
    except GardenError as e:
        print("Caught GardenError:", e)
    try:
        trigger_water_error()
    except GardenError as e:
        print("Caught GardenError:", e)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
