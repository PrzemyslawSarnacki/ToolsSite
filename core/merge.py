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
from core.modules.pdf import merge_pages, rotate_pages, allowed_file
from werkzeug.utils import secure_filename

bp = Blueprint("merge", __name__, url_prefix="/merge")
bp.config = {}

@bp.record
def record_params(setup_state):
  app = setup_state.app
  bp.config = dict([(key,value) for (key,value) in app.config.items()])


@bp.route("/", methods=["POST", "GET"])
def merge():
    if request.method == 'POST':
        print("kki")
        if "file" not in request.files:
            print("No file attached in request")
            return redirect(url_for("merge"))
        files = request.files.getlist("file")
        if len(files) < 2:
            print("No file selected")
            return redirect(url_for("merge"))
        filenames = []
        for f in files:
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(bp.config["UPLOAD_FOLDER"], filename))
                filenames.append(filename)
            else:
                print("File doesn't have pdf extension!")
                return redirect(url_for("merge"))
        process_multiple_files(bp.config["UPLOAD_FOLDER"], filenames)
        return redirect(url_for("merge.uploaded_file", filename="merged_document.pdf"))
    print("okki")
    return render_template("/upload/upload_form.html")


def process_file(path, filename):
    rotate_pages(path, filename, bp.config["DOWNLOAD_FOLDER"])

def process_multiple_files(path, filenames):
    merge_pages(path, filenames, bp.config["DOWNLOAD_FOLDER"])


@bp.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(
        bp.config["DOWNLOAD_FOLDER"], filename, as_attachment=True
    )

