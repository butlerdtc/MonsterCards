"""V2 of edit card component
Converts all print and input statements to Easygui boxes.
Created by Robson Butler - 22/05/24
"""
import easygui

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
# Stat list from 00_monster_base_v3
stats = ["Strength", "Speed", "Stealth", "Cunning"]

# Loops until user cancels or confirms the card
while True:
    edit_options = easygui.buttonbox("What would you like to do?",
                                     "Options",
                                     ["Edit", "Confirm", "Cancel"])
    if edit_options == "Cancel":
        # Will cancel adding/updating the card
        easygui.msgbox("Card has not been updated/added")
        break
    elif edit_options == "Confirm":
        # Will add/update the card to the catalogue
        easygui.msgbox("Card has been added/updated")
        break
    else:
        # If edit is chosen loops until user edits card or cancels
        while True:
            # Makes a list of each card name to be used as temporary buttons
            cards = []
            for card in card_catalogue:
                cards.append(card)
            cards.append("Cancel")
            # This step won't be here when broken down as other components
            # do this step
            chosen_card = easygui.buttonbox("Please choose card",
                                            "Choose card",
                                            cards)
            if chosen_card == "Cancel":
                # Ends loop if user cancels
                easygui.msgbox("Cancelled", "Cancelled")
                break
            if chosen_card in card_catalogue:
                # Asks if they want to change the card name
                edit_name = easygui.buttonbox("Would you like to edit the"
                                              " card name?", "Edit",
                                              ["Yes", "No"])
                if edit_name == "No":
                    searched_stat = easygui.buttonbox("What stat would "
                                                      "you like to change?",
                                                      "Stats", stats)
                    # Asks for new stat value
                    while True:
                        new_value = easygui.integerbox(f"Enter new value for "
                                                       f"{searched_stat}",
                                                       "New stat",
                                                       upperbound=10000000,
                                                       lowerbound=-10000000)
                        if 1 <= new_value <= 25:
                            # Updates stat in catalogue
                            card_catalogue[chosen_card][searched_stat] = (
                                new_value)
                            break
                        else:
                            easygui.msgbox("Please enter a value between "
                                           "1 and 25", "Error")
                    break
                else:
                    # Asks for new name then updates it
                    new_name = easygui.enterbox("Enter new card name",
                                                "New name")
                    card_catalogue[new_name] = card_catalogue.pop(chosen_card)
                    break
print(card_catalogue)
