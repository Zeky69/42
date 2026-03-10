"""
Docstring for ex4.ft_inventory_system
"""

import sys


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


def main() -> None:
    inventory = dict()

    for arg in sys.argv[1:]:
        parts = arg.split(':')
        name = parts[0]
        try:
            quantity = ft_str_to_int(parts[1])
            inventory.update({name: quantity})
        except ValueError:
            continue
    total_items = 0
    for qty in inventory.values():
        total_items += qty

    unique_types = len(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")

    print("=== Current Inventory ===")
    processed = dict()

    for _ in inventory:
        max_qty = -1
        max_key = ""

        for key, val in inventory.items():
            if processed.get(key) is None:
                if val > max_qty:
                    max_qty = val
                    max_key = key
                elif val == max_qty:
                    pass
        if max_key != "":
            percentage = (max_qty / total_items) * 100
            unit_str = "unit" if max_qty == 1 else "units"
            print(f"{max_key}: {max_qty} {unit_str} ({percentage:.1f}%)")
            processed[max_key] = 1

    print("=== Inventory Statistics ===")
    most_abundant_item = ""
    most_abundant_qty = -1
    least_abundant_item = ""
    least_abundant_qty = total_items + 1 if total_items > 0 else 0

    for key, val in inventory.items():
        if val > most_abundant_qty:
            most_abundant_qty = val
            most_abundant_item = key

        if val < least_abundant_qty:
            least_abundant_qty = val
            least_abundant_item = key

    most_unit = "unit" if most_abundant_qty == 1 else "units"
    least_unit = "unit" if least_abundant_qty == 1 else "units"

    print(f"Most abundant: {most_abundant_item} \
({most_abundant_qty} {most_unit})")
    print(f"Least abundant: {least_abundant_item} \
({least_abundant_qty} {least_unit})")

    print("=== Item Categories ===")
    categories = dict()
    categories['Moderate'] = dict()
    categories['Scarce'] = dict()

    for key, val in inventory.items():
        if val >= 5:
            categories['Moderate'].update({key: val})
        else:
            categories['Scarce'].update({key: val})

    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")

    print("=== Management Suggestions ===")
    restock_needed = []
    for key, val in inventory.items():
        if val < 2:
            restock_needed = restock_needed + [key]

    print(f"Restock needed: {restock_needed}")

    print("=== Dictionary Properties Demo ===")

    keys_list = [k for k in inventory.keys()]
    values_list = [v for v in inventory.values()]

    print(f"Dictionary keys: {keys_list}")
    print(f"Dictionary values: {values_list}")

    check_item = 'sword'

    exists = inventory.get(check_item) is not None
    print(f"Sample lookup - '{check_item}' in inventory: {exists}")


if __name__ == "__main__":
    main()
