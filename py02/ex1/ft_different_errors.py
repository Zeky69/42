"""
This module demonstrates handling different types of errors
that may occur in agricultural data processing.
"""


def garden_operations(action: str) -> None:
    """
    Docstring for garden_operations
    :param action: Description
    """
    if action == "value":
        int("abc")
    elif action == "zero":
        print(1 / 0)
    elif action == "file":
        f = open("missing.txt", "r")
        f.close()
    elif action == "key":
        plant_dict = {"rose": 5, "tulip": 10}
        print(plant_dict["missing_plant"])


def test_error_types() -> None:
    print("\nTesting ValueError...")
    try:
        garden_operations("value")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
