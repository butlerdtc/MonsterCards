# Test file
import easygui


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

stats = ["Strength", "Speed", "Stealth", "Cunning"]

# Tests function works
card_found, marker = search_card(card_catalogue, "Search catalogue")

temp = []
for card, stat_ in card_found.items():
    temp.append(card)
    for stats_, values in stat_.items():
        temp.append(values)
        index = temp.index(values)


# Function to get the card catalogue, it's a function so copies can be made
def get_card_catalogue():
    return {
        "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
        "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
        "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
        "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
        "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
        "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
        "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
        "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
        "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
        "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
    }

# Original dictionary to hold the original values
original_catalogue = get_card_catalogue()

# Suppose some modifications are made to the card catalogue
# For example, let's increment the "Strength" of "Stoneling" by 1
modified_catalogue = get_card_catalogue()
modified_catalogue["Stoneling"]["Strength"] += 1

# Check if any values have been modified
values_modified = False
for card, stats in modified_catalogue.items():
    for stat, value in stats.items():
        if original_catalogue[card][stat] != value:
            values_modified = True
            break

if values_modified:
    print("Values have been modified.")
else:
    print("Values are the same as the original dictionary.")
