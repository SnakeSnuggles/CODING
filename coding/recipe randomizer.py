import random
with open('Main.txt', 'r') as file:
    main = []
    for x in file:
        main.append(x)

with open('Side.txt', 'r') as file:
    side = []
    for x in file:
        side.append(x)

numberofmeals = int(input('How many meals would you like to generate? '))
mealnumber = 1
mealplan = []

while mealnumber <= numberofmeals:
    randonint = random.randint(0, len(main) - 1)
    newmeal = main[randonint]
    nodoubles = True
    for x in mealplan:
        if x == newmeal:
            nodoubles = False
                
    if nodoubles == True:
        mealplan.append(newmeal)
        mealnumber += 1

number = 1
print('''
Mains:
''')
for i in mealplan:
    print(f'{number}) {i}')
    number += 1
print('''Sides:
''')