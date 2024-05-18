import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root=tk.Tk()
can1=tk.Canvas(root,width=300,height=300)
can1.pack()

def takeSS():
    myss=pyautogui.screenshot()
    save_path=asksaveasfilename()
    myss.save(save_path+"_screenshot.png")
    
myButton=tk.Button(text="Take ScreenShot",command=takeSS,font=10)
can1.create_window(150,150,window=myButton)





