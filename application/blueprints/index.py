"""Blueprint for homepage."""

from flask import Blueprint, jsonify, url_for

index = Blueprint('index', __name__)

@index.route("/")
def home():
    """Return information about available API endpoints."""
    return jsonify({
        "available_endpoints": {
            "version": {
                "url": url_for("version.app_version"),
                "method": "GET",
                "description": "Get application version"
            },
            "metrics": {
                "url": url_for("prometheus_metrics"),
                "method": "GET",
                "description": "Prometheus metrics"
            },
            "temperature": {
                "url": url_for("temperature.get_temperature"),
                "method": "GET",
                "description": "Get temperature data (supports ?box_ids=id1,id2)",
                "params": {
                    "box_ids": "Comma-separated list of box IDs"
                }
            }
        }
    })
