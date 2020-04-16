from flask import Flask, redirect, render_template
from upload import test, upload 
from youtube import download, success
app = Flask(__name__)


@app.route('/home')
def hello():
    return render_template("/index/index_form.html")


if __name__ == "__main__":
    app.run(debug=True)
