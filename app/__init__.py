from flask import Flask

from app.config import Settings


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Settings())
    from app import views

    app.register_blueprint(views.bp)
    return app
