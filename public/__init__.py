from flask import Flask, Blueprint
from importlib import import_module

def register_blueprints(app):
    views = import_module('.views', package=__name__)
    for name in dir(views):
        view = getattr(views, name)
        if isinstance(view, Blueprint):
            app.register_blueprint(view)

def create_app():
    app = Flask(__name__, template_folder='templates')

    # Register blueprints
    register_blueprints(app)

    return app
