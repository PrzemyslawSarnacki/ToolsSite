from docx2pdf import convert
import os, shutil

ALLOWED_EXTENSIONS = {'docx'}

def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def conv2pdf(path, DOWNLOAD_FOLDER):
   convert(path, DOWNLOAD_FOLDER)

def clear_directory(directory):
   for root, dirs, files in os.walk(directory):
      for f in files:
         os.unlink(os.path.join(root, f))
      for d in dirs:
         shutil.rmtree(os.path.join(root, d))

def get_filename(directory):
   print("List dir:")
   print(os.listdir(directory))
   return os.listdir(directory)[0]
