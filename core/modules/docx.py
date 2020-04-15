from docx2pdf import convert
import os

print(os.getcwd())

def convert_docx_to_pdf(path):
    convert("DC_SDN_lab1_mininet.docx", os.getcwd() + "/" + "output.pdf")
    