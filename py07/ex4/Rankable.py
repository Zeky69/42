from abc import ABC, abstractmethod


class Rankable(ABC):
    """Abstract interface for tournament ranking capabilities."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return the current competitive rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Record additional wins and adjust rating accordingly."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Record additional losses and adjust rating accordingly."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Return a summary of the current ranking information."""
        pass
