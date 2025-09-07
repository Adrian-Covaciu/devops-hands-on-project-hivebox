"""Blueprint for temperature endpoint."""

import os
from datetime import datetime, timezone, timedelta
from flask import Blueprint, request
from extensions import cache
import requests

default_box_ids = [
    "5eba5fbad46fb8001b799786",
    "5c21ff8f919bf8001adf2488",
    "5ade1acf223bd80019a1011c",
]
box_ids = os.environ.get("BOX_IDS", ",".join(default_box_ids)).split(",")

def get_sensor_data(sensor_id):
    """Fetch sensor data from the API for a given box."""
    sensor_url = f"https://api.opensensemap.org/boxes/{sensor_id}"
    r = requests.get(url=sensor_url, timeout=10)
    return r.json().get("sensors", [])

def extract_temperature(sensor):
    """Extract temperature if measurement is less than 1 hour old."""
    if sensor["title"] != "Temperatur":
        return None
    last_measurement = sensor["lastMeasurement"]["createdAt"]
    time_measured = datetime.strptime(last_measurement, "%Y-%m-%dT%H:%M:%S.%fZ")
    time_measured = time_measured.replace(tzinfo=timezone.utc)
    if datetime.now(timezone.utc) - time_measured < timedelta(hours=1):
        return float(sensor["lastMeasurement"]["value"])
    return None

@cache.memoize(timeout=300)
def average_temperature(ids):
    """Calculate average temperature."""
    temps = []
    for sensor_id in ids:
        sensors = get_sensor_data(sensor_id)
        for sensor in sensors:
            temp = extract_temperature(sensor)
            if temp is not None:
                temps.append(temp)
                print(f"Sensor ID: {sensor_id}, Temperature: {temp}")
    if not temps:
        return None
    average = sum(temps) / len(temps)
    return {"average_temperature": average, "status": status_temperature(average)}

def status_temperature(temperature_value):
    """Function that returns the status of the temperature."""
    if temperature_value is None:
        return "No data available"
    if temperature_value < 10:
        return "Too Cold"
    if 11 <= temperature_value <= 36:
        return "Good"
    return "Too Hot"

temperature = Blueprint('temperature', __name__ )

@temperature.route('/temperature')
def get_temperature():
    """Route to get the average temperature 
    from the last hour of all sensors in the given boxes."""
    box_ids_args = request.args.get("box_ids")
    if box_ids_args:
        ids = box_ids_args.split(",")
    else:
        ids = box_ids
    return average_temperature(ids)
