import random
try:
    number = int(input('How many trys? '))
    yes = 0
    no = 0
    while number >= 0:
        l = ['yes', 'no']
        ln = random.randint(0,1)
        if ln == 0:
            yes += 1
        elif ln == 1:
            no += 1
        number -= 1
    
    print(f"Yes: {yes}")
    print(f"No: {no}")
    if no >= yes:
        diference = no - yes 
        print(f"Diference: {diference}, no is bigger")
    elif yes >= no:
        diference = yes - no
        print(f"Diference: {diference}, yes is bigger")
    if ln == 1:
        print('yes')
    else:
        print('no')
except:
    try:
        print('Idiot')
        number = int(input('How many trys? '))
        yes = 0
        no = 0
        while number >= 0:
            l = ['yes', 'no']
            ln = random.randint(0,1)
            if ln == 0:
                yes += 1
            elif ln == 1:
                no += 1
            number -= 1

        print(f"Yes: {yes}")
        print(f"No: {no}")
        if no >= yes:
            diference = no - yes 
            print(f"Diference: {diference}, no is bigger")
        elif yes >= no:
            diference = yes - no
            print(f"Diference: {diference}, yes is bigger")
        if ln == 1:
            print('yes')
        else:
            print('no')

    except:
        import time
        print('double Idiot')
        time.sleep(0.9)
        print("I'm done")