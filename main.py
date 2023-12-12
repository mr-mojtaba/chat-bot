# Need to install ( pip install pyautogui )
import pyautogui
from time import sleep

ls = ["Hi",
      "How are you?",
      "Do you know I'm a Robot?",
      "Take care",
      "Byyyy!"]


sleep(1)
pyautogui.click(460, 692)
for i in ls:
    pyautogui.write(i, interval=0.25)
    pyautogui.hotkey("shift", "enter")
pyautogui.press("enter")
