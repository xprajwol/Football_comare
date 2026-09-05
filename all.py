def all_players():
    with open("all.txt", "r") as a:
        return [player.strip() for player in a.read().split(",") if player.strip()]
    print(all_players())
