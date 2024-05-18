import pyautogui
import time

msg=3

while msg>0:
    time.sleep(4)
    pyautogui.typewrite("Hello")
    time.sleep(2)
    pyautogui.press("enter")
    msg=msg-1