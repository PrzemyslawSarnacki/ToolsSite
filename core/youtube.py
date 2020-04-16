from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
)
import os
from modules.youtube import download_mp3

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

@app.route("/youtube")
def download():
    return render_template("/youtube/youtube_form.html")
def home_page():
    return redirect("/home")

@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        if "link" not in request.form:
            print("No url attached in request")
            return redirect("/")
        link = request.form.get("link")
        print(link)
        # download_mp3(link)
        return render_template("/youtube/success.html", link=link)


if __name__ == "__main__":
    app.run(debug=True)
