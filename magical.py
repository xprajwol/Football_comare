def magical_players():
    with open("magical.txt", "r") as magical:
        return [player.strip() for player in magical.read().split(",") if player.strip()]
