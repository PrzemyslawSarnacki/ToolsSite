from flask import Flask, redirect, render_template
<<<<<<< HEAD
from upload import test, upload 
from youtube import download, success
app = Flask(__name__)
=======
from core.youtube import *
from core.merge import *

bp = Blueprint("index", __name__, url_prefix="/")
>>>>>>> c228893dba3a0beee269f4d0bb747cdddc17d0bc


@bp.route('/')
def index():
    return render_template("/index/index_form.html")
<<<<<<< HEAD


if __name__ == "__main__":
    app.run(debug=True)
=======
>>>>>>> c228893dba3a0beee269f4d0bb747cdddc17d0bc
