"""V2 of the welcome screen and options screen component
Adds instructions and options screen to V1.
Created by Robson Butler - 02/05/24
"""

# Dictionary to store the original cards
card_catalogue = {"Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25,
                                "Cunning": 15},
                  "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21,
                                "Cunning": 19},
                  "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18,
                                 "Cunning": 22},
                  "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23,
                                 "Cunning": 6},
                  "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10,
                               "Cunning": 5},
                  "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14,
                               "Cunning": 5},
                  "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19,
                                 "Cunning": 2},
                  "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4,
                               "Cunning": 12},
                  "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17,
                                "Cunning": 4},
                  "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3,
                                "Cunning": 2}
                  }

# Welcome message
print("Welcome to the Monster card catalogue!")
instructions = ("\nThis is a catalogue for monster cards. In the next screen "
                "you will have a few options.\nYou can add a new card "
                "to the catalogue\nYou can search for a card in the catalogue"
                "\nYou can delete a card from the catalogue\nYou can print all"
                " the cards in the catalogue\nYou can update existing card "
                "information in the catalogue\nHave fun exploring the "
                "catalogue and managing your monster cards!")
# Loops until user enters valid input (Yes or No)
while True:
    show_instructions = (input("Would you like to see the instructions(Yes/No)"
                               ": ").title())
    # Will accept 'Y' as valid input then shows the instructions
    if show_instructions == "Yes" or show_instructions == "Y":
        print(instructions)
        break
    # Will accept 'N' as valid input then continues program
    elif show_instructions == "No" or show_instructions == "N":
        print("Continue")
        break
    else:
        print("Please enter a valid option")
# Loops until user chooses and enters a valid option (Options screen)
while True:
    choice = input("Your options: 'Add card' 'Search card' 'Delete card' "
                   "'Show cards' 'Exit'\nWhat would you like to do? ").title()

    if choice == "Add Card":
        print(choice)
        break
    elif choice == "Search Card":
        print(choice)
        break
    elif choice == "Delete Card":
        print(choice)
        break
    elif choice == "Show Cards":
        print(choice)
        break
    elif choice == "Exit":
        print(choice)
        break
    else:
        print("Please choose a valid option")
