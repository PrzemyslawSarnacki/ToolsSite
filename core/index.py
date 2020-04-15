from flask import Flask, redirect, render_template
from upload import test, upload 

app = Flask(__name__)


@app.route('/home')
def hello():
    return render_template("/index/index_form.html")

@app.route('/')
def home():
    return upload()

if __name__ == "__main__":
    app.run(debug=True)
