"""Main entry point for the Flask application."""

from flask import Flask
from blueprints import temperature, version
from extensions import cache
from metrics import init_metrics

# Flask app instantiation and blueprints
app = Flask(__name__)
app.register_blueprint(temperature, url_prefix='')
app.register_blueprint(version, url_prefix='')

# Configuration and extensions
app.config.from_object("config")
cache.init_app(app)
init_metrics(app)

if __name__ == "__main__":
    app.run(
        host=app.config.get("FLASK_HOST"),
        port=app.config.get("FLASK_PORT"),
    )
