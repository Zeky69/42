from typing import Optional, List
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Orchestrates card game turns using pluggable factory and strategy."""

    def __init__(self) -> None:
        self._factory: Optional[CardFactory] = None
        self._strategy: Optional[GameStrategy] = None
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """Attach a card factory and strategy to the engine."""
        self._factory = factory
        self._strategy = strategy

    def _build_hand(self) -> List:
        """Create a representative hand using the configured factory."""
        dragon = self._factory.create_creature('Fire Dragon')
        goblin = self._factory.create_creature('Goblin Warrior')
        bolt = self._factory.create_spell()
        self._cards_created += 3
        return [dragon, goblin, bolt]

    def simulate_turn(self) -> dict:
        """Simulate one game turn and return the result."""
        if self._factory is None or self._strategy is None:
            raise RuntimeError("Engine not configured. Call configure_engine.")

        hand = self._build_hand()
        hand_display = [
            f"{c.name} ({c.cost})" for c in hand
        ]

        result = self._strategy.execute_turn(hand, [])
        damage = result['actions']['damage_dealt']
        self._total_damage += damage
        self._turns_simulated += 1

        return {
            'hand': hand_display,
            'turn_result': result,
        }

    def get_engine_status(self) -> dict:
        """Return current engine statistics."""
        strategy_name = (
            self._strategy.get_strategy_name()
            if self._strategy else 'None'
        )
        return {
            'turns_simulated': self._turns_simulated,
            'strategy_used': strategy_name,
            'total_damage': self._total_damage,
            'cards_created': self._cards_created,
        }
