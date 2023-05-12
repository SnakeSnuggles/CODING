import random

def percenthappen(x):
    while True:
        randomintofdeath = random.randint(0,100)
        
        x = int(whatispercentinput)
        if randomintofdeath <= x:
            print('Made')
        else:
            print("Made not")    

whatispercentinput = input('What is the percent you are working with? ')
percenthappen(0)
