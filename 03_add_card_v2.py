"""V2 of add card component
Changes V1 to check if card is already in the catalogue and will make user
enter new name if it is found. Now uses a list of each stat to iterate through
instead of asking for each stat in a separate line of code.
Created by Robson Butler - 13/05/24
"""

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
    # Asks for new card name
    new_card_name = input("Please enter name of the new card: ").title()
    # Checks if card name is already in the catalogue
    if new_card_name in card_catalogue:
        print("This card is already in the catalogue\nPlease enter a new name")
        continue
    else:
        # Adds new card name to temporary dictionary
        temporary_dict[new_card_name] = {}
        break

# Iterates through each stat from the list to get new values
for stat in stats:
    temporary_dict[new_card_name][stat] = int(input(f"Enter {new_card_name}'s "
                                                    f"{stat} value: "))
# Prints new card and details
print(temporary_dict)
