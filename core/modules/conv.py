from docx2pdf import convert
import os

ALLOWED_EXTENSIONS = {'docx'}

def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_docx_to_pdf(filename):
    convert(filename, "output.pdf")