def good_players():
    with open("good.txt", "r") as good:
        return [player.strip() for player in good.read().split(",") if player.strip()]
