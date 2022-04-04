quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
 

# Quick way of generating all of the capital letters
capitals = []

for i in range(65,91):
    capitals.append(chr(i))


# Use a for loop and an if statement to print just the capitals in the quote above.
for l in quote:
    if l in capitals:
        print(l)
