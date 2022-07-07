import pyautogui
import os
import keyboard
import time

from rich import print as rprint
from pygame import mixer

mixer.init() 
beep = mixer.Sound("beep.wav")

def print_msg_box(msg, indent=1, width=None, title=None):

    lines = msg.split('\n')
    space = " " * indent
    if not width:

        width = max(map(len, lines))

    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:

        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore

    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    
    rprint(box)

def title(run):

    os.system('cls')
    if run == 1:

        print_msg_box("\nLongVinter AutoFisher\nver 0.8 \nmade by Ariq\n\n[Running]\n", indent = 10)
    else:

        print_msg_box("\nLongVinter AutoFisher\nver 0.8 \nmade by Ariq\n\n[Paused]\n", indent = 10)

    run = 1

def fishing():

    global running
    running = True
    if keyboard.is_pressed('F6'):

        pos = pyautogui.position()
        while running:

            title(1)
            pyautogui.moveTo(pos)
            if keyboard.is_pressed('F5'):

                title(2)
                print('Program paused')
                keyboard.wait("F6")
                time.sleep(3)

            else:

                if pyautogui.locateOnScreen('proper_spot.png', region=(26, 55, 373, 93), confidence=0.7) != None:
                    
                    title(2)
                    rprint('Spot not right')
                    beep.play()
                    time.sleep(2)
                    beep.play()

                    keyboard.wait("F6")

                    time.sleep(3)

                else:

                    pyautogui.press('e')
                    print(pyautogui.click())
                    pyautogui.press('e')
    else:
        pass


if __name__ == "__main__":

    title(1)

    while True:

        fishing()
