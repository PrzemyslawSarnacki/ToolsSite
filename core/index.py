<<<<<<< HEAD
from flask import (Flask, redirect, render_template)
app = Flask(__name__)
=======
from flask import Flask, redirect, render_template
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
