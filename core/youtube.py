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
from core.modules.youtube import download_mp3, download_video, download_playlist

bp = Blueprint("youtube", __name__, url_prefix="/youtube")
bp.config = {}

@bp.record
def record_params(setup_state):
    app = setup_state.app
    bp.config = dict([(key,value) for (key,value) in app.config.items()])


@bp.route("/", methods=["GET", "POST"])
def video():
    if request.method == "POST":
        if "link" not in request.form:
            print("No url attached in request")
            return redirect(url_for("youtube.youtube"))
        link = request.form.get("link")
        filename = download_video(link)
        return redirect(url_for("youtube.uploaded_file", filename=filename))
    return render_template("/youtube/youtube_form.html", context="Download Video")

@bp.route("/mp3", methods=["GET", "POST"])
def mp3():
    if request.method == "POST":
        if "link" not in request.form:
            print("No url attached in request")
            return redirect(url_for("youtube.youtube"))
        link = request.form.get("link")
        filename = download_mp3(link)
        return redirect(url_for("youtube.uploaded_file", filename=filename))
    return render_template("/youtube/youtube_form.html", context="Download MP3")

@bp.route("/playlist", methods=["GET", "POST"])
def playlist():
    if request.method == "POST":
        if "link" not in request.form:
            print("No url attached in request")
            return redirect(url_for("youtube.playlist"))
        link = request.form.get("link")
        filename = download_playlist(link, bp.config["DOWNLOAD_FOLDER"])
        return redirect(url_for("youtube.uploaded_file", filename=filename))
    return render_template("/youtube/youtube_form.html", context="Download Playlist")


@bp.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        if "link" not in request.form:
            print("No url attached in request")
            return redirect(url_for("youtube.youtube"))
        link = request.form.get("link")
        return render_template("/youtube/success.html", link=link)
    return render_template("/youtube/youtube_form.html")

@bp.route("/download/<filename>")
def uploaded_file(filename):
    return send_from_directory(
        bp.config["DOWNLOAD_FOLDER"], filename, as_attachment=True
    )
