from fpdf import FPDF
from analysis import * 

class PDF(FPDF):                    
	
    def header(self):                          
        self.image('unnamed.jpg', 8, 6, 26)   
        self.set_font('Arial', 'B', 15)                
        self.cell(80)                                 
        self.cell(20, 20, 'Pipelines Project', 2, 0, 'C')  
        self.ln(20)                            

    def footer(self):                                                         
        self.set_y(-15)                                                         
        self.set_font('Arial', 'I', 8)                                          
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '', 0, 0, 'C')
        self.cell(-10, 10, 'Alejandra Aranzadi', 10, 0, 'C') 

def create():
    pdf=PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 22)
    pdf.cell(60)
    pdf.cell(120, 120, 'Fertility vs. GDP')
    pdf.image('GettyImages_748319837.0.jpg', x=40, y=100, w=130, h=90, type = '', link = '')
    pdf.add_page()
    pdf.cell(60)
    pdf.set_font('Arial', 'I', 14)
    pdf.cell(-35)
    pdf.cell(100, 40, 'The data shows that ferlity has a reverse correlation with GDP.')
    pdf.cell(60)
    pdf.set_font('Arial', 'I', 14)
    pdf.cell(-165)
    pdf.cell(100, 70, 'The less GDP a country has, the more children per woman are born')
    pdf.image('mytable.jpg', x=50, y=80, w=130, h=90, type = '', link = '')
    pdf.output('Fertility vs. GDP.pdf', 'F')
    return PDF

import smtplib
import getpass

def mailing(to):
    gmail_user = input("Sender's email adress: ")
    gmail_password = getpass.getpass("Enter password: ")

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        print("Connected to gmail servers")
    except:  
        print("Something went wrong...")

    from_mail = gmail_user
    #to = input("Who should receive the mail?")
    subject = "Fertiliity vs. GDP"
    body = "Checkout my latest data analytics project about fertility related to GDP: https://github.com/alearanzadi/data-analysis-pipeline.git. Regards"

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (from_mail, ", ".join(to), subject, body)

    server.sendmail(from_mail, to, message)
    server.close()

    