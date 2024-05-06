"""V2 of the welcome screen and options screen component
Converts V1 to a function and converts all print statements to easygui boxes.
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
        easygui.msgbox("Thanks for using this program", "Goodbye")
        # If selected this stops the program
        exit()


# Main routine
main()
