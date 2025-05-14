"""Blueprint for version endpoint."""

from flask import Blueprint

version = Blueprint('version', __name__)

application_version = "0.0.2"

@version.route("/version")
def app_version():
    """Route to get the application version."""
    return application_version
