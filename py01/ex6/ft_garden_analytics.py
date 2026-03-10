"""
Docstring for ex6.ft_garden_analytics
"""


class Garden:
    """
    Docstring for Garden
    """
    def __init__(self, name: str) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        """
        self.name = name
        self.plants = []

    def add_plant(self, plant) -> None:
        """
        Docstring for add_plant

        :param self: Description
        :param plant: Description
        """
        self.plants.append(plant)
        print(f"Plant {plant.name} added to garden {self.name}")

    def grow_plants(self) -> None:
        """
        Docstring for grow_plants

        :param self: Description
        """
        for plant in self.plants:
            plant.grow()

    def stats(self) -> dict:
        """
        Docstring for stats

        :param self: Description
        """
        stats = GardenManager.GardenStats([self])
        return stats.calculate_stats()


class GardenManager:
    """
    Docstring for GardenManager
    """
    class GardenStats:
        """
        Docstring for GardenStats
        """
        def __init__(self, gardens: list) -> None:
            """
            Docstring for __init__

            :param self: Description
            :param gardens: Description
            """
            self.gardens = gardens

        def total_plants(self) -> int:
            """
            Docstring for total_plants

            :param self: Description
            """
            total = 0
            for garden in self.gardens:
                for plant in garden.plants:
                    total += 1
            return total

        def total_height(self) -> int:
            """
            Docstring for total_height

            :param self: Description
            """
            total_height = 0
            for garden in self.gardens:
                for plant in garden.plants:
                    total_height += plant.height
            return total_height

        def len(self) -> int:
            """
            Docstring for len

            :param self: Description
            """
            return len(self.gardens)

        def get_type_of_plants(self) -> dict:
            """
            Docstring for get_type_of_plants

            :param self: Description
            """
            types = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
            for garden in self.gardens:
                for plant in garden.plants:
                    plant_type = plant.get_type()
                    if plant_type not in types:
                        types[plant_type] = 0
                    types[plant_type] += 1
            return types

        def get_score(self) -> int:
            """
            Docstring for get_score

            :param self: Description
            """
            score = 0
            for garden in self.gardens:
                for plant in garden.plants:
                    if plant.get_type() == "PrizeFlower":
                        score += plant.prize + 1
                    else:
                        score += 1
            return score

        def calculate_stats(self) -> dict:
            """
            Docstring for calculate_stats

            :param self: Description
            """
            return {
                "total_plants": self.total_plants(),
                "total_height": self.total_height(),
                "types_of_plants": self.get_type_of_plants(),
                "score": self.get_score()
            }

    def __init__(self, name: str) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        """
        self.name = name
        self.gardens = []
        self.stats = self.GardenStats(self.gardens)

    @staticmethod
    def validate_height(height: int) -> bool:
        """
        Docstring for validate_height

        :param height: Description
        """
        return height > 0

    @classmethod
    def create_garden_network(cls, name: str,
                              gardens: list) -> "GardenManager":
        """
        Docstring for create_garden_network

        :param cls: Description
        :param name: Description
        :param gardens: Description
        """
        manager = cls(name)
        for garden in gardens:
            manager.add_garden(garden)
        return manager

    def add_garden(self, garden) -> None:
        """
        Docstring for add_garden

        :param self: Description
        :param garden: Description
        """
        self.gardens.append(garden)

    def grow_gardens(self) -> None:
        """
        Docstring for grow_gardens

        :param self: Description
        """
        for garden in self.gardens:
            garden.grow_plants()


class Plant:
    """
    Docstring for Plant
    """
    def __init__(self, name: str, height: int) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        :param height: Description
        """
        self.name = name
        self.height = height
        self._type = "Plant"

    def grow(self) -> None:
        """
        Docstring for grow

        :param self: Description
        """
        if not GardenManager.validate_height(self.height):
            self.height = 1
        self.height += 1

    def get_type(self) -> str:
        """
        Docstring for get_type

        :param self: Description
        """
        return self._type

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        """
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    Docstring for FloweringPlant
    """
    def __init__(self, name: str, height: int, color: str) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        :param height: Description
        :param color: Description
        """
        super().__init__(name, height)
        self.color = color
        self._type = "FloweringPlant"

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        """
        return super().__str__() + f", {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """
    Docstring for PrizeFlower
    """
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        :param height: Description
        :param color: Description
        :param prize: Description
        """
        super().__init__(name, height, color)
        self.prize = prize
        self._type = "PrizeFlower"

    def add_prize(self) -> None:
        """
        Docstring for add_prize

        :param self: Description
        """
        self.prize += 1

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        """
        return super().__str__() + f", Prize points: {self.prize}"


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    alice = Garden("Alice")

    oak = Plant("Oak Tree", 100)
    alice.add_plant(oak)

    rose = FloweringPlant("Rose", 25, "red")
    alice.add_plant(rose)

    sun = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice.add_plant(sun)

    print(f"{alice.name} is helping all plants grow...")
    for plant in alice.plants:
        plant.grow()
        print(f"{plant.name} grew 1cm")

    print(f"=== {alice.name}'s Garden Report ===")
    print("Plants in garden:")
    for plant in alice.plants:
        print(f"- {plant}")

    stats = alice.stats()
    print(f'''Plants added: {stats['total_plants']}
          , Total growth: {stats['total_plants']}cm''')

    types = stats['types_of_plants']
    print(f'''Plant types: {types['Plant']} regular, {types['FloweringPlant']}
          flowering, {types['PrizeFlower']} prize flowers''')

    print(f"Height validation test: {GardenManager.validate_height(10)}")

    bob = Garden("Bob")
    bob.add_plant(Plant("Bush", 10))

    mgr = GardenManager.create_garden_network("Network", [alice, bob])

    bob_stats = bob.stats()

    print(f'''Garden scores - {alice.name}: {stats['score']},
          {bob.name}: {bob_stats['score']}''')
    print(f"Total gardens managed: {mgr.stats.len()}")
