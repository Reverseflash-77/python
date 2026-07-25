gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

answer = int(input('Do you like Dawn or Dusk?\n'
                   '1. Dawn\n'
                   '2. Dusk\n'
                   'Enter your choice (1 or 2): '))
if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('Wrong input.')

answer = int(input('When I\'m dead, I want people to remember me as:\n'
                   '1. The Good\n'
                   '2. The Great\n'
                   '3. The Wise\n'
                   '4. The Bold\n'
                   'Enter your choice (1 to 4): '))
if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print('Wrong input.')

answer = int(input('Which kind of instrument most pleases your ear?\n'
                   '1. The violin\n'
                   '2. The trumpet\n'
                   '3. The piano\n'
                   '4. The drum\n'
                   'Enter your choice (1 to 4): '))
if answer == 1:
    slytherin += 4
elif answer == 2:
    hufflepuff += 4
elif answer == 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print('Wrong input.')


print(
    f'''------------------
Final Scores
------------------
Gryffindor: {gryffindor}
Ravenclaw: {ravenclaw}
Hufflepuff: {hufflepuff}
Slytherin: {slytherin}
------------------
Results
------------------'''
)
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print('You belong in Gryffindor!')
elif ravenclaw >= gryffindor and ravenclaw >= hufflepuff and ravenclaw >= slytherin:
    print('You belong in Ravenclaw!')
elif hufflepuff >= gryffindor and hufflepuff >= ravenclaw and hufflepuff >= slytherin:
    print('You belong in Hufflepuff!')
elif slytherin >= gryffindor and slytherin >= ravenclaw and slytherin >= hufflepuff:
    print('You belong in Slytherin!')
