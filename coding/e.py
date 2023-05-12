from pynput.keyboard import Key, Controller
import keyboard

thethingthatcandostufftrustmeIknowwhatiamdoing = Controller()
noob = keyboard
number = 286

while True:
    if keyboard.read_key() == 'e':
        bobo = f'e{number}'
        thethingthatcandostufftrustmeIknowwhatiamdoing.type(bobo)
        
        thethingthatcandostufftrustmeIknowwhatiamdoing.type(Key.enter)
        number += 1
