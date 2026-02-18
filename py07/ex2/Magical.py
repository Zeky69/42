from abc import ABC, abstractmethod
from typing import List


class Magical(ABC):
    """Abstract interface defining magical capabilities."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List) -> dict:
        """Cast a spell against one or more targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Channel mana to increase the available mana pool."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Return the current magic statistics."""
        pass
