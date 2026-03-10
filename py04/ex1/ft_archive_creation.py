def create_new_archive():
    filename = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"Initializing new storage unit: {filename}")

    try:

        with open(filename, "w") as vault:
            print("Storage unit created successfully...")
            print("Inscribing preservation data...")
            entry1 = "[ENTRY 001] New quantum algorithm discovered\n"
            entry2 = "[ENTRY 002] Efficiency increased by 347%\n"
            entry3 = "[ENTRY 003] Archived by Data Archivist trainee\n"

            vault.write(entry1)
            vault.write(entry2)
            vault.write(entry3)

            print(entry1.strip())
            print(entry2.strip())
            print(entry3.strip())

        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")

    except Exception as e:
        print(f"CRITICAL ERROR: Failed to initialize storage unit: {e}")


if __name__ == "__main__":
    create_new_archive()
