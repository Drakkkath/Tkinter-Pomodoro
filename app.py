#pylint: disable=W0614
#The comment above disables unused imports warnings of pylint

from sys import platform
import tkinter as tk
from tkinter import *

#Main window of the app
root = tk.Tk()

#Setting the title
root.title("Pomodoro")

#Setting the app's icon
if (platform == "linux"):
    icon = PhotoImage(file = "icon.png")
    root.iconphoto(False, icon)
else:
    root.iconbitmap("icon.ico")

#Setting the screen's resolution
root.geometry("400x400")

#Disabling screen resizing by the user
root.resizable(0, 0)



root.mainloop()
