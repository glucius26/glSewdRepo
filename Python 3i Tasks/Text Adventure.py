def display_title():
    print("|-----------------------------------------------|")
    print("|  ----  -----   -----   .  ------  -------   | |")
    print("| |        |     |   /      |       |         | |")
    print("|  ----    |     |---    |  |---    |------   | |")
    print("|     |    |     |   \   |  |       |           |")
    print("|  ----    |     |    |  |  |       |______   . |")
    print("|-----------------------------------------------|")
    print("Welcome to Strife!")
    print("1. Begin")
    print("2. Quit")
    menuChoice = int(input("Enter your choice: "))
    if menuChoice == 1:
        display_location(current_room)
    else:
        return
    pass

def display_location(location_name):
    """Display description of current location."""
    # Hint: Use if/elif statements or a dictionary
    # to store location descriptions
    if location_name == "start":
        print("You awoke in a dark cavern, struggling to remember what happened last, or how you got there. All you know is that you have to leave this place.")
        get_command()
    elif location_name == "center":
        print("You limp your way to a room that is much larger than the one you came from, your tiny footsteps almost echoing against the walls.")
        get_command()
    pass

def get_command():
    """Get a command from the player. Return the command."""
    # Commands might be: north, south, east, west, take, inventory, quit
    if current_room == "start":
        action = str(input("Do you want to examine the room(ex), head north(hn), or check inventory(inv)? "))
        if action == "ex" and "map" not in inventory:
            print("You strain your eyes, trying to find something, anything to help you.")
            print("You find a rough-looking map on the floor. (GOT MAP)")
            inventory.append("map")
            get_command()
        elif action == "ex" and "map" in inventory:
            print("You couldn't find anything else.")
            get_command()
        elif action == "hn":
            move_player("start", "hn")
        elif action == "inv":
            show_inventory(inventory)
    elif current_room == "center":
        action = str(input("Testing testing"))
    pass

def move_player(current_location, direction):
    """
    Move the player in the given direction.
    Return the new location, or current location if can't move that way.
    """
    if current_location == "start" and direction == "hn":
        current_room = "center"
        display_location(current_room)
    pass

def show_inventory(items):
    """Display the player's inventory."""
    print("Inventory:")
    for item in inventory:
        print(f"{item} ", end="")
    print(" ")
    print("Type the name of the object you want to use or type ex to exit")
    invChoice = str(input(" "))
    if invChoice == "ex":
        get_command()
    pass

def check_win_condition(items):
    """Check if player has won. Return True or False."""
    # YOUR CODE HERE
    pass

# Main program
current_room = "start"
inventory = []
playing = True
display_title()

# YOUR CODE HERE - Write the main game loop
# Use the functions above to create the complete program