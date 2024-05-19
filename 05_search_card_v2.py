"""V2 of search for a card
Converts V1 to use easygui instead of print statements and added a while loop
to loop until user input is found on catalogue.
Created by Robson Butler - 19/05/24
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

# Loops until a card has been found
while True:
    # Asks user to enter the name of a card
    search = easygui.enterbox("Please enter the name of the card",
                              "Search for card").title()
    # Checks if card entered is in the catalogue
    if search in card_catalogue:
        easygui.msgbox("Card has been found in the catalogue",
                       "Card found")
        break
    else:
        easygui.msgbox("That card was not found in the catalogue\nPlease "
                       "enter a card in the catalogue", "Card not found")
