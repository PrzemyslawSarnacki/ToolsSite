from flask import Flask, render_template, request, redirect, url_for, send_from_directory  
import os 
from modules.pdf import merge_pages, rotate_pages

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(dir_path, 'uploads')  
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER']	= UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER


@app.route('/')  
def upload():  
    return render_template("/upload/upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():
    if request.method == 'POST':
        files = request.files.getlist('file')
        filenames = []
        for f in files:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
            filenames.append(f.filename)
        process_multiple_files(app.config['UPLOAD_FOLDER'], filenames)
        return redirect(url_for('uploaded_file', filename="merged_document.pdf"))
        # return render_template("/upload/success.html", names=files)
  
def process_file(path, filename):
    rotate_pages(path, filename)

def process_multiple_files(path, filenames):
    merge_pages(path, filenames, DOWNLOAD_FOLDER)



@app.route('/uploads/<filename>')
def uploaded_file(filename):
   return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':  
    app.run(debug = True)  
