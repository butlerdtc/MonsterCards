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
            chosen_card = (input("Please choose card from catalogue to edit"
                                 "(or cancel): ").title())
            if chosen_card == "Cancel":
                # Ends loop if user cancels
                print("Cancelled")
                break
            if chosen_card in card_catalogue:
                edit_name = input("Would you like to edit the card name?(Y/N)"
                                  "").lower()
                if edit_name == "n":
                    searched_stat = input("What stat would you like to change?"
                                          "").title()
                    for name, stats in card_catalogue:
                        if searched_stat in stats:
                            new_value = int(input(f"Enter new value for "
                                                  f"{searched_stat}: "))
                            card_catalogue[chosen_card][searched_stat] = (
                                new_value)
                            break
                        else:
                            print("Please enter valid stat")
                elif edit_name == "y":
                    new_name = input("Enter new card name: ")
                    card_catalogue[new_name] = card_catalogue.pop(chosen_card)
                    break
print(card_catalogue)
