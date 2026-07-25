rows = 5
for i in range(rows):
    spaces = ' ' * i 
    stars = '*' * (2 * rows - 1 - 2 * i)
    print(spaces + stars)