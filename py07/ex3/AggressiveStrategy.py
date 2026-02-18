from typing import List
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Strategy that prioritizes attacking and board presence."""

    AVAILABLE_MANA = 5

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        """Return targets sorted by priority (player direct > creatures)."""
        return sorted(
            available_targets,
            key=lambda t: 0 if t == 'Enemy Player' else 1,
        )

    def execute_turn(self, hand: List, battlefield: List) -> dict:
        """Play low-cost cards first, then attack targets."""
        mana = self.AVAILABLE_MANA
        played = []
        damage = 0

        for card in sorted(hand, key=lambda c: c.cost):
            if card.cost <= mana:
                played.append(card)
                mana -= card.cost
                if isinstance(card, CreatureCard):
                    damage += card.attack
                elif (
                    isinstance(card, SpellCard)
                    and card.effect_type == 'damage'
                ):
                    damage += card.cost

        targets = self.prioritize_targets(['Enemy Player'])

        return {
            'strategy': self.get_strategy_name(),
            'actions': {
                'cards_played': [c.name for c in played],
                'mana_used': self.AVAILABLE_MANA - mana,
                'targets_attacked': targets,
                'damage_dealt': damage,
            },
        }
