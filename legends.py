def legends_players():
    with open("legends.txt", "r") as legends:
        return [player.strip() for player in legends.read().split(",") if player.strip()]
