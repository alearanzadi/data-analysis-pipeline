from adquisition import load_data
from clean import *
from scraping import *
from analysis import *
from outputs import *
from testPDF import *
import argparse

def main(to):
    data = load_data()
    data = clean_data(data)
    scraping = scrap()
    merging = merge(scraping, data)
    creating = create()
    mailing(to)
    convertHtmlToPdf(srchtml, outputFilename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Input an email and you will get the information')
    parser.add_argument('--email', dest='email', default="alejandraironhack@gmail.com", type=str, help="Receiver's")
    args = parser.parse_args()

    if "@" in args.email:
        main(args.email)
    else:
        print("Invalid email, please type again")


    