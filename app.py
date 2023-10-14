from tkinter import *
from windows.response import createResponseWindow
from template.template import createPDF
from tkinter import messagebox

mainWindow = Tk()
mainWindow.title('Carbon Credit Calculator')
mainWindow.minsize(width=1280, height=720)

formFields = []

fileNameLabel = Label(mainWindow, text="Digite o nome do arquivo (opcional): ")
fileNameEntry = Entry(mainWindow)
##This input can be empty
# formFields.append(fileNameEntry)

nameEntryLabel = Label(mainWindow, text="Digite o seu nome: ")
nameEntry = Entry(mainWindow)
formFields.append(nameEntry)

#Function that gets user data and calls second window.

messagebox.showinfo(title='Preencha o formulário.', message='Preencha os campos obrigatórios!')

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


fileNameLabel.pack()
fileNameEntry.pack()
nameEntryLabel.pack()
nameEntry.pack()
sendDataBtn.pack()

mainWindow.mainloop()