import sys
if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores = []
    error_found = False
    for i in sys.argv[1:]:
        try:
            score = int(i)
            scores.append(score)
        except ValueError:
            print(f"Error: Invalid score '{i}'")
            error_found = True
            break
    if not scores and not error_found:
        print("No scores provided. Usage: python3 " +
              "ft_score_analytics.py <score1> <score2> ...")
    elif not error_found:
        total_scores = sum(scores)
        highest_score = max(scores)
        lowest_score = min(scores)
        average_score = total_scores / len(scores)
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {total_scores}")
        print(f"Average score: {average_score:.2f}")
        print(f"High score: {highest_score}")
        print(f"Low score: {lowest_score}")
        print(f"Score range: {highest_score - lowest_score}")
