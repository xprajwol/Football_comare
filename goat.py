def goat_players():
    with open("goat.txt", "r") as goat:
        return [player.strip() for player in goat.read().split(",") if player.strip()]
