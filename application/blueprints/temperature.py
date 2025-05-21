"""Blueprint for temperature endpoint."""

from datetime import datetime, timezone, timedelta
from flask import Blueprint
import requests
import os

box_ids = os.environ.get("BOX_IDS", "5eba5fbad46fb8001b799786,5c21ff8f919bf8001adf2488,5ade1acf223bd80019a1011c").split(",")

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

def status_temperature(temperature):
    """Function that returns the status of the temperature."""
    if temperature is None:
        return "No data available"
    elif temperature < 10:
        return "Too Cold"
    elif 11 <= temperature <= 36:
        return "Good"
    else:
        return "Too Hot"

temperature = Blueprint('temperature', __name__ )

@temperature.route('/temperature')
def get_temperature():
    """Route to get the average temperature 
    from the last hour of all sensors in the given boxes."""
    return average_temperature(box_ids)
