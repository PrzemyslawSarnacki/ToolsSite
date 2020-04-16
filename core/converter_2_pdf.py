from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
)
import os
from modules.converter_2_pdf import convert_docx_to_pdf, allowed_file
from werkzeug.utils import secure_filename
dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(dir_path, "uploads")
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/downloads/"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024

@app.route('/converter_2_pdf')
def conv2pdf():
    return render_template("/converter_2_pdf/converter_2_pdf.html")

@app.route("/converter_2_pdf_success", methods=["POST"])
def upload_success():
    if request.method == "POST":
        if "file" not in request.files:
            print("No file attached in request")
            return redirect("/converter_2_pdf")
        files = request.files.getlist("file")
        if len(files) < 2:
            print("No file selected")
            return redirect("/converter_2_pdf")
        filenames = []
        for f in files:
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                filenames.append(filename)
            else:
                print("File doesn't have docx extension!")
                return redirect("/upload")
        convert_docx_to_pdf(filename)
        return redirect(url_for("uploaded_file", filename="output.pdf"))
    return render_template("/converter_2_pdf/converter_2_pdf_form.html")

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(
        app.config["DOWNLOAD_FOLDER"], filename, as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
