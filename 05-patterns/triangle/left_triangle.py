row = 5
for i in range(row):
    spaces = ' ' * (row - i - 1)
    stars = '*' * (i + 1)
    print(spaces + stars)