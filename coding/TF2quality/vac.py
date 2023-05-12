from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()
import keyboard
import time

typing = False

while True:
    
    if keyboard.read_key() == 'e':
        keyboard.press('r')
        keyboard.release('r')
        mouse.click(Button.right)

        keyboard.press('r')
        keyboard.release('r')
        mouse.click(Button.right)

        keyboard.press('r')
        keyboard.release('r')
        mouse.click(Button.right)

        keyboard.press('r')
        keyboard.release('r')
        mouse.click(Button.right)

        keyboard.press('r')
        keyboard.release('r')
        mouse.click(Button.right)
        time.sleep(0.01)


