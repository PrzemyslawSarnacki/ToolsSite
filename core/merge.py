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
def merge(context=""):
    if request.method == 'POST':
        filenames = []
        for key, f in request.files.items():
            if key.startswith('file'):
                if f and allowed_file(f.filename):
                    filename = secure_filename(f.filename)
                    f.save(os.path.join(bp.config['UPLOAD_FOLDER'], filename))
                    filenames.append(filename)
                else:
                    print("File doesn't have pdf extension!")
                    return redirect(url_for("merge.merge"))
        print("okk")
        process_multiple_files(bp.config["UPLOAD_FOLDER"], filenames)
        print("ok1")
        # print(bp.config)
        return redirect(url_for("merge.download"))
    return render_template('/upload/upload_form.html', context=request.args.get('context'))


def process_file(path, filename):
    rotate_pages(path, filename, bp.config["DOWNLOAD_FOLDER"])

def process_multiple_files(path, filenames):
    merge_pages(path, filenames, bp.config["DOWNLOAD_FOLDER"])


@bp.route("/uploads", methods=["POST", "GET"])
def download():
    try:
        filename="merged.pdf"
        return send_from_directory(
            bp.config["DOWNLOAD_FOLDER"], filename, as_attachment=True
        )    
    except:
        return redirect(url_for("merge.merge", context="Mamy Problem"))


