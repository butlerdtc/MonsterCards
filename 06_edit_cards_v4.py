"""V4 of edit card component
This adds markers to output correct instructions and edits the menu to work
for other components output but still doesn't confirm the edited card.
Created by Robson Butler - 23/05/24
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


# This function runs the menu that lets user edit or not
def editing_menu(card_dict, formatted_card_dict, marker, stat_list):
    # This checks which component has been used based on the marker or if None
    if marker == 0 or card_dict is None or formatted_card_dict is None:
        # If None is returned, 0 will have been as well so this returns None
        return None
    elif marker == 1:
        # If marker is 1, the add function has been run so the statements are
        # 'added' instead of 'updated'
        edited_statements = "added"
    else:
        # If marker is 2, the search function has been run so the statements
        # are replaced with 'updated' instead of 'added'
        edited_statements = "updated"
    # Loops until user cancels or confirms the card
    while True:
        edit_options = easygui.buttonbox(f"Would you like to edit, cancel"
                                         f" or confirm this card?\n"
                                         f"\n{formatted_card_dict}", "Options",
                                         ["Edit", "Confirm", "Cancel"])
        if edit_options == "Cancel":
            easygui.msgbox(f"Card has not been {edited_statements}",
                           f"{edited_statements.title()} card")
            return None
        elif edit_options == "Confirm":
            # Will add/update the card to the catalogue
            easygui.msgbox(f"Card has been {edited_statements}",
                           f"{edited_statements.title()} card")
            return card_dict
        else:
            card_dict = edit_card_details(card_dict, stat_list)


# This function will edit the card then return the edited card
def edit_card_details(card_information, stat_list):
    # If edit is chosen loops until user edits card or cancels
    while True:
        if card_information is None:
            # Ends loop if user cancels
            easygui.msgbox("Cancelled", "Cancelled")
            return None
        card_name = list(card_information.keys())[0]
        # Asks if they want to change the card name
        edit_name = easygui.buttonbox("Would you like to edit the"
                                      " card name?", "Edit",
                                      ["Yes", "No"])
        if edit_name == "No":
            searched_stat = easygui.buttonbox("What stat would "
                                              "you like to change?",
                                              "Stats", stat_list)
            # Asks for new stat value
            while True:
                new_value = easygui.integerbox(f"Enter new value for "
                                               f"{searched_stat}",
                                               "New stat",
                                               upperbound=10000000,
                                               lowerbound=-10000000)
                if 1 <= new_value <= 25:
                    # Updates stat in catalogue
                    card_information[card_name][searched_stat] = (
                        new_value)
                    return card_information
                else:
                    easygui.msgbox("Please enter a value between "
                                   "1 and 25", "Error")
        else:
            # Asks for new name then updates it
            new_name = easygui.enterbox("Enter new card name",
                                        "New name")
            card_information[new_name] = card_information.pop(card_name)
            return card_information


# Main routine
# For testing the catalogue will only have one card
card_catalogue = {"Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25,
                                "Cunning": 15}}
# List of all stats
stats = ["Strength", "Speed", "Stealth", "Cunning"]

formatted_card = card_formatter_list(card_catalogue)
result = editing_menu(card_catalogue, formatted_card, 1, stats)
print(result)
