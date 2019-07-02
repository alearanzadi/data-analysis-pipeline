from xhtml2pdf import pisa             
from urllib.request import urlopen
url = urlopen("http://0.0.0.0:8000/tablachachi.html")

srchtml=url.read()
pisa.showLogging()

outputFilename = "test.pdf"

def convertHtmlToPdf(sourceHtml, outputFilename):
    resultFile = open(outputFilename, "w+b")

    pisaStatus = pisa.CreatePDF(
            sourceHtml,               
            dest=resultFile)           

    resultFile.close()                

    return pisaStatus.err