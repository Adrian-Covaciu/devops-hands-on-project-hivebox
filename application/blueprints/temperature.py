"""Blueprint for temperature endpoint."""

from datetime import datetime, timezone, timedelta
import os
from flask import Blueprint
import requests

default_box_ids = [
    "5eba5fbad46fb8001b799786",
    "5c21ff8f919bf8001adf2488",
    "5ade1acf223bd80019a1011c",
]
box_ids = os.environ.get("BOX_IDS", ",".join(default_box_ids)).split(",")

def average_temperature(ids):
    """Function that calculates the average temperature 
    from the last hour of all sensors in the given boxes."""
    temp_sum = 0.0
    count = 0
    for sensor_id in ids:
        sensor_url = f"https://api.opensensemap.org/boxes/{sensor_id}"
        r = requests.get(url=sensor_url, timeout=10)
        data = r.json()
        sensors = data['sensors']
        for sensor in sensors:
            if sensor["title"] == "Temperatur":
                last_measurement = sensor["lastMeasurement"]["createdAt"]
                time_measured = datetime.strptime(last_measurement, "%Y-%m-%dT%H:%M:%S.%fZ")
                time_measured = time_measured.replace(tzinfo=timezone.utc)
                time_now = datetime.now(timezone.utc)
                if time_now - time_measured < timedelta(hours=1):
                    temp = float(sensor["lastMeasurement"]["value"])
                    print(f"Sensor ID: {sensor_id}, Temperature: {temp}")
                    temp_sum += temp
                    count += 1
    if count == 0:
        return None  # Avoid division by zero
    average = temp_sum / count
    status = status_temperature(average)
    return {"average_temperature": average, "status": status}

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
    return average_temperature(box_ids)
