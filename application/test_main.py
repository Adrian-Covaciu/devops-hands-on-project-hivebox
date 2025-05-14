"""File containing Unit tests for main.py functions."""

import re
from main import app

def test_temperature():
    """Test the /temperature endpoint."""
    with app.test_client() as client:
        response = client.get("/temperature")
        assert response.status_code == 200
        assert response.content_type == "application/json", f"Expected application/json, got {response.content_type}"

        data = response.get_json()
        temperature = data.get("average_temperature")
        assert isinstance(temperature, float), f"Expected float, got {type(temperature)}"

def test_version():
    """Test the /version endpoint."""
    with app.test_client() as client:
        response = client.get("/version")
        assert response.status_code == 200

        version_str = response.data.decode("utf-8")
        assert re.match(r"^\d+\.\d+\.\d+$", version_str), f"Invalid version format: {version_str}"
