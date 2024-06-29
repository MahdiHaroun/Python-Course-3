nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    for y in x:
        print("     level2: " + y)
#**************************************************************
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings = []

for x in L:
    for y in x:
        if 'b' in y:  # Check if 'b' is in the string 'y', not in the list 'x'
            b_strings.append(y)

print(b_strings)
