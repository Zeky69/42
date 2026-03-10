"""
Docstring for ex2.ft_custom_errors
"""


class GardenError(Exception):
    """Base class for garden-related exceptions."""
    pass


class PlantError(GardenError):
    """Exception raised for errors related to plants."""
    pass


class WaterError(GardenError):
    """Exception raised for errors related to watering."""
    pass


def test_custom_errors() -> None:
    """
    Test function to demonstrate custom error handling.
    """
    print("=== Custom Garden Errors Demo ===")
    try:
        print("\nTesting PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as pe:
        print(f"Caught a PlantError: {pe}")

    try:
        print("\nTesting WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as we:
        print(f"Caught a WaterError: {we}")

    try:
        print("\nTesting catching all garden errors...")
        raise PlantError("The tomato plant is wilting!")
    except GardenError as ge:
        print(f"Caught a garden error: {ge}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as ge:
        print(f"Caught a garden error: {ge}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
