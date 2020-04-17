from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
    Blueprint,
)
import os
from core.modules.conv import conv2pdf, allowed_file
from werkzeug.utils import secure_filename

bp = Blueprint("conv", __name__, url_prefix="/conv")
bp.config = {}

@bp.record
def record_params(setup_state):
  app = setup_state.app
  bp.config = dict([(key,value) for (key,value) in app.config.items()])

@bp.route("/", methods=["POST", "GET"])
def conv():
    if request.method == 'POST':
        print("stage 1")
        if "file" not in request.files:
            print("No file attached in request")
            return redirect(url_for("conv.conv"))
        files = request.files.getlist("file")
        filenames = []
        for f in files:
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(bp.config["UPLOAD_FOLDER"], filename))
                filenames.append(filename)
            else:
                print("File doesn't have docx extension!")
                return redirect(url_for("conv.conv"))
        print("stage 2")
        process_file()
        return redirect(url_for("conv.uploaded_file", filename="merged_document.pdf"))
    print("nope")
    return render_template("/upload/upload_form.html")

def process_file():
    print("weszlo")
    conv2pdf(bp.config["UPLOAD_FOLDER"], bp.config["DOWNLOAD_FOLDER"])

@bp.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(
        bp.config["DOWNLOAD_FOLDER"], filename, as_attachment=True
    )    