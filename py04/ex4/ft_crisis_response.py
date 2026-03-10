
def crisis_handler(filename):
    print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as vault:
            content = vault.read().strip()
            print(f"SUCCESS: Archive recovered - {content}")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly: {e}")
        print("STATUS: Crisis handled, recovery protocols active")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("lost_archive.txt")
    print()
    crisis_handler("classified_vault.txt")
    print()
    crisis_handler("standard_archive.txt")
    print()
    print("\nAll crisis scenarios handled successfully. Archives secure.")
