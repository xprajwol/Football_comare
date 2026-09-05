def great_players():
    with open("great.txt", "r") as great:
        return [player.strip() for player in great.read().split(",") if player.strip()]
