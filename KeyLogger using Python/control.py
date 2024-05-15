from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlMouse():
    mouse=Controller()
    mouse.position=(0,200)


def controlKeyboard():
    keyboard=Controller()
    keyboard.type("Iam Freaking!")

controlKeyboard()




