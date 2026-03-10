"""
Docstring for ex5.ft_count_harvest_recursive
"""


def ft_count_harvest_recursive():
    def countdown(day):
        if day == 0:
            return
        countdown(day - 1)
        print(f"Day {day}")

    days_until_harvest = int(input("Days until harvest: "))
    countdown(days_until_harvest)
    print("Harvest time!")
