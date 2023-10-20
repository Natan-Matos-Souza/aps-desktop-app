from tkinter import *
from windows.response import createResponseWindow
from tkinter import messagebox

mainWindow = Tk()
mainWindow.title('SustenTech | Cálculo de Crédito de Carbono')


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

companyAddressLabel = Label(mainWindow, text='Digite o endereço da empresa')
companyAddressEntry = Entry(mainWindow)

visualContents.append(companyAddressLabel)
visualContents.append(companyAddressEntry)

formFields.append(companyAddressEntry)

companyVehiclesQuantityLabel = Label(mainWindow, text='Quantos veículos há em sua empresa: ')
companyVehiclesQuantityEntry = Entry(mainWindow)

visualContents.append(companyVehiclesQuantityLabel)
visualContents.append(companyVehiclesQuantityEntry)

formFields.append(companyVehiclesQuantityEntry)

carPolutionLabel = Label(mainWindow, text='Digite a emissão média de carbono do veículo por quilômetro: (em KG)')
carPolutionEntry = Entry(mainWindow)

visualContents.append(carPolutionLabel)
visualContents.append(carPolutionEntry)

formFields.append(carPolutionEntry)

carDistancePerDayLabel = Label(mainWindow, text="Digite quantos quilômetros, em média, um carro de sua empresa circula pela cidade por dia: ")
carDistancePerDayEntry = Entry(mainWindow)


visualContents.append(carDistancePerDayLabel)
visualContents.append(carDistancePerDayEntry)

formFields.append(carDistancePerDayEntry)

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
        "company_name": companyNameEntry.get(),
        "company_address": companyAddressEntry.get(),
        "vehicles_quantity": int(companyVehiclesQuantityEntry.get()),
        "vehicle_polution_per_kilometer": float(carPolutionEntry.get()),
        "vehicle_distance_per_day": int(carDistancePerDayEntry.get())
        }

        if fileNameEntry.get():
            data['filename'] = fileNameEntry.get()
        else:
            data['filename'] = 'file'
        
        ##validating data
        mustBeInteger = [data['vehicles_quantity']]
        invalidForm = False

        for field in mustBeInteger:

            if not isinstance(field, int) or not field > 0:
                invalidForm = True

        if not invalidForm:
            createResponseWindow(data)
        else:
            messagebox.showinfo(title='Preencha o formulário', message='Você não preencheu os campos obrigatórios.')

    else:
        messagebox.showinfo(title='Preencha o formulário', message='Você não preencheu os campos obrigatórios.')

sendDataBtn = Button(mainWindow, text='Próximo', command=lambda: getData())

visualContents.append(sendDataBtn)

##Rendering visual elements
for contents in visualContents:
    contents.pack()

mainWindow.mainloop()