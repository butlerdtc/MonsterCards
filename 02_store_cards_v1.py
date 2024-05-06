"""V1 of system to store the cards
Stores the existing cards in 2 different ways, a dictionary and a list.
Created by Robson Butler - 06/05/24
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
