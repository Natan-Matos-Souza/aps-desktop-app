from tkinter import *
from template.template import createPDF
from tkinter import filedialog
from tkinter import messagebox


def createResponseWindow(data:dict):

    responseWindow = Tk()

    def storePDF():

        formIsEmpty = False

        for field in formFields:

            if not field.get():
                formIsEmpty = True

        
        if not formIsEmpty:

            isFormInvalid = False

            mustBeInt = []

            for field in mustBeInt:
                
                if isinstance(field, int) or not field > 0:
                    isFormInvalid = True



            if not isFormInvalid:
                path = filedialog.askdirectory(mustexist=True)

                data['path'] = path

                # createPDF(pdfData)

                responseWindow.destroy()
            else:
                messagebox.showinfo(title="Formulário preenchido incorretamente", message="Preencha o formulário corretamente!")

        else:
            messagebox.showinfo(title="Formulário preenchido incorretamente", message="Preencha os campos obrigatórios do formulário!")


    visualContents = []

    formFields = []


    generatePdfBtn = Button(responseWindow, text='Generate PDF', command=storePDF)

    visualContents.append(generatePdfBtn)

    responseWindow.mainloop()

    for content in visualContents:
        content.pack()
