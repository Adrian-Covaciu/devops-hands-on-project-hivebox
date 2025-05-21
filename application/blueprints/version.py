"""Blueprint for version endpoint."""

from flask import Blueprint
import os

version = Blueprint('version', __name__)

application_version = os.environ.get("APPLICATION_VERSION", "0.0.2")

@version.route("/version")
def app_version():
    """Route to get the application version."""
    return application_version
