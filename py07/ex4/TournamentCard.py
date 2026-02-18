from typing import Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

_RATING_CHANGE = 16


class TournamentCard(Card, Combatable, Rankable):
    """Card with full combat and tournament ranking capabilities."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense: int,
        initial_rating: int = 1000,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self._rating = initial_rating
        self._wins = 0
        self._losses = 0

    # --- Card ---

    def play(self, game_state: dict) -> dict:
        """Deploy the tournament card to the battlefield."""
        if 'mana' in game_state:
            game_state['mana'] -= self.cost
        if 'battlefield' in game_state:
            game_state['battlefield'].append(self.name)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Tournament card enters the arena',
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info['type'] = 'Tournament'
        info['attack_power'] = self.attack_power
        info['defense'] = self.defense
        return info

    # --- Combatable ---

    def attack(self, target) -> dict:
        """Attack a target and return the combat result."""
        target_name = (
            target.name if hasattr(target, 'name') else str(target)
        )
        return {
            'attacker': self.name,
            'target': target_name,
            'damage': self.attack_power,
            'combat_type': 'tournament',
        }

    def defend(self, incoming_damage: int) -> dict:
        """Block incoming damage and return the result."""
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

    # --- Rankable ---

    def calculate_rating(self) -> int:
        return self._rating

    def update_wins(self, wins: int) -> None:
        """Record wins and increase rating."""
        self._wins += wins
        self._rating += wins * _RATING_CHANGE

    def update_losses(self, losses: int) -> None:
        """Record losses and decrease rating."""
        self._losses += losses
        self._rating -= losses * _RATING_CHANGE

    def get_rank_info(self) -> Dict:
        return {
            'name': self.name,
            'rating': self._rating,
            'wins': self._wins,
            'losses': self._losses,
        }

    # --- Tournament-specific ---

    def get_tournament_stats(self) -> Dict:
        """Return full tournament statistics for this card."""
        return {
            'name': self.name,
            'rating': self._rating,
            'wins': self._wins,
            'losses': self._losses,
            'attack_power': self.attack_power,
            'defense': self.defense,
        }

    def get_interfaces(self) -> List[str]:
        """Return the list of implemented interface names."""
        return ['Card', 'Combatable', 'Rankable']
