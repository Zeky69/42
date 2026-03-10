class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when there is a specific problem with a plant."""
    pass


class WaterError(GardenError):
    """Raised when there is a problem with the water supply."""
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, name: str) -> None:
        """
        Adds a plant to the list.
        Raises ValueError if the name is empty.
        """
        if not name:
            raise ValueError("Plant name cannot be empty!")
        self.plants.append(name)
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """
        Simulates watering all plants.
        Uses try/finally to ensure the system closes.
        """
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant is None:
                    print("Skipping invalid plant entry")
                    continue
                print(f"Watering {plant} - success")
        except Exception as e:
            print(f"Unexpected error during watering: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str, water_level: int,
                           sunlight_hours: int) -> None:
        """
        Checks health parameters.
        Raises PlantError if parameters are invalid.
        """
        if water_level > 10:
            raise PlantError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise PlantError(f"Sunlight hours {sunlight_hours} is too low \
(min 2)")

        print(f"{plant_name}: healthy (water: {water_level}, sun: \
{sunlight_hours})")

    def simulate_tank_issue(self) -> None:
        """
        Simulates a critical infrastructure failure.
        Raises a generic GardenError.
        """
        raise GardenError("Not enough water in tank")


def test_garden_management() -> None:
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
    except ValueError as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("")
    except ValueError as e:
        print(f"Error adding plant: {e}")

    print("Watering plants...")
    manager.water_plants()

    print("Checking plant health...")

    try:
        manager.check_plant_health("tomato", 5, 8)
    except PlantError as e:
        print(f"Error checking tomato: {e}")

    try:
        manager.check_plant_health("lettuce", 15, 8)
    except PlantError as e:
        print(f"Error checking lettuce: {e}")

    print("Testing error recovery...")
    try:
        manager.simulate_tank_issue()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
