from typing import Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Powerful card combining combat and magical abilities."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense: int,
        mana_pool: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.mana_pool = mana_pool

    def play(self, game_state: dict) -> dict:
        """Deploy the elite card to the battlefield."""
        if 'mana' in game_state:
            game_state['mana'] -= self.cost
        if 'battlefield' in game_state:
            game_state['battlefield'].append(self.name)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Elite card deployed with combat and magic',
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info['type'] = 'Elite'
        info['attack_power'] = self.attack_power
        info['defense'] = self.defense
        info['mana_pool'] = self.mana_pool
        return info

    def attack(self, target) -> dict:
        """Perform a melee attack against a target."""
        target_name = target.name if hasattr(target, 'name') else str(target)
        return {
            'attacker': self.name,
            'target': target_name,
            'damage': self.attack_power,
            'combat_type': 'melee',
        }

    def defend(self, incoming_damage: int) -> dict:
        """Block incoming damage using the defense value."""
        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked
        return {
            'defender': self.name,
            'damage_taken': taken,
            'damage_blocked': blocked,
            'still_alive': True,
        }

    def get_combat_stats(self) -> Dict:
        return {
            'name': self.name,
            'attack_power': self.attack_power,
            'defense': self.defense,
        }

    def cast_spell(self, spell_name: str, targets: List) -> dict:
        """Cast a named spell against a list of targets."""
        mana_cost = len(targets) * 2
        self.mana_pool = max(0, self.mana_pool - mana_cost)
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': [t if isinstance(t, str) else t.name
                        for t in targets],
            'mana_used': mana_cost,
        }

    def channel_mana(self, amount: int) -> dict:
        """Channel additional mana into the pool."""
        self.mana_pool += amount
        return {
            'channeled': amount,
            'total_mana': self.mana_pool,
        }

    def get_magic_stats(self) -> Dict:
        return {
            'name': self.name,
            'mana_pool': self.mana_pool,
        }
