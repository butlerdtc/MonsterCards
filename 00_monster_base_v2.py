"""Monster cards  base component V2
Each component gets added after creation and testing. Added while loop to main
component that should have been there originally. Functions added from
components 3 and 4.
Created by Robson Butler - 19/05/24
"""
import easygui


# Function to user choose what option they would like to execute
def main(catalogue, stat_list):
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
    while True:
        # Asks user to choose an option
        choice = easygui.buttonbox("What would you like to do?", "Options",
                                   ["Add card", "Search card", "Delete card",
                                    "Show cards", "Exit"])
        # Added 'Add card' component, rest added eventually
        if choice == "Add card":
            new_card_dict = add_card(catalogue, stat_list)
            formatted_new_card = card_formatter_list(new_card_dict)
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


# Function to check if dictionary or any stat in dictionary is empty
def dict_none_checker(dictionary, number_pairs):
    # Check if the dictionary is empty if so return none
    if not dictionary:
        return None

    # Iterates through each pair in the dictionary
    for key, value in dictionary.items():
        # Checks if the key is not None and not empty, if it is returns none
        if key is None or not key:
            return None

        # Checks if the number of pairs in the dictionary matches the number of
        # stats. This prevents the function returning half a dictionary.
        if len(value) != number_pairs:
            return None

    # If all keys have the expected number of pairs and the key is not none
    # return the initial dictionary
    return dictionary


# Function to allow user to add a new card
def add_card(catalogue, values):
    number_stats = len(values)
    while True:
        # Dictionary to store entered data until its confirmed and added
        temporary_dict = {}
        # Marks if user cancels the program
        cancel_marker = False
        # Asks for new card name
        new_card_name = easygui.enterbox("Please enter name of the new card",
                                         "New name")
        # This checks if the user selected cancel or entered a name
        if new_card_name is not None:
            # Converts user input to have a capital letter
            new_name = new_card_name.title()
            # Checks if card name is already in the catalogue then prints error
            if new_name in catalogue:
                easygui.msgbox("This card is already in the catalogue\nPlease"
                               " enter a new name", "Error")
                continue
            else:
                # Adds new card name to temporary dictionary
                temporary_dict[new_name] = {}
                # Iterates through each stat from the list to get new values
                for stat in values:
                    while True:
                        stat_value = easygui.integerbox(f"Enter {new_name}'s "
                                                        f"{stat} value",
                                                        f"{stat} value",
                                                        upperbound=10000000,
                                                        lowerbound=-10000000)
                        # If user selects cancel runs confirmation check
                        if stat_value is None:
                            # This asks to confirm cancelling the card
                            confirm_stat = easygui.buttonbox("Are you sure"
                                                             " you want to "
                                                             "cancel adding a "
                                                             "card",
                                                             "Confirm "
                                                             "cancellation",
                                                             ["Yes", "No"])
                            if confirm_stat == "No":
                                continue
                            else:
                                cancel_marker = True
                                break

                        # If input within correct range adds value to stat(key)
                        if 1 <= stat_value <= 25:
                            temporary_dict[new_name][stat] = stat_value
                            break
                        # If cancel not selected and input not valid prints
                        # error
                        else:
                            easygui.msgbox("Please enter a value between 1"
                                           " and 25", "Error")
        # Breaks loop if user cancels (same for all break's below)
                    if cancel_marker:
                        break
                if cancel_marker:
                    break

                break
        else:
            # This asks to confirm cancelling the card
            confirm_name = easygui.buttonbox("Are you sure you want to "
                                             "cancel adding a card",
                                             "Confirm cancellation",
                                             ["Yes", "No"])
            if confirm_name == "No":
                continue
            else:
                break

    # Runs value checker to ensure all stats have values and weren't cancelled
    checked_dictionary = dict_none_checker(temporary_dict, number_stats)
    return checked_dictionary


# Function to format dictionaries into a list style design
def card_formatter_list(cards):
    # If dictionary is none from other components returns none or else formats
    if cards is None:
        return None
    else:
        # Temporary list to store each formatted dictionary item
        temporary_list = []
        # Iterates through each card in catalogue
        for card, items in cards.items():
            temporary_list.append(f"{card}:")
            # Sorts through each stat and value for each card
            for item, stat in items.items():
                temporary_list.append(f" - " + f"{item}: {stat}")
            # New line between each card
            temporary_list.append("")

        # Removes unnecessary features from each value such as '(' or '['
        list_output = "\n".join(temporary_list)
        return list_output


# Function to format dictionaries into a table style design
def card_formatter_table(cards, header):
    # Returns none if dictionary is none from other components or runs program
    if cards is None:
        return None
    else:
        # Table outline
        outline = "+------------------------+-----------------+"
        outline_length = len(outline)
        # Uses any name that the user enters as the title
        title = header
        title_length = len(title)
        # Calculates the number of decorations needed based on length values
        decor_number = (outline_length - title_length) // 2
        # Uses '*' as the decoration and subtracts 1 for space between title
        clean_title = "*" * (decor_number - 1)
        # These set and add the title and table names to the heading boxes
        formatted_output = f"\n{clean_title} {title} {clean_title}\n"
        formatted_output += f"{outline}\n"
        formatted_output += "|          Card          |    Stat Value   |\n"
        formatted_output += f"{outline}\n"
        # Iterates through each card in dictionary
        for card, items in cards.items():
            length_card = len(card)
            total_space = 24
            # Calculates the number of spaces needed on each side of name
            spaces_number = (total_space - length_card) // 2
            # Subtracts 3 to leave space on either side of card for decor
            new_spaces = " " * (spaces_number - 3)
            # Calculates if extra spaces are needed if card name was odd number
            remaining = (total_space - length_card) % 2
            # Adds name, spacing, decor, header to the string
            formatted_output += (f"|{new_spaces}** {card} **{new_spaces + ' ' * 
                                 remaining}|   ** Stats **   |\n")
            # Iterates through each stat in that card
            for item, stat in items.items():
                # A constant to act as base for number of spaces needed
                total_after_space = 16
                after_space = total_after_space - len(item)
                # Converts integer to a string so length can be calculated
                stat_string = f"{stat}"
                length_stat = len(stat_string)
                # If stat length is 2, 7 spaces are needed after or if 1 only 8
                if length_stat == 2:
                    stat_after_space = 7
                else:
                    stat_after_space = 8
                formatted_output += (f"|     -  {item}{' ' * after_space}|"
                                     f"{' ' * 8}{stat}{' ' * stat_after_space}"
                                     f"|\n")
            # Adds outline to bottom of card
            formatted_output += f"{outline}\n"

        return formatted_output


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
# Stores list of stats to make iterating through each card easier
stats = ["Strength", "Speed", "Stealth", "Cunning"]

main(card_catalogue, stats)
