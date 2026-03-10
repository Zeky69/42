import sys


if __name__ == "__main__":
    print("=== Command Quest ===")

    if len(sys.argv) == 1:
        print("No arguments provided!")

    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")

        index = 1
        for arg in sys.argv[1:]:
            print(f"Argument {index}: {arg}")
            index += 1

    print(f"Total arguments: {len(sys.argv)}")
