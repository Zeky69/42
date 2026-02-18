from abc import ABC, abstractmethod
from typing import List


class GameStrategy(ABC):
    """Abstract interface for game turn strategies."""

    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> dict:
        """Execute a full turn given the current hand and battlefield."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of this strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List) -> List:
        """Return targets sorted by strategic priority."""
        pass
