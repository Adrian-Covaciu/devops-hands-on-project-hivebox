"""Main entry point for the Flask application."""

from flask import Flask
from blueprints import temperature, version

app = Flask(__name__)
app.register_blueprint(temperature, url_prefix='')
app.register_blueprint(version, url_prefix='')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
