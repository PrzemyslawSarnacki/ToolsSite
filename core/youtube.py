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
from core.modules.youtube import download_mp3

bp = Blueprint("youtube", __name__, url_prefix="/youtube")

<<<<<<< HEAD
app = Flask(__name__)


@app.route("/youtube", methods=["POST"])
=======
@bp.route("/")
def youtube():
    return render_template("/youtube/youtube_form.html")


@bp.route("/success", methods=["POST"])
>>>>>>> c228893dba3a0beee269f4d0bb747cdddc17d0bc
def success():
    if request.method == "POST":
        if "link" not in request.form:
            print("No url attached in request")
            return redirect(url_for("youtube.youtube"))
        link = request.form.get("link")
        print(link)
        # download_mp3(link)
        return render_template("/youtube/success.html", link=link)
    return render_template("/youtube/youtube_form.html")

