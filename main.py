from adquisition import load_data
from clean import *
from scraping import *
from analysis import *
from outputs import *
from testPDF import *


def main():
    data = load_data()
    data = clean_data(data)
    scraping = scrap()
    merging = merge(scraping, data)
    creating = create()
    mailing()
    convertHtmlToPdf(srchtml, outputFilename)

if __name__ == '__main__': 
    main()