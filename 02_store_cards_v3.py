"""V3 of system to store the cards
Updates V1 to edit card details to simulate user editing card.
Created by Robson Butler - 09/05/24
"""

# Trial 1, a list to store the original cards
catalogue_list = [
    ["Stoneling", 7, 1, 25, 15],
    ["Vexscream", 1, 6, 21, 19],
    ["Dawnmirage", 5, 15, 18, 22],
    ["Blazegolem", 15, 20, 23, 6],
    ["Websnake", 7, 15, 10, 5],
    ["Moldvine", 21, 18, 14, 5],
    ["Vortexwing", 19, 13, 19, 2],
    ["Rotthing", 16, 7, 4, 12],
    ["Froststep", 14, 14, 17, 4],
    ["Wispghoul", 17, 19, 3, 2]
]

# Trial 2, a dictionary to store the original cards
catalogue_dict = {"Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25,
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

# Temporary details to act as user input
temp_name = "Vexscream"
temp_stat = "Speed"
temp_speed = 20

# Trialling for editing details for trial 1 (list)
print("Trial 1:")
found = False
for card in catalogue_list:
    if card[0] == temp_name:
        found = True
        original_speed_1 = card[2]
        print(f"Inputted name: {temp_name}\n{temp_stat} stat: Original = "
              f"{original_speed_1}, New = {temp_speed}")
        print(f"Original: {card[0]}, Strength: {card[1]}, Speed: {card[2]}, "
              f"Stealth: {card[3]}, Cunning: {card[4]}")
        card[2] = temp_speed
        print(f"New: {card[0]}, Strength: {card[1]}, Speed: {card[2]}, "
              f"Stealth: {card[3]}, Cunning: {card[4]}")
        print()
        break

if not found:
    print("Not found")

# Trialling for editing details for trial 2 (dictionary)
print("Trial 2:")
if temp_name in catalogue_dict:
    original_speed_2 = catalogue_dict[temp_name][temp_stat]
    print(f"Inputted name: {temp_name}\n{temp_stat} stat: Original = "
          f"{original_speed_2}, New = {temp_speed}")
    print(f"Original: {catalogue_dict[temp_name]}")
    catalogue_dict[temp_name][temp_stat] = temp_speed
    print(f"New: {catalogue_dict[temp_name]}")
else:
    print("Not found")
