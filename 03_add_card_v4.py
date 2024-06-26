"""V4 of add card component
Converts V3 into a function and uses the catalogue and stat list as arguments.
Adds a new function 'value_checker' to check if user cancels during the
component and then returns 'None' if yes or the new card if no.
Created by Robson Butler - 14/05/24
"""
import easygui


# Function to check if dictionary or any stat in dictionary is empty
def dict_none_checker(dictionary, number_pairs):
    # Check if the dictionary is empty if so return none
    if not dictionary:
        return None

    # Iterates through each pair in the dictionary
    for key, value in dictionary.items():
        # Checks if the key is not None and not empty, if it is returns none
        if key is None or not key:
            return None

        # Checks if the number of pairs in the dictionary matches the number of
        # stats. This prevents the function returning half a dictionary.
        if len(value) != number_pairs:
            return None

    # If all keys have the expected number of pairs and the key is not none
    # return the initial dictionary
    return dictionary


# Function to allow user to add a new card
def add_card(catalogue, values):
    number_stats = len(values)
    while True:
        # This keeps track if this function is used (Affects edit component)
        added_used = 0
        # Dictionary to store entered data until its confirmed and added
        temporary_dict = {}
        # Marks if user cancels the program
        cancel_marker = False
        # Asks for new card name
        new_card_name = easygui.enterbox("Please enter name of the new card",
                                         "New name")
        # This checks if the user selected cancel or entered a name
        if new_card_name is not None:
            # Converts user input to have a capital letter
            new_name = new_card_name.title()
            # Checks if card name is already in the catalogue then prints error
            if new_name in catalogue:
                easygui.msgbox("This card is already in the catalogue\nPlease"
                               " enter a new name", "Error")
                continue
            else:
                # Adds new card name to temporary dictionary
                temporary_dict[new_name] = {}
                # Iterates through each stat from the list to get new values
                for stat in values:
                    while True:
                        stat_value = easygui.integerbox(f"Enter {new_name}'s "
                                                        f"{stat} value",
                                                        f"{stat} value",
                                                        upperbound=10000000,
                                                        lowerbound=-10000000)
                        # If user selects cancel runs confirmation check
                        if stat_value is None:
                            # This asks to confirm cancelling the card
                            confirm_stat = easygui.buttonbox("Are you sure"
                                                             " you want to "
                                                             "cancel adding a "
                                                             "card",
                                                             "Confirm "
                                                             "cancellation",
                                                             ["Yes", "No"])
                            if confirm_stat == "No":
                                continue
                            else:
                                cancel_marker = True
                                break

                        # If input within correct range adds value to stat(key)
                        if 1 <= stat_value <= 25:
                            temporary_dict[new_name][stat] = stat_value
                            break
                        # If cancel not selected and input not valid prints
                        # error
                        else:
                            easygui.msgbox("Please enter a value between 1"
                                           " and 25", "Error")
        # Breaks loop if user cancels (same for all break's below)
                    if cancel_marker:
                        break
                if cancel_marker:
                    break

                break
        else:
            # This asks to confirm cancelling the card
            confirm_name = easygui.buttonbox("Are you sure you want to "
                                             "cancel adding a card",
                                             "Confirm cancellation",
                                             ["Yes", "No"])
            if confirm_name == "No":
                continue
            else:
                break

    # Runs value checker to ensure all stats have values and weren't cancelled
    checked_dictionary = dict_none_checker(temporary_dict, number_stats)
    # If none is not returned it sets added_used to 1 to mark it's been used
    if checked_dictionary is not None:
        # Sets it to 1 rather than false so edit function can identify which
        # component was used
        added_used = 1
    return checked_dictionary, added_used


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

# Stores list of stats to make iterating through each card easier
stats = ["Strength", "Speed", "Stealth", "Cunning"]

# This tests whether the component returns the correct information
result = add_card(card_catalogue, stats)
if result is not None:
    print(result)
else:
    print("None - found")
