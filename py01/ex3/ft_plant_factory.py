"""
Docstring for ex3.ft_plant_factory
"""


class Plant:
    """
    Docstring for Plant
    """
    def __init__(self, name: str, height: int, days: int) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        :param height: Description
        :param days: Description
        """
        self.name = name
        self.height = height
        self.days = days
        print(f"Created: {self.name} ({self.height}cm, {self.days} days)")

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        """
        return f"{self.name} ({self.height}cm, {self.days} days)"


if __name__ == "__main__":
    plants = [
        ("Rose", 25, 30), ("Oak", 200, 365),
        ("Cactus", 5, 90), ("Sunflower", 80, 45),
        ("Fern", 15, 120)
        ]
    print("=== Plant Factory Output ===")

    garden = []
    for name, height, days in plants:
        plant = Plant(name, height, days)
        garden.append(plant)
    print()
    print(f"Total plants created: {len(garden)}")
