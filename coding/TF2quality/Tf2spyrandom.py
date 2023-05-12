import random
from pynput.keyboard import Key, Controller, Listener
import keyboard
import time



thethingthatcandostufftrustmeIknowwhatiamdoing = Controller()
keynumber = ['2', '3', '4','6', '7', '8']
print("We are ready to go!")

while True:
    randomcrap = random.randint(0, len(keynumber) - 1)
    if keyboard.read_key() == '4':
        time.sleep(0.46)
        thethingthatcandostufftrustmeIknowwhatiamdoing.press(keynumber[randomcrap])
        thethingthatcandostufftrustmeIknowwhatiamdoing.release(keynumber[randomcrap])
        time.sleep(0.01)
