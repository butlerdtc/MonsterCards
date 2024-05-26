"""V5 of edit card component
This version adds a new function to update the edited cards details to the
catalogue. The edit menu had to be slightly altered to output the original name
so the update function could work.
Created by Robson Butler - 24/05/24
"""
import easygui


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
            print(found_card)
            # Assigns the card name as key to the stat values the card has
            all_card_details = {search: found_card}
            # Sets it to 2 rather than false so edit function can identify
            # which component was used
            search_used = 2
            return all_card_details, search_used


# This function runs the menu that lets user edit or not
def editing_menu(card_dict, formatted_card_dict, marker, stat_list):
    # Sets original card none as None so if card_dict is None it returns None
    original_card_none = None
    # This checks which component has been used based on the marker or if None
    if marker == 0 or card_dict is None:
        # If None is returned, 0 will have been as well so this returns None
        return None, original_card_none
    elif marker == 1:
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
                                         f"\n{formatted_card_dict}", "Options",
                                         ["Edit", "Confirm", "Cancel"])
        # Returns None if user cancels
        if edit_options == "Cancel":
            easygui.msgbox(f"Card has not been {edited_statements}",
                           f"Card not {edited_statements}")
            return None, original_card_none
        # Returns the edited card dictionary if they confirm
        elif edit_options == "Confirm":
            # Will add/update the card to the catalogue
            easygui.msgbox(f"Card has been {edited_statements}",
                           f"{edited_statements.title()} card")
            return card_dict, original_card_name
        # If edit they run the function to actually edit the card
        else:
            card_dict, new_formatted_card = edit_card_details(card_dict,
                                                              stat_list)
            if card_dict is None:  # Handle cancellation of editing
                return None, original_card_none
            # Regenerates the formatted card with the updated changes
            formatted_card_dict = new_formatted_card


# This function will edit the card then return the edited card
def edit_card_details(card_information, stats_list):
    # This is a copy of the original information that is returned if the user
    # selects no when confirming so the edited data doesn't get returned when
    # it shouldn't
    original_card_info = card_information.copy()
    # Loops until user edits card or cancels
    while True:
        # Converts the card dictionary to a list, so they name can be used
        card_name = list(card_information.keys())[0]
        # Asks if they want to change the card name, stats or cancel
        chosen_change = easygui.buttonbox("Would you like to edit the "
                                          "card name or the cards stats?",
                                          "Choose what to edit",
                                          ["Name", "Stats", "Cancel"])
        if chosen_change == "Stats":
            # Lets user choose what stat to change
            searched_stat = easygui.buttonbox("What stat would "
                                              "you like to change?",
                                              "Choose stat", stats_list)
            # Asks for new stat value
            while True:
                # Sets the original stat so, it can be used in messages
                original_stat = card_information[card_name][searched_stat]
                # Gets user input for new stat
                new_value = easygui.integerbox(f"Enter new value for "
                                               f"{searched_stat}",
                                               "New stat",
                                               upperbound=10000000,
                                               lowerbound=-10000000)
                if new_value is not None:
                    if 1 <= new_value <= 25:
                        # Asks user to confirm stat change
                        confirm_stat = easygui.buttonbox(f"Are you sure you "
                                                         f"want to edit "
                                                         f"{card_name}'s "
                                                         f"{searched_stat} "
                                                         f"from "
                                                         f"{original_stat} to "
                                                         f"{new_value}",
                                                         f"Confirm "
                                                         f"{searched_stat} "
                                                         f"change",
                                                         ["No", "Yes"])
                        # Continues loop if they don't confirm
                        if confirm_stat == "No":
                            formatted_card_info = (
                                card_formatter_list(original_card_info))
                            return original_card_info, formatted_card_info
                        else:
                            # Updates stat in card dictionary
                            card_information[card_name][searched_stat] = (
                                new_value)
                            # Regenerates the formatted card
                            updated_formatted_card = (card_formatter_list
                                                      (card_information))
                            return card_information, updated_formatted_card
                    else:
                        easygui.msgbox("Please enter a value between "
                                       "1 and 25", "Error")
                # Continues the loop if they cancel adding a stat
                else:
                    break
        # Runs this if they choose to edit the card name
        elif chosen_change == "Name":
            # Asks for new name
            new_name = easygui.enterbox("Enter new card name",
                                        "New name")
            # Checks if user cancelled adding new name
            if new_name is not None:
                # Asks user to confirm updating name
                confirm_new_name = easygui.buttonbox(f"Are you sure you want "
                                                     f"'{new_name}' to replace"
                                                     f" '{card_name}'",
                                                     "Confirm new name",
                                                     ["No", "Yes"])
                # If not confirmed loop runs again
                if confirm_new_name == "No":
                    formatted_card_info = card_formatter_list(original_card_info)
                    return original_card_info, formatted_card_info
                else:
                    # Updates the card dictionary to replace old with new name
                    card_information[new_name] = card_information.pop(
                        card_name)
                    # Regenerates the formatted card
                    updated_formatted_card = card_formatter_list(
                        card_information)
                    return card_information, updated_formatted_card
            # If user cancelled adding new name runs loop again
            else:
                continue
        # If they cancel returns the unedited card and unedited formatted card
        else:
            # Returns unedited card and formatted card details
            formatted_details = card_formatter_list(original_card_info)
            return original_card_info, formatted_details


# Function uses the card dictionary from edit menu and updates the catalogue
def update_catalogue(original_name, edited_card, catalogue):
    print("Original Name:", original_name)
    print("Edited Card:", edited_card)
    if edited_card is None:
        print("Edited card is None. Returning catalogue as is.")
        return catalogue
    else:
        if original_name in catalogue:
            print("Original name found in catalogue.")
            if original_name in edited_card:
                print("Original name also found in edited card.")
                catalogue[original_name].update(edited_card[original_name])
            else:
                print("Original name not found in edited card. Deleting original entry.")
                del catalogue[original_name]
            for name, values in edited_card.items():
                if name != original_name:
                    print("Updating catalogue with edited card.")
                    catalogue[name] = values
        print("Returning updated catalogue.")
        return catalogue


# Main routine
card_catalogue = {"Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25,
                                "Cunning": 15},
                  "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21,
                                "Cunning": 19},
                  "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18,
                                 "Cunning": 22},
                  # "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23,
                  #                "Cunning": 6},
                  # "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10,
                  #              "Cunning": 5},
                  # "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14,
                  #              "Cunning": 5},
                  # "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19,
                  #                "Cunning": 2},
                  # "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4,
                  #              "Cunning": 12},
                  # "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17,
                  #               "Cunning": 4},
                  # "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3,
                  #               "Cunning": 2}
                  }

# List of all stats
stats = ["Strength", "Speed", "Stealth", "Cunning"]

# Tests functions work
chosen_card, search_marked = search_card(card_catalogue, "Search card")
# formatted_card = card_formatter_list(chosen_card)
# result, old_name = editing_menu(chosen_card, formatted_card, search_marked,
#                                 stats)
# card_catalogue = update_catalogue(old_name, result, card_catalogue)
