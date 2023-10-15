from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import os

def createPDF(data: dict):

    if not isinstance(data, dict):
        print('"data" must be a dict')
    
    
    fileName = f'{data["filename"]}.pdf'
    filePath = data["filepath"]

    if os.path.exists(f'{filePath}/{fileName}'):
        nameIsValid = False
        fileCounter = 0

        while nameIsValid != True:

            fileCounter += 1
            fileName = f'{data["filename"]}{fileCounter}.pdf'

            if not os.path.exists(f'{filePath}/{fileName}'):
                nameIsValid = True
                print(f'O arquivo foi salvo com nome: {fileName}')

    pdf = canvas.Canvas(f'{filePath}/{fileName}', pagesize=A4)
    pdf.drawCentredString(113*mm, 270*mm, 'Olá!')
    pdf.save()    