stopitnow = True

while stopitnow == True:
    b = input("What is the base? ")
    h = input('What is the height? ')
    unit = input('What is the unit? ')
    try:
        a = int(b) * int(h) 
        print(f"With a height of {h}{unit} and a base of {b}{unit} the area would be {a}{unit}².")
        break
    except:
        print('Error, you know what you did wrong so try again')
