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
    elif location_name == "northmost":
        print("Heading north you find a very strange room, smaller than the others, but just as empty.")
        get_command()
    elif location_name == "eastmost":
        print("Heading east you enter yet another room, this one with particularly high ceilings.")
        get_command()
    elif location_name == "westmost":
        print("Heading west you find another stone room. This one resembles a dining hall.")
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
        action = str(input("Do you want to examine the room(ex), head north(hn), head east(he), head south(hs), head west(hw), or check inventory(inv) "))
        if action == "ex":
            print("This room is much larger than the others, though very empty, there is a very large crystal in the center. On the crystal there is an inscryption: 'If thou wants to leave, thou must face my master. Be forewarned, he will not leave without resistance' There is a button-shaped protrusion next to the text.")
            if "Warhammer Of Zillyhoo" not in inventory:
                print("You decide you'll need a weapon of some kind to face, 'The Master.'")
                get_command()
            else:
                print("you steel yourself for the upcoming strife as you press the button.")
                print("The crystal immediately rumbles to life, reshaping itself into what you can only describe as a crystal golem.")
                print("You ready the Warhammer of Zillyhoo and ...")
                print("WHAM!")
                print("After just a single strike from the mighty hammer, the golem is shattered. Perhaps it was the power of the WOZ, or maybe it was just because crystal isn't that strong...")
                print("A strange light fills the cavern. It surrounds you.")
                print("It envelops you.")
                print("The light blinds you, and you shut your eyes, putting your hands over to shield them.")
                print("silence")
                print("...")
                print("...")
                print("...")
                print("...")
                print("...")
                print("You peek from behind your hands...")
                print("You lay outside on grass as the world's noise returns. You have escaped the cavern.")
                check_win_condition(True)
        elif action == "hn":
            move_player("center", "hn")
        elif action == "he":
            move_player("center", "he")
        elif action == "hs":
            move_player("center", "hs")
        elif action == "hw":
            move_player("center", "hw")
        elif action == "inv":
            show_inventory(inventory)
    elif current_room == "northmost":
        action = str(input("Do you want to examine room(ex), check inventory(inv), or head back(hb)?"))
        if action == "ex":
            print("A long, colorful box sits in the center of the room. The box appears to be locked with a password with 5 digits. On the walls of the chamber are the numbers '4128,' then claw marks where the last number would be.")
            if "paper" not in inventory:
                print("Guess I'll have to find the last number...")
                get_command()
            elif "paper" in inventory:
                codeQ = int(input("|Enter Code: "))
                if codeQ == 41286:
                    print("...")
                    print("...")
                    print("...")
                    print("Click")
                    print("The box flings open, revealing a colorful and very powerful looking hammer. It's definitely not a reference to Homestuck.")
                    print("GOT WARHAMMER OF ZILLYHOO")
                    inventory.append("Warhammer Of Zillyhoo")
                    get_command()
                else:
                    print("...")
                    print("...")
                    print("...")
                    print("...Nothing happened.")
                    get_command()
        elif action == "inv":
            show_inventory(inventory)
        elif action == "hb":
            move_player("northmost", "hb")
    elif current_room == "eastmost":
        action = str(input("Do you want to examine the room(ex), check inventory(inv), or head back(hb)?"))
        if action == "ex" and "strange rock" not in inventory:
            print("This room is box-like, only slightly larger from the room you woke up in. You see a strange purple rock in the center.")
            print("GOT PURPLEROCK")
            inventory.append("strange rock")
            get_command()
        elif action == "ex" and "strange rock" in inventory:
            print("The same room, only strange rock-less.")
            get_command()
        elif action == "inv":
            show_inventory(inventory)
        elif action == "hb":
            move_player("eastmost", "hb")
    elif current_room == "westmost":
        action = str(input("Do you want to examine the room(ex), check inventory(inv), or head back(hb)?"))
        if action == "ex" and "strange rock" not in inventory:
            print("There are banners adorning the walls of this part of the cave, and there is a large stone table at the center. On top of the table is a small, purple box that appears to be locked. The lock itself is strange, there being an indent of a rough shape where the keyhole should be.")
            get_command()
        elif action == "ex" and "strange rock" in inventory:
            print("There are banners adorning the walls of this part of the cave, and there is a large stone table at the center. On top of the table is a small, purple box that appears to be locked. The lock itself is strange, there being an indent of a rough shape where the keyhole should be.")
            print("Noting the strange keyhole, you decide to put the purple rock into the indentation.")
            print("...")
            print("...")
            print("Click.")
            print("The box opens and inside was a small sheet of paper.")
            print("GOT PAPER")
            inventory.append("paper")
            inventory.remove("strange rock")
            get_command()
        elif action == "inv":
            show_inventory(inventory)
        elif action == "hb":
            move_player("westmost", "hb")
    pass

def move_player(current_location, direction):
    """
    Move the player in the given direction.
    Return the new location, or current location if can't move that way.
    """
    global current_room
    if current_location == "start" and direction == "hn":
        current_room = "center"
        display_location(current_room)
    elif current_location == "center" and direction == "hn":
        current_room = "northmost"
        display_location(current_room)
    elif current_location == "center" and direction == "he":
        current_room = "eastmost"
        display_location(current_room)
    elif current_location == "center" and direction == "hs":
        current_room = "start"
        display_location(current_room)
    elif current_location == "center" and direction == "hw":
        current_room = "westmost"
        display_location(current_room)
    elif current_location == "northmost" and direction == "hb":
        current_room = "center"
        display_location(current_room)
    elif current_location == "eastmost" and direction == "hb":
        current_room = "center"
        display_location(current_room)
    elif current_location == "westmost" and direction == "hb":
        current_room = "center"
        display_location(current_room)
    pass

def show_inventory(items):
    """Display the player's inventory."""
    print("Inventory:")
    for item in inventory:
        print(f" {item} ||", end="")
    print(" ")
    print("Type the name of the object you want to look at or type ex to exit")
    invChoice = str(input(" "))
    if invChoice == "ex":
        get_command()
    elif invChoice == "map" and "map" in inventory:
        print("-------------------------------------------------------------")
        print("|                        --------                           |")
        print("|                       |        |                 N        |")
        print("|                       |        |              W  +  E     |")
        print("|                       --      --                 S        |")
        print("|                        |      |                           |")
        print("|                        |      |                           |")
        print("|                 --------       ---------                  |")
        print("|         _______|                        |_________        |")
        print("|        |                                          |       |")
        print("|        |                                          |       |")
        print("|        | --------                        ----------       |")
        print("|                 |------        --------|                  |")
        print("|                       |        |                          |")
        print("|                       |        |                          |")
        print("|                       |        |                          |")
        print("|                       ----------                          |")
        print("-------------------------------------------------------------")
        show_inventory(inventory)
    elif invChoice == "strange rock" and "strange rock" in inventory:
        print("-------------------------------------------------------------")
        print("|                                                           |")
        print("|                        -----------                        |")
        print("|                      /            \                       |")
        print("|                      \             \                      |")
        print("|                       |            |                      |")
        print("|                        \           |                      |")
        print("|                         \__________/                      |")
        print("|                                                           |")
        print("|                                                           |")
        print("-------------------------------------------------------------")
        print("A strange rock. It has a muted purple color.")
        show_inventory(inventory)
    elif invChoice == "paper" and "paper" in inventory:
        print("-------------------------------------------------------------")
        print("|                                                           |")
        print("|                                                           |")
        print("|                ---------------                            |")
        print("|               |                \                          |")
        print("|               |      |          |                         |")
        print("|               |      |___       |                         |") 
        print("|               |      |   \      |                         |")
        print("|               |       \__/      |                         |") 
        print("|               |                 |                         |")
        print("|               |                 |                         |")
        print("|               \                 |                         |")
        print("|                ----------------/                          |")
        print("|                                                           |")
        print("|                                                           |")
        print("|                                                           |")
        print("|                                                           |")
        print("-------------------------------------------------------------")
        print("A small piece of paper. It looks like it has the letter 6 on it.")
        show_inventory(inventory)
    elif invChoice == "Warhammer Of Zillyhoo" and "Warhammer Of Zillyhoo" in inventory:
        print("------------------------------------------------------------------------")
        print("|                                                                      |")
        print("|                                                                      |")
        print("|            /\                                                        |")
        print("|       ____/  \_____                                                  |")
        print("|       \           /                                                  |")
        print("|        \___     _/           |                                       |")
        print("|           | /\ |            / \                                      |")
        print("|           |/  \|           /   \                                     |")
        print("|           / / /           |     |                    ________        |")
        print("|           | | |           /     \                   /        \       |")
        print("|           \ \ \          |       |                 /          \      |")
        print("|           _\_\_\________/_________\_              /            \     |")
        print("|          /            |             |------|____ /              \    |")
        print("|         /   ___________|     -----|  |      |    |               |   |")
        print("|        /\  /            |        /     |     |    |              |   |")
        print("|      _/__\/    __________|      /        |    |____|             |   |")
        print("|    /      \   /           |    /____      |----|    \            |   |")
        print("|   / .    . \ /             |_____    ______|         \           |   |")
        print("|  |  _____  |                    \   \                 \         /    |")
        print("|  \  \___/ /                      \   \                 \_______/     |")
        print("|   \_____/                         \   \                              |")
        print("|                                    \   \                             |")
        print("|                                    _\   \_                           |")
        print("|                                    \      \                          |")
        print("|                                     \      \                         |")
        print("|                                      \      \                        |")
        print("|                                       \      \                       |")
        print("|                                        \      \                      |")
        print("|                                         \      \                     |")
        print("|                                          \     /                     |")
        print("|                                           \___/                      |")
        print("|                                                                      |")
        print("------------------------------------------------------------------------")
        print("Wow original design. Experts say this is 100% not a Homestuck Reference. You can feel your fingers cramping looking at the ASCII art. I mean the artisan ship.")
        show_inventory(inventory)
    pass

def check_win_condition(items):
    """Check if player has won. Return True or False."""
    if items == True:
        print("YOU WIN!")
    pass

# Main program
current_room = "start"
inventory = []
playing = True
display_title()

# YOUR CODE HERE - Write the main game loop
# Use the functions above to create the complete program