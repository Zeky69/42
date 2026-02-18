from typing import Dict, List
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Concrete factory that produces fantasy-themed cards."""

    _CREATURES: List[Dict] = [
        {'name': 'Fire Dragon', 'cost': 5, 'rarity': 'Legendary',
         'attack': 7, 'health': 5},
        {'name': 'Goblin Warrior', 'cost': 2, 'rarity': 'Common',
         'attack': 5, 'health': 2},
    ]
    _SPELLS: List[Dict] = [
        {'name': 'Lightning Bolt', 'cost': 3, 'rarity': 'Common',
         'effect_type': 'damage'},
    ]
    _ARTIFACTS: List[Dict] = [
        {'name': 'Mana Ring', 'cost': 2, 'rarity': 'Rare',
         'durability': 5, 'effect': '+1 mana per turn'},
    ]

    def __init__(self) -> None:
        self._created = 0

    @property
    def created_count(self) -> int:
        return self._created

    def create_creature(
        self, name_or_power: 'str | int | None' = None
    ) -> CreatureCard:
        """Create a fantasy creature card."""
        data = self._CREATURES[0]
        if isinstance(name_or_power, str):
            for c in self._CREATURES:
                if c['name'].lower() == name_or_power.lower():
                    data = c
                    break
        elif isinstance(name_or_power, int):
            data = self._CREATURES[
                name_or_power % len(self._CREATURES)
            ]
        self._created += 1
        return CreatureCard(
            data['name'], data['cost'], data['rarity'],
            data['attack'], data['health'],
        )

    def create_spell(
        self, name_or_power: 'str | int | None' = None
    ) -> SpellCard:
        """Create a fantasy spell card."""
        data = self._SPELLS[0]
        self._created += 1
        return SpellCard(
            data['name'], data['cost'], data['rarity'],
            data['effect_type'],
        )

    def create_artifact(
        self, name_or_power: 'str | int | None' = None
    ) -> ArtifactCard:
        """Create a fantasy artifact card."""
        data = self._ARTIFACTS[0]
        self._created += 1
        return ArtifactCard(
            data['name'], data['cost'], data['rarity'],
            data['durability'], data['effect'],
        )

    def create_themed_deck(self, size: int) -> dict:
        """Create a balanced themed deck of the given size."""
        deck: Dict = {'creatures': [], 'spells': [], 'artifacts': []}
        for i in range(size):
            if i % 3 == 0:
                deck['creatures'].append(self.create_creature(i // 3))
            elif i % 3 == 1:
                deck['spells'].append(self.create_spell())
            else:
                deck['artifacts'].append(self.create_artifact())
        return deck

    def get_supported_types(self) -> dict:
        """Return the card types and themes supported by this factory."""
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring'],
        }
