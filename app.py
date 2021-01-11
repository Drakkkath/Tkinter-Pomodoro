#pylint: disable=W0614
#The comment above disables unused imports warnings of pylint

import tkinter as tk
from tkinter import *

#Main window of the app
root = tk.Tk()

#Setting the title
root.title("Pomodoro")

#Setting the screen's resolution
root.geometry("400x400")

#Disabling screen resizing by the user
root.resizable(0, 0)



root.mainloop()
