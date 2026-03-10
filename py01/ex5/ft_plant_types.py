"""
Docstring for ex5.ft_plant_types
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


class Flower(Plant):
    """
    Docstring for Flower
    """
    def __init__(self, name: str, height: int, days: int, color: str) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        :param height: Description
        :param days: Description
        :param color: Description
        """
        super().__init__(name, height, days)
        self.color = color

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        """
        return f'''{self.name} (Flower): {self.height}cm,
    {self.days} days, {self.color} color'''

    def bloom(self) -> None:
        """
        Docstring for bloom

        :param self: Description
        """
        print(f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    """
    Docstring for Tree
    """
    def __init__(self, name: str, height: int, days: int,
                 trunk_diameter: int) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        :param height: Description
        :param days: Description
        :param trunk_diameter: Description
        """
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def __str__(self):
        """
        Docstring for __str__

        :param self: Description
        """
        return f'''{self.name} (Tree): {self.height}cm, {self.days} days,
    {self.trunk_diameter}cm diameter'''

    def produce_shade(self) -> None:
        """
        Docstring for produce_shade

        :param self: Description
        """
        trunk_area = (self.trunk_diameter / 10) ** 2 * 3.14159
        print(f'''{self.name.capitalize()} provides
              {(trunk_area // 1):.0f} square meters of shade''')


class Vegetable(Plant):
    """
    Docstring for Vegetable
    """
    def __init__(self, name: str, height: int, days: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        :param height: Description
        :param days: Description
        :param harvest_season: Description
        :param nutritional_value: Description
        """
        super().__init__(name, height, days)
        self.nutritional_value = nutritional_value
        self.harvest_season = harvest_season

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        """
        return f'''{self.name} (Vegetable): {self.height}cm, {self.days} days,
    {self.harvest_season} harvest'''


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    daisy = Flower("Daisy", 15, 20, "white")

    print(rose)
    rose.bloom()

    print()

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 450, 1500, 40)
    print(oak)
    oak.produce_shade()
    print()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 10, 60, "autumn", "vitamin A")

    print(tomato)
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")
