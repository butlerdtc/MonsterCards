"""V2 of card formatter
Converts V1 to a function and now returns a formatted string, so it can be used
in an easygui box instead of just print statements. This formats the card so
its printed as a list with bullet points for each stat.
Created by Robson Butler - 16/05/24
"""
import easygui


# Function to format dictionaries
def card_formatter(cards):
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
formatted_catalogue = card_formatter(card_catalogue)
easygui.msgbox(formatted_catalogue, "Card catalogue")
