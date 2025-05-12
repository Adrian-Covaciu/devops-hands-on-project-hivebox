from flask import Blueprint

version = Blueprint('version', __name__)

application_version = "0.0.2"

@version.route("/version")
def app_version():
    return application_version