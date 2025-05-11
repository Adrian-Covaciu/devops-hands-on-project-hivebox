
from flask import Flask
import requests


app = Flask(__name__)
application_version = "0.0.2"
box_ids = [
    "5eba5fbad46fb8001b799786",
    "5c21ff8f919bf8001adf2488",
    "5ade1acf223bd80019a1011c"
]

@app.route("/version")
def app_version():
    return application_version

@app.route("/temperature")
def temperature():
    return temperature

