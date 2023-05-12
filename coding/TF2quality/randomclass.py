import random
from pynput.keyboard import Key, Controller
import keyboard
import time

thethingthatcandostufftrustmeIknowwhatiamdoing = Controller()
keynumber = ['1', '2', '3', '4', '5', '7', '8']
print("We are ready to go!")
while True:
    randomcrap = random.randint(0, len(keynumber) - 1)
    if keyboard.read_key() == ',':
        time.sleep(0.7)
        thethingthatcandostufftrustmeIknowwhatiamdoing.press(keynumber[randomcrap])
        thethingthatcandostufftrustmeIknowwhatiamdoing.release(keynumber[randomcrap])
        time.sleep(0.01)
