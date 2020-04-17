from docx2pdf import convert
import os


def convert_docx_to_pdf(path):
    convert("core/uploads/Sprawozdanie-Lab1-sieci-neuronowe-1.docx", "core/downloads/output.pdf")

convert_docx_to_pdf("")