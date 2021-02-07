from flask import (
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
    Blueprint,
)
import os
from core.modules.conv import (
    conv2pdf,
    allowed_file,
    clear_directory,
    get_filename,
    conv_to_pdf_linux,
)
from werkzeug.utils import secure_filename

bp = Blueprint("conv", __name__, url_prefix="/conv")
bp.config = {}


@bp.record
def record_params(setup_state):
    app = setup_state.app
    bp.config = dict([(key, value) for (key, value) in app.config.items()])
    bp.config["DROPZONE_MAX_FILES"] = 1


@bp.route("/", methods=["POST", "GET"])
def conv(context=""):
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
                    print("File doesn't have docx extension!")
                    return redirect(url_for("conv.conv"))
        process_file(filenames[0])
        return redirect(url_for("conv.download", filename="output.pdf"))
    return render_template("/conv/conv_form.html", context=request.args.get("context"))


def process_file(filename):
    print(filename.split(".")[0])
    # conv2pdf(bp.config["UPLOAD_FOLDER"] + "/" + filename, bp.config["DOWNLOAD_FOLDER"] + "/" + filename.split(".")[0] + ".pdf")
    conv_to_pdf_linux(
        bp.config["UPLOAD_FOLDER"] + "/" + filename, bp.config["DOWNLOAD_FOLDER"]
    )


@bp.route("/uploads")
def download():
    try:
        filename = get_filename(bp.config["DOWNLOAD_FOLDER"])
        print(filename)
        return send_from_directory(
            bp.config["DOWNLOAD_FOLDER"], filename, as_attachment=True
        )
    except:
        return redirect(url_for("conv.conv", context="Mamy Problem"))
