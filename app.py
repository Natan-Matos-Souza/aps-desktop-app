from tkinter import *
from windows.response import createResponseWindow
from template.template import createPDF
from tkinter import messagebox

mainWindow = Tk()
mainWindow.title('Carbon Credit Calculator')
mainWindow.minsize(width=1280, height=720)

visualContents = []

formFields = []

fileNameLabel = Label(mainWindow, text="Digite o nome do arquivo (opcional): ")
fileNameEntry = Entry(mainWindow)

visualContents.append(fileNameLabel)
visualContents.append(fileNameEntry)

companyNameLabel = Label(mainWindow, text='Digite o nome da sua empresa: ')
companyNameEntry = Entry(mainWindow)

visualContents.append(companyNameLabel)
visualContents.append(companyNameEntry)

formFields.append(companyNameEntry)

#Function that gets user data and calls second window.
def getData():
    
    def formIsEmpty():
        formIsEmpty = False

        for field in formFields:
            if not field.get():
                formIsEmpty = True

        return formIsEmpty

    if not formIsEmpty():
        data = {
        "filename": None,
        "name": 'Natan Matos'
        }

        if fileNameEntry.get():
            data['filename'] = fileNameEntry.get()
        else:
            data['filename'] = 'file'

        createResponseWindow(data)
    else:
        messagebox.showinfo(title='Preencha o formulário', message='Você não preencheu os campos obrigatórios.')

sendDataBtn = Button(mainWindow, text='Send', command=lambda: getData())

visualContents.append(sendDataBtn)


for contents in visualContents:
    contents.pack()

mainWindow.mainloop()