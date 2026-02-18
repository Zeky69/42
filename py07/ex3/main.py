from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("Simulating aggressive turn...")
    result = engine.simulate_turn()

    hand_str = '[' + ', '.join(result['hand']) + ']'
    print(f"Hand: {hand_str}")
    print("Turn execution:")
    turn = result['turn_result']
    print(f"Strategy: {turn['strategy']}")
    print(f"Actions: {turn['actions']}")

    print("Game Report:")
    print(engine.get_engine_status())

    print(
        "Abstract Factory + Strategy Pattern: "
        "Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
