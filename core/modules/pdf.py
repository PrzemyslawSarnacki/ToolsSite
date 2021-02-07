from PyPDF2 import PdfFileReader, PdfFileWriter
import os

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def rotate_pages(path, filename, DOWNLOAD_FOLDER, degrees=90):
    output_name = "/rotated.pdf"
    output = PdfFileWriter()
    input_file = PdfFileReader(open(os.path.join(path, filename), 'rb'))
    for page_number in range(input_file.getNumPages()):
        page = input_file.getPage(page_number)
        page.rotateClockwise(degrees)
        output.addPage(page)
    output_stream = open(DOWNLOAD_FOLDER  + output_name, 'wb')
    output.write(output_stream)
    output_stream.close()

def rotate_certain_page(path, filename, DOWNLOAD_FOLDER, page_to_rotate):
    input_file = PdfFileReader(open(path, 'rb'))
    output = PdfFileWriter()
    for page_number in range(input_file.getNumPages()):
        page = input_file.getPage(page_number)
        if page_number == page_to_rotate:
            page.rotateClockwise(180)
        output.addPage(page)
    output_stream = open(DOWNLOAD_FOLDER + filename, 'wb')
    output.write(output_stream)
    output_stream.close()

def merge_pages(path, filenames, DOWNLOAD_FOLDER):
    output_name = "/merged.pdf"
    output = PdfFileWriter()
    for filename in filenames:    
        input_file = PdfFileReader(open(os.path.join(path, filename), 'rb'))
        for page_number in range(input_file.getNumPages()):
            page = input_file.getPage(page_number)
            output.addPage(page)
    output_stream = open(DOWNLOAD_FOLDER  + output_name, 'wb')
    output.write(output_stream)
    output_stream.close()
