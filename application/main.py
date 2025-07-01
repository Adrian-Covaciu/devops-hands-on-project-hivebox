"""Main entry point for the Flask application."""

from flask import Flask
from blueprints import temperature, version
from extensions import cache

app = Flask(__name__)
app.register_blueprint(temperature, url_prefix='')
app.register_blueprint(version, url_prefix='')
app.config.from_object("config")

cache.init_app(app)

if __name__ == "__main__":
    app.run(
        host=app.config.get("FLASK_RUN_HOST"),
        port=app.config.get("FLASK_RUN_PORT"),
    )
