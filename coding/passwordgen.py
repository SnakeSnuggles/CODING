import random
numbers = ['1','2','3','4','5','6','7','8','9','0']
letterslower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lettershigher = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symoles = ['!','@','#','$','%','^','&','*','-','_','=','+','/','<','>','.',',','?','|',]
password = []

char = 10
while char != 0:
    choosethelist = random.randint(0,2)
    randomletterlower = random.randint(0,len(letterslower) - 1)
    randomletteruper = random.randint(0,len(lettershigher) - 1)
    randomnumber = random.randint(0,len(numbers) - 1)
    randomsymlobe = random.randint(0,len(symoles) - 1)
    if choosethelist == 0:

        password.append(numbers[randomnumber])
    
    elif choosethelist == 1:
        isupperorlower = random.randint(1,2)
        if isupperorlower == 1:
            password.append(letterslower[randomletteruper])
        elif isupperorlower == 2:
            password.append(lettershigher[randomletteruper])

    elif choosethelist == 2:
        
        password.append(symoles[randomsymlobe])
    char -= 1

print(''.join(password))

