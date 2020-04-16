import os

from flask import Flask, render_template


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""

    dir_path = os.path.dirname(os.path.realpath(__file__))
    UPLOAD_FOLDER = os.path.join(dir_path, "uploads")
    DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/downloads/"



    app = Flask(__name__, instance_relative_config=True)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return "Hello"

    # register the database commands
    from core import db

    db.init_app(app)

    # apply the blueprints to the app
    from core import merge, youtube, index, conv

    app.register_blueprint(youtube.bp)
    app.register_blueprint(merge.bp)
    app.register_blueprint(index.bp)
    app.register_blueprint(conv.bp)
    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app
