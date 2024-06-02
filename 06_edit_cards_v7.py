"""V7 of edit card component
This version is a later addition as it turns out the component did not function
properly if the user cancelled so the update function was removed and added
directly into the edit menu and the copy library was used to make it work.
Created by Robson Butler - 02/06/24
"""
import easygui
import copy


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


# Main routine
card_catalogue = get_card_catalogue()

# Copies the catalogue to serve as an unedited version
copy_catalogue = copy.deepcopy(card_catalogue)

# List of all stats
stats = ["Strength", "Speed", "Stealth", "Cunning"]

# Tests functions work
chosen_card, search_marked = search_card(card_catalogue, "Search card")
formatted_card = card_formatter_list(chosen_card)
result = editing_menu(chosen_card, formatted_card, search_marked, stats,
                      card_catalogue)
if result is not None:
    card_catalogue = result
else:
    card_catalogue = copy_catalogue

print(card_catalogue)
