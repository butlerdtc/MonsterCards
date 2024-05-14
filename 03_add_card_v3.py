"""V3 of add card component
Changes V2 to use easygui boxes instead of print statements and now uses if
statements to check if user selects cancel (returns None) and won't crash if
they do, also changes the stat entering code to be inside the same loop. Checks
if the entered stat value is within the 0 - 25 range.
Created by Robson Butler - 14/05/24
"""
import easygui

# Card catalogue from 00_monster_base_v1
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

# Stores list of stats to make iterating through each card easier
stats = ["Strength", "Speed", "Stealth", "Cunning"]

while True:
    # Dictionary to store entered data until its confirmed and added
    temporary_dict = {}
    # Flag to mark if user cancels the program
    cancel_marker = False
    # Asks for new card name
    new_card_name = easygui.enterbox("Please enter name of the new card",
                                     "New name")
    # This checks if the user selected cancel or entered a name
    if new_card_name is not None:
        # Converts user input to have a capital letter
        new_name = new_card_name.title()
        # Checks if card name is already in the catalogue then prints error
        if new_name in card_catalogue:
            easygui.msgbox("This card is already in the catalogue\nPlease"
                           " enter a new name", "Error")
            continue
        else:
            # Adds new card name to temporary dictionary
            temporary_dict[new_name] = {}
            # Iterates through each stat from the list to get new values
            for stat in stats:
                while True:
                    stat_value = easygui.integerbox(f"Enter {new_name}'s "
                                                    f"{stat} value",
                                                    f"{stat} value")
                    # If user selects cancel component ends
                    if stat_value is None:
                        cancel_marker = True
                        break

                    # If input within correct range adds value to stat(key)
                    if 0 <= stat_value <= 25:
                        temporary_dict[new_name][stat] = stat_value
                        break
                    # If cancel not selected and input not valid prints error
                    else:
                        easygui.msgbox("Please enter a value between 0 "
                                       "and 25", "Error")
                # Breaks loop if user cancels (same for break's below)
                if cancel_marker:
                    break
            if cancel_marker:
                break

            break
    else:
        break

# Prints new card and details
print(temporary_dict)
