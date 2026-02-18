import random
from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Manages card registration, matches, and rankings."""

    def __init__(self) -> None:
        self._cards: Dict[str, TournamentCard] = {}
        self._id_counters: Dict[str, int] = {}
        self._matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a card and return its unique tournament ID."""
        prefix = card.name.split()[-1].lower()
        self._id_counters[prefix] = (
            self._id_counters.get(prefix, 0) + 1
        )
        card_id = f"{prefix}_{self._id_counters[prefix]:03d}"
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Simulate a match between two registered cards."""
        c1 = self._cards[card1_id]
        c2 = self._cards[card2_id]

        if c1.attack_power > c2.attack_power:
            winner_id, loser_id = card1_id, card2_id
        elif c2.attack_power > c1.attack_power:
            winner_id, loser_id = card2_id, card1_id
        else:
            winner_id, loser_id = random.choice(
                [(card1_id, card2_id), (card2_id, card1_id)]
            )

        winner = self._cards[winner_id]
        loser = self._cards[loser_id]
        winner.update_wins(1)
        loser.update_losses(1)
        self._matches_played += 1

        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating(),
        }

    def get_leaderboard(self) -> List[dict]:
        """Return cards sorted by rating, highest first."""
        sorted_cards = sorted(
            self._cards.items(),
            key=lambda item: item[1].calculate_rating(),
            reverse=True,
        )
        board = []
        for rank, (card_id, card) in enumerate(sorted_cards, 1):
            info = card.get_rank_info()
            board.append({
                'rank': rank,
                'name': info['name'],
                'rating': info['rating'],
                'wins': info['wins'],
                'losses': info['losses'],
            })
        return board

    def generate_tournament_report(self) -> dict:
        """Return a summary report of the tournament platform."""
        total = len(self._cards)
        avg = (
            sum(c.calculate_rating() for c in self._cards.values())
            // total
        ) if total > 0 else 0
        return {
            'total_cards': total,
            'matches_played': self._matches_played,
            'avg_rating': avg,
            'platform_status': 'active',
        }
