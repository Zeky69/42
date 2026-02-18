from typing import Dict
from ex0.Card import Card


class ArtifactCard(Card):
    """Concrete card representing a permanent game modifier."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """Place the artifact into play as a permanent modifier."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Permanent: {self.effect}',
        }

    def activate_ability(self) -> Dict:
        """Activate the artifact's ongoing ability, consuming durability."""
        if self.durability <= 0:
            return {
                'artifact': self.name,
                'activated': False,
                'reason': 'No durability remaining',
            }
        self.durability -= 1
        return {
            'artifact': self.name,
            'effect': self.effect,
            'activated': True,
            'durability_remaining': self.durability,
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info['type'] = 'Artifact'
        info['durability'] = self.durability
        info['effect'] = self.effect
        return info
