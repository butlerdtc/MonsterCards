"""V1 of edit card component
Basic edit program that has limited functionality but allows user to edit card
name or stat value in the catalogue.
Created by Robson Butler - 21/05/24
"""

# Catalogue from 00_monster_base_v2
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
# Loops until user enters a valid choice
while True:
    edit_options = (input("Would you like to 'confirm' card, 'edit' or 'cancel"
                          "'? ").title())
    if edit_options == "Cancel":
        # Will cancel adding/updating the card
        print("Cancelled")
        break
    elif edit_options == "Confirm":
        # Will add/update the card to the catalogue
        print("Confirmed")
        break
    elif edit_options == "Edit":
        # If edit is entered loops until user edits card or cancels
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
                # If they don't want to edit the card name
                if edit_name == "n":
                    # User enters what stat they want to edit
                    searched_stat = input("What stat would you like to change?"
                                          "").title()
                    for name, stats in card_catalogue:
                        # If stat is correct updates old value with new value
                        if searched_stat in stats:
                            new_value = int(input(f"Enter new value for "
                                                  f"{searched_stat}: "))
                            card_catalogue[chosen_card][searched_stat] = (
                                new_value)
                            break
                        else:
                            print("Please enter valid stat")
                # If they want to edit card name it asks for input then
                # updates the old name
                elif edit_name == "y":
                    new_name = input("Enter new card name: ")
                    card_catalogue[new_name] = card_catalogue.pop(chosen_card)
                    break
    else:
        print("Please choose valid option")
# Prints the catalogue
print(card_catalogue)
