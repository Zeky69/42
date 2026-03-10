import sys


def manage_communication_streams():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: \n")

    sys.stdout.write(f"[STANDARD] Archive status from {id}: {status}\n")

    sys.stderr.write("[ALERT] System diagnostic: Communication channels \
verified\n")

    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    manage_communication_streams()
