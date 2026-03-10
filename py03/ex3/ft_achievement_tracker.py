if __name__ == "__main__":

    print("=== Achievement Tracker System ===\n")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}")

    unique_alice = alice.difference(bob).difference(charlie)
    unique_bob = bob.difference(alice).difference(charlie)
    unique_charlie = charlie.difference(alice).difference(bob)

    rare_achievements = unique_alice.union(unique_bob).union(unique_charlie)
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    alice_bob_common = alice.intersection(bob)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)

    print(f"Alice vs Bob common: {alice_bob_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")
