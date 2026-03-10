
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        with open("ancient_fragment.txt", "r") as file:
            print("Connection established...\n")
            content = file.read()
            print("RECOVERED DATA:")
            print(content)
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")
