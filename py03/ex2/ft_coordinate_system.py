import math


def calculate_distance(p1: tuple, p2: tuple) -> float:
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 +
                     (p2[2] - p1[2]) ** 2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    pos1 = (10, 20, 5)
    print(f"Position created: {pos1}")

    origin = (0, 0, 0)
    dist1 = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {dist1:.2f}\n")

    coord_str = "3,4,0"
    print(f"Parsing coordinates: \"{coord_str}\"")

    parts = coord_str.split(',')
    pos2 = (int(parts[0]), int(parts[1]), int(parts[2]))

    print(f"Parsed position: {pos2}")
    dist2 = calculate_distance(origin, pos2)
    print(f"Distance between {origin} and {pos2}: {dist2:.1f}\n")

    invalid_str = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{invalid_str}\"")

    try:
        parts_invalid = invalid_str.split(',')
        invalid_pos = (int(parts_invalid[0]), int(parts_invalid[1]),
                       int(parts_invalid[2]))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")

    print("\nUnpacking demonstration:")
    x, y, z = pos2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
