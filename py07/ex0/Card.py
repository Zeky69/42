from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    """Abstract base class defining the universal card blueprint."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play the card, applying its effect to the game state."""
        pass

    def get_card_info(self) -> Dict:
        """Return a dictionary with the card's basic information."""
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        """Return True if the card can be played with the available mana."""
        return available_mana >= self.cost
