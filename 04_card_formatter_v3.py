"""V3 of card formatter
This is an instance of trialling a different way to format the cards.
Converts V1 to a function to and now returns a formatted string. This trial
adds outlines and creates a table of the cards but still results in the same
data but presented in a different way.
Created by Robson Butler - 17/05/24
"""


# Function to format dictionaries into a table style design
def card_formatter(cards, header):
    # Table outline
    outline = "+------------------------+-----------------+"
    outline_length = len(outline)
    # Uses any name that the user enters as the title
    title = header
    title_length = len(title)
    # Calculates the number of decorations needed based on length values
    decor_number = (outline_length - title_length) // 2
    # Uses '*' as the decoration and subtracts 1 to leave space between title
    clean_title = "*" * (decor_number - 1)
    # These set and add the title and table names to the heading boxes
    formatted_output = f"\n{clean_title} {title} {clean_title}\n"
    formatted_output += f"{outline}\n"
    formatted_output += "|          Card          |    Stat Value   |\n"
    formatted_output += f"{outline}\n"
    # Iterates through each card in dictionary
    for card, items in cards.items():
        length_card = len(card)
        total_space = 24
        # Calculates the number of spaces needed on each side of name
        spaces_number = (total_space - length_card) // 2
        # Subtracts 3 to leave space on either side of card for decor and space
        new_spaces = " " * (spaces_number - 3)
        # Calculates if any extra spaces are needed if card name was odd number
        remaining = (total_space - length_card) % 2
        # Adds name, spacing, decor, header to the string
        formatted_output += (f"|{new_spaces}** {card} **{new_spaces + ' ' * 
                             remaining}|   ** Stats **   |\n")
        # Iterates through each stat in that card
        for item, stat in items.items():
            # A constant to act as base for number of spaces needed
            total_after_space = 16
            after_space = total_after_space - len(item)
            # Converts integer to a string so length can be calculated
            stat_string = f"{stat}"
            length_stat = len(stat_string)
            # If stat length is 2 only 7 spaces are needed after or if 1 only 8
            if length_stat == 2:
                stat_after_space = 7
            else:
                stat_after_space = 8
            formatted_output += (f"|     -  {item}{' ' * after_space}|"
                                 f"{' ' * 8}{stat}{' ' * stat_after_space}|"
                                 f"\n")
        # Adds outline to bottom of card
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
formatted_catalogue = card_formatter(card_catalogue, "Card Catalogue")
print(formatted_catalogue)
