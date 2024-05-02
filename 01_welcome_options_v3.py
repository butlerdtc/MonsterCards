"""V3 of the welcome screen and options screen component
Converts V2 to a function and converts all print statements to easygui boxes.
This version also removes all the loops as easygui removes the need for them.
Created by Robson Butler - 02/05/24
"""
import easygui


# Function to user choose what option they would like to execute
def main():
    # Welcome message
    easygui.msgbox("Welcome to the Monster card catalogue!", "Welcome")

    instructions = ("This is a catalogue for monster cards. In the next "
                    "screen you will have a few options.\n\n - You can add a "
                    "new card to the catalogue\n - You can search for a card "
                    "in the catalogue and then edit its details\n - You can "
                    "delete a card from the catalogue\n - You can print all "
                    "the cards in the catalogue\n - You can update existing "
                    "card information in the catalogue\n\nHave fun exploring "
                    "the catalogue and managing your monster cards!")

    # Asks if user needs the instructions
    show_instructions = easygui.buttonbox("Would you like to see the "
                                          "instructions?",
                                          "View instructions?",
                                          ["Yes", "No"])
    if show_instructions == "Yes":
        easygui.msgbox(instructions, "Instructions")
    # Asks user to choose an option
    choice = easygui.buttonbox("What would you like to do?", "Options",
                               ["Add card", "Search card", "Delete card",
                                "Show cards", "Exit"])
    # All the message boxes will get replaced with the components eventually
    if choice == "Add card":
        easygui.msgbox(choice, choice)
    elif choice == "Search card":
        easygui.msgbox(choice, choice)
    elif choice == "Delete card":
        easygui.msgbox(choice, choice)
    elif choice == "Show cards":
        easygui.msgbox(choice, choice)
    else:
        # If user selects 'Exit' this stops the program
        exit()


# Main routine
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
main()
