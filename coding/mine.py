from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import keyboard
keyboard1 = KeyboardController()
mouse = MouseController()
blockstobebroken = 1000
while True:
    if keyboard.read_key() == 'e':
        while blockstobebroken != 0:
            keyboard1.press('d')
            keyboard1.release('d')
            mouse.click(Button.left)
            blockstobebroken -= 1
            