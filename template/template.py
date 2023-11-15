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
                # print(f'O arquivo foi salvo com nome: {fileName}')

    pdf = canvas.Canvas(f'{filePath}/{fileName}', pagesize=A4)
    
    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFontSize(18)
    pdf.drawCentredString(113*mm, 270*mm, 'Relatório Sobre Crédito de Carbono')


    ##

    ##PDF COMPANY INFO
    pdf.setFillColorRGB(0, 255, 0)
    pdf.setFontSize(12)

    pdf.drawString(20*mm, 250*mm, 'Nome da Empresa:')
    pdf.drawString(20*mm, 240*mm, 'Endereço da Empresa:')
    pdf.drawString(20*mm, 230*mm, 'Data do documento:')
    pdf.setFillColorRGB(0, 0, 0)
    # pdf.drawCentredString(77*mm, 250*mm, data["companyName"])
    # pdf.drawCentredString(77*mm, 240*mm, data["companyCity"])
    # pdf.drawCentredString(77*mm, 230*mm, data["date"])



    pdf.save()    