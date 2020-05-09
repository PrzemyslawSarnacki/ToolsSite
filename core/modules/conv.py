from docx2pdf import convert
import os, shutil
import sys
import subprocess
import re
import subprocess
import tempfile



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


# with filesystem
def conv_to_pdf_linux(path, DOWNLOAD_FOLDER):
   utility = 'soffice'
   print(path)
   print(DOWNLOAD_FOLDER)
   filename = "/mnt/c/Users/Przemyslaw/Projects/ToolsSite/core/uploads/test.docx"
   command = [utility, '--convert-to', 'pdf', path, '--outdir', DOWNLOAD_FOLDER]
   p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# with tempfiles
def convert_to_raw_bytes(self, file, input_format, output_format):
    temp_path = tempfile.NamedTemporaryFile(suffix=".%s" % (input_format, ))
    temp_path.write(file)
    temp_path.flush()

    unoconv_bin = 'unoconv'
    command = [unoconv_bin, '--stdout', '-e', 'UseLosslessCompression=false', '-e', 'ReduceImageResolution=false', '--format', output_format, temp_path.name]
    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data, stderrdata = p.communicate()

    if stderrdata:
        raise Exception(str(stderrdata))

    temp_path.close()

    return data



def convert_to(folder, source, timeout=None):
    args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', folder, source]

    process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    filename = re.search('-> (.*?) using filter', process.stdout.decode())

    if filename is None:
        raise LibreOfficeError(process.stdout.decode())
    else:
        
        return filename.group(1)


def libreoffice_exec():
    # TODO: Provide support for more platforms
    if sys.platform == 'darwin':
        return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
    return 'libreoffice'


class LibreOfficeError(Exception):
    def __init__(self, output):
        self.output = output
