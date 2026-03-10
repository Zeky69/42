"""
Docstring for ex4.ft_garden_security
"""


class SecurePlant:
    """
    Docstring for SecurePlant
    """
    def __init__(self, name: str, height: int = 0, days: int = 0) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        """
        self.name = name
        self._height = height
        self._days = days
        print(f"Plant created: {self.name}")

    def __str__(self):
        """
        Docstring for __str__

        :param self: Description
        """
        return f"{self.name} ({self._height}cm, {self._days} days)"

    def set_height(self, height: int) -> None:
        """
        Docstring for set_height

        :param self: Description
        :param height: Description
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, days: int) -> None:
        """
        Docstring for set_age

        :param self: Description
        :param days: Description
        """
        if days < 0:
            print(f"Invalid operation attempted: age {days} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._days = days
            print(f"Age updated: {days} days [OK]")

    def get_height(self) -> int:
        """
        Docstring for get_height

        :param self: Description
        """
        return self._height

    def get_age(self) -> int:
        """
        Docstring for get_age

        :param self: Description
        """
        return self._days


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"Current plant: {plant}")
