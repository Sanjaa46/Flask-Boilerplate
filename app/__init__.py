from flask import Flask
from app.core.config import Settings, get_settings
from app.modules.health.routes import bp as health_bp


def create_app(settings: Settings | None = None) -> Flask:
    settings = settings or get_settings()
    app = Flask(__name__)
    app.extensions["settings"] = settings
    app.config["SECRET_KEY"] = settings.secret_key.get_secret_value()
    app.config["DEBUG"] = settings.debug
    app.config["TESTING"] = settings.environment == "test"

    app.register_blueprint(health_bp)

    return app