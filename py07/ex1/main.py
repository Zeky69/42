from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(ArtifactCard(
        "Mana Crystal", 2, "Rare", 5, "+1 mana per turn"
    ))
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("Drawing and playing cards:")
    for _ in range(3):
        card = deck.draw_card()
        if card is None:
            break
        card_type = card.get_card_info().get('type', 'Unknown')
        print(f"Drew: {card.name} ({card_type})")
        print(f"Play result: {card.play({})}")

    print(
        "Polymorphism in action: Same interface, different card behaviors!"
    )


if __name__ == "__main__":
    main()
