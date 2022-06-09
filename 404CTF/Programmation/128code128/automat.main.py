
from time import sleep
import pyautogui
sleep(3)
while True:
    pyautogui.click(1500, 1000)
    pyautogui.click(1500, 1000)
    with pyautogui.hold('shift'):
        with pyautogui.hold('ctrl'):
            pyautogui.press('c')
    sleep(0.1)
    pyautogui.click(500, 1000)
    with pyautogui.hold('shift'):
        with pyautogui.hold('ctrl'):
            pyautogui.press('v')
    sleep(0.1)  
    pyautogui.press('return')
    pyautogui.click(1500, 1000)
    with pyautogui.hold('shift'):
        with pyautogui.hold('ctrl'):
            pyautogui.press('v')
    sleep(1)

