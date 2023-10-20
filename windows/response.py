from tkinter import *
from template.template import createPDF
from tkinter import filedialog


def createResponseWindow(data:dict):
    responseWindow = Tk()

    def storePDF():
        path = filedialog.askdirectory(mustexist=True)

        pdfData = data

        pdfData['path'] = path

        print(pdfData)

        createPDF(pdfData)

        responseWindow.destroy()

    generatePdfBtn = Button(responseWindow, text='Generate PDF', command=storePDF)

    print(data)
    generatePdfBtn.pack()

    responseWindow.mainloop()
