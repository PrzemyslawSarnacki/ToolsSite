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
from core.modules.conv import convert_docx_to_pdf, allowed_file
from werkzeug.utils import secure_filename

bp = Blueprint("conv", __name__, url_prefix="/conv")
bp.config = {}

@bp.record
def record_params(setup_state):
  app = setup_state.app
  bp.config = dict([(key,value) for (key,value) in app.config.items()])


@bp.route("/")
def conv():
    return render_template("/conv/conv_form.html")

@bp.route("/success", methods=["POST", "GET"])
def success():
    if request.method == "POST":
        f = request.files['file']  
        f.save(os.path.join(bp.config["UPLOAD_FOLDER"], f.filename))
        convert_docx_to_pdf(f.filename)
        return redirect(url_for("conv.uploaded_file", filename="merged_document.pdf"))
    return render_template("/conv/conv_form.html")

@bp.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(
        bp.config["DOWNLOAD_FOLDER"], filename, as_attachment=True
    )    