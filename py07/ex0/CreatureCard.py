from typing import Dict
from ex0.Card import Card


class CreatureCard(Card):
    """Concrete card representing a creature on the battlefield."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """Summon the creature to the battlefield."""
        if 'mana' in game_state:
            game_state['mana'] -= self.cost
        if 'battlefield' in game_state:
            game_state['battlefield'].append(self.name)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield',
        }

    def get_card_info(self) -> Dict:
        """Return a dictionary with full creature card information."""
        info = super().get_card_info()
        info['type'] = 'Creature'
        info['attack'] = self.attack
        info['health'] = self.health
        return info

    def attack_target(self, target: 'CreatureCard') -> dict:
        """Resolve combat between this creature and a target."""
        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack,
            'combat_resolved': True,
        }
