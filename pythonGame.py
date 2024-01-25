import random

def Start():
    # inventory = ["Axe", "Key", "Wire Cutters"]
    inventory = [] # This list stores all of the items in the inventory
    control_panel = False # Control Panel is set to deactivated
    north_room_zombie = False # Zombie in the North Room is set to alive
    west_corridor_zombie = False # Zombie in the West Corridor is set to alive
    reception_zombie = False # Zombie in the Reception is set to alive
    utility_zombie = False # Zombie in Utility Room is set to alive
    player_health = 400 # Player Health is set to 400

    # Welcome Text

    print("\n"
          "                  |-Welcome to ESCAPE.1!-|                   \n"
          "                  ------------------------                   \n"
          "    |-You wake up in a laboratory bed during a lockdown-|    \n"
          " |-All of the scientists have been infected by the Z-virus-| \n"
          " \n"
          "                              -                              ")

    # User Guide
    
    print("""
You must navigate the compound, acquire items,
interact with machines and kill the zombies!

USER GUIDE:
- Use the choice menu by typing in the corresponding numbers
for the options on the menu to perform various actions.
- Defeat zombies by using a turn based combat system,
where the attack moves are selected by pressing 1 and 2.
- There are 2 ways of escaping, you will need to activate machinery,
kill zombies and acquire items to escape.
- Recover your health by going to the Laboratory and using the Healing Device.
- Arm yourself with a Fire Axe to kill the Zombies.
""")

    # Text Logo for the Game

    print("|----------------------------------------------------------|")
    print("|----------------------------------------------------------|")
    print("|-------------------------ESCAPE.1-------------------------|")
    print("|----------------------------------------------------------|")

    Laboratory(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie, utility_zombie,
               player_health)# Calls the Laboratory function


def Laboratory(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie, utility_zombie,
               player_health):
    print("|----------------------------------------------------------|")
    print("Location: LABORATORY" + "        Health: " + str(player_health)) # Displays Location and Player Health
    print("--------------------")
    print("You are in what looks like a laboratory!") # Location description
    print("There is a single door.")
    print("What do you do?")

    choice = input("1.Try the door| 2.Use Healing Device| 3.Check inventory : ") # Shows choices and asks for input on what the player wants to do

    if choice == "1": # If player chose choice 1 (Go to Corridor hub)
        CorridorHub(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie, utility_zombie,
                    player_health)# Calls the CorridorHub function
    elif choice == "2": # If player chose choice 2 (Use Healing Device)
        player_health = 400 # Player Health is set to 400
        print("-")
        print("The Device heals you to Full Health")
        Laboratory(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                   utility_zombie, player_health)# Calls the Laboratory function
    elif choice == "3": # If player chose choice 3 (Check Inventory)
        if len(inventory) == 0: # If there are no items in the inventory
            print("|----------------|")
            print("Inventory is Empty")
            Laboratory(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                       utility_zombie, player_health)# Calls the Laboratory function
        elif len(inventory) != 0: # If there is atleast one item in the inventory
            print("INVENTORY:")
            for item in inventory: # For every item in the inventory list, print out the item
                print("|-------|")
                print(item)
            else:
                print("|-------|")
            Laboratory(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                       utility_zombie, player_health)# Calls the Laboratory function

    else: # If the player has made an invalid choice
        print("|----------------------------------------------------------|")
        print("You made an invalid choice.")
        Laboratory(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie, utility_zombie,
                   player_health)# Calls the Laboratory function


def CorridorHub(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                utility_zombie, player_health):
    print("|----------------------------------------------------------|")
    print("Location: CORRIDOR HUB" + "        Health: " + str(player_health)) # Displays Location and Player Health
    print("You can see 3 doors leading to different corridors and a door to the laboratory.") # Location description

    if "Axe" in inventory: # If the Axe is in the players inventory
        choice = input("1.Laboratory| 2.North Corridor| 3.West Corridor| 4.South Corridor| 5.Check Inventory :")# Shows choices and asks for input on what the player wants to do

        if choice == "1": # If player chose choice 1 (Go to Laboratory)
            Laboratory(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                       utility_zombie, player_health)# Calls the Laboratory function
        elif choice == "2": # If player chose choice 2 (Go to North Corridor)
            NorthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)# Calls the North Corridor function
        elif choice == "3": # If player chose choice 3 (Go to West Corridor)
            WestCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                         utility_zombie, player_health)# Calls the West Corridor function
        elif choice == "4": # If player chose choice 4 (Go to South Corridor)
            SouthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)# Calls the South Corridor function
        elif choice == "5": # If player chose choice 5 (Check Inventory)
            if len(inventory) == 0: # If there are no items in the inventory
                print("|----------------|")
                print("Inventory is Empty")
                CorridorHub(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)# Calls the CorridorHub function
            elif len(inventory) != 0: # If there is atleast one item in the inventory
                print("INVENTORY:")
                for item in inventory: # For every item in the inventory list, print out the item
                    print("|-------|")
                    print(item)
                else:
                    print("|-------|")
                CorridorHub(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)# Calls the CorridorHub function
        else: # If the player has made an invalid choice
            print("|----------------------------------------------------------|")
            print("You made an invalid choice.")
            CorridorHub(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                        utility_zombie, player_health)# Calls the CorridorHub function

    elif "Axe" not in inventory: # If the Axe is not in the players inventory
        print("You see a Fire Axe Box on the wall. What do you do?")

        choice = input("1.Search the Fire Axe Box| 2.Laboratory| 3.North Corridor| 4.West Corridor| 5.South Corridor|"
                       "6.Check Inventory:")# Shows choices and asks for input on what the player wants to do

        if choice == "1": # If player chose choice 1 (Search Fire Axe Box)
            print("|----------------------------------------------------------|")
            print("Fire Axe added to inventory.")
            inventory.append("Axe") # "Axe" is added to inventory
            CorridorHub(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                        utility_zombie, player_health)# Calls the CorridorHub function
        elif choice == "2": # If player chose choice 2 (Go to Laboratory)
            Laboratory(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                       utility_zombie, player_health)# Calls the Laboratory function
        elif choice == "3": # If player chose choice 3 (Go to North Corridor)
            NorthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)# Calls the NorthCorridor function
        elif choice == "4": # If player chose choice 4 (Go to West Corridor)
            WestCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                         utility_zombie, player_health)# Calls the WestCorridor function
        elif choice == "5": # If player chose choice 5 (Go to South Corridor)
            SouthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)# Calls the SouthCorridor function
        elif choice == "6": # If player chose choice 6 (Check Inventory)
            if len(inventory) == 0: # If there are no items in the inventory
                print("|----------------|")
                print("Inventory is Empty")
                CorridorHub(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)# Calls the CorridorHub function
            elif len(inventory) != 0: # If there is atleast one item in the inventory
                print("INVENTORY:")
                for item in inventory: # For every item in the inventory list, print out the item
                    print("|-------|")
                    print(item)
                else:
                    print("|-------|")
                CorridorHub(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)# Calls the CorridorHub function
        else: # If the player has made an invalid choice
            print("|----------------------------------------------------------|")
            print("You made an invalid choice.")
            CorridorHub(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                        utility_zombie, player_health)# Calls the CorridorHub function


def NorthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                  utility_zombie, player_health):
    print("|----------------------------------------------------------|")
    print("Location: NORTH CORRIDOR" + "        Health: " + str(player_health))
    print("The corridor leads to the northern room. You can also head back to the corridor hub. What do you do?")

    choice = input("1.Enter North Room| 2.Head back to Corridor Hub| 3.Check Inventory : ")

    if choice == "1":
        NorthRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie, utility_zombie,
                  player_health)
    elif choice == "2":
        CorridorHub(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie, utility_zombie,
                    player_health)
    elif choice == "3":
        if len(inventory) == 0:
            print("|----------------|")
            print("Inventory is Empty")
            NorthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)
        elif len(inventory) != 0:
            print("INVENTORY:")
            for item in inventory:
                print("|-------|")
                print(item)
            else:
                print("|-------|")
            NorthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)
    else:
        print("|----------------------------------------------------------|")
        print("You made an invalid choice.")
        NorthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                      utility_zombie, player_health)


def NorthRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
              utility_zombie, player_health):  # add zombie to this room + combat
    print("|----------------------------------------------------------|")
    print("Location: NORTH ROOM" + "        Health: " + str(player_health))

    if north_room_zombie == False:
        print("As you enter the North Room a zombie attacks you!")  # --------------------- ZOMBIE
        if "Axe" in inventory:
            room_history = "NorthRoom"
            Combat(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                   utility_zombie, room_history, player_health)
        else:
            print("You do not have a weapon to defend yourself with and are DEFENCELESS ")
            print("RIP you DIED! You were killed by the Zombie!")
            print("-")
            restart_game = input("Play again? 1. YES 2.NO :")

            if restart_game == "1":
                Start()
            elif restart_game == "2":
                exit()

    elif north_room_zombie == True:
        print("|----------------------------------------------------------|")
        print("The room is empty with a rotting dead zombie inside, you don't want to stay there.")
        print("You leave.")
        NorthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                      utility_zombie, player_health)


def WestCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                 utility_zombie, player_health):  # add zombie to this room + combat
    print("|----------------------------------------------------------|")
    print("Location: WEST CORRIDOR" + "        Health: " + str(player_health))

    if west_corridor_zombie == False:
        print("As you enter the West Corridor a zombie attacks you!")  # --------------------- ZOMBIE
        if "Axe" in inventory:
            room_history = "WestCorridor"
            Combat(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                   utility_zombie, room_history, player_health)
        else:
            print("You do not have a weapon to defend yourself with and are DEFENCELESS ")
            print("RIP you DIED! You were killed by the Zombie!")
            print("-")
            restart_game = input("Play again? 1. YES 2.NO :")

            if restart_game == "1":
                Start()
            elif restart_game == "2":
                exit()
    elif west_corridor_zombie == True:
        print(
            "You notice a door to the Reception along with the door back to the Corridor Hub. What do you do?")

        choice = input("1.Enter the Reception| 2.Head back to Corridor Hub| 3. Check Inventory : ")

        if choice == "1":
            Reception(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                      utility_zombie, player_health)
        elif choice == "2":
            CorridorHub(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                        utility_zombie, player_health)
        elif choice == "3":
            if len(inventory) == 0:
                print("|----------------|")
                print("Inventory is Empty")
                WestCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                             utility_zombie, player_health)
            elif len(inventory) != 0:
                print("INVENTORY:")
                for item in inventory:
                    print("|-------|")
                    print(item)
                else:
                    print("|-------|")
                WestCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                             utility_zombie, player_health)
        else:
            print("You made an invalid choice.")
            WestCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                         utility_zombie, player_health)


def Reception(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
              utility_zombie, player_health):  # add zombie to this room + combat
    print("|----------------------------------------------------------|")
    print("Location: RECEPTION" + "        Health: " + str(player_health))

    if reception_zombie == False:
        print("As you enter the Reception a zombie attacks you!")  # --------------------- ZOMBIE
        if "Axe" in inventory:
            room_history = "Reception"
            Combat(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                   utility_zombie, room_history, player_health)
        else:
            print("You do not have a weapon to defend yourself with and are DEFENCELESS ")
            print("RIP you DIED! You were killed by the Zombie!")
            print("-")
            restart_game = input("Play again? 1. YES 2.NO :")

            if restart_game == "1":
                Start()
            elif restart_game == "2":
                exit()
    elif reception_zombie == True:
        print("You notice the Building Entrance door along with the door back to the West Corridor. What do you do?")

        choice = input("1.Open the Building Entrance door| 2.Head back to the West Corridor| 3.Check Inventory : ")

        if control_panel == True:
            if choice == "1":
                print("|----------------------------------------------------------|")
                print("YOU SUCCESSFULLY ESCAPE!")
                print("-")
                restart_game = input("Play again? 1. YES 2.NO :")

                if restart_game == "1":
                    Start()
                elif restart_game == "2":
                    exit()
            elif choice == "2":
                WestCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                             utility_zombie, player_health)
            elif choice == "3":
                if len(inventory) == 0:
                    print("|----------------|")
                    print("Inventory is Empty")
                    Reception(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                              utility_zombie, player_health)
                elif len(inventory) != 0:
                    print("INVENTORY:")
                    for item in inventory:
                        print("|-------|")
                        print(item)
                    else:
                        print("|-------|")
                    Reception(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                              utility_zombie, player_health)
            else:
                print("|----------------------------------------------------------|")
                print("You made an invalid choice.")
                Reception(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)
        elif control_panel == False:
            if choice == "1":
                print("|----------------------------------------------------------|")
                print("You can't open the door. It seems you need to activate a control panel in order for it to open.")
                Reception(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)
            elif choice == "2":
                WestCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                             utility_zombie, player_health)
            elif choice == "3":
                if len(inventory) == 0:
                    print("|----------------|")
                    print("Inventory is Empty")
                    Reception(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                              utility_zombie, player_health)
                elif len(inventory) != 0:
                    print("INVENTORY:")
                    for item in inventory:
                        print("|-------|")
                        print(item)
                    else:
                        print("|-------|")
                    Reception(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                              utility_zombie, player_health)
            else:
                print("|----------------------------------------------------------|")
                print("You made an invalid choice.")
                Reception(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)


def SouthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie, utility_zombie,
                  player_health):
    print("|----------------------------------------------------------|")
    print("Location: SOUTH CORRIDOR" + "        Health: " + str(player_health))
    print("The corridor leads to the Control Room. You can also head back to the corridor hub. What do you do?")

    choice = input("1.Enter the Control Room| 2.Head back to Corridor Hub| 3.Check Inventory : ")

    if choice == "1":
        ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie, utility_zombie,
                    player_health)
    elif choice == "2":
        CorridorHub(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie, utility_zombie,
                    player_health)
    elif choice == "3":
        if len(inventory) == 0:
            print("|----------------|")
            print("Inventory is Empty")
            SouthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)
        elif len(inventory) != 0:
            print("INVENTORY:")
            for item in inventory:
                print("|-------|")
                print(item)
            else:
                print("|-------|")
            SouthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)
    else:
        print("You made an invalid choice.")
        SouthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                      utility_zombie, player_health)


def ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie, utility_zombie,
                player_health):
    print("|----------------------------------------------------------|")
    print("Location: CONTROL ROOM" + "        Health: " + str(player_health))
    print("The Control Room contains a control panel along with a number of doors. What do you do?")

    if control_panel == False:
        choice = input("1.Activate the Control Panel| 2.Open door to the outdoors| 3.Open Utility Room door| "
                       "4.Go to South Corridor| 5.Check Inventory : ")

        if choice == "1":
            print("|----------------------------------------------------------|")
            print("-CONTROL PANEL ACTIVATED-")
            control_panel = True
            ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                        utility_zombie, player_health)
        elif choice == "2":

            if "Key" not in inventory:
                print("|----------------------------------------------------------|")
                print("The door is locked and needs a key. You decide to do something else.")
                ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)
            elif "Key" in inventory:
                print("|----------------------------------------------------------|")
                print("You use the Key to open the door!")
                Outdoors(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                         utility_zombie, player_health)

        elif choice == "3":
            UtilityRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                        utility_zombie, player_health)
        elif choice == "4":
            SouthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)
        elif choice == "5":
            if len(inventory) == 0:
                print("|----------------|")
                print("Inventory is Empty")
                ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)
            elif len(inventory) != 0:
                print("INVENTORY:")
                for item in inventory:
                    print("|-------|")
                    print(item)
                else:
                    print("|-------|")
                ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)
        else:
            print("|----------------------------------------------------------|")
            print("You made an invalid choice.")
            ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                        utility_zombie, player_health)

    elif control_panel == True:
        choice = input(
            "1.Deactivate the Control Panel| 2.Open door to the outdoors| 3.Open Utility Room door| "
            "4.Go to South Corridor| 5. Check Inventory : ")

        if choice == "1":
            print("|----------------------------------------------------------|")
            print("-CONTROL PANEL DEACTIVATED-")
            control_panel = False
            ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                        utility_zombie, player_health)
        elif choice == "2":

            if "Key" not in inventory:
                print("|----------------------------------------------------------|")
                print("The door is locked and needs a key. You decide to do something else.")
                ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)
            elif "Key" in inventory:
                print("|----------------------------------------------------------|")
                print("You use the Key to open the door!")
                Outdoors(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                         utility_zombie, player_health)

        elif choice == "3":
            UtilityRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                        utility_zombie, player_health)
        elif choice == "4":
            SouthCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)
        elif choice == "5":
            if len(inventory) == 0:
                print("|----------------|")
                print("Inventory is Empty")
                ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)
            elif len(inventory) != 0:
                print("INVENTORY:")
                for item in inventory:
                    print("|-------|")
                    print(item)
                else:
                    print("|-------|")
                ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)
        else:
            print("You made an invalid choice.")
            ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                        utility_zombie, player_health)


def Outdoors(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie, utility_zombie,
             player_health):
    print("|----------------------------------------------------------|")
    print("Location: OUTDOORS" + "        Health: " + str(player_health))
    print("There is a large fence seperating you from freedom. What do you do?")

    if "Wire Cutters" not in inventory:
        choice = input("1.Inspect the area| 2.Go back indoors| 3. Check Inventory : ")

        if choice == "1":
            print("|----------------------------------------------------------|")
            print("It looks like if I got some Wire Cutters I could cut a hole in the fence and escape!")
            Outdoors(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                     utility_zombie, player_health)
        elif choice == "2":
            ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                        utility_zombie, player_health)
        elif choice == "3":
            if len(inventory) == 0:
                print("|----------------|")
                print("Inventory is Empty")
                Outdoors(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                         utility_zombie, player_health)
            elif len(inventory) != 0:
                print("INVENTORY:")
                for item in inventory:
                    print("|-------|")
                    print(item)
                else:
                    print("|-------|")
                Outdoors(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                         utility_zombie, player_health)
        else:
            print("|----------------------------------------------------------|")
            print("You made an invalid choice.")
            Outdoors(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                     utility_zombie, player_health)

    elif "Wire Cutters" in inventory:
        choice = input("1.Cut a hole in the fence| 2.Go back indoors| 3.Check Inventory : ")

        if choice == "1":
            print("|----------------------------------------------------------|")
            print("YOU SUCCESSFULLY ESCAPE!")
            print("-")
            restart_game = input("Play again? 1. YES 2.NO :")

            if restart_game == "1":
                Start()
            elif restart_game == "2":
                exit()

        elif choice == "2":
            ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                        utility_zombie, player_health)
        elif choice == "3":
            if len(inventory) == 0:
                print("|----------------|")
                print("Inventory is Empty")
                Outdoors(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                         utility_zombie, player_health)
            elif len(inventory) != 0:
                print("INVENTORY:")
                for item in inventory:
                    print("|-------|")
                    print(item)
                else:
                    print("|-------|")
                Outdoors(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                         utility_zombie, player_health)
        else:
            print("|----------------------------------------------------------|")
            print("You made an invalid choice.")
            Outdoors(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                     utility_zombie, player_health)


def UtilityRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                utility_zombie, player_health):  # add zombie to this room + combat
    print("|----------------------------------------------------------|")
    print("Location: UTILITY ROOM" + "        Health: " + str(player_health))

    if utility_zombie == False:
        print("As you enter the Utility Room a zombie attacks you!")  # --------------------- ZOMBIE
        if "Axe" in inventory:
            room_history = "Utility"
            Combat(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                   utility_zombie, room_history, player_health)
        else:
            print("You do not have a weapon to defend yourself with and are DEFENCELESS ")
            print("RIP you DIED! You were killed by the Zombie!")
            print("-")
            restart_game = input("Play again? 1. YES 2.NO :")

            if restart_game == "1":
                Start()
            elif restart_game == "2":
                exit()
    elif utility_zombie == True:

        if "Wire Cutters" not in inventory:
            print(
                "You notice some Wire Cutters on the floor and the door back to the Control Room. What do you do?")

            choice = input("1.Pick up the Wire Cutters| 2.Go back to the Control Room| 3.Check Inventory : ")

            if choice == "1":
                print("|----------------------------------------------------------|")
                print("Wire Cutters added to inventory!")
                inventory.append("Wire Cutters")
                UtilityRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)
            elif choice == "2":
                ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)
            elif choice == "3":
                if len(inventory) == 0:
                    print("|----------------|")
                    print("Inventory is Empty")
                    UtilityRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                                utility_zombie, player_health)
                elif len(inventory) != 0:
                    print("INVENTORY:")
                    for item in inventory:
                        print("|-------|")
                        print(item)
                    else:
                        print("|-------|")
                    UtilityRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                                utility_zombie, player_health)
            else:
                print("You made an invalid choice.")
                UtilityRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)

        elif "Wire Cutters" in inventory:
            print("The room is empty with a rotting dead zombie inside, you don't want to stay there.")
            print("You leave.")
            ControlRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                        utility_zombie, player_health)

    #########################################################################################################


def Combat(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie, utility_zombie,
           room_history, player_health):

    print("|---------------------------------------------------------------|")
    print("You are now Battling the Zombie. Use your Fire Axe and defeat it!")

    play_again = True

    # Set up the play again loop
    while play_again:
        winner = None

        computer_health = 100

        # determine whose turn it is
        turn = random.randint(1, 2)  # heads or tails
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("Player attacks first!")
        else:
            player_turn = False
            computer_turn = True
            print("Zombie attacks first!")

        print("\nPlayer health: ", player_health, "Zombie health: ", computer_health)

        # set up the main game loop
        while (player_health != 0 or computer_health != 0):

            heal_up = False  # determine if heal has been used by the player. Resets false each loop.
            miss = False  # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected
            moves = {"Attack": random.randint(18, 25),
                     "Heavy Attack": random.randint(10, 35)}

            if player_turn:
                print(
                    "\nPlease select a move:\n1. Attack (DMG 18-25)\n2. Heavy Attack (DMG 10-35)")

                player_move = input("> ").lower()

                move_miss = random.randint(1, 5)  # 20% of missing
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    player_move = 0  # player misses and deals no damage
                    print("You missed!")
                else:
                    if player_move in ("1", "Attack"):
                        player_move = moves["Attack"]
                        print("\nYou used Attack. It dealt ", player_move, " damage.")
                    elif player_move in ("2", "Heavy Attack"):
                        player_move = moves["Heavy Attack"]
                        print("\nYou used Heavy Attack. It dealt ", player_move, " damage.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else:  # computer turn

                move_miss = random.randint(1, 5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    computer_move = 0  # the computer misses and deals no damage
                    print("The Zombie missed!")
                else:
                    if computer_health > 30:
                        if player_health > 75:
                            computer_move = moves["Attack"]
                            print("\nThe Zombie used Attack. It dealt ", computer_move, " damage.")
                        elif player_health > 35 and player_health <= 75:  # computer decides whether to go big or play it safe
                            imoves = ["Attack", "Heavy Attack"]
                            imoves = random.choice(imoves)
                            computer_move = moves[imoves]
                            print("\nThe Zombie used ", imoves, ". It dealt ", computer_move, " damage.")
                        elif player_health <= 35:
                            computer_move = moves["Heavy Attack"]  # FINISH HIM!
                            print("\nThe Zombie used Heavy Attack. It dealt ", computer_move, " damage.")
                    else:
                        if player_health > 75:
                            computer_move = moves["Attack"]
                            print("\nThe Zombie used Attack. It dealt ", computer_move, " damage.")
                        elif player_health > 35 and player_health <= 75:
                            imoves = ["Attack", "Heavy Attack"]
                            imoves = random.choice(imoves)
                            computer_move = moves[imoves]
                            print("\nThe Zombie used ", imoves, ". It dealt ", computer_move, " damage.")
                        elif player_health <= 35:
                            computer_move = moves["Heavy Attack"]  # FINISH HIM!
                            print("\nThe Zombie used Heavy Attack. It dealt ", computer_move, " damage.")

            if player_turn:
                computer_health -= player_move
                if computer_health < 0:
                    computer_health = 0  # cap minimum health at 0
                    winner = "Player"
                    break
            else:
                player_health -= computer_move
                if player_health < 0:
                    player_health = 0
                    winner = "Computer"
                    break

            print("\nPlayer health: ", player_health, "Zombie health: ", computer_health)

            # switch turns
            player_turn = not player_turn
            computer_turn = not computer_turn

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("\nPlayer health: ", player_health, "Zombie health: ", computer_health)
            print("-")
            print("\nCongratulations! You are alive...... For now!")
            print("-")
            print("\nExiting Combat")

            if room_history == "NorthRoom":
                north_room_zombie = True
                if "Key" not in inventory:
                    print("|----------------------------------------------------------|")
                    print("Now that you have taken care of the zombie, you search the room.")
                    print("|----------------------------------------------------------|")
                    print("You find a BLUE KEY!")
                    inventory.append("Key")
                    NorthRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                              utility_zombie, player_health)
            elif room_history == "WestCorridor":
                west_corridor_zombie = True
                WestCorridor(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                             utility_zombie, player_health)
            elif room_history == "Reception":
                reception_zombie = True
                Reception(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                          utility_zombie, player_health)
            elif room_history == "Utility":
                utility_zombie = True
                UtilityRoom(inventory, control_panel, north_room_zombie, west_corridor_zombie, reception_zombie,
                            utility_zombie, player_health)
        else:
            print("Player health: ", player_health, "Zombie health: ", computer_health)
            print("-")
            print("RIP you DIED! You were killed by the Zombie!")
            print("-")
            restart_game = input("Play again? 1. YES 2.NO :")

            if restart_game == "1":
                Start()
            elif restart_game == "2":
                exit()


Start()
