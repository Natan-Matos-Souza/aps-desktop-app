from tkinter import *

def createResponseWindow(data:dict):
    responseWindow = Tk()

    mainLabel = Label(responseWindow, text=data['name']).pack()

    responseWindow.mainloop()
