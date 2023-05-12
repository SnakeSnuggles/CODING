import random

chance = random.randint(1,100)


#Opens file gets contents 
with open('games.txt', 'r') as file:
    games = []
    for x in file:
        games.append(x)


with open('buygames', 'r') as file:
    buygames = []
    for x in file:
        buygames.append(x)

#removes \n
gameswithoutn = []
for sub in games:
    gameswithoutn.append(sub.replace("\n", ""))
buygameswithoutn = []
for sub in buygames:
    buygameswithoutn.append(sub.replace("\n", ""))

buychosen = random.randint(0,len(buygameswithoutn)-1)

#check
if chance != 1:
    #chosing the game owned
    x = 1
    while x != 0:
        game = random.randint(0,len(games)- 1)
        print(gameswithoutn[game])
        x -= 1
#chooses the game you buy
else:
    
    print(f"You're buying {buygameswithoutn[buychosen]}")

print(f'''You did not
{chance}
''')
