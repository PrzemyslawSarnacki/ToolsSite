from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def rotate_pages(path, filename, DOWNLOAD_FOLDER):
    input_file = PdfFileReader(open(path, 'rb'))
    output = PdfFileWriter()
    for page_number in range(input_file.getNumPages()):
        page = input_file.getPage(page_number)
        page.rotateClockwise(180)
        output.addPage(page)
    output_stream = open(DOWNLOAD_FOLDER + filename, 'wb')
    output.write(output_stream)

def merge_pages(path, filenames, DOWNLOAD_FOLDER):
    output_name = "merged_document.pdf"
    output = PdfFileWriter()
    for filename in filenames:    
        input_file = PdfFileReader(open(os.path.join(path, filename), 'rb'))
        for page_number in range(input_file.getNumPages()):
            page = input_file.getPage(page_number)
            output.addPage(page)
    output_stream = open(DOWNLOAD_FOLDER + output_name, 'wb')
    output.write(output_stream)