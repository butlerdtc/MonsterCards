"""V1 of add card component
Asks the user to enter new card name and a value for each of the four
categories then prints the result. Basic structure to build on.
Created by Robson Butler - 13/05/24
"""

# These input statements ask user for new cards name and stat values
new_name = input("Please enter the name of the new card: ").title()
new_strength = int(input("Enter new cards strength value: "))
new_speed = int(input("Enter new cards speed value: "))
new_stealth = int(input("Enter new cards stealth value: "))
new_cunning = int(input("Enter new cards cunning value: "))

# These print the new card's name and stat values
print(f"\n{new_name}:")
print(f"Strength: {new_strength}")
print(f"Speed: {new_speed}")
print(f"Stealth: {new_stealth}")
print(f"Cunning: {new_cunning}")
