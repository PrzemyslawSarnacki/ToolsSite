from docx2pdf import convert
import os

ALLOWED_EXTENSIONS = {'docx'}

def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def conv2pdf(path, DOWNLOAD_FOLDER):
    convert(r"C:\Users\Przemyslaw\Projects\ToolsSite\core/uploads/Sprawozdanie-Lab1-sieci-neuronowe-1.docx", r"C:\Users\Przemyslaw\Projects\ToolsSite\core\downloads\output.pdf")