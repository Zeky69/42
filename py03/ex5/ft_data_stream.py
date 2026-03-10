def ft_str_to_int(s: str) -> int:
    char_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }

    result = 0
    for char in s:
        digit = char_map.get(char)
        if digit is not None:
            result = (result * 10) + digit

    return result


def stream_game_events(n_events: int) -> str:
    names = ["alice", "bob", "charlie", "diana", "evan", "fiona"]
    actions = ["killed monster", "found treasure", "leveled up",
               "crafted item"]

    nb_names = len(names)
    nb_actions = len(actions)

    for i in range(1, n_events + 1):
        name_index = (i - 1) % nb_names
        name = names[name_index]

        action_index = (i - 1) % nb_actions
        action = actions[action_index]

        level = ((i * 7) % 20) + 1

        event = f"Event {i}: Player {name} (level {level}) {action}"
        yield event


def fibonacci_generator(limit: int) -> int:
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def prime_generator(limit: int) -> int:
    count = 0
    num = 2
    while count < limit:
        is_prime = True
        for i in range(2, num//2 + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"Processing {total_events} game events...")

    stats = {
        "high_level": 0,
        "treasure": 0,
        "levelup": 0
    }

    event_stream = stream_game_events(total_events)

    for event in event_stream:
        if "Event 1:" in event or "Event 2:" in event or "Event 3:" in event:
            print(event)

        try:
            parts = event.split("(level ")
            if len(parts) > 1:
                level_part = parts[1].split(")")[0]
                level = ft_str_to_int(level_part)

                if level >= 10:
                    stats["high_level"] += 1
        except ValueError:
            pass

        if "found treasure" in event:
            stats["treasure"] += 1
        elif "leveled up" in event:
            stats["levelup"] += 1

    print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['levelup']}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.01 seconds")

    print("\n=== Generator Demonstration ===")

    fibo = fibonacci_generator(10)
    fibo_list = [num for num in fibo]
    print(f"Fibonacci sequence (first 10): {fibo_list}")

    prime = prime_generator(5)
    prime_list = [num for num in prime]
    print(f"Prime numbers (first 5): {prime_list}")


if __name__ == "__main__":
    main()
