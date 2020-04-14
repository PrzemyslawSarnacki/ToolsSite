import os
from PyPDF2 import PdfFileReader, PdfFileWriter

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(dir_path, 'uploads/')  
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'

print(UPLOAD_FOLDER)
print(DOWNLOAD_FOLDER)
filenames = []
for filename in os.listdir(UPLOAD_FOLDER):
        filenames.append(filename)
# filenames = 
# print(filenames)


def merge_pages(path, filenames):
    output_name = "merged_document.pdf"
    output = PdfFileWriter()
    for filename in filenames:    
        input_file = PdfFileReader(open(path + filename, 'rb'))
        for page_number in range(input_file.getNumPages()):
            page = input_file.getPage(page_number)
            output.addPage(page)
    output_stream = open(DOWNLOAD_FOLDER + output_name, 'wb')
    output.write(output_stream)

merge_pages(UPLOAD_FOLDER, filenames)