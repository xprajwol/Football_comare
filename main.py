def main():

    # Import the necessary functions from the respective modules
    from all import all_players
    from goat import goat_players
    from legends import legends_players
    from great import great_players
    from good import good_players
    from talent import talent_players

    #print all players name in the list
    print(all_players())
    

    # Get user input for a player name
    user_input = input("Enter a player name: ")

    #Loop up to player say bye
    while user_input.lower() != "bye":
        #checking area
        if user_input.strip().casefold() in {name.casefold() for name in goat_players()}:
            print(f"{user_input} is a GOAT player!")
        elif user_input.strip().casefold() in {name.casefold() for name in legends_players()}:
            print(f"{user_input} is a LEGEND player!")
        elif user_input.strip().casefold() in {name.casefold() for name in great_players()}:
            print(f"{user_input} is a GREAT player!")
        elif user_input.strip().casefold() in {name.casefold() for name in good_players()}:
            print(f"{user_input} is a GOOD player!")
        elif user_input.strip().casefold() in {name.casefold() for name in talent_players()}:
            print(f"{user_input} is a TALENT player!")
        else:
            print(f"{user_input} is not a recognized player.")
        
        # Get the next player name
        user_input = input("Enter a player name (or 'bye' to exit): ")
      

#main function calling
if __name__ == "__main__":
    main()
