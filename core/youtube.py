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

@bp.route("/")
def youtube():
    return render_template("/youtube/youtube_form.html")


@bp.route("/success", methods=["POST"])
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

