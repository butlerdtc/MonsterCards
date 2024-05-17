"""V2 of card formatter
Converts V1 to a function to and now returns a formatted string, so it can be
used in an easygui box instead of just print statements.
Created by Robson Butler - 16/05/24
"""


def card_formatter(cards):
    outline = "+------------------------+-----------------+"
    outline_length = len(outline)
    title = "Card Catalogue"
    title_length = len(title)
    decor_number = (outline_length - title_length) // 2
    clean_title = "*" * (decor_number - 1)
    formatted_output = f"\n{clean_title} {title} {clean_title}\n"
    formatted_output += f"{outline}\n"
    formatted_output += "|          Card          |    Stat Value   |\n"
    formatted_output += f"{outline}\n"
    for card, items in cards.items():
        length_card = len(card)
        total_space = 24
        spaces_number = (total_space - length_card) // 2
        new_spaces = " " * (spaces_number - 2)
        remaining = (total_space - length_card) % 2
        formatted_output += (f"|{new_spaces}* {card} *{new_spaces + ' ' * 
                             remaining}|    * Stats *    |\n")
        for item, stat in items.items():
            after_space = 16 - len(item)
            stat_string = f"{stat}"
            length_stat = len(stat_string)
            if length_stat == 2:
                stat_space_number = 7
            else:
                stat_space_number = 8
            formatted_output += (f"|     -  {item}{' ' * after_space}|"
                                 f"{' ' * 8}{stat}{' ' * stat_space_number}|"
                                 f"\n")
        formatted_output += f"{outline}\n"

    return formatted_output


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

# Tests function works
formatted_catalogue = card_formatter(card_catalogue)
print(formatted_catalogue)
