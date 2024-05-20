"""V3 of search for a card
Converts V2 to a function and uses the formatter from 04_card_formatter_v4.
This trial uses an enter box to let the user type in the card name.
Created by Robson Butler - **/05/24
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
    if catalogue is None:
        return None
    else:
        # Loops until a card has been found
        while True:
            # Asks user to enter name of card
            search = easygui.enterbox("Please enter the name of the card",
                                      title)
            # If user cancels it returns None
            if search is None:
                return None
            # Capitalizes user input
            formatted_search = search.title()
            # Checks if card searched is in the catalogue
            if formatted_search in card_catalogue:
                found_card = catalogue[formatted_search]
                # Assigns the card name as key to the stat values the card has
                all_card_details = {formatted_search: found_card}
                return all_card_details
            else:
                easygui.msgbox("That card was not found in the catalogue\n\n"
                               "Please enter a card in the catalogue",
                               "Card not found")


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
# Tests function works
card_found = search_card(card_catalogue, "Search catalogue")
if card_found is not None:
    card_printed = card_formatter_list(card_found)
    easygui.msgbox(card_printed, "Card")
else:
    print("None")
