from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import os


def createPDF(data: dict):

    if not isinstance(data, dict):
        print('"data" must be a dict')
    
    if not os.path.exists('files'):
        os.mkdir('files')
    
    fileName = f'{data["filename"]}.pdf'

    if os.path.exists(f'files/{fileName}'):
        nameIsValid = False
        fileCounter = 0

        while nameIsValid != True:

            fileCounter += 1
            fileName = f'{data["filename"]}{fileCounter}.pdf'

            if not os.path.exists(f'files/{fileName}'):
                nameIsValid = True
                print(fileName)
    


# data = {
#     "filename": "file"
# }

# createPDF(data)