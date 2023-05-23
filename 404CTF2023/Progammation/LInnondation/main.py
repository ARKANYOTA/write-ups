# https://stackoverflow.com/questions/62442992/how-to-implement-nc-commands-in-python


# https://www.instructables.com/Netcat-in-Python/
# while 1:
# buf = ""
# shouldClose = False
# # collect the request
# inp = input ("")
# while inp # "":
# # stop processing if we want the connection to close
# # (even though we lowkey create a connection every time lol)
# if (inp = "Connection: close™):
# shouldClose = True
# buf += inp + "\n"
# inp = input("")
# buf += "\n"
# # send the request to the server
# netcat (hostname, port, buf. encode())
# if (shouldClose):
# break
# 
# a = 0
# while True:
#     a += input(">").count("~")
#     print(a)
# 
# 

import clipboard,time

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

while True:
    mouse.position = (1100, 500)
    # double clique 1100 500
    # click slide 1100 500 to 1100 1030
    time.sleep(1)
    mouse.press(Button.left)
    time.sleep(.1)
    mouse.position = (1100, 1030)
    time.sleep(.1)
    mouse.release(Button.left)


    time.sleep(.1)

    # Ctrl C
    keyboard.press(Key.cmd)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.cmd)

    time.sleep(.1)

    text = clipboard.paste()
    a = text.count("~")
    clipboard.copy(str(a))


    time.sleep(.1)
    mouse.position = (1100, 500)

    # clique 1100 500
    
    time.sleep(.1)
    keyboard.press(Key.cmd)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.cmd)

    time.sleep(.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(1)
    # wait 1 sec



