def secure_vault_operations():

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    try:
        with open("classified_data.txt", "r") as source:
            print("\nSECURE EXTRACTION:")
            content = source.read()
            print(content.strip())
    except FileNotFoundError:
        print("ERROR: Classified data vault not found.")
    except Exception as e:
        print(f"ERROR: An unexpected error occurred during extraction: {e}")

    with open("security_protocols.txt", "w") as vault:
        print("\nSECURE PRESERVATION:")
        log_entry = "[CLASSIFIED] New security protocols archived"
        vault.write(log_entry + "\n")
        print(log_entry)

    print("\nVault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    secure_vault_operations()
