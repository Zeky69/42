from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 2, 1)

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    available_mana = 6
    game_state = {'mana': available_mana, 'battlefield': []}
    print(f"Playing {dragon.name} with {available_mana} mana available:")
    print(f"Playable: {dragon.is_playable(available_mana)}")
    print(f"Play result: {dragon.play(game_state)}")

    print(f"{dragon.name} attacks {goblin.name}:")
    print(f"Attack result: {dragon.attack_target(goblin)}")

    low_mana = 3
    print(f"Testing insufficient mana ({low_mana} available):")
    print(f"Playable: {dragon.is_playable(low_mana)}")

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
