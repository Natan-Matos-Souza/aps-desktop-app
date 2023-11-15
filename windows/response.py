from tkinter import *
from template.template import createPDF
from tkinter import filedialog
from tkinter import messagebox

def createResponseWindow(data:dict):

    visualContents = []

    formFields = []

    responseWindow = Tk()

    responseWindow.title('Sustentch | Cálculo de Crédito de Carbono')

    def storePDF():

        formIsEmpty = False

        for field in formFields:

            if not field.get():
                formIsEmpty = True

        
        if not formIsEmpty:

            isFormInvalid = False

            mustBeInt = []

            for field in mustBeInt:
                
                if not isinstance(field, int) or not field > 0:
                    isFormInvalid = True



            if not isFormInvalid:

                #Getting form data
                formData = {
                    "futureVehicleQuantityEntry": futureVehicleQuantityEntry.get(),
                    "futureVehiclePolutionPerKilometerEntry": futureVehiclePolutionPerKilometerEntry.get(),
                    "futureCarDistancePerDayEntry": futureCarDistancePerDayEntry.get()
                }                    


                def calculateCarbonCredit(firstFormData, secondFormData):

                    global data


                    reducedPolutionPerDay = firstFormData['']



                path = filedialog.askdirectory(mustexist=True)

                data['filepath'] = path


                # print(formData)
                createPDF(data)

                responseWindow.destroy()
            else:
                messagebox.showinfo(title="Formulário preenchido incorretamente", message="Preencha o formulário corretamente!")

        else:
            messagebox.showinfo(title="Formulário preenchido incorretamente", message="Preencha os campos obrigatórios do formulário!")



    futureVehicleQuantityLabel = Label(responseWindow, text="Digite a quantidade de carros que sua empresa pretender ter no futuro: ")
    futureVehicleQuantityEntry = Entry(responseWindow)
    
    visualContents.append(futureVehicleQuantityLabel)
    visualContents.append(futureVehicleQuantityEntry)

    formFields.append(futureVehicleQuantityEntry)

    futureVehiclePolutionPerKilometerLabel = Label(responseWindow, text="Digite a quantidade média de emissão de carbono dos carros que a empresa utilizará futuramente: ")
    futureVehiclePolutionPerKilometerEntry = Entry(responseWindow)

    visualContents.append(futureVehiclePolutionPerKilometerLabel)
    visualContents.append(futureVehiclePolutionPerKilometerEntry)

    formFields.append(futureVehiclePolutionPerKilometerEntry)

    futureCarDistancePerDayLabel = Label(responseWindow, text='Digite quantos quilômetros, em média, o carro percorrerá por dia:')
    futureCarDistancePerDayEntry = Entry(responseWindow)

    visualContents.append(futureCarDistancePerDayLabel)
    visualContents.append(futureCarDistancePerDayEntry)
    formFields.append(futureCarDistancePerDayEntry)


    generatePdfBtn = Button(responseWindow, text='Gerar Relatório', command=storePDF)

    visualContents.append(generatePdfBtn)


    for content in visualContents:
        content.pack()

    responseWindow.mainloop()
