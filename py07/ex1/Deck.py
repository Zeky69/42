import random
from typing import Dict, List, Optional
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    """Deck management system for any card type derived from Card."""

    def __init__(self) -> None:
        self._cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove the first card with the given name. Returns True if found."""
        for i, card in enumerate(self._cards):
            if card.name == card_name:
                self._cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        """Randomly shuffle the deck in place."""
        random.shuffle(self._cards)

    def draw_card(self) -> Optional[Card]:
        """Draw and return the top card of the deck."""
        if not self._cards:
            return None
        return self._cards.pop(0)

    def get_deck_stats(self) -> Dict:
        """Return statistics about the current deck composition."""
        total = len(self._cards)
        creatures = sum(
            1 for c in self._cards if isinstance(c, CreatureCard)
        )
        spells = sum(
            1 for c in self._cards if isinstance(c, SpellCard)
        )
        artifacts = sum(
            1 for c in self._cards if isinstance(c, ArtifactCard)
        )
        avg_cost = (
            round(sum(c.cost for c in self._cards) / total, 1)
            if total > 0 else 0.0
        )
        return {
            'total_cards': total,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': avg_cost,
        }
