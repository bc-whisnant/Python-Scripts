import os
from tkinter import *


window=Tk()

def openPrograms():
    #chrome, sublime text, filezila, itunes
    filezillaPath = "C:\Program Files\FileZilla FTP Client"
    chromePath = "C:\Program Files\Google\Chrome\Application"
    itunesPath = "C:\Program Files\iTunes"
    os.system("start filezilla.exe {filezillaPath}")
    os.system("start chrome.exe {chromePath}")
    os.system("start iTunes.exe {itunesPath}")

b1 = Button(window, text="Open Programs", command=openPrograms)
b1.grid(row=0, column=0)


window.mainloop()
