#pylint: disable=W0614
#The comment above disables unused imports warnings of pylint

from sys import platform
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from playsound import playsound

#Main window of the app
root = tk.Tk()

#Setting the title
root.title("Pomodoro")

#Setting the app's icon
if (platform == "linux"):
    icon = PhotoImage(file = "icon.png")
    root.iconphoto(False, icon)
elif (platform[:3] == "win"):
    root.iconbitmap("icon.ico")  #MacOS is not taken into consideration

#Setting the screen's resolution
root.geometry("400x400")

#Disabling screen resizing by the user
root.resizable(0, 0)

freeze = False

def start_command():
    global minute
    global second

    if second == 0:
        if minute != 0:
            minute -= 1
            second = 59
        else:
            start.config(state = ACTIVE)
            playsound("alarm.mp3")
            return None
    else:
        second -= 1

    timer.config(text = "%02d"%minute + ":" + "%02d"%second)
    start.config(state = DISABLED)
    timer.after(1, start_command)




minute = 20
second = 0
font_style = tkFont.Font(family="Lucida Grande", size=50)
timer = Label(root, text = "%02d"%minute + ":" + "%02d"%second, font = font_style)
start = Button(root, text = "Start", command = start_command)

timer.pack(pady = 50)
start.pack()


root.mainloop()
