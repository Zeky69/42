from abc import ABC, abstractmethod


class Combatable(ABC):
    """Abstract interface defining combat capabilities."""

    @abstractmethod
    def attack(self, target) -> dict:
        """Attack a target and return combat result."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage and return result."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Return the current combat statistics."""
        pass
