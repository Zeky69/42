from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")

    card_methods = ['play', 'get_card_info', 'is_playable']
    combat_methods = ['attack', 'defend', 'get_combat_stats']
    magic_methods = ['cast_spell', 'channel_mana', 'get_magic_stats']

    print("EliteCard capabilities:")
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combat_methods}")
    print(f"- Magical: {magic_methods}")

    warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 3, 8)

    print(f"Playing {warrior.name} (Elite Card):")

    print("Combat phase:")
    print(f"Attack result: {warrior.attack('Enemy')}")
    print(f"Defense result: {warrior.defend(5)}")

    print("Magic phase:")
    spell = warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])
    print(f"Spell cast: {spell}")
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
