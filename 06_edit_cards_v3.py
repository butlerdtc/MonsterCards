"""V3 of edit card component
This converts V2 into two functions, one to ask user if they want to edit,
cancel or confirm then one to edit the card then return the result. This still
needs to be edited to actually edit the cards and work for other components
outputs.
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
def edit_menu(card_dict, formatted_card_dict, stat_list):
    # Loops until user cancels or confirms the card
    while True:
        edit_options = easygui.buttonbox(f"Would you like to edit, cancel"
                                         f" or confirm this card?\n"
                                         f"\n{formatted_card_dict}", "Options",
                                         ["Edit", "Confirm", "Cancel"])
        if edit_options == "Cancel":
            easygui.msgbox("Card has not been updated/added")
            return None
        elif edit_options == "Confirm":
            # Will add/update the card to the catalogue
            easygui.msgbox("Card has been added/updated")
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
result = edit_menu(card_catalogue, formatted_card, stats)
print(result)
