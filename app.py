from tkinter import *
from windows.response import createResponseWindow
from template.template import createPDF

mainWindow = Tk()
mainWindow.title('Carbon Credit Calculator')
mainWindow.minsize(width=1280, height=720)

fileNameLabel = Label(mainWindow, text="Digite o nome do arquivo: ")
fileNameEntry = Entry(mainWindow)

nameEntryLabel = Label(mainWindow, text="Digite o seu nome: ")
nameEntry = Entry(mainWindow)


##main btn
# getNameBtn = Button(mainWindow, text='Send', command=lambda: createResponseWindow({"name": nameEntry.get()}))

sendDataBtn = Button(mainWindow, text='Send', command=lambda: createResponseWindow({"filename": fileNameEntry.get()}))


fileNameLabel.pack()
fileNameEntry.pack()
nameEntryLabel.pack()
nameEntry.pack()
sendDataBtn.pack()

mainWindow.mainloop()