
def parse_score(text):
    """Parse A-B score and return two integers."""
    if not isinstance(text, str):
        return None

    try:
        parts = text.strip().split('-')

        if len(parts) != 2:
            return None

        a, b = parts

        if not a.strip() or not b.strip():
            return None

        a, b = int(a.strip()), int(b.strip())

        if a < 0 or b < 0:
            return None

        return a, b

    except (ValueError, TypeError):
        return None


def game_lead(text):
    """Calculate the difference between valid tennis points."""
    if not isinstance(text, str):
        return None

    points = {'0': 0, '15': 1, '30': 2, '40': 3}

    try:
        parts = text.strip().split('-')

        if len(parts) != 2:
            return None

        first, second = parts
        first = first.strip()
        second = second.strip()

        if first not in points or second not in points:
            return None

        return points[first] - points[second]

    except (ValueError, TypeError):
        return None


def set_spread(games_csv):
    """Calculate maximum minus minimum games."""
    if not isinstance(games_csv, str):
        return None

    try:
        parts = games_csv.strip().split(',')

        if any(not p.strip() for p in parts):
            return None

        games = [int(p.strip()) for p in parts]

        if not games or any(g < 0 for g in games):
            return None

        return max(games) - min(games)

    except (ValueError, TypeError):
        return None


def main():
    print("==== Running parse_score ====")
    user_input = input("Enter points won as A-B (e.g. 3-2): ")
    result = parse_score(user_input)
    print("Points A and B:", result)

    print("\n==== Running game_lead ====")
    user_input = input("Enter a game score (e.g. 40-30): ")
    result = game_lead(user_input)
    print("Lead in Points:", result)

    print("\n==== Running set_spread ====")
    user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
    result = set_spread(user_input)
    print("Spread:", result)


if __name__ == "__main__":
    main()
