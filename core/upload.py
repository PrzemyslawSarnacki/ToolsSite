from flask import Flask, render_template, request  
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(dir_path, 'uploads')  

app = Flask(__name__)
app.config['UPLOAD_FOLDER']	= UPLOAD_FOLDER

 
@app.route('/')  
def upload():  
    return render_template("/upload/upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        files = request.files.getlist('file')
        for f in files:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))  
        return render_template("/upload/success.html", names=files)
  
if __name__ == '__main__':  
    app.run(debug = True)  
