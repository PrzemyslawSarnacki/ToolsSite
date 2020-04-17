from docx2pdf import convert
import os

ALLOWED_EXTENSIONS = {'docx'}

def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def conv2pdf(path, DOWNLOAD_FOLDER):
   print("weszlo2")
   print(path)
   print("weszlo3")
   print(DOWNLOAD_FOLDER)
   print("weszlo4")
   convert(path, DOWNLOAD_FOLDER)
   print("weszlo5")