from tkinter import *
from template.template import createPDF
from tkinter import filedialog


def createResponseWindow(data:dict):
    responseWindow = Tk()

    #  generatePdfBtn = Button(responseWindow, text="Genarate PDF", command=lambda: createPDF(data)).pack()


    def storePDF():
        path = filedialog.askdirectory(mustexist=True)

        pdfData = {
            "filename": data["filename"],
            "filepath": path
        }

        createPDF(pdfData)

        responseWindow.destroy()

    generatePdfBtn = Button(responseWindow, text='Generate PDF', command=storePDF)

    generatePdfBtn.pack()

    responseWindow.mainloop()
