from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def _fmt_interfaces(interfaces: list) -> str:
    return '[' + ', '.join(interfaces) + ']'


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")

    platform = TournamentPlatform()

    dragon = TournamentCard(
        "Fire Dragon", 5, "Legendary", 7, 3, 1200
    )
    wizard = TournamentCard(
        "Ice Wizard", 4, "Rare", 4, 6, 1150
    )

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    for card, card_id in [(dragon, dragon_id), (wizard, wizard_id)]:
        info = card.get_rank_info()
        interfaces = _fmt_interfaces(card.get_interfaces())
        print(f"{card.name} (ID: {card_id}):")
        print(f"- Interfaces: {interfaces}")
        print(f"- Rating: {info['rating']}")
        print(f"- Record: {info['wins']}-{info['losses']}")

    print("Creating tournament match...")
    match = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match}")

    print("Tournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(
            f"{entry['rank']}. {entry['name']} - "
            f"Rating: {entry['rating']} "
            f"({entry['wins']}-{entry['losses']})"
        )

    print("Platform Report:")
    print(platform.generate_tournament_report())

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously! ")


if __name__ == "__main__":
    main()
