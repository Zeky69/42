def main() -> None:
    print("=== Game Analytics Dashboard ===")

    raw_data = [
        {
            "name": "alice",
            "score": 2300,
            "achievements": ["first_kill", "level_10", "boss_slayer"],
            "region": "north"
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": ["first_kill", "team_player"],
            "region": "east"
        },
        {
            "name": "charlie",
            "score": 2150,
            "achievements": ["level_10", "collector", "boss_slayer", "mvp"],
            "region": "north"
        },
        {
            "name": "diana",
            "score": 2050,
            "achievements": ["speed_run", "no_damage"],
            "region": "central"
        }
    ]

    print("\n=== List Comprehension Examples ===")

    high_scorers = [p["name"] for p in raw_data if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [p["score"] * 2 for p in raw_data]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [
        p["name"] for p in raw_data if len(p["achievements"]) > 0
    ]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {p["name"]: p["score"] for p in raw_data}
    print(f"Player scores: {player_scores}")

    achievement_counts = {p["name"]: len(p["achievements"]) for p in raw_data}
    print(f"Achievement counts: {achievement_counts}")

    score_categories = {
        "high": sum([1 for p in raw_data if p["score"] > 2000]),
        "medium": sum([1 for p in raw_data if 1500 <= p["score"] <= 2000]),
        "low": sum([1 for p in raw_data if p["score"] < 1500])
    }
    print(f"Score categories: {score_categories}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = {p["name"] for p in raw_data}
    print(f"Unique players: {sorted(unique_players)}")

    unique_achievements = {ach for p in raw_data for ach in p["achievements"]}
    print(f"Unique achievements: {sorted(unique_achievements)}")

    active_regions = {p["region"] for p in raw_data}
    print(f"Active regions: {sorted(active_regions)}")

    print("\n=== Combined Analysis ===")

    total_players = len(raw_data)
    total_unique_ach = len(unique_achievements)

    all_scores = [p["score"] for p in raw_data]
    if len(all_scores) > 0:
        average_score = sum(all_scores) / len(all_scores)
    else:
        average_score = 0

    max_score_val = max(all_scores)
    top_performer = [p for p in raw_data if p["score"] == max_score_val][0]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_ach}")
    print(f"Average score: {average_score}")

    tp_name = top_performer['name']
    tp_score = top_performer['score']
    tp_ach_count = len(top_performer['achievements'])

    print(f"Top performer: {tp_name} ({tp_score} points, "
          f"{tp_ach_count} achievements)")


if __name__ == "__main__":
    main()
