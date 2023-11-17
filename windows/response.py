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

                data['futureVehicleQuantity'] = futureVehicleQuantityEntry.get()
                data['futureVehiclePolutionPerKilometer'] = futureVehiclePolutionPerKilometerEntry.get()
                data['futureCarDistancePerDay'] = futureCarDistancePerDayEntry.get()


                def calculateCarbonCredit(formData):

                    polutionInfo = {}

                    polutionInfo['currentPolutionPerDay'] = float(formData["vehicle_distance_per_day"])  * float(formData["vehicle_polution_per_kilometer"]) * float(formData["vehicles_quantity"])

                    polutionInfo['futurePolutionPerDay'] = float(formData['futureVehiclePolutionPerKilometer']) * float(formData['futureCarDistancePerDay']) * float(formData['futureVehicleQuantity'])

                    polutionInfo['carbonReduction'] = polutionInfo["currentPolutionPerDay"] - polutionInfo["futurePolutionPerDay"]

                    polutionInfo['daysToGetCarbonCredit'] = 1000000/polutionInfo['carbonReduction']
                    

                    return polutionInfo



                path = filedialog.askdirectory(mustexist=True)

                polutionInfo = calculateCarbonCredit(data)

                data['filepath'] = path

                data['carbonReductionPerDay'] = polutionInfo['carbonReduction']
                data['carbonReductionPerMonth'] = data['carbonReductionPerDay'] * 30
                data['carbonReductionPerYear'] = data['carbonReductionPerDay'] * 30 * 12
                data['daysToGetCarbonCredit'] = polutionInfo['daysToGetCarbonCredit']
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
