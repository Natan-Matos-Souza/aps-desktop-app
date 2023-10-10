from tkinter import *
from windows.response import createResponseWindow

mainWindow = Tk()
mainWindow.title('Carbon Credit Calculator')
mainWindow.minsize(width=1280, height=720)

nameEntryLabel = Label(mainWindow, text="Digite o seu nome: ")
nameEntry = Entry(mainWindow)


##main btn
getNameBtn = Button(mainWindow, text='Send', command=lambda: createResponseWindow({"name": nameEntry.get()}))

nameEntryLabel.pack()
nameEntry.pack()
getNameBtn.pack()

mainWindow.mainloop()