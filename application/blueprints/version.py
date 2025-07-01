"""Blueprint for version endpoint."""

import os
from flask import Blueprint


version = Blueprint('version', __name__)

application_version = os.environ.get("APPLICATION_VERSION", "0.0.5")

@version.route("/version")
def app_version():
    """Route to get the application version."""
    return application_version
