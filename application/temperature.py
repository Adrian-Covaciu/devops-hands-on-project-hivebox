import requests
from datetime import datetime, timezone, timedelta

def average_temperature(box_ids):
    temp_sum = 0.0
    count = 0
    for sensor_id in box_ids:
        URL = f"https://api.opensensemap.org/boxes/{sensor_id}"
        r = requests.get(url=URL)
        data = r.json()
        sensors = data['sensors']
        for sensor in sensors:
            if sensor["title"] == "Temperatur":
                last_measurement = sensor["lastMeasurement"]["createdAt"]
                time_measured = datetime.strptime(last_measurement, "%Y-%m-%dT%H:%M:%S.%fZ")
                time_measured = time_measured.replace(tzinfo=timezone.utc)  # Make it timezone-aware (UTC)
                time_now = datetime.now(timezone.utc)
                if time_now - time_measured < timedelta(hours=1):
                    temp = float(sensor["lastMeasurement"]["value"])
                    print(f"Sensor ID: {sensor_id}, Temperature: {temp}")
                    temp_sum += temp
                    count += 1
    if count == 0:
        return None  # Avoid division by zero
    return temp_sum / count