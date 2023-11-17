from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from datetime import datetime
import os

def createPDF(data: dict):

    if not isinstance(data, dict):
        print('"data" must be a dict')
    
    
    data['carbonReduction'] = 20
    data['date'] = f'{datetime.today().day}/{datetime.today().month}/{datetime.today().year}'
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
    pdf.drawString(20*mm, 220*mm, 'Redução de carbono por dia:')
    pdf.drawString(20*mm, 210*mm, 'Redução de carbono por mês:')
    pdf.drawString(20*mm, 200*mm, 'Redução de carbono por ano:')
    pdf.drawString(20*mm, 190*mm, 'Quantidade de dias necessários para obter 1 crédito de carbono:')
    pdf.setFillColorRGB(0, 0, 0)
    pdf.drawString(70*mm, 250*mm, data["company_name"])
    pdf.drawString(70*mm, 240*mm, data["company_address"])
    pdf.drawString(70*mm, 230*mm, data["date"])
    pdf.drawString(80*mm, 220*mm, f'{data["carbonReductionPerDay"]} KG por dia')
    pdf.drawString(80*mm, 210*mm, f'{data["carbonReductionPerMonth"]} KG por mês')
    pdf.drawString(80*mm, 200*mm, f'{data["carbonReductionPerYear"]} KG por ano')
    pdf.drawString(146*mm, 190*mm, f'{data["carbonReductionPerYear"]} dias')



    pdf.save()