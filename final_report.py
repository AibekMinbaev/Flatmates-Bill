import webbrowser
import os

from filestack import Client
from fpdf import FPDF


class PdfReport:
    """
    Creates PDF file that contains data about the flatmates
    such as their names, their due amount
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        # pdf format
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')

        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times', size=12)

        # Insert name and due amount of flatmate1
        flatmate1_pays = str(flatmate1.pays(bill, flatmate2))
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pays, border=0, ln=1)

        # Insert name and due amount of flatmate2
        flatmate2_pays = str(flatmate2.pays(bill, flatmate1))
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pays, border=0, ln=1)

        #pdf.output(f"files/{self.filename}")

        #Change directory to files, generate and open the PDF
        os.chdir('files')
        pdf.output(self.filename)
        webbrowser.open(self.filename)

        # I think it gives me an error because my file is on the cloud,
        #but this is not a problem


class FileSharer:

    def __init__(self, filepath, api_key="AexgcyGzxRBqrepeLcieQz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
