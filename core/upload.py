from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
)
import os
from modules.pdf import merge_pages, rotate_pages, allowed_file
from werkzeug.utils import secure_filename

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(dir_path, "uploads")
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/downloads/"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER



@app.route("/")
def upload():
    return render_template("/upload/upload_form.html")


@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        if "file" not in request.files:
            print("No file attached in request")
            return redirect("/")
        files = request.files.getlist("file")
        if len(files) < 2:
            print("No file selected")
            return redirect("/")
        filenames = []
        for f in files:
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                filenames.append(filename)
            else:
                print("File doesn't have pdf extension!")
                redirect("/")
        process_multiple_files(app.config["UPLOAD_FOLDER"], filenames)
        return redirect(url_for("uploaded_file", filename="merged_document.pdf"))


def process_file(path, filename):
    rotate_pages(path, filename, DOWNLOAD_FOLDER)


def process_multiple_files(path, filenames):
    merge_pages(path, filenames, DOWNLOAD_FOLDER)


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(
        app.config["DOWNLOAD_FOLDER"], filename, as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
