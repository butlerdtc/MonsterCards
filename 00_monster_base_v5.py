"""Monster cards  base component V5
Each component gets added after creation and testing. Functions updated from
component 6. Incorporated the updated edit component so it now functions
properly.
Created by Robson Butler - 02/06/24
"""
import easygui
import copy


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
        # A deep copy of the catalogue before user edits it
        copied_catalogue = copy.deepcopy(catalogue)

        # This sorts the catalogue alphabetically
        sorted_catalogue = sort_card_catalogue(catalogue)
        # Asks user to choose an option
        choice = easygui.buttonbox("What would you like to do?", "Options",
                                   ["Add card", "Search card", "Delete card",
                                    "Show cards", "Exit"])
        if choice == "Add card":
            # This gets the new cards dictionary and added stores if it was
            # cancelled
            new_card_dict, added = add_card(sorted_catalogue, stat_list)
            # This formats the new card for use in displaying it
            formatted_new_card = card_formatter_list(new_card_dict)

            # This gets the result of the edit menu
            result = (editing_menu(new_card_dict, formatted_new_card, added,
                      stat_list, catalogue))

            if result is not None:
                catalogue = result
            else:
                catalogue = copied_catalogue

        elif choice == "Search card":
            searched_card_dict, searched = search_card(sorted_catalogue,
                                                       "Search catalogue")
            formatted_searched_card = card_formatter_list(searched_card_dict)

            result_ = (editing_menu(searched_card_dict, formatted_searched_card,
                       searched, stat_list, catalogue))

            if result_ is not None:
                catalogue = result_
            else:
                catalogue = copied_catalogue

        elif choice == "Delete card":
            searched_card_deletion, _ = search_card(sorted_catalogue,
                                                    "Delete card")
            # Calls delete function and regenerates catalogue
            catalogue = delete_card(searched_card_deletion, sorted_catalogue)
        elif choice == "Show cards":
            print_cards = print_catalogue(sorted_catalogue)
            print(print_cards)
        else:
            easygui.msgbox("Thanks for using this program", "Goodbye")
            # If selected this stops the program
            exit()


# Function to get the card catalogue, it's a function so copies can be made
def get_card_catalogue():
    return {
        "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25,
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


# Function to sort the catalogue by the first letter of the card names
def sort_card_catalogue(catalogue):
    # Sorts the dictionary by the first letters of each card using 'sorted'
    sorted_card_catalogue = dict(sorted(catalogue.items()))
    return sorted_card_catalogue


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
        # This keeps track if this function is used (Affects edit component)
        added_used = 0
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
    # If none is not returned it sets added_used to 1 to mark it's been used
    if checked_dictionary is not None:
        # Sets it to 1 rather than false so edit function can identify which
        # component was used
        added_used = 1
    return checked_dictionary, added_used


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


# Function to search catalogue for a card
def search_card(catalogue, title):
    # Loops until a card has been found
    while True:
        # This keeps track if this function is used (Affects edit component)
        search_used = 0
        # Sets an empty list and appends each card name
        card_list = []
        for card in catalogue:
            card_list.append(card)
        # Uses list of card names as choices so the user can select one
        search = easygui.choicebox("Please choose a card",
                                   title, card_list)
        if search is None:
            return None, search_used
        # Checks if card searched is in catalogue
        if search:
            found_card = catalogue[search]
            # Assigns the card name as key to the stat values the card has
            all_card_details = {search: found_card}
            # Sets it to 2 rather than false so edit function can identify
            # which component was used
            search_used = 2
            return all_card_details, search_used


# This function runs the editing menu to let the user edit cards
def editing_menu(card_dict, formatted_card_dict, choice_marker, stat_list,
                 catalogue):

    # This checks which component has been used based on the marker or if None
    if choice_marker == 0 or card_dict is None:
        # If None is returned, 0 will have been as well so this returns None
        return None

    elif choice_marker == 1:
        # If marker is 1, the add function has been run so the statements are
        # 'added' instead of 'updated'
        edited_statements = "added"

    else:
        # If marker is 2, the search function has been run so the statements
        # are replaced with 'updated' instead of 'added'
        edited_statements = "updated"

    # This keeps track of the original card name for use in update function
    original_card_name = list(card_dict.keys())[0]

    # Loops until user cancels or confirms the card
    while True:
        # Asks user if they want to edit, confirm or cancel
        edit_options = easygui.buttonbox(f"Would you like to edit, cancel"
                                         f" or confirm this card?\n"
                                         f"\n{formatted_card_dict}",
                                         "Options",
                                         ["Edit", "Confirm", "Cancel"])
        if edit_options == "Cancel":
            easygui.msgbox(f"Card has not been {edited_statements}",
                           f"Card not {edited_statements}")
            # Returns None to show that the user cancelled
            return None

        # Returns the updated catalogue
        elif edit_options == "Confirm":
            easygui.msgbox(f"Card has been {edited_statements}",
                           f"{edited_statements.title()} card")

            # Checks if the original name is in the catalogue
            if original_card_name in catalogue:
                # Checks if the edited card's name was changed
                if original_card_name in card_dict:
                    # Updates the stats of the card if name wasn't changed
                    catalogue[original_card_name].update(
                        card_dict[original_card_name])
                else:
                    # If the cards name was edited this deletes the original
                    # cards information from the catalogue
                    del catalogue[original_card_name]
                    # Adds new card and details to catalogue
                    catalogue.update(card_dict)
            else:
                # Adds new card to catalogue
                catalogue.update(card_dict)

            # Returns the edited catalogue
            return catalogue

        # If edit they run the function to actually edit the card
        else:

            # Gets the edited card details and new formatted details
            card_dict, new_formatted_card = edit_card_details(card_dict,
                                                              stat_list)
            # Regenerates the formatted card with the updated changes
            formatted_card_dict = new_formatted_card


# This function will let the user edit the card, then returns the edited card
def edit_card_details(card_information, stats_list):
    # Loops until user edits card or cancels
    while True:
        # Converts the card dictionary to a list, so the name can be used
        card_name = list(card_information.keys())[0]

        # Asks if they want to change the card's name, stats or cancel
        chosen_change = easygui.buttonbox("Would you like to edit the "
                                          "card name or the cards stats?",
                                          "Choose what to edit",
                                          ["Name", "Stats", "Cancel"])
        if chosen_change == "Stats":
            # Lets user choose what stat to change
            searched_stat = easygui.buttonbox("What stat would "
                                              "you like to change?",
                                              "Choose stat", stats_list)
            # Asks user for new stat value
            while True:
                # Sets the original stat so, it can be used in messages
                original_stat = card_information[card_name][searched_stat]

                # Gets user input for new stat
                new_value = easygui.integerbox(f"Enter new value for "
                                               f"{searched_stat}",
                                               "New stat",
                                               upperbound=10000000,
                                               lowerbound=-10000000)
                # If user didn't cancel checks if value is within valid range
                if new_value is not None:
                    if 1 <= new_value <= 25:
                        # Message to confirm that can be used in EasyGui
                        confirm_message = (f"Are you sure you want to edit "
                                           f"{card_name}'s {searched_stat} "
                                           f"from {original_stat} to "
                                           f"{new_value}")

                        # Asks user to confirm stat change
                        confirm_stat = easygui.buttonbox(confirm_message,
                                                         f"Confirm "
                                                         f"{searched_stat} "
                                                         f"change",
                                                         ["No", "Yes"])
                        # Continues loop if they don't confirm
                        if confirm_stat == "No":
                            continue
                        else:
                            # Updates stat in card dictionary
                            card_information[card_name][searched_stat] = (
                                new_value)

                            return card_information, card_formatter_list(
                                card_information)
                    else:
                        easygui.msgbox("Please enter a value between "
                                       "1 and 25", "Error")
                # Continues the loop if they cancel adding a stat
                else:
                    break

        # Runs this if they choose to edit the card name
        elif chosen_change == "Name":
            # Loops until user cancels or enters valid new name
            while True:
                # Asks for new name
                new_name = easygui.enterbox("Enter new card name",
                                            "New name")
                # Checks if user cancelled adding new name
                if new_name is not None:

                    # Finds the length of the new name
                    new_name_length = len(new_name)

                    # If the new name is less than 3 characters reruns loop
                    if new_name_length < 3:
                        easygui.msgbox("Card name cannot be less than 3 "
                                       "characters\n\nPlease enter a new "
                                       "name", "Error")
                        continue
                    else:
                        # Capitalizes new name
                        upper_name = new_name.title()

                        # Asks user to confirm updating name
                        confirm_new_name = easygui.buttonbox(f"Are you "
                                                             f"sure you want "
                                                             f"'{upper_name}' "
                                                             f"to replace "
                                                             f"'{card_name}'",
                                                             "Confirm new"
                                                             " name",
                                                             ["No",
                                                              "Yes"])
                        # If user doesn't confirm the loop runs again
                        if confirm_new_name == "No":
                            break
                        else:
                            # Updates the card dictionary to replace old name
                            card_information[upper_name] = (
                                card_information.pop(card_name))

                            return card_information, card_formatter_list(
                                card_information)

                # If user cancelled adding new name runs loop again
                else:
                    break

        # If they cancel returns the unedited card and unedited formatted card
        else:
            return card_information, card_formatter_list(card_information)


# Function to delete chosen card from the catalogue
def delete_card(searched_card, catalogue):
    # If the user didn't cancel searching, run the deletion code
    if searched_card is not None:
        # This finds the card name for use
        card_name = list(searched_card.keys())[0]
        # Formats the cards details for use in messages
        presented_details = card_formatter_list(searched_card)
        # Asks user if they want to delete card or not
        choice = easygui.buttonbox(f"Is this the card you want to delete?\n\n"
                                   f"{presented_details}", "Delete card?",
                                   ["Yes", "No"])
        # If they select yes ask for further confirmation
        if choice == "Yes":
            confirm = easygui.buttonbox(f"Confirm you want to delete "
                                        f"'{card_name}'",
                                        "Confirmation",
                                        ["Delete card", "Cancel deletion"])
            # If they choose delete the card and details are removed
            if confirm == "Delete card":
                catalogue.pop(card_name)
            # If not deletion is cancelled
            else:
                easygui.msgbox(f"{card_name} was not deleted\n\nReturning "
                               f"to options screen", "Deletion cancelled")
        # If not deletion is cancelled
        else:
            easygui.msgbox(f"{card_name} was not deleted\n\nReturning "
                           f"to options screen", "Deletion cancelled")
    # Returns the catalogue, changed or not
    return catalogue


# Function to display cards that will be printed then print them to the console
def print_catalogue(full_catalogue):
    # List to keep track of all card names
    card_list = []
    # Adds all card names and '-' to the list
    for card_name in full_catalogue:
        card_list.append(f"     -   {card_name}")
    all_names = "\n".join(card_list)
    # Displays message of cards that will be printed
    easygui.msgbox(f"These are the cards in the catalogue:\n\n{all_names}"
                   f"\n\nAll cards have been printed to the console",
                   "Catalogue printed")
    # Calls the formatter to get all the formatted catalogue
    printed_catalogue = card_formatter_table(full_catalogue,
                                             "Card Catalogue")
    # Returns the formatted catalogue
    return printed_catalogue


# Main routine
card_catalogue = get_card_catalogue()

stats = ["Strength", "Speed", "Stealth", "Cunning"]

main(card_catalogue, stats)
