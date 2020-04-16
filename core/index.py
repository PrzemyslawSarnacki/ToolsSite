from flask import Flask, redirect, render_template
from core.youtube import *
from core.merge import *

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route('/')
def index():
    return render_template("/index/index_form.html")
