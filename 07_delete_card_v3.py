"""V3 of delete card
This converts V2 into a function and adjusts the messages to be clearer to the
user.
Created by Robson Butler - 26/05/24
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
            # Assigns the card name as key to the stat values the card has
            all_card_details = {search: found_card}
            # Sets it to 2 rather than false so edit function can identify
            # which component was used
            search_used = 2
            return all_card_details, search_used


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

# This uses the search function from 05_search_card_v5 to find card to delete
delete, _ = search_card(card_catalogue, "Delete card")
result = delete_card(delete, card_catalogue)
print(result)
