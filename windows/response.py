from tkinter import *
from template.template import createPDF


def createResponseWindow(data:dict):
    responseWindow = Tk()

    generatePdfBtn = Button(responseWindow, text="Genarate PDF", command=lambda: createPDF(data)).pack()

    responseWindow.mainloop()
