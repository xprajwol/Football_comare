def talent_players():
    with open("talent.txt", "r") as talent:
        return [player.strip() for player in talent.read().split(",") if player.strip()]
