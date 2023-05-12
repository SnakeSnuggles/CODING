import random
import time
from pynput.keyboard import Key, Controller
import keyboard
import time

def clases():

    keynumber, classes = ['1', '2', '3', '4', '5', '7', '8'], ['Scout', 'Soldier', 'Pyro', 'Demoman', 'Heavy', 'Engineer', 'Medic', 'Sniper', 'Spy']
    randomcrap = random.randint(0, len(keynumber) - 1)
    howlong = random.randint(1,10)
    print(F'You will be playing {classes[randomcrap]} for {howlong} minutes')
    thethingthatcandostufftrustmeIknowwhatiamdoing = Controller()
    print("We are ready to go!")
    time.sleep(0.7)
    thethingthatcandostufftrustmeIknowwhatiamdoing.press(',')
    thethingthatcandostufftrustmeIknowwhatiamdoing.release(',')
    time.sleep(0.7)
    thethingthatcandostufftrustmeIknowwhatiamdoing.press(keynumber[randomcrap])
    thethingthatcandostufftrustmeIknowwhatiamdoing.release(keynumber[randomcrap])
    time.sleep(0.01)


x = 1
while x != 0:
    if keyboard.read_key() == '/':
        x -= 1

while True:
    clases()
    if keyboard.read_key() == 'o':
        clases()
