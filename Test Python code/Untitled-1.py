"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.00
numChars = 18
color = "black"
woodType = "oak"

# Charge for this sign.


# Number of characters.
if numChars > 5:
    charge = 35 + (numChars - 5) * 4
elif numChars > 0:
    charge = 35


# Color of characters.
if color == "gold":
    charge += 15 
if color == "black":
    charge += 0
    
# Type of wood.
if woodType == "oak":
    charge += 20
if woodType == "pine":
    charge += 0

# Write assignment and if statements here as appropriate.

# Output Charge for this sign.

print("The charge for this sign is $" + str(charge))