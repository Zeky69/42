"""
Docstring for ex2.ft_plant_growth
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

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        """
        return f"{self.name}: {self.height}cm, {self.days} days old"

    def grow(self) -> None:
        """
        Docstring for grow

        :param self: Description
        """
        self.height += 1

    def age(self) -> None:
        """
        Docstring for age

        :param self: Description
        """
        self.days += 1

    def get_info(self) -> str:
        """
        Docstring for get_info

        :param self: Description
        """
        return str(self)

    def get_older(self) -> int:
        """
        Docstring for get_older

        :param self: Description
        """
        return self.days


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    track = plant.height
    print("=== Day 1 ===")
    print(plant.get_info())
    print("=== Day 7 ===")
    for day in range(6):
        plant.grow()
        plant.age()
    print(plant.get_info())
    print(f"Growth this week: +{plant.height - track}cm")
