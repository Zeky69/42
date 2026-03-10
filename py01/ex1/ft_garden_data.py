"""
Docstring for ex1.ft_garden_data
"""


class Plant:
    """
    Docstring for Plant
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        :param height: Description
        :param age: Description
        """
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        """
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def get_info(self) -> dict:
        """
        Docstring for get_info

        :param self: Description
        """
        return {
            "name": self.name,
            "height": self.height,
            "age": self.age
        }


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(rose)
    print(sunflower)
    print(cactus)
