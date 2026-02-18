from typing import Dict, List
from ex0.Card import Card


class SpellCard(Card):
    """Concrete card representing an instant magical effect."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """Cast the spell, consuming it on use."""
        effects = {
            'damage': f'Deal {self.cost} damage to target',
            'heal': f'Restore {self.cost} health to target',
            'buff': f'Grant +{self.cost} to target',
            'debuff': f'Apply -{self.cost} to target',
        }
        effect_text = effects.get(
            self.effect_type, f'Apply {self.effect_type} effect'
        )
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': effect_text,
        }

    def resolve_effect(self, targets: List) -> Dict:
        """Resolve the spell effect against a list of targets."""
        return {
            'spell': self.name,
            'effect_type': self.effect_type,
            'targets': [str(t) for t in targets],
            'resolved': True,
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info['type'] = 'Spell'
        info['effect_type'] = self.effect_type
        return info
