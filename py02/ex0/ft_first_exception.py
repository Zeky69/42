"""
Module for validating agricultural temperature data.

This module provides a robust way to check temperature inputs
and handle errors gracefully without crashing.
"""


def check_temperature(temp_str: str) -> int | None:
    """
    Validates and converts a temperature string.

    Args:
        temp_str (str): The temperature input to check.

    Returns:
        int: The valid temperature if successful, None otherwise.
    """
    try:
        temp = int(temp_str)

        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input() -> None:
    """
    Demonstrates the validation pipeline with various inputs.
    """
    inputs = ["25", "abc", "100", "-50"]

    for value in inputs:
        print(f"Testing temperature: {value}")
        check_temperature(value)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature_input()
