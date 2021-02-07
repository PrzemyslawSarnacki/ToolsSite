from flask import (
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
    Blueprint,
)
import os
from core.modules.pdf import merge_pages, rotate_pages, allowed_file
from core.modules.conv import clear_directory
from werkzeug.utils import secure_filename

bp = Blueprint("rotate", __name__, url_prefix="/rotate")
bp.config = {}


@bp.record
def record_params(setup_state):
    app = setup_state.app
    bp.config = dict([(key, value) for (key, value) in app.config.items()])


@bp.route("/", methods=["POST", "GET"])
def rotate(context=""):
    if request.method == "POST":
        filenames = []
        clear_directory(bp.config["UPLOAD_FOLDER"])
        clear_directory(bp.config["DOWNLOAD_FOLDER"])
        for key, f in request.files.items():
            if key.startswith("file"):
                if f and allowed_file(f.filename):
                    filename = secure_filename(f.filename)
                    f.save(os.path.join(bp.config["UPLOAD_FOLDER"], filename))
                    filenames.append(filename)
                else:
                    print("File doesn't have pdf extension!")
                    return redirect(url_for("rotate.rotate"))
        process_file(bp.config["UPLOAD_FOLDER"], filenames[0])
        return redirect(url_for("rotate.download", filename="rotated.pdf"))
    return render_template(
        "/rotate/rotate_form.html", context=request.args.get("context")
    )

def process_file(path, filename):
    rotate_pages(
        path, filename, bp.config["DOWNLOAD_FOLDER"])


@bp.route("/uploads", methods=["POST", "GET"])
def download():
    try:
        filename = "rotated.pdf"
        return send_from_directory(
            bp.config["DOWNLOAD_FOLDER"], filename, as_attachment=True
        )
    except:
        return redirect(url_for("rotate.rotate", context="Mamy Problem"))

